# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39109164668 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 5 |
| B | 39116285471 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 5 |
| C | 39124635012 | `8b902df8d857` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,878 | -0.2% (-0.7 to +0.2) | +0.0% (-0.6 to +0.7) | -0.1% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.09%) |
| throughput (operations a second) | 2,895 | 2,887 | -0.3% (-0.7 to +0.2) | +0.0% (-0.6 to +0.7) | -0.1% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, 95th percentile (ms) | 0.367 | 0.364 | -0.9% (-5.4 to +3.6) | -0.2% (-2.7 to +2.4) | +2.2% (-6.5 to +11.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.567 | 0.561 | -1.1% (-7.0 to +4.8) | +0.3% (-1.5 to +2.1) | +0.6% (-6.6 to +7.7) | **the runs disagree** |
| latency, mean (ms) | 0.226 | 0.225 | -0.3% (-6.6 to +5.9) | +0.3% (-1.6 to +2.3) | -1.3% (-5.6 to +3.1) | STEADY, under the floor (the three runs' mean 0.42%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 504.5 | -1.5% (-3.5 to +0.6) | -0.9% (-1.0 to -0.7) | -1.3% (-3.7 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 417.5 | 413.7 | -0.9% (-2.6 to +0.8) | -0.6% (-1.3 to +0.1) | -0.9% (-3.5 to +1.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 680,242 | 688,688 | +1.2% (-2.4 to +4.9) | -0.1% (-3.6 to +3.4) | +2.0% (-1.7 to +5.7) | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.23 | -6.6% (-26.8 to +13.6) | +4.5% (-17.3 to +26.3) | -10.0% (-39.3 to +19.3) | **the runs disagree** |
| host CPU-seconds | 429.2 | 393.1 | -8.4% (-36.1 to +19.3) | +5.5% (-22.3 to +33.3) | -11.8% (-46.3 to +22.8) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.323 | 0.297 | -8.2% (-36.1 to +19.7) | +5.4% (-22.8 to +33.6) | -11.8% (-46.3 to +22.7) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (+2.23 to +5.1) | +4 (+4 to +4) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% (-0.1 to -0.0) | +0.1% (-0.4 to +0.5) | -0.1% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,901 | 2,900 | -0.0% (-0.1 to -0.0) | +0.1% (-0.4 to +0.5) | -0.1% (-0.1 to -0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.322 | 0.326 | +1.2% (-2.3 to +4.8) | -0.3% (-2.8 to +2.2) | +1.1% (-2.5 to +4.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.478 | 0.483 | +1.0% (-1.6 to +3.6) | +0.0% (-1.1 to +1.1) | +1.3% (-1.9 to +4.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.2 | 0.201 | +0.4% (-2.4 to +3.3) | +0.5% (-2.8 to +3.9) | +0.9% (-3.2 to +5.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.1 | -0.8% (-0.9 to -0.6) | -0.8% (-1.8 to +0.3) | -1.2% (-3.4 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 418.7 | 415.5 | -0.8% (-2.4 to +0.8) | +0.1% (-1.6 to +1.9) | -0.7% (-4.1 to +2.8) | STEADY, under the floor (the three runs' mean 0.43%) |
| pages read into the cache (misses) | 709,938 | 704,361 | -0.8% (-21.2 to +19.6) | +3.2% (-7.0 to +13.4) | +1.4% (-2.6 to +5.3) | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.162 | -9.0% (-27.3 to +9.4) | +17.8% (-12.4 to +48.0) | -1.4% (-52.2 to +49.5) | **the runs disagree** |
| host CPU-seconds | 302.6 | 269.5 | -10.9% (-34.6 to +12.7) | +21.0% (-15.3 to +57.4) | -1.8% (-63.8 to +60.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.202 | -10.9% (-34.6 to +12.7) | +21.0% (-15.6 to +57.5) | -1.8% (-63.7 to +60.2) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (+2.23 to +5.1) | +3 (+0.516 to +5.48) | +3 (+0.516 to +5.48) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,888 | -0.1% (-0.1 to +0.0) | -0.1% (-0.1 to +0.0) | -0.0% (-0.4 to +0.4) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% (-0.1 to -0.0) | -0.1% (-0.1 to -0.0) | -0.0% (-0.4 to +0.3) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.436 | 0.435 | -0.2% (-1.2 to +0.8) | -0.2% (-3.6 to +3.2) | -0.9% (-2.9 to +1.0) | STEADY, under the floor (the three runs' mean 0.43%) |
| latency, 99th percentile (ms) | 0.599 | 0.601 | +0.3% (-2.9 to +3.4) | -3.7% (-11.4 to +4.0) | -1.0% (-6.9 to +4.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.222 | 0.222 | +0.1% (-4.0 to +4.2) | +0.5% (-3.1 to +4.2) | -1.2% (-3.2 to +0.7) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 503.2 | -1.7% (-2.5 to -1.0) | -2.2% (-3.8 to -0.6) | -1.9% (-3.2 to -0.6) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 404.1 | 399.2 | -1.2% (-5.7 to +3.2) | -1.4% (-5.1 to +2.2) | -2.5% (-5.8 to +0.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 269,691 | 264,617 | -1.9% (-12.1 to +8.3) | -0.4% (-16.0 to +15.1) | +2.9% (-4.6 to +10.5) | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.161 | -6.2% (-69.9 to +57.5) | +17.6% (-7.8 to +43.1) | -8.9% (-49.2 to +31.4) | **the runs disagree** |
| host CPU-seconds | 117.2 | 107.5 | -8.3% (-85.1 to +68.4) | +20.7% (-8.7 to +50.0) | -10.3% (-57.8 to +37.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.202 | -8.3% (-85.0 to +68.4) | +20.6% (-8.6 to +49.9) | -10.3% (-58.0 to +37.5) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.67 (+2.23 to +5.1) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% (-0.0 to +0.0) | -0.1% (-0.3 to +0.2) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% (-0.0 to +0.0) | -0.1% (-0.3 to +0.1) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.314 | 0.315 | +0.4% (-1.4 to +2.3) | -0.3% (-1.9 to +1.3) | -0.9% (-3.0 to +1.3) | STEADY, under the floor (the three runs' mean 0.24%) |
| latency, 99th percentile (ms) | 0.491 | 0.485 | -1.2% (-4.2 to +1.9) | -0.2% (-1.7 to +1.3) | -0.1% (-1.7 to +1.5) | STEADY, under the floor (the three runs' mean 0.47%) |
| latency, mean (ms) | 0.194 | 0.197 | +1.2% (-1.0 to +3.3) | +1.3% (-5.4 to +7.9) | -0.6% (-14.6 to +13.4) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 494.3 | -3.5% (-15.0 to +8.1) | -1.3% (-4.0 to +1.4) | -0.4% (-0.9 to +0.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| bytes in the cache, mean (MB) | 419.3 | 400.6 | -4.5% (-16.9 to +8.0) | -1.4% (-5.8 to +3.1) | -1.0% (-4.4 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 744,406 | 693,091 | -6.9% (-20.9 to +7.1) | -3.8% (-31.9 to +24.3) | +4.1% (-14.7 to +22.8) | shown, not judged |
| host CPU busy (share of the run) | 0.162 | 0.183 | +12.7% (+4.1 to +21.3) | +24.9% (-22.9 to +72.7) | -22.9% (-75.1 to +29.2) | **the runs disagree** |
| host CPU-seconds | 273.1 | 314.3 | +15.1% (+4.9 to +25.3) | +30.0% (-27.4 to +87.3) | -26.5% (-86.4 to +33.5) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.205 | 0.236 | +15.1% (+4.8 to +25.3) | +30.0% (-27.5 to +87.4) | -26.5% (-86.3 to +33.4) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +3 (+0.516 to +5.48) | +2.67 (-0.202 to +5.54) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (1 trials, 0 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 0 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,644 | 5,662 | +0.3% (-0.1 to +0.8) | +0.2% (-2.0 to +2.4) | +0.7% (-2.5 to +3.9) | STEADY, under the floor (the three runs' mean 0.41%) |
| throughput (operations a second) | 5,665 | 5,682 | +0.3% (-0.2 to +0.8) | +0.2% (-2.0 to +2.4) | +0.7% (-2.5 to +3.9) | STEADY, under the floor (the three runs' mean 0.40%) |
| latency, 95th percentile (ms) | 0.455 | 0.453 | -0.4% (-4.0 to +3.1) | +0.0% (-1.3 to +1.3) | +0.4% (-0.5 to +1.3) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 0.729 | 0.718 | -1.6% (-3.0 to -0.1) | -0.6% (-2.7 to +1.6) | +0.1% (-3.9 to +4.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 0.258 | 0.258 | +0.1% (-4.0 to +4.1) | -2.6% (-5.3 to +0.1) | -2.6% (-7.5 to +2.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.3 | -0.7% (-1.2 to -0.2) | -2.0% (-4.3 to +0.3) | -1.5% (-4.8 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 416.4 | 414.4 | -0.5% (-1.3 to +0.4) | -1.3% (-2.9 to +0.4) | -1.1% (-5.0 to +2.7) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 671,319 | 679,345 | +1.2% (-2.6 to +5.0) | +1.3% (-3.3 to +5.9) | +1.5% (-10.2 to +13.2) | shown, not judged |
| host CPU busy (share of the run) | 0.287 | 0.292 | +1.6% (-6.9 to +10.1) | +0.8% (-13.8 to +15.4) | +3.7% (-19.8 to +27.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 487.5 | 497.8 | +2.1% (-7.9 to +12.1) | +0.8% (-18.6 to +20.1) | +4.3% (-25.2 to +33.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.186 | 0.189 | +1.7% (-8.0 to +11.4) | +0.5% (-20.4 to +21.4) | +3.4% (-25.5 to +32.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused).

**Across 4 untouched workloads: 10 gauge-rows GAIN, 3 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
