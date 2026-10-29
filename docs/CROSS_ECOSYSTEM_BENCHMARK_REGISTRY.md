# Cross-ecosystem benchmark registry

Copyright 2026 The Omni-Compass LLC. Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.

Status: proposed experimental designs, not executed benchmarks. Vendor names denote target public technologies, not private access, endorsement or proven superiority.

| Ecosystem | Native baseline | Paired workload | Primary evidence |
|---|---|---|---|
| Microsoft Azure | AKS HPA / Cluster Autoscaler / KEDA, valid nonconflicting configuration | HTTP burst and message backlog | goodput, P95, pending time, node-hours, actual bill |
| Google | GKE Standard autoscaling; Autopilot separately | HTTP and batch bursts | completed work, P95, billed CPU/memory |
| Amazon AWS | EKS Karpenter / Cluster Autoscaler | heterogeneous node provisioning | scheduling delay, SLO, instance-hours |
| NVIDIA | vLLM or Dynamo serving stack when installed | matched inference prompts and token lengths | TTFT, ITL, request goodput, GPU energy |
| Meta | public PyTorch inference runtime | model-serving bursts | completed tokens, P95, joules |
| Cisco | authorized Intersight Workload Optimizer, or native VM controls separately | consolidation and workload surges | SLO, migration effects, total cost |
| xAI | authorized public API or open serving implementation | matched prompt stream | latency, tokens and API price; no inference about internal governor |
| Tesla | authorized lab CPU/GPU equipment | batch computation | work, deadline, energy, restoration |
| Oracle | OKE and OCI scaling | service burst | work, latency, node-hours |
| IBM / Red Hat | OpenShift autoscaling | event-driven queue | backlog age, completed work, cost |
| Databricks / Snowflake | supported warehouse/job scaling | query concurrency | successful queries, latency, credits |
| Cloudflare / Fastly | supported edge workload controls | traffic burst | completed requests, P95, billed usage |

Protocol: A=native with recommended settings; B=identical native plus Omni under supported authority; W=watch-only with no writes; C=Omni direct only where independently implemented and clearly labeled. Randomize paired arm order and freeze trace, hardware, model, software, quotas, and configuration. Do not intentionally cripple native. Never run two competing autoscalers against the same target.

Primary outcome is useful completed work under the same allowed capacity or total cost and declared SLO. Record raw work, P95, failures, energy, machines, money, and rollback. Distinguish exact equality, practical equivalence, and statistically inconclusive effects. Keep adverse metrics and missing runs. Declare every guardrail before data collection; stale telemetry or failed actuator read-back means no admission.

Each result needs engine/source SHA, paired inputs, hardware and cloud prices, per-repetition receipts, raw logs, independent meters where relevant, hashes, confidence intervals, and documented native controller interaction. A comparison to a public implementation is not a test of any vendor's private fleet. Hardware and paid cloud campaigns require a separately approved budget.

Use tools/paired_slo_goodput.py for its request-level schema. This registry is a roadmap, not a claim of successful physical tests.

References:
- https://learn.microsoft.com/en-us/azure/aks/concepts-scale
- https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview
- https://karpenter.sh/
- https://github.com/ai-dynamo/dynamo
- https://github.com/pytorch/pytorch
- https://developer.cisco.com/docs/intersight-workload-optimizer/
