# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40043212711 | `f22776e60a87` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40044594345 | `0d532c7a2dbd` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40045925918 | `e4a97f22dce1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,875 | +0.0% (-0.3 to +0.3) | -0.1% (-0.3 to +0.1) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.14%) |
| throughput (operations a second) | 2,885 | 2,886 | +0.0% (-0.3 to +0.3) | -0.1% (-0.4 to +0.1) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.14%) |
| latency, 95th percentile (ms) | 0.37 | 0.367 | -0.8% (-1.5 to -0.1) | -0.3% (-2.9 to +2.2) | +1.2% (-5.0 to +7.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.598 | 0.597 | -0.3% (-2.6 to +2.0) | -1.3% (-7.2 to +4.6) | +0.8% (-9.7 to +11.3) | **the runs disagree** |
| latency, mean (ms) | 0.222 | 0.223 | +0.3% (-1.3 to +1.9) | -0.6% (-3.4 to +2.3) | +0.8% (-2.1 to +3.7) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.4 | -0.9% (-1.4 to -0.4) | -0.8% (-1.1 to -0.4) | -0.8% (-1.4 to -0.3) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 417.4 | 415.3 | -0.5% (-1.0 to +0.0) | -0.6% (-1.5 to +0.4) | -0.5% (-0.8 to -0.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| pages read into the cache (misses) | 679,081 | 682,938 | +0.6% (-1.7 to +2.8) | -0.3% (-1.5 to +0.9) | +1.3% (-2.1 to +4.7) | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.261 | +7.4% (-25.1 to +39.9) | +2.0% (-10.8 to +14.8) | -2.8% (-27.7 to +22.1) | **the runs disagree** |
| host CPU-seconds | 422.3 | 463.1 | +9.7% (-33.4 to +52.7) | +2.9% (-15.8 to +21.6) | -3.9% (-34.6 to +26.9) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.318 | 0.349 | +9.6% (-33.5 to +52.7) | +2.9% (-15.9 to +21.8) | -3.8% (-34.6 to +27.0) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,935 | -0.1% (-0.3 to +0.1) | -0.1% (-0.3 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| throughput (operations a second) | 2,940 | 2,937 | -0.1% (-0.3 to +0.1) | -0.1% (-0.3 to +0.1) | -0.1% (-0.1 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| latency, 95th percentile (ms) | 0.149 | 0.166 | +11.4% (-26.3 to +49.1) | +2.7% (-9.7 to +15.2) | +1.3% (-1.6 to +4.2) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.354 | 0.364 | +2.8% (-5.8 to +11.4) | +2.8% (-5.5 to +11.0) | +0.1% (-2.5 to +2.8) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.0681 | 0.0697 | +2.3% (-8.7 to +13.4) | +1.6% (-4.8 to +8.0) | +0.4% (-0.0 to +0.8) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.7 | -0.4% (-0.6 to -0.3) | -0.8% (-1.3 to -0.3) | -0.6% (-1.1 to -0.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 3 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 418.0 | 419.1 | +0.2% (-2.4 to +2.9) | -1.0% (-4.1 to +2.1) | -0.2% (-1.8 to +1.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 712,552 | 738,240 | +3.6% (-4.8 to +12.0) | -2.2% (-22.8 to +18.5) | +0.3% (-11.7 to +12.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.083 | -13.5% (-86.2 to +59.1) | +9.1% (-20.1 to +38.3) | +10.9% (-8.5 to +30.4) | **the runs disagree** |
| host CPU-seconds | 175.4 | 148.8 | -15.2% (-94.0 to +63.7) | +10.9% (-26.2 to +47.9) | +13.2% (-10.8 to +37.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.131 | 0.111 | -15.1% (-94.0 to +63.7) | +10.9% (-26.1 to +47.9) | +13.2% (-10.8 to +37.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +3.67 (+2.23 to +5.1) | +3.67 (-0.128 to +7.46) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,877 | -0.1% (-0.2 to +0.0) | -0.0% (-0.2 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| throughput (operations a second) | 2,888 | 2,886 | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| latency, 95th percentile (ms) | 0.503 | 0.507 | +0.7% (-0.8 to +2.1) | +0.9% (-0.1 to +1.8) | +0.1% (-0.9 to +1.0) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.652 | 0.668 | +2.5% (-2.8 to +7.7) | +1.3% (-7.8 to +10.3) | -0.7% (-5.1 to +3.7) | **the runs disagree** |
| latency, mean (ms) | 0.223 | 0.224 | +0.7% (+0.3 to +1.1) | +1.5% (-0.5 to +3.5) | +0.7% (-0.7 to +2.1) | **LOSS** (the same way in all three runs; 1 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 500.9 | -2.2% (-3.7 to -0.7) | -2.4% (-4.3 to -0.4) | -4.4% (-13.4 to +4.5) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 397.0 | 396.9 | -0.0% (-3.5 to +3.4) | -2.2% (-5.1 to +0.7) | -4.9% (-14.5 to +4.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 260,515 | 271,870 | +4.4% (-0.5 to +9.2) | -0.6% (-10.8 to +9.6) | +1.1% (-6.6 to +8.8) | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.191 | -8.9% (-34.5 to +16.6) | -5.6% (-27.8 to +16.7) | +7.3% (-48.0 to +62.5) | **the runs disagree** |
| host CPU-seconds | 149.4 | 132.1 | -11.6% (-45.2 to +22.1) | -6.8% (-33.2 to +19.5) | +9.1% (-60.1 to +78.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.249 | -11.5% (-45.1 to +22.0) | -6.8% (-33.2 to +19.5) | +9.1% (-60.0 to +78.2) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +5 (+2.52 to +7.48) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); run B: left native (3 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: acting: 384 to 512 (3 trials, 2 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | -0.2% (-0.3 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.15%) |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | -0.1% (-0.3 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.14%) |
| latency, 95th percentile (ms) | 0.302 | 0.306 | +1.3% (+0.5 to +2.1) | +1.0% (-1.2 to +3.1) | +2.0% (+0.4 to +3.7) | **LOSS** (the same way in all three runs; 2 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.471 | 0.463 | -1.7% (-4.6 to +1.2) | +2.2% (-0.9 to +5.4) | +1.3% (-3.8 to +6.4) | **the runs disagree** |
| latency, mean (ms) | 0.19 | 0.189 | -0.5% (-1.1 to +0.2) | +1.0% (-2.2 to +4.2) | +2.1% (-0.1 to +4.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 477.8 | -6.7% (-21.1 to +7.8) | -0.5% (-0.9 to -0.1) | -4.2% (-20.8 to +12.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 417.7 | 396.3 | -5.1% (-19.1 to +8.8) | +0.4% (-3.1 to +3.9) | -3.1% (-18.9 to +12.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 650,187 | 796,726 | +22.5% (+11.5 to +33.6) | +0.1% (-4.8 to +4.9) | +7.0% (-19.3 to +33.4) | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.179 | -12.2% (-39.7 to +15.2) | +13.9% (-3.8 to +31.6) | -4.4% (-13.5 to +4.8) | **the runs disagree** |
| host CPU-seconds | 362.7 | 308.6 | -14.9% (-48.2 to +18.4) | +17.1% (-6.2 to +40.4) | -6.0% (-18.4 to +6.4) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.272 | 0.232 | -14.9% (-48.2 to +18.3) | +17.1% (-6.1 to +40.3) | -5.9% (-18.3 to +6.4) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (-0.484 to +4.48) | +2.67 (-0.202 to +5.54) | +1.67 (+0.232 to +3.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 1 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,752 | 5,744 | -0.1% (-0.4 to +0.2) | +1.0% (-3.3 to +5.3) | -0.2% (-0.8 to +0.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (operations a second) | 5,770 | 5,763 | -0.1% (-0.4 to +0.1) | +1.0% (-3.4 to +5.3) | -0.2% (-0.8 to +0.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, 95th percentile (ms) | 0.348 | 0.349 | +0.3% (-0.4 to +1.0) | +0.1% (-0.8 to +1.0) | -0.4% (-1.8 to +1.1) | EVEN, under the floor (every run under 0.5%; the largest 0.39%) |
| latency, 99th percentile (ms) | 0.628 | 0.626 | -0.3% (-1.8 to +1.2) | +0.1% (-3.8 to +4.0) | -0.4% (-3.0 to +2.2) | EVEN, under the floor (every run under 0.5%; the largest 0.42%) |
| latency, mean (ms) | 0.165 | 0.165 | -0.2% (-2.5 to +2.2) | -2.9% (-7.8 to +2.0) | -0.6% (-1.0 to -0.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 501.3 | -2.1% (-7.4 to +3.2) | -0.6% (-1.3 to +0.0) | -0.7% (-1.2 to -0.2) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 416.2 | 409.9 | -1.5% (-6.8 to +3.7) | -0.2% (-0.9 to +0.5) | -0.4% (-1.1 to +0.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 693,007 | 708,353 | +2.2% (-5.5 to +9.9) | +2.5% (-8.5 to +13.4) | -0.2% (-2.9 to +2.5) | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.243 | +3.6% (-3.3 to +10.5) | +4.7% (-12.6 to +21.9) | -1.6% (-12.4 to +9.2) | **the runs disagree** |
| host CPU-seconds | 427.6 | 447.5 | +4.6% (-3.9 to +13.2) | +5.9% (-15.4 to +27.1) | -2.2% (-16.9 to +12.5) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.168 | +4.7% (-3.9 to +13.2) | +4.7% (-13.2 to +22.7) | -2.1% (-16.5 to +12.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +3.33 (+0.465 to +6.2) | +4.33 (+2.9 to +5.77) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (4 trials, 1 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

**Across 4 untouched workloads: 11 gauge-rows GAIN (0 in all three of our runs), 7 LOSS (0 in all three of our runs), 0 power given (0 in all three of our runs), 12 EVEN, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
