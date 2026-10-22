# Omni v14: every clock in seconds, the full decision every 15 seconds

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 22 October 2026: the governor's full read of the state and its decision every 15 seconds, the pace of
the pod autoscaler it sits on, "with the clocks counted in seconds. Test 10S and never above 60", native or better, never
worse, and anything found worse fixed. Omni v14 is omni-v13 (`docs/OMNI_V13.md`) with every clock of the governor stated in
seconds, so that its decision period sets only how often it reads the state and never what a rule means, the default period
15 seconds, and the faults found on the way fixed. Its fingerprint is `OMNI_V14.json`. Every benchmark runs again on it, A, B
and C; every earlier table stands as its own engine's result, and results from two versions are never pooled. The readings
of the toy gate below are our own models (evidence class S), never a benchmark result. Run and scored by The Omni-Compass LLC's
own code. No outside party has reviewed or approved these results.

## 1. Why the governor decided once a minute

- **Native's clocks are its projects' own defaults.** The Kubernetes pod autoscaler recomputes every 15 s (the controller
  manager's `--horizontal-pod-autoscaler-sync-period`, default 15 s, kept by the managed clouds); the processor readings it
  uses are refreshed every 15 s (metrics-server's resolution); it waits 5 minutes before it removes pods (its downscale
  stabilization); the cluster autoscaler scans every 10 s and removes an unneeded machine after 10 minutes (2 in our Azure and
  Amazon scripts); KEDA polls every 30 s. No setup of ours changes the pod autoscaler's 15 s.
- **Ours was written in, never measured.** The first harness, of 26 September (commit `3b86a5163a`), has the governor
  "compute every minute"; the fleet law's constants were selected on the 15-second fleet harness with a decision every 60 s
  (`FLEET_DECISION_SECONDS = 60`, `omnicompass/adapter.py`), and the rules were written in decisions. On 14 October the founder
  asked for 15, 10 and 5 s. Omni v7 (16 October) restated six rules in seconds (`docs/OMNI_V7.md`, section 4) and kept 60 s
  as the default, because the engine core still advanced one fixed step a decision and the toy at 15 s read LOSS rows.
- **What still counted decisions on omni-v13**, each found in the code and fixed here: the engine core's step and its blend
  of each observation; the fleet law's dwell counts; the edge's window, narrowing, memory, wobble and lesson; the compass law's
  damping and velocity smoothing; the closure law's step; the conveyance's cadence; the shared host's busy reading; the
  modelled heat; the cold start's wait; the batch admission's and resumption's pace. At 15 s each ran four times as fast.

## 2. The rule

Let Δ be the decision period in seconds, Δ₀ = 60 s the period every constant was stated at, and r = Δ / Δ₀. Every quantity of
the governor is defined in seconds; Δ sets only how often the state is read. Each clock is one of four kinds.

1. **A condition held for T seconds** is held for n(T) = max(1, round(T / Δ)) readings (omni-v7). The readings span between
   (n − 1)·Δ and n·Δ of the condition, so the rule's time is met to within one period, nearer the faster it reads.
2. **A move away from native** (a machine given back, a held job admitted, a paused job resumed) goes at most once every
   T_move seconds, whatever Δ: one a minute. **A move toward native or toward safety** (fail up past the wall, a machine woken
   on a breach, the operator's target handed back, a job paused on heat, a trial abandoned) goes at the first reading that calls
   for it. A faster reading therefore reacts sooner and never takes anything away faster. **A move away from native that
   cannot be undone** is held to the longest horizon its own law states: in the cloud a machine given back is the cloud's to
   delete once it has stood empty for its scale-down time, and the governor never adds one, so it never gives back the
   machines the largest requests of the last R seconds need at its own headroom (the closure law's warm reserve, R = 960
   steps of the 15-second harness, 4 hours), and gives back nothing before it has read those R seconds.
3. **A filter or a memory** keeps its time constant: a factor λ₀ a reading at Δ₀ becomes λ(Δ) = λ₀ʳ; a blend that takes in the
   share a₀ of an observation becomes a(Δ) = 1 − (1 − a₀)ʳ; an integration step h₀ becomes h₀·r.
4. **An estimator that depends on the spacing of its samples** is stated in time: the wobble of the service is read from
   readings one response-time window apart (lag L = round(W / Δ), W = 60 s), so two readings that share requests never make the
   service look steadier than it is; the compass's damping is the critical damping of the rate its lever moves at (the target
   moves period / 60 of a step each decision, a rate a minute), so it is stated at Δ₀.

**The identity.** At Δ = Δ₀ every clock's value is omni-v13's: r = 1 leaves every factor, share, step, count and lag as it was
(`tests/test_clocks_in_seconds.py`), so wherever the cloud's rule (`--give-back-only`) is off, omni-v14 at 60 s is omni-v13 at
60 s, read for read and write for write. The three cloud fixes of section 4 (5, 6 and 7) act at every period, 60 s included.

**Convergence.** The engine core blends an observation in and then advances its equations, so the two are applied in turn
within a step. At a finer step the governor comes nearer the one path of the continuous engine: the same minute of telemetry
read at 60, 15 and 1 s leaves the engine nearer the 1 s path at 15 s than at 60 s (`tests/test_clocks_in_seconds.py`).

## 3. Every clock, mapped

| Clock | Where | omni-v13 (a reading) | omni-v14 (in seconds) | at 60 s | at 15 s | at 10 s |
|---|---|---|---|---|---|---|
| The engine core's step | `omnicompass/adapter.py` | 0.1 a decision | 0.1·r (the engine's own time, 0.1 a minute) | 0.1 | 0.025 | 0.0167 |
| Its blend of each observation | the same | 0.339 a decision | 1 − 0.661ʳ (time constant 145 s) | 0.339 | 0.0983 | 0.0667 |
| The fleet law's dwell counts | the same | 1 and 5 decisions | 60 s and 300 s | 1 and 5 | 4 and 20 | 6 and 30 |
| The edge's window | `omnicompass/edge.py` | 20 decisions | 1,200 s | 20 | 80 | 120 |
| The edge's narrowing | the same | 0.05 a decision | 1 − 0.95ʳ (5% a minute) | 0.05 | 0.0127 | 0.0085 |
| The edge's memory of a fall | the same | 0.9995 a decision | 0.9995ʳ (half-life 23 h) | 0.9995 | 0.999875 | 0.999917 |
| The edge's wobble | the same | readings a decision apart | readings 60 s apart | lag 1 | lag 4 | lag 6 |
| The edge's lesson from a fall | `omni_controller/controller.py` | 0.1 a decision | 0.1 a minute of fall | 0.1 | 0.025 | 0.0167 |
| The compass's damping k_d | `omnicompass/compass_law.py` | (2√(k_p τ/Δ) − 1)·Δ ×3 | stated at Δ₀: 180 s | 180 | 180 (v13: 135) | 180 (v13: 117) |
| Its velocity smoothing | the same | 0.3 a decision | 0.3ʳ (time constant 50 s) | 0.3 | 0.740 | 0.818 |
| The closure law's step | `omni_controller/controller.py` | every decision | once a minute; an add held between, nothing given back | every decision | every 4th | every 6th |
| The conveyance | the same | every third fast check | every 15 s of the governor's schedule | 15 s | 15 s (v13: 22.5 s) | 15 s (v13: 30 s) |
| The shared host's busy share (replica raise) | `omni_controller/capacity.py` | since the last decision | over the last minute | 1 interval | 4 intervals | 6 intervals |
| The modelled heat | `omni_controller/muscles.py` | 0.86 a decision | 0.86ʳ (time constant 398 s) | 0.86 | 0.963 | 0.975 |
| The cold start's wait | the same | 3 decisions | 180 s | 3 | 12 | 18 |
| A held job admitted, a paused job resumed | the same | one a decision | one a minute | 1 a minute | 1 a minute | 1 a minute |
| The warm reserve in the cloud (machines never given back) | `omni_controller/controller.py` | none | the largest requests of the last 14,400 s at the governor's headroom; nothing given back before 14,400 s are read | 240 readings | 960 readings | 1,440 readings |

