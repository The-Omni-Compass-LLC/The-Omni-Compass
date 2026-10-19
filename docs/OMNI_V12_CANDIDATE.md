# Omni v12 candidate: two faults fixed, waiting for the founder's word

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This branch, `v12-candidate`, is omni-v11 (`docs/OMNI_V11.md`, digest `745aa53ec8eeb67b`) with two faults fixed. The faults
were found on the omni-v11 runs and in our own reading of the code on 19 October. It is not the engine that stands. omni-v11
stays on main until the founder says "land v12" (`docs/CHANGE_CONTROL.md`, rule 6). Then `tools/land_engine.py v12` writes
the fingerprint, the version list and the campaign, and every benchmark runs again on it. Nothing here is a benchmark result.
The readings below are our own models (evidence class S), run on our own machine. Run and scored by The Omni-Compass LLC's
own code. No outside party has reviewed or approved these results.

| # | Change | Where | The fault it fixes |
|---|---|---|---|
| 1 | A raise the cluster's admission refuses is not written again until the pod's limit changes, the raise shrinks, or a wait passes (5 minutes, doubled at each refusal up to an hour) | `omni_controller/muscles.py`, the conveyance | omni-v11 capacity test: admission refused every CPU-limit raise (`exceeded quota: omni-cap`) and the governor wrote it again at every fast check, about 9 refused writes a minute, 970 to 1,000 an hour (`results/STEERING.md`) |
| 2 | The swarm's proximity reflex hands back the planner's cruise in the tick it is triggered; its reach grows with the square of the speed (0.5 m at the planner's cruise, as before) | `tools/run_swarm.py`, `Drone.step` | the omni-v11 reflex let the override fall 0.01 a tick, so a drone kept flying fast about a second after it saw a neighbour; on one mission draw outside the counted cells two drones came within 0.083 m (`results/toy_gate/V12_SWARM_REFLEX.md`) |

## 1. The refused raise

On the kind rig the governor's role could not read the namespace's quota. As written, an unreadable quota is "no budget
known", and the cluster's admission is the authority. Admission refused each raise, and the refusal was read back and audited,
so nothing wrong was ever set. But the governor asked again at every fast check. The table read EVEN, and the service was never
touched, but a governor that repeats a refused command every few seconds hammers the API server. Fixed: the refusal is the
authority's answer. The same raise is held until something changes: the pod's limit (someone else moved it), a smaller raise
(the budget moved), or the wait (5 minutes, then 10, 20, 40, 60, never longer). An accepted raise clears the hold. The audit
records each hold and its wait (`held_s`).

The toy gate (`tools/toy_gate.py`, the `convey_refused` toy: the quota unreadable and every raise past the operator's limit
refused, seeds 1 to 8): the candidate wrote **49.75 commands a day against omni-v11's 1,985.5 (−97.5%, GAIN)**. Every other
gauge was identical to omni-v11's to the last digit: requests served, pod start wait, p95, alert minutes, host busy, CPU given
and pod-seconds. On the convey toys with a readable quota and with an unreadable quota that admission accepts, the candidate
and omni-v11 are identical on every gauge. Tests: `tests/test_refused_raise.py`.

## 2. The swarm's reflex

`results/toy_gate/V12_SWARM_REFLEX.md` holds the whole reading on gym-pybullet-drones, an outside simulator, on the counted
cells and on mission draws the wire was never run on. With the fix, every drone stays at or outside the keep-out on every cell
and draw tried, and 49% to 92% of omni-v11's energy cut is kept. That is the price of the reflex acting at once: on the long
cell the energy cut falls from −19.8% to −14.5% against native.

## 3. Studied and left out: the verdict's upper end (branch `v12-verdict-study`)

The toy gate's verdict toy: give-back steps that truly cost 0 to 5% more, against a 2% allowance, on lognormal work (log
spread 0.25), 300 seeds.

| True extra cost of the step | omni-v11, 20 pieces of work a decision | candidate, 20 a decision | omni-v11, 200 a decision | candidate, 200 a decision |
|---|---:|---:|---:|---:|
| +0% (free) | 60% kept | 0% (never started) | 66% kept | **98% kept** |
| +1% | 50% | 0% | 53% | 43% |
| +2% (the allowance) | 39% | 0% | 40% | 4% |
| +3% | 28% | 0% | 26% | **0%** |
| +5% | 14% | 0% | 7% | **0%** |

Where the work arrives fast enough to read a 2% step in a trial's time, the candidate keeps a free step more often than
omni-v11 does (98% against 66%), and it never keeps a step past the allowance (3% and 5%: 0% against 26% and 7%). Where the
work is too slow, the trial is not started and the knob stays native.

**The price, said before any run.** The data-store wires feed the verdict one cost sample a second, and each phase of a trial
has 40 decisions (MySQL 120). We read the spread of every reference phase in the omni-v11 data-store audits (runs A, B and C of
`V11_SYSBENCH`, `V11_PGBENCH`, `V11_YCSB`, `V11_REDIS` and `V11_KAFKA`). Each workload would need **432 to 23,430 samples a
phase** (PostgreSQL 432 to 695; MySQL 3,115 to 6,157; MongoDB 1,003 to 19,358; Redis 1,134 to 18,747; Kafka 13,411 to 23,430).
That is far more than 40 or 120. Under the candidate, no data-store trial would start in those benchmarks: every data-store
knob would stay native, and the data-store GAIN rows would read EVEN. The rule keeps a hidden cost out. It also gives up those
gains until a wire can measure long enough or less noisily. The founder decides between the two. The same holds on the toy
cluster, which is set from a real run's regime: the governor reads about 80 requests a decision and the rule needs about 4,000
a phase, so 1,102 of the candidate's give-back trials were never started, no step was allowed, and the governor read identical
to native on every gauge, the machine-hour cut and the energy per core-hour cut of omni-v11 gone (the cluster toys of the
three-change candidate, seeds 1 to 8, `results/toy_gate/V12_VS_V11.md`). The rule as written is therefore not in the candidate:
`omnicompass/verdict.py` is omni-v11's bytes, and the rule is kept on the branch `v12-verdict-study`. The fault it answers stays on
the next version's list until a trial design that reads a 2% step in a trial's time is shown in the toy gate.

Tests: `tests/test_verdict_upper.py`, on the study branch.

## 4. The toy gate against omni-v11

`results/toy_gate/V12_VS_V11.md` (seeds 1 to 8; the cluster toys at 60 s and 15 s and with the blink, the three convey toys and
the verdict toy at 20 and 200 pieces of work a decision): the two-fix candidate reads **identical to omni-v11 on every gauge of
every toy but one**, the convey toy whose every raise is refused, where it writes 49.75 commands a day against 1,985.5 (−97.5%,
GAIN). No reading of the candidate against omni-v11 is a LOSS. The standing engine's own readings against native in these toys
are omni-v11's and unchanged by the candidate. The same record shows, under each cluster table, the candidate as first pushed
with the verdict's upper end: identical to native, no give-back trial started (section 3).

What landing needs, once the founder says "land v12": `tools/land_engine.py v12 --since <UTC>` (the fingerprint, the version
list, the conductor's campaign, the package 0.12.0), `docs/OMNI_V12.md` from this page, the words on every page that names the
engine, both manuals rebuilt, the release manifest at 0 FAIL, and every benchmark run again on it, A, B and C.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
