# Preregistration: the compass law on real Kubernetes (set 26)

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Written and committed before the run. The run's commit is the one that carries this file; nothing in the law, the
harness or this rule changes after it starts.

## What is run

Workflow `benchmark-reps` on `main`, 10 repetitions. Each repetition runs three arms back to back on the same runner,
each on a fresh six-worker kind cluster, in an order rotated by repetition (`scripts/kind_paired.sh`):

| Arm | What governs |
|---|---|
| native | Kubernetes alone (HPA at target 50, scheduler); Omni-Compass not started |
| omni | Omni-Compass on top with the engine's allocation law (`--law governor`, the law of sets 22 to 25) |
| compass | Omni-Compass on top with the compass law (`--law compass`, `omni_controller/controller.py`) |

Load: fixed rate (`loadgen=open`), the same work in every arm. 900 measured seconds per arm. SLO 500 ms at the 95th
percentile. Every Omni arm runs the six-state engine on every decision, the nervous system's authority and release
gate, the shield, the compass, and ends with the reset, which must return the HPA target, its replica range,
the pods' CPU limits and every worker to native, with no record left (`scripts/kind_bench.sh`).

## The compass law in the live controller

The service position is the 95th-percentile response time over the SLO (0 calm, 1 the line); a blind probe or a pod
waiting for a place reads as past the wall. The force is `A tanh((K_P (p - 0.5) + K_D v) / A)` with K_D for critical
damping times the realm push factor 3, the same law and gains as on every realm muscle (`realms/compass_arm.py`):
up gain 0.10, down gain 0.02, release threshold -0.2. Two levers:

1. **HPA target**, cover from 60% of the operator's target to the operator's own: the up force lowers it (more pods),
   the down force returns it toward the operator's. It is never tighter than native.
2. **Node pool**: past the 0.95 wall one machine more at once; one machine back only while the force is below -0.2,
   the position is below the center, and the nervous system's release gate is open.

## Outcomes and the rule

Primary: **worker nodes in service** (mean) and **95th-percentile response time**, each arm against native, paired
over the 10 repetitions with a t-based 95% interval (`tools/live_reps.py`).

Band first: the compass arm is a win only if its p95 is not worse than native's (the upper end of the 95% interval of the
paired difference at or under 0) **and** failed requests are not higher. If that holds and machines in service fall
with an interval wholly below 0, the label is **better on machines within the band**. If machines fall but the band
condition fails, the label is **tradeoff**. Otherwise **not established**.

Secondary, reported, not used for the label: p99, mean response time, HPA replicas, pods started, pod start wait, CPU
including Omni-Compass's own, the declared energy models. The omni arm is reported against native and against the
compass arm by the same rule. A run that fails its own checks (reset, controller stopped early, missing permission)
is marked invalid and left out, never silently counted.

Evidence class **L**: real Kubernetes software on kind. Energy on kind is a declared model, not a meter.

## Set 26 result

Compass arm against native: machines in service -17.2% (-26.4% to -7.9% of native), p95 -64.8%, failed requests 0 on
both: **better on machines within the band** (`results/live/LIVE_REPS_26.md`). The allocation law in the same set:
machines -35.8%, p95 -55.4%.

## Set 27 (written before the run)

The compass in the live controller now reads the service as the GPU compass does (`omni_controller/gpu_compass.py`, GPU
amendments 6 and 7): the mean response time of the latency window between the bare service time (a tenth of the SLO)
and the SLO, held at the compass's center 0.4 (the GPU service profile); p95 at or past the SLO, a blind probe or a pod
waiting for a place is past the wall. Everything else, the arms (native, omni, compass), the load, the duration, the
outcomes and the labelling rule above, is unchanged. The run's commit is the one that carries this section.

## Set 27 result

Compass arm, aligned with the GPU governor, against native: machines in service -15.9% (-1.462 to -0.450 machines),
p95 -65.5% (-311.8 to -156.1 ms), p99 -72.6%, failed requests 0 on both: **better on machines within the band**
(`results/live/LIVE_REPS_27.md`, run 37071353971, commit `d46c959`). The allocation law in the same set: machines
-36.6%, p95 -53.1%.

## The verdict in the live controller (2026-10-03, before any further set)

The compass law gives a machine back only where it measures that the service is no worse for it
(`omnicompass/verdict.py`, stepwise, in `omni_controller/controller.py`). While the service is calm (inside the compass,
no pod waiting, no breach), one more machine is given back on trial. The response times of 200 requests served without
it are set against 200 served just before and against the cluster as it first ran on its own:
- at most 2% slower than both: the machine stays given back;
- slower than that: it is taken back and not tried again for 120 decisions.

Where no machine passes, the pool stays as the cluster runs it alone. The HPA target's cover is unchanged: from 60% of
the operator's target up to the operator's own, never looser than native. Every trial is in the audit. The next set
runs with this verdict; sets 26 and 27 ran before it and stay as they ran.

## Set 28 and set 29 (2026-10-03, set 29 written before its run)

Set 28 (run 37087620193, commit `24666d7`) ran the compass law with the verdict. With Omni-Compass on top against native:
- machines in service −4.7%;
- p95 −65.3%, p99 −68.6%;
- pods waiting 0;
- failed requests 0.

Total CPU including Omni-Compass's own came out **+2.2%** (+0.003 to +0.042 cores), more than the 2% the one rule
allows (`DISCLOSURES.md`, section 3). The cause is the controller's own cost: 0.063 cores, mostly a new kubectl process
for every read, about 20 a minute. The compass law with the verdict freed only 0.040 cores of work. The allocation law in
the same set: machines −29.6%, p95 −58.0%, total CPU including its own −1.2% (not significant). Set 28's receipt is
`results/live/LIVE_REPS_28.md`, published with this section.

**Set 29** runs the same arms, load, duration, outcomes and rule as set 28. One thing changes: the controller reads
through one `kubectl proxy` started once, under the same least-privilege identity, so a read is a local HTTP request
instead of a new kubectl process (`omni_controller/controller.py`, `Kube`; writes are unchanged; `tests/test_api_proxy.py`).
The label also requires total CPU including Omni-Compass's own to be no more than 2% above native.

Set 29 result (run 37094338955, commit `a3721cc`): the compass law with the verdict, total CPU including its own **−4.7%**
(−0.071 to −0.017 cores), passes; Omni-Compass's own CPU 0.011 cores (set 28: 0.063). Machines −5.1%, p95 −64.4%,
p99 −71.1%, HPA replicas −7.6%, failed requests 0. No measure significantly worse than native in either arm. Receipt:
`results/live/LIVE_REPS_29.md`.

## The cost to match (written before its run)

