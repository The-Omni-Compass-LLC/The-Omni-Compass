# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2022_phase_2: 5 buildings, 8,760 hours

Omni-Compass moved the commands in 7,855 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.1080 | 0.9880 | -10.83% | better: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.2124 | 1.0078 | -16.87% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1665 | 1.0021 | -14.09% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.1124 | 0.9764 | -12.23% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 0.9983 | 1.0000 | +0.17% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.1231 | 1.0785 | -3.97% | better: less ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.9787 | 0.9888 | +1.03% | WORSE: more daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9828 | 0.9895 | +0.68% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.1970 | 1.0921 | -8.77% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 1 of 1 | 0 of 1 | -10.83% |
| electricity bought | 1 of 1 | 0 of 1 | -16.87% |
| carbon | 1 of 1 | 0 of 1 | -14.09% |
| daily peak draw | 1 of 1 | 0 of 1 | -12.23% |
| highest peak | 0 of 1 | 1 of 1 | +0.17% |
| ramping (swings hour to hour) | 1 of 1 | 0 of 1 | -3.97% |
| daily load unevenness | 0 of 1 | 1 of 1 | +1.03% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +0.68% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -8.77% |
