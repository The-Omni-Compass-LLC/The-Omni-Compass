#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The whole GPU test on a rented NVIDIA machine, one command (docs/GPU_RUN_GUIDE.md, section C):
#
#   sudo bash scripts/gpu_rented_run.sh                       everything, in the order below
#   sudo STOP_AFTER_PROBE=1 bash scripts/gpu_rented_run.sh    only steps 1 and 2: the machine checked and the chip measured
#                                                             (about 10 minutes; nothing counts; the numbers come back)
#
# 1. checks the machine (NVIDIA GPU, root, PyTorch with CUDA, power management Enabled, the driver's library for the fast
#    write path: nvidia-ml-py, installed if missing), then the wire check (tools/gpu_wire_check.py: both of the card's
#    wires follow, read back and go home);
# 2. the card probe (tools/gpu_probe.py, about 5 minutes, never counted): idle power at each park level, how fast the
#    clock comes back to the top, what parking costs the first request after a rest, and each kind of work at each clock;
# 3. declares the envelope before any trial (docs/GPU_PREREGISTRATION.md, amendment 3);
# 4. smoke: 3 repetitions x 3 arms x 180 s (about 40 minutes). It checks the wiring on real hardware. It never counts;
# 5. real AI serving, first because it is what a buyer runs: a language model served by vLLM in its own environment,
#    5 repetitions x 3 arms x 300 s (the time to first token, the time per token, the energy), then the capacity test on
#    each arm (the most requests per second inside the response line at the same power), about 2.5 hours; if vLLM
#    cannot install or start, the stage says so and nothing else is affected (SKIP_LLM=1);
# 6. the preregistered confirmation, 10 repetitions x 3 arms x 600 s (about 6 hours), on the same committed code
#    (STOP_AFTER_SMOKE=1 stops after step 4), on the pinned compute-bound workload (matrix products);
# 7. the second preregistered confirmation, the same 10 x 3 x 600 s on AI token generation (the decode workload: every
#    weight streamed from memory once per pass, batch one), about 6 hours more (SKIP_DECODE=1 skips it);
# 8. an operator's power cap underneath (70% of the default limit): the cap alone vs the cap with Omni-Compass on top,
#    at the usual load and fully loaded, 5 repetitions each, 300 s per arm, about 3 hours (SKIP_CAP=1). On one card
#    running flat out the firmware already uses every watt the cap allows: expect no more work there (amendment 13);
# 9. the GPU fault drill, about 10 minutes (SKIP_DRILL=1); everything so far is then packed;
# 10. the whole stacks with this card inside (tools/run_hil.py): the six organisms at 1, 10, 100 and 1,000 copies with
#    the card inside, native and Omni, about 25 hours on one card (SKIP_HIL=1 skips it; on an 8-card machine
#    scripts/gpu_8card.sh runs the organisms side by side);
# 11. packs every result folder into one file to send back, and prints the label each table chose by rule.
# PRICE_PER_HOUR (the machine's price in dollars) prints what each stage costs before it starts.
set -euo pipefail
echo "Omni-Compass: evaluation and simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
cd "$(dirname "$0")/.."
SMI="${NVIDIA_SMI:-nvidia-smi}"; PY="${PYTHON:-python3}"; GPU="${GPU:-0}"
STAMP="${STAMP:-$(date -u +%Y%m%dT%H%M%SZ)}${CARD_TAG:+-$CARD_TAG}"   # CARD_TAG: one folder per card (scripts/gpu_8card.sh)
mkdir -p results/gpu

echo "== checking the machine"
[ "$(id -u)" = 0 ] || [ -n "${SIM:-}" ] || { echo "run with sudo: setting the power limit needs root"; exit 1; }
command -v "$SMI" >/dev/null || { echo "nvidia-smi not found: this machine has no NVIDIA driver"; exit 1; }
# one copy only: two copies on one card write the same power limit and every arm of both is invalid (amendment 4)
exec 9>"${LOCK:-/tmp/omni-gpu-bench${CARD_TAG:+-$CARD_TAG}.lock}"
flock -n 9 || { echo "another copy of this test is already running on this machine. Start it once only: wait for it to finish (or reboot the machine), then run this one command again."; exit 1; }
BUSY=$($SMI -i "$GPU" --query-compute-apps=pid,process_name --format=csv,noheader 2>/dev/null || true)
[ -z "$BUSY" ] || { echo "something else is using the GPU, so the test would not be measuring only itself:"; echo "$BUSY"; echo "stop it (or reboot the machine), then run this one command again."; exit 1; }
# every run starts from the card's own default limit, not from whatever an earlier or aborted run left behind
DEF=$($SMI -i "$GPU" --query-gpu=power.default_limit --format=csv,noheader,nounits | tr -d ' ')
[ -n "${SIM:-}" ] || $SMI -i "$GPU" -pl "${DEF%.*}" >/dev/null || { echo "cannot set the default power limit $DEF W"; exit 1; }
echo "power limit reset to the card's default: $DEF W"
[ -n "${SIM:-}" ] || $SMI -i "$GPU" -rgc >/dev/null 2>&1 || true
echo "clock range reset to the card's own"
$SMI -i "$GPU" --query-gpu=name,driver_version,power.limit,power.min_limit,power.management --format=csv,noheader
$PY -c "import torch, sys; sys.exit(0 if torch.cuda.is_available() else 1)" 2>/dev/null || [ -n "${SIM:-}" ] \
  || { echo "PyTorch with CUDA not found: pip install torch, or rent an image that has it"; exit 1; }
