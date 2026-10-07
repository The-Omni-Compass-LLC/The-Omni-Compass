# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.

Source: GitHub Actions workflow `aks-metered`, run 37534538088, commit `f162ce8` (Omni v1, `tools/omni_version.py --commit f162ce8`), 2026-10-06/07, job `aggregate`, artifact `live-reps-aks`; raw files under `results/live/raw/run-37534538088/` (`aks-1` to `aks-5`). The burst sized to the cluster: the load generator's replicas stepping 1 3 1 4 1 3 over a 1,800 s window, eastus, `Standard_D2s_v4` workers (1 to 4) under Azure's own cluster autoscaler, a fresh cluster per arm, deleted after it; arms native and omni (Omni-Compass on top of native), order rotated, 5 repetitions dispatched: repetition 4 lost its native cluster to an Azure API error at cluster creation ("UnmarshalEntity encountered error: EOF") and is excluded as preregistered, so **4 paired repetitions** are read; repetition 4 is being run again and the table will be remade with 5 when it lands. Evidence class L, the bill metered (Azure's own count of machines every 15 s, priced at list). A single run read by `tools/live_reps.py`'s own paired interval; runs B and C to follow.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.908 | 1.945 |
| node-hours | 0.9578 | 0.977 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 185.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 183.3 |
| response time (ms), mean | 492.3 | 493.3 |
| response time (ms), 95th percentile | 1069 | 1138 |
| response time (ms), 99th percentile | 5886 | 4332 |
| time over the response line (% of samples) | 34.98 | 34.36 |
| failed requests (%) | 22.6 | 15.62 |
| pods with no machine to take them (unschedulable) | 2.5 | 1.8 |
| time pods had no machine to take them, pod-minutes | 3.538 | 2.43 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.717 | 3.493 |
| utilisation (used / allocatable) | 0.5885 | 0.5836 |
| CPU used (cores), mean | 2.133 | 2.156 |
| Omni's own CPU (cores), mean | 0 | 0.00912 |
| CPU used with Omni's own (cores), mean | 2.133 | 2.165 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 168.2 | 169.3 |
| HPA replicas, mean | 9.692 | 9.726 |
| pods started | 5.25 | 5 |
| pod start wait, total (s) | 248 | 175.8 |
| pod start wait, mean (s) | 48.82 | 35.16 |
| machines billed, machine-hours | 1.086 | 1.14 |
| compute bill at list price ($) | 0.1042 | 0.1095 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 4 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.908 | 1.956 | +2.5% | -0.05758 to +0.1526 | no |
| node-hours | 0.9578 | 0.9831 | +2.6% | -0.02439 to +0.0748 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 183.6 | 186.2 | +1.4% | -1.511 to +6.709 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 184.6 | +2.4% | -3.227 to +12 | no |
| response time (ms), mean | 492.3 | 491.2 | -0.2% | -124.4 to +122.2 | no |
| response time (ms), 95th percentile | 1069 | 1203 | +12.6% | -958.8 to +1227 | no |
| response time (ms), 99th percentile | 5886 | 3996 | -32.1% | -4304 to +523.4 | no |
| time over the response line (% of samples) | 34.98 | 33.85 | -3.2% | -5.076 to +2.826 | no |
| failed requests (%) | 22.6 | 13.87 | -38.6% | -24.49 to +7.04 | no |
| pods with no machine to take them (unschedulable) | 2.5 | 1.5 | -40.0% | -4.897 to +2.897 | no |
| time pods had no machine to take them, pod-minutes | 3.538 | 1.812 | -48.8% | -7.385 to +3.935 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.717 | 2.742 | -52.0% | -10.37 to +4.419 | no |
| utilisation (used / allocatable) | 0.5885 | 0.5807 | -1.3% | -0.02953 to +0.01396 | no |
| CPU used (cores), mean | 2.133 | 2.157 | +1.1% | -0.01659 to +0.06346 | no |
| Omni's own CPU (cores), mean | 0 | 0.00945 | +0.00945 (native is 0) | +0.006096 to +0.0128 | yes, more |
| CPU used with Omni's own (cores), mean | 2.133 | 2.166 | +1.5% | -0.009109 to +0.07489 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 168.2 | 170.2 | +1.2% | -2.759 to +6.713 | no |
| HPA replicas, mean | 9.692 | 9.718 | +0.3% | -0.04243 to +0.09577 | no |
| pods started | 5.25 | 5 | -4.8% | -1.046 to +0.5455 | no |
| pod start wait, total (s) | 248 | 136 | -45.2% | -485.9 to +261.9 | no |
| pod start wait, mean (s) | 48.82 | 27.2 | -44.3% | -98.41 to +55.18 | no |
| machines billed, machine-hours | 1.086 | 1.154 | +6.3% | -0.04231 to +0.179 | no |
| compute bill at list price ($) | 0.1042 | 0.1108 | +6.3% | -0.004062 to +0.01718 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*