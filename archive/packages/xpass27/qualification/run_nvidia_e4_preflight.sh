#!/usr/bin/env bash
set -euo pipefail
OUT=${OUT:-results/xpass25_gpu}; mkdir -p "$OUT"
command -v nvidia-smi >/dev/null || { echo UNSUPPORTED_NO_NVIDIA_SMI; exit 3; }
nvidia-smi -L | tee "$OUT/gpu_identity.txt"
nvidia-smi --query-gpu=index,name,uuid,power.min_limit,power.max_limit,power.default_limit,power.limit,power.draw,temperature.gpu,utilization.gpu --format=csv,noheader,nounits | tee "$OUT/preflight.csv"
python3 - <<'PY2' "$OUT/preflight.csv" "$OUT/run_contract.json"
import csv,json,sys
r=next(csv.reader(open(sys.argv[1]))); json.dump({'evidence_class':'E4_CANDIDATE','physical_result':'NOT_YET_EXECUTED','gpu_index':r[0].strip(),'gpu_name':r[1].strip(),'gpu_uuid':r[2].strip(),'original_power_limit_W':r[6].strip(),'rule':'write only after explicit paired harness chooses a supported bounded cap; restore original and verify'},open(sys.argv[2],'w'),indent=2)
PY2
echo 'PREFLIGHT_PASS_WRITE_NOT_PERFORMED'
