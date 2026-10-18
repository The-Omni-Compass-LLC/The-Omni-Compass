# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2020_climate_zone_3: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,836 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0302 | 1.0281 | -0.21% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0110 | 1.0101 | -0.09% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.0407 | 1.1527 | +10.77% | WORSE: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.7778 | 0.9961 | +28.08% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2660 | 1.6226 | +28.16% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0711 | 1.1677 | +9.02% | WORSE: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9709 | 1.0811 | +11.35% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0066 | 1.0117 | +0.51% | WORSE: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -49.02% | same |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 0 of 1 | +0.00% |
| electricity bought | 1 of 1 | 0 of 1 | -0.21% |
| carbon | 1 of 1 | 0 of 1 | -0.09% |
| daily peak draw | 0 of 1 | 1 of 1 | +10.77% |
| highest peak | 0 of 1 | 1 of 1 | +28.08% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +28.16% |
| daily load unevenness | 0 of 1 | 1 of 1 | +9.02% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +11.35% |
| distance from zero net energy | 0 of 1 | 1 of 1 | +0.51% |
| energy not served | 0 of 1 | 0 of 1 | -49.02% |