# run as root on a clone the login user owns, so git is told the directory is safe; unreadable git refuses the run
GITST=$(git -c safe.directory='*' status --porcelain -- omni_controller omnicompass tools scripts docs/GPU_PREREGISTRATION.md) \
  || { echo "git cannot read this clone: run from a fresh git clone of the repository"; exit 1; }
[ -z "$GITST" ] || { echo "the code has local changes: the confirmation runs only on committed code (git stash, or a fresh clone)"; exit 1; }
echo "code: commit $(git -c safe.directory='*' rev-parse --short HEAD), unchanged"

echo "== wire check (both wires follow, read back and go home; nothing runs if this fails)"
$PY tools/gpu_wire_check.py --gpu "$GPU" --smi "$SMI" | tee "results/gpu/wirecheck-$STAMP.txt"
[ "${PIPESTATUS[0]}" = 0 ] || { echo "WIRE CHECK FAILED: send results/gpu/wirecheck-$STAMP.txt back; nothing else was run."; exit 1; }

echo "== the fast write path (the driver's own library, nvidia-ml-py)"
$PY -c "import pynvml; pynvml.nvmlInit()" 2>/dev/null || $PY -m pip install -q nvidia-ml-py >/dev/null 2>&1 || true
if $PY -c "import pynvml; pynvml.nvmlInit()" 2>/dev/null; then echo "NVML ready: clock writes take milliseconds";
else echo "WARNING: NVML not available; the governor falls back to nvidia-smi (tens of ms a write), so its own trials will keep parking shallow"; fi

echo "== the card probe (about 5 minutes; measures the chip, never counts)"
set +e
$PY tools/gpu_probe.py --gpu "$GPU" --smi "$SMI" --out "results/gpu/probe-$STAMP" | tee "results/gpu/probe-$STAMP.log"
set -e
$SMI -i "$GPU" -rgc >/dev/null 2>&1 || true
if [ -n "${STOP_AFTER_PROBE:-}" ]; then
  tar czf "results/gpu/omni-gpu-$STAMP-probe.tar.gz" "results/gpu/probe-$STAMP" "results/gpu/wirecheck-$STAMP.txt"
  echo "== stopped after the probe, as asked. Send this file back: results/gpu/omni-gpu-$STAMP-probe.tar.gz"; exit 0
fi
price() { [ -n "${PRICE_PER_HOUR:-}" ] && python3 -c "print(f'about \${float(\"$1\")*float(\"$PRICE_PER_HOUR\"):.0f}')" || echo ""; }
echo "== the plan: smoke 0.7 h $(price 0.7); AI serving 2.5 h $(price 2.5); compute 6 h $(price 6); token generation 6 h $(price 6); operator cap 3 h $(price 3); drill 0.2 h; organisms 25 h $(price 25). Skip any with SKIP_LLM, SKIP_DECODE, SKIP_CAP, SKIP_HIL=1."

if [ -z "${ENVELOPE:-}" ]; then
  ENVELOPE="results/gpu/envelope-$STAMP.json"
  $PY tools/declare_envelope.py "$ENVELOPE" --gpu "$GPU" --smi "$SMI"
fi
export ENVELOPE

echo "== smoke (wiring check on real hardware; never counted)"
set +e
PHASE=smoke REPS="${SMOKE_REPS:-3}" DURATION="${SMOKE_DURATION:-180}" COOLDOWN="${SMOKE_COOLDOWN:-30}" \
  OUT="results/gpu/smoke-$STAMP" bash scripts/gpu_paired.sh
smoke_rc=$?
set -e
PACK=("results/gpu/smoke-$STAMP" "$ENVELOPE" "results/gpu/wirecheck-$STAMP.txt" "results/gpu/probe-$STAMP")
if [ "$smoke_rc" != 0 ]; then
  echo "SMOKE INVALID (exit $smoke_rc): the wiring needs a fix before any confirmation. Send the packed file back."
elif [ -n "${STOP_AFTER_SMOKE:-}" ]; then
  echo "smoke valid; stopping as asked (STOP_AFTER_SMOKE)."
