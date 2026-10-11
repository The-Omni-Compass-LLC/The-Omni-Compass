#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One paired repetition on a real, billed Amazon Elastic Kubernetes Service cluster (.github/workflows/eks-metered.yml):
# every arm back to back, each on a fresh cluster built the same way, in an order rotated by repetition, the same design
# as scripts/aks_paired.sh on Azure and scripts/gke_paired.sh on Google Cloud. Each cluster (eksctl, managed node groups):
#   system group 1 machine, tainted CriticalAddonsOnly=true:NoSchedule (EKS's add-ons, the Kubernetes cluster
#                autoscaler, metrics-server and the load generator; never measured, never governed)
#   work group   omni-role=work, agentpool=work0, starts at EKS_MAX_NODES machines, under the Kubernetes cluster
#                autoscaler (EKS has none built in: the upstream one is installed with the same scale-down profile the
#                AKS run uses: 2 minutes unneeded, 2 minutes after an add, a scan every 10 s), which removes a machine
#                once it is empty. Native: the autoscaler alone. Omni on top: the same autoscaler, with Omni-Compass idling
#                the machines it gives back, which the autoscaler then removes
# The measuring is scripts/kind_bench.sh in its managed-cluster mode (PLATFORM=eks: kubectl only; Amazon's load balancer
# answers with a host name, which that mode reads when no address is given). Each cluster is deleted when its arm ends.
# Written to the same design as the AKS run and not yet run on Amazon: its first repetition is a shakedown, and any arm
# that fails its own checks is marked INVALID and never counted.
# Usage: REP=n ARMS="native compass omni" [AWS_REGION=us-east-1 EKS_INSTANCE=m5.large EKS_MAX_NODES=4 RUN_ID=...]
#        bash scripts/eks_paired.sh            (credentials from the environment: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
set -euo pipefail
echo "Omni-Compass: evaluation and simulation use only. Commercial use requires a signed, paid Omni-Compass Enterprise License (LICENSE, NOTICE)."
REP="${REP:?set REP}"; read -r -a arms <<< "${ARMS:-native compass omni}"
REGION="${AWS_REGION:-us-east-1}"; TYPE="${EKS_INSTANCE:-m5.large}"; MAX="${EKS_MAX_NODES:-4}"; RUNID="${RUN_ID:-local}"
K8S="${EKS_VERSION:-}"; MS_VERSION="${METRICS_SERVER_EKS:-v0.7.2}"   # EKS_VERSION empty: eksctl's default, a supported version
export AKS_MAX_NODES="$MAX" WORKER_SEL="omni-role=work"          # kind_bench.sh's managed-cluster mode reads these names
k=${#arms[@]}; off=$(( (REP - 1) % k ))
order=( "${arms[@]:off}" "${arms[@]:0:off}" )
echo "repetition $REP, order: ${order[*]}, work group $TYPE x up to $MAX in $REGION"
# Pre-flight, before anything is built or billed: the instance type is offered in the region, and the on-demand vCPU
# quota for standard instances (L-1216C47A) has room for the system machine and the whole work group.
vcpu=$(aws ec2 describe-instance-types --region "$REGION" --instance-types "$TYPE" \
  --query 'InstanceTypes[0].VCpuInfo.DefaultVCpus' --output text 2>/dev/null || true)
case "$vcpu" in ''|None) echo "pre-flight: $TYPE is not offered in $REGION: nothing built, nothing billed"; exit 2;; esac
quota=$(aws service-quotas get-service-quota --region "$REGION" --service-code ec2 --quota-code L-1216C47A \
  --query 'Quota.Value' --output text 2>/dev/null | cut -d. -f1)
need=$(( (MAX + 1) * vcpu ))
if [ -n "$quota" ] && [ "$quota" != None ] && [ "$quota" -lt "$need" ]; then
  echo "pre-flight: needs $need on-demand vCPUs in $REGION, quota $quota: nothing built, nothing billed"; exit 2
