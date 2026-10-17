# The live engine, appraised: does the page show the repository's mechanism as it is?

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The question an underwriter asks of a picture of a mechanism: is every moving part the repository's own, run as the
repository runs it, and does every word on the page say only what the parts do? This appraisal answers it for
`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` by reverse engineering: each part of the page is reproduced from the
repository's own code by an independent path and compared, value by value. Run and scored by The Omni-Compass LLC's own
code. No outside party has reviewed or approved these results.

## Method: four independent reproductions

| Part of the page | What it claims to be | Reproduced against | Result | Rerun with |
|---|---|---|---|---|
| The brain, nerves, compass law and verdict (JavaScript in the page) | a port of `omnicompass/core.py`, `adapter.py`, `nervous_system.py`, `compass_law.py`, `verdict.py` (omni-v7 fingerprint) | the Python itself, on seeded inputs: 8,000 governor decisions, 48,000 organ grants, 4,800 compass forces, 300 verdict intervals, 400 whole verdict trials | largest difference 2 × 10⁻¹⁵; 0 grants, 0 verdicts differ | `docs/engine/check_live_engine.py` |
| Section 1, one organism | the realms harness's own organism run, native and the max, under the climb | `realms/harness.py run_organism_arm`, seeds 3000 and 3001 | decisions over the line and every plant's work identical (seed 3000: 900 native, 849 the max, both paths) | `docs/engine/check_records.py` |
| Section 1, each muscle alone | the harness's own single-muscle runs, native and the max with its twin, under the line | `realms/harness.py run_muscle_arm`, 60 muscles × 2 arms, seeds 3000 and 3001 | 120 of 120 runs identical per seed | `docs/engine/check_records.py` |
| Section 2, the cloud's setting | the shipped controller as `tools/toy_gate.py` wires it | `tools/toy_gate.py --worker`, seeds 3000 and 3001 | machine-hours identical (seed 3000: 27.604 both arms); verdict steps allowed and refused identical (3 and 3) | `docs/engine/check_records.py` |
| Section 2, on top of the HPA | the shipped controller as `pilot/selfpilot.py run_day` wires it | `pilot/selfpilot.py run_day`, seeds 3000 and 3001 | machines and pods waiting identical on every one of 1,440 ticks; writes identical (25) | `docs/engine/check_records.py` |
| Section 3, a GPU card | `realms/gpu_card.py` (omni-v7 fingerprint), native and Omni-Compass on top, the card as shipped and under an operator's cap, AI and compute-bound work | `realms/gpu_card.run` untouched, every arm, seeds 5100, 5101 and 5102 | the run's own result identical; every second's energy and requests add up to it | `docs/engine/check_records.py` |
| Section 3, Linux, one host | `tools/toy_gate.py`'s conveyance model, the shipped `Muscles.convey` and `quota.py` on the CFS quota | `tools/toy_gate.py worker_convey` untouched, seeds 3000, 3001 and 3002 | its own result line identical; requests and the host's busy share add up to it | `docs/engine/check_records.py` |
| Section 3, the receipts | every judged row of the 22 omni-v7 receipts in `results/live/V7_*.md` | the receipts themselves, read row by row by `docs/engine/export_scenarios.py` | 210 GAIN, 38 power given, 509 EVEN, 25 LOSS, 11 the runs disagree | `docs/engine/export_scenarios.py` |

## Grades

| Criterion | Grade | Basis |
|---|---|---|
| Fidelity of the brain's mathematics to the code | A+ | equal to machine precision on every quantity drawn |
| Fidelity of the harness views to the harness | A+ | every record identical to the harness's own functions on two seeds |
| Fidelity of the live controller view to the shipped controller | A+ | identical to the toy gate's own worker and to `pilot/selfpilot.py` |
| Fidelity of the stacks (section 3) to their models and receipts | A+ | the GPU card and the Linux host identical to their own runs; every receipt row as written, the LOSS rows kept |
| Native is native, Omni-Compass sits on top | A | native runs its own controllers in every view; Omni-Compass never replaces them and never goes below native's setting (the twin, the floor), proven by the identical records |
| Every word matches what the parts do | A | the bottom line, the guide, the anatomy and the section notes say where the brain steers (the live controller) and where it reads (the harness views); three overreaching claims were found on 17 October and corrected |
| Readings by the three-run rule | A | every judged row read by the rule of `tools/readings.py`; gauges no rule aims at are shown, never judged |
| Disclosures and labels | A | evidence class on every view, the teaching model marked as drawn and as larger than the harness reads, the wiring declaration, the contact lines |
| Readability for an engineer or a referee | A− | complete, with a bottom line and contents; long |
| **The page as a likeness of the mechanism** | **A** | |

