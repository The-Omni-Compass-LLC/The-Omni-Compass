# Preregistration: the bowl law on real Kubernetes (set 26)

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
| bowl | Omni-Compass on top with the bowl law (`--law bowl`, `omni_controller/controller.py`) |

Load: fixed rate (`loadgen=open`), the same work in every arm. 900 measured seconds per arm. SLO 500 ms at the 95th
percentile. Every Omni arm runs the six-state engine on every decision, the nervous system's authority and release
gate, the shield, the compass, and ends with the kill switch, which must return the HPA target, its replica range,
the pods' CPU limits and every worker to native, with no record left (`scripts/kind_bench.sh`).

## The bowl law in the live controller

The service position is the 95th-percentile response time over the SLO (0 calm, 1 the line); a blind probe or a pod
waiting for a place reads as past the wall. The force is `A tanh((K_P (p - 0.5) + K_D v) / A)` with K_D for critical
damping times the realm push factor 3, the same law and gains as on every realm muscle (`realms/bowl_arm.py`):
up gain 0.10, down gain 0.02, release threshold -0.2. Two levers:

1. **HPA target**, cover from 60% of the operator's target to the operator's own: the up force lowers it (more pods),
   the down force returns it toward the operator's. It is never tighter than native.
2. **Node pool**: past the 0.95 wall one machine more at once; one machine back only while the force is below -0.2,
   the position is below the center, and the nervous system's release gate is open.

## Outcomes and the rule

Primary: **worker nodes in service** (mean) and **95th-percentile response time**, each arm against native, paired
over the 10 repetitions with a t-based 95% interval (`tools/live_reps.py`).

Band first: the bowl arm is a win only if its p95 is not worse than native's (the upper end of the 95% interval of the
paired difference at or under 0) **and** failed requests are not higher. If that holds and machines in service fall
with an interval wholly below 0, the label is **better on machines within the band**. If machines fall but the band
condition fails, the label is **tradeoff**. Otherwise **not established**.

Secondary, reported, not used for the label: p99, mean response time, HPA replicas, pods started, pod start wait, CPU
including Omni-Compass's own, the declared energy models. The omni arm is reported against native and against the
bowl arm by the same rule. A run that fails its own checks (kill switch, controller stopped early, missing permission)
is marked invalid and left out, never silently counted.

Evidence class **L**: real Kubernetes software on kind. Energy on kind is a declared model, not a meter.

## Set 26 result

Bowl arm against native: machines in service -17.2% (-26.4% to -7.9% of native), p95 -64.8%, failed requests 0 on
both: **better on machines within the band** (`results/live/LIVE_REPS_26.md`). The allocation law in the same set:
machines -35.8%, p95 -55.4%.

## Set 27 (written before the run)

The bowl in the live controller now reads the service as the GPU bowl does (`omni_controller/gpu_bowl.py`, GPU
amendments 6 and 7): the mean response time of the latency window between the bare service time (a tenth of the SLO)
and the SLO, held at the bowl's center 0.4 (the GPU service profile); p95 at or past the SLO, a blind probe or a pod
waiting for a place is past the wall. Everything else, the arms (native, omni, bowl), the load, the duration, the
outcomes and the labelling rule above, is unchanged. The run's commit is the one that carries this section.

## Set 27 result

Bowl arm, aligned with the GPU governor, against native: machines in service -15.9% (-1.462 to -0.450 machines),
p95 -65.5% (-311.8 to -156.1 ms), p99 -72.6%, failed requests 0 on both: **better on machines within the band**
(`results/live/LIVE_REPS_27.md`, run 37071353971, commit `d46c959`). The allocation law in the same set: machines
-36.6%, p95 -53.1%.

## The verdict in the live controller (2026-10-03, before any further set)

The bowl law gives a machine back only where it measures that the service is no worse for it
(`omnicompass/verdict.py`, stepwise, in `omni_controller/controller.py`). While the service is calm (inside the bowl,
no pod waiting, no breach), one more machine is given back on trial. The response times of 200 requests served without
it are set against 200 served just before and against the cluster as it first ran on its own:
- at most 2% slower than both: the machine stays given back;
- slower than that: it is taken back and not tried again for 120 decisions.

