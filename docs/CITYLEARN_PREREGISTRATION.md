# Omni-Compass on top of CityLearn's own controller: written before the confirmation run

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Any commercial use requires a signed,
> paid Omni-Compass Enterprise License. See [`LICENSE`](../LICENSE) and [`NOTICE`](../NOTICE).

Written 2026-10-05, before any district other than the tuning district was run with Omni-Compass.

## Why CityLearn

Our own 656-muscle models show the mechanism; they cannot prove it on equipment we did not write. CityLearn
(Intelligent Environments Lab, University of Texas at Austin; MIT license; github.com/intelligent-environments-lab/citylearn)
is an independent, widely used simulator of real buildings from measured data: each building's load, its solar
panels and its battery, hour by hour for a year, with its own controllers and its own scoring. Neither side built it to
win. Evidence class: an independent recognized simulator.

## The arms

- **Native:** CityLearn's own rule-based battery controller (`citylearn.agents.rbc.BasicRBC`), unchanged.
- **Native + Omni-Compass:** the same controller, with the compass law (`omnicompass/compass_law.py`) on top of its battery
  commands (`tools/run_citylearn.py`). The reading is the district's draw without its batteries the hour before (the
  demand the batteries answer, never their own effect); its band is the 10th to the 90th percentile of the past week's
  draw (only hours already seen). A positive force pushes every battery command toward discharge, a negative force
  toward charge, by at most 0.5 of the command's range, always inside the battery's own limits. The adjustment glides:
  it changes by at most 0.05 an hour. At 90% of the year every command is handed back to the native controller.

## How the settings were chosen (disclosed)

On the tuning district only, `citylearn_challenge_2022_phase_1` (5 buildings):

| Wiring | Bill | Electricity bought | Carbon | Daily peak | Highest peak | Ramping |
|---|---:|---:|---:|---:|---:|---:|
| Reading the draw with the batteries in it (a feedback loop) | +3.8% | -1.5% | +1.5% | +17.0% | +29.1% | +218% |
| Reading the draw without the batteries, no glide | -19.3% | -18.2% | -16.5% | -15.5% | -1.4% | +16.1% |
| ... glide 0.1 an hour | -17.3% | -20.2% | -17.8% | -17.5% | -1.4% | +1.8% |
| **... glide 0.05 an hour (frozen)** | **-10.5%** | **-17.8%** | **-14.7%** | **-11.9%** | **-1.4%** | **-4.4%** |
| ... glide 0.03 an hour | -8.6% | -15.8% | -12.9% | -9.6% | -1.4% | -7.5% |

(Change against native; CityLearn's own scores, lower is better.) Frozen: gain 0.5, response 1 hour, glide 0.05 an
hour: the setting at which every score was better than native on the tuning district. The tuning district is not
counted in the confirmation.

## The confirmation (untouched districts)

Every other CityLearn district that runs with the native controller: `citylearn_challenge_2022_phase_2`,
`citylearn_challenge_2022_phase_3`, `citylearn_challenge_2022_phase_all`, `citylearn_challenge_2021`,
`citylearn_challenge_2020_climate_zone_1` to `_4`, and `citylearn_challenge_2023_phase_1`. Each district is one
deterministic year, native and native + Omni-Compass. Reported per district and across districts: every CityLearn
score, native, native + Omni-Compass, the change, and read in words (better or worse), with the number of districts
better and worse for each score. Workflow `citylearn`; the report is written to results/citylearn/CITYLEARN.md when it has run.

## Round 1 result, and the amendment written before round 2 (2026-10-05)

Round 1 (workflow `citylearn`, run 37253566738, report `results/citylearn/round1/CITYLEARN.md`, raw files
`results/live/raw/run-37253566738/`) split by the kind of
storage in the district:

| Districts | Bill | Electricity bought | Carbon | Daily peak | Highest peak | Ramping |
|---|---|---|---|---|---|---|
| 2022 phases 2, 3 and all (electric batteries; 5, 7, 17 buildings) | -4.2% to -10.8% | -8.9% to -16.9% | -6.6% to -14.1% | -11.0% to -14.0% | -2.7% to +0.5% | -7.1% to +3.4% |
| 2020 climate zones 1-4 and 2021 (cold and hot water tanks; 9 buildings) | the same | -0.0% to -0.8% | -0.5% to +0.1% | +5.5% to +11.5% (worse) | +10.4% to +28.1% (worse) | +23.5% to +31.4% (worse) |
| 2023 phase 1 (720 hours, 3 buildings) | +0.3% | -0.1% | -0.8% | -4.6% | the same | +25.3% (worse) |

The cause: the wiring pushed every storage command the same way from the district's electricity reading, the water
tanks (cooling_storage, dhw_storage) included. A tank is a thermal muscle; moving when it charges by an electricity
reading made the peaks worse.

**Amendment (one wire, one muscle):** the compass steers only the electric batteries (`electrical_storage`) from the
electricity reading; every water tank stays native (it would need its own wire and its own reading, the tank's
temperature). A district with no electric battery is run and reported with Omni-Compass steering nothing. Gain,
response, glide and band are unchanged. Round 1's districts have been seen and are not the test of this amendment.

**Round 2, the untouched districts:** every other district CityLearn ships that runs with its rule-based controller:
`baeda_3dem`, `ca_alameda_county_neighborhood`, `citylearn_challenge_2022_phase_all_demand_response`,
`citylearn_challenge_2022_phase_all_plus_evs`, `citylearn_challenge_2022_phase_all_robustness`,
`citylearn_challenge_2023_phase_2_local_evaluation`, `citylearn_challenge_2023_phase_2_online_evaluation_1` to `_3`,
and the `citylearn_challenge_2023_phase_3` sets. Disclosed: the three 2022 variants share buildings with the 2022
districts of round 1 (different scenarios: demand response, electric vehicles, robustness). A district whose files the
rule-based controller cannot run is reported as such, never left out silently. Reported as in round 1, round 1 kept
beside it.


**Round 2, running it (2026-10-05, before any of its scores were read):** nine districts stopped before a score. Six of
the newer districts size their solar panels with NREL's System Advisor Model (PySAM), which the runner lacked. The three
three-phase demonstration districts ship with CityLearn's non-flat interface, which its own rule-based controller
refuses. The runner now installs PySAM and opens every district with the flat interface. These are harness fixes only:
the controller, gain, response, glide and band are unchanged, and both arms see the same district.

**Round 2, the result (2026-10-05, GitHub run 37271184088, `results/citylearn/round2/CITYLEARN.md`):** four districts
ran to the end: Alameda County, Travis County, Chittenden County and the 2022 robustness district. Electricity bought
was lower in all four (2.1-14.7%), the daily peak lower in all four (0.8-14.0%), and hour-to-hour ramping lower in all
four (1.3-7.2%). The robustness district came out bill 8.6% lower, carbon 11.9% lower and daily peak 14.0% lower. Its
monthly load unevenness was 0.11% higher, the one row worse than native, reported as measured. In the other three
districts the bill and carbon came out the same. Five districts cannot be run by CityLearn's own rule-based controller in
any arm: they need CityLearn's entity interface, which that controller refuses, or they carry an appliance action it
does not know. Each is listed in the report with CityLearn's own message.