else
  if [ -z "${SKIP_LLM:-}" ]; then
    echo "== real AI serving: a language model served by vLLM, the firmware alone vs with Omni-Compass on top, then capacity"
    set +e; OUT="results/gpu/run-$STAMP-llm" bash scripts/gpu_vllm.sh; set -e
    PACK+=("results/gpu/run-$STAMP-llm")
    tar czf "results/gpu/omni-gpu-$STAMP-llm.tar.gz" "${PACK[@]}"
    echo "== AI serving packed (send this now if you like): results/gpu/omni-gpu-$STAMP-llm.tar.gz"
  fi
  echo "== confirmation (preregistered: 10 repetitions, 600 s per arm, frozen code)"
  set +e
  PHASE=confirm OUT="results/gpu/run-$STAMP" bash scripts/gpu_paired.sh
  confirm_rc=$?
  set -e
  PACK+=("results/gpu/run-$STAMP")
  $PY -c "import json,sys; h=json.load(open(sys.argv[1])).get('headline',{}); print('RESULT, BY RULE (compute-bound):', h.get('verdict','(no verdict)'))" \
    "results/gpu/run-$STAMP/GPU_REPS.json" 2>/dev/null || echo "no table produced (exit $confirm_rc)"
  if [ -z "${SKIP_DECODE:-}" ]; then
    echo "== second confirmation: AI token generation (preregistered: 10 repetitions, 600 s per arm, frozen code)"
    set +e
    PHASE=confirm WORKLOAD_ARGS="--kind decode" OUT="results/gpu/run-$STAMP-decode" bash scripts/gpu_paired.sh
    decode_rc=$?
    set -e
    PACK+=("results/gpu/run-$STAMP-decode")
    $PY -c "import json,sys; h=json.load(open(sys.argv[1])).get('headline',{}); print('RESULT, BY RULE (AI token generation):', h.get('verdict','(no verdict)'))" \
      "results/gpu/run-$STAMP-decode/GPU_REPS.json" 2>/dev/null || echo "no table produced (exit $decode_rc)"
  fi
  tar czf "results/gpu/omni-gpu-$STAMP-confirmations.tar.gz" "${PACK[@]}"
  echo "== both confirmations packed (send this now if you like): results/gpu/omni-gpu-$STAMP-confirmations.tar.gz"
  # an operator's power cap underneath (the envelope's lowest watts, 70% of the default limit): the cap alone against
  # the cap with Omni-Compass on top, at the usual load and then fully loaded (more work from the same watts)
  CAP=$($PY -c "import json,sys; print(int(float(json.load(open(sys.argv[1]))['power_min_w'])))" "$ENVELOPE")
  if [ -z "${SKIP_CAP:-}" ]; then
    for kind in cap cap-full; do
      [ "$kind" = cap ] && WA="" || WA="--phases 1.3,1.3,1.3"
      echo "== an operator's power cap underneath ($CAP W): the cap alone vs the cap with Omni-Compass on top${WA:+, fully loaded (more work from the same watts)}"
      [ -n "${SIM:-}" ] || $SMI -i "$GPU" -pl "$CAP" >/dev/null
      set +e
      PHASE=confirm REPS_CONFIRM="${REPS_CAP:-5}" DURATION="${DURATION_CAP:-300}" WORKLOAD_ARGS="$WA" \
        OUT="results/gpu/run-$STAMP-$kind" bash scripts/gpu_paired.sh
      set -e
      [ -n "${SIM:-}" ] || $SMI -i "$GPU" -pl "${DEF%.*}" >/dev/null
      PACK+=("results/gpu/run-$STAMP-$kind")
    done
  fi
  if [ -z "${SKIP_DRILL:-}" ]; then
    echo "== the GPU fault drill: governor killed outright, the master switch pulled, the response feed blind"
    set +e; OUT="results/gpu/drill-$STAMP" bash scripts/gpu_fault_drill.sh; set -e
    PACK+=("results/gpu/drill-$STAMP")
  fi
  tar czf "results/gpu/omni-gpu-$STAMP-partial.tar.gz" "${PACK[@]}"
  echo "== everything so far packed: results/gpu/omni-gpu-$STAMP-partial.tar.gz"
  if [ -z "${SKIP_HIL:-}" ]; then
    echo "== the whole stacks with this card inside: six organisms at 1x, 10x, 100x and 1,000x copies, native and Omni (tools/run_hil.py)"
    set +e
    ENV_FLOOR_W=$($PY -c "import json,sys; print(json.load(open(sys.argv[1]))['power_min_w'])" "$ENVELOPE") \
      NVIDIA_SMI="$SMI" GPU="$GPU" $PY tools/run_hil.py --out "results/hil/run-$STAMP" | tee "results/gpu/hil-$STAMP.log" | grep -E "^== |^\| |^- "
    hil_rc=${PIPESTATUS[0]}
    set -e
    PACK+=("results/hil/run-$STAMP")
    echo "whole stacks: exit $hil_rc (0 valid, 2 a validity problem, see results/hil/run-$STAMP/HIL.md)"
  fi
fi
tar czf "results/gpu/omni-gpu-$STAMP.tar.gz" "${PACK[@]}"
echo "== send this one file back: results/gpu/omni-gpu-$STAMP.tar.gz"