The question a buyer asks: what would native Kubernetes have to spend to answer as fast as it does with Omni-Compass on
top? Each repetition runs, on the same runner and the same work, in rotated order:
- native (the operator's HPA target 50);
- native tuned harder by its operator, HPA target 40, 30 and 20 (more pods, faster answers), no Omni-Compass (`ARM=native40`, `native30`, `native20` in `scripts/kind_bench.sh`);
- native with Omni-Compass on top, the allocation law (`omni`);
- native with Omni-Compass on top, the compass law with the verdict (`compass`).

The report (`tools/live_reps.py`, "The cost to match") lists every arm's p95, p99, HPA replicas, CPU including
Omni-Compass's own, and machines in service. For each Omni-Compass arm it names the cheapest native setting (by CPU)
whose p95 is at or under Omni-Compass's, and that setting's extra replicas, CPU and machines over Omni-Compass. If no
native setting tried reaches it, the report says so and gives the lowest native p95. 10 repetitions, 900 measured
seconds per arm, fixed-rate load.

## The fault test (written before its run)

Health, security and the babysitting a cluster needs, measured. Every arm (native; native with Omni-Compass on top,
the allocation law; native with Omni-Compass on top, the compass law with the verdict) meets the same four faults at the
same moments (`scripts/kind_faults.sh`, `FAULTS=1`):
1. at 15% of the run, a worker machine dies (its kind container is stopped) and comes back two minutes later;
2. at 35%, traffic triples for two minutes;
3. at 55%, a pod with no CPU limit burns CPU for two minutes;
4. at 75%, the response-time probe goes blind for one minute.

For each fault the report (`tools/live_reps.py`, "The fault test") gives the time to recover (from the fault's start
until responses stay under the line for 30 s straight, at most 300 s) and the share of samples over the line or failed
in the 300 s after it, paired against native over 10 repetitions. All the usual gauges are reported as well, now
including the share of response samples over the line (`pilot/bench_report.py`). Lower is better in each.

**The fault test, first run** (run 37094604580, commit `a149d4e`; `results/live/FAULTS.md`). Omni-Compass on top
recovered faster than native from every fault (allocation law: machine down −29%, runaway pod −35%, spike −7%; compass
law: −14%, −17%, −6%), p95 −53% and −55%, p99 −27% (not significant) and −57%. One measure was worse: with the compass law,
**HPA replicas +8.2%** (+0.41 to +0.99, significant), with CPU and machines unchanged and no energy saved, so outside
the one rule (`DISCLOSURES.md`, section 3). The cause: past the wall the compass lowers the HPA target at once (more pods,
the faster recovery), then handed the operator's target back step by step and held each step for the autoscaler's
window, so the extra pods outlived the fault.

**The change, written before the re-run** (`omni_controller/controller.py`, the compass's push and pull on the HPA target;
`tests/test_compass_controller.py`, "fault over"): once the responses are back inside the band (the compass's position under
its center), the response line is clean and no pod is waiting, the operator's own target returns at once and is not
held by the window. More pods only while the fault lasts. The re-run is the same fault test, arms, load, duration and
rule (set 30 F); set 30 runs the same code without faults, to show nothing else moved.

**Set 30 and set 30 F** (runs 37105047258 and 37105046042, commit `acc1c4e`; `results/live/LIVE_REPS_30.md`,
`results/live/FAULTS_30.md`). Set 30, no faults: nothing significantly worse in either arm; the compass law's machines
−9.9%, p95 −64.9%, time over the line −98.7%, HPA replicas −32.2%, total CPU −6.5%. Set 30 F: recovery faster than native
from every fault in both arms; the compass law's HPA replicas **+5.6%** (first run +8.2%), still significant, with CPU and
machines unchanged. The allocation law, which recovers as fast or faster, held no extra pods (+2.0%, not significant).

**The second change, written before set 31 F** (`omni_controller/controller.py`; `tests/test_compass_controller.py`,
"blind"). Past the wall, the compass lowers the HPA target (more pods) only when the cause is load: the response line
breached with every sense live and no pod waiting. Past the wall from a blind sense, or from pods waiting for a machine
that is gone, more pods answer neither, so the target is the operator's own: fail up is native's own setting, as on the
card, where fail up is the card's own clock and limit. The machine reflex (one machine more past the wall) is unchanged.
Set 31 F is the same fault test, arms, load, duration and rule; set 31 the same without faults.

**Set 31 and set 31 F** (runs 37110007121 and 37110005322, commit `0a38e76`; `results/live/LIVE_REPS_31.md`,
`results/live/FAULTS_31.md`). Set 31 F: the compass law's HPA replicas under faults **−1.1%** (not significant): the extra
pods are gone. Nothing significantly worse in either arm; recovery faster than native from every fault (compass law,
machine down −49%). Set 31: nothing significantly worse; the compass law's machines −10.4%, p95 −66.0%, p99 −73.0%, time over
the line −99.4%, HPA replicas −44.5%, pods started 0 against native's 4.3, total CPU −6.1%.

## The bill on a real cloud (written before its run)

The question a buyer pays for: the same work, a smaller bill? On kind every machine stays powered, so a machine given
back saves only a declared model's energy. On a real cloud the machine is deleted and stops being billed. The run
(`.github/workflows/aks-metered.yml`, `scripts/aks_paired.sh`, `scripts/kind_bench.sh` with `PLATFORM=aks`):

- **The cluster.** Azure Kubernetes Service, a fresh cluster for every arm, built the same way:
  - a system pool of one machine, tainted so no workload lands on it (AKS's add-ons and the load generator: kind's
    control plane);
  - a work pool starting at 4 machines (Standard_D2s_v5) under **Azure's own cluster autoscaler** (min 1, max 4; scale
    down after 2 minutes unneeded), which deletes a machine once it is empty.
- **The arms**, rotated in each repetition:
  - native: Kubernetes with Azure's autoscaler alone;
  - native with Omni-Compass on top, the compass law with the verdict (`compass`);
  - native with Omni-Compass on top, the allocation law (`omni`).

  With Omni-Compass on top, the machines it gives back are idled (new pods go elsewhere, their pods leave first), and
  Azure's autoscaler then deletes them. Omni-Compass never deletes a machine itself.
