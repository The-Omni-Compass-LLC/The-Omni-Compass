# Omni v16: every clock of the governor in seconds, the decision pace a clean setting (candidate)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v16 is built on the branch `v16-candidate` on the founder's word of 22 October ("Go"), on the plan put to him that night:
put every clock of the Kubernetes governor in seconds, read the decision pace at 60, 15, 10 and 5 s in our own models, run
each pace three times on GitHub's own machines, and let the fastest pace with no LOSS and little cost become the default
(`docs/PACE_PREREGISTRATION.md`). It is omni-v15 (`docs/OMNI_V15.md`) with the clocks changed and nothing else: every gain,
guard, preset and muscle is omni-v15's. Read in the toy gate against omni-v15 on the same seeds before any run
(`results/toy_gate/V16_VS_V15.md`), and the pace read alone on a plant that moves every 5 s
(`results/toy_gate/V16_PACE.md`). The readings from the toy gate are our own models (evidence class S), never a benchmark
result. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## Why

Every engine through omni-v15 took its full decision every 60 s. The number was written into the first harness on 26
September, with no reason recorded, and never measured against another; the engine was then tuned at 60 s and several of
its rules were written in decisions, which locked 60 s in. Native's pod autoscaler checks every 15 s, the metrics it reads
refresh every 15 s, the Cluster Autoscaler scans every 10 s, KEDA every 30 s. The founder asked for 15, 10 and 5 s on 14
October; six rules moved to seconds on 16 October (omni-v7) and the rest did not, so turning the period also changed what
the remaining rules meant. omni-v16 finishes the job: turning the period changes only how often the governor looks.

## What counted in decisions, and what it counts now

Every value below is the one omni-v15 used when a decision comes every 60 s (the reference step; `REF_PERIOD_S`).

| Clock | omni-v15 (per decision) | omni-v16 (per second) | Where |
|---|---|---|---|
| the brain's blending of each reading | 0.339 of the state a decision | 1 − (1 − 0.339)^k a decision, k = period / 60 s: 0.339 a minute | `omnicompass/adapter.py` (`Governor.step`, `period_s`) |
| the brain's inner time | 0.1 of its macro interval a decision | 0.1 k a decision | the same |
| the brain's dwell and wait before giving a machine back | 1 and 5 decisions (the fleet law) | the same seconds: 60 and 300 s | the same |
| the brain's machines added or removed | up to 8 and 1 a decision | up to 8 and 1 over the last minute's decisions | the same; the C++ twin `cpp/src/governor.cpp` identically |
| the compass's damping (kd) | critical damping for the decision period | critical damping at the minute, so the law's push and pull per second are the same at any period | `omni_controller/controller.py` |
| the compass's velocity smoothing | 0.3 a decision | 0.3 a minute | the same |
| the edge's window, narrowing, the floor's forgetting, memory, wobble step | 20 decisions; 0.05, 0.9995 a decision; one decision's change | 20 minutes; 0.05, 0.9995 a minute; a minute's change | `omnicompass/edge.py` (`pace`) |
| what a breach teaches the edge | 0.1 a decision of breach | 0.1 a minute of breach | `omni_controller/controller.py` |
| machines added past the scheduling floor | one step a decision | one step a minute (the release has been one a minute since v7); the floor's machines at once | the same (`ADD_PERIOD_S`) |
| a command's time to land (proprioception) | the next decision | a minute, every decision reading it until it lands | the same (`LAND_S`) |
| the host's busy share (kind's shared runner) | since the last decision | over the last minute | `omni_controller/capacity.py` (`span`) |
| the heat law | 0.86 of the heat kept a decision | 0.86 a minute | `omni_controller/muscles.py` |
| held batch jobs admitted; jobs paused or resumed | one a decision | one a minute | the same |
| a quiet deployment scaled to zero | 3 idle decisions | 180 idle seconds (`--coldstart-idle-s`) | the same |
| the coast toward fewer pods | coast step × period / 60 a raise | the coast step a raise (a raise comes at most once a window) | `omni_controller/controller.py` |
| the conveyance | every third fast check, never at a decision (so never at a decision every 5 s) | every 15 s, whichever check falls due (`--convey-every-s`) | the same |
| the loop | each wait began when the step ended (a 60 s decision came every 62 to 67 s on kind) | keeps its own schedule; a missed slot is skipped, never run in a burst | the same (`main`) |

Six rules already counted seconds since omni-v7 and stay as they were: the line's clear time, cruise, the strict window,
the trial spacing, the wait after a refusal, and a trial's length; so does the release of one machine a minute.

## At 60 s it is omni-v15

On the toy cluster at a decision every 60 s, omni-v16 makes exactly omni-v15's decisions: 4,578 audit records, none
different (seed 1; the gate's eight seeds read every gauge identical). The brain's C++ twin equals the Python at 60, 15, 10
and 5 s (`tests/test_cpp_governor_parity.py`, 4,320 directives each, no difference). Two changes can be seen at 60 s on a
real cluster and nowhere else: the conveyance comes every 15 s exactly (omni-v15: about 3.7 passes a minute), and the
loop keeps its schedule (omni-v15's decisions drifted by the steps' own time).

## The pace

(Filled in from `results/toy_gate/V16_PACE.md` and the three runs of `docs/PACE_PREREGISTRATION.md`.)

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
