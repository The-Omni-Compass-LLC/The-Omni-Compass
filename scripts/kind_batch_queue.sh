#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
#
# The batch queue under a queueing system of its own (docs/BATCH_QUEUE_PREREGISTRATION.md; register rows 63 and 91):
# Kueue (Kubernetes SIG Scheduling, Apache-2.0), Volcano (the CNCF, Apache-2.0) or the KAI scheduler (NVIDIA, Apache-2.0)
# admits and places a stream of jobs, the same in every arm, installed from its own release on the fresh cluster of each
# arm before the arms are told apart. Native is the queueing system as its project ships it, on Kubernetes alone;
# Omni-Compass sits on top with its own levers and never writes the queueing system's objects.
#   PHASE=install  install it from its release (its SHA-256 pinned), every piece of it on the control plane (the measured
#                  workers carry only the work, as with every add-on), wait until it answers; (Kueue) the operator's
#                  queue: one ClusterQueue whose quota is the workers' allocatable CPU and memory, read live, and one
#                  LocalQueue; (Volcano, KAI) its default queues as shipped; the stream's image pulled onto every worker
#   PHASE=submit   the stream: BATCH_JOBS jobs of BATCH_COMPLETIONS pods, BATCH_PARALLELISM at a time, one every
#                  BATCH_EVERY_S seconds from the window's opening, each pod hashing BATCH_MB MB; batch_done.txt when the
#                  last job has succeeded
#   PHASE=end      every job's and every pod's times (jobs.json, pods.json) and the queueing system's own objects
#                  (batch_queue_end.json)
set -euo pipefail
OUT_DIR="${OUT_DIR:?}"
Q="${BATCH_QUEUE:?set BATCH_QUEUE=kueue, volcano or kai}"
KUEUE_VERSION="${KUEUE_VERSION:-v0.20.2}"       # released 15 October 2026
VOLCANO_VERSION="${VOLCANO_VERSION:-v1.16.0}"   # released 14 October 2026
KAI_VERSION="${KAI_VERSION:-v0.18.6}"           # released 15 October 2026 (its chart, oci://ghcr.io/kai-scheduler/...)
# each release file's SHA-256, pinned when this test was preregistered (a different version names its own)
KUEUE_SHA256="${KUEUE_SHA256:-1ab14ecd590575ac57f50fa4cbcf529766bc2c32ba974bda1614381281ec52b4}"     # manifests.yaml, v0.20.2
VOLCANO_SHA256="${VOLCANO_SHA256:-9aa62e15541f5e955d73353da9321ab233a2cbe0f8fbac4b4a4d38ba497303ee}" # volcano-development.yaml, v1.16.0
KAI_SHA256="${KAI_SHA256:-dff53248c4a044249a1f62ca8d35bd8dfc02719b99e302b35c69f946f4c5b7ff}"         # the chart archive, v0.18.6
JOBS="${BATCH_JOBS:-24}"; COMPLETIONS="${BATCH_COMPLETIONS:-10}"; PARALLELISM="${BATCH_PARALLELISM:-5}"
EVERY="${BATCH_EVERY_S:-30}"; MB="${BATCH_MB:-3000}"
case "$Q" in kueue) NS=kueue-system ;; volcano) NS=volcano-system ;; kai) NS=kai-scheduler ;;
  *) echo "BATCH_QUEUE must be kueue, volcano or kai (got $Q)"; exit 1 ;; esac

