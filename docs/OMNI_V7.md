# Omni v7 candidate: tighter convergence on top of v6

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This is the candidate for the next engine (branch `v7-candidate`), not a completed benchmark claim. Main and the ongoing Azure and broad v6 campaign keep the frozen v6 engine (`OMNI_V6.json`). Results from the two versions are never pooled. v7 is v6 with five changes, each found from a v6 run's own files or from the governing rules themselves:

| # | Change | Where | What it tightens |
|---|---|---|---|
| 1 | CPU conveyance obeys the namespace quota | `omni_controller/quota.py`, `muscles.py` | no write Kubernetes would refuse |
| 2 | One processor conveyed once; no raise while a pod starts or a shared host runs near its top | `omni_controller/capacity.py`, `muscles.py` | the pod start wait |
| 3 | The verdict reads a trial in the reports' own words (GAIN, EVEN, LOSS) | `omnicompass/verdict.py` | the do-no-harm trigger |
| 4 | Every rule counts in seconds, not decisions | `omni_controller/controller.py` | the same behaviour at any decision period |
| 5 | The cloud's rule in one word, `--give-back-only` | `omni_controller/controller.py`, `deploy/install/omni-compass-cloud.yaml`, `scripts/kind_bench.sh` | the bill can only fall or stay |

## 1. Quota-aware conveyance

The original capacity run 38722001872 tried to raise a pod CPU limit while its namespace CPU quota was already full. The candidate reads each namespace's ResourceQuota CPU-limit hard/used values, obeys the stricter pending spec/status ceiling, and reserves each accepted increase across all target deployments in one conveyance pass. It does not increase or delete an operator quota. PriorityClass scope selectors are matched from pod metadata, without deployment or quota names hardwired into the governor. Unknown quota state, read failures and unsupported scopes preserve native limits for expansion; reductions remain possible. Decreases do not create spendable headroom until observed by Kubernetes.

Kubernetes admission remains authoritative. A concurrent rejected write is audited and does not become an invented conveyance gain. The node's existing CPU cushion, operator CPU floor, security hold, workload schedule and benchmark validity checks remain intact. The separate runner shutdown in the historical run has no established cause and is not claimed fixed by this actuator change.

## 2. One processor conveyed once

The v6 three-run KEDA table (`results/live/V6_KEDA_REQUESTS.md`) read the pod start wait, mean, +12.5%, +12.0% and +22.7% (EVEN on the three-run rule, LOSS in two single runs). The cause, from the 151 pod starts in its raw files: a start takes longer when the runner's processor is busier, in both arms alike (7.9 s against 8.1 s at 25 to 50% busy, 9.2 s against 9.9 s at 50 to 75%), and only the omni arm reached 75 to 100% busy (20 starts, 12.4 s). On kind every node is a container on one 4-core runner and reports all four cores as its own, so conveyance gave each of three serving pods 3,700m of that one processor. v7 counts a machine's processor once: where every node stands on one host (providerID `kind://`, the same test the replica room uses), the host is the machine, A its CPU once, Q every other pod's requests on all its nodes, P every serving pod on it. No limit is raised while that host is at or over 75% busy or its busy share cannot be read, and on any cluster no limit is raised on a machine where a pod is starting; lowering is never held back, and each hold is written to the audit (`"convey": "held"`). On separate machines the arithmetic is unchanged.

## 3. The verdict in words

The verdict (`omnicompass/verdict.py`) is the engine's do-no-harm trigger: before a knob may move one step further from native, the step runs as a trial and its cost per piece of work is compared with the cost at the reference. Through v6 the comparison was the two medians alone: the step was allowed if m[trial] ≤ m[ref] · (1 + tolerance). On noisy work a median wanders, so a step that truly cost more than the allowance was often allowed by chance.

v7 (`judge="interval"`, the default) reads the trial exactly as a report reads a row (`tools/readings.py`). On the logarithm of each piece of work's cost, so that a heavy tail does not decide it, the change is

