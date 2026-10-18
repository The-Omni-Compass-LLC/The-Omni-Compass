# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2020_climate_zone_2: 9 buildings, 8,760 hours

Omni-Compass moved the commands in 7,834 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0495 | 1.0415 | -0.76% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0293 | 1.0240 | -0.52% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.0700 | 1.1525 | +7.70% | WORSE: more daily peak draw |
| highest peak (`all_time_peak_average`) | 0.7823 | 0.9732 | +24.40% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2416 | 1.5746 | +26.82% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0746 | 1.1336 | +5.49% | WORSE: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9642 | 1.0684 | +10.81% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0148 | 1.0213 | +0.64% | WORSE: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -55.25% | better: less energy not served |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 0 of 1 | +0.00% |
| electricity bought | 1 of 1 | 0 of 1 | -0.76% |
| carbon | 1 of 1 | 0 of 1 | -0.52% |
| daily peak draw | 0 of 1 | 1 of 1 | +7.70% |
| highest peak | 0 of 1 | 1 of 1 | +24.40% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +26.82% |
| daily load unevenness | 0 of 1 | 1 of 1 | +5.49% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +10.81% |
| distance from zero net energy | 0 of 1 | 1 of 1 | +0.64% |
| energy not served | 1 of 1 | 0 of 1 | -55.25% |