Where no machine passes, the pool stays as the cluster runs it alone. The HPA target's cover is unchanged: from 60% of
the operator's target up to the operator's own, never looser than native. Every trial is in the audit. The next set
runs with this verdict; sets 26 and 27 ran before it and stay as they ran.

## Set 28 and set 29 (2026-10-03, set 29 written before its run)

Set 28 (run 37087620193, commit `24666d7`) ran the bowl law with the verdict. With Omni-Compass on top against native:
- machines in service −4.7%;
- p95 −65.3%, p99 −68.6%;
- pods waiting 0;
- failed requests 0.

Total CPU including Omni-Compass's own came out **+2.2%** (+0.003 to +0.042 cores), more than the 2% the one rule
allows (`DISCLOSURES.md`, section 3). The cause is the controller's own cost: 0.063 cores, mostly a new kubectl process
for every read, about 20 a minute. The bowl law with the verdict freed only 0.040 cores of work. The allocation law in
the same set: machines −29.6%, p95 −58.0%, total CPU including its own −1.2% (not significant). Set 28's receipt is
`results/live/LIVE_REPS_28.md`, published with this section.

**Set 29** runs the same arms, load, duration, outcomes and rule as set 28. One thing changes: the controller reads
through one `kubectl proxy` started once, under the same least-privilege identity, so a read is a local HTTP request
instead of a new kubectl process (`omni_controller/controller.py`, `Kube`; writes are unchanged; `tests/test_api_proxy.py`).
The label also requires total CPU including Omni-Compass's own to be no more than 2% above native.

Set 29 result (run 37094338955, commit `a3721cc`): the bowl law with the verdict, total CPU including its own **−4.7%**
(−0.071 to −0.017 cores), passes; Omni-Compass's own CPU 0.011 cores (set 28: 0.063). Machines −5.1%, p95 −64.4%,
p99 −71.1%, HPA replicas −7.6%, failed requests 0. No measure significantly worse than native in either arm. Receipt:
`results/live/LIVE_REPS_29.md`.

## The cost to match (written before its run)

