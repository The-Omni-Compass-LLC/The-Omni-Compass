# The 17 omni-v21 LOSS rows that had no cause written, read from their own files: 31 October 2026

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The LOSS ledger (`docs/LOSS_LEDGER.md`) carried 50 rows on omni-v21; 33 had their cause written from the data stores' own files (`docs/STORE_ROOT_CAUSES_2026-10-30.md`) and 17 had none. This page reads those 17 from the runs' own files on the branch `raw` (every run's folder named beside its table), with the repository's own tools: the pod start wait with `tools/pod_phases.py` (Kubernetes' pod watch and the host's processor record, every serving pod's start split into scheduling, the node side and the app's own probe, and placed by the host's busy share over its start and the node's state), and the governor's audit (`audit.jsonl`, every decision and every write with its reason) for the rest. Evidence class L, the real thing on one GitHub runner, where every kind node is a container on the one machine. Each cause is written into `tools/loss_ledger.py` and stands beside its row in the ledger. Nothing here moves a table; the rows stand as their tables read them. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The pod start wait: thirteen rows in eight tables

**The reading, the same in every table.** Omni-Compass's arm starts its pods while the one shared machine is busier, and starts more of them where it moves the autoscaler's target; native's arm starts fewer, at a quieter host. Each start's wait is the kubelet's own (the node side: pulling nothing, the image pre-pulled, but creating the container on a busy host) plus the app's readiness probe. The two-fold decomposition below (`tools/pod_phases.py`) splits the change in the mean wait into the shift of starts into other strata (a busier host, an empty node) and the wait in the same stratum. In six of the eight tables the whole rise, or more than it, is the shift: in the same stratum Omni-Compass's pods start as fast or faster (ALL_FOUR −0.02 s, KEDA on the CPU target −0.01 s, ROBUST_LONG −0.07 s, TRACE −0.11 s, GOLDILOCKS +0.03 s). In two it is partly the same stratum (FAIRNESS +0.19 s of +0.39 s; ROBUST_KILL +0.09 s of +0.25 s), read in section 4 and below. The **total** rows rise for a second reason: a total is the sum over starts, and Omni-Compass's arm starts more pods where its target moves (GOLDILOCKS 167 against 100; ROBUST_KILL 194 against 163; BATCH 22 against none), each start a wait that native never paid because it never started the pod.

**What it is, and what moves it.** The host's busy share is the test machine's: on GitHub's one runner every kind node, the load generator, the governor and the service share four cores, so a pod created while the machine is 70% to 100% busy waits longer at the kubelet than one created at 0% to 50%. On a real cluster each node is its own machine and this stratum does not exist. The founder's order of 13 October (a test machine's limit is never reported as Omni-Compass's result) and the finding of 18 October (`docs/POD_START_WAIT.md`, the same decomposition on KEDA's HTTP add-on) apply. The rows stand as LOSS by the key; the cause is the rig, and the one engine question in them is the count: whether a pod Omni-Compass started inside the window was needed. That is answered by the same tables' service rows (work inside the line and the response time, GAIN where the pods were added), and is on the next version's list as the pods-waiting rule's twin: a start on a host already at its top is a start the immune system may hold (omni-v21's hand-back on a waiting pod reads pending pods, not the host's busy share).

### ALL FOUR: `results/live/V21_ALL_FOUR.md`, runs 40227146512, 40250382783, 40272629580

The row: pod start wait, total (15.7%, 42.2%, 19.2% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 49 | 1.47 | 0.00 | 0.98 | 0.49 |
| native | 0.0 to 0.5 | already serving | 115 | 1.61 | 0.02 | 1.00 | 0.59 |
| omni | 0.0 to 0.5 | empty | 36 | 1.42 | 0.00 | 0.69 | 0.72 |
| omni | 0.0 to 0.5 | already serving | 38 | 1.55 | 0.00 | 1.00 | 0.55 |
| omni | 0.5 to 0.7 | already serving | 83 | 1.75 | 0.01 | 1.04 | 0.70 |
| omni | 0.7 to 1.0 | already serving | 41 | 1.68 | 0.05 | 0.98 | 0.66 |
Mean wait: native 1.57 s, omni 1.64 s, ΔW̄ = +0.07 s (+4.4%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.09 s; the wait in the same stratum: -0.02 s.

### BATCH: `results/live/V21_BATCH.md`, runs 40230821800, 40251625381, 40274018452

The row: pod start wait, total and mean (native 0; omni 0.9, 4 and 1.5 s total a repetition).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| omni | 0.0 to 0.5 | already serving | 17 | 1.29 | 0.00 | 0.76 | 0.53 |
| omni | 0.7 to 1.0 | empty | 5 | 8.40 | 0.00 | 6.20 | 2.20 |

### FAIRNESS: `results/live/V21_FAIRNESS.md`, runs 40227151053, 40250387280, 40272634568

The row: pod start wait, mean (4.9%, 10.1%, 51.0% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 43 | 1.30 | 0.00 | 0.77 | 0.53 |
| native | 0.0 to 0.5 | already serving | 97 | 1.48 | 0.00 | 0.82 | 0.66 |
| native | 0.5 to 0.7 | already serving | 15 | 1.67 | 0.00 | 1.00 | 0.67 |
| native | 0.7 to 1.0 | already serving | 6 | 2.50 | 0.00 | 2.00 | 0.50 |
| omni | 0.0 to 0.5 | empty | 30 | 1.57 | 0.00 | 0.97 | 0.60 |
| omni | 0.0 to 0.5 | already serving | 61 | 1.70 | 0.07 | 0.95 | 0.69 |
| omni | 0.5 to 0.7 | already serving | 10 | 1.60 | 0.00 | 1.00 | 0.60 |
| omni | 0.7 to 1.0 | already serving | 29 | 2.66 | 0.00 | 1.93 | 0.72 |
Mean wait: native 1.49 s, omni 1.88 s, ΔW̄ = +0.39 s (+25.9%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.19 s; the wait in the same stratum: +0.19 s.

### GOLDILOCKS: `results/live/V21_GOLDILOCKS.md`, runs 40222183655, 40245490699, 40267231266

The row: pod start wait, total (75.0%, 102.3%, 137.0% more) and mean (19.4%, 32.1%, 11.2% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | already serving | 100 | 1.37 | 0.00 | 0.85 | 0.52 |
| omni | 0.0 to 0.5 | already serving | 42 | 1.50 | 0.10 | 0.76 | 0.64 |
| omni | 0.5 to 0.7 | already serving | 86 | 1.71 | 0.05 | 1.20 | 0.47 |
| omni | 0.7 to 1.0 | already serving | 39 | 1.79 | 0.00 | 1.15 | 0.64 |
Mean wait: native 1.37 s, omni 1.68 s, ΔW̄ = +0.31 s (+22.4%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.27 s; the wait in the same stratum: +0.03 s.

### KEDA CPU REQUESTS: `results/live/V21_KEDA_CPU_REQUESTS.md`, runs 40232040937, 40254201062, 40276902708

The row: pod start wait, total (84.1%, 30.9%, 27.5% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 31 | 1.35 | 0.00 | 0.84 | 0.52 |
| native | 0.0 to 0.5 | already serving | 120 | 1.51 | 0.00 | 0.82 | 0.68 |
| omni | 0.0 to 0.5 | empty | 27 | 1.52 | 0.00 | 0.70 | 0.81 |
| omni | 0.0 to 0.5 | already serving | 105 | 1.45 | 0.00 | 0.79 | 0.66 |
| omni | 0.5 to 0.7 | already serving | 41 | 1.51 | 0.05 | 0.66 | 0.80 |
| omni | 0.7 to 1.0 | already serving | 37 | 1.84 | 0.00 | 1.11 | 0.73 |
Mean wait: native 1.48 s, omni 1.54 s, ΔW̄ = +0.06 s (+4.1%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.07 s; the wait in the same stratum: -0.01 s.

### ROBUST KILL: `results/live/V21_ROBUST_KILL.md`, runs 40240618830, 40261931876, 40286252440

The row: pod start wait, total (10.1%, 24.4%, 78.6% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 47 | 1.38 | 0.00 | 0.72 | 0.66 |
| native | 0.0 to 0.5 | already serving | 116 | 1.47 | 0.00 | 0.89 | 0.58 |
| omni | 0.0 to 0.5 | empty | 35 | 1.54 | 0.00 | 0.91 | 0.63 |
| omni | 0.0 to 0.5 | already serving | 94 | 1.59 | 0.01 | 0.94 | 0.64 |
| omni | 0.5 to 0.7 | already serving | 50 | 1.88 | 0.06 | 1.16 | 0.66 |
| omni | 0.7 to 1.0 | already serving | 15 | 2.07 | 0.00 | 1.33 | 0.73 |
Mean wait: native 1.44 s, omni 1.69 s, ΔW̄ = +0.25 s (+17.3%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.16 s; the wait in the same stratum: +0.09 s.

### ROBUST LONG: `results/live/V21_ROBUST_LONG.md`, runs 40240697625, 40261936964, 40286258686

The row: pod start wait, total (90.0%, 221.7%, 324.0% more) and mean (24.5%, 27.0%, 25.6% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 16 | 1.31 | 0.06 | 0.56 | 0.69 |
| native | 0.0 to 0.5 | already serving | 39 | 1.36 | 0.00 | 0.74 | 0.62 |
| native | 0.5 to 0.7 | already serving | 2 | 2.00 | 0.00 | 1.00 | 1.00 |
| omni | 0.0 to 0.5 | empty | 11 | 1.18 | 0.00 | 0.64 | 0.55 |
| omni | 0.0 to 0.5 | already serving | 38 | 1.37 | 0.00 | 0.87 | 0.50 |
| omni | 0.5 to 0.7 | already serving | 66 | 1.86 | 0.00 | 1.26 | 0.61 |
| omni | 0.7 to 1.0 | already serving | 26 | 1.88 | 0.00 | 1.42 | 0.46 |
Mean wait: native 1.37 s, omni 1.68 s, ΔW̄ = +0.31 s (+22.8%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.38 s; the wait in the same stratum: -0.07 s.

### TRACE GOOGLE2011: `results/live/V21_TRACE_GOOGLE2011.md`, runs 40232036723, 40252903510, 40275448206

The row: pod start wait, total (109.0%, 87.9%, 279.2% more).

| Arm | Host busy over the start | Node | Starts | Wait (s) | Scheduling (s) | Node side (s) | App and probe (s) |
|---|---|---|---:|---:|---:|---:|---:|
| native | 0.0 to 0.5 | empty | 44 | 1.61 | 0.00 | 1.00 | 0.61 |
| native | 0.0 to 0.5 | already serving | 131 | 1.55 | 0.01 | 0.89 | 0.66 |
| native | 0.5 to 0.7 | empty | 1 | 2.00 | 0.00 | 1.00 | 1.00 |
| native | 0.5 to 0.7 | already serving | 4 | 2.00 | 0.00 | 1.00 | 1.00 |
| omni | 0.0 to 0.5 | empty | 43 | 1.47 | 0.00 | 0.88 | 0.58 |
| omni | 0.0 to 0.5 | already serving | 167 | 1.47 | 0.01 | 0.89 | 0.56 |
| omni | 0.5 to 0.7 | already serving | 124 | 1.81 | 0.05 | 1.10 | 0.66 |
| omni | 0.7 to 1.0 | already serving | 78 | 2.18 | 0.09 | 1.41 | 0.68 |
Mean wait: native 1.58 s, omni 1.70 s, ΔW̄ = +0.13 s (+8.0%). Of it, the shift of starts into other strata (a busier host, an empty node): +0.23 s; the wait in the same stratum: -0.11 s.

## 2. CruiseKube: three rows, two arms that are one system

`results/live/V21_CRUISEKUBE.md`, runs 40220956277, 40245486755, 40267226299: the mean response time (0.9%, 1.4%, 2.4% slower), the 95th percentile (0.0%, 1.8%, 1.0%), the time over the response line (4.3% more in run A; 0 to 0 in B and C). In all 30 repetitions of the three runs the governor wrote nothing (`omni_writes.txt`: 0 in every repetition; the audit's decisions read "release permitted" and "node organ has no contraction authority"). By the preregistration (`docs/CRUISEKUBE_PREREGISTRATION.md`) Omni-Compass's muscles on this rig are the autoscaler's replica range, carried to KEDA's ScaledObject, the node pool and the rollout guard; the CPU limit is CruiseKube's alone (one knob, one writer) and the machines are kind's, fixed. The service stayed inside its line in every repetition (run A's 95th percentile 127.6 ms in both arms, 0.01% of samples over the line), so the range had nothing to carry, and the two arms ran the same system. The rows are the rig's noise between two native arms; no engine moves them. What would: more repetitions a run, to shrink the noise, or a load that takes the service to its line, where the range has work to do.

## 3. The batch queue: one request of 965, once in ten

`results/live/V21_BATCH.md`, failed requests (native 0; omni 0.01036%): one request failed in one arm of the thirty, repetition 6 of run 40230821800, at 20.1 s into the window, a 10 s timeout (`latency.csv`: 10,016.6 ms), while the web service stood at 4 replicas and a 670 ms mean response under the queue's load (`audit.jsonl`, the reflex readings at 15.7 s and 20.3 s). By then the governor had written only its records and the rollout pause (12.1 s and 14.1 s); no replica, limit or machine had moved. No other request failed in any arm of the three runs. A count that must never rise reads LOSS without a floor; its cause is one timeout under the queue's own load, not a move of the governor's. The batch table's pod start rows (section 1) are the 22 pods Omni-Compass's arm started inside the windows where native started none, 17 on serving nodes at 1.29 s each and 5 on an empty node while the host was 70% to 100% busy, at 8.40 s each.

## 4. The noisy neighbour: the second app's failed requests, and its pods' starts

`results/live/V21_FAIRNESS.md`, runs 40227151053, 40250387280, 40272634568: the second app's failed requests (1.1%, 1.1%, 3.7% more), and the pod start wait's mean (section 1). The rig (`scripts/kind_bench.sh`, `TWO_APP=1`, `deploy/kind/noisy.yaml`): php-apache, the governed service, and php-noisy, a neighbour with its own autoscaler (target 50%, 1 to 10 replicas) and its own surging load, on the same six workers; both deployments ask 200m and are limited to 500m a pod. Every write the governor made in run A's ten repetitions names php-apache: 312 conveyances (idle CPU on a worker given to its serving pod, 122 of them handed back "the shared host at its top"), its autoscaler target (to 75%, and to 30% on the SLO reflex), the rollout guard; none names php-noisy. Run A's means: the neighbour's 95th percentile 331.9 ms against 395.1 ms with Omni-Compass on top, its time over the line 15.68% against 16.15%, its failed requests 13.65% against 13.8%; the governed app's own failed requests fell (4.359% to 4.139%) and its alert minutes fell (9 to 8.6).

**The mechanism.** Conveyance reads a worker's idle CPU and gives it to the governed app's pod by raising its limit. The CPU is idle at that moment; when the neighbour's load surges, its pods find it taken until the hand-back, which comes at the shared host's top, not at the neighbour's line. The governor watches php-apache's response line and its own markers; the neighbour's line is not a marker it reads, so omni-v21's immune system, which hands a muscle back when its own markers turn against native, cannot see this harm. It is a harm at the organism (do no harm, `DISCLOSURES.md` section 3), small (the neighbour's failures up 1.1% to 3.7% of its own 13.7%) and real in all three runs. **The next version's work, through the model gate:** conveyance on a shared worker reads every other serving pod's response line where the rig publishes one, and hands back when a neighbour's line is threatened, as it hands back at the host's top today; and a conveyance is never larger than the worker's idle CPU less the other pods' requests (the neighbour's 200m a pod is what the scheduler promised it). The same stratum's +0.19 s on the neighbour's pod starts is the same CPU: a neighbour pod created on a worker whose idle CPU was conveyed away starts slower.

## 5. The fixed-capacity test at its top cap: 3 cores, the completed work

`results/live/V21_CAPACITY.md`, `3000:work` (0.6%, 1.1%, 0.2% less by the mean; run A's own interval −1.4% to +0.2%, across zero; its own table reads the row EVEN, no difference beyond the noise, as do runs B and C): at the 3-core cap the service completes 12,011 requests of 13,500 offered on native and 11,939 with Omni-Compass on top, with 0.0% against 0.1% failed and the 95th percentile 642 against 669 ms. The governor's writes at this cap (`capacity-run-40222187614/cap-3000-*/bench-compass-*/audit.jsonl`) are conveyances of idle CPU to the serving pods on each of the six workers (13 to 15 a worker over the five pairs), the operator's records, and the autoscaler target to 30% on the SLO reflex (five times). A conveyance adds a limit, never takes one; the completed count fell 0.6% by the mean with every run's interval across zero. The row reads LOSS by the mean of three runs none of which is beyond its noise: the rig's noise at the cap where the service is already inside its line. What decides it: the benchmark's three runs on the engine that stands, and more pairs a cap (five today).

## 6. What goes on the next version's list from this page

1. Conveyance on a shared worker that reads the neighbours' lines and leaves them their requests (section 4): omni-v23's candidate, the model gate first (a two-app model set from these runs' own files).
2. A pod start held while the host is at its top (section 1): the pods-waiting rule's twin, judged in the model on the organism's work and response before any run.
3. The rig: the host's busy share over each start recorded beside every pod start row on the receipts, so the stratum is read with the row (`tools/live_reps.py`), and the CruiseKube and capacity rigs given a load that reaches the service's line.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
