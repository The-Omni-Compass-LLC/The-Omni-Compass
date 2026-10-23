# The live engine, appraised: does the page show the repository's mechanism as it is?

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The question an underwriter asks of a picture of a mechanism: is every moving part the repository's own, run as the
repository runs it, and does every word on the page say only what the parts do? This appraisal answers it for
`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` by reverse engineering: each part of the page is reproduced from the
repository's own code by an independent path and compared, value by value. Run and scored by The Omni-Compass LLC's own
code. No outside party has reviewed or approved these results.

**Engine.** The engine that stands is **omni-v16** (`OMNI_V16.json`, digest `5c5502f12b1c0ce4`, 55 files, since 22 October): omni-v15 with every clock of the Kubernetes governor in seconds, so its decision period changes only how often it looks; at a decision every 60 s, the step the page's port of the brain runs, every value is omni-v15's, so the port is unchanged by it. omni-v15 was omni-v14 with the brain's power-cap request trimming only while the response line has been clean for the governor's own clear time, and every wire that holds a governor's rules inside the fingerprint; the page's port of the brain computes its states, push and headroom, not the power-cap request, so the port is unchanged by it. omni-v14 was omni-v13 with a knob that leaves any muscle native and the operator's commands run without a shell, neither of which the page's ports run.
Since omni-v8 it has changed `tools/run_citylearn.py` (outage buildings' batteries stay native, omni-v8; the wire reads the
coming hour, omni-v9; the glide that cuts the bill most, omni-v10), the realms harness's t table and the Kubernetes governor (a
reading with no machine in service is held, never read as an overload, omni-v11; a CPU-limit raise the cluster's admission
refused is held, not written again at every check, omni-v12; the CPU limits it gave go back to the operator's on a shared host at its
top beside another workload's room, omni-v13; a muscle left native on the operator's word, the operator's commands without a shell, omni-v14; the brain's power-cap request through the line's own clear time, omni-v15; every clock of the governor in seconds, omni-v16), and added `omnicompass/student_t.py` (the
exact Student t); every other engine file is unchanged since omni-v8. Every record on the page was made again on the omni-v9
tree, whose bytes omni-v16 keeps in every file the page reads but the governor and the brain, whose clocks read as before at a decision every 60 s and whose new guards act only on a reading
with no machine in service, on a raise the cluster refused, on a shared host at its top, on a muscle left native and on a response line not yet clean (the page's controller trace has none: recorded again on the
omni-v12 tree on 19 October, it is identical to the record on the page), and its workflow rebuilds them on omni-v16: every run, tick and
decision is identical to the one it replaced, and the intervals are drawn with the exact t (the waiting line's interval widens
in its fourth digit; every word stays). The receipts of the real runs are each benchmark's newest engine's table; their engines, their words and every LOSS row of
Omni-Compass against its native are in the counts below, written by the build from the records at every run (21 October: the
counts had stood still while the tables moved), and replaced as omni-v16's three runs land.

**Wired to the engine.** The page is rebuilt by GitHub itself (`.github/workflows/live-engine.yml`,
`docs/engine/build_live_engine.py`) on every change to the engine, a model, a harness or a result on main, after every
front-page refresh and every three hours: every record is made again by the repository's own code on the engine that
stands, the page's engine is checked against the Python and the C++, every record against the repository's own runs, and
the page carries the commit, the time and GitHub's own list of the runs running and queued. The build stamps the engine
`tools/omni_version.py` reads on the page and rebuilds every record on it; `--check` fails a page whose engine differs.

<!-- counts: written by docs/engine/build_live_engine.py at every build; never edited by hand -->
**The counts of the records on the page** (omni-v16, digest `5c5502f12b1c0ce4`), written by the build from the records it made, so a check rebuilds them exactly:

