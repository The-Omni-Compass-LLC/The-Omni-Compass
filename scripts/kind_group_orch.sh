#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The group's orchestrator and its stream (scripts/kind_group.sh; docs/GROUP_PREREGISTRATION.md). D is the arm's folder,
# N the members (kind clusters omni-m1 ... omni-mN, their kubeconfigs in D), ORCH karmada, ocm or none (the group alone).
#   PHASE=install  (karmada) Karmada as its own CLI installs it on a cluster of its own (omni-host), from its pinned release
#                  (karmadactl and the CRD archive checked against their pinned SHA-256), every member joined to it in push
#                  mode, and the operator's one propagation policy for the stream (deploy/kind/karmada-propagation.yaml);
#                  (ocm) Open Cluster Management's hub as its own CLI installs it on omni-host (clusteradm, checked against
#                  its pinned SHA-256, the pinned bundle), every member registered by clusteradm join and accepted on the
#                  hub, and the default cluster set bound to the namespace the placements live in
#   PHASE=submit   once every member's window is open: the batch rig's stream, BATCH_JOBS jobs one every BATCH_EVERY_S
#                  seconds (deploy/kind/batch-stream-job.yaml, as scripts/kind_batch_queue.sh writes it), each sent to the
#                  orchestrator (Karmada: the job to its API server; OCM: a Placement of its own, OCM's decision, then the
#                  job as a ManifestWork in the chosen member's namespace), or on the group alone to the members in turn;
#                  batch_done.txt once every job has succeeded
#   PHASE=end      the orchestrator's own record of every job (orch_jobs.json) and of where it placed each (orch_end.json)
# Credentials (Karmada's certificates, the members' kubeconfigs for it, OCM's bootstrap token) stay outside the run's files
# and are removed at the end.
set -euo pipefail
D="${D:?}"; N="${N:?}"; ORCH="${ORCH:?}"
KARMADA_VERSION="${KARMADA_VERSION:-v1.19.0}"   # released 31 August 2026
KARMADACTL_SHA256="${KARMADACTL_SHA256:-cf690eacc25ed13b6a27366c1b0b33e0e6edd2833e379922d420a5355550ef3d}"   # karmadactl-linux-amd64.tgz
KARMADA_CRDS_SHA256="${KARMADA_CRDS_SHA256:-e8d225a910924432f90d0e0397890d7d94b5a444b32e4586343570feeeafe100}" # crds.tar.gz
CLUSTERADM_VERSION="${CLUSTERADM_VERSION:-v1.4.0}"   # released 8 October 2026; its default bundle of OCM's components is 1.4.0
CLUSTERADM_SHA256="${CLUSTERADM_SHA256:-aa94241caf353a515a0778e0ce608b4c68ced9b3e7f6fb5fe23f48393926153b}"   # clusteradm_linux_amd64.tar.gz
OCM_BUNDLE="${OCM_BUNDLE:-1.4.0}"
JOBS="${BATCH_JOBS:-24}"; COMPLETIONS="${BATCH_COMPLETIONS:-10}"; PARALLELISM="${BATCH_PARALLELISM:-5}"
EVERY="${BATCH_EVERY_S:-30}"; MB="${BATCH_MB:-3000}"; DURATION="${DURATION:-1200}"
W="${RUNNER_TEMP:-/tmp}/omni-group-$(basename "$D")"   # Karmada's data and certificates, OCM's token: never in the run's files
KC="$W/data/karmada-apiserver.config"
HUB="$D/kubeconfig-host"                                   # the orchestrator's own cluster (removed with the run's kubeconfigs)
ip_of() { docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' "$1"; }
fetch() {   # url, file, sha256
  local t got
  for t in 1 2 3; do curl -fsSL --retry 5 --retry-delay 3 "$1" -o "$2" && break; sleep 10; done
  got=$(sha256sum "$2" | cut -d' ' -f1)
  [ "$got" = "$3" ] || { echo "INVALID RUN: $1 is not the pinned file (sha256 $got, pinned $3)"; exit 1; }
}
ocm_place() {   # NAME: a Placement of its own for this job, in the namespace the default cluster set is bound to, with OCM's
  # default prioritizers (Steady and Balance, the latter spreading the decisions among the clusters); once OCM has decided,
  # the job as a ManifestWork in the chosen member's namespace on the hub, which its work agent applies there
  local name="$1" cluster="" t
  kubectl --kubeconfig "$HUB" apply -f - >/dev/null <<EOF
apiVersion: cluster.open-cluster-management.io/v1beta1
kind: Placement
metadata: {name: $name, namespace: default, labels: {app: omni-batch-stream}}
spec:
  numberOfClusters: 1
  clusterSets: [default]
EOF
  for t in $(seq 1 60); do
    cluster=$(kubectl --kubeconfig "$HUB" -n default get placementdecisions -l "cluster.open-cluster-management.io/placement=$name" -o json 2>/dev/null \
      | jq -r '[.items[].status.decisions[]?.clusterName] | first // empty')
    [ -n "$cluster" ] && break
    sleep 2
  done
  [ -n "$cluster" ] || { echo "$(date -u +%s) $name: no placement decision in 120 s" >> "$D/batch_submit.log"; return 1; }
  python3 - "$D/job.yaml" "$name" "$cluster" <<'PY' | kubectl --kubeconfig "$HUB" apply -f - >/dev/null
import sys, yaml
job = yaml.safe_load(open(sys.argv[1]))
print(yaml.safe_dump({"apiVersion": "work.open-cluster-management.io/v1", "kind": "ManifestWork",
                      "metadata": {"name": sys.argv[2], "namespace": sys.argv[3], "labels": {"app": "omni-batch-stream"}},
                      "spec": {"workload": {"manifests": [job]}}}, sort_keys=False))
PY
  echo "$cluster" > "$D/ocm_decision_$name"
}
case "${PHASE:?set PHASE=install, submit or end}" in
install)
  case "$ORCH" in karmada|ocm) ;; *) echo "nothing to install for $ORCH"; exit 0 ;; esac
  rm -rf "$W"; mkdir -p "$W/bin"
  # the orchestrator's cluster on the cluster cores, as every member's nodes are; the governor's core stays its own
  ncpu=$(nproc)
  [ "$ncpu" -lt 2 ] || docker update --cpuset-cpus "0-$((ncpu - 2))" omni-host-control-plane >/dev/null
  host_ip=$(ip_of omni-host-control-plane)
  if [ "$ORCH" = ocm ]; then
    fetch "https://github.com/open-cluster-management-io/clusteradm/releases/download/${CLUSTERADM_VERSION}/clusteradm_linux_amd64.tar.gz" \
      "$W/clusteradm.tgz" "$CLUSTERADM_SHA256"
    tar -xzf "$W/clusteradm.tgz" -C "$W/bin" clusteradm
    # the hub (cluster manager) as clusteradm installs it, the components of the pinned bundle; the join command it hands
    # out holds the bootstrap token, kept outside the run's files
    "$W/bin/clusteradm" init --kubeconfig "$HUB" --bundle-version "$OCM_BUNDLE" --wait --output-join-command-file "$W/join.sh" \
      > "$D/ocm_init.log" 2>&1 || { tail -40 "$D/ocm_init.log"; exit 1; }
    token=$(grep -o -- '--hub-token [^ ]*' "$W/join.sh" | head -1 | cut -d' ' -f2 || true)
    [ -n "$token" ] || token=$("$W/bin/clusteradm" get token --kubeconfig "$HUB" 2>/dev/null | grep -o -- '--hub-token [^ ]*' | head -1 | cut -d' ' -f2 || true)
    [ -n "$token" ] || { echo "INVALID RUN: the hub handed out no bootstrap token"; exit 1; }
    # every member registered by clusteradm join (its klusterlet in its own namespaces, as OCM places it) by the address its
    # agents reach the hub at, then accepted on the hub; the arm waits until every member is Available
    for i in $(seq 1 "$N"); do
      for t in 1 2 3; do
        "$W/bin/clusteradm" join --kubeconfig "$D/kubeconfig-m$i" --hub-token "$token" --hub-apiserver "https://$host_ip:6443" \
          --cluster-name "omni-m$i" --bundle-version "$OCM_BUNDLE" --force-internal-endpoint-lookup --wait >> "$D/ocm_join.log" 2>&1 && break
        [ "$t" = 3 ] && { tail -20 "$D/ocm_join.log"; exit 1; }; sleep 10
      done
    done
    members=$(seq -s, -f 'omni-m%g' 1 "$N")
    for t in 1 2 3; do
      "$W/bin/clusteradm" accept --kubeconfig "$HUB" --clusters "$members" --wait >> "$D/ocm_accept.log" 2>&1 && break
      [ "$t" = 3 ] && { tail -20 "$D/ocm_accept.log"; exit 1; }; sleep 10
    done
    for t in $(seq 1 60); do
      ready=$(kubectl --kubeconfig "$HUB" get managedclusters -o json | jq '[.items[] | select(any(.status.conditions[]?; .type == "ManagedClusterConditionAvailable" and .status == "True"))] | length')
      [ "$ready" = "$N" ] && break
      [ "$t" = 60 ] && { echo "INVALID RUN: $ready of $N members Available in OCM"; kubectl --kubeconfig "$HUB" get managedclusters; exit 1; }
      sleep 5
    done
    # the default cluster set (every joined cluster is in it) bound to the namespace the placements live in
    kubectl --kubeconfig "$HUB" apply -f - >/dev/null <<EOF
