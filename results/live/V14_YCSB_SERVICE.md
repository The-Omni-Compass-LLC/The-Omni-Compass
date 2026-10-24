# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39623244880 | `e32bbb605501` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |
| B | 39628035584 | `990711a99dc4` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |
| C | 39630660108 | `67b7cd6bf1e8` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,931 | -0.1% (-0.4 to +0.3) | -0.1% (-0.3 to +0.2) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| throughput (operations a second) | 2,939 | 2,936 | -0.1% (-0.4 to +0.2) | -0.1% (-0.3 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| latency, 95th percentile (ms) | 0.162 | 0.163 | +0.2% (-46.2 to +46.7) | +0.7% (-2.0 to +3.4) | +2.8% (-19.2 to +24.8) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.396 | 0.391 | -1.3% (-26.0 to +23.3) | +0.9% (-4.7 to +6.5) | +0.7% (-14.9 to +16.3) | **the runs disagree** |
| latency, mean (ms) | 0.0819 | 0.0823 | +0.5% (-17.5 to +18.5) | +0.2% (-4.7 to +5.2) | -0.2% (-6.0 to +5.5) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 506.9 | -1.0% (-1.2 to -0.7) | -0.8% (-1.3 to -0.3) | -0.9% (-1.2 to -0.5) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 419.1 | 416.6 | -0.6% (-1.0 to -0.2) | -0.3% (-1.0 to +0.4) | -0.4% (-0.7 to -0.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 2 of 3 clear of the noise) |
| pages read into the cache (misses) | 690,618 | 693,348 | +0.4% (-2.0 to +2.7) | +1.5% (-2.7 to +5.7) | +0.4% (-4.3 to +5.2) | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.107 | -9.1% (-42.4 to +24.2) | +5.7% (-37.1 to +48.6) | -14.5% (-34.1 to +5.1) | **the runs disagree** |
| host CPU-seconds | 215.0 | 192.4 | -10.5% (-48.0 to +27.0) | +7.7% (-48.1 to +63.5) | -16.2% (-38.4 to +6.1) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.144 | -10.5% (-47.9 to +26.9) | +7.7% (-48.3 to +63.8) | -16.2% (-38.4 to +6.1) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 1 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,925 | 2,923 | -0.1% (-0.1 to -0.0) | -0.1% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| throughput (operations a second) | 2,928 | 2,926 | -0.1% (-0.1 to -0.0) | -0.1% (-0.2 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| latency, 95th percentile (ms) | 0.244 | 0.248 | +1.6% (-3.0 to +6.3) | +2.0% (-0.9 to +5.0) | +6.7% (-26.7 to +40.0) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.431 | 0.433 | +0.3% (-3.9 to +4.6) | +0.9% (-2.1 to +4.0) | +6.5% (-17.5 to +30.6) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.126 | 0.127 | +1.2% (-3.0 to +5.5) | +0.1% (-2.4 to +2.7) | +3.4% (-11.4 to +18.2) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.7 | -0.4% (-0.6 to -0.3) | -0.6% (-0.8 to -0.4) | -0.5% (-0.8 to -0.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 3 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 418.7 | 419.8 | +0.3% (-1.0 to +1.5) | +0.2% (-0.8 to +1.2) | +0.5% (-2.4 to +3.3) | EVEN, under the floor (every run under 0.5%; the largest 0.47%) |
| pages read into the cache (misses) | 700,229 | 741,772 | +5.9% (+0.9 to +11.0) | +2.0% (-4.7 to +8.7) | +7.3% (+0.6 to +13.9) | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.133 | +10.2% (-110.0 to +130.5) | -1.5% (-38.6 to +35.5) | -19.0% (-54.3 to +16.2) | **the runs disagree** |
| host CPU-seconds | 216.1 | 240.5 | +11.3% (-125.7 to +148.3) | -1.8% (-45.7 to +42.1) | -20.8% (-59.0 to +17.4) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.18 | +11.3% (-125.7 to +148.4) | -1.8% (-45.7 to +42.1) | -20.8% (-58.9 to +17.4) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +2.67 (+1.23 to +4.1) | +2 (+2 to +2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | -0.0% (-0.1 to +0.1) | -0.0% (-0.3 to +0.3) | +0.6% (-2.5 to +3.8) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (operations a second) | 2,888 | 2,888 | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | +0.6% (-2.6 to +3.9) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, 95th percentile (ms) | 0.421 | 0.422 | +0.3% (-0.9 to +1.5) | +1.2% (-12.3 to +14.6) | +1.1% (-4.2 to +6.4) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.571 | 0.57 | -0.1% (-6.0 to +5.8) | +0.2% (-25.5 to +25.9) | +1.7% (-4.0 to +7.5) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.21 | 0.214 | +1.9% (-2.4 to +6.2) | -2.5% (-15.6 to +10.5) | -3.5% (-12.6 to +5.6) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 498.7 | -2.6% (-5.1 to -0.1) | -0.9% (-2.0 to +0.1) | -3.8% (-11.3 to +3.7) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 400.3 | 393.9 | -1.6% (-5.0 to +1.9) | +0.2% (-0.8 to +1.1) | -3.4% (-8.3 to +1.4) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 272,631 | 273,811 | +0.4% (-4.4 to +5.3) | +3.0% (-8.1 to +14.0) | +3.9% (-26.0 to +33.9) | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.232 | +12.6% (-49.8 to +74.9) | -8.0% (-41.8 to +25.8) | +13.9% (-44.8 to +72.6) | **the runs disagree** |
| host CPU-seconds | 146.8 | 169.4 | +15.3% (-64.0 to +94.6) | -9.6% (-48.9 to +29.7) | +16.2% (-55.5 to +87.9) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.318 | +15.3% (-64.0 to +94.6) | -9.7% (-48.9 to +29.6) | +15.8% (-54.2 to +85.8) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 5 | +5 (+2.52 to +7.48) | +2.67 (-0.202 to +5.54) | +5 (+2.52 to +7.48) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,908 | +0.1% (-0.4 to +0.6) | -0.1% (-0.5 to +0.4) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| throughput (operations a second) | 2,911 | 2,912 | +0.1% (-0.3 to +0.4) | -0.1% (-0.5 to +0.4) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.06%) |
| latency, 95th percentile (ms) | 0.188 | 0.187 | -0.7% (-3.5 to +2.0) | -0.9% (-2.9 to +1.1) | +0.1% (-0.3 to +0.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.357 | 0.357 | -0.1% (-3.5 to +3.3) | -0.9% (-10.6 to +8.9) | -1.0% (-1.5 to -0.5) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| latency, mean (ms) | 0.146 | 0.141 | -3.8% (-13.3 to +5.7) | -0.4% (-3.7 to +2.9) | -1.5% (-4.6 to +1.7) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.9 | -0.6% (-1.8 to +0.6) | -0.5% (-0.6 to -0.3) | -0.5% (-1.1 to +0.0) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 418.9 | 416.5 | -0.6% (-3.0 to +1.9) | -0.2% (-0.9 to +0.5) | -1.1% (-3.5 to +1.3) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| pages read into the cache (misses) | 714,025 | 675,732 | -5.4% (-19.7 to +8.9) | +1.4% (-10.5 to +13.2) | +2.4% (-14.8 to +19.5) | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.156 | +8.0% (-34.5 to +50.5) | +5.8% (-32.0 to +43.6) | -17.6% (-38.3 to +3.1) | **the runs disagree** |
| host CPU-seconds | 258.4 | 282.1 | +9.2% (-40.1 to +58.4) | +6.8% (-38.5 to +52.2) | -20.7% (-41.0 to -0.4) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.194 | 0.211 | +9.1% (-39.9 to +58.1) | +6.8% (-38.7 to +52.3) | -20.7% (-41.0 to -0.4) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +2 (+2 to +2) | +2.67 (-0.202 to +5.54) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,736 | 5,733 | -0.1% (-0.5 to +0.4) | -0.1% (-0.2 to +0.0) | -0.1% (-1.1 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| throughput (operations a second) | 5,751 | 5,748 | -0.1% (-0.5 to +0.4) | -0.1% (-0.3 to +0.1) | -0.1% (-1.1 to +0.9) | EVEN, under the floor (every run under 0.5%; the largest 0.08%) |
| latency, 95th percentile (ms) | 0.377 | 0.375 | -0.4% (-1.7 to +1.0) | +0.5% (-3.5 to +4.5) | +1.3% (+1.0 to +1.7) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.595 | 0.596 | +0.2% (-0.9 to +1.3) | +1.2% (-7.6 to +10.1) | -0.1% (-1.0 to +0.9) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.204 | 0.203 | -0.3% (-2.4 to +1.9) | +0.3% (-3.3 to +3.9) | +1.4% (-0.7 to +3.5) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.8 | -0.8% (-1.3 to -0.3) | -1.1% (-3.6 to +1.4) | -1.2% (-4.1 to +1.8) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| bytes in the cache, mean (MB) | 416.9 | 414.9 | -0.5% (-0.9 to -0.0) | -1.0% (-3.1 to +1.2) | -1.0% (-3.4 to +1.5) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| pages read into the cache (misses) | 688,625 | 692,655 | +0.6% (-5.2 to +6.4) | +1.6% (-2.2 to +5.5) | +1.1% (-3.3 to +5.4) | shown, not judged |
| host CPU busy (share of the run) | 0.273 | 0.276 | +1.2% (-16.6 to +19.0) | -0.0% (-1.9 to +1.9) | +1.3% (-4.1 to +6.7) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 496.3 | 504.2 | +1.6% (-22.3 to +25.5) | -0.1% (-1.5 to +1.4) | +1.2% (-6.9 to +9.2) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.19 | +1.6% (-21.9 to +25.1) | -0.0% (-1.3 to +1.3) | +1.1% (-7.9 to +10.2) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.67 (+2.23 to +5.1) | +4.67 (+3.23 to +6.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run C: left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused).

**Across 4 untouched workloads: 12 gauge-rows GAIN (0 in all three of our runs), 8 LOSS (0 in all three of our runs), 3 power given (0 in all three of our runs), 11 EVEN, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