The question a buyer asks: what would native Kubernetes have to spend to answer as fast as it does with Omni-Compass on
top? Each repetition runs, on the same runner and the same work, in rotated order:
- native (the operator's HPA target 50);
- native tuned harder by its operator, HPA target 40, 30 and 20 (more pods, faster answers), no Omni-Compass (`ARM=native40`, `native30`, `native20` in `scripts/kind_bench.sh`);
- native with Omni-Compass on top, the allocation law (`omni`);
- native with Omni-Compass on top, the bowl law with the verdict (`bowl`).

The report (`tools/live_reps.py`, "The cost to match") lists every arm's p95, p99, HPA replicas, CPU including
Omni-Compass's own, and machines in service. For each Omni-Compass arm it names the cheapest native setting (by CPU)
whose p95 is at or under Omni-Compass's, and that setting's extra replicas, CPU and machines over Omni-Compass. If no
native setting tried reaches it, the report says so and gives the lowest native p95. 10 repetitions, 900 measured
seconds per arm, fixed-rate load.

## The fault test (written before its run)

Health, security and the babysitting a cluster needs, measured. Every arm (native; native with Omni-Compass on top,
the allocation law; native with Omni-Compass on top, the bowl law with the verdict) meets the same four faults at the
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
recovered faster than native from every fault (allocation law: machine down −29%, runaway pod −35%, spike −7%; bowl
law: −14%, −17%, −6%), p95 −53% and −55%, p99 −27% (not significant) and −57%. One measure was worse: with the bowl law,
**HPA replicas +8.2%** (+0.41 to +0.99, significant), with CPU and machines unchanged and no energy saved, so outside
the one rule (`DISCLOSURES.md`, section 3). The cause: past the wall the bowl lowers the HPA target at once (more pods,
the faster recovery), then handed the operator's target back step by step and held each step for the autoscaler's
window, so the extra pods outlived the fault.

**The change, written before the re-run** (`omni_controller/controller.py`, the bowl's push and pull on the HPA target;
`tests/test_bowl_controller.py`, "fault over"): once the responses are back inside the band (the bowl's position under
its center), the response line is clean and no pod is waiting, the operator's own target returns at once and is not
held by the window. More pods only while the fault lasts. The re-run is the same fault test, arms, load, duration and
rule (set 30 F); set 30 runs the same code without faults, to show nothing else moved.

**Set 30 and set 30 F** (runs 37105047258 and 37105046042, commit `acc1c4e`; `results/live/LIVE_REPS_30.md`,
`results/live/FAULTS_30.md`). Set 30, no faults: nothing significantly worse in either arm; the bowl law's machines
−9.9%, p95 −64.9%, time over the line −98.7%, HPA replicas −32.2%, total CPU −6.5%. Set 30 F: recovery faster than native
from every fault in both arms; the bowl law's HPA replicas **+5.6%** (first run +8.2%), still significant, with CPU and
machines unchanged. The allocation law, which recovers as fast or faster, held no extra pods (+2.0%, not significant).

**The second change, written before set 31 F** (`omni_controller/controller.py`; `tests/test_bowl_controller.py`,
"blind"). Past the wall, the bowl lowers the HPA target (more pods) only when the cause is load: the response line
breached with every sense live and no pod waiting. Past the wall from a blind sense, or from pods waiting for a machine
that is gone, more pods answer neither, so the target is the operator's own: fail up is native's own setting, as on the
card, where fail up is the card's own clock and limit. The machine reflex (one machine more past the wall) is unchanged.
Set 31 F is the same fault test, arms, load, duration and rule; set 31 the same without faults.

**Set 31 and set 31 F** (runs 37110007121 and 37110005322, commit `0a38e76`; `results/live/LIVE_REPS_31.md`,
`results/live/FAULTS_31.md`). Set 31 F: the bowl law's HPA replicas under faults **−1.1%** (not significant): the extra
pods are gone. Nothing significantly worse in either arm; recovery faster than native from every fault (bowl law,
machine down −49%). Set 31: nothing significantly worse; the bowl law's machines −10.4%, p95 −66.0%, p99 −73.0%, time over
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
  - native with Omni-Compass on top, the bowl law with the verdict (`bowl`);
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
top (the allocation law) and with the bowl law and the verdict, in rotated order, on the same six workers, the
open-loop load rising in eight equal steps of one load generator each (6 requests a second per generator, 1 to 8
generators, 200 s a step, 1,600 measured seconds; `load_steps` in `benchmark-reps`). A run's capacity is the highest
step at which no more than 5% of the response samples (every 5 s, through the Service) are over the line (500 ms) or
failed, every lower step holding too, the first 30 s of each step left to settle (`tools/live_reps.py`, `capacity`).
Reported: each arm's mean capacity in requests a second, its change against native and the 95% interval of the paired
difference over 10 repetitions; every usual gauge beside it. Labelled by the one rule: nothing more than 2% worse.


## The fairness test (written before its run)

The question a buyer with many tenants asks: when one application surges, does Omni-Compass on top protect its
neighbour, or starve it? Each repetition runs native, native with Omni-Compass on top (the allocation law) and with the
bowl law and the verdict, in rotated order, on the same six workers, with two applications on them (`TWO_APP=1`,
`deploy/kind/noisy.yaml`): php-apache under its usual fixed-rate load, and a noisy neighbour, the same image and the
same HPA rule, whose own fixed-rate load surges in steps (0, 0, 6, 0, 6, 0 load generators of 6 requests a second, the
same moments in every arm). Each application's response time is probed through its own Service. Omni-Compass governs
both HPAs (`deploy/kind/rbac-omni-noisy.yaml`: the second HPA and nothing else more). Reported: every usual gauge for
php-apache, and the neighbour's p95, p99, time over the line and failed requests, each paired against native over 10
repetitions with its 95% interval. The label is the one rule, applied to both applications: nothing more than 2% worse
for either.

## The capacity and fairness results, and the amendment they call for (2026-10-03 evening, before either is run again)

**Capacity** (`results/live/CAPACITY.md`, run 37150909816): the bowl law served 33.0 requests a second within the line
against native's 24.6, **+34.1% (95% interval of the paired difference +6.2 to +10.6 requests a second)**, with
response times about half of native's and fewer failures. One measure significantly worse: pods started 7.3 against
5.6 (+30.4%) while the mean HPA replicas were 26.9% lower: churn, not more pods. **Fairness**
(`results/live/FAIRNESS.md`, run 37154210570): the neighbour unharmed under both laws; with the bowl law php-apache's
failed requests 3.89% to 4.90% (+0.12 to +1.90 points), pending pods and pod start wait worse, no machine saved. By the
one rule neither result is labelled better. Both causes are read from the controller's code; both corrections are
stated here, as law, before the tests run again.

**1. Only a sensed muscle moves (the fairness cause).** Let the probe measure the response time of the services in a
set $\mathcal{S}$ (`--sensed ns/deployment,...`; empty means every HPA, the single-service case). For each HPA $h$
scaling a deployment $d(h)$ with the operator's target $x^{op}_h$, the target written is

$$x_h(t) = \begin{cases} \text{the bowl's (or the allocation law's) target} & d(h) \in \mathcal{S} \\ x^{op}_h & d(h) \notin \mathcal{S} \end{cases}$$