Already in seconds since omni-v7 and unchanged: the breach's clear time 180 s, cruise 120 s, the strict window 300 s, the
give-back trial's spacing 600 s, its recheck 7,200 s and its phase 1,200 s; one machine given back a minute; the compass's move
of the autoscaler's target and coasting, a rate a minute; the pod reflex's window 30 s and the response-time window 60 s.

## 4. The faults fixed with it

| # | Fault on omni-v13 | Fix in omni-v14 | Found |
|---|---|---|---|
| 1 | At a period under 60 s the cushion in front of the line narrowed: its window covered fewer minutes, it narrowed and forgot faster, and readings that share requests made the service look up to twice as steady | the edge in seconds (section 3) | reading the code for the founder's question |
| 2 | The engine core's clock and its blend ran four times as fast at 15 s | the core in seconds | the same |
| 3 | The compass's damping was computed for the decision period while its lever moved at a rate a minute (omni-v7's step scale): at 15 s it was a quarter weaker | the damping at the lever's own rate | the same |
| 4 | The conveyance ran at every third fast check, so it slowed at shorter periods (22.5 s at 15 s, 30 s at 10 s) and never ran where the period was under the fast checks' own | every 15 s of the governor's schedule, at a decision or a fast check | the same |
| 5 | In the cloud the governor ordered machines that no longer existed (the cloud had deleted them); the order changed nothing, and the next decision read it as a command that did not land, which held every give-back until the cloud made a machine again | the order held to the machines that exist, open or idle | the toy gate's audits (382 such holds in one modelled day) |
| 6 | In the cloud a give-back was judged on the load of the moment only, while the cloud deletes a machine given back once it has stood empty for 10 minutes and the governor never adds one: a machine given back in a dip was gone when the requests came back, and pods waited for a new one (in the toy gate at 15 s and 10 s, pods waiting for a place +16% to +21% against native, LOSS; at 60 s the same rise, EVEN only by its spread) | the closure law's warm reserve, which the live governor had never wired: the machines the largest requests of the last 4 hours need, at the governor's own headroom, are never given back in the cloud, and nothing is given back before those 4 hours are read (an unread reading is never room); and no give-back trial starts while every machine in service is inside the reserve, so the verdict never counts a step it could not take | the toy gate's per-seed readings, traced minute by minute (seed 2: a machine given back at 12.8 h, deleted at 13.0 h, the requests above the four machines left from 13.5 h, 19 pods waiting 90 s at 14.45 h where native's autoscaler had kept five) |
| 7 | In the cloud the fast check between decisions ordered machines for pods that wait, though only the cloud adds a machine there: an order past the machines that exist changed nothing (a waiting pod already lands on an idle one) | the fast check's order held to the machines that exist, as the decision's (5) | the same per-seed audits |
| 8 | The toy gate's cloud took an idle machine's room away at once, as if drained, and gave its pods no machine, so the governor in the model never counted an idle machine still carrying work and missed the running pods' requests; pods waited in the model where they wait nowhere on a real cluster (the shipped actuator, `scripts/kind_nodepool.sh`: PreferNoSchedule, no pod moved, a pod that finds the open machines full lands on an idle one at once; the Azure receipts read pods waiting EVEN in all four sets) | the toy's cloud corrected to the actuator as shipped (`tools/toy_gate.py`) | the toy gate's per-seed readings |

