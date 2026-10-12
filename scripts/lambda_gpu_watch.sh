#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# Watch one rented Lambda machine running an Omni-Compass GPU run (.github/workflows/lambda-gpu.yml), for at most
# MINUTES, and give it back the moment the run is over:
#   the run printed its last line ("send this one file back"): fetch every result file, give the machine back;
#   the hour budget plus one hour has passed (the deadline): fetch whatever results exist, give the machine back;
#   the machine is already gone: nothing to do.
# Writes the state (done, deadline, gone or watching) to OUT/state. The key never leaves the environment.
# Usage: bash scripts/lambda_gpu_watch.sh ID IP DEADLINE_EPOCH MINUTES OUT     (SSH_KEY: the private key file)
set -uo pipefail
echo "Omni-Compass: evaluation and simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
ID="$1"; IP="$2"; DEADLINE="$3"; MINUTES="$4"; OUT="$5"
EVERY="${EVERY:-600}"
mkdir -p "$OUT"
SSH=(ssh -i "${SSH_KEY:?set SSH_KEY}" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20 -o ServerAliveInterval=30 "ubuntu@$IP")
SCP=(scp -i "$SSH_KEY" -o StrictHostKeyChecking=accept-new -o ConnectTimeout=20)
give_back() { python3 scripts/lambda_gpu.py terminate "$ID" || python3 scripts/lambda_gpu.py terminate "$ID"; }
fetch() {   # every result file the run packed, its log, and the machine's own card list; partial if the run was cut
  "${SCP[@]}" "ubuntu@$IP:omni/results/gpu/omni-*.tar.gz" "$OUT/" 2>/dev/null || true
  "${SCP[@]}" "ubuntu@$IP:omni/run.log" "$OUT/run.log" 2>/dev/null || true
  "${SSH[@]}" "nvidia-smi --query-gpu=index,name,power.limit,power.default_limit --format=csv" > "$OUT/cards.csv" 2>/dev/null || true
  if ! ls "$OUT"/omni-*.tar.gz >/dev/null 2>&1; then
    "${SSH[@]}" "cd omni && tar czf /tmp/omni-partial.tar.gz results/gpu run.log 2>/dev/null; true" || true
    "${SCP[@]}" "ubuntu@$IP:/tmp/omni-partial.tar.gz" "$OUT/omni-partial.tar.gz" 2>/dev/null || true
  fi
  ( cd "$OUT" && sha256sum ./* > SHA256SUMS.txt 2>/dev/null ) || true
}
T_END=$(( $(date +%s) + MINUTES * 60 ))
while :; do
  st=$(python3 scripts/lambda_gpu.py status "$ID" 2>/dev/null | awk '{print $3}')
  if [ "$st" = terminated ]; then echo gone > "$OUT/state"; echo "machine $ID is already given back"; exit 0; fi
  if "${SSH[@]}" "grep -q 'send this one file back' omni/run.log" 2>/dev/null; then
    echo "the run is over: fetching the results"; fetch; give_back; echo done > "$OUT/state"; exit 0
  fi
  if [ "$(date +%s)" -ge "$DEADLINE" ]; then
    echo "the deadline has passed: fetching what exists and giving the machine back"; fetch; give_back
    echo deadline > "$OUT/state"; exit 0
  fi
  if [ "$(date +%s)" -ge "$T_END" ]; then echo watching > "$OUT/state"; echo "still running; the next watch carries on"; exit 0; fi
  "${SSH[@]}" "tail -n 2 omni/run.log" 2>/dev/null | sed 's/^/  run: /' || echo "  (no answer from the machine this time)"
  sleep "$EVERY"
done