The probe's position $p$ is a statement about $\mathcal{S}$ alone. A push on a muscle outside $\mathcal{S}$ answers no
sensed error and adds pods that compete with $\mathcal{S}$ for the same machines (the run's pending pods and failures).
It is the GPU law's own rule, applied to Kubernetes: where Omni-Compass cannot sense, it stands at native's own setting.

**2. Pods owed to a growing demand stay (the churn cause).** Let $u(t)$ be the CPU the workers use and $W$ the HPA's
scale-down window ($W = 300$ s unless the operator set one). The demand is *still growing* when

$$G(t) = \Big[\, u(t) > (1 + \epsilon)\, \min_{t - W \le s \le t} u(s) \,\Big], \qquad \epsilon = 0.05 .$$

After a breach the bowl lowers the target to the bottom of its cover, $x = x_{lo} = 0.6\,x^{op}$ (more pods, at once).
Before this amendment, the first decision with the position back under the centre, $p < c = 0.4$, no breach and no
pod waiting, returned $x = x^{op}$ at once. Under a rising load the autoscaler then removed the extra pods one window
later and started them again at the next step: the run's churn. The return is now

$$x \leftarrow x^{op} \quad \text{only if} \quad p < c,\ \ \text{no breach},\ \ \text{no pod waiting},\ \ \neg G(t),$$

and while $G(t)$ holds the target stays where the breach put it. A fault or a spike that has passed has a flat or
falling $u$, so $G$ is false and the operator's target returns at once, as the fault test requires (set 31 F:
HPA replicas under faults −1.1%); only a demand still climbing keeps its pods. $\epsilon = 0.05$ is set above the
decision-to-decision noise of the node CPU reading. A rise too small to clear it leaves the rule as it was before this
amendment (the target returns at once), so the correction can remove churn but cannot add any.

Nothing else changes: the bowl's band, gains and centre, the verdict, the fail-up rules, the release gate and the
node-pool law are as registered. Tests: `tests/test_bowl_controller.py`, cases *demand* and *sensed*, beside the
existing *fault over*, *blind* and kill-switch cases.

**The re-runs**, on the commit that carries this amendment, unchanged in design: the capacity test (`load_steps` 1 to
8, 1,600 s), the fairness test (`two_app` 1, 900 s) and the fault test (`faults` 1, 900 s), 10 paired repetitions
each, arms native / omni / bowl. The second application is now probed and reported as before, and its HPA is held at
the operator's target. Labelled by the one rule. Every number, whatever it says, is published beside the runs above.

