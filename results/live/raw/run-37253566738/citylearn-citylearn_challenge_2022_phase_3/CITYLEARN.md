# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2022_phase_3: 7 buildings, 8,760 hours

Omni-Compass moved the commands in 7,854 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.0848 | 1.0395 | -4.17% | better: less electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.1573 | 1.0544 | -8.89% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.1155 | 1.0414 | -6.65% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.0973 | 0.9770 | -10.96% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 0.9942 | 0.9987 | +0.45% | WORSE: more highest peak |
| ramping (swings hour to hour) (`ramping_average`) | 1.1814 | 1.2213 | +3.37% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 1.0176 | 0.9684 | -4.83% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.9838 | 0.9784 | -0.55% | better: less monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.0809 | 1.0454 | -3.28% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 |  | same |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 1 of 1 | 0 of 1 | -4.17% |
| electricity bought | 1 of 1 | 0 of 1 | -8.89% |
| carbon | 1 of 1 | 0 of 1 | -6.65% |
| daily peak draw | 1 of 1 | 0 of 1 | -10.96% |
| highest peak | 0 of 1 | 1 of 1 | +0.45% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +3.37% |
| daily load unevenness | 1 of 1 | 0 of 1 | -4.83% |
| monthly load unevenness | 1 of 1 | 0 of 1 | -0.55% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -3.28% |
