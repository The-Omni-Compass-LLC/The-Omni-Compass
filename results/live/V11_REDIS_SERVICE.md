# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149267883 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39158996767 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39167569649 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,192 | +0.7% (-0.1 to +1.4) | +0.6% (+0.2 to +1.1) | +1.1% (+0.5 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.79 | 0.795 | +0.7% (-0.1 to +1.4) | +0.6% (+0.1 to +1.1) | +1.1% (+0.5 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% (-0.1 to +0.3) | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% (-0.0 to +0.5) | +0.2% (+0.1 to +0.2) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.16%) |
| latency, mean (ms) | 1.34 | 1.32 | -1.7% (-4.4 to +1.0) | -1.9% (-3.8 to +0.0) | -3.5% (-5.1 to -1.9) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.9 | +1.4% (+0.3 to +2.6) | +1.0% (-0.5 to +2.5) | +2.9% (+0.3 to +5.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.2 | 61.8 | +1.0% (-0.1 to +2.1) | +0.6% (-0.7 to +2.0) | +2.1% (-0.2 to +4.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| keys evicted | 138,050 | 135,913 | -1.5% (-4.0 to +0.9) | -1.5% (-3.8 to +0.8) | -3.4% (-6.4 to -0.5) | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.131 | -1.5% (-30.4 to +27.5) | +6.8% (-46.6 to +60.2) | +3.1% (-28.4 to +34.6) | **the runs disagree** |
| host CPU-seconds | 224.0 | 219.6 | -1.9% (-35.1 to +31.2) | +7.5% (-53.8 to +68.8) | +3.6% (-31.2 to +38.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.409 | -2.6% (-35.8 to +30.6) | +6.8% (-54.8 to +68.5) | +2.5% (-31.5 to +36.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 20.3 | +20.3 (+3.79 to +36.9) | +19.7 (+8.46 to +30.9) | +22 (+17.7 to +26.3) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (13 trials, 2 allowed, 0 refused); acting: 56 to 72 (13 trials, 2 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run B: acting: 56 to 72 (14 trials, 2 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 56 to 72 (14 trials, 2 allowed, 0 refused); run C: acting: 56 to 72 (13 trials, 2 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to -0.0) | -0.1% (-0.1 to -0.1) | EVEN, under the floor (the three runs' mean 0.07%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.0) | -0.1% (-0.1 to -0.1) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% (-0.3 to +0.3) | +0.0% (-0.1 to +0.1) | -0.0% (-0.8 to +0.8) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.1% (-0.3 to +0.5) | +0.3% (+0.0 to +0.5) | +0.1% (-0.6 to +0.7) | EVEN, under the floor (the three runs' mean 0.14%) |
| latency, mean (ms) | 1.68 | 1.69 | +0.3% (-1.0 to +1.7) | +0.5% (+0.0 to +0.9) | +0.3% (-0.6 to +1.3) | EVEN, under the floor (the three runs' mean 0.38%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.1 | -2.9% (-5.9 to +0.0) | -3.3% (-6.2 to -0.5) | -2.2% (-2.4 to -2.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 57.2 | 56.2 | -1.7% (-5.1 to +1.8) | -2.1% (-5.3 to +1.2) | -0.9% (-1.1 to -0.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,762 | 71,838 | +0.1% (-0.2 to +0.4) | +0.2% (-0.0 to +0.5) | +0.2% (+0.2 to +0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.117 | -12.5% (-32.4 to +7.5) | +3.6% (-57.3 to +64.5) | +21.5% (-28.5 to +71.5) | **the runs disagree** |
| host CPU-seconds | 95.5 | 82.1 | -14.1% (-35.4 to +7.3) | +4.6% (-65.8 to +75.0) | +24.6% (-35.7 to +84.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.493 | 0.424 | -14.0% (-35.3 to +7.3) | +4.7% (-65.7 to +75.1) | +24.7% (-35.7 to +85.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 7.33 | +7.33 (+1.6 to +13.1) | +7.33 (+1.6 to +13.1) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,286 | +1.6% (+1.0 to +2.1) | +1.6% (+0.9 to +2.4) | +1.4% (+0.8 to +2.0) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.858 | +1.6% (+1.0 to +2.1) | +1.6% (+0.9 to +2.4) | +1.4% (+0.7 to +2.0) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.48 | 5.47 | -0.2% (-0.5 to +0.1) | -0.1% (-0.2 to +0.0) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.09%) |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% (-0.1 to -0.0) | +0.0% (-0.2 to +0.2) | +0.2% (-0.0 to +0.5) | EVEN, under the floor (the three runs' mean 0.07%) |
| latency, mean (ms) | 0.956 | 0.886 | -7.3% (-9.9 to -4.7) | -7.0% (-10.5 to -3.4) | -6.2% (-9.1 to -3.4) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 63.9 | -0.2% (-4.9 to +4.6) | +1.9% (+0.2 to +3.5) | +0.6% (-0.4 to +1.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 60.8 | -0.8% (-6.1 to +4.5) | +1.4% (+0.5 to +2.3) | -0.1% (-0.5 to +0.3) | **the runs disagree** |
| keys evicted | 103,641 | 95,051 | -8.3% (-11.5 to -5.0) | -8.8% (-12.9 to -4.6) | -7.2% (-10.8 to -3.6) | shown, not judged |
| host CPU busy (share of the run) | 0.0917 | 0.104 | +13.2% (-16.5 to +42.9) | -1.5% (-18.4 to +15.4) | +22.7% (-7.6 to +53.1) | **the runs disagree** |
| host CPU-seconds | 159.7 | 183.5 | +14.9% (-18.1 to +48.0) | -1.6% (-21.2 to +18.1) | +24.0% (-8.6 to +56.6) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.317 | +13.2% (-19.9 to +46.3) | -3.1% (-21.9 to +15.7) | +22.4% (-10.3 to +55.0) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 25.7 | +25.7 (+11.1 to +40.2) | +20.7 (+16.9 to +24.5) | +21 (+16 to +26) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 56 to 64 (14 trials, 1 allowed, 3 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 2 refused); run C: left native (14 trials, 0 allowed, 2 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused); left native (12 trials, 0 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.7 | 937.6 | +1.3% (+1.1 to +1.4) | +1.3% (+1.2 to +1.3) | +1.3% (+1.1 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.1 to +1.5) | +1.3% (+1.2 to +1.3) | +1.3% (+1.1 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.1% (-0.6 to +0.4) | +0.1% (+0.0 to +0.1) | +0.1% (+0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% (-0.5 to +0.6) | +0.2% (+0.1 to +0.4) | +0.2% (+0.1 to +0.3) | EVEN, under the floor (the three runs' mean 0.16%) |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% (-2.9 to -1.1) | -1.7% (-1.8 to -1.6) | -1.7% (-2.2 to -1.3) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+1.5 to +2.8) | +2.5% (+2.0 to +3.1) | +2.3% (+1.0 to +3.6) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.4 to +2.4) | +1.7% (+0.9 to +2.5) | +1.9% (+1.6 to +2.2) | **power given in all three of our runs** |
| keys evicted | 243,123 | 236,726 | -2.6% (-6.1 to +0.9) | -1.8% (-5.3 to +1.7) | -2.6% (-6.2 to +1.0) | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.136 | -2.6% (-5.5 to +0.3) | +6.4% (-12.9 to +25.8) | +2.4% (-14.8 to +19.6) | **the runs disagree** |
| host CPU-seconds | 233.7 | 226.9 | -2.9% (-6.4 to +0.5) | +7.7% (-14.4 to +29.8) | +2.9% (-16.9 to +22.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.538 | -4.1% (-7.7 to -0.6) | +6.4% (-15.4 to +28.1) | +1.6% (-18.1 to +21.3) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 15.3 | +15.3 (+9.08 to +21.6) | +15.3 (+10.2 to +20.5) | +14.7 (+10.9 to +18.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run B: acting: 56 to 80 (13 trials, 3 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 1 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run C: acting: 64 to 80 (10 trials, 2 allowed, 1 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 56 to 72 (10 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 0 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 EVEN, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