- **The same work** in every arm: the fixed-rate load of sets 22 onward, 900 measured seconds after 120 s of warm-up.
- **The bill.** Every 15 s, the number of work machines that exist (in service or idle, every one is billed),
  integrated over the measured window: billed machine-hours, priced at Azure's list price for the machine
  (USD 0.096 an hour for Standard_D2s_v5, Linux, pay as you go, set in the workflow's input). Omni-Compass never reads
  this count.
- **Outcomes.** Billed machine-hours and the bill (lower is better), and every gauge of sets 28 and 29 (response time,
  failures, pods waiting, CPU including Omni-Compass's own), paired against native with 95% intervals over 5
  repetitions. Labelled by the one rule (`DISCLOSURES.md`, section 3): nothing more than 2% worse, and only where the
  bill or energy is saved.
- **Housekeeping.** One repetition at a time; each cluster deleted when its arm ends, before the next is made; the
  resource group deleted at the end of every repetition whatever happens. It needs the repository secret
  `AZURE_CREDENTIALS`.

## The capacity test (written before its run)

The question behind "more work for the same cost": on the same machines, how much more work does Kubernetes serve
with Omni-Compass on top before its answers break the line? Each repetition runs native, native with Omni-Compass on
top (the allocation law) and with the compass law and the verdict, in rotated order, on the same six workers, the
open-loop load rising in eight equal steps of one load generator each (6 requests a second per generator, 1 to 8
generators, 200 s a step, 1,600 measured seconds; `load_steps` in `benchmark-reps`). A run's capacity is the highest
step at which no more than 5% of the response samples (every 5 s, through the Service) are over the line (500 ms) or
failed, every lower step holding too, the first 30 s of each step left to settle (`tools/live_reps.py`, `capacity`).
Reported: each arm's mean capacity in requests a second, its change against native and the 95% interval of the paired
difference over 10 repetitions; every usual gauge beside it. Labelled by the one rule: nothing more than 2% worse.


## The fairness test (written before its run)

The question a buyer with many tenants asks: when one application surges, does Omni-Compass on top protect its
neighbour, or starve it? Each repetition runs native, native with Omni-Compass on top (the allocation law) and with the
compass law and the verdict, in rotated order, on the same six workers, with two applications on them (`TWO_APP=1`,
`deploy/kind/noisy.yaml`): php-apache under its usual fixed-rate load, and a noisy neighbour, the same image and the
same HPA rule, whose own fixed-rate load surges in steps (0, 0, 6, 0, 6, 0 load generators of 6 requests a second, the
same moments in every arm). Each application's response time is probed through its own Service. Omni-Compass governs
both HPAs (`deploy/kind/rbac-omni-noisy.yaml`: the second HPA and nothing else more). Reported: every usual gauge for
php-apache, and the neighbour's p95, p99, time over the line and failed requests, each paired against native over 10
repetitions with its 95% interval. The label is the one rule, applied to both applications: nothing more than 2% worse
for either.

## The capacity and fairness results, and the amendment they call for (2026-10-03 evening, before either is run again)

**Capacity** (`results/live/CAPACITY.md`, run 37150909816): the compass law served 33.0 requests a second within the line
against native's 24.6, **+34.1% (95% interval of the paired difference +6.2 to +10.6 requests a second)**, with
response times about half of native's and fewer failures. One measure significantly worse: pods started 7.3 against
5.6 (+30.4%) while the mean HPA replicas were 26.9% lower: churn, not more pods. **Fairness**
(`results/live/FAIRNESS.md`, run 37154210570): the neighbour unharmed under both laws; with the compass law php-apache's
failed requests 3.89% to 4.90% (+0.12 to +1.90 points), pending pods and pod start wait worse, no machine saved. By the
one rule neither result is labelled better. Both causes are read from the controller's code; both corrections are
stated here, as law, before the tests run again.

**1. Only a sensed muscle moves (the fairness cause).** Let the probe measure the response time of the services in a
set $\mathcal{S}$ (`--sensed ns/deployment,...`; empty means every HPA, the single-service case). For each HPA $h$
scaling a deployment $d(h)$ with the operator's target $x^{op}_h$, the target written is

$$x_h(t) = \begin{cases} \text{the compass's (or the allocation law's) target} & d(h) \in \mathcal{S} \\ x^{op}_h & d(h) \notin \mathcal{S} \end{cases}$$

The probe's position $p$ is a statement about $\mathcal{S}$ alone. A push on a muscle outside $\mathcal{S}$ answers no
sensed error and adds pods that compete with $\mathcal{S}$ for the same machines (the run's pending pods and failures).
It is the GPU law's own rule, applied to Kubernetes: where Omni-Compass cannot sense, it stands at native's own setting.

**2. Pods owed to a growing demand stay (the churn cause).** Let $u(t)$ be the CPU the workers use and $W$ the HPA's
scale-down window ($W = 300$ s unless the operator set one). The demand is *still growing* when

$$G(t) = \Big[\, u(t) > (1 + \epsilon)\, \min_{t - W \le s \le t} u(s) \,\Big], \qquad \epsilon = 0.05 .$$

After a breach the compass lowers the target to the bottom of its cover, $x = x_{lo} = 0.6\,x^{op}$ (more pods, at once).
Before this amendment, the first decision with the position back under the centre, $p < c = 0.4$, no breach and no
pod waiting, returned $x = x^{op}$ at once. Under a rising load the autoscaler then removed the extra pods one window
later and started them again at the next step: the run's churn. The return is now

$$x \leftarrow x^{op} \quad \text{only if} \quad p < c,\ \ \text{no breach},\ \ \text{no pod waiting},\ \ \neg G(t),$$

and while $G(t)$ holds the target stays where the breach put it. A fault or a spike that has passed has a flat or
falling $u$, so $G$ is false and the operator's target returns at once, as the fault test requires (set 31 F:
HPA replicas under faults −1.1%); only a demand still climbing keeps its pods. $\epsilon = 0.05$ is set above the
decision-to-decision noise of the node CPU reading. A rise too small to clear it leaves the rule as it was before this
amendment (the target returns at once), so the correction can remove churn but cannot add any.

Nothing else changes: the compass's band, gains and centre, the verdict, the fail-up rules, the release gate and the
node-pool law are as registered. Tests: `tests/test_compass_controller.py`, cases *demand* and *sensed*, beside the
existing *fault over*, *blind* and reset cases.

**The re-runs**, on the commit that carries this amendment, unchanged in design: the capacity test (`load_steps` 1 to
8, 1,600 s), the fairness test (`two_app` 1, 900 s) and the fault test (`faults` 1, 900 s), 10 paired repetitions
each, arms native / omni / compass. The second application is now probed and reported as before, and its HPA is held at
the operator's target. Labelled by the one rule. Every number, whatever it says, is published beside the runs above.

## The re-runs under the amendment: results (2026-10-04)

All three on commit `199f350`, 10 paired repetitions each, the design unchanged.

- **Fault test, set 32 F** (`results/live/FAULTS_32.md`, run 37162459956): **no measure significantly worse under
  either law.** The compass law recovers from a lost machine 58% faster and starts 34% fewer pods; the amendment left the
  fault behaviour of set 31 F intact.
- **Fairness** (`results/live/FAIRNESS_2.md`, run 37162458834): **correction 1 holds.** With the compass law php-apache's
  failed requests are no longer worse (−14.0%, not significant; before +26.0%), pending pods −10.5% (before +65.2%);
  the neighbour unharmed under both laws. The compass law's response-time gains in this test are no longer significant.
  Still worse under both laws: the mean pod start wait (+1.1 s compass, +1.7 s allocation law).
- **Capacity** (`results/live/CAPACITY_2.md`, run 37162457542): the compass law served **24.6 against native's 16.2
  requests a second, +51.9% (+6.2 to +10.6)**, the same paired difference as the first run on slower runners;
  response times −28% to −56%, failures −9.6%, HPA replicas −10.7%. **Correction 2 did not remove the extra pod
  starts** (5.1 against 3.8, +34.2%; before +30.4%): its premise, that the extra starts were pods removed and started
  again between steps, is not borne out. With the mean replicas lower, the reading the data support is pods started
  earlier on a rising load, the mechanism of the added capacity. Correction 2 stays (it removes no gain and added no
  measure worse); the pod-start rows stand as measured, and by the one rule neither the capacity nor the fairness arm
  is labelled better while they do.

## The pod record, and the second amendment (2026-10-04, before the next runs)

**What the pod record shows** (`tools/pod_report.py`, workflow `pod-report`, read from the stored artifacts of runs
37162457542 and 37162458834; nothing re-run). In the capacity test native started its pods once, early (33 of 38 in
the first fifth of the window), and removed none. With Omni-Compass on top, two minutes into the window the controller
raised the HPA target above the operator's (the conveyance: each pod given a larger CPU limit, the target raised by the
same factor so each pod stays as busy, $x = g\,x^{op}$; 114% with the compass law, 190% with the allocation law). The
autoscaler then removed pods (14 with the compass law, 35 with the allocation law, over ten repetitions), and the next
load steps started them again. **The extra starts are exactly those removals.** Correction 2 above read the wrong
signal: the CPU used by the whole node, where one load step is lost in the node's own load.

**3. A raise of the target waits for a steady demand.** Let the demand on an HPA's service be read from the
autoscaler's own status, $D(t) = \bar{u}(t)\, r(t)$: the pods' mean CPU utilisation of their request times the pods
running, the CPU used in units of one pod's request. With $W$ the HPA's scale-down window and $\epsilon = 0.05$,

