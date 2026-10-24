# CityLearn, every district: the A/B/C three-run table (Omni v7)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run (under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the values the table prints (it keeps no JSON twin; a printed size of exactly 0.50% counts as at the floor); every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

CityLearn (University of Texas at Austin) is an independent, deterministic simulator of real buildings with its own controller (BasicRBC) and its own scores; every score is one CityLearn itself aims lower. Native is that controller; omni is the same controller with the compass law on top of its electric battery commands only (`tools/run_citylearn.py`). The same districts ran three times as separate GitHub runs on the same frozen engine. Because the simulator is deterministic, the runs must reproduce each other: a score reads **GAIN** or **LOSS in all three of our runs** when all three runs give the same sign, judged by what the score is for and never by its sign: the electricity bought, the bill, the carbon, the peaks, the swings and the unevenness are the power the district draws and holds and the wear of moving it, so a fall is a cut, a GAIN, and a rise is **power given**; a rise in the energy not served or the time uncomfortable (the occupants' misses) is a LOSS. **EVEN, the same** when the change is under one part in a million, and **the runs differ** when they do not reproduce, which is a finding about the simulator or the harness and is said so. A district with no electric battery gets nothing from Omni (a water tank stays native), so any native/omni difference in it is CityLearn's own run-to-run variation, never an Omni result. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Districts in the run |
|---|---|---|---|---:|
| A | 38937540021 | `1ccba53a74fe` | omni-v7 (digest d6d467b824c585f1, 46 files) | 22 |
| B | 38949618073 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 22 |
| C | 38959444615 | `cf8dccec0604` | omni-v7 (digest d6d467b824c585f1, 46 files) | 22 |

## Districts with electric batteries: omni against native, each run

### ca_alameda_county_neighborhood: 100 buildings, 100 batteries, 4 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| electricity bought (`electricity_consumption_total`) | -5.88% | -5.88% | -5.88% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| daily peak draw (`daily_peak_average`) | -3.61% | -3.61% | -3.61% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.05% | -3.05% | -3.05% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | -3.94% | -3.94% | -3.94% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -0.97% | -0.97% | -0.97% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.72% | -0.72% | -0.72% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.10% | -0.10% | -0.10% | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | EVEN, the same |

### citylearn_challenge_2022_phase_all_robustness: 17 buildings, 17 batteries, 0 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | -8.61% | -8.61% | -8.61% | **GAIN in all three of our runs** |
| electricity bought (`electricity_consumption_total`) | -14.66% | -14.66% | -14.66% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | -11.89% | -11.89% | -11.89% | **GAIN in all three of our runs** |
| daily peak draw (`daily_peak_average`) | -13.95% | -13.95% | -13.95% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -2.73% | -2.73% | -2.73% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | -7.18% | -7.18% | -7.18% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.90% | -2.90% | -2.90% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.11% | +0.11% | +0.11% | EVEN, under the floor (every run under 0.5%; the largest 0.11%) |
| distance from zero net energy (`zero_net_energy`) | -6.10% | -6.10% | -6.10% | **GAIN in all three of our runs** |

### citylearn_challenge_2023_phase_2_local_evaluation: 3 buildings, 3 batteries, 3 water tanks left native, 720 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.35% | +0.35% | +0.35% | EVEN, under the floor (every run under 0.5%; the largest 0.35%) |
| electricity bought (`electricity_consumption_total`) | -0.27% | -0.27% | -0.27% | EVEN, under the floor (every run under 0.5%; the largest 0.27%) |
| carbon (`carbon_emissions_total`) | -0.17% | -0.17% | -0.17% | EVEN, under the floor (every run under 0.5%; the largest 0.17%) |
| daily peak draw (`daily_peak_average`) | -1.61% | -1.61% | -1.61% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| ramping (swings hour to hour) (`ramping_average`) | +6.24% | +6.24% | +6.24% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.86% | -2.86% | -2.86% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | +0.07% | +0.07% | +0.07% | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| distance from zero net energy (`zero_net_energy`) | -0.06% | -0.06% | -0.06% | EVEN, under the floor (every run under 0.5%; the largest 0.06%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +5.96% | +5.96% | +5.96% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.12% | +0.12% | +0.12% | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |

### citylearn_challenge_2023_phase_2_online_evaluation_1: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.34% | +0.34% | +0.34% | EVEN, under the floor (every run under 0.5%; the largest 0.34%) |
| electricity bought (`electricity_consumption_total`) | -0.15% | -0.15% | -0.15% | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| carbon (`carbon_emissions_total`) | -0.16% | -0.16% | -0.16% | EVEN, under the floor (every run under 0.5%; the largest 0.16%) |
| daily peak draw (`daily_peak_average`) | -1.34% | -1.34% | -1.34% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.49% | -3.49% | -3.49% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +5.56% | +5.56% | +5.56% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.05% | -2.05% | -2.05% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.07% | -0.07% | -0.07% | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +5.50% | +5.50% | +5.50% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.02% | +0.02% | +0.02% | EVEN, under the floor (every run under 0.5%; the largest 0.02%) |

### citylearn_challenge_2023_phase_2_online_evaluation_2: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.32% | +0.32% | +0.32% | EVEN, under the floor (every run under 0.5%; the largest 0.32%) |
| electricity bought (`electricity_consumption_total`) | -0.18% | -0.18% | -0.18% | EVEN, under the floor (every run under 0.5%; the largest 0.18%) |
| carbon (`carbon_emissions_total`) | -0.17% | -0.17% | -0.17% | EVEN, under the floor (every run under 0.5%; the largest 0.17%) |
| daily peak draw (`daily_peak_average`) | -1.30% | -1.30% | -1.30% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.49% | -3.49% | -3.49% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +5.60% | +5.60% | +5.60% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -1.67% | -1.67% | -1.67% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.07% | -0.07% | -0.07% | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +6.25% | +6.25% | +6.25% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.15% | +0.15% | +0.15% | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |

### citylearn_challenge_2023_phase_2_online_evaluation_3: 3 buildings, 3 batteries, 3 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.30% | +0.30% | +0.30% | EVEN, under the floor (every run under 0.5%; the largest 0.30%) |
| electricity bought (`electricity_consumption_total`) | -0.17% | -0.17% | -0.17% | EVEN, under the floor (every run under 0.5%; the largest 0.17%) |
| carbon (`carbon_emissions_total`) | -0.18% | -0.18% | -0.18% | EVEN, under the floor (every run under 0.5%; the largest 0.18%) |
| daily peak draw (`daily_peak_average`) | -1.54% | -1.54% | -1.54% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | -3.49% | -3.49% | -3.49% | **GAIN in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +5.45% | +5.45% | +5.45% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -2.26% | -2.26% | -2.26% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.06% | -0.06% | -0.06% | EVEN, under the floor (every run under 0.5%; the largest 0.06%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +9.80% | +9.80% | +9.80% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | -0.01% | -0.01% | -0.01% | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |

### citylearn_challenge_2023_phase_3_1: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.26% | +0.26% | +0.26% | EVEN, under the floor (every run under 0.5%; the largest 0.26%) |
| electricity bought (`electricity_consumption_total`) | -0.10% | -0.10% | -0.10% | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| carbon (`carbon_emissions_total`) | -0.13% | -0.13% | -0.13% | EVEN, under the floor (every run under 0.5%; the largest 0.13%) |
| daily peak draw (`daily_peak_average`) | -2.20% | -2.20% | -2.20% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +2.53% | +2.53% | +2.53% | **power given in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +4.51% | +4.51% | +4.51% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -3.96% | -3.96% | -3.96% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -1.18% | -1.18% | -1.18% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.02% | -0.02% | -0.02% | EVEN, under the floor (every run under 0.5%; the largest 0.02%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +1.97% | +1.97% | +1.97% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.02% | +0.02% | +0.02% | EVEN, under the floor (every run under 0.5%; the largest 0.02%) |

### citylearn_challenge_2023_phase_3_2: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.19% | +0.19% | +0.19% | EVEN, under the floor (every run under 0.5%; the largest 0.19%) |
| electricity bought (`electricity_consumption_total`) | -0.10% | -0.10% | -0.10% | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| carbon (`carbon_emissions_total`) | -0.12% | -0.12% | -0.12% | EVEN, under the floor (every run under 0.5%; the largest 0.12%) |
| daily peak draw (`daily_peak_average`) | -2.18% | -2.18% | -2.18% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +2.53% | +2.53% | +2.53% | **power given in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +4.89% | +4.89% | +4.89% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -4.14% | -4.14% | -4.14% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.53% | -0.53% | -0.53% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | +0.04% | +0.04% | +0.04% | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +4.14% | +4.14% | +4.14% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.09% | +0.09% | +0.09% | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |

### citylearn_challenge_2023_phase_3_3: 6 buildings, 6 batteries, 6 water tanks left native, 2,208 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.26% | +0.26% | +0.26% | EVEN, under the floor (every run under 0.5%; the largest 0.26%) |
| electricity bought (`electricity_consumption_total`) | -0.07% | -0.07% | -0.07% | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| carbon (`carbon_emissions_total`) | -0.08% | -0.08% | -0.08% | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| daily peak draw (`daily_peak_average`) | -2.56% | -2.56% | -2.56% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +2.53% | +2.53% | +2.53% | **power given in all three of our runs** |
| ramping (swings hour to hour) (`ramping_average`) | +4.79% | +4.79% | +4.79% | **power given in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -4.68% | -4.68% | -4.68% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.96% | -0.96% | -0.96% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.01% | -0.01% | -0.01% | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| energy not served (`annual_normalized_unserved_energy_total`) | +2.22% | +2.22% | +2.22% | **LOSS in all three of our runs** |
| time uncomfortable (`discomfort_proportion`) | +0.01% | +0.01% | +0.01% | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |

### tx_travis_county_neighborhood: 100 buildings, 100 batteries, 39 water tanks left native, 8,760 hours

| CityLearn score (CityLearn aims every score lower) | A | B | C | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| electricity bought (`electricity_consumption_total`) | -3.00% | -3.00% | -3.00% | **GAIN in all three of our runs** |
| carbon (`carbon_emissions_total`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| daily peak draw (`daily_peak_average`) | -1.88% | -1.88% | -1.88% | **GAIN in all three of our runs** |
| highest peak (`all_time_peak_average`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| ramping (swings hour to hour) (`ramping_average`) | -2.91% | -2.91% | -2.91% | **GAIN in all three of our runs** |
| daily load unevenness (`daily_one_minus_load_factor_average`) | -1.15% | -1.15% | -1.15% | **GAIN in all three of our runs** |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | -0.71% | -0.71% | -0.71% | **GAIN in all three of our runs** |
| distance from zero net energy (`zero_net_energy`) | -0.58% | -0.58% | -0.58% | **GAIN in all three of our runs** |
| energy not served (`annual_normalized_unserved_energy_total`) | +0.00% | +0.00% | +0.00% | EVEN, the same |
| time uncomfortable (`discomfort_proportion`) | +0.00% | +0.00% | +0.00% | EVEN, the same |

## Across the districts with batteries

A district counts only when all three runs agree.

| CityLearn score | GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | EVEN | The runs differ |
|---|---:|---:|---:|---:|---:|
| electricity bill | 1 | 0 | 0 | 9 | 0 |
| electricity bought | 3 | 0 | 0 | 7 | 0 |
| carbon | 1 | 0 | 0 | 9 | 0 |
| daily peak draw | 10 | 0 | 0 | 0 | 0 |
| highest peak | 5 | 0 | 3 (citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 2 | 0 |
| ramping (swings hour to hour) | 3 | 0 | 7 (citylearn_challenge_2023_phase_2_local_evaluation, citylearn_challenge_2023_phase_2_online_evaluation_1, citylearn_challenge_2023_phase_2_online_evaluation_2, citylearn_challenge_2023_phase_2_online_evaluation_3, citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 0 | 0 |
| daily load unevenness | 10 | 0 | 0 | 0 | 0 |
| monthly load unevenness | 8 | 0 | 0 | 2 | 0 |
| distance from zero net energy | 2 | 0 | 0 | 8 | 0 |
| energy not served | 0 | 7 (citylearn_challenge_2023_phase_2_local_evaluation, citylearn_challenge_2023_phase_2_online_evaluation_1, citylearn_challenge_2023_phase_2_online_evaluation_2, citylearn_challenge_2023_phase_2_online_evaluation_3, citylearn_challenge_2023_phase_3_1, citylearn_challenge_2023_phase_3_2, citylearn_challenge_2023_phase_3_3) | 0 | 2 | 0 |
| time uncomfortable | 0 | 0 | 0 | 9 | 0 |

## Districts with no electric battery: nothing for Omni to move

The runner changes only `electrical_storage` commands, so in these districts omni applied nothing. Any difference between the arms is CityLearn's own run-to-run variation and says nothing about Omni; where the two arms agree, the simulator is deterministic there.

| District | Buildings | Water tanks (native) | Scores where native and omni differ in A | Reproduced over A, B, C |
|---|---:|---:|---|---|
| baeda_3dem | 4 | 7 | none | yes |
| quebec_neighborhood_with_demand_response_set_points | 20 | 0 | time uncomfortable +0.25% | no |
| quebec_neighborhood_without_demand_response_set_points | 20 | 0 | time uncomfortable -0.28% | no |

## Districts CityLearn cannot run with its own controller

The same for native and omni; listed, never dropped.

| District | CityLearn's own error |
|---|---|
| citylearn_challenge_2022_phase_all_demand_response | `ValueError: demand_response.enabled=true requires interface='entity'.` |
| citylearn_challenge_2022_phase_all_plus_evs | `ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1` |
| citylearn_three_phase_dynamic_asset_changes_demo_15s_parquet | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_dynamic_assets_only_demo | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_dynamic_assets_only_demo_15s_parquet | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_dynamic_topology_demo | `ValueError: topology_mode='dynamic' requires interface='entity'.` |
| citylearn_three_phase_electrical_service_demo | `ValueError: Unknown action name: deferrable_appliance_deferrable_appliance_1` |
| citylearn_three_phase_electrical_service_demo_15s_parquet | `ImportError: Reading Parquet CityLearn datasets requires the optional 'pyarrow' dependency. Install pyarrow or use CSV f` |
| vt_chittenden_county_neighborhood | `Exception: Unable to get response from GitHub API for endpoint: https://api.github.com/repos/citylearn-project/CityLearn; no result` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
