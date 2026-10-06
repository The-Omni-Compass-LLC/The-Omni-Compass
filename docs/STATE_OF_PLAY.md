# Omni-Compass: state of play (read this first)

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Protected by copyright, patents and trademarks: Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Current facts only. Earlier states, failures and chronology are kept whole in `docs/HISTORY.md`. The release this page
describes is identified by `RELEASE_MANIFEST.json` (commit, fingerprints of the engine, the C++ twins, the GPU protocol,
the live evidence and the verification receipt), which `verify.py` checks against the files.

**Rerun everything:** `pip install -r requirements.txt && python verify.py` ends with `VERIFICATION: PASS`.

## In one paragraph (2026-10-06, Omni v1)

**Omni v1, confirmed three times.** On real Kubernetes, every test ran three times as separate GitHub runs on the frozen
engine, ten pairs each (`docs/OMNI_V1.md`, the six `results/live/V1_*.md` tables). Work inside the response line **+42%
to +48%** in all three runs of the all-four test (18.6 → 27.6 requests a second in run A), confirmed better; the 95th
percentile **−57% to −69%** in every run of the steady, wandering, all-four and fault tests, confirmed better; failed
requests −12% to −13% where load swings, confirmed better; machines −1.5% to −3.4% at steady load and −15% to −24% on
the batch queue, confirmed better, no difference beyond the noise elsewhere; energy a declared model (kind never powers a
machine down); beside a noisy neighbour, no difference beyond the noise on every row. The paragraph below is the earlier
engine's reading, kept as the record it was.

Omni-Compass sits on top of Kubernetes and hardware and gets more out of what is already there. On real Kubernetes,
the engine before v1 (the live controller at rules 1-8, commit `353903683009`), ten pairs per test, native against
compass with the same work sent to both:
**41.7% more work handled inside the response line on the same machines** (capacity, all four in one run), responses
**59-64% faster** at the 95th percentile (steady, wandering, all four, faults), 12% fewer failed requests where load
swings, energy equal or lower, and not one pod left without a machine. Machines: up to 2% fewer. Omni gives a machine
back only when a paired trial shows the service no slower without it, and on these clusters one machine fewer made
requests 30-45% slower in most trials, so it kept them and spent them on speed and work (earlier engines without that
check parked 29-36%: `docs/history/`). All of it together, real machines only: **the Omni index +12.9%**
(`results/OMNI_INDEX.md`).

**Omni v1** (`docs/OMNI_V1.md`): the engine is frozen and fingerprinted (`OMNI_V1.json`), and every test above runs
three times on it, as separate GitHub runs (A the result, B and C the replications); each table reads confirmed better,
confirmed worse, no difference beyond the noise, or the runs disagree, and replaces the earlier engine's table as it
lands. Running on v1 now: the Kubernetes suite three times, the batch test, the six organisms at 1, 10, 100 and 1,000
copies with the real cluster inside, the big organisms on rented Azure machines, the Azure steady and burst bill tests,
CityLearn, and the power grid.

**What is shown and what is not.** Shown: more work inside the response line on the same machines (34-52% across the
three capacity runs on earlier engines) and a faster tail, on real Kubernetes. Not yet shown: an energy or cloud-bill
saving on real machines. On kind the machines are containers on one runner, so a machine out of service saves modelled
watts, not a metered bill, and Azure's bill did not move on the earlier engine (`results/live/AKS_BILL.md`); the v1 Azure
runs are the test of that. The current card governor has not run on a real GPU.

The card: the first real run (NVIDIA A10, 2026-10-02) used a card controller since replaced; it is not a result to
stand on. In simulation the current controller (amendment 12) is clearly faster under an operator's power cap (p95
6-7% faster, time over the line 1 point lower) and saves 0.5-3.7% energy on the card's own firmware with p95 even
(`results/sim/gpu_two_wire/`). The real card runs next: one card, the card inside the six organisms, then eight cards.

The 656 muscles are models of real control systems. With the real cluster or the real card inside, they show the
mechanism (work the same, energy 0.1-0.2% lower, time over the line lower than native in every organism); they are
never counted in the headline.