$$S(t) = \Big[\, t - t_0 \ge 0.9\,W \ \wedge\ \max_{[t-W,\,t]} D \le (1+\epsilon)\min_{[t-W,\,t]} D \,\Big]$$

($t_0$ the oldest sample in the window). A new target above the one standing (fewer, larger pods) is written only
when $S(t)$ holds; the autoscaler itself removes pods only after its scale-down window, and Omni-Compass now asks the
same of its own consolidation. A lower target (more pods) is never held, and the return of the operator's own target
after a fault (rule 2) is unchanged. Correction 2's growth test $G(t)$ now reads the same $D(t)$ of the HPA concerned,
not the node's CPU. Tests: `tests/test_compass_controller.py`, case *steady*.

The capacity, fairness and fault tests are run again on the commit that carries this amendment, unchanged in design,
and published beside the runs above whatever they show. The bill run on Azure (`aks-metered`, run 37171672509)
started on commit `199f350`, before this amendment, and is reported as of that commit.

## The third amendment, and a change considered and declined (2026-10-04, before the next runs)

**4. A lower target is never held.** Until now every new HPA target, in either direction, was held for one autoscaler
window $W$ while the line was clean, so on a step up the compass's push (a lower target, more pods) could wait up to $W$
and the pods arrive after the line is missed. The hold exists because a raise inside the window removes pods the
autoscaler then starts again; a lower target asks for pods and removes none. The hold now applies to raises only:

