#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Real AI serving on the card: a language model served by vLLM, the card's firmware alone against the firmware with
# Omni-Compass on top (scripts/gpu_paired.sh with tools/llm_workload.py as the workload). vLLM is installed in its own
# environment (it pins its own PyTorch), so nothing else on the machine changes. If it cannot be installed or started,
# the stage says so and exits without touching anything measured before it.
#
#   sudo OUT=results/gpu/run-STAMP-llm ENVELOPE=... bash scripts/gpu_vllm.sh
#   LLM_MODEL (default Qwen/Qwen2.5-0.5B-Instruct, open, no account needed), LLM_RATE (requests per second, default 4),
#   REPS_LLM (default 5), DURATION_LLM (default 300 s per arm); then the capacity test, CAP_REPS (default 2) per arm,
#   LLM_STEPS (requests per second, default 2,4,8,12,16,24,32,48,64), LLM_STEP_S (default 60 s); SKIP_CAPACITY=1 skips it
# Several cards: GPU=0,1,2,3,4,5,6,7 serves one model across them (vLLM tensor parallel, one Omni-Compass governor per
# card); LLM_MODEL then defaults to Qwen/Qwen2.5-7B-Instruct (open, no account needed).
# Your own serving engine: start it yourself (vLLM, TensorRT-LLM's trtllm-serve, SGLang, NVIDIA NIM, Triton's
# OpenAI-compatible frontend: anything that answers /v1/completions), then LLM_URL=http://host:port LLM_MODEL=<name>
# runs the same paired test against it; nothing is installed or started.
set -uo pipefail
cd "$(dirname "$0")/.."
OUT="${OUT:?set OUT}"; GPU="${GPU:-0}"
IFS=, read -r -a CARDS <<< "$GPU"; TP=${#CARDS[@]}
DEFMODEL=Qwen/Qwen2.5-0.5B-Instruct; [ "$TP" = 1 ] || DEFMODEL=Qwen/Qwen2.5-7B-Instruct
VENV="${VLLM_VENV:-/opt/omni-vllm}"; MODEL="${LLM_MODEL:-$DEFMODEL}"; PORT="${LLM_PORT:-8000}"
mkdir -p "$OUT"
if [ -n "${LLM_URL:-}" ]; then
  echo "== your own serving engine at $LLM_URL (model $MODEL): nothing installed or started"
  curl -sf "$LLM_URL/v1/models" >/dev/null 2>&1 || { echo "nothing answers at $LLM_URL/v1/models" | tee "$OUT/SKIPPED.txt"; exit 0; }
else
echo "== real AI serving: installing vLLM in its own environment ($VENV)"
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV" && "$VENV/bin/pip" install -q --upgrade pip && "$VENV/bin/pip" install -q vllm \
    || { echo "vLLM could not be installed on this machine; real AI serving skipped (nothing else is affected)" | tee "$OUT/SKIPPED.txt"; exit 0; }
fi
echo "== starting the model server: $MODEL"
CUDA_VISIBLE_DEVICES="$GPU" "$VENV/bin/python" -m vllm.entrypoints.openai.api_server --model "$MODEL" --port "$PORT" \
  --gpu-memory-utilization 0.80 --max-model-len 2048 --tensor-parallel-size "$TP" > "$OUT/vllm.log" 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null; wait $SRV 2>/dev/null' EXIT
for _ in $(seq 1 120); do
  curl -sf "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1 && break
  kill -0 "$SRV" 2>/dev/null || break
  sleep 5
done
curl -sf "http://127.0.0.1:$PORT/v1/models" >/dev/null 2>&1 \
  || { echo "the model server did not start; real AI serving skipped (see $OUT/vllm.log)" | tee "$OUT/SKIPPED.txt"; exit 0; }
LLM_URL="http://127.0.0.1:$PORT"
fi
export LLM_URL LLM_MODEL="$MODEL"
python3 tools/llm_workload.py calibrate --out "$OUT" > "$OUT/calibrate.log" 2>&1 \
  || { echo "calibration failed; real AI serving skipped" | tee "$OUT/SKIPPED.txt"; exit 0; }
SLO=$(python3 -c "import json; print(round(10*json.load(open('$OUT/calib.json'))['service_ms'],1))")
echo "one request at a time: $(python3 -c "import json; print(round(json.load(open('$OUT/calib.json'))['service_ms']))") ms; response line $SLO ms"
PHASE=confirm REPS_CONFIRM="${REPS_LLM:-5}" DURATION="${DURATION_LLM:-300}" SLO_MS="$SLO" GPU="$GPU" \
  WORKLOAD_CMD="python3 tools/llm_workload.py run" OUT="$OUT" bash scripts/gpu_paired.sh
paired_rc=$?

# The capacity test (amendment 13): the most work inside the response line at the same power. The request rate climbs
# step by step (tools/llm_workload.py capacity) until the 95th percentile passes the line; the last step inside it is the
# capacity. Native and Omni-Compass on top alternate, CAP_REPS times each, on the card's own start limit.
[ -n "${SKIP_CAPACITY:-}" ] && exit $paired_rc
SMI="${NVIDIA_SMI:-nvidia-smi}"; C="$OUT/capacity"; mkdir -p "$C"
for rep in $(seq 1 "${CAP_REPS:-2}"); do
  order="native omni"; [ $((rep % 2)) = 0 ] && order="omni native"
  for arm in $order; do
    D="$C/rep-$rep-$arm"; mkdir -p "$D"; rm -f "$D/kill"
    SIGS=""; for g in "${CARDS[@]}"; do SIGS="${SIGS:+$SIGS,}/tmp/omni-sig-$$-$g.sock"; done
    pids=()
    if [ "$arm" = omni ]; then
      for g in "${CARDS[@]}"; do
        python3 -m omni_controller.gpu_compass --mode cap --gpus "$g" --smi "$SMI" --signal "/tmp/omni-sig-$$-$g.sock" \
          --audit "$D/audit-$g.jsonl" --kill-file "$D/kill" > "$D/governor-$g.log" 2>&1 &
        pids+=($!)
      done
      sleep 2
    fi
    echo "== capacity, rep $rep, arm $arm"
    python3 tools/llm_workload.py capacity --out "$D" --slo-ms "$SLO" --signal "$SIGS" > "$D/capacity.log" 2>&1 || echo "capacity exited $?" >> "$D/capacity.log"
    touch "$D/kill"; for p in "${pids[@]}"; do wait "$p" 2>/dev/null; done
    for g in "${CARDS[@]}"; do $SMI -i "$g" -rgc >/dev/null 2>&1 || true; done
  done
done
python3 - "$C" <<'PYEOF'
import json, sys, glob, os
sys.path.insert(0, os.getcwd())
from tools.legal import stamp
c = sys.argv[1]; rows = {}
for f in sorted(glob.glob(os.path.join(c, "rep-*-*", "capacity.json"))):
    rep, arm = os.path.basename(os.path.dirname(f)).split("-")[1:3]
    rows.setdefault(arm, []).append(json.load(open(f)))
mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")
L = ["# Capacity inside the response line, the same power (amendment 13)", "",
     "| arm | repetitions | requests per second | tokens per second |", "|---|---:|---:|---:|"]
for arm in ("native", "omni"):
    r = rows.get(arm, [])
    L.append(f"| {arm} | {len(r)} | {mean([x['capacity_requests_per_s'] for x in r]):.2f} | {mean([x['capacity_tokens_per_s'] for x in r]):.0f} |")
n = mean([x["capacity_tokens_per_s"] for x in rows.get("native", [])]); o = mean([x["capacity_tokens_per_s"] for x in rows.get("omni", [])])
if n == n and o == o and n > 0:
    L += ["", f"Omni-Compass on top against the card alone: {o / n - 1:+.1%} tokens per second inside the line (two repetitions each: one reading; a confirmation needs the A, B and C runs)."]
open(os.path.join(c, "CAPACITY.md"), "w").write("\n".join(stamp(L)) + "\n"); print("\n".join(L))
PYEOF
exit $paired_rc