| What | Count |
|---|---|
| Three-run tables played back from their raw files (sections 5c and 5d) | 81, with 243 runs |
| Raw files checked against their run's own `SHA256SUMS_ALL.txt` | 165,143 of 165,143 matched; 0 unmatched |
| Receipts (every judged row of each benchmark's newest table) | 85: omni-v16 13, omni-v12 54, omni-v11 10, omni-v10 8 |
| Omni-Compass against its native (55 tables), as the tables wrote them | 256 GAIN, 38 power given, 1231 EVEN, 7 LOSS, 1 the runs disagree, 9 the runs differ, 478 shown, 164 tuning (the page applies the floor of 0.5% at load; after it: 239 GAIN, 33 power given, 1253 EVEN, 7 LOSS, 1 the runs disagree, 9 the runs differ, 478 shown, 164 tuning) |
| The orchestrators' own cost (30 four-ways tables: the orchestrator as shipped against the organism alone, and the comparisons where Omni-Compass is on the other side), never a reading of Omni-Compass | 106 GAIN, 12 power given, 417 EVEN, 103 LOSS, 1 the runs disagree, 270 shown (the page applies the floor of 0.5% at load; after it: 106 GAIN, 12 power given, 417 EVEN, 103 LOSS, 1 the runs disagree, 270 shown) |
| LOSS rows of Omni-Compass against its native | 7: queue: job turnaround, submitted to done, mean (s) under `V12_ARMADA_4W_BARE.md` (omni-v12: +5.1% (+1.9 to +8.3), +8.9% (+4.9 to +12.9), +9.1% (+0.9 to +17.3)); queue: job turnaround, submitted to done, mean (s) under `V12_BINPACK.md` (omni-v12: +1.4% (+0.8 to +1.9), +1.0% (+0.4 to +1.7), +1.2% (+0.7 to +1.6)); pod start wait, total (s) under `V12_CRANE_4W_TOP.md` (omni-v12: +80.9% (+37.3 to +124.5), +104.5% (+46.9 to +162.2), +54.4% (+20.0 to +88.9)); response time (ms), 99th percentile under `V12_KUBERAY_4W_BARE.md` (omni-v12: +9.8% (+1.5 to +18.0), +4.4% (+0.1 to +8.7), +13.0% (+4.7 to +21.2)); batch: queue finished (s) under `V12_KUBERAY_4W_BARE.md` (omni-v12: +0.8% (+0.1 to +1.5), +0.7% (+0.2 to +1.2), +0.6% (+0.2 to +1.1)); alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) under `V12_OCM_4W_TOP.md` (omni-v12: +5.7% (+1.4 to +10.0), +6.1% (+0.8 to +11.4), +45.5% (+5.7 to +85.2)); queue: job turnaround, submitted to done, mean (s) under `V12_VANILLA.md` (omni-v12: +0.9% (+0.2 to +1.7), +0.9% (+0.1 to +1.6), +1.2% (+0.6 to +1.8)) |

<!-- end counts -->

## Method: six independent reproductions