## The re-runs under the amendment: results (2026-10-04)

All three on commit `199f350`, 10 paired repetitions each, the design unchanged.

- **Fault test, set 32 F** (`results/live/FAULTS_32.md`, run 37162459956): **no measure significantly worse under
  either law.** The bowl law recovers from a lost machine 58% faster and starts 34% fewer pods; the amendment left the
  fault behaviour of set 31 F intact.
- **Fairness** (`results/live/FAIRNESS_2.md`, run 37162458834): **correction 1 holds.** With the bowl law php-apache's
  failed requests are no longer worse (−14.0%, not significant; before +26.0%), pending pods −10.5% (before +65.2%);
  the neighbour unharmed under both laws. The bowl law's response-time gains in this test are no longer significant.
  Still worse under both laws: the mean pod start wait (+1.1 s bowl, +1.7 s allocation law).
- **Capacity** (`results/live/CAPACITY_2.md`, run 37162457542): the bowl law served **24.6 against native's 16.2
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
same factor so each pod stays as busy, $x = g\,x^{op}$; 114% with the bowl law, 190% with the allocation law). The
autoscaler then removed pods (14 with the bowl law, 35 with the allocation law, over ten repetitions), and the next
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
not the node's CPU. Tests: `tests/test_bowl_controller.py`, case *steady*.

The capacity, fairness and fault tests are run again on the commit that carries this amendment, unchanged in design,
and published beside the runs above whatever they show. The bill run on Azure (`aks-metered`, run 37171672509)
started on commit `199f350`, before this amendment, and is reported as of that commit.

## The third amendment, and a change considered and declined (2026-10-04, before the next runs)

**4. A lower target is never held.** Until now every new HPA target, in either direction, was held for one autoscaler
window $W$ while the line was clean, so on a step up the bowl's push (a lower target, more pods) could wait up to $W$
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

A narrower form was proposed the same day (`docs/proposals/AMENDMENT_RISING_STEP_CAP.md`): while the demand rises and a
pod of the sensed service is pending, raise `maxReplicas` by the pending count and lower the target to match. It is
declined for a mechanical reason as well as the one above. The replica cap does not make pods pending: at the cap the
autoscaler simply asks for no more pods, so the pending count there is zero and the write would never fire where it is
aimed. A pod is pending only when the scheduler finds no machine with room for it, and more places under the cap give
such a pod nowhere more to go; the answer to that is a machine, which the bowl already asks for. The part of the
proposal that holds, asking for pods at once on a step up instead of after a window, is rule 4 above.

On the CPU fill (used over allocatable about 0.10 in every arm): on kind every worker reports all of the host's cores
as its own, so the allocatable counts the same cores once per worker and the fill reads far lower than the machine
doing the work. Every receipt from the next runs on carries the host's own busy share and core count
(`host_cpu.csv`, `tools/live_reps.py`), so the room left on the real machine is measured, not inferred.

The capacity, fairness and fault tests are run again on the commit that carries this amendment, beside the runs of
commit `5d2e238` (rule 3 alone), so each rule's effect stays separable.

## The second amendment's runs: results (2026-10-04)

`results/live/AMENDMENT_2_RUNS.md`, commit `5d2e238` (rule 3 alone), 10 paired repetitions each.

- **Capacity: no measure significantly worse under either law.** Bowl law 24.6 against native's 17.4 requests a
  second, +41.4% (+5.4 to +9.0); allocation law 25.2, +44.8% (+4.9 to +10.7). The bowl law's pods started 5.7 against
  4.1, interval −0.64 to +3.84: no longer significant. Rule 3 removed the significant pod-start excess and lifted the
  allocation law's capacity from +0.0% to +44.8%.
- **Faults: no measure significantly worse under either law.**
- **Fairness: the bowl law, no measure significantly worse for either application.** The allocation law: php-apache
  much better, and the neighbour's failed requests **+0.74 points (+0.19 to +1.28), significant**. The allocation law
  conveys idle CPU to the service it senses; on machines shared with a surging neighbour that CPU is the neighbour's
  headroom. The allocation law is not labelled better in this test.