| Test (real) | Work | Speed | Machines | Energy | Source |
|---|---|---|---|---|---|
| All four in one run: load up and down one step at a time, 10 pairs | **+29%** | p95 -62% | **-3.6%** | -0.3% | `results/live/ALL_FOUR.md` |
| Capacity, load rising, 10 pairs | **+48%** | p95 -50% | -1% | -0.3% | `results/live/AMENDMENT_3_RUNS.md` |
| Sets 22-27, same work, 10 pairs each | same, none failed | p95 -55% to -65% | **-29% to -36%** | -0.1% to -0.5% | `results/live/LIVE_REPS_22.md` to `results/live/LIVE_REPS_27.md` |
| Six organisms, cluster inside, 5 pairs each | requests served +0.5% to +6% | p95 -24% to -40% | same to -2% | -0.1% to -0.6% | `results/live/SIX_KUBE.md` |
| Azure AKS, steady load, 5 pairs | same | p95 -20% | same | (billed) same | `results/live/AKS_BILL.md` |

All four in one run is done: every one better and proven in the same run (`results/live/ALL_FOUR.md`). Running now: demand that wanders (up, spike, down, back up,
idle, 10 pairs), the Azure burst bill test, and the 1,000-copy grid of the six organisms on Lambda.

## The engine now, and what runs on it (2026-10-05)

The live controller is frozen at rules 1-8 (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendments 1-8): rules 5-8 were added
today (a pinned gauge is not a steady demand; coasting; cruise; the emergency brake). Every result above was measured on
an earlier version of the controller, and each names its commit. So that every number comes from one engine, the whole
Kubernetes suite runs again on the frozen engine: all four in one run, demand that wanders, the steady same-work set,
the fault and fairness tests, the batch test, and the six organisms at every size; the Azure burst bill test and the two
big organisms on rented Azure machines too. The card harness changed only in how it judges (amendment 11 of the GPU
preregistration), so the single card and the eight cards run once, on this engine, on Lambda.

Back on the frozen engine so far, ten pairs each:
- **Faults** (`results/live/FAULTS.md`): p95 −60%, mean response −35%, time over the line −23%, pending pods −77%.
  Recovery is faster after every fault: machine down 42 s against 70 s, a blind probe 54 s against 66 s, a runaway pod
  98 s against 105 s, a spike the same.
- **Fairness** (`results/live/FAIRNESS.md`): a noisy neighbour on the same cluster. Mean response −15%, nothing worse,
  and the neighbour's own app no worse. The earlier engine scored −0.3% on the index here; this engine scores +5.6%.

Independent simulator: CityLearn round 1 split (the 2022 battery districts better on bill -4% to -11%, electricity -9%
to -17%, carbon -7% to -14%; the 2020-2021 water-tank districts worse on peaks and ramping), the fix (only the electric
batteries are steered), and round 2 on every untouched district (`docs/CITYLEARN_PREREGISTRATION.md`).

## Measured on real systems: the newest set, Omni-Compass against Kubernetes as it runs today

**Set 24 (2026-10-02, commit `c908054`) repeats it again: machines in service −31.6%, p95 −60.1%, p99 −64.1%, HPA
replicas −38.6%, 0 failed requests, total CPU including Omni-Compass's own −1.8% (not significant)**
(`results/live/LIVE_REPS_24.md`). Set 23 before it: p95 −62%, replicas −37%, pod starts −64%, 0 failed requests, no
energy or total-CPU difference (`results/live/LIVE_REPS_23.md`). The set-22 table below stands as first measured.

Set 22 (`results/live/LIVE_REPS_22.md`): 10 paired repetitions on real Kubernetes (kind), each pair on one machine,
Kubernetes with its autoscaler alone against the same Kubernetes with Omni-Compass on top. The load is sent at a fixed
rate, so both arms were given **the same work**.

| Result | Kubernetes alone | With Omni-Compass | Change (95% interval) |
|---|---:|---:|---|
| **Energy, parked machines still on at idle power** (declared model, no meter) | 160.3 Wh | 160.1 Wh | **−0.1%, no difference** |
| **Response time, 95th percentile** | 407.9 ms | 158.8 ms | **−61%** (proven) |
| Response time, 99th percentile | 639.4 ms | 245.1 ms | −62% (proven) |
| Response time, mean | 179.9 ms | 98.4 ms | −45% (proven) |
| Failed requests | 0 | 0 | equal |
| Pods waiting to start, pod-minutes | 0.265 | 0.025 | −91% (proven) |
| Replicas, mean | 8.93 | 6.91 | −23% (proven) |
| Machines in service, mean (all stayed powered) | 6 | 4.14 | −31% (proven) |
| CPU used by the service | 1.036 cores | 0.957 cores | −7.6% (proven) |
| Omni's own CPU (its controller and every command it ran) | 0 | 0.070 cores | +0.070 (proven) |
| **CPU used, service and Omni together** | 1.036 cores | 1.026 cores | **−0.9%, no difference** |

