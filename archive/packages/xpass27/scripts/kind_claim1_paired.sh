#!/usr/bin/env bash
# Current-brain live Kubernetes re-pair. Historical Set-22 is pre-canonical-evolve and must not be relabeled.
# Usage: REP=23 bash scripts/kind_claim1_paired.sh
set -euo pipefail
export OMNI_CLAIM_MODE="${OMNI_CLAIM_MODE:-CLAIM1}"
case "$OMNI_CLAIM_MODE" in CLAIM1|LIVE_GATE) ;; *) echo "OMNI_CLAIM_MODE must be CLAIM1 or LIVE_GATE"; exit 2;; esac
REP="${REP:-23}"
ARMS="${ARMS:-native watch omni}"
OUT_META="${OUT_META:-LIVE_REPS_${REP}_MODE.txt}"
{
 echo "rep=$REP"
 echo "arms=$ARMS"
 echo "claim_mode=$OMNI_CLAIM_MODE"
 echo "CLAIM1=current XPASS8+ canonical controlled evolve; LIVE_GATE=historical compatibility only"
 git rev-parse HEAD 2>/dev/null || true
} > "$OUT_META"
OMNI_CLAIM_MODE="$OMNI_CLAIM_MODE" REP="$REP" ARMS="$ARMS" bash scripts/kind_paired.sh

# Fail closed on provenance: the wrapper label is not evidence unless the Omni audit itself says CLAIM1.
OMNI_AUDIT="bench-omni-${REP}/audit.jsonl"
if [[ ! -s "$OMNI_AUDIT" ]]; then
  echo "INVALID RUN: missing Omni audit $OMNI_AUDIT" >&2
  exit 3
fi
python tools/verify_kind_claim_mode.py "$OMNI_AUDIT" --expected "$OMNI_CLAIM_MODE" > "bench-omni-${REP}/claim_mode_receipt.json"

# Cross-arm semantic validator: fail closed if any folder is mislabeled or if Watch executed a write.
python tools/validate_kind_e3_receipts.py --rep "$REP" --arms "$ARMS" --expected-mode "$OMNI_CLAIM_MODE" > "KIND_E3_REP_${REP}_VALIDATION.json"