## What the mechanism reads, as the page shows it

| View | GAIN in all three runs | EVEN | Power given |
|---|---|---|---|
| Each muscle alone (realms harness, the line) | misses −18% to −27%; the waiting line cleared 24% to 27% sooner | work | energy +0.003% |
| One organism (realms harness, the climb) | misses −5% to −6%; energy −0.0005% | work | none |
| Live controller on top of the HPA (toy cluster) | none | machines (−4% to −8%), power, pods waiting, response time, time over the line | none |
| Live controller, the cloud's tune-down (toy cluster) | none | every gauge | none |
| A GPU card, the card as shipped (`realms/gpu_card.py`) | none | every gauge: at the max the card's limit is its top; at the tune-down the one step tried is refused (LOSS read on its cost) | none |
| A GPU card under an operator's 105 W cap, compute-bound | response time −8% to −11% | requests, energy, time over the line | none |
| Linux, one host (the CFS-quota conveyance model) | requests served +64%; response time −53% mean and at the 95th percentile | alert minutes | host CPU +31%, limits +167%, pods +18%; **pod start wait +6% to +8%, LOSS** (the model's: a busier host starts pods slower; EVEN on real Kubernetes) |
| The 22 receipts of omni-v7 (classes L and S) | 210 rows | 509 rows | 38 rows; **25 rows LOSS, all CityLearn** (7 small challenge districts: energy not served +2% to +10%, the hour-to-hour swings, discomfort, the highest peak); 11 rows where the runs disagree (drone swarms 9, Redis 1, MySQL 1) |
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
5. **The verdict's rule depends on the noise more than on the cost.** omni-v7 refuses any step whose interval of cost
   lies wholly above zero. Where the cost carries no noise (the GPU card's model) it refuses a step costing +0.14% a
   request, well inside the 2% allowance, so the card never leaves native at the tune-down and the recorded +3.4%
   requests per kJ (`results/sim/gpu_two_wire`, written under omni-v6's medians) no longer stands on omni-v7. Where the
   cost is noisy (σ 0.25 of log response time, the load swinging, 200 requests a side as the Kubernetes controller
   measures) a step costing +3% passes about a quarter of the time and +5% about one time in twenty; on a steady day
   (σ 0.05) +3% never passes. The page's verdict lab now opens wired as the controller is (200 requests) on the measured
   noise; it opened at 30 requests and σ 0.25 before, which read the engine weaker than it is wired. Any change to the
   rule is the next engine version, the owner's to order.
6. **CityLearn carries the only LOSS rows of omni-v7.** In 7 of its 10 battery districts (the small challenge districts)
   energy not served rises 2% to 10%, with more hour-to-hour swing and discomfort; the 17-building district reads one
   LOSS (monthly unevenness), and the two 100-building districts read no LOSS (GAIN on 7 and 6 of their 11 scores, the
   rest EVEN). Under the founder's order a LOSS is root-caused, fixed and rerun.
7. **The Linux model's pod start wait reads LOSS** (+6% to +8%, +8.8% in `results/toy_gate/TOY_GATE.md` over ten seeds):
   the raised limits keep the host busier and its start time is fitted to rise with the busy share. The two repairs
   written for it were refused by the toy gate. On real Kubernetes the start wait reads EVEN.
8. **The page replays recorded runs.** The harness and controller views are the repository's runs, recorded on seeds
   3000, 3001 and 3002 and replayed; they cannot be stressed by hand. The teaching model can, and is labelled as drawn.

## Limitations

Evidence class S throughout the models (our own models), class L only in the receipts quoted. Three seeds per view, six
hours per controller run, 240 decisions per organism run. The checks prove the page shows the code as it runs; they do
not prove the code's results hold outside the models it runs on, which is what the real runs and the receipts are for.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