- **Same work, much faster answers**, with no failed requests and far less waiting.
- **No energy saving is shown on kind.** Every machine stays powered; energy is a declared model, and counted at the
  idle power a parked machine really draws it is unchanged.
- **No CPU saving once Omni's own cost is counted.** The service used 7.6% less CPU; the controller spent almost all
  of it. Cutting the controller's cost is the next improvement.
- The reset restored every setting in every run.

## Kubernetes sets 25 and 26 (2026-10-02, 10 paired repetitions each, equal work)

| Run | Machines in service | p95 | Failed | Total CPU incl. Omni's own | Receipt |
|---|---:|---:|---:|---:|---|
| Set 25, the engine's allocation law | **−32.3%** | **−57.3%** | 0 / 0 | −0.6% (not significant) | `results/live/LIVE_REPS_25.md` |
| Set 26, the engine's allocation law | **−35.8%** | **−55.4%** | 0 / 0 | −1.5% (not significant) | `results/live/LIVE_REPS_26.md` |
| Set 26, **the compass law in the live controller** | **−17.2%** | **−64.8%** | 0 / 0 | +1.0% (not significant) | same; label by the preregistered rule: **better on machines within the band** |
| Set 27, the engine's allocation law | **−36.6%** | **−53.1%** | 0 / 0 | −0.0% (not significant) | `results/live/LIVE_REPS_27.md` |
| Set 27, **the compass law aligned with the GPU governor** | **−15.9%** | **−65.5%** | 0 / 0 | +0.2% (not significant) | same; label by the preregistered rule: **better on machines within the band** |

Set 27 (running): the compass in the live controller reads the service as the corrected GPU compass does (mean response time,
center 0.4), against native and the allocation law (`docs/K8S_COMPASS_PREREGISTRATION.md`).

## Measured on a real GPU: the card's own meter (evidence class P)

**First confirmation, NVIDIA A10 on Lambda, 2026-10-02** (`results/gpu/run-20261002T082232Z/GPU_REPS.md`, 10 paired
repetitions × native / watch / Omni, 600 s each, frozen at commit `c908054`, checksums verified). Wire check 7 of 7;
2,144 writes, none refused, every one read back, every arm ended at the start limit; watch equal to native.

| Gauge | Native | Omni | Change (95% interval) |
|---|---:|---:|---|
| **Work per energy** (requests per kJ) | 50.79 | 52.62 | **+3.6% (+2.7% to +4.5%), proven** |
| GPU energy | 69,180 J | 66,790 J | −3.5%, proven |
| Requests served / not served | 3,514 / 0 | 3,514 / 0 | equal |
| **Response time, 95th percentile** | 510 ms | 809 ms | **+58.5%, worse, proven** |

**Result, by rule: ENERGY IMPROVEMENT WITH SERVICE TRADEOFF** (the p95 guardrail of +10% failed). The six organisms
with the same card inside (`results/hil/run-20261002T082232Z/HIL.md`, 3 repetitions each): the card's work per energy
+1.6% to +2.8% in every organism, the same requests, its p95 500 to about 600-935 ms. The cause, from the card's own
samples, was wiring in the governor (amendment 6 of `docs/GPU_PREREGISTRATION.md`): busy bursts served at 736-768 MHz
against 861-889 MHz on its own. Corrected (amendments 6 and 7); the corrected governor has not yet run on a card.

## Simulated (models: they show the mechanism, not a measurement)