fi
echo "pre-flight: $TYPE ($vcpu vCPU) x $(( MAX + 1 )) needs $need vCPUs, quota ${quota:-unknown}: ok"
gone() { eksctl delete cluster --name "$1" --region "$REGION" --wait >/dev/null 2>&1 || true; }
for arm in "${order[@]}"; do
  name=$(echo "omni-$arm-$REP-$RUNID" | tr '[:upper:]_' '[:lower:]-' | cut -c1-60)
  gone "$name"
  echo "######## creating $name"
  cat > "/tmp/eks-$name.yaml" <<YAML
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata: {name: $name, region: $REGION${K8S:+, version: "$K8S"}}
iam:
  withOIDC: true
  serviceAccounts:
    - metadata: {name: cluster-autoscaler, namespace: kube-system}
      wellKnownPolicies: {autoScaler: true}
managedNodeGroups:
  - name: system
    instanceType: $TYPE
    desiredCapacity: 1
    minSize: 1
    maxSize: 1
    labels: {omni-role: system}
    taints: [{key: CriticalAddonsOnly, value: "true", effect: NoSchedule}]
  - name: work0
    instanceType: $TYPE
    desiredCapacity: $MAX
    minSize: 1
    maxSize: $MAX
    labels: {omni-role: work, agentpool: work0}
    tags: {"k8s.io/cluster-autoscaler/enabled": "true", "k8s.io/cluster-autoscaler/$name": "owned"}
YAML
  eksctl create cluster -f "/tmp/eks-$name.yaml"
  aws eks update-kubeconfig --name "$name" --region "$REGION"
  kubectl wait --for=condition=Ready nodes --all --timeout=900s
  # the Kubernetes cluster autoscaler (EKS ships none): auto-discovery by the work group's tags, AKS's scale-down profile,
  # on the system machine (it tolerates the taint)
  helm repo add autoscaler https://kubernetes.github.io/autoscaler >/dev/null 2>&1 || true
  helm repo update >/dev/null
  # the autoscaler release that matches the cluster's own Kubernetes minor version (one release per minor)
  minor=$(kubectl version -o json | python3 -c "import json,sys; print(json.load(sys.stdin)['serverVersion']['minor'].rstrip('+'))")
  helm upgrade --install cluster-autoscaler autoscaler/cluster-autoscaler ${CA_CHART_VERSION:+--version "$CA_CHART_VERSION"} -n kube-system \
    --set image.tag="v1.${minor}.0" \
    --set autoDiscovery.clusterName="$name" --set awsRegion="$REGION" \
    --set rbac.serviceAccount.create=false --set rbac.serviceAccount.name=cluster-autoscaler \
    --set extraArgs.scale-down-unneeded-time=2m --set extraArgs.scale-down-delay-after-add=2m --set extraArgs.scan-interval=10s \
    --set "tolerations[0].key=CriticalAddonsOnly" --set "tolerations[0].operator=Exists" \
    --set "nodeSelector.omni-role=system" --wait
  # metrics-server (EKS ships none; AKS and GKE do): the pinned release, on the system machine
  kubectl apply -f "https://github.com/kubernetes-sigs/metrics-server/releases/download/$MS_VERSION/components.yaml"
  kubectl -n kube-system patch deployment metrics-server --type=merge -p \
    '{"spec":{"template":{"spec":{"nodeSelector":{"omni-role":"system"},"tolerations":[{"key":"CriticalAddonsOnly","operator":"Exists","effect":"NoSchedule"}]}}}}'
  kubectl -n kube-system rollout status deployment/metrics-server --timeout=300s
  aws eks describe-cluster --name "$name" --region "$REGION" --output json > "/tmp/eks-$name.json"
  echo "######## ARM $arm (repetition $REP)"
  mkdir -p "bench-$arm-$REP"; cp "/tmp/eks-$name.json" "bench-$arm-$REP/eks_cluster.json"
  if ! PLATFORM=eks ARM="$arm" OUT_DIR="bench-$arm-$REP" bash scripts/kind_bench.sh; then
    echo "ARM $arm (repetition $REP) FAILED its checks: marked invalid" | tee "bench-$arm-$REP/INVALID"; fail=1
  fi
  gone "$name"
done
exit "${fail:-0}"