The eighth is a fault of our model, not of the engine: the LOSS rows the model printed for pods waiting at 15 s on omni-v13
(+112%) were its own. It is corrected for both engines alike, and every reading in section 6 is on the corrected model.

## 5. What the period costs and gains

- **Noticing.** An event is read at worst one period after it happens and on average half a period: 60 s and 30 s at a
  decision a minute; 15 s and 7.5 s at 15 s; 10 s and 5 s at 10 s. The fast checks (every 5 s) are unchanged.
- **Reading.** Full reads of the state an hour: 3,600 / Δ, so 60, 240 and 360; each lists every machine, pod and autoscaler.
  The governor's own processor is measured in every run (Omni's own CPU, cores; 0.008 to 0.019 cores in the omni-v12 tables at
  a decision a minute with fast checks every 5 s).
- **Freshness.** The processor readings refresh every 15 s, so at 15 s every full read is new and at 10 s two in three; the
  response times and the pods waiting refresh with every request and event.
- **Never above 60 s.** Above a minute a reading covers only part of the time since the last (the response-time window is
  60 s), so the cushion's statistics would never see some of the requests; the rig refuses a period over 60 s or under the
  fast checks' own (`scripts/kind_bench.sh`).
- **No faster than the muscles answer.** A pod starts in 8 to 12 s on kind and the autoscaler syncs every 15 s; a period under
  that reads states the last move has not reached yet. Every move away from native is paced in seconds (section 2) and the
  release gate holds a machine while its last command has not landed, so a faster reading cannot stack moves.

## 6. The toy gate against omni-v13

To be filled from `results/toy_gate/V14_VS_V13.md`.

## 7. What stays omni-v13's

Every gain, guard, preset, muscle, band and threshold; the verdict and its interval; the closure law's setting; the GPU
governors (their own 2 s loop); the realms' arms (their own ticks); the fleet harness's arms. Engines before omni-v14 ran at a
decision a minute, and their tables stand as their own.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
