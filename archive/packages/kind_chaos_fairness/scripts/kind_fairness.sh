#!/usr/bin/env bash
# Two apps: victim (light) + noisy (heavy). Native HPA-only vs Omni on both HPAs.
# Records replica counts. Restore both HPA targets to 50.
set -euo pipefail
OUT_DIR="${OUT_DIR:-kind_fair_out}"; PHASE_S="${PHASE_S:-300}"; mkdir -p "$OUT_DIR"

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl -n kube-system patch deployment metrics-server --type=json \
  -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
kubectl -n kube-system rollout status deployment/metrics-server --timeout=300s
kubectl apply -f deploy/kind/two-app-fairness.yaml
kubectl rollout status deployment/php-victim --timeout=300s
kubectl rollout status deployment/php-noisy --timeout=300s
kubectl run load-victim --image=busybox:1.36 --restart=Never -- /bin/sh -c \
  "while true; do wget -q -O- http://php-victim >/dev/null; sleep 2; done" || true
kubectl run load-noisy --image=busybox:1.36 --restart=Never -- /bin/sh -c \
  "while true; do for i in \$(seq 1 40); do wget -q -O- http://php-noisy >/dev/null; done; sleep 1; done" || true
for i in $(seq 1 30); do kubectl top nodes >/dev/null 2>&1 && break; sleep 10; done

snap() {
  local tag=$1
  {
    echo "tag=$tag"
    kubectl get hpa php-victim php-noisy
    kubectl get deploy php-victim php-noisy
  } | tee "$OUT_DIR/snap_$tag.txt"
  kubectl get hpa php-victim -o jsonpath='{.status.desiredReplicas}' > "$OUT_DIR/victim_replicas_$tag.txt" || echo 0 > "$OUT_DIR/victim_replicas_$tag.txt"
  kubectl get hpa php-noisy -o jsonpath='{.status.desiredReplicas}' > "$OUT_DIR/noisy_replicas_$tag.txt" || echo 0 > "$OUT_DIR/noisy_replicas_$tag.txt"
}

echo "== Phase A native (HPA only)"
sleep "$PHASE_S"
snap native

echo "== Phase B Omni target (both HPAs if the controller walks all HPA objects)"
python -m omni_controller.controller --mode target --interval 30 --iterations $((PHASE_S / 30)) \
  --audit "$OUT_DIR/audit_omni.jsonl" --kill-file "$OUT_DIR/kill" &
OMNI_PID=$!
sleep "$PHASE_S"
kill "$OMNI_PID" 2>/dev/null || true
wait "$OMNI_PID" 2>/dev/null || true
snap omni

echo "== Restore"
touch "$OUT_DIR/kill"
python -m omni_controller.controller --mode target --iterations 1 \
  --audit "$OUT_DIR/audit_kill.jsonl" --kill-file "$OUT_DIR/kill"
v=$(kubectl get hpa php-victim -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}')
n=$(kubectl get hpa php-noisy -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}')
echo "restored victim=$v noisy=$n" | tee "$OUT_DIR/kill_switch.txt"
test "$v" = "50"
test "$n" = "50"

vrn=$(cat "$OUT_DIR/victim_replicas_native.txt" || echo 0)
vro=$(cat "$OUT_DIR/victim_replicas_omni.txt" || echo 0)
nrn=$(cat "$OUT_DIR/noisy_replicas_native.txt" || echo 0)
nro=$(cat "$OUT_DIR/noisy_replicas_omni.txt" || echo 0)
{
  echo "victim_replicas native=$vrn omni=$vro"
  echo "noisy_replicas native=$nrn omni=$nro"
  echo "observe_writes=$(grep -c '"write"' "$OUT_DIR/audit_omni.jsonl" || true) (live phase, writes expected)"
} | tee "$OUT_DIR/score.txt"
