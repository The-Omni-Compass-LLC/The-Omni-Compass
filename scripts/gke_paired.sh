#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a real, billed Google Kubernetes Engine cluster (.github/workflows/gke-metered.yml): every
# arm back to back, each on a fresh cluster built the same way, in an order rotated by repetition, the same design as
# scripts/aks_paired.sh on Azure and scripts/kind_paired.sh on kind. Each cluster:
#   system pool  1 machine, tainted CriticalAddonsOnly=true:NoSchedule (GKE's add-ons, which tolerate that taint, and the
#                load generator; never measured, never governed)
#   work pool    omni-role=work, agentpool=work0, starts at GKE_MAX_NODES machines, under Google's own cluster
#                autoscaler (min 1, max GKE_MAX_NODES, the optimize-utilization profile), which deletes a machine once
#                it is empty. Native: the autoscaler alone. Omni on top: the same autoscaler, with Omni-Compass idling the
#                machines it gives back, which the autoscaler then deletes
# The measuring is scripts/kind_bench.sh in its managed-cluster mode (PLATFORM=gke reads as the same cloud-neutral mode
# AKS uses: kubectl only, the probe through the cloud's load balancer, the load generator on the tainted system machine,
# the bill counted from every work machine that exists every 15 s by its agentpool label). Each cluster is deleted
# when its arm ends, before the next is made, so nothing keeps billing.
# Written to the same design as the AKS run and not yet run on Google Cloud: its first repetition is a shakedown, and
# any arm that fails its own checks is marked INVALID and never counted.
# Usage: REP=n ARMS="native compass omni" GCP_PROJECT=... [GCP_ZONE=us-central1-a GKE_MACHINE=e2-standard-2
#        GKE_MAX_NODES=4 RUN_ID=...] bash scripts/gke_paired.sh
set -euo pipefail
echo "Omni-Compass: evaluation and simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass omni}"
PROJECT="${GCP_PROJECT:?set GCP_PROJECT}"; ZONE="${GCP_ZONE:-us-central1-a}"; MACHINE="${GKE_MACHINE:-e2-standard-2}"
MAX="${GKE_MAX_NODES:-4}"; RUNID="${RUN_ID:-local}"
export AKS_MAX_NODES="$MAX" WORKER_SEL="omni-role=work"          # kind_bench.sh's managed-cluster mode reads these names
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, work pool $MACHINE x up to $MAX in $ZONE (project $PROJECT)"
# Pre-flight, before anything is built or billed: the machine type is offered in the zone, and the region's CPU quota
# has room for the system machine and the whole work pool. One refusal ends the repetition here, in a minute.
cpus=$(gcloud compute machine-types describe "$MACHINE" --zone "$ZONE" --project "$PROJECT" --format='value(guestCpus)' 2>/dev/null || true)
[ -n "$cpus" ] || { echo "pre-flight: $MACHINE is not offered in $ZONE: nothing built, nothing billed"; exit 2; }
region="${ZONE%-*}"
need=$(( (MAX + 1) * cpus ))
free=$(gcloud compute regions describe "$region" --project "$PROJECT" --format=json \
  | python3 -c "import json,sys; q=[x for x in json.load(sys.stdin).get('quotas', []) if x['metric']=='CPUS']; print(int(q[0]['limit']-q[0]['usage']) if q else 0)")
if [ "$free" -lt "$need" ]; then echo "pre-flight: needs $need vCPUs in $region, $free free: nothing built, nothing billed"; exit 2; fi
echo "pre-flight: $MACHINE ($cpus vCPU) x $(( MAX + 1 )) needs $need of $free free vCPUs in $region: ok"
gone() { gcloud container clusters delete "$1" --zone "$ZONE" --project "$PROJECT" --quiet >/dev/null 2>&1 || true; }
for arm in "${order[@]}"; do
  name=$(echo "omni-$arm-$REP-$RUNID" | tr '[:upper:]_' '[:lower:]-' | cut -c1-40)     # GKE: lowercase, at most 40 characters
  gone "$name"
  echo "######## creating $name"
  gcloud container clusters create "$name" --zone "$ZONE" --project "$PROJECT" \
    --num-nodes 1 --machine-type "$MACHINE" --node-taints CriticalAddonsOnly=true:NoSchedule --node-labels omni-role=system \
    --autoscaling-profile optimize-utilization --release-channel regular --quiet
  gcloud container node-pools create work0 --cluster "$name" --zone "$ZONE" --project "$PROJECT" \
    --machine-type "$MACHINE" --num-nodes "$MAX" --enable-autoscaling --min-nodes 1 --max-nodes "$MAX" \
    --node-labels omni-role=work,agentpool=work0 --quiet
  gcloud container clusters get-credentials "$name" --zone "$ZONE" --project "$PROJECT"
  kubectl wait --for=condition=Ready nodes --all --timeout=600s
  gcloud container clusters describe "$name" --zone "$ZONE" --project "$PROJECT" --format=json > "/tmp/gke-$name.json"
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"; cp "/tmp/gke-$name.json" "bench-$arm-$REP/gke_cluster.json"
  if ! PLATFORM=gke ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "bench-$arm-$REP/INVALID"; fail=1
  fi
  gone "$name"
done
exit "${fail:-0}"
