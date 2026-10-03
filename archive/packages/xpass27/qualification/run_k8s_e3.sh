#!/usr/bin/env bash
set -euo pipefail
MODE=${1:-preflight}; OUT=${OUT:-results/xpass25_live}; mkdir -p "$OUT"
case "$MODE" in
 preflight) kubectl version -o json > "$OUT/kubectl_version.json"; kubectl get nodes -o json > "$OUT/nodes.json";;
 watch) kubectl get deploy -A -o json > "$OUT/deploy_before.json"; sleep 5; kubectl get deploy -A -o json > "$OUT/deploy_after.json";;
 *) echo "Use repository-specific paired harness after preflight; no generic destructive write is issued by this wrapper."; exit 2;;
esac
