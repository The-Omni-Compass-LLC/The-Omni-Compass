# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2020_climate_zone_1: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,827 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0269 | 1.0264 | -0.05% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0086 | 1.0089 | +0.03% | WORSE: more carbon |
| daily peak draw (`daily_peak_average`) | 1.0240 | 1.1419 | +11.51% | WORSE: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.8778 | 1.0535 | +20.02% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2513 | 1.6443 | +31.40% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0534 | 1.1616 | +10.27% | WORSE: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9784 | 1.0967 | +12.09% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0092 | 1.0133 | +0.40% | WORSE: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -57.04% | better: less energy not served |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 0 of 1 | +0.00% |
| electricity bought | 1 of 1 | 0 of 1 | -0.05% |
| carbon | 0 of 1 | 1 of 1 | +0.03% |
| daily peak draw | 0 of 1 | 1 of 1 | +11.51% |
| highest peak | 0 of 1 | 1 of 1 | +20.02% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +31.40% |
| daily load unevenness | 0 of 1 | 1 of 1 | +10.27% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +12.09% |
| distance from zero net energy | 0 of 1 | 1 of 1 | +0.40% |
| energy not served | 1 of 1 | 0 of 1 | -57.04% |
