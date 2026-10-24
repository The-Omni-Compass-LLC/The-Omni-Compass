# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149263618 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39158992412 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39167564949 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,924 | 2,924 | +0.0% (-0.0 to +0.0) | -0.2% (-0.7 to +0.3) | +0.2% (-0.2 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.20%) |
| throughput (operations a second) | 2,932 | 2,931 | -0.0% (-0.3 to +0.2) | -0.2% (-0.7 to +0.3) | +0.2% (-0.2 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.20%) |
| latency, 95th percentile (ms) | 0.253 | 0.236 | -6.7% (-21.2 to +7.7) | -0.3% (-5.5 to +4.9) | +0.1% (-1.8 to +2.0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.475 | 0.421 | -11.4% (-49.2 to +26.5) | -0.1% (-8.9 to +8.8) | +0.0% (-2.6 to +2.6) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.114 | 0.109 | -5.0% (-19.7 to +9.7) | -0.8% (-6.5 to +4.9) | +0.6% (-1.6 to +2.9) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.6 | -0.9% (-1.2 to -0.5) | -0.7% (-1.0 to -0.4) | -1.4% (-3.9 to +1.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 418.4 | 416.7 | -0.4% (-0.9 to +0.2) | -0.2% (-0.9 to +0.6) | -1.0% (-3.6 to +1.6) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 687,674 | 696,351 | +1.3% (-0.8 to +3.3) | +0.9% (-2.7 to +4.5) | +1.3% (-0.4 to +3.0) | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.137 | +9.7% (-71.9 to +91.3) | +0.0% (-22.7 to +22.8) | +1.5% (-6.3 to +9.3) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 220.9 | 248.5 | +12.5% (-81.0 to +106.0) | +0.3% (-29.2 to +29.9) | +1.5% (-8.7 to +11.7) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.186 | +12.5% (-81.0 to +105.9) | +0.5% (-29.1 to +30.1) | +1.2% (-8.6 to +11.1) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,886 | -0.1% (-0.2 to -0.0) | -0.0% (-0.2 to +0.2) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| throughput (operations a second) | 2,895 | 2,893 | -0.1% (-0.1 to -0.0) | -0.0% (-0.2 to +0.2) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| latency, 95th percentile (ms) | 0.378 | 0.38 | +0.6% (-3.6 to +4.8) | -1.9% (-6.8 to +3.0) | +1.1% (-3.8 to +6.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.572 | 0.575 | +0.6% (-9.8 to +11.0) | -1.9% (-4.7 to +1.0) | +0.0% (-4.3 to +4.3) | **the runs disagree** |
| latency, mean (ms) | 0.213 | 0.215 | +0.9% (-2.5 to +4.3) | -0.6% (-4.3 to +3.2) | +0.1% (-1.6 to +1.9) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 486.9 | -4.9% (-20.1 to +10.3) | -1.5% (-4.5 to +1.5) | -0.6% (-1.1 to -0.1) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 417.8 | 398.7 | -4.6% (-18.4 to +9.3) | -1.4% (-3.1 to +0.4) | -0.2% (-2.5 to +2.1) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 722,947 | 741,624 | +2.6% (-17.5 to +22.7) | -1.8% (-13.8 to +10.3) | +4.4% (-26.9 to +35.7) | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.189 | -6.2% (-43.5 to +31.2) | -8.6% (-27.4 to +10.2) | -5.9% (-30.0 to +18.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds | 348.3 | 320.1 | -8.1% (-54.1 to +37.9) | -10.2% (-33.1 to +12.7) | -7.3% (-36.6 to +22.0) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.241 | -8.1% (-54.1 to +37.9) | -10.2% (-33.0 to +12.6) | -7.3% (-36.6 to +22.1) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| cache size changes written (the knob's moves) | 0 | 2.33 | +2.33 (-0.535 to +5.2) | +4 (+4 to +4) | +3 (+0.516 to +5.48) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% (-0.3 to +0.3) | +0.1% (-0.1 to +0.3) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| throughput (operations a second) | 2,895 | 2,895 | -0.0% (-0.1 to +0.1) | +0.1% (-0.2 to +0.3) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.06%) |
| latency, 95th percentile (ms) | 0.437 | 0.44 | +0.6% (-5.6 to +6.8) | +0.4% (-13.0 to +13.7) | -1.6% (-2.8 to -0.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.637 | 0.63 | -1.1% (-18.0 to +15.8) | -4.1% (-37.1 to +28.9) | -1.3% (-3.6 to +0.9) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.223 | 0.225 | +1.3% (-0.7 to +3.2) | +0.7% (-8.6 to +10.0) | -1.5% (-2.6 to -0.4) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 479.8 | -6.3% (-16.5 to +3.9) | -2.4% (-3.9 to -1.0) | -3.2% (-11.8 to +5.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 398.2 | 379.4 | -4.7% (-19.0 to +9.6) | -2.8% (-4.9 to -0.8) | -2.0% (-14.3 to +10.3) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| pages read into the cache (misses) | 266,183 | 290,018 | +9.0% (-14.3 to +32.2) | +3.8% (-4.9 to +12.5) | +6.0% (+3.5 to +8.5) | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.206 | +31.3% (-8.0 to +70.6) | +20.1% (-72.8 to +112.9) | -2.8% (-63.1 to +57.6) | **the runs disagree** |
| host CPU-seconds | 104.3 | 143.6 | +37.7% (-8.1 to +83.5) | +23.1% (-79.2 to +125.4) | -3.4% (-75.4 to +68.7) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.27 | +37.7% (-8.0 to +83.4) | +23.0% (-79.0 to +125.0) | -3.4% (-75.4 to +68.7) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +3.67 (-0.128 to +7.46) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 384 to 512 (3 trials, 2 allowed, 0 refused); acting: 384 to 512 (3 trials, 2 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,892 | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to +0.1) | -0.5% (-2.4 to +1.4) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | -0.6% (-2.4 to +1.3) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, 95th percentile (ms) | 0.319 | 0.323 | +1.1% (-4.3 to +6.6) | -2.0% (-11.6 to +7.6) | +3.3% (-7.2 to +13.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.503 | 0.506 | +0.6% (-3.8 to +5.0) | -2.0% (-5.0 to +1.0) | +1.7% (-0.8 to +4.1) | **the runs disagree** |
| latency, mean (ms) | 0.203 | 0.203 | +0.3% (-1.4 to +2.0) | +0.6% (-5.7 to +6.9) | +8.0% (-19.6 to +35.5) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.0 | -0.6% (-1.3 to +0.1) | -1.1% (-3.0 to +0.8) | -0.4% (-0.5 to -0.4) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 421.6 | 419.4 | -0.5% (-3.0 to +2.0) | -1.5% (-2.4 to -0.5) | -0.2% (-1.6 to +1.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| pages read into the cache (misses) | 661,866 | 725,456 | +9.6% (+3.7 to +15.6) | +9.0% (+5.0 to +13.1) | +4.9% (-12.0 to +21.8) | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.19 | -2.8% (-19.2 to +13.5) | +2.0% (-40.3 to +44.3) | -0.3% (-41.2 to +40.6) | **the runs disagree** |
| host CPU-seconds | 338.8 | 327.4 | -3.4% (-23.4 to +16.6) | +2.2% (-44.5 to +48.9) | -0.7% (-45.6 to +44.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.246 | -3.4% (-23.4 to +16.6) | +2.2% (-44.6 to +49.0) | -0.4% (-45.7 to +44.9) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +2.67 (+1.23 to +4.1) | +2 (+2 to +2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,701 | 5,699 | -0.0% (-0.9 to +0.8) | -0.1% (-0.9 to +0.7) | +0.1% (-1.0 to +1.2) | EVEN, under the floor (every run under 0.5%; the largest 0.11%) |
| throughput (operations a second) | 5,717 | 5,715 | -0.0% (-0.9 to +0.8) | -0.1% (-0.9 to +0.7) | +0.1% (-1.0 to +1.2) | EVEN, under the floor (every run under 0.5%; the largest 0.11%) |
| latency, 95th percentile (ms) | 0.435 | 0.435 | +0.0% (-4.7 to +4.7) | +0.2% (-0.8 to +1.2) | +0.0% (-2.9 to +2.9) | EVEN, under the floor (every run under 0.5%; the largest 0.23%) |
| latency, 99th percentile (ms) | 0.629 | 0.629 | +0.0% (-2.2 to +2.2) | +1.2% (-0.1 to +2.4) | -0.2% (-2.3 to +1.8) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.253 | 0.254 | +0.2% (-4.5 to +4.8) | -0.0% (-1.9 to +1.8) | +0.2% (-3.2 to +3.5) | EVEN, under the floor (every run under 0.5%; the largest 0.18%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.3 | -0.9% (-1.5 to -0.3) | -1.0% (-1.4 to -0.6) | -0.9% (-1.1 to -0.6) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 417.1 | 414.0 | -0.7% (-1.0 to -0.4) | -0.7% (-1.3 to -0.1) | -0.6% (-1.5 to +0.2) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| pages read into the cache (misses) | 675,579 | 684,015 | +1.2% (-0.3 to +2.8) | +0.3% (-3.9 to +4.6) | +0.5% (-1.4 to +2.4) | shown, not judged |
| host CPU busy (share of the run) | 0.285 | 0.286 | +0.1% (-8.1 to +8.2) | -2.2% (-5.5 to +1.0) | +0.6% (-5.4 to +6.7) | **the runs disagree** |
| host CPU-seconds | 484.2 | 485.2 | +0.2% (-10.3 to +10.7) | -3.1% (-7.4 to +1.3) | +0.5% (-8.0 to +9.0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.183 | +0.1% (-11.2 to +11.5) | -3.1% (-6.5 to +0.4) | +0.3% (-9.2 to +9.8) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

**Across 4 untouched workloads: 14 gauge-rows GAIN (1 in all three of our runs), 4 LOSS (0 in all three of our runs), 0 power given (0 in all three of our runs), 12 EVEN, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