| Part of the page | What it claims to be | Reproduced against | Result | Rerun with |
|---|---|---|---|---|
| The brain, nerves, compass law and verdict (JavaScript in the page) | a port of `omnicompass/core.py`, `adapter.py`, `nervous_system.py`, `compass_law.py`, `verdict.py`, `student_t.py` (omni-v16 fingerprint) | the Python itself, on seeded inputs: 8,000 governor decisions, 48,000 organ grants, 4,800 compass forces, 300 verdict intervals, 400 whole verdict trials, 500 degrees of freedom of the exact t | largest difference 2 × 10⁻¹⁵; 0 grants, 0 verdicts, 0 t values differ | `docs/engine/check_live_engine.py` |
| The core in C++ | the page's six-state derivative and RK4 step against the repository's C++ twin (`cpp/src/core.cpp`, compiled by the check with `docs/engine/cpp_core_probe.cpp`) | 2,000 seeded states and parameters | largest relative difference 4.4 × 10⁻¹⁶ (derivative), 2.2 × 10⁻¹⁶ (RK4 step) | `docs/engine/check_live_engine.py` |
| Section 1, one organism | the realms harness's own organism run, native and the max, under the climb | `realms/harness.py run_organism_arm`, seeds 3000 and 3001 | decisions over the line and every plant's work identical (seed 3000: 900 native, 849 the max, both paths) | `docs/engine/check_records.py` |
| Section 1, each muscle alone | the harness's own single-muscle runs, native and the max with its twin, under the line | `realms/harness.py run_muscle_arm`, 60 muscles × 2 arms, seeds 3000 and 3001 | 120 of 120 runs identical per seed | `docs/engine/check_records.py` |
| Section 2, the cloud's setting | the shipped controller as `tools/toy_gate.py` wires it | `tools/toy_gate.py --worker`, seeds 3000 and 3001 | machine-hours identical (seed 3000: 27.604 both arms); verdict steps allowed and refused identical (3 and 3) | `docs/engine/check_records.py` |
| Section 2, on top of the HPA | the shipped controller as `pilot/selfpilot.py run_day` wires it | `pilot/selfpilot.py run_day`, seeds 3000 and 3001 | machines and pods waiting identical on every one of 1,440 ticks; writes identical (25) | `docs/engine/check_records.py` |
| Section 1, the immune system | Omni-Compass's organism reading its own immune system: every room against its twin, the heat debt, the body giving back | the same run of `realms/harness.py`'s organism with the readings taken as `max_body_step` reads them (read only: the organism's record is identical with and without them) | run A: 7 decisions with an inflamed room (`pump_speed`), heat debt 1,109 W fading to 21 W, the pools' 26 extra machines handed back; runs B and C: none | `docs/engine/export_harness_trace.py` |
| Section 4, the official runs | each three-run table's runs A, B and C played back from their raw files (`docs/engine/export_runs.py`) | every file's SHA-256 against the run's own `SHA256SUMS_ALL.txt`; every Kubernetes repetition scored by `tools/live_reps.py arm_gauges` on its own files, the mean over repetitions against the run's own `LIVE_REPS.json` | every run's files and their match in the counts above, written at every build (on 21 October: 81 tables, 243 runs, 165,095 of 165,095 files); the scorer's means equal each run's result to 4.2 × 10⁻¹⁶ | `docs/engine/build_live_engine.py --check` |
| Section 3, a GPU card | `realms/gpu_card.py` (inside the omni-v16 fingerprint, unchanged since omni-v8), native and Omni-Compass on top, the card as shipped and under an operator's cap, AI and compute-bound work | `realms/gpu_card.run` untouched, every arm, seeds 5100, 5101 and 5102 | the run's own result identical; every second's energy and requests add up to it | `docs/engine/check_records.py` |
| Section 3, Linux, one host | `tools/toy_gate.py`'s conveyance model, the shipped `Muscles.convey` and `quota.py` on the CFS quota | `tools/toy_gate.py worker_convey` untouched, seeds 3000, 3001 and 3002 | its own result line identical; requests and the host's busy share add up to it | `docs/engine/check_records.py` |
| Section 3, every muscle on omni-v8 | the realms runner's own table of 1,107 muscles and seven organisms, native and the max | `results/realms_v5/REALMS_V5.json` (omni-v8, commit 9819a903c, seeds 3000 to 3009), read by `docs/engine/export_scenarios.py` | 527 GAIN, 159 the same as native, 421 at their limit on native, 0 LOSS; all seven organisms GAIN under all three loads | `docs/engine/export_scenarios.py` |
| Section 4, the receipts | every judged row of each benchmark's newest table (`results/live/V*_*.md`) | the receipts themselves, read row by row by `docs/engine/export_scenarios.py` | the counts above, written at every build: every word, Omni-Compass against its native apart from the orchestrators' own cost, every LOSS row named | `docs/engine/export_scenarios.py` |

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
| Disclosures and labels | A | evidence class on every view, the stress-test model (native and Omni-Compass on top, side by side) marked as drawn and as larger than the harness reads, the wiring declaration, the contact lines |
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
| Linux, one host (the CFS-quota conveyance model) | requests served +64%; response time −53% mean and at the 95th percentile | alert minutes | host CPU +31%, limits +167%, pods +18%; pod start wait rose 6% to 8%, one value a run and so no interval: shown, not judged (the model's: a busier host starts pods slower; EVEN on real Kubernetes) |
| Every muscle of the catalog on omni-v8, each alone (realms runner) | 527 muscles (493 faster, 409 fewer misses, 33 more work) | 159 the same as native, 421 at their limit on native | **0 LOSS** under any load |
| The seven organisms on omni-v8 (realms runner) | all seven under all three loads: misses −1.1% to −8.8%; on the climb five also more work | work | energy +0.000% to +0.05% |
| The receipts of each benchmark's newest table (classes L and S) | the counts above | the counts above | the counts above, every LOSS row of Omni-Compass against its native named with its table and its three runs |
| Real Kubernetes, omni-v10 (class L, `results/live/V10_GOLDILOCKS.md`, `V10_KEDA_REQUESTS.md`, `V10_KEDA_CPU_REQUESTS.md`, `V10_CRUISEKUBE.md`, `V10_CAPACITY.md`) | response time −51% to −73% at the 95th percentile on Goldilocks and both KEDA setups; KEDA HTTP replicas −13% to −19%, pods started −17% to −24% | machines, failed requests; CruiseKube and fixed capacity on every gauge | parked-worker energy +1.4% to +2.4%; LOSS: the KEDA HTTP pod start wait |

## Material findings for the owner

1. **The models read small where the real runs read large.** In every modelled harness the two arms differ little; on
   real Kubernetes the response time falls by half or more. The real gains come through the pod CPU limits (conveyance),
   which the realms plants and the toy cluster do not carry as real Kubernetes does. An underwriter values the class L
   receipts, not the models, for the size of the benefit.
2. **The harness's native is estimated, not measured** (`realms/presets.py`: "round engineering figures"). The native
   register (`docs/engine/NATIVE_REGISTER.md`) finds the max's "native at its limit" rule right on real defaults for power
   limits, CPU clocks and admission gates, and one setting off: the HPA target, 70% in the harness against 50% in the
   repository's real runs. Correcting it is a change inside the omni-v16 fingerprint, the next engine version.
3. **No cut in the cloud bill is shown yet.** The real Azure bill (`results/live/AKS_BILL.md`, an earlier engine, four
   repetitions) reads machines billed −0.6%, EVEN; Azure's own autoscaler ran that light load on fewer than two workers.
   The one gauge clear of the noise there was fewer replicas (−3.7%, GAIN).
4. **`pilot/selfpilot.py` no longer runs its omni day on a machine without `kubectl`**: the controller now starts a
   `kubectl proxy` when it builds its reader. The check stubs that one call; the simulated cluster answers every read.
   A one-line repair (`--no-api-proxy` in its arguments) is the owner's to make.
5. **The verdict's rule depends on the noise more than on the cost.** omni-v16 (its verdict omni-v11's, byte for byte) refuses any step whose interval of cost
   lies wholly above zero. Where the cost carries no noise (the GPU card's model) it refuses a step costing +0.14% a
   request, well inside the 2% allowance, so the card never leaves native at the tune-down and the recorded +3.4%
   requests per kJ (`results/sim/gpu_two_wire`, written under omni-v6's medians) does not stand on any engine since. Where the
   cost is noisy (σ 0.46 of log response time on the Google 2011 day and 0.43 with the load swinging, measured on 19
   October inside each window of 200 requests of the omni-v10 runs' latency.csv;
   the σ 0.05 and 0.25 written here before did not come from those files and are withdrawn), with 200 requests a side
   as the Kubernetes controller measures, a step costing +3% passes about 31% of the time (the medians alone: 45%),
   +5% about 15% and +10% about 1%, while a free step is kept about 59% of the time (2,000 modelled trials each, class S).
   The page's verdict lab opens on that measured noise. Any change to the
   rule is the next engine version, the owner's to order.
6. **CityLearn's LOSS rows were root-caused and repaired, and its omni-v10 table reads no LOSS** (88 EVEN, 27 GAIN, 1 power
   given, 3 where the runs disagree). The earlier table read LOSS on the energy not served and the time uncomfortable in the
   2023 small challenge districts, the only ones that simulate outages; the repair leaves an outage building's battery native
   (its charge is its building's reserve), reads the coming hour and glides at the speed that cuts the bill most with no LOSS
   (omni-v8 to omni-v10, `docs/OMNI_V10.md`).
7. **The Linux model's pod start wait rises** (+6% to +8%, one value a run and so no interval, shown and not judged; +8.8% in `results/toy_gate/TOY_GATE.md` over ten seeds):
   the raised limits keep the host busier and its start time is fitted to rise with the busy share. The two repairs
   written for it were refused by the toy gate. On real Kubernetes it reads EVEN on KEDA on CPU and requests and LOSS on KEDA's HTTP add-on (+13% to +21%, the test machine, `docs/POD_START_WAIT.md`; the kind rig pre-pulls the image from 18 October).
8. **The page replays recorded runs.** The harness and controller views are the repository's runs, recorded on seeds
   3000, 3001 and 3002 and replayed; they cannot be stressed by hand. The stress-test model can (native alone and Omni-Compass on top of the same native, side by side), and is labelled as drawn.

## Limitations

Evidence class S throughout the models (our own models), class L only in the receipts quoted. Three seeds per view, six
hours per controller run, 240 decisions per organism run. The checks prove the page shows the code as it runs; they do
not prove the code's results hold outside the models it runs on, which is what the real runs and the receipts are for.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
