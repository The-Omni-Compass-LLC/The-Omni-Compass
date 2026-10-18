# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2021: 9 buildings, 35,040 hours

Omni-Compass moved the commands in 31,363 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0000 | 1.0000 | +0.00% | same |
| electricity bought (`electricity_consumption_total`) | 1.0358 | 1.0327 | -0.30% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.0173 | 1.0183 | +0.09% | WORSE: more carbon |
| daily peak draw (`daily_peak_average`) | 1.1463 | 1.2094 | +5.50% | WORSE: more daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0570 | 1.1672 | +10.43% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.2989 | 1.6920 | +30.26% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.1975 | 1.2352 | +3.15% | WORSE: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 1.0641 | 1.1725 | +10.19% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0190 | 1.0202 | +0.12% | WORSE: more distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | -55.92% | better: less energy not served |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 0 of 1 | +0.00% |
| electricity bought | 1 of 1 | 0 of 1 | -0.30% |
| carbon | 0 of 1 | 1 of 1 | +0.09% |
| daily peak draw | 0 of 1 | 1 of 1 | +5.50% |
| highest peak | 0 of 1 | 1 of 1 | +10.43% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +30.26% |
| daily load unevenness | 0 of 1 | 1 of 1 | +3.15% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +10.19% |
| distance from zero net energy | 0 of 1 | 1 of 1 | +0.12% |
| energy not served | 1 of 1 | 0 of 1 | -55.92% |
