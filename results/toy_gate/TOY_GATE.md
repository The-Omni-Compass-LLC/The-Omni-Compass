# The toy gate: the candidate against the engine that stands, in our own models

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_one, as `tools/toy_gate.py` reads a model now): a paired change of 0.5% or more either way is a change and never reads EVEN; it reads its word by the gauge's aim, with "(not clear of the noise)" beside it where its 95% interval over the seeds crosses zero; under 0.5% it reads EVEN, under the floor. Each reading was decided again from the JSON twin's own mean, interval and relative change, and every row whose words moved is printed again, its numbers wearing their words' signs; every seed, number and row is as first written. Where a paragraph below says EVEN for an interval across zero, this rule replaces it. Evidence class S, our own models, never a benchmark result.
<!-- end: read again -->

Seeds 1 to 10, 1.0 day each where a day is run; the standing engine omni-v6 (main at b7b5f319a), the candidate omni-v7 (v7-candidate, digest d6d467b824c585f1). Evidence class S, our own models: a reading here says whether a change shows promise before a real run, never what a benchmark found. Each candidate reading is paired by seed with the standing engine's (the mean change, its 95% interval over the seeds, the word by the gauge's aim: tools/readings.py).

The convey toys were run on 16 October against the corrected candidate (digest d6d467b824c585f1; the quota read corrected, omni_controller/quota.py); the cluster and verdict toys were run on 15 October against the candidate as first pushed (digest 1a0d1d1b91bc49ad), whose cluster and verdict code is the same bytes. candidate_as_first_pushed holds the first candidate's reading on the unreadable quota, the fault the live trials found.

## cluster (a decision every 60 s)

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| machine_hours | 130.669 | 129.211 | 128.920 | =0.23% EVEN, under the floor | +1.12% GAIN (not clear of the noise) | +1.34% GAIN (not clear of the noise) |
| kwh_per_core_hour | 0.036 | 0.035 | 0.035 | =0.14% EVEN, under the floor | +2.34% GAIN | +2.48% GAIN |
| pending_pod_minutes_per_hour | 6.258 | 19.585 | 20.387 | −4.10% LOSS (not clear of the noise) | −212.95% LOSS | −225.77% LOSS (not clear of the noise) |
| hpa_shortfall_minutes_per_hour | 3.650 | 3.656 | 3.656 | =0.00% EVEN, under the floor | =0.17% EVEN, under the floor | =0.17% EVEN, under the floor |
| p95_ms | 80.551 | 81.094 | 81.035 | =0.07% EVEN, under the floor | −0.67% LOSS | −0.60% LOSS (not clear of the noise) |
| alert_minutes | 27.300 | 28.000 | 27.800 | +0.71% GAIN (not clear of the noise) | −2.56% LOSS (not clear of the noise) | −1.83% LOSS (not clear of the noise) |

Counts over all seeds: steps_allowed {'base': 79, 'cand': 65}, steps_refused {'base': 99, 'cand': 99}, trials_abandoned {'base': 149, 'cand': 151}, machines_parked {'base': 1526, 'cand': 1771}, errors {'base': 0, 'cand': 0}

## cluster15 (a decision every 15 s)

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| machine_hours | 130.669 | 186.907 | 131.054 | +29.88% GAIN | +43.04% power given | =0.29% EVEN, under the floor |
| kwh_per_core_hour | 0.036 | 0.033 | 0.035 | +6.32% power given | -8.45% GAIN | -2.66% GAIN |
| pending_pod_minutes_per_hour | 6.258 | 66.732 | 13.186 | -80.24% GAIN | +966.29% LOSS | +110.70% LOSS |
| hpa_shortfall_minutes_per_hour | 3.650 | 3.672 | 3.650 | +0.60% GAIN (not clear of the noise) | −0.60% LOSS (not clear of the noise) | =0.00% EVEN, under the floor |
| p95_ms | 80.551 | 83.090 | 80.792 | +2.77% GAIN | −3.15% LOSS | =0.30% EVEN, under the floor |
| alert_minutes | 27.300 | 29.900 | 27.700 | +7.36% GAIN | −9.52% LOSS | −1.47% LOSS (not clear of the noise) |

Counts over all seeds: steps_allowed {'base': 253, 'cand': 75}, steps_refused {'base': 194, 'cand': 91}, trials_abandoned {'base': 2437, 'cand': 236}, machines_parked {'base': 11200, 'cand': 5315}, errors {'base': 0, 'cand': 0}