apiVersion: cluster.open-cluster-management.io/v1beta2
kind: ManagedClusterSetBinding
metadata: {name: default, namespace: default}
spec: {clusterSet: default}
EOF
    {
      echo "orchestrator=ocm (Open Cluster Management) bundle $OCM_BUNDLE; clusteradm $CLUSTERADM_VERSION sha256=$CLUSTERADM_SHA256"
      echo "members: $(kubectl --kubeconfig "$HUB" get managedclusters -o jsonpath='{range .items[*]}{.metadata.name} {end}')"
      echo "placement: one Placement per job (numberOfClusters 1, cluster set default, OCM's default prioritizers Steady and Balance), the job as a ManifestWork in the member it decides"
      echo "images, with the digest each resolved to (the hub, then member omni-m1's agents):"
      kubectl --kubeconfig "$HUB" get pods -A -o json | jq -r '[.items[].status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
      kubectl --kubeconfig "$D/kubeconfig-m1" get pods -A -o json | jq -r '[.items[] | select(.metadata.namespace | startswith("open-cluster-management")) | .status.containerStatuses[]? | "  \(.image) \(.imageID)"] | unique[]'
    } | tee "$D/orch.txt"
    rm -f "$W/join.sh"
    exit 0
  fi
  rel="https://github.com/karmada-io/karmada/releases/download/${KARMADA_VERSION}"
  fetch "$rel/karmadactl-linux-amd64.tgz" "$W/karmadactl.tgz" "$KARMADACTL_SHA256"
  fetch "$rel/crds.tar.gz" "$W/crds.tar.gz" "$KARMADA_CRDS_SHA256"
  tar -xzf "$W/karmadactl.tgz" -C "$W/bin" karmadactl
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
    if [ "$ORCH" = ocm ]; then
      where="ocm, placed in a member of its choosing"
      ocm_place "$name" || ocm_place "$name" || echo "$(date -u +%s) $name was not placed by OCM" >> "$D/batch_submit.log"
      [ ! -s "$D/ocm_decision_$name" ] || where="ocm, placed in $(cat "$D/ocm_decision_$name")"
    else
      if [ "$ORCH" = none ]; then to="$D/kubeconfig-m$(( (i - 1) % N + 1 ))"; where="member $(( (i - 1) % N + 1 ))"; else to="$KC"; where="$ORCH"; fi
      for t in 1 2 3 4 5 6; do kubectl --kubeconfig "$to" apply -f "$D/job.yaml" --request-timeout=20s >/dev/null && break; sleep 5; done
    fi
    echo "$(date -u +%s) submitted $name to $where" >> "$D/batch_submit.log"
    [ "$i" = "$JOBS" ] || sleep "$EVERY"
  done
  done_jobs() {   # jobs that have succeeded: as Karmada reports them, or summed over the members (the group alone; OCM, whose
    # work agents run the jobs in the members)
    if [ "$ORCH" = karmada ]; then
      kubectl --kubeconfig "$KC" get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
        | jq '[.items[] | select(any(.status.conditions[]?; .type == "Complete" and .status == "True"))] | length' || echo 0
    else
      for i in $(seq 1 "$N"); do kubectl --kubeconfig "$D/kubeconfig-m$i" get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
        | jq '[.items[] | select((.status.succeeded // 0) >= .spec.completions)] | length' || echo 0; done | awk '{s+=$1} END {print s+0}'
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
  elif [ "$ORCH" = ocm ] && [ -s "$HUB" ]; then
    # every ManifestWork (the job as it was sent to OCM, named as the job) and every placement decision
    kubectl --kubeconfig "$HUB" get manifestworks -A -l app=omni-batch-stream -o json > "$D/orch_jobs.json" 2>/dev/null || echo '{"items": []}' > "$D/orch_jobs.json"
    kubectl --kubeconfig "$HUB" -n default get placementdecisions -o json 2>/dev/null \
      | jq '[.items[] | {job: .metadata.labels["cluster.open-cluster-management.io/placement"], clusters: [.status.decisions[]?.clusterName]}]' > "$D/orch_end.json" || true
    for dep in cluster-manager-placement-controller cluster-manager-registration-controller cluster-manager-work-webhook; do
      kubectl --kubeconfig "$HUB" -n open-cluster-management-hub logs "deployment/$dep" --tail=200 > "$D/$dep.log" 2>&1 || true
    done
    rm -f "$D"/ocm_decision_*
  fi
  rm -rf "$W"
  ;;
*) echo "PHASE must be install, submit or end"; exit 1 ;;
esac
# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