| Result | Where |
|---|---|
| GPU governor with share floor and busy gate (one wire, the power limit), MLPerf-calibrated card: +5.1% and +1.3% work per kJ, p95 within +10% | `results/gpu/sim/after` |
| **Two-wire GPU card under the compass law, corrected governor** (amendments 6-7), 10 seeds and 10 fresh seeds, geometric means: **service** profile work per energy **+6.9% / +3.8%**, energy −6.4% / −3.7%, p95 **−5.9% / −2.3%** (faster), time over the line −0.03 / −0.04 pp; **batch** profile +8.1% / +4.2%, p95 +7.0% / −2.3%; the one-wire governor +0.1%; both wires restored every seed | `results/sim/gpu_two_wire/RESULT.md`, `fresh/` |
| **The six organisms** (Compute 345, Physics 262, Energy 282, Distribution 337, the four stacked 1,226, the whole tower 656), native against the compass law on every muscle, 1,000 paired runs at 1× and at 10× size: work per energy +0.20% to +0.30%, energy −0.21% to −0.32%, work −0.01% to −0.02%, time over the service line **+0.19 to +0.27 pp in every cell (band first not held)**, every knob handed back. 100× and 1,000× are running | `results/scale/GRID.md` |
| Speed lock (speed won elsewhere spent on GPU watts) | `results/gpu/sim/pipeline/` |
| CPU and GPU on one conserved power budget: +1.4% to +5.7% work served against a fixed cap, never over the budget | `results/hardware/NODE_EXCHANGE_*.json`, `docs/CONVEYANCE_LAW.md` |
| GPU groups sharing a site budget: 0 minutes over the budget | `results/hardware/SITE_EXCHANGE_HELDOUT_*.json` |
| Platform leagues, faults, PlanetLab traces, stack benchmark | `tuning/`, `results/protocol/`, `results/` (see `docs/history/BENCHMARK_REPORT.md`) |
| **The 656-muscle tower as organisms**, round 3 (preregistered, 10 seeds; every realm carries the shared spine; Omni as the shipped controller commands): the whole tower native against one governor on top, work per energy **+0.1%, SUPERIOR WITHIN GUARDRAILS**; inside the realms the spine costs service: Energy +0.2% with +1.9 pp violations (tradeoff), Compute 0.0% (+2.1 pp, not established), Distribution −0.1% and Physics −0.7% (**WORSE**). Rounds 1 and 2 kept, superseded | `results/realms/REALMS.md`, `docs/REALM_MUSCLES.md` |

## Verified in code

| Property | Where |
|---|---|
| The canonical engine is `symmetric_verified`; the printed chart is a named variant, not benchmarked | `docs/CANONICAL_ENGINE.md` |
| Nine laws twinned in C++20 and proven equal to the Python; sealed by fingerprint | `results/SEAL.json`, `tools/seal.py` |
| The conveyance law conserves its budget and converges (proof and 20,000 random systems) | `docs/CONVEYANCE_LAW.md`, `tests/test_conveyance.py` |
| Safety shield: 2,000,000 adversarial cases, 0 violations; C++ engine: 100,000,000 decisions, no failures | `tests/test_shield_properties.py`, `results/SOAK.json` |

## Open

1. **Band first.** In every organism and every size the compass law raises the time over the service line by about 0.2
   points. The rule is no win unless that is at or under native's. This is the first thing to fix in the law.
2. **The first real-hardware run:** `sudo bash scripts/gpu_rented_run.sh` on a rented NVIDIA machine (smoke, then the
   10 preregistered repetitions, `docs/GPU_RUN_GUIDE.md`), or the gpu-bench workflow on GitHub's GPU runner. Then a
   second machine of the same type, then another GPU type. Status 2026-10-02: the rented-card run above is under way. GitHub's GPU runner has never been
   assigned to a job (every run waited in the queue; the repository is public, so the ordinary runners are free while a
   GPU runner is always billed, and the account has an Actions billing notice). The envelope rule is preregistered
   (amendment 3).
3. **Work per energy on kind:** count requests served, or run an open-loop load at a fixed rate, so work per energy can
   be stated instead of estimated (set 22, `LOADGEN=open`).
4. **CPU and GPU on one power budget on hardware:** the law is simulated; the live exchange is not wired.
5. **A global stability proof** of the forced six-state system (`docs/FORMAL_STATUS.md`).
6. **The principal embodiment for filings** (`docs/CANONICAL_ENGINE.md`, section 5): a decision for the company.

## Where things are

| Path | What it is |
|---|---|
| `docs/INTEGRATION_MANUAL.md` | the manual in the box: wiring it in yourself, stack by stack |
| `docs/METRICS_CATALOG.md` | every gauge, and whether it is measured or modelled |
| `docs/COMPARISON.md` | against Kubernetes, OpenShift, Turbonomic, Borg, Twine and others |
| `docs/CANONICAL_ENGINE.md` | the one engine the software runs |
| `omnicompass/`, `cpp/` | the engine and its laws; the C++20 twins |
| `omni_controller/` | the Kubernetes controller, the GPU governor, the muscles |
| `results/live/` | every live run, including failed and withdrawn ones |
| `docs/HISTORY.md` | earlier states of play |

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