## convey

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| requests_served | 31423.739 | 51596.881 | 51596.881 | +0.00% EVEN (identical) | +64.20% GAIN | +64.20% GAIN |
| start_wait_s | 9.793 | 10.652 | 10.652 | +0.00% EVEN (identical) | +8.78% LOSS | +8.78% LOSS |
| start_wait_p95_s | 10.000 | 11.000 | 11.000 | +0.00% EVEN (identical) | +10.00% LOSS | +10.00% LOSS |
| p95_ms | 228.935 | 107.420 | 107.420 | +0.00% EVEN (identical) | -53.08% GAIN | -53.08% GAIN |
| alert_minutes | 0.000 | 0.000 | 0.000 | EVEN (identical) | EVEN (identical) | EVEN (identical) |
| host_busy | 0.282 | 0.371 | 0.371 | +0.00% EVEN (identical) | +31.53% power given | +31.53% power given |
| limit_given_m | 4137.292 | 11062.167 | 11062.167 | +0.00% EVEN (identical) | +167.38% power given | +167.38% power given |
| pod_seconds | 29788.500 | 35179.500 | 35179.500 | +0.00% EVEN (identical) | +18.10% power given | +18.10% power given |

Counts over all seeds: starts {'native': 270, 'base': 210, 'cand': 210}, starts_past_75 {'native': 0, 'base': 0, 'cand': 0}

## verdict

| True extra cost of a give-back step | Allowed, standing | Allowed, candidate |
|---|---|---|
| +0% | 63% | 60% |
| +1% | 56% | 50% |
| +2% | 47% | 39% |
| +3% | 40% | 28% |
| +5% | 26% | 14% |

## convey_unreadable_quota

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| requests_served | 31423.739 | 51596.881 | 51596.881 | +0.00% EVEN (identical) | +64.20% GAIN | +64.20% GAIN |
| start_wait_s | 9.793 | 10.652 | 10.652 | +0.00% EVEN (identical) | +8.78% LOSS | +8.78% LOSS |
| start_wait_p95_s | 10.000 | 11.000 | 11.000 | +0.00% EVEN (identical) | +10.00% LOSS | +10.00% LOSS |
| p95_ms | 228.935 | 107.420 | 107.420 | +0.00% EVEN (identical) | -53.08% GAIN | -53.08% GAIN |
| alert_minutes | 0.000 | 0.000 | 0.000 | EVEN (identical) | EVEN (identical) | EVEN (identical) |
| host_busy | 0.282 | 0.371 | 0.371 | +0.00% EVEN (identical) | +31.53% power given | +31.53% power given |
| limit_given_m | 4137.292 | 11062.167 | 11062.167 | +0.00% EVEN (identical) | +167.38% power given | +167.38% power given |
| pod_seconds | 29788.500 | 35179.500 | 35179.500 | +0.00% EVEN (identical) | +18.10% power given | +18.10% power given |

Counts over all seeds: starts {'native': 270, 'base': 210, 'cand': 210}, starts_past_75 {'native': 0, 'base': 0, 'cand': 0}

The candidate as first pushed (digest 1a0d1d1b91bc49ad), the reading that caught the fault:

| Gauge | Native | Standing | Candidate as first pushed | Against standing | Against native |
|---|---:|---:|---:|---|---|
| requests_served | 31423.739 | 51596.881 | 31423.739 | -39.10% LOSS | +0.00% EVEN (identical) |
| start_wait_s | 9.793 | 10.652 | 9.793 | -8.07% GAIN | +0.00% EVEN (identical) |
| start_wait_p95_s | 10.000 | 11.000 | 10.000 | -9.09% GAIN | +0.00% EVEN (identical) |
| p95_ms | 228.935 | 107.420 | 228.935 | +113.12% LOSS | +0.00% EVEN (identical) |
| alert_minutes | 0.000 | 0.000 | 0.000 | EVEN (identical) | EVEN (identical) |
| host_busy | 0.282 | 0.371 | 0.282 | -23.97% GAIN | +0.00% EVEN (identical) |
| limit_given_m | 4137.292 | 11062.167 | 4137.292 | -62.60% GAIN | +0.00% EVEN (identical) |
| pod_seconds | 29788.500 | 35179.500 | 29788.500 | -15.32% GAIN | +0.00% EVEN (identical) |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