$$\text{write } x_h(t) \iff x_h(t) < x_h^{\text{now}}\ \vee\ \text{no write in } [t-W,\,t)\ \vee\ \text{the operator's own target returns},$$

with rule 3 still requiring a steady demand before any raise. Tests: `tests/test_convey.py` (a lower target written at
once inside the window).

**Declined: raising the replica cap above the operator's.** `deploy/kind/demo.yaml` sets `maxReplicas: 10`, and at
the top of the capacity test both arms meet it. Lifting it would let Omni-Compass run more pods than the operator
authorised, which is more resources, not the same resources used better, and it would break the shield's standing
rule that Omni-Compass never moves past an operator's bound. Native would need the same cap for the comparison to
stay fair. It stays at the operator's value in every arm; a higher cap is the operator's decision, tested as its own
setting if ever asked for. Already in place and unchanged: a pod waiting for a place reads as past the wall and asks
for one machine more at once.

A narrower form was proposed the same day (`docs/history/AMENDMENT_RISING_STEP_CAP.md`): while the demand rises and a
pod of the sensed service is pending, raise `maxReplicas` by the pending count and lower the target to match. It is
declined for a mechanical reason as well as the one above. The replica cap does not make pods pending: at the cap the
autoscaler simply asks for no more pods, so the pending count there is zero and the write would never fire where it is
aimed. A pod is pending only when the scheduler finds no machine with room for it, and more places under the cap give
such a pod nowhere more to go; the answer to that is a machine, which the compass already asks for. The part of the
proposal that holds, asking for pods at once on a step up instead of after a window, is rule 4 above.

On the CPU fill (used over allocatable about 0.10 in every arm): on kind every worker reports all of the host's cores
as its own, so the allocatable counts the same cores once per worker and the fill reads far lower than the machine
doing the work. Every receipt from the next runs on carries the host's own busy share and core count
(`host_cpu.csv`, `tools/live_reps.py`), so the room left on the real machine is measured, not inferred.

The capacity, fairness and fault tests are run again on the commit that carries this amendment, beside the runs of
commit `5d2e238` (rule 3 alone), so each rule's effect stays separable.

## The second amendment's runs: results (2026-10-04)

`results/live/AMENDMENT_2_RUNS.md`, commit `5d2e238` (rule 3 alone), 10 paired repetitions each.

- **Capacity: no measure significantly worse under either law.** Compass law 24.6 against native's 17.4 requests a
  second, +41.4% (+5.4 to +9.0); allocation law 25.2, +44.8% (+4.9 to +10.7). The compass law's pods started 5.7 against
  4.1, interval −0.64 to +3.84: no longer significant. Rule 3 removed the significant pod-start excess and lifted the
  allocation law's capacity from +0.0% to +44.8%.
- **Faults: no measure significantly worse under either law.**
- **Fairness: the compass law, no measure significantly worse for either application.** The allocation law: php-apache
  much better, and the neighbour's failed requests **+0.74 points (+0.19 to +1.28), significant**. The allocation law
  conveys idle CPU to the service it senses; on machines shared with a surging neighbour that CPU is the neighbour's
  headroom. The allocation law is not labelled better in this test.

**Standing after rule 3: the compass law is clean in all three tests** (no measure significantly worse, capacity +41.4%).
Rule 4 (a lower target never held) runs next on commit `583c97f`, beside these, to see whether it adds capacity without
costing a row.

## The fourth amendment: the replica cap as a lever the operator grants (2026-10-04, before its run)

The founder's instruction: no number in the harness is hard-wired; every one moves where the system lets it. The cap
of 10 in `deploy/kind/demo.yaml` is the value of Kubernetes' own php-apache example, not a choice of any operator, and
an earlier session read it as an operator's bound. It becomes a lever, under the operator's grant.

**5. Replica room.** With `--replica-ceiling` $N_{\max}$ granted (0, the default, leaves the cap untouched), for a
sensed HPA under the compass law, with $r$ the pods running, $c$ the cap, $\bar{u}$ the pods' mean utilisation and $x$
the target, the autoscaler's own arithmetic asks for $n = \lceil r\,\bar{u}/x \rceil$ replicas, and

$$c \leftarrow \min(N_{\max},\, n) \quad \text{if } r \ge c,\ n > c,\ p \ge \text{centre or the line is breached};$$
$$c \leftarrow c^{op} \quad \text{if } n \le c^{op},\ p < \text{centre},\ \text{no breach},\ S(t).$$

The cap is raised only while it binds and the line is threatened, to what the autoscaler asks and never past the grant,
and returns to the operator's once the demand has held still for a window. The operator's range is recorded before
the first change; the reset restores it. Tests: `tests/test_compass_controller.py`, case *room*.

**Its run** (a setting of its own, labelled as such): the capacity test unchanged, `replica_ceiling` 30, beside the
runs without it. Native keeps its cap of 10, as an operator who has not raised it would; the extra pods the compass uses
are counted in the HPA replicas row, so the receipt shows what the capacity cost in pods, not the gain alone.

## The third and fourth amendments, and the bill on a real cloud: results (2026-10-04)

**Rule 4** (`results/live/AMENDMENT_3_RUNS.md`, commit `583c97f`): **the compass law has no measure more than 2% worse in
any of the three tests.** Capacity +48.1% (+5.7 to +9.9), nothing worse; fairness, neither application worse (energy
per core-hour on the declared standby model +1.5%, inside the allowance); faults, nothing worse, lost-machine recovery
−61%. The allocation law: capacity +55.6%, nothing worse; in fairness the neighbour no longer worse. The first runs with
the real machine metered: a 4-core GitHub runner 48% to 70% busy, where kind's "used / allocatable" reads 0.07 to 0.10.

**Rule 5, the replica lever** (`results/live/REPLICA_ROOM.md`, commit `2101c3d`, ceiling 30): the compass law served 24.6
requests a second, the same as without the lever, with 78% more pods and 26 pod starts against native's 4.6, both
significant. **The replica cap was not what limited the service; the machine doing the work was.** The lever stays,
off by default, as the operator's to grant where machines have room; it is not part of Omni-Compass's default setting
and this setting is not labelled better.

**The bill on a real cloud** (`results/live/AKS_BILL.md`, run 37187059424, commit `5b2832f`, four paired repetitions):
**no difference in the bill either way** (allocation law −0.6%, compass law +0.8%, intervals across zero) and no measure
significantly worse. Azure's own autoscaler already ran the workload on about 1.86 of 4 workers, so this light
workload leaves no machine to give back. The machine savings measured on kind, where native has no node autoscaler, do
not carry to a cloud with one at this load; that is the reading of record. The preregistered size `Standard_D2s_v5` is
not allowed in the subscription's region; `Standard_D2s_v4` (same 2 vCPU, 8 GiB and list price) was used. Three
earlier attempts stopped at the load generator's placement before any measurement and are not results.


## The burst bill test (written before its run, 2026-10-04)

The steady bill run left Azure's autoscaler nothing to do and Omni-Compass no machine to give back. The question a
buyer asks is the bill under load that moves: on a real cloud, with Azure's own cluster autoscaler underneath, does
native with Omni-Compass on top bill fewer machine-hours than native alone when demand rises and falls? Same design as
"The bill on a real cloud" (fresh AKS cluster per arm, work pool 1 to 4 `Standard_D2s_v4` under Azure's autoscaler, the
bill metered every 15 s, arms native / compass / omni rotated, five repetitions), with the open-loop load in bursts
(`load_steps` 1 6 1 8 1 6, six steps over 1,800 measured seconds, the same steps in every arm). Reported: machine-hours
and the bill at list price, paired against native with their 95% intervals, beside every service gauge. Labelled by the
one rule: a lower bill counts only if nothing is more than 2% worse.


## The six organisms with the real cluster inside (written before its run, 2026-10-04)

Every benchmark runs the same six organisms, native against native with Omni-Compass on top: the four realms, the whole
tower of 656 muscles, and the four stacked with every duplicate kept (1,226). Six organisms, two arms, twelve columns.
The model grid (`six`) and the card in the loop (`tools/run_hil.py`, single card and eight cards) already do. The
Kubernetes runs now do too (`tools/run_kil.py`, workflow `six-kube` on kind, input `organism` on `aks-metered`).

Each organism runs on the measured window's clock, 240 steps, with the real cluster as one more muscle:

- efferent: the organism's offered compute work at step k, D(k) = sum over its compute pools of lam_i(k) / sum of
  lam0_i, the seeded trace, identical in both arms. The load generator runs
  r(k) = 1 + round((LOAD_MAX - 1) (D(k) - min D) / (max D - min D)) replicas, LOAD_MAX = 6 declared here, open-loop load.
- afferent: the cluster's watts (capture.csv, the declared power model, every 15 s, identical accounting in both arms)
  are added to the organism's source, zone and site power, as the card's watts are in the card harness.
- the clock (stated 2026-10-07, after the 1,000-copy runs): the organism must keep the window's clock. `tools/run_kil.py`
  records how long after the window its last step ended (`behind_s`); the report (`tools/six_kube_report.py`) shows it as
  "organism behind its window (s)", shown and not judged, and marks a repetition OFF THE CLOCK when either arm ended more
  than 5% of the window late, because its last steps then saw a cluster whose load schedule had already ended. The pairing
  stands (both arms slip alike), the mark stays on the cell. The remedy is a longer window for that size on that machine
  (240 steps, each at least the machine's time to step the organism once), never a change to the organism or the law:
  the four stacked at 1,000 copies (1.7 million muscles) step in about 31 s on an 8-vCPU machine, so their window is
  10,800 s (45 s steps), against 2,880 s for the tower at 1,000 copies.

Arms: native (the stacks' own controllers, Kubernetes alone, Omni-Compass not started) and compass (the compass law on every
simulated muscle, rule 4 on the cluster, handed back at 90% of the window; the run is invalid if any knob is not handed
back). Five paired repetitions per organism, order rotated, each arm on a fresh six-worker kind cluster, 960 measured
seconds. Seed 6000 for every organism and arm.

Reported in `SIX_KUBE.md` (`tools/six_kube_report.py`): twelve columns of means, then per organism every gauge paired
against native with its 95% interval. Cluster rows are measured; organism rows are models (evidence S). Each organism is
labelled by the one rule: no measure more than 2% worse (CPU and host load shown, not judged), and a gain counts only
where energy or the bill is lower with an interval wholly below zero.


### Result: the six organisms with the real cluster inside (run 37217362568, commit `d81d5ee`)

Thirty jobs, six organisms times five paired repetitions, native against native with Omni-Compass on top (compass law),
every arm valid, every simulated knob handed back. Full report `results/live/SIX_KUBE.md`; raw files
`results/live/raw/run-37217362568/`.

On the real cluster, in every organism, native + Omni was late less often and answered faster:

| Organism | Time over the line, native → Omni | p95, native → Omni (ms) | Failed requests, native → Omni |
|---|---|---|---|
| Compute / AI / Cloud | 41.0% → 26.7% (better, -35%) | 3,967 → 2,653 (better, -33%, inside the noise) | 14.9% → 13.3% |
| Physics / Robotics / Autonomous | 28.4% → 15.5% (better, -45%) | 2,440 → 1,767 (better, -28%) | 5.7% → 5.0% |
| Energy / Facility / Industrial | 21.6% → 10.4% (better, -52%) | 1,951 → 1,482 (better, -24%) | 3.8% → 3.2% |
| Distribution / Specialized | 40.7% → 21.1% (better, -48%) | 2,830 → 1,943 (better, -31%) | 11.1% → 9.3% |
| The whole tower (656) | 25.8% → 14.7% (better, -43%, inside the noise) | 2,085 → 1,247 (better, -40%, inside the noise) | 12.8% → 9.1% |
| The four stacked (1,226) | 55.6% → 43.0% (better, -23%) | 3,703 → 2,803 (better, -24%) | 31.7% → 27.6% |

No measure came out worse beyond the noise in any organism. Energy (declared model) and CPU moved by under 3%, lower
with Omni in every organism. The modelled organisms around the cluster: work the same, energy 0.1-0.2% lower, time over
the line 0.5-2% lower, in every organism (evidence S).

Read with it: at a peak of six open-loop load generators the 4-core runner is past what the six workers can serve in
both arms (native late 22-56% of the time, 4-32% of requests failed; host 65-91% busy). The comparison is fair (same
load, same seed, same runner per pair); the absolute levels are an overloaded cluster, and a lower `load_max` is the
setting for a cluster inside its capacity.


## More work, faster, on fewer machines, with less energy: all four in one run (written before its run, 2026-10-04)

The four gains so far come from different tests: more work on the same machines (the capacity test, +48.1%), the same
work faster on fewer machines (sets 22-27), energy equal or lower in each. This test measures all four in one run.

Design: `benchmark-reps`, ten paired repetitions, arms native and compass (rule 4), order rotated, fresh six-worker kind
cluster per arm, open-loop load rising and then falling, `load_steps` 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1, 180 s a step
(2,700 measured seconds). The rise is the capacity test (`tools/live_reps.py capacity`, read on the way up to the
peak: the highest load step at which no more than 5% of response samples are over the 500 ms line or failed, every
lower step too). The fall is where machines are no longer needed and can be handed back. Over the whole window:
p95 response time, worker machines in service, energy (declared model; on kind it is not a meter), CPU with Omni's own.

Reported for each, native + Omni against native, paired, with the 95% interval and read in words (better or worse):
work (capacity, requests a second inside the line), speed (p95), machines (worker machines in service, mean), energy.

## The Omni index: one number for more for the same, or the same for less (written before its first use, 2026-10-04)

Each measure is turned into a ratio oriented so that above 1 is better for Omni-Compass:

- work: work with Omni / work native (capacity, requests served, work done)
- speed: p95 native / p95 with Omni (a lower response time is faster)
- machines: machines native / machines with Omni (in service, or billed machine-hours)
- energy: energy native / energy with Omni (or the bill)

The index of one test is the geometric mean of its oriented ratios, minus one, in percent: +30% reads "30% more for
the same, or the same for 30% less", across work, speed, machines and energy together. A measure a test did not take is
left out of that test, never filled in. A measure inside the noise is counted at its mean and flagged. A category
(real Kubernetes on GitHub, Azure, the card, the eight cards, the modelled muscles) is the geometric mean of its tests;
the headline is the geometric mean of the real categories, each weighted the same; the modelled muscles are shown
beside it, never inside it. Computed by `tools/omni_index.py` from each test's own paired results; nothing is typed in.


## Demand that wanders: up, spike, partway down, back up, down to idle (written before its run, 2026-10-04)

Real demand does not rise once and fall once. It climbs, spikes, eases part way, climbs again and finally settles to
idle. This test drives that shape and asks whether machines follow it in order: the emptiest machine idles first on the
way down (powered and Ready at its floor, never off), the warm machines wake first on the way up (no boot), one machine
always in service for the first burst (`scripts/kind_nodepool.sh`).

Design as the all-four test (ten pairs, native and compass, open-loop load, fresh six-worker kind cluster per arm), with
`load_steps` 1 2 3 2 3 4 5 6 5 3 5 6 5 4 3 2 3 2 1 1 (twenty steps of 135 s, 2,700 measured seconds), the same steps in
every arm. Reported, native + Omni against native, paired with the 95% interval and read in words: time over the 500 ms
line, failed requests, p95, worker machines in service (and its trace step by step), energy (declared model), CPU with
Omni's own, pods started. No capacity is read (the load does not only rise).


### Amendment to the wandering test, written before its run (2026-10-04)

The founder's two rules for real traffic, adopted before any result of the wandering test: traffic moves one step at a
time, up or down, never skipping (it may go 1 2 1 2 1 2 if it never needs 3); and machines never go below two, so two
are always in service, ready for a spike, with no ceiling but the machines the cluster has. The run started with the
earlier steps (which jumped 5 to 3 and 3 to 5) was cancelled before it finished; none of it is reported.

From this amendment: the machine floor is two in every arm Omni-Compass governs (`MIN_NODES`, default 2: the
controller's `--min-nodes`, the actuator `scripts/kind_nodepool.sh`, and every benchmark script). Native's own floor is
the cluster's: kind keeps all six workers. The wandering steps are 1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3 2 1 2 1
(twenty-five steps of 108 s, 2,700 measured seconds), every change one step, the same in every arm. Everything else
is as written above.


### Result: all four in one run (run 37226863122)

Ten paired repetitions, every arm valid. **Work +29.3%** (capacity 24.6 to 31.8 requests a second inside the line,
interval +5.4 to +9.0), **p95 -62.3%** (685.8 to 258.3 ms), time over the line -40.9%, failed requests -12.1%,
**machines in service -3.6%**, **energy -0.3%** (declared model), CPU with Omni's own -1.9%: each proven. No measure
worse beyond the noise (pending pod-minutes +19.6% and pods started +4.0%, both inside the noise). This run's machine
floor was one; the floor of two was adopted after it started. Report `results/live/ALL_FOUR.md`; raw files
`results/live/raw/run-37226863122/`; the Omni index updated (`results/OMNI_INDEX.md`).


### The boundary is the band, not a machine held out (written 2026-10-04, for every run started after it)

Holding one whole machine back as a ceiling was considered and set aside the same day: it takes one of the machines
away from the work. Every machine is usable (Omni-Compass's most is every machine that exists); the floor of two stays
for quiet times. The protection against running into the wall is the band inside every machine: capacity is added at
95% of the response line, before the line is reached, and a machine goes back only if the ones left still run at or
under the engine's utilisation target. An operator who wants whole machines held back can set `NODE_CUSHION` (off by
default). The wandering run under way (37235231963) uses every machine, as every run after it does.


## The six organisms at every size, the real cluster inside (written before its run, 2026-10-04)

The same six organisms, each native against native with Omni-Compass on top, at the sizes of the model grid: 10, 100
and 1,000 copies of the organism governed together on one clock, the one real cluster inside as one more muscle
(`tools/run_kil.py --scale`; size 1 is the run already recorded, `results/live/SIX_KUBE.md`). Workflow `six-kube`, one
job per organism, size and repetition, both arms on one runner, order rotated, fresh six-worker kind cluster per arm.

- Repetitions: 5 at 10 and 100 copies, 3 at 1,000. Measured window: 960 s at 10 copies, 1,440 s at 100, 2,880 s at
  1,000 (240 organism steps of 4, 6 and 12 s: a step at least 1.5 times what the organism takes to compute on this
  runner, measured: 0.18 s at 10 copies of the four stacked, 2.4 s at 100).
- The organism is built before the window opens (`organism.ready`); the window opens the moment it is built
  (`organism.go`), so the cluster and the organism start on one clock however long the build takes. If the organism
  falls behind its own clock, `organism.json` records by how much (`behind_s`).
- Machine floor two, every machine usable (the founder's rules above), open-loop load, peak six generators.
- Declared before the run: 1,000 copies of the whole tower (656,000 modelled muscles) and of the four stacked (1.2
  million) need about 6 and 11 GB of memory beside the cluster, past what one GitHub runner holds. They are run; if a
  runner cannot hold them, the job's failure is reported as that, never as a result.

Reported in `SIX_KUBE.md` by organism and size, every gauge paired against native with its 95% interval and read in
words.

The run dimension of the model grid (1, 10, 100, 1,000 runs) is a count of seeds; on the real cluster each repetition
is a real paired run of an hour or more, so the real cluster carries the repetitions above, and the model grid carries
1 to 1,000 runs.


### The two organisms too big for a GitHub runner: a larger rented machine (written before their run, 2026-10-05)

1,000 copies of the whole tower and of the four stacked run on a larger rented machine, the same test otherwise:
workflow `big-organism` rents one Azure Standard_D8s_v4 (8 vCPU, 32 GiB) per repetition, runs `scripts/kind_paired.sh`
on it (native against native with Omni-Compass on top, fresh six-worker kind cluster per arm, 2,880 measured seconds,
the organism at 1,000 copies with the real cluster inside), copies every file back and deletes the machine whatever
happens. Three paired repetitions per organism, two machines at a time. Its results join `SIX_KUBE.md` at 1,000 copies;
the same cells from GitHub runners count only if the runner held them.


### The burst bill test on Azure: two native arms lost to the harness, and the fix (2026-10-05)

Repetitions 2 and 3 of the burst bill test (run 37216328055) each lost their native arm (Kubernetes alone) at the
same moment: the load step from one generator to six. Native's two work machines were full, answers timed out, and the
API server stopped answering for minutes. The capture script ran with stop-on-first-error, so one unanswered reading
ended the recording, and the load schedule stopped at its next unanswered scale; the arm failed its checks and was
marked invalid. The Omni-Compass arms of the same repetitions ran every step. Those two arms are not counted.

That is a fault of the harness, and it threw away exactly the moments a cluster struggles. Fixed: a reading the API
server does not answer is logged (`capture.csv.errors`) and skipped, and the recording goes on; a scale the API server
does not answer is tried again, then logged, and the schedule goes on (`fleet/capture/kube_capture.sh`,
`scripts/kind_bench.sh`, `tools/run_kil.py`). Repetitions 4 and 5 started on the earlier code. When the run ends, three
more repetitions of the same test run on the fixed code, and the report counts every valid pair and names every
invalid arm with its cause.


## Amendment 6: a pinned gauge is not a steady demand (written before its run, 2026-10-05)

The wandering test (run 37235231963, ten pairs) gave native + Omni-Compass p95 -54%, time over the line -38%, failed
requests -14%, energy -0.3% and CPU -2%, each proven, and 1.5 more pod starts a run (+36%, proven). The founder holds
that result back until the cause is fixed and the test is run again.

The cause, read from the run's own audit (repetition 4, 12 pod starts against native's 7): at 972 s the load eased
from five generators to four, rule 3 found the demand steady, and the target was raised (50 to 190: fewer pods); the
load then climbed back to eight and the pods were started again. The demand was not steady. The autoscaler stood at its
replica cap, every pod as busy as it could be, so the reading (utilisation times pods) could not rise however much the
load did: a pinned gauge reads flat.

Rule 5 (amends rule 3): a decision at which the autoscaler stands at its replica cap marks the window pinned; a window
that touched the cap is not steady, so no raise of the target, and no return of a raised cap, until one whole
autoscaler window after the cap was last touched (`omni_controller/controller.py _steady`, `self.pinned`; tested in
`tests/test_compass_controller.py`). Nothing else changes.

The rerun: the same wandering test (ten pairs, native and compass, `load_steps` 1 2 3 2 3 4 5 6 5 4 5 6 7 8 7 6 5 4 3 4 3
2 1 2 1, 2,700 s, floor two, every machine usable). Reported in full, every gauge read in words; the first run is kept
in its raw files and named beside the rerun.


## Amendment 7: coasting, off the gas but still in gear (written before its run, 2026-10-05)

The founder's picture: a car in drive. At idle it creeps, ready (the floor of two machines). On the gas it speeds up at
once (more pods, machines woken, no boot). Off the gas it coasts down gradually toward idle; it does not drop into
neutral. The brake is for stopping (the reset hands everything back at once).

Rule 6: a raise of the HPA target (toward fewer pods) moves by at most `--coast-step` points of utilisation in one
autoscaler window (default 25, `COAST_STEP`; 0 turns it off). The first wandering run raised the target 50 to 190 in
one move; under rule 6 the same raise takes several calm windows (50, 75, 100, ...). A demand that comes back part way
finds the pods still running and is met at once by a lower target, with no pod started again. A lower target (more
pods) is never limited: the gas is always immediate. Rules 5 and 6 together: never ease off while the gauge is pinned,
and then ease off a step at a time (`omni_controller/controller.py`; tested in `tests/test_convey.py`).

The rerun with rule 5 alone (run 37255770249) was stopped before it finished, to run the test once with both rules;
none of it is reported. The rerun: the wandering test as written in amendment 6.


## Amendment 8: cruise and the emergency brake, and the batch test (written before its run, 2026-10-05)

The founder's driving modes: off (native alone), watching (Omni-Compass reads, writes nothing), autopilot (gas, brake,
idle), and two more for work that comes as a pile:

- **Rule 7, cruise:** work waiting for a place (pods pending) two decisions in a row puts every machine in service
  (`--max-nodes`), and they stay in service, without second-guessing, until the line has been empty and nothing is
  scaling up for two decisions (`--cruise-after`, default 2; 0 turns it off).
- **Rule 8, the emergency brake:** nothing waiting, no response-time breach, nothing scaling up, and the sensed
  services' demand at or under 0.05 of one pod's request (`--brake-demand`): the machines go straight to the floor
  (two) in one move. Every check of the release gate still holds (every sense live, the last command landed, the
  machines left at or under the utilisation target) except one machine per decision. Never below the floor.
- Tested through the live controller: `tests/test_cruise_brake.py` (in `verify.py`).

**The batch test:** a queue of jobs on the six-worker kind cluster (`WORKLOAD=batch`, `deploy/kind/batch-jobs.yaml`):
one Kubernetes Job of 240 pods, 60 at a time (more than the workers hold, so work waits for a place), each hashing
3,000 MB (real CPU work, identical in every arm), opened with the measured window (1,500 s); the service's load
generator stands at zero. Ten pairs, native and compass, order rotated. Reported, paired with the 95% interval and read in
words: how long the queue took to finish, the worker machines in service after it finished, machines in service and
energy over the whole window, CPU with Omni-Compass's own, pods started. Cruise must not slow the queue; the brake must
show in the machines held after it.

## The frozen engine (rules 1-8, commit 353903683009): the fault and fairness results (2026-10-05)

Both tests ran again with nothing changed but the engine: ten pairs each, native and omni, order rotated.

- The fault test (GitHub run 37262797634, `results/live/FAULTS.md`): better and proven on p95 (−60.1%), mean response
  (−34.5%), time over the line (−22.6%) and pending pods (−76.5%). Nothing came out worse beyond the noise. Recovery
  after the fault, paired means: machine down 42 s against 70 s, a blind probe 54 s against 66 s, a runaway pod 98 s
  against 105 s, a spike 266 s against 267 s.
- The fairness test (GitHub run 37262799317, `results/live/FAIRNESS.md`): better and proven on mean response (−15.0%).
  Nothing came out worse beyond the noise, the neighbour's app included.

These replace the earlier engine's fault and fairness sections of `results/live/AMENDMENT_3_RUNS.md` in the Omni index.
That file stays as first measured.

The Azure burst bill test and the big organisms, running them (2026-10-05): Azure no longer offers this subscription
Standard_D2s_v5 in eastus, so AKS workers are Standard_D2s_v4 (2 vCPU, 8 GiB, the same list price, USD 0.096 an
hour). Both arms use the same size; the steady-load result of record (`results/live/AKS_BILL.md`) stays as measured on
D2s_v5. The big-organism machine failed while seven kind nodes joined (kubelet-start). Fresh Ubuntu ships too few
inotify watchers for that; the rented machine now raises them as kind's own documentation advises. Neither change
touches the controller.

## Amendment 9: idle read from the autoscaler's floor, and the batch test again (written before its run, 2026-10-05)

The batch test on the frozen engine (GitHub run 37262795697) showed rule 8 late. The queue emptied 664 s into the
window, but the emergency brake fired at 1,574 s. The reason: a served service is never at zero CPU. The response
probe alone keeps one pod at about 10% of its request, which reads as demand 0.10, above the brake's 0.05. Rule 8 now
also counts a service as idle when its autoscaler stands at its least pods (`minReplicas`), wants no more, and runs at
no more than half its target utilisation. Every other condition of rule 8 holds as before: nothing waiting, no breach,
nothing scaling up, the release gate, every sense live, the last command landed, and the machines left carrying what
runs now under the utilisation target. Test: `tests/test_cruise_brake.py` (it brakes at the idle floor, and it does not
brake above the floor or busy at it).

Effect on what was already measured: none. The steady, fault, fairness, wandering and all-four runs on the frozen engine
had the service at one pod with nothing waiting in 0 of 5,102 readings, so the amended rule could not have fired in any
of them.

Three of the ten batch pairs stopped, all in the omni arm. The API server answered 500 under the batch load (60 jobs
asking for 30 cores on a 4-core runner), and the recording script ended on an unanswered `kubectl top nodes`. That is a
harness fault: a reading the API server does not answer is now logged and skipped, and the end-of-window reads are tried
again. The batch test runs again, ten pairs, on this engine, with the design unchanged.

## Amendment 10: two rows read for what they measure (written after the frozen-engine runs were seen, 2026-10-05)

Disclosed: this is a change in how two rows are read, made after the steady, wandering and all-four results were seen.
Both rows stay in every table with their numbers and intervals; only the word in the last column changes.

- **Pending pods.** The row counts pods pending in each 15 s snapshot. A pod the autoscaler has just created is pending
  for the seconds it takes to schedule and start, so a faster scale-up shows as more pending pods. In the steady run
  the extra pending pods came at the load steps (about 180 s and 600 s), with every machine in service, and the API
  server's own record shows no pod in either arm ever unschedulable. The row is now shown, not judged. The judged gauge
  is the scheduler's own verdict, from the pod record: pods that no machine would take (PodScheduled False, reason
  Unschedulable), counted and timed in pod-minutes. In the five frozen-engine runs it is 0 in every arm.
- **Energy per core-hour.** It is energy divided by CPU used. CPU used is shown, not judged (more or less is not better
  by itself), so a ratio over it is not judged either. Energy itself stays judged.

Nothing else changes. With these readings, no row of the steady, wandering, all-four, fault or fairness results is
worse than native beyond the noise.

## Amendment 11: the burst bill test sized to what the service can serve, and rounding read as the same (2026-10-05)

Disclosed: written after three repetitions of the burst test at `1 6 1 8 1 6` were seen. In them about 41% of requests
failed in both arms. The service's own autoscaler sat pinned at its cap of 10 pods, and 6 and 8 load generators (36
and 48 requests a second) ask more than 10 pods can serve, whatever the machines. A test where neither arm can do the
work cannot show a difference. The burst test runs at `1 3 1 4 1 3`: the peak is one step above the steady test's peak
of 3, and inside what the capped service can serve. Everything else is as preregistered: five repetitions,
1,800 measured seconds, Azure's autoscaler underneath, the bill metered every 15 s, native against compass. The three
repetitions at the old steps stay in the archive (`results/live/raw/run-37294579764/`) and are reported as the reason
for this amendment, not as a result.