case "${PHASE:?set PHASE=install, submit or end}" in
install)
  W=$(mktemp -d)   # the release and its placed copy stay off the run's files (1 to 2 MB each); its SHA-256 is kept
  if [ "$Q" = kai ]; then
  # KAI's chart at its pinned version, its archive checked against the pinned SHA-256, installed by Helm with the chart's
  # own placement setting (deploy/kind/kai-values.yaml), which its operator applies to every component it runs; the
  # components stand once their number has held for half a minute and every one is available
  url="oci://ghcr.io/kai-scheduler/kai-scheduler/kai-scheduler"
  for t in 1 2 3; do
    helm pull "$url" --version "$KAI_VERSION" --destination "$W" > "$OUT_DIR/kai_chart_pull.log" 2>&1 && break
    [ "$t" = 3 ] && { echo "INVALID RUN: KAI's chart could not be fetched ($url $KAI_VERSION)"; cat "$OUT_DIR/kai_chart_pull.log"; exit 1; }; sleep 10
  done
  chart=$(ls "$W"/kai-scheduler-*.tgz | head -1)
  got=$(sha256sum "$chart" | cut -d' ' -f1)
  [ "$got" = "$KAI_SHA256" ] || { echo "INVALID RUN: KAI's chart is not the one pinned (sha256 $got, pinned $KAI_SHA256)"; exit 1; }
  helm install kai-scheduler "$chart" --namespace "$NS" --create-namespace -f deploy/kind/kai-values.yaml --wait --timeout 15m \
    > "$OUT_DIR/kai_helm.log" 2>&1 || { tail -40 "$OUT_DIR/kai_helm.log"; kubectl get pods -n "$NS" -o wide; exit 1; }
  last=-1; held=0
  for t in $(seq 1 90); do
    d=$(kubectl get deploy -n "$NS" -o json)
    n=$(echo "$d" | jq '.items | length')
    short=$(echo "$d" | jq '[.items[] | select((.status.availableReplicas // 0) < (.spec.replicas // 1))] | length')
    if [ "$n" = "$last" ] && [ "$short" = 0 ] && [ "$n" -ge 2 ]; then held=$((held + 1)); else held=0; fi
    last=$n
    [ "$held" -ge 3 ] && kubectl get queues.scheduling.run.ai default-queue -o name >/dev/null 2>&1 && break
    [ "$t" = 90 ] && { echo "INVALID RUN: KAI's components did not all stand within 15 minutes"; kubectl get deploy,pods -n "$NS" -o wide; exit 1; }
    sleep 10
  done
  # a deployment the chart's setting does not reach is placed on the control plane after install, as CruiseKube's are
  for dep in $(kubectl get deploy -n "$NS" -o json | jq -r '.items[] | select((.spec.template.spec.nodeSelector // {}) | has("node-role.kubernetes.io/control-plane") | not) | .metadata.name'); do
    kubectl patch -n "$NS" "deployment/$dep" --type=merge -p '{"spec":{"template":{"spec":{"nodeSelector":{"node-role.kubernetes.io/control-plane":""},"tolerations":[{"key":"node-role.kubernetes.io/control-plane","operator":"Exists","effect":"NoSchedule"}]}}}}' >/dev/null
    kubectl rollout status -n "$NS" "deployment/$dep" --timeout=300s >/dev/null
    echo "placed on the control plane after install: $dep" >> "$OUT_DIR/kai_placement.txt"
  done
  # every serving pod of KAI on the control plane (a pod a move replaced is given two minutes to finish on its worker; a
  # finished install hook and a node agent of a DaemonSet are recorded, the same in both arms)
  off() { kubectl get pods -n "$NS" -o json | jq -r --argjson term "$1" '[.items[]
      | select(.status.phase == "Running" or .status.phase == "Pending")
      | select(([.metadata.ownerReferences[]?.kind] | index("DaemonSet")) | not)
      | select($term or .metadata.deletionTimestamp == null)
      | select((.spec.nodeName // "") | test("control-plane") | not) | .metadata.name] | join(" ")'; }
  for _ in $(seq 1 24); do [ -z "$(off true)" ] && break; sleep 5; done
  away=$(off false)
  [ -z "$away" ] || { echo "INVALID RUN: KAI's pods on a measured worker: $away"; kubectl get pods -n "$NS" -o wide; exit 1; }
  kubectl get pods -n "$NS" -o wide >> "$OUT_DIR/kai_placement.txt"
  else
  # the project's own release file, fetched whole and checked against its pinned SHA-256; every Deployment and Job of the
  # queueing system is placed on the control plane before the file is applied (Volcano's certificate Job ships with no
  # placement and would otherwise run once on a measured worker), the file otherwise applied as shipped
  if [ "$Q" = kueue ]; then url="https://github.com/kubernetes-sigs/kueue/releases/download/${KUEUE_VERSION}/manifests.yaml"
  else url="https://raw.githubusercontent.com/volcano-sh/volcano/${VOLCANO_VERSION}/installer/volcano-development.yaml"; fi
  for t in 1 2 3; do
    curl -fsSL --retry 3 -o "$W/release.yaml" "$url" && break
    [ "$t" = 3 ] && { echo "INVALID RUN: $Q's release file could not be fetched ($url)"; exit 1; }; sleep 10
  done
  want="$VOLCANO_SHA256"; [ "$Q" = kueue ] && want="$KUEUE_SHA256"
  got=$(sha256sum "$W/release.yaml" | cut -d' ' -f1)
  [ "$got" = "$want" ] || { echo "INVALID RUN: $Q's release file is not the one pinned (sha256 $got, pinned $want)"; exit 1; }
  python3 - "$W/release.yaml" "$NS" > "$W/applied.yaml" <<'PY'
import sys, yaml
docs = [d for d in yaml.safe_load_all(open(sys.argv[1])) if d]
for d in docs:
    if d.get("kind") in ("Deployment", "Job", "DaemonSet", "StatefulSet") and d["metadata"].get("namespace") == sys.argv[2]:
        spec = d["spec"]["template"]["spec"]
        spec["nodeSelector"] = {**(spec.get("nodeSelector") or {}), "node-role.kubernetes.io/control-plane": ""}
        spec["tolerations"] = (spec.get("tolerations") or []) + [
            {"key": "node-role.kubernetes.io/control-plane", "operator": "Exists", "effect": "NoSchedule"}]
print(yaml.safe_dump_all(docs, sort_keys=False), end="")
PY
  for t in 1 2 3; do   # server-side: the custom resource definitions are larger than a client-side apply may annotate
    kubectl apply --server-side -f "$W/applied.yaml" >/dev/null && break
    [ "$t" = 3 ] && { echo "INVALID RUN: $Q could not be applied"; exit 1; }; sleep 10
  done
  kubectl wait -n "$NS" --for=condition=Available deploy --all --timeout=600s >/dev/null
  [ "$Q" = kueue ] || kubectl wait -n "$NS" --for=condition=complete job --all --timeout=600s >/dev/null
  away=$(kubectl get pods -n "$NS" -o json | jq '[.items[] | select(.spec.nodeName != null and (.spec.nodeName | test("control-plane") | not))] | length')
  [ "$away" = 0 ] || { echo "INVALID RUN: $away of $Q's pods are not on the control plane"; kubectl get pods -n "$NS" -o wide; exit 1; }
  fi
  if [ "$Q" = kueue ]; then
    # the operator's queue, as Kueue's own single-ClusterQueue setup writes it, its quota the workers' capacity read live;
    # the API version is the one the installed release serves first
    ver=$(kubectl get --raw /apis/kueue.x-k8s.io | jq -r '.preferredVersion.groupVersion')
    read -r cpu mem < <(kubectl get nodes -l '!node-role.kubernetes.io/control-plane' -o json | python3 -c '
import json, sys
def cpu(v): return float(v[:-1]) / 1000 if v.endswith("m") else float(v)
def mib(v):
    for s, f in (("Ki", 1 / 1024), ("Mi", 1), ("Gi", 1024), ("Ti", 1024 ** 2)):
        if v.endswith(s): return float(v[:-2]) * f
    return float(v) / 2 ** 20
n = json.load(sys.stdin)["items"]
c = sum(cpu(x["status"]["allocatable"]["cpu"]) for x in n)
m = int(sum(mib(x["status"]["allocatable"]["memory"]) for x in n))
print("%g %dMi" % (c, m))')
    for t in $(seq 1 20); do   # the webhook answers a little after its deployment is Available
      kubectl apply -f - >/dev/null 2>&1 <<EOF && break
apiVersion: ${ver}
kind: ResourceFlavor
metadata: {name: default-flavor}
---
apiVersion: ${ver}
kind: ClusterQueue
metadata: {name: omni-cluster-queue}
spec:
  namespaceSelector: {}
  resourceGroups:
    - coveredResources: ["cpu", "memory"]
      flavors:
        - name: default-flavor
          resources:
            - {name: cpu, nominalQuota: "${cpu}"}
            - {name: memory, nominalQuota: "${mem}"}
---
apiVersion: ${ver}
kind: LocalQueue
metadata: {namespace: default, name: omni-queue}
spec: {clusterQueue: omni-cluster-queue}
EOF
      [ "$t" = 20 ] && { echo "INVALID RUN: Kueue's queue objects were refused"; exit 1; }; sleep 6
    done
    echo "kueue ${KUEUE_VERSION} (${ver}); ClusterQueue quota cpu ${cpu}, memory ${mem}" > "$OUT_DIR/batch_queue.txt"
  elif [ "$Q" = kai ]; then
    echo "kai ${KAI_VERSION}; its chart's default queues as shipped ($(kubectl get queues.scheduling.run.ai -o jsonpath='{range .items[*]}{.metadata.name} {end}'))" > "$OUT_DIR/batch_queue.txt"
    kubectl get queues.scheduling.run.ai -o json > "$OUT_DIR/kai_queues.json"
  else
    for t in $(seq 1 20); do   # Volcano's own default queue, as shipped, made by its controllers once they run
      kubectl get queues.scheduling.volcano.sh default -o name >/dev/null 2>&1 && break
      [ "$t" = 20 ] && { echo "INVALID RUN: Volcano's default queue never appeared"; exit 1; }; sleep 6
    done
    echo "volcano ${VOLCANO_VERSION}; the default queue as shipped" > "$OUT_DIR/batch_queue.txt"
  fi
  echo "release $url sha256 $got (the pinned file)" >> "$OUT_DIR/batch_queue.txt"
  # the stream's image on every worker before the window, as the served image is (deploy/kind/prepull.yaml): a job's wait is
  # the queueing system's and the scheduler's, never a download on the one machine all kind nodes share
  kubectl apply -f - >/dev/null <<'EOF'
apiVersion: apps/v1
kind: DaemonSet
metadata: {name: rig-prepull-batch, namespace: kube-system, labels: {app: rig-prepull-batch}}
spec:
  selector: {matchLabels: {app: rig-prepull-batch}}
  template:
    metadata: {labels: {app: rig-prepull-batch}}
    spec:
      terminationGracePeriodSeconds: 0
      initContainers:
        - {name: stream, image: "busybox:1.36", command: ["true"], resources: {requests: {cpu: 1m, memory: 8Mi}}}
      containers:
        - {name: done, image: "registry.k8s.io/pause:3.10", resources: {requests: {cpu: 1m, memory: 4Mi}}}
EOF
  kubectl -n kube-system rollout status daemonset/rig-prepull-batch --timeout=300s >/dev/null \
    || { echo "INVALID RUN: the stream's image was not pulled onto every worker"; exit 1; }
  kubectl -n kube-system delete daemonset rig-prepull-batch --wait=true --timeout=120s >/dev/null
  kubectl -n kube-system wait --for=delete pod -l app=rig-prepull-batch --timeout=120s >/dev/null 2>&1 || true
  echo "busybox:1.36 pre-pulled on every worker" >> "$OUT_DIR/batch_queue.txt"
  kubectl get deploy -n "$NS" -o jsonpath='{range .items[*]}{.metadata.name}={.spec.template.spec.containers[0].image}{"\n"}{end}' >> "$OUT_DIR/batch_queue.txt"
  cat "$OUT_DIR/batch_queue.txt"
  ;;
submit)
  START=$(date -u +%s); label=""; podlabel=""; sched=""
  [ "$Q" = kueue ] && label="kueue.x-k8s.io/queue-name: omni-queue"
  [ "$Q" = volcano ] && sched="schedulerName: volcano"
  [ "$Q" = kai ] && { label="kai.scheduler/queue: default-queue"; podlabel="$label"; sched="schedulerName: kai-scheduler"; }
  for i in $(seq 1 "$JOBS"); do
    sed -e "s/JOB_NAME/omni-batch-$(printf %03d "$i")/" -e "s/BATCH_COMPLETIONS/${COMPLETIONS}/" -e "s/BATCH_PARALLELISM/${PARALLELISM}/" \
        -e "s/BATCH_MB/${MB}/" -e "s|POD_QUEUE_LABEL|${podlabel:-omni-stream: \"1\"}|" -e "s|QUEUE_LABEL|${label:-omni-stream: \"1\"}|" \
        -e "s|SCHEDULER_LINE|${sched:-terminationGracePeriodSeconds: 30}|" \
        deploy/kind/batch-stream-job.yaml > "$OUT_DIR/job.yaml"
    for t in 1 2 3 4 5 6; do kubectl apply -f "$OUT_DIR/job.yaml" --request-timeout=20s >/dev/null && break; sleep 5; done
    echo "$(date -u +%s) submitted omni-batch-$(printf %03d "$i")" >> "$OUT_DIR/batch_submit.log"
    [ "$i" = "$JOBS" ] || sleep "$EVERY"
  done
  # batch_done.txt once the last job has succeeded; the wait ends with the window (DURATION from its opening), so a stream
  # not done in the window leaves no time written and the scorer counts the window's end
  until [ "$(kubectl get jobs -l app=omni-batch-stream -o json --request-timeout=20s 2>/dev/null \
            | jq '[.items[] | select((.status.succeeded // 0) >= .spec.completions)] | length')" = "$JOBS" ]; do
    [ "$(date -u +%s)" -lt "$(( START + ${DURATION:?} ))" ] || exit 0; sleep 5
  done
  date -u +%s > "$OUT_DIR/batch_done.txt"
  ;;
end)
  kubectl get jobs -l app=omni-batch-stream -o json > "$OUT_DIR/jobs.json" 2>/dev/null || echo '{"items": []}' > "$OUT_DIR/jobs.json"
  kubectl get pods -l app=omni-batch-stream -o json > "$OUT_DIR/pods.json" 2>/dev/null || echo '{"items": []}' > "$OUT_DIR/pods.json"
  if [ "$Q" = kueue ]; then
    kubectl get clusterqueues,localqueues,workloads -A -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  elif [ "$Q" = kai ]; then
    kubectl get queues.scheduling.run.ai,podgroups.scheduling.run.ai -A -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  else
    kubectl get queues,podgroups -A -o json > "$OUT_DIR/batch_queue_end.json" 2>/dev/null || true
  fi
  ;;
*) echo "PHASE must be install, submit or end"; exit 1 ;;
esac

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
