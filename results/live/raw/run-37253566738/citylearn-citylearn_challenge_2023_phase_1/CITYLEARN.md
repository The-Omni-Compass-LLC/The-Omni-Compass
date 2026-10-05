# Omni-Compass on top of CityLearn's own controller

CityLearn 3.0.2 (Intelligent Environments Lab, University of Texas at Austin; MIT license): an independent simulator of real buildings from measured data, with its own controllers and its own scoring. Native: CityLearn's rule-based battery controller (BasicRBC). Native + Omni: the same controller with the bowl law on top of its battery commands (gain 0.5, response 1.0 h, glide 0.05 an hour, band from the past week's district draw, handed back at 90% of the year). Every number is CityLearn's own score: the controller over no battery at all, lower is better for every row. Evidence class: an independent recognized simulator (not our model).

## citylearn_challenge_2023_phase_1: 3 buildings, 720 hours

Omni-Compass moved the commands in 625 hours; every command handed back at 90%: yes.

| CityLearn score (over no battery; lower is better) | Native | Native + Omni | Change | Reading |
|---|---:|---:|---:|---|
| electricity bill (`cost_total`) | 1.8368 | 1.8430 | +0.34% | WORSE: more electricity bill |
| electricity bought (`electricity_consumption_total`) | 1.8916 | 1.8892 | -0.13% | better: less electricity bought |
| carbon (`carbon_emissions_total`) | 1.8808 | 1.8659 | -0.79% | better: less carbon |
| daily peak draw (`daily_peak_average`) | 1.3043 | 1.2441 | -4.61% | better: less daily peak draw |
| highest peak (`all_time_peak_average`) | 1.0886 | 1.0886 | +0.00% | same |
| ramping (swings hour to hour) (`ramping_average`) | 0.9318 | 1.1678 | +25.33% | WORSE: more ramping (swings hour to hour) |
| daily load unevenness (`daily_one_minus_load_factor_average`) | 0.7120 | 0.6557 | -7.92% | better: less daily load unevenness |
| monthly load unevenness (`monthly_one_minus_load_factor_average`) | 0.8333 | 0.8337 | +0.06% | WORSE: more monthly load unevenness |
| distance from zero net energy (`zero_net_energy`) | 1.9008 | 1.8984 | -0.13% | better: less distance from zero net energy |
| energy not served (`annual_normalized_unserved_energy_total`) | 0.0000 | 0.0000 | +36.30% | same |
| time uncomfortable (`discomfort_proportion`) | 0.9600 | 0.9485 | -1.19% | better: less time uncomfortable |

## Across every district

The tuning district is left out of this table.

| CityLearn score | Districts better | Districts worse | Mean change |
|---|---:|---:|---:|
| electricity bill | 0 of 1 | 1 of 1 | +0.34% |
| electricity bought | 1 of 1 | 0 of 1 | -0.13% |
| carbon | 1 of 1 | 0 of 1 | -0.79% |
| daily peak draw | 1 of 1 | 0 of 1 | -4.61% |
| highest peak | 0 of 1 | 0 of 1 | +0.00% |
| ramping (swings hour to hour) | 0 of 1 | 1 of 1 | +25.33% |
| daily load unevenness | 1 of 1 | 0 of 1 | -7.92% |
| monthly load unevenness | 0 of 1 | 1 of 1 | +0.06% |
| distance from zero net energy | 1 of 1 | 0 of 1 | -0.13% |
| energy not served | 0 of 1 | 0 of 1 | +36.30% |
| time uncomfortable | 1 of 1 | 0 of 1 | -1.19% |
