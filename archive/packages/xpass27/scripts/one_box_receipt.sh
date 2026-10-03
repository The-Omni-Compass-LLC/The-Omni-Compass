#!/usr/bin/env bash
# One machine, one clock: Kubernetes and the NVIDIA card sampled together.
# Fails closed if either plant is missing. Does not claim the cluster sees the GPU
# unless a node allocatable nvidia.com/gpu is actually present.
set -u
OUT="${OUT:-one-box-out}"
SECONDS_N="${SECONDS_N:-60}"
INTERVAL="${INTERVAL:-5}"
mkdir -p "$OUT/samples"
restore() {
  if [ -n "${START_LIMIT:-}" ]; then
    nvidia-smi -pl "$START_LIMIT" >/dev/null 2>&1 || true
  fi
}
trap restore EXIT

if ! command -v nvidia-smi >/dev/null 2>&1; then
  echo "NO_CARD" | tee "$OUT/FAIL.txt"
  exit 2
fi
nvidia-smi --query-gpu=name,uuid,driver_version,power.limit,power.min_limit,power.max_limit,power.draw,clocks.sm,temperature.gpu,clocks_throttle_reasons.active --format=csv > "$OUT/gpu_identity.csv"
START_LIMIT="$(nvidia-smi --query-gpu=power.limit --format=csv,noheader,nounits | head -1 | awk '{print int($1)}')"
echo "$START_LIMIT" > "$OUT/start_limit_w.txt"

# A small enforced-limit probe. Restored on exit. If the driver refuses, record that and continue sampling.
MIN_LIMIT="$(nvidia-smi --query-gpu=power.min_limit --format=csv,noheader,nounits | head -1 | awk '{print int($1)}')"
PROBE=$(( START_LIMIT - 20 ))
if [ "$PROBE" -lt "$MIN_LIMIT" ]; then PROBE="$MIN_LIMIT"; fi
if nvidia-smi -pl "$PROBE" > "$OUT/power_write.txt" 2>&1; then
  echo probe_requested_w="$PROBE" | tee -a "$OUT/power_write.txt"
else
  echo "POWER_WRITE_REFUSED" | tee -a "$OUT/power_write.txt"
fi
nvidia-smi --query-gpu=power.limit,power.draw --format=csv,noheader > "$OUT/enforced_after_write.csv"

if ! command -v kind >/dev/null 2>&1; then
  curl -fsSL -o /tmp/kind https://kind.sigs.k8s.io/dl/v0.27.0/kind-linux-amd64 || { echo "KIND_DOWNLOAD_FAILED" | tee "$OUT/FAIL.txt"; exit 3; }
  chmod +x /tmp/kind
  sudo mv /tmp/kind /usr/local/bin/kind
fi
if ! command -v kubectl >/dev/null 2>&1; then
  curl -fsSL -o /tmp/kubectl "https://dl.k8s.io/release/$(curl -fsSL https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" || { echo "KUBECTL_DOWNLOAD_FAILED" | tee "$OUT/FAIL.txt"; exit 3; }
  chmod +x /tmp/kubectl
  sudo mv /tmp/kubectl /usr/local/bin/kubectl
fi
kind delete cluster --name onebox >/dev/null 2>&1 || true
kind create cluster --name onebox --wait 180s > "$OUT/kind_create.log" 2>&1 || { echo "KIND_CREATE_FAILED" | tee "$OUT/FAIL.txt"; exit 4; }
kubectl get nodes -o wide > "$OUT/nodes.txt"
kubectl apply -f - <<'YAML' > "$OUT/workload_apply.txt"
apiVersion: apps/v1
kind: Deployment
metadata: {name: onebox-load, namespace: default}
spec:
  replicas: 1
  selector: {matchLabels: {app: onebox-load}}
  template:
    metadata: {labels: {app: onebox-load}}
    spec:
      containers:
      - name: pause
        image: registry.k8s.io/pause:3.10
YAML
kubectl rollout status deployment/onebox-load --timeout=120s > "$OUT/rollout.txt" 2>&1 || true
ALLOC="$(kubectl get nodes -o jsonpath='{.items[0].status.allocatable.nvidia\.com/gpu}' 2>/dev/null || true)"
echo "${ALLOC:-0}" > "$OUT/allocatable_gpu.txt"

# RAPL, if this CPU exposes it. Absence is recorded, not invented.
if [ -r /sys/class/powercap/intel-rapl:0/energy_uj ]; then
  cat /sys/class/powercap/intel-rapl:0/energy_uj > "$OUT/rapl_start_uj.txt" || true
  ls /sys/class/powercap > "$OUT/rapl_zones.txt" || true
else
  echo "NO_RAPL" > "$OUT/rapl_zones.txt"
fi

python3 - << PY
import csv, json, subprocess, time, pathlib
out = pathlib.Path("$OUT")
n = int("$SECONDS_N")
step = int("$INTERVAL")
rows = []
t0 = time.time()
while time.time() - t0 < n:
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    gpu = subprocess.check_output(["nvidia-smi","--query-gpu=power.draw,power.limit,utilization.gpu,clocks.sm,temperature.gpu","--format=csv,noheader,nounits"], text=True).strip()
    pods = subprocess.check_output(["kubectl","get","pods","-l","app=onebox-load","--no-headers"], text=True).strip()
    rows.append({"t": ts, "gpu": gpu, "pods": pods})
    time.sleep(step)
(out/"samples.json").write_text(json.dumps(rows, indent=1))
print(f"samples {len(rows)}")
PY

if [ -r /sys/class/powercap/intel-rapl:0/energy_uj ]; then
  cat /sys/class/powercap/intel-rapl:0/energy_uj > "$OUT/rapl_end_uj.txt" || true
fi
restore
trap - EXIT
nvidia-smi --query-gpu=power.limit --format=csv,noheader > "$OUT/end_limit.txt"

python3 - << 'PY'
import json, pathlib, os
out = pathlib.Path(os.environ.get("OUT","one-box-out"))
alloc = (out/"allocatable_gpu.txt").read_text().strip() if (out/"allocatable_gpu.txt").exists() else "0"
start = (out/"start_limit_w.txt").read_text().strip()
end = (out/"end_limit.txt").read_text().strip().split()[0]
samples = json.loads((out/"samples.json").read_text())
receipt = {
  "plant": "one_machine",
  "card_present": True,
  "cluster_present": True,
  "cluster_sees_gpu": alloc not in ("", "0"),
  "allocatable_nvidia_gpu": alloc,
  "start_limit_w": start,
  "end_limit_w": end,
  "restored": end.startswith(start),
  "samples": len(samples),
  "rapl": (out/"rapl_zones.txt").read_text().strip() if (out/"rapl_zones.txt").exists() else "NO_RAPL",
  "claim": "same-clock host card plus kind cluster; GPU visible to pods only if allocatable_nvidia_gpu > 0",
}
(out/"ONE_BOX_RECEIPT.json").write_text(json.dumps(receipt, indent=1)+"\n")
print(json.dumps(receipt, indent=1))
PY
echo ONE_BOX_DONE