In every table a paired change under one part in a million of the value reads "same", the number still shown
(`SAME_REL`, `docs/MECHANISM_OF_ACTION.md` 9.5).

## Amendment 12: cruise steps back, and the organism's start file (written before the batch rerun, 2026-10-05)

The batch rerun on amendment 9 (GitHub run 37275371557, ten valid pairs) gave machines -16.9%, -27.2% once the queue
was done, and energy -11.6% on the standby model. The queue finished 10 s later (584 s against 594 s, +1.8%). Omni held
every machine in service throughout, so the time went elsewhere: every five seconds the floor step read every pod (240
batch pods), every node, node metrics and every HPA, on the one 4-core runner the queue was using. In cruise every
machine is already in service, so those reads can change no action. From this amendment, while cruising the floor step
makes no read and no write, and the service's target stays at the operator's own (`docs/MECHANISM_OF_ACTION.md` 9.3;
`tests/test_compass_controller.py`). Cruise never engaged in the steady, wandering, all-four, fault or fairness runs,
so this changes nothing there. The batch test runs again, ten pairs, design unchanged.

The organism with the real cluster inside waits for a start file. One repetition of six-kube (the four stacked, 1 copy,
repetition 2) read that file in the instant it existed but was still empty, and stopped. The file is now written whole
or not at all, and read only once it holds a number. That repetition is reported as stopped, never counted.

