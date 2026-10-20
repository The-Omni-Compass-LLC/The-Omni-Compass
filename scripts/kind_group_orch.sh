#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The group's orchestrator and its stream (scripts/kind_group.sh; docs/GROUP_PREREGISTRATION.md). D is the arm's folder,
# N the members (kind clusters omni-m1 ... omni-mN, their kubeconfigs in D), ORCH karmada or none (the group alone).
#   PHASE=install  (karmada) Karmada as its own CLI installs it on a cluster of its own (omni-host), from its pinned release
#                  (karmadactl and the CRD archive checked against their pinned SHA-256), every member joined to it in push
#                  mode, and the operator's one propagation policy for the stream (deploy/kind/karmada-propagation.yaml)
#   PHASE=submit   once every member's window is open: the batch rig's stream, BATCH_JOBS jobs one every BATCH_EVERY_S
#                  seconds (deploy/kind/batch-stream-job.yaml, as scripts/kind_batch_queue.sh writes it), each sent to the
#                  orchestrator, or on the group alone to the members in turn; batch_done.txt once every job has succeeded
#   PHASE=end      the orchestrator's own record of every job (orch_jobs.json) and of where it placed each (orch_end.json)
# Credentials (Karmada's certificates, the members' kubeconfigs for it) stay outside the run's files and are removed at the end.
set -euo pipefail
D="${D:?}"; N="${N:?}"; ORCH="${ORCH:?}"
KARMADA_VERSION="${KARMADA_VERSION:-v1.19.0}"   # released 31 August 2026
KARMADACTL_SHA256="${KARMADACTL_SHA256:-cf690eacc25ed13b6a27366c1b0b33e0e6edd2833e379922d420a5355550ef3d}"   # karmadactl-linux-amd64.tgz
KARMADA_CRDS_SHA256="${KARMADA_CRDS_SHA256:-e8d225a910924432f90d0e0397890d7d94b5a444b32e4586343570feeeafe100}" # crds.tar.gz
JOBS="${BATCH_JOBS:-24}"; COMPLETIONS="${BATCH_COMPLETIONS:-10}"; PARALLELISM="${BATCH_PARALLELISM:-5}"
EVERY="${BATCH_EVERY_S:-30}"; MB="${BATCH_MB:-3000}"; DURATION="${DURATION:-1200}"
W="${RUNNER_TEMP:-/tmp}/omni-group-$(basename "$D")"   # Karmada's data and certificates: never in the run's files
KC="$W/data/karmada-apiserver.config"
ip_of() { docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$1"; }
fetch() {   # url, file, sha256
  local t got
  for t in 1 2 3; do curl -fsSL --retry 5 --retry-delay 3 "$1" -o "$2" && break; sleep 10; done
  got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "INVALID RUN: $1 is not the pinned file (sha256 $got, pinned $3)"; exit 1; }
}
case "${PHASE:?set PHASE=install, submit or end}" in
install)
  [ "$ORCH" = karmada ] || { echo "nothing to install for $ORCH"; exit 0; }
  rm -rf "$W"; mkdir -p "$W/bin"
  rel="https://github.com/karmada-io/karmada/releases/download/${KARMADA_VERSION}"
  fetch "$rel/karmadactl-linux-amd64.tgz" "$W/karmadactl.tgz" "$KARMADACTL_SHA256"
  fetch "$rel/crds.tar.gz" "$W/crds.tar.gz" "$KARMADA_CRDS_SHA256"
  tar -xzf "$W/karmadactl.tgz" -C "$W/bin" karmadactl
  # the orchestrator's cluster on the cluster cores, as every member's nodes are; the governor's core stays its own
  ncpu=$(nproc)
  [ "$ncpu" -lt 2 ] || docker update --cpuset-cpus "0-$((ncpu - 2))" omni-host-control-plane >/dev/null
  host_ip=$(ip_of omni-host-control-plane)
  "$W/bin/karmadactl" init --kubeconfig "$D/kubeconfig-host" --karmada-data "$W/data" --karmada-pki "$W/pki" \
    --crds "$W/crds.tar.gz" --karmada-apiserver-advertise-address "$host_ip" --wait-component-ready-timeout 600 \
    > "$D/karmada_init.log" 2>&1 || { tail -40 "$D/karmada_init.log"; exit 1; }
  # every member joined in push mode by the address the orchestrator's pods reach it at (its control plane on the runner's
  # container network)
  for i in $(seq 1 "$N"); do
    ip=$(ip_of "omni-m$i-control-plane")
    kind get kubeconfig --internal --name "omni-m$i" | sed "s#https://omni-m$i-control-plane:6443#https://$ip:6443#" > "$W/m$i.kubeconfig"
    for t in 1 2 3; do
      "$W/bin/karmadactl" join "omni-m$i" --kubeconfig "$KC" --cluster-kubeconfig "$W/m$i.kubeconfig" >> "$D/karmada_join.log" 2>&1 && break
      [ "$t" = 3 ] && { tail -20 "$D/karmada_join.log"; exit 1; }; sleep 10
    done
  done
  for t in $(seq 1 60); do
    ready=$(kubectl --kubeconfig "$KC" get clusters -o json | jq '[.items[] | select(any(.status.conditions[]?; .type == "Ready" and .status == "True"))] | length')
    [ "$ready" = "$N" ] && break
    [ "$t" = 60 ] && { echo "INVALID RUN: $ready of $N members Ready in Karmada"; kubectl --kubeconfig "$KC" get clusters -o wide; exit 1; }
    sleep 5
  done
  members=$(seq -s, -f 'omni-m%g' 1 "$N")
  sed "s/MEMBER_CLUSTERS/[${members}]/" deploy/kind/karmada-propagation.yaml | kubectl --kubeconfig "$KC" apply -f - > /dev/null
  {
    echo "orchestrator=karmada $KARMADA_VERSION; karmadactl sha256=$KARMADACTL_SHA256; crds.tar.gz sha256=$KARMADA_CRDS_SHA256"
    echo "members: $(kubectl --kubeconfig "$KC" get clusters -o jsonpath='{range .items[*]}{.metadata.name} {end}')"
    echo "propagation policy: $(kubectl --kubeconfig "$KC" get propagationpolicy omni-batch-stream -o json | jq -c '.spec.placement')"
    echo "images, with the digest each resolved to:"
    kubectl --kubeconfig "$D/kubeconfig-host" get pods -A -o json | jq -r '[.items[].status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
  } | tee "$D/orch.txt"
  ;;
