# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40135943683 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| B | 40137072959 | `19db275eb391` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |
| C | 40138209461 | `96ebf29137fe` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,935 | -0.1% (-0.2 to +0.0) | -0.1% (-0.3 to +0.0) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.05%) |
| throughput (operations a second) | 2,942 | 2,939 | -0.1% (-0.2 to +0.0) | -0.1% (-0.2 to -0.0) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.128 | 0.134 | +4.4% (-8.8 to +17.6) | +0.9% (-0.6 to +2.3) | -1.1% (-4.6 to +2.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.354 | 0.364 | +2.7% (-10.7 to +16.1) | +1.4% (+0.3 to +2.6) | -1.0% (-2.3 to +0.2) | **the runs disagree** |
| latency, mean (ms) | 0.0761 | 0.0766 | +0.7% (-7.5 to +8.9) | +1.4% (-1.1 to +3.9) | +0.0% (-1.9 to +2.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.1 | -1.0% (-1.1 to -0.8) | -1.0% (-1.7 to -0.4) | -0.9% (-1.5 to -0.3) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 420.1 | 417.5 | -0.6% (-0.8 to -0.4) | -0.6% (-1.1 to -0.1) | -0.6% (-0.8 to -0.5) | **GAIN in all three of our runs** |
| pages read into the cache (misses) | 680,968 | 682,634 | +0.2% (-2.5 to +2.9) | +1.5% (-0.8 to +3.8) | +2.0% (-0.8 to +4.7) | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.106 | -6.7% (-70.3 to +56.9) | +2.9% (-9.2 to +14.9) | +4.9% (-28.1 to +38.0) | **the runs disagree** |
| host CPU-seconds | 206.6 | 190.4 | -7.8% (-79.5 to +63.8) | +3.5% (-11.2 to +18.3) | +6.6% (-37.2 to +50.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.142 | -7.8% (-79.6 to +63.9) | +3.6% (-11.0 to +18.2) | +6.5% (-37.3 to +50.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+1.52 to +6.48) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,882 | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.0) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (the three runs' mean 0.06%) |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.0) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms) | 0.342 | 0.341 | -0.4% (-5.1 to +4.3) | +1.2% (-2.2 to +4.5) | +3.7% (-12.0 to +19.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.591 | 0.588 | -0.5% (-2.8 to +1.8) | +0.7% (-0.5 to +1.8) | -0.1% (-2.7 to +2.5) | **the runs disagree** |
| latency, mean (ms) | 0.201 | 0.201 | +0.0% (-1.7 to +1.8) | +1.1% (-1.8 to +4.0) | +1.1% (-3.2 to +5.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.8 | -0.6% (-1.5 to +0.2) | -1.2% (-3.2 to +0.9) | -0.5% (-1.0 to -0.0) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 416.9 | 415.2 | -0.4% (-1.8 to +0.9) | -1.6% (-2.1 to -1.2) | -0.2% (-0.9 to +0.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 715,036 | 706,228 | -1.2% (-8.9 to +6.4) | -5.4% (-11.2 to +0.3) | -1.0% (-6.8 to +4.9) | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.205 | +18.3% (-16.9 to +53.5) | -11.2% (-36.8 to +14.5) | -3.7% (-48.4 to +41.1) | **the runs disagree** |
| host CPU-seconds | 292.4 | 359.4 | +22.9% (-21.7 to +67.5) | -13.9% (-45.4 to +17.6) | -5.8% (-61.8 to +50.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.27 | +22.9% (-21.7 to +67.5) | -13.9% (-45.3 to +17.5) | -5.8% (-61.9 to +50.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+0.465 to +6.2) | +4.33 (+2.9 to +5.77) | +3.33 (+0.465 to +6.2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 0 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to -0.0) | -3.0% (-10.1 to +4.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | -2.9% (-9.9 to +4.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 95th percentile (ms) | 0.437 | 0.435 | -0.5% (-5.4 to +4.3) | +1.5% (-5.9 to +8.8) | +3.7% (-9.9 to +17.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.591 | 0.591 | +0.0% (-4.1 to +4.1) | -0.1% (-9.2 to +9.0) | +5.9% (-15.5 to +27.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.218 | 0.216 | -1.0% (-6.0 to +4.0) | +0.2% (-6.0 to +6.3) | +8.8% (-8.1 to +25.7) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 501.9 | -2.0% (-4.4 to +0.4) | -1.7% (-1.8 to -1.6) | -2.7% (-4.6 to -0.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| bytes in the cache, mean (MB) | 399.6 | 394.4 | -1.3% (-4.2 to +1.6) | -1.1% (-5.7 to +3.6) | -1.4% (-8.0 to +5.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 263,402 | 272,507 | +3.5% (-7.7 to +14.6) | +1.7% (-0.7 to +4.2) | +1.2% (-5.8 to +8.2) | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.198 | +6.2% (-14.9 to +27.2) | +35.2% (-97.9 to +168.2) | +3.8% (-63.4 to +71.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 128.8 | 138.4 | +7.4% (-16.9 to +31.8) | +38.8% (-109.5 to +187.1) | +5.3% (-76.2 to +86.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.26 | +7.4% (-17.0 to +31.8) | +38.8% (-109.4 to +187.0) | +8.8% (-80.8 to +98.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 4.67 | +4.67 (+1.8 to +7.54) | +4 (+4 to +4) | +6 (+6 to +6) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | -0.1% (-0.4 to +0.2) | EVEN, under the floor (the three runs' mean 0.05%) |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% (-0.1 to +0.1) | -0.1% (-0.3 to +0.1) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.315 | 0.315 | -0.2% (-2.6 to +2.2) | -0.7% (-1.5 to +0.1) | +1.7% (-5.7 to +9.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.494 | 0.494 | -0.1% (-1.8 to +1.7) | -0.2% (-11.6 to +11.2) | +0.7% (-5.8 to +7.3) | EVEN, under the floor (the three runs' mean 0.16%) |
| latency, mean (ms) | 0.193 | 0.192 | -0.7% (-4.6 to +3.2) | -0.8% (-9.8 to +8.2) | -0.3% (-12.2 to +11.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 486.1 | -5.1% (-21.4 to +11.3) | -0.7% (-1.6 to +0.2) | -0.9% (-1.9 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| bytes in the cache, mean (MB) | 420.8 | 400.6 | -4.8% (-23.7 to +14.1) | -0.2% (-2.1 to +1.7) | -0.2% (-3.0 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 690,477 | 722,378 | +4.6% (-26.0 to +35.2) | -3.0% (-19.1 to +13.1) | -6.2% (-16.7 to +4.4) | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.195 | -2.0% (-38.9 to +35.0) | -10.4% (-91.6 to +70.7) | +16.8% (-59.5 to +93.1) | **the runs disagree** |
| host CPU-seconds | 349.6 | 340.4 | -2.6% (-48.4 to +43.1) | -12.3% (-106.2 to +81.6) | +20.1% (-72.6 to +112.7) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.256 | -2.7% (-48.4 to +43.1) | -12.3% (-106.2 to +81.6) | +20.1% (-72.6 to +112.8) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+1.9 to +4.77) | +3.33 (+0.465 to +6.2) | +3.33 (+0.465 to +6.2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,684 | 5,686 | +0.0% (-0.5 to +0.5) | -0.1% (-0.4 to +0.2) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.05%) |
| throughput (operations a second) | 5,701 | 5,703 | +0.0% (-0.5 to +0.6) | -0.1% (-0.4 to +0.2) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.428 | 0.428 | +0.0% (-1.0 to +1.0) | +0.0% (-5.4 to +5.4) | -1.2% (-14.4 to +12.0) | EVEN, under the floor (the three runs' mean 0.39%) |
| latency, 99th percentile (ms) | 0.656 | 0.654 | -0.3% (-2.0 to +1.4) | +1.9% (-4.5 to +8.3) | -3.7% (-15.1 to +7.7) | **the runs disagree** |
| latency, mean (ms) | 0.245 | 0.245 | +0.2% (-0.5 to +1.0) | -0.3% (-6.4 to +5.8) | -0.9% (-4.6 to +2.9) | EVEN, under the floor (the three runs' mean 0.31%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.3 | -0.5% (-0.7 to -0.3) | -1.0% (-1.3 to -0.7) | -1.5% (-3.7 to +0.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| bytes in the cache, mean (MB) | 416.9 | 415.0 | -0.5% (-0.6 to -0.4) | -0.4% (-0.6 to -0.2) | -1.4% (-3.6 to +0.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| pages read into the cache (misses) | 679,750 | 684,928 | +0.8% (-1.7 to +3.3) | +0.1% (-3.4 to +3.5) | +1.1% (-3.6 to +5.7) | shown, not judged |
| host CPU busy (share of the run) | 0.317 | 0.324 | +2.2% (+0.2 to +4.1) | +1.7% (-28.5 to +31.9) | -2.3% (-59.9 to +55.3) | **the runs disagree** |
| host CPU-seconds | 568.2 | 585.5 | +3.0% (+1.2 to +4.8) | +2.3% (-33.4 to +38.0) | -2.9% (-69.9 to +64.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.22 | +2.9% (+0.6 to +5.2) | +2.4% (-33.4 to +38.1) | -2.9% (-69.9 to +64.2) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused).

**Across 4 untouched workloads: 9 gauge-rows GAIN, 5 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 EVEN, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
