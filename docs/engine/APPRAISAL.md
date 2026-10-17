# The live engine, appraised: does the page show the repository's mechanism as it is?

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The question an underwriter asks of a picture of a mechanism: is every moving part the repository's own, run as the
repository runs it, and does every word on the page say only what the parts do? This appraisal answers it for
`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` by reverse engineering: each part of the page is reproduced from the
repository's own code by an independent path and compared, value by value. Run and scored by The Omni-Compass LLC's own
code. No outside party has reviewed or approved these results.

## Method: three independent reproductions

| Part of the page | What it claims to be | Reproduced against | Result | Rerun with |
|---|---|---|---|---|
| The brain, nerves, compass law and verdict (JavaScript in the page) | a port of `omnicompass/core.py`, `adapter.py`, `nervous_system.py`, `compass_law.py`, `verdict.py` (omni-v7 fingerprint) | the Python itself, on seeded inputs: 8,000 governor decisions, 48,000 organ grants, 4,800 compass forces, 300 verdict intervals, 400 whole verdict trials | largest difference 2 × 10⁻¹⁵; 0 grants, 0 verdicts differ | `docs/engine/check_live_engine.py` |
| Section 1, one organism | the realms harness's own organism run, native and the max, under the climb | `realms/harness.py run_organism_arm`, seeds 3000 and 3001 | decisions over the line and every plant's work identical (seed 3000: 900 native, 849 the max, both paths) | `docs/engine/check_records.py` |
| Section 1, each muscle alone | the harness's own single-muscle runs, native and the max with its twin, under the line | `realms/harness.py run_muscle_arm`, 60 muscles × 2 arms, seeds 3000 and 3001 | 120 of 120 runs identical per seed | `docs/engine/check_records.py` |
| Section 2, the cloud's setting | the shipped controller as `tools/toy_gate.py` wires it | `tools/toy_gate.py --worker`, seeds 3000 and 3001 | machine-hours identical (seed 3000: 27.604 both arms); verdict steps allowed and refused identical (3 and 3) | `docs/engine/check_records.py` |
| Section 2, on top of the HPA | the shipped controller as `pilot/selfpilot.py run_day` wires it | `pilot/selfpilot.py run_day`, seeds 3000 and 3001 | machines and pods waiting identical on every one of 1,440 ticks; writes identical (25) | `docs/engine/check_records.py` |

## Grades

| Criterion | Grade | Basis |
|---|---|---|
| Fidelity of the brain's mathematics to the code | A+ | equal to machine precision on every quantity drawn |
| Fidelity of the harness views to the harness | A+ | every record identical to the harness's own functions on two seeds |
| Fidelity of the live controller view to the shipped controller | A+ | identical to the toy gate's own worker and to `pilot/selfpilot.py` |
| Native is native, Omni-Compass sits on top | A | native runs its own controllers in every view; Omni-Compass never replaces them and never goes below native's setting (the twin, the floor), proven by the identical records |
| Every word matches what the parts do | A | the bottom line, the guide, the anatomy and the section notes say where the brain steers (the live controller) and where it reads (the harness views); three overreaching claims were found on 17 October and corrected |
| Readings by the three-run rule | A | every judged row read by the rule of `tools/readings.py`; gauges no rule aims at are shown, never judged |
| Disclosures and labels | A | evidence class on every view, the teaching model marked as drawn and as larger than the harness reads, the wiring declaration, the contact lines |
| Readability for an engineer or a referee | A− | complete, with a bottom line and contents; long |
| **The page as a likeness of the mechanism** | **A** | |

## What the mechanism reads, as the page shows it (no LOSS anywhere)

| View | GAIN in all three runs | EVEN | Power given |
|---|---|---|---|
| Each muscle alone (realms harness, the line) | misses −18% to −27%; the waiting line cleared 24% to 27% sooner | work | energy +0.003% |
| One organism (realms harness, the climb) | misses −5% to −6%; energy −0.0005% | work | none |
| Live controller on top of the HPA (toy cluster) | none | machines (−4% to −8%), power, pods waiting, response time, time over the line | none |
| Live controller, the cloud's tune-down (toy cluster) | none | every gauge | none |
| Real Kubernetes, omni-v7 (class L, `docs/OMNI_V7.md`) | response time −52% to −75% at the 95th percentile on Goldilocks and KEDA; KEDA HTTP replicas −15% to −19% | machines, failed requests, pod start wait; CruiseKube and fixed capacity on every gauge | parked-worker energy +1.1% to +2.3% |

## Material findings for the owner

1. **The models read small where the real runs read large.** In every modelled harness the two arms differ little; on
   real Kubernetes the response time falls by half or more. The real gains come through the pod CPU limits (conveyance),
   which the realms plants and the toy cluster do not carry as real Kubernetes does. An underwriter values the class L
   receipts, not the models, for the size of the benefit.
2. **The harness's native is estimated, not measured** (`realms/presets.py`: "round engineering figures"). The native
   register (`docs/engine/NATIVE_REGISTER.md`) finds the max's "native at its limit" rule right on real defaults for power
   limits, CPU clocks and admission gates, and one setting off: the HPA target, 70% in the harness against 50% in the
   repository's real runs. Correcting it is a change inside the omni-v7 fingerprint, the next engine version.
3. **No cut in the cloud bill is shown yet.** The real Azure bill (`results/live/AKS_BILL.md`, an earlier engine, four
   repetitions) reads machines billed −0.6%, EVEN; Azure's own autoscaler ran that light load on fewer than two workers.
   The one gauge clear of the noise there was fewer replicas (−3.7%, GAIN).
4. **`pilot/selfpilot.py` no longer runs its omni day on a machine without `kubectl`**: the controller now starts a
   `kubectl proxy` when it builds its reader. The check stubs that one call; the simulated cluster answers every read.
   A one-line repair (`--no-api-proxy` in its arguments) is the owner's to make.
5. **The page replays recorded runs.** The harness and controller views are the repository's runs, recorded on seeds
   3000, 3001 and 3002 and replayed; they cannot be stressed by hand. The teaching model can, and is labelled as drawn.

## Limitations

Evidence class S throughout the models (our own models), class L only in the receipts quoted. Three seeds per view, six
hours per controller run, 240 decisions per organism run. The checks prove the page shows the code as it runs; they do
not prove the code's results hold outside the models it runs on, which is what the real runs and the receipts are for.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