Also found and fixed on 2026-10-05, from the compass rename: each modelled muscle's compass was made fresh at every
decision (`docs/MECHANISM_OF_ACTION.md` 9.1). That touched the modelled organism rows of the runs started after the rename
(six-kube 37280090832, big organism 37287311224); their cluster rows are unaffected. The organism runs go again on the
fixed code.

The batch test on amendment 12 (GitHub run 37344765837, ten pairs, `results/live/BATCH.md`): machines in service -20.7%,
-32.4% once the queue was done, energy -14.3% on the standby model, mean response -11.7%, all proven. The queue finished
+1.1% later, inside the noise (it was +1.8% and proven before cruise stepped back). No pod was left without a machine.
Nothing came out worse beyond the noise.

## The fleet that can show one machine: Azure at 11 and 15 workers (written before its run, 2026-10-07)

The Azure runs so far used a work pool of 1 to 4 machines. One machine is a quarter to a half of that fleet, and the
app's replica ceiling (10 pods of 200m, about one worker's worth) kept Azure's autoscaler at about 1.9 workers in both
arms, so nothing under a quarter of the fleet could show. The steady run on v1 (5 pairs) read even on every gauge. That
is a statement about the lever, not about the law. This run makes the lever big enough to see one machine.

- **Fleet.** The subscription allows 200 vCPUs in eastus but 10 vCPUs in each machine family (every family's request to
  raise it was refused through the API on 2026-10-07: the subscription's terms), so one family gives at most 5 machines.
  The fleet is therefore several work pools, one 2-vCPU machine family each, each capped at what its family allows:
  `worker_pools` = `Standard_D2s_v4:4,Standard_D2as_v4:5,Standard_D2_v4:5,Standard_D2a_v4:5,Standard_D2ds_v4:5,Standard_D2s_v3:5,Standard_E2s_v4:5,Standard_E2as_v4:5`,
  39 workers (the DSv4 family also carries the system machine, hence 4). Every pool carries the label `omni-role=work`,
  the worker selector in both arms; the first pool keeps one machine, the others may scale to zero; every pool starts
  full and Azure's own autoscaler trims, as before. One machine is then 2.6% of the fleet. Mixed machine families are how
  real cloud fleets run; the bill is each pool's machine-hours at its own list price (`pool_prices`), Azure's own count
  every 15 s. The same autoscaler profile, a fresh cluster per arm. (Written first for 11 then 15 workers of one family;
  the family allowance made that impossible and this replaces it before any such run.)
- **Ceiling.** `hpa_max` = 9 × workers = 351 at 39 workers: nine 200m pods fit one 2-vCPU worker, so the fleet can
  fill. The same ceiling in every arm; the restore checks expect it back untouched.
- **Load.** The load generator's replica steps scale with the fleet, the same in every arm (one load replica drove
  about five pods at 50% on the 4-worker runs). Steady: `18 35 53 18 35 18` over 900 s at 39 workers (the peak asks
  for about 265 pods, thirty workers' worth). Burst: `11 35 11 53 11 35` over 1,800 s (the 4-worker burst was
  `1 3 1 4 1 3`). A fleet of another size scales the steps by workers/39, rounded.
- **Everything else as preregistered**: native (Azure's autoscaler alone) against omni (Omni-Compass on top of it,
  rule 4 on the node pool, the HPA target inside its range, handed back at 90% of the window), 5 paired repetitions,
  order rotated, the bill Azure's own machine count every 15 s at list price, the reading by `tools/live_reps.py`'s
  paired interval, every gauge reported. Engine: Omni v3 first (the newest), v1 after if the credits allow.
- **What it can say.** Better, clear of the noise, in bill or response time: Omni has value on the managed service when
  the fleet is big enough to see a machine. Even again: Omni's value there is nil at this size too, and that is the
  reading. Worse: our own wiring is suspected first, found, fixed, and the run is made again.
- **Cost.** About $8 for the steady set and $15 for the burst set at 15 workers, at list price.

---
*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
