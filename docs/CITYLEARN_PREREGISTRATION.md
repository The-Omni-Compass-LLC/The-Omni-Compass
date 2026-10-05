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
- **Native + Omni-Compass:** the same controller, with the bowl law (`omnicompass/bowl.py`) on top of its battery
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
