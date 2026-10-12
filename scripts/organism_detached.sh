#!/bin/bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# The detached big-organism test on a rented machine (any cloud): every repetition of every organism in turn, native
# against native with Omni-Compass on top (scripts/kind_paired.sh: a fresh six-worker kind cluster per arm, the organism at
# the asked size with the real cluster inside), each cell's files moved into cells/<cell>/ when it ends, one .exit per
# cell, ALL_DONE at the end. The same test as big-organism-detached.yml's machine on Azure; .github/workflows/
# cloud-organism.yml runs it on Google Cloud or Amazon. TEST=robust runs the robustness long scenario instead
# (docs/ROBUSTNESS_PREREGISTRATION.md: ROBUST=long, the wandering schedule repeated to fill the window, no organism).
#   ORGS=tower,stack SCALE=1000 REPS=3 DUR=10800 TEST=organism bash scripts/organism_detached.sh
set -u
cd "$(dirname "$0")/.."
echo "Omni-Compass: evaluation and simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
ORGS="${ORGS:-stack}"; SCALE="${SCALE:-1000}"; REPS="${REPS:-3}"; DUR="${DUR:-10800}"; TEST="${TEST:-organism}"
export PATH="$PWD/.v/bin:$PATH" ARMS="${ARMS:-native compass}" DURATION="$DUR" ORGANISM_SCALE="$SCALE" LOAD_MAX="${LOAD_MAX:-6}" LOADGEN=open
export CLOSURE=tuning/GLOBAL_LEAGUE_PREREGISTRATION.json
mkdir -p cells
cell_end() {   # $1 cell, $2 rep, $3 exit code
  mkdir -p "cells/$1" && mv bench-*-"$2" "cells/$1/" 2>/dev/null; mv "paired-$1.log" "cells/$1/paired.log"
  echo "$3" > "cells/$1/paired.exit"; echo "$(date -u +%FT%TZ) end $1 exit $3"
}
if [ "$TEST" = robust ]; then
  w="1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1"; s=""
  for i in $(seq 1 $((DUR / 900))); do s="$s $w"; done
  export ROBUST=long LOAD_STEPS_IN="${s# }"
  for rep in $(seq 1 "$REPS"); do
    cell="robust-long-x$DUR-$rep"; echo "$(date -u +%FT%TZ) start $cell"
    REP=$rep bash scripts/kind_paired.sh > "paired-$cell.log" 2>&1; cell_end "$cell" "$rep" $?
  done
else
  for rep in $(seq 1 "$REPS"); do for org in $(echo "$ORGS" | tr , ' '); do
    cell="six-$org-x$SCALE-$rep"; echo "$(date -u +%FT%TZ) start $cell"
    ORGANISM=$org REP=$rep bash scripts/kind_paired.sh > "paired-$cell.log" 2>&1; cell_end "$cell" "$rep" $?
  done; done
fi
touch ALL_DONE
echo "$(date -u +%FT%TZ) all done"