submit)
  for t in $(seq 1 480); do [ "$(find "$D/barrier" -name 'ready-*' | wc -l)" -ge "$N" ] && break; sleep 5; done
  [ "$(find "$D/barrier" -name 'ready-*' | wc -l)" -ge "$N" ] || { echo "the members' windows never opened"; exit 1; }
  START=$(date -u +%s); echo "$START" > "$D/stream_start.txt"
  for i in $(seq 1 "$JOBS"); do
    name="omni-batch-$(printf %03d "$i")"
    sed -e "s/JOB_NAME/$name/" -e "s/BATCH_COMPLETIONS/${COMPLETIONS}/" -e "s/BATCH_PARALLELISM/${PARALLELISM}/" \
        -e "s/BATCH_MB/${MB}/" -e 's|POD_QUEUE_LABEL|omni-stream: "1"|' -e 's|QUEUE_LABEL|omni-stream: "1"|' \
        -e "s|SCHEDULER_LINE|terminationGracePeriodSeconds: 30|" deploy/kind/batch-stream-job.yaml > "$D/job.yaml"
    if [ "$ORCH" = none ]; then to="$D/kubeconfig-m$(( (i - 1) % N + 1 ))"; where="member $(( (i - 1) % N + 1 ))"; else to="$KC"; where="$ORCH"; fi
    for t in 1 2 3 4 5 6; do kubectl --kubeconfig "$to" apply -f "$D/job.yaml" --request-timeout=20s >/dev/null && break; sleep 5; done
    echo "$(date -u +%s) submitted $name to $where" >> "$D/batch_submit.log"
    [ "$i" = "$JOBS" ] || sleep "$EVERY"
  done
  done_jobs() {   # jobs that have succeeded, as the orchestrator reports them, or summed over the members
    if [ "$ORCH" = none ]; then
      for i in $(seq 1 "$N"); do kubectl --kubeconfig "$D/kubeconfig-m$i" get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
        | jq '[.items[] | select((.status.succeeded // 0) >= .spec.completions)] | length' || echo 0; done | awk '{s+=$1} END {print s+0}'
    else
      kubectl --kubeconfig "$KC" get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
        | jq '[.items[] | select(any(.status.conditions[]?; .type == "Complete" and .status == "True"))] | length' || echo 0
    fi
  }
  until [ "$(done_jobs)" = "$JOBS" ]; do
    [ "$(date -u +%s)" -lt "$(( START + DURATION ))" ] || exit 0   # not done in the window: no time written, the window's end counts
    sleep 5
  done
  date -u +%s > "$D/batch_done.txt"
  ;;
end)
  if [ "$ORCH" = karmada ] && [ -s "$KC" ]; then
    kubectl --kubeconfig "$KC" get jobs -l app=omni-batch-stream -o json > "$D/orch_jobs.json" 2>/dev/null || echo '{"items": []}' > "$D/orch_jobs.json"
    kubectl --kubeconfig "$KC" get resourcebindings -A -o json 2>/dev/null \
      | jq '[.items[] | select(.spec.resource.kind == "Job") | {job: .spec.resource.name, clusters: .spec.clusters}]' > "$D/orch_end.json" || true
    for dep in karmada-scheduler karmada-controller-manager; do
      kubectl --kubeconfig "$D/kubeconfig-host" -n karmada-system logs "deployment/$dep" --tail=200 > "$D/$dep.log" 2>&1 || true
    done
  fi
  rm -rf "$W"
  ;;
*) echo "PHASE must be install, submit or end"; exit 1 ;;
esac
# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
