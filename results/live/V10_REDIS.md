# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39108184403 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39115246841 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39123587108 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.0% (+0.3 to +1.8) | +1.0% (+0.2 to +1.7) | +0.8% (+0.5 to +1.2) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.798 | +1.0% (+0.4 to +1.7) | +1.0% (+0.2 to +1.7) | +0.9% (+0.5 to +1.2) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.52 | 5.52 | +0.0% (-0.2 to +0.3) | +0.0% (-0.2 to +0.3) | +0.0% (-0.5 to +0.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.59 | 5.6 | +0.1% (-0.2 to +0.3) | +0.1% (-0.1 to +0.3) | +0.7% (-0.8 to +2.1) | STEADY, under the floor (the three runs' mean 0.29%) |
| latency, mean (ms) | 1.24 | 1.2 | -3.3% (-6.7 to +0.1) | -2.8% (-5.3 to -0.4) | -2.1% (-3.3 to -0.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.4% (+0.8 to +3.9) | +1.9% (-0.7 to +4.6) | +1.9% (-0.3 to +4.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% (+0.6 to +2.9) | +1.6% (-0.4 to +3.6) | +1.5% (+0.1 to +2.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 138,152 | 133,440 | -3.4% (-6.1 to -0.8) | -3.1% (-6.0 to -0.2) | -2.7% (-4.1 to -1.3) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.105 | +1.0% (-12.4 to +14.4) | -5.5% (-6.2 to -4.8) | -2.3% (-15.0 to +10.3) | **the runs disagree** |
| host CPU-seconds | 182.7 | 184.6 | +1.0% (-13.7 to +15.8) | -6.0% (-6.7 to -5.2) | -2.7% (-16.7 to +11.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.343 | +0.0% (-15.4 to +15.5) | -6.9% (-7.0 to -6.7) | -3.5% (-17.2 to +10.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| ceiling changes written (the knob's moves) | 0 | 21.7 | +21.7 (+15.9 to +27.4) | +19.7 (+12.1 to +27.3) | +19 (+14 to +24) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% (-0.2 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.1 to -0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% (-0.1 to +0.2) | -0.0% (-0.3 to +0.3) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% (+0.1 to +0.3) | +0.2% (-0.3 to +0.6) | +0.1% (-0.3 to +0.5) | STEADY, under the floor (the three runs' mean 0.15%) |
| latency, mean (ms) | 1.73 | 1.74 | +0.3% (-0.1 to +0.7) | +0.0% (-0.5 to +0.5) | +0.2% (-0.1 to +0.5) | STEADY, under the floor (the three runs' mean 0.19%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.4 | -2.5% (-2.8 to -2.1) | -2.5% (-2.7 to -2.3) | -2.3% (-2.8 to -1.9) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% (-1.6 to -0.8) | -1.2% (-1.3 to -1.0) | -1.0% (-1.3 to -0.7) | **GAIN in all three of our runs** |
| keys evicted | 71,693 | 71,860 | +0.2% (+0.2 to +0.3) | +0.0% (-0.0 to +0.1) | +0.0% (-0.3 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.142 | -7.7% (-36.2 to +20.7) | -5.8% (-52.5 to +40.9) | -7.9% (-48.1 to +32.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 106.1 | 96.3 | -9.2% (-42.4 to +24.0) | -6.7% (-61.1 to +47.8) | -9.0% (-53.8 to +35.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.547 | 0.497 | -9.1% (-42.3 to +24.1) | -6.7% (-61.1 to +47.8) | -9.0% (-53.7 to +35.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,281 | +1.1% (+0.6 to +1.7) | +1.0% (-1.1 to +3.0) | +1.6% (+1.6 to +1.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.855 | +1.1% (+0.6 to +1.7) | +1.0% (-1.1 to +3.1) | +1.7% (+1.6 to +1.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% (-0.3 to +0.2) | +0.0% (-0.1 to +0.1) | -0.0% (-0.8 to +0.7) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.0% (-0.3 to +0.4) | +0.2% (+0.1 to +0.2) | +0.1% (-0.3 to +0.5) | STEADY, under the floor (the three runs' mean 0.11%) |
| latency, mean (ms) | 1.06 | 1.01 | -5.0% (-6.9 to -3.1) | -3.9% (-13.2 to +5.3) | -7.3% (-7.7 to -6.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.3 | +0.5% (-1.6 to +2.6) | +0.2% (-3.3 to +3.7) | +1.4% (+0.2 to +2.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 61.3 | +0.0% (-1.3 to +1.4) | -0.0% (-3.6 to +3.5) | +1.0% (+0.2 to +1.8) | STEADY, under the floor (the three runs' mean 0.34%) |
| keys evicted | 103,421 | 97,098 | -6.1% (-9.1 to -3.2) | -5.1% (-16.7 to +6.4) | -8.9% (-9.2 to -8.6) | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.116 | -6.5% (-15.0 to +2.1) | -1.7% (-7.8 to +4.3) | +4.1% (-5.8 to +13.9) | **the runs disagree** |
| host CPU-seconds | 207.7 | 192.7 | -7.2% (-16.9 to +2.5) | -1.8% (-9.0 to +5.4) | +4.5% (-6.9 to +15.9) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.334 | -8.2% (-18.1 to +1.6) | -2.8% (-8.0 to +2.5) | +2.8% (-8.6 to +14.3) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+21 to +21) | +20.3 (+12.7 to +27.9) | +22.3 (+19.5 to +25.2) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (12 trials, 0 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (11 trials, 0 allowed, 3 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 2 refused); left native (12 trials, 0 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.5 | 937.2 | +1.3% (+1.1 to +1.4) | +1.2% (+1.2 to +1.3) | +1.3% (+1.1 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.2 to +1.4) | +1.2% (+1.2 to +1.3) | +1.3% (+1.2 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.49 | 5.49 | +0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | -0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.56 | 5.56 | +0.1% (-0.1 to +0.2) | +0.2% (-0.1 to +0.4) | +0.3% (-0.1 to +0.6) | STEADY, under the floor (the three runs' mean 0.17%) |
| latency, mean (ms) | 2.13 | 2.09 | -1.9% (-2.3 to -1.4) | -1.7% (-2.0 to -1.5) | -1.8% (-2.5 to -1.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.3% (+2.1 to +2.6) | +2.2% (+2.1 to +2.3) | +2.3% (+2.1 to +2.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 62.0 | +2.1% (+2.0 to +2.3) | +2.0% (+2.0 to +2.1) | +1.7% (+1.5 to +1.8) | **power given in all three of our runs** |
| keys evicted | 243,216 | 234,806 | -3.5% (-3.6 to -3.3) | -3.4% (-3.5 to -3.3) | -1.0% (-1.3 to -0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.096 | -12.9% (-20.3 to -5.5) | -2.6% (-22.6 to +17.4) | +2.4% (-15.8 to +20.7) | **the runs disagree** |
| host CPU-seconds | 193.7 | 166.3 | -14.2% (-21.9 to -6.5) | -2.9% (-25.7 to +20.0) | +2.9% (-18.0 to +23.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.394 | -15.3% (-22.9 to -7.6) | -4.0% (-26.7 to +18.7) | +1.5% (-19.4 to +22.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 13.7 | +13.7 (+10.8 to +16.5) | +13 (+13 to +13) | +16 (+16 to +16) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run C: acting: 64 to 80 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 0 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 STEADY, 6 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
