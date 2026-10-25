# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39821393310 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39840016313 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39860237154 | `15915c961cd2` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,194 | +0.9% (+0.8 to +1.0) | +0.8% (+0.1 to +1.6) | +1.1% (+0.9 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.797 | +1.0% (+0.9 to +1.0) | +0.8% (+0.1 to +1.5) | +1.2% (+0.9 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.64 | 5.64 | -0.1% (-0.2 to +0.1) | +0.1% (-0.1 to +0.2) | -0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.73 | 5.75 | +0.2% (-0.2 to +0.6) | +0.2% (-0.1 to +0.6) | +0.0% (-0.4 to +0.5) | STEADY, under the floor (the three runs' mean 0.15%) |
| latency, mean (ms) | 1.31 | 1.27 | -3.0% (-3.6 to -2.5) | -2.3% (-5.4 to +0.8) | -3.7% (-4.3 to -3.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.9 | +2.9% (+1.6 to +4.2) | +1.9% (+0.4 to +3.3) | +2.8% (+2.6 to +2.9) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% (+1.5 to +2.6) | +1.4% (+0.3 to +2.5) | +2.0% (+1.9 to +2.2) | **power given in all three of our runs** |
| keys evicted | 138,199 | 133,964 | -3.1% (-3.3 to -2.8) | -2.6% (-5.4 to +0.1) | -3.8% (-4.9 to -2.8) | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.127 | +1.0% (-16.5 to +18.6) | -0.2% (-53.7 to +53.3) | +14.8% (-57.7 to +87.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 221.8 | 224.6 | +1.2% (-19.2 to +21.7) | +0.0% (-59.9 to +59.9) | +15.4% (-59.9 to +90.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.417 | 0.418 | +0.3% (-20.3 to +20.8) | -0.8% (-60.1 to +58.5) | +14.1% (-61.4 to +89.7) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 20.3 | +20.3 (+17.5 to +23.2) | +19.7 (+12.1 to +27.3) | +23 (+23 to +23) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.0) | +0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.03%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.718 | -0.0% (-0.1 to +0.1) | -0.1% (-0.1 to +0.0) | +0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% (-0.2 to +0.4) | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% (-0.2 to +0.7) | +0.2% (-0.2 to +0.5) | -0.1% (-0.6 to +0.4) | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 1.74 | 1.75 | +0.3% (-0.2 to +0.8) | +0.3% (-0.5 to +1.1) | -0.1% (-1.5 to +1.2) | STEADY, under the floor (the three runs' mean 0.16%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.5 | -2.4% (-3.1 to -1.8) | -3.2% (-7.1 to +0.7) | -2.3% (-3.0 to -1.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 57.2 | 56.5 | -1.1% (-1.8 to -0.4) | -2.0% (-6.4 to +2.3) | -1.0% (-1.8 to -0.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 71,754 | 71,790 | +0.0% (-0.2 to +0.3) | +0.2% (+0.0 to +0.4) | -0.0% (-0.8 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.147 | -2.9% (-8.5 to +2.7) | -10.3% (-62.1 to +41.5) | -1.7% (-99.0 to +95.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 102.7 | 99.1 | -3.5% (-10.5 to +3.6) | -11.3% (-67.9 to +45.4) | -1.4% (-102.0 to +99.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.53 | 0.512 | -3.4% (-10.4 to +3.5) | -11.2% (-68.0 to +45.6) | -1.4% (-101.9 to +99.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +7.33 (+1.6 to +13.1) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,282 | +1.4% (+0.8 to +2.0) | +1.1% (-0.2 to +2.5) | +1.4% (+1.1 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.856 | +1.3% (+0.8 to +1.9) | +1.1% (-0.3 to +2.6) | +1.5% (+0.8 to +2.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.24 | 5.22 | -0.2% (-1.2 to +0.7) | -0.4% (-2.2 to +1.3) | -0.6% (-2.6 to +1.4) | STEADY, under the floor (the three runs' mean 0.42%) |
| latency, 99th percentile (ms) | 5.39 | 5.28 | -2.1% (-11.0 to +6.8) | -0.2% (-2.1 to +1.8) | -1.8% (-8.8 to +5.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.9 | 0.831 | -7.6% (-10.9 to -4.3) | -5.2% (-12.9 to +2.5) | -7.3% (-9.8 to -4.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.8 | +1.3% (+0.3 to +2.3) | +0.6% (-1.3 to +2.6) | +1.5% (+0.2 to +2.7) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.3 | 61.6 | +0.6% (-1.0 to +2.1) | +0.4% (-1.5 to +2.3) | +0.8% (+0.0 to +1.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 103,523 | 96,008 | -7.3% (-10.0 to -4.5) | -6.1% (-14.3 to +2.1) | -7.9% (-11.7 to -4.0) | shown, not judged |
| host CPU busy (share of the run) | 0.0658 | 0.0681 | +3.6% (-3.0 to +10.2) | +8.7% (-22.8 to +40.3) | +8.1% (-3.0 to +19.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 115.8 | 121.0 | +4.5% (-2.0 to +11.1) | +10.7% (-23.6 to +45.0) | +10.4% (-2.5 to +23.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.21 | +3.1% (-3.3 to +9.6) | +9.4% (-24.3 to +43.2) | +8.8% (-4.1 to +21.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 20.0 | +20 (+17.5 to +22.5) | +19.7 (+9.32 to +30) | +22 (+17.7 to +26.3) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (12 trials, 0 allowed, 2 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused); left native (13 trials, 0 allowed, 2 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); run C: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.5 | 937.3 | +1.3% (+1.2 to +1.3) | +1.3% (+1.1 to +1.5) | +1.2% (+1.2 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.2 to +1.4) | +1.3% (+1.1 to +1.5) | +1.2% (+1.2 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% (-0.0 to +0.1) | +0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% (-0.0 to +0.5) | +0.2% (-0.1 to +0.6) | +0.1% (-0.1 to +0.3) | STEADY, under the floor (the three runs' mean 0.19%) |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% (-2.1 to -1.4) | -1.8% (-2.1 to -1.5) | -1.8% (-2.3 to -1.3) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+2.1 to +2.3) | +2.7% (+1.3 to +4.2) | +2.3% (+1.9 to +2.7) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.3 to +2.5) | +2.0% (+1.8 to +2.1) | +2.1% (+2.0 to +2.2) | **power given in all three of our runs** |
| keys evicted | 243,183 | 236,802 | -2.6% (-6.3 to +1.0) | -2.8% (-4.1 to -1.4) | -3.4% (-3.5 to -3.3) | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.142 | +3.8% (-42.3 to +49.8) | +2.7% (-16.6 to +22.0) | -2.0% (-35.9 to +31.8) | **the runs disagree** |
| host CPU-seconds | 228.5 | 238.9 | +4.5% (-49.3 to +58.3) | +3.4% (-20.2 to +27.0) | -2.2% (-40.3 to +35.9) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.549 | 0.566 | +3.2% (-50.2 to +56.6) | +2.0% (-21.5 to +25.6) | -3.3% (-41.0 to +34.3) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 13.3 | +13.3 (+11.9 to +14.8) | +14.3 (+11.5 to +17.2) | +13 (+8.03 to +18) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 12 gauge-rows GAIN, 0 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 3 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
