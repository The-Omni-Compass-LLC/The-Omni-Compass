#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a real, billed Azure Kubernetes Service cluster (.github/workflows/aks-metered.yml): every
# arm back to back, each on a fresh cluster built the same way, in an order rotated by repetition, the same as
# scripts/kind_paired.sh on kind. Each cluster:
#   system pool  1 machine, tainted CriticalAddonsOnly=true:NoSchedule (AKS's add-ons and the load generator; never
#                measured, never governed: kind's control plane)
#   work pool    agentpool=work, starts at AKS_MAX_NODES machines, under Azure's own cluster autoscaler (min 1, max
#                AKS_MAX_NODES), which deletes a machine once it is empty. Native: the autoscaler alone. Omni on top: the
#                same autoscaler, with Omni-Compass idling the machines it gives back, which the autoscaler then deletes
# The bill (scripts/kind_bench.sh, PLATFORM=aks) counts every work machine that exists, every 15 s. Each cluster is
# deleted when its arm ends, before the next is made, so nothing keeps billing and the subscription's core quota holds.
# Usage: REP=n ARMS="native compass omni" AZ_RG=... bash scripts/aks_paired.sh
set -euo pipefail
echo "Omni-Compass: evaluation and simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass omni}"
RG="${AZ_RG:?set AZ_RG}"; LOC="${AZ_LOCATION:-eastus}"; SIZE="${AKS_VM_SIZE:-Standard_D2s_v4}"
MAX="${AKS_MAX_NODES:-4}"
# The work pools: one or several, each its own machine family with its own ceiling ("size:max,size:max,..."). Several
# families are how a fleet gets past a subscription's per-family core allowance (10 vCPUs a family here, 200 in the
# region) and how real cloud fleets run anyway. Every pool carries the label omni-role=work (the worker selector), the
# first pool keeps one machine, the others may scale to zero; every pool starts full, Azure's autoscaler trims.
POOLS="${AKS_WORKER_POOLS:-$SIZE:$MAX}"
TOTAL=0; for p in ${POOLS//,/ }; do TOTAL=$(( TOTAL + ${p##*:} )); done
export AKS_MAX_NODES="$TOTAL" WORKER_SEL="omni-role=work"
PROFILE="${AKS_AUTOSCALER_PROFILE:-scale-down-unneeded-time=2m scale-down-delay-after-add=2m scan-interval=10s}"
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, work pools $POOLS (up to $TOTAL workers) in $LOC"
# Pre-flight, before anything is built or billed: every pool's size must be offered to this subscription in the region,
# and its machine family must have the vCPUs free (the per-family allowance, not the regional one, is what a fleet fails
# on; a family with no allowance at all reads "remaining 0" only once the cluster is half built). One refusal ends the
# repetition here, in a minute, instead of after ten minutes of cluster building.
az vm list-usage -l "$LOC" -o json > "/tmp/usage-$LOC.json"
bad=0
for p in ${POOLS//,/ }; do
  psize="${p%%:*}"; pmax="${p##*:}"
  fam=$(az vm list-skus -l "$LOC" --size "$psize" --resource-type virtualMachines -o tsv --query "[0].family" 2>/dev/null)
  restricted=$(az vm list-skus -l "$LOC" --size "$psize" --resource-type virtualMachines -o tsv --query "[0].restrictions[0].reasonCode" 2>/dev/null)
  vcpus=$(az vm list-skus -l "$LOC" --size "$psize" --resource-type virtualMachines -o tsv --query "[0].capabilities[?name=='vCPUs'].value | [0]" 2>/dev/null)
  if [ -z "$fam" ]; then echo "pre-flight: $psize is not offered in $LOC"; bad=1; continue; fi
  if [ -n "$restricted" ]; then echo "pre-flight: $psize is restricted in $LOC ($restricted)"; bad=1; continue; fi
  read -r used limit < <(python3 -c "import json,sys; u=[x for x in json.load(open(sys.argv[1])) if x['name']['value']==sys.argv[2]]; print(u[0]['currentValue'], u[0]['limit']) if u else print(0, 0)" "/tmp/usage-$LOC.json" "$fam")
  need=$(( pmax * ${vcpus:-2} )); [ "$psize" = "$SIZE" ] && need=$(( need + ${vcpus:-2} ))     # the system machine shares the first pool's family
  if [ $(( limit - used )) -lt "$need" ]; then echo "pre-flight: $psize ($fam) needs $need vCPUs, $(( limit - used )) free of $limit"; bad=1; else echo "pre-flight: $psize ($fam) $need of $(( limit - used )) free vCPUs: ok"; fi
done
[ "$bad" = 0 ] || { echo "pre-flight failed: nothing built, nothing billed"; exit 2; }
az group create -n "$RG" -l "$LOC" -o none
gone() { az aks delete -g "$RG" -n "$1" --yes -o none 2>/dev/null || true; }
for arm in "${order[@]}"; do
  name="omni-$arm-$REP"
  gone "$name"
  echo "######## creating $name"
  # shellcheck disable=SC2086
  # the control plane's tier (AKS_TIER): free, or standard (about $0.10 an hour a cluster, Azure's uptime SLA). Neither is in
  # the bill, which counts worker machines only; standard is the way past "creating a new cluster is unavailable at this
  # time in region", which Azure's free tier returned for hours on 2026-10-07 (docs/K8S_COMPASS_PREREGISTRATION.md, amendment 4)
  az aks create -g "$RG" -n "$name" -l "$LOC" --tier "${AKS_TIER:-free}" --node-count 1 --node-vm-size "$SIZE" \
    --nodepool-name system --nodepool-taints CriticalAddonsOnly=true:NoSchedule \
    --cluster-autoscaler-profile $PROFILE --generate-ssh-keys -o none
  i=0
  for p in ${POOLS//,/ }; do
    psize="${p%%:*}"; pmax="${p##*:}"; pmin=$([ "$i" = 0 ] && echo 1 || echo 0)
    az aks nodepool add -g "$RG" --cluster-name "$name" -n "work$i" --mode User --node-vm-size "$psize" --labels omni-role=work \
      --node-count "$pmax" --enable-cluster-autoscaler --min-count "$pmin" --max-count "$pmax" -o none   # AKS also labels its nodes agentpool=work$i
    i=$(( i + 1 ))
  done
  az aks get-credentials -g "$RG" -n "$name" --admin --overwrite-existing
  kubectl wait --for=condition=Ready nodes --all --timeout=600s
  az aks show -g "$RG" -n "$name" -o json > "/tmp/aks-$name.json"
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"; cp "/tmp/aks-$name.json" "bench-$arm-$REP/aks_cluster.json"
  if ! PLATFORM=aks ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "bench-$arm-$REP/INVALID"; fail=1
  fi
  gone "$name"
done
exit "${fail:-0}"