d = mean ln c[trial] − mean ln c[ref],  with the 95% interval  d ± 1.96 · √(s²[ref] / n[ref] + s²[trial] / n[trial])  (Welch's standard error),

and with τ = ln(1 + tolerance) the allowance in the same units:

- the interval wholly above zero is a **LOSS**: the step is refused and undone, whatever the allowance says;
- wholly below zero is a **GAIN**; across zero is **EVEN**;
- while the interval's half-width exceeds τ, the evidence is wider than the allowance, and the trial measures on, up to three times `min_samples`, before it decides;
- a GAIN or EVEN step is allowed only if both estimates are inside the allowance: the median (v6's guard, kept) and d ≤ τ;
- a stepwise knob is read the same way against the costs first measured at native as well, so a run of small steps cannot add up past the allowance.

Every judgement writes its reading and its intervals to the audit (`"reading"`, `"interval_ln"`). `judge="median"` reproduces v6 exactly.

On noisy work (log-normal costs, σ = 0.25, a 2% allowance, 300 trials each, seeded):

| True cost of the step | Allowed through v6 (medians) | Allowed in v7 (in words) |
|---|---|---|
| +0% (free) | 63% | 60% |
| +1% | 56% | 50% |
| +2% (at the allowance) | 47% | 39% |
| +3% | 40% | 28% |
| +5% | 26% | 14% |

A step that costs more than the allowance is allowed about a third less often at +3% and about half as often at +5%; a free step is kept almost as often. A step whose cost is clearly higher reads LOSS and is refused. These are properties of the rule on modelled costs (class S), not benchmark results (`tests/test_verdict_interval.py`).

## 4. Every rule counts in seconds

Five of the governor's rules counted decisions: the clear time after a breach (3), the cruise wait (2), the strict window (5), the verdict's probe spacing (10), recheck (120) and trial length (20). At a decision every 60 seconds those are 3, 2, 5, 10, 120 and 20 minutes; at 15 seconds they would silently shrink fourfold, and a give-back trial's 20 decisions would last 5 minutes instead of 20. v7 states each rule in seconds (`--slo-clear-s 180`, `--cruise-after-s 120`, `--strict-window-s 300`, `--verdict-every-s 600`, `--verdict-recheck-s 7200`, `--verdict-trial-s 1200`) and converts it to decisions at the running period, n = max(1, round(seconds / period)). At 60 s every count is v6's; an explicit count (`--slo-clear`, `--cruise-after`, `--strict-window`, `--verdict-every`, `--verdict-recheck`) still wins.

Two moves are made rates in time as well: the compass moves the HPA target by the same amount a minute at any period (its step is scaled by period / 60, and coasting likewise), and a node pool gives back at most one machine a minute (`RELEASE_PERIOD_S = 60`), however often the governor decides.

The default decision period stays 60 seconds. The governor core (`omnicompass/core.py`) still advances its own state by one fixed step (`MACRO_DT = 0.1`) per decision; a faster default waits for that clock to be stated in seconds too and for a test that shows no LOSS (`CLAUDE.md`, "Faster, but only where it hurts nothing"). The fast checks already run every 5 s; native's pod autoscaler runs its own 15-second check untouched underneath.

## 5. The cloud's rule in one word

In a cloud Omni-Compass shows one thing: the same work as native for a smaller bill, never a bigger one. Through v6 that rule was assembled from several settings in the workflow (`OMNI_MACHINES_ONLY=1`, the dial at the tune-down, the sensed and capped deployments left empty). v7 makes it one flag, enforced in the governor itself: `--give-back-only` turns off every pod-, processor-, power-, clock-, cooling- and batch-actuator, sets the replica ceiling to 0 and the dial to the tune-down, and leaves the node pool as the only knob. Whatever else is passed, the governor can then only park a machine the cloud already made, after its own trial, and wake it on a breach: no more pods and no more machines than native. The Azure, Google and Amazon install file (`deploy/install/omni-compass-cloud.yaml`) and the machines-only branch of `scripts/kind_bench.sh` pass it.

## Validation

Five shared-host regressions pass (`tests/test_convey_shared_host.py`: the host counted once, a busy or unread host holds, a start holds while lowering proceeds, separate machines keep their own arithmetic, the start test reads the pod). Eight quota regressions pass; the original source fails both the full-quota regression and the admission-rejection regression. Existing conveyance integration checks pass unchanged. The verdict's rule tests (`tests/test_verdict_interval.py`, `tests/test_verdict.py`: v6's medians kept under `judge="median"`, a noiseless 1.5% rise refused against a 1% allowance under v7), the time-correct tests (`tests/test_time_correct.py`, `tests/test_cloud_cadence.py`) and the cloud tests (`tests/test_cloud_machines_only.py`) pass, as do every verdict user's tests (Redis, Kafka, pgbench, sysbench, YCSB, CPU power, GPU). Live GitHub trials on the v7 commit (KEDA's add-ons, Goldilocks, CruiseKube, capacity) repeats the original cap 1500m / repetition 4 / 1200-second-per-arm case at the original request rates. Its completion and measured result must be read from its artifact, with any LOSS retained. The trial cannot launch Azure, Google, Amazon or GPUs.

Reference: Kubernetes [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) and [in-place container resource resizing](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/). The CPU budget helper is included in both the engine and actuator fingerprints. README.md, LICENSE, NOTICE, DISCLOSURES.md, PATENTS.md and TRADEMARKS.md accompany the trial artifact.

© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