**Standing after rule 3: the bowl law is clean in all three tests** (no measure significantly worse, capacity +41.4%).
Rule 4 (a lower target never held) runs next on commit `583c97f`, beside these, to see whether it adds capacity without
costing a row.

## The fourth amendment: the replica cap as a lever the operator grants (2026-10-04, before its run)

The founder's instruction: no number in the harness is hard-wired; every one moves where the system lets it. The cap
of 10 in `deploy/kind/demo.yaml` is the value of Kubernetes' own php-apache example, not a choice of any operator, and
an earlier session read it as an operator's bound. It becomes a lever, under the operator's grant.

**5. Replica room.** With `--replica-ceiling` $N_{\max}$ granted (0, the default, leaves the cap untouched), for a
sensed HPA under the bowl law, with $r$ the pods running, $c$ the cap, $\bar{u}$ the pods' mean utilisation and $x$
the target, the autoscaler's own arithmetic asks for $n = \lceil r\,\bar{u}/x \rceil$ replicas, and

$$c \leftarrow \min(N_{\max},\, n) \quad \text{if } r \ge c,\ n > c,\ p \ge \text{centre or the line is breached};$$
$$c \leftarrow c^{op} \quad \text{if } n \le c^{op},\ p < \text{centre},\ \text{no breach},\ S(t).$$

The cap is raised only while it binds and the line is threatened, to what the autoscaler asks and never past the grant,
and returns to the operator's once the demand has held still for a window. The operator's range is recorded before
the first change; the kill switch restores it. Tests: `tests/test_bowl_controller.py`, case *room*.

**Its run** (a setting of its own, labelled as such): the capacity test unchanged, `replica_ceiling` 30, beside the
runs without it. Native keeps its cap of 10, as an operator who has not raised it would; the extra pods the bowl uses
are counted in the HPA replicas row, so the receipt shows what the capacity cost in pods, not the gain alone.

## The third and fourth amendments, and the bill on a real cloud: results (2026-10-04)

**Rule 4** (`results/live/AMENDMENT_3_RUNS.md`, commit `583c97f`): **the bowl law has no measure more than 2% worse in
any of the three tests.** Capacity +48.1% (+5.7 to +9.9), nothing worse; fairness, neither application worse (energy
per core-hour on the declared standby model +1.5%, inside the allowance); faults, nothing worse, lost-machine recovery
−61%. The allocation law: capacity +55.6%, nothing worse; in fairness the neighbour no longer worse. The first runs with
the real machine metered: a 4-core GitHub runner 48% to 70% busy, where kind's "used / allocatable" reads 0.07 to 0.10.

**Rule 5, the replica lever** (`results/live/REPLICA_ROOM.md`, commit `2101c3d`, ceiling 30): the bowl law served 24.6
requests a second, the same as without the lever, with 78% more pods and 26 pod starts against native's 4.6, both
significant. **The replica cap was not what limited the service; the machine doing the work was.** The lever stays,
off by default, as the operator's to grant where machines have room; it is not part of Omni-Compass's default setting
and this setting is not labelled better.

**The bill on a real cloud** (`results/live/AKS_BILL.md`, run 37187059424, commit `5b2832f`, four paired repetitions):
**no difference in the bill either way** (allocation law −0.6%, bowl law +0.8%, intervals across zero) and no measure
significantly worse. Azure's own autoscaler already ran the workload on about 1.86 of 4 workers, so this light
workload leaves no machine to give back. The machine savings measured on kind, where native has no node autoscaler, do
not carry to a cloud with one at this load; that is the reading of record. The preregistered size `Standard_D2s_v5` is
not allowed in the subscription's region; `Standard_D2s_v4` (same 2 vCPU, 8 GiB and list price) was used. Three
earlier attempts stopped at the load generator's placement before any measurement and are not results.

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
