# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40287958759 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40291376191 | `f70084ae1bb3` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40293208904 | `2d426169d766` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,903 | +1.0% (-3.2 to +5.2) | -0.0% (-0.2 to +0.2) | +0.1% (-0.4 to +0.6) | EVEN, under the floor (the three runs' mean 0.36%) |
| throughput (operations a second) | 2,883 | 2,913 | +1.0% (-3.1 to +5.2) | -0.0% (-0.2 to +0.1) | +0.1% (-0.5 to +0.7) | EVEN, under the floor (the three runs' mean 0.36%) |
| latency, 95th percentile (ms) | 0.223 | 0.227 | +1.8% (-3.3 to +6.9) | -1.1% (-27.4 to +25.2) | -1.0% (-14.3 to +12.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.461 | 0.465 | +0.9% (-8.6 to +10.4) | -0.1% (-12.7 to +12.5) | -1.5% (-14.6 to +11.6) | **the runs disagree** |
| latency, mean (ms) | 0.18 | 0.176 | -2.6% (-13.2 to +8.0) | -1.3% (-11.1 to +8.5) | +0.6% (-10.2 to +11.3) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 556.1 | +8.6% (-13.8 to +31.0) | -0.4% (-0.5 to -0.3) | +8.9% (-18.9 to +36.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 414.5 | 448.1 | +8.1% (-11.9 to +28.1) | -0.0% (-0.8 to +0.8) | +8.3% (-18.1 to +34.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 679,391 | 641,786 | -5.5% (-26.6 to +15.5) | +1.2% (-4.2 to +6.5) | -7.3% (-31.4 to +16.8) | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.199 | -2.2% (-34.7 to +30.3) | -2.3% (-101.6 to +96.9) | +2.7% (-20.2 to +25.6) | **the runs disagree** |
| host CPU-seconds | 370.1 | 360.4 | -2.6% (-41.9 to +36.6) | -3.0% (-115.3 to +109.4) | +3.2% (-23.9 to +30.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.27 | -3.6% (-39.3 to +32.1) | -3.0% (-115.3 to +109.4) | +3.1% (-23.7 to +29.9) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 6.67 | +6.67 (-1.32 to +14.7) | +4.67 (+1.8 to +7.54) | +12 (+12 to +12) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 209.2 | 212.1 | +1.4% (-3.6 to +6.4) | +0.1% (-6.0 to +6.2) | +1.1% (-8.3 to +10.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 207.2 | 209.5 | +1.1% (-3.8 to +6.1) | -0.3% (-6.4 to +5.7) | +0.9% (-8.4 to +10.1) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.05 | 2.58 | +25.9% (+20.3 to +31.5) | +26.6% (+13.4 to +39.7) | +22.2% (-1.2 to +45.6) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 370.1 | 360.4 | -2.6% (-41.9 to +36.6) | -3.0% (-115.3 to +109.4) | +3.2% (-23.9 to +30.3) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 640 (6 trials, 2 allowed, 0 refused); acting: 512 to 576 (6 trials, 1 allowed, 1 refused); left native (5 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: left native (7 trials, 0 allowed, 2 refused); acting: 512 to 576 (7 trials, 1 allowed, 1 refused); acting: 512 to 704 (7 trials, 3 allowed, 0 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.2) | +0.2% (-0.2 to +0.5) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | +0.1% (-0.2 to +0.5) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 0.326 | 0.325 | -0.4% (-3.1 to +2.3) | +1.5% (-4.1 to +7.0) | -5.0% (-17.0 to +6.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.496 | 0.499 | +0.6% (-0.7 to +1.9) | +1.9% (-7.2 to +10.9) | -3.4% (-5.9 to -1.0) | **the runs disagree** |
| latency, mean (ms) | 0.197 | 0.196 | -0.5% (-1.8 to +0.8) | +0.6% (-1.3 to +2.4) | -2.5% (-7.9 to +2.8) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 510.2 | -0.3% (-0.4 to -0.3) | -0.4% (-0.5 to -0.3) | +8.5% (-3.9 to +21.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| bytes in the cache, mean (MB) | 418.1 | 419.3 | +0.3% (-1.1 to +1.6) | +0.0% (-1.5 to +1.6) | +8.1% (-2.9 to +19.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 710,378 | 705,496 | -0.7% (-9.4 to +8.0) | +0.0% (-10.3 to +10.3) | -8.5% (-19.4 to +2.5) | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.189 | -8.4% (-30.7 to +14.0) | +5.1% (-10.0 to +20.3) | -11.3% (-26.6 to +4.0) | **the runs disagree** |
| host CPU-seconds | 363.6 | 326.6 | -10.2% (-38.2 to +17.9) | +6.1% (-12.5 to +24.7) | -13.0% (-29.5 to +3.5) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.245 | -10.2% (-38.2 to +17.9) | +6.1% (-12.4 to +24.6) | -13.0% (-29.5 to +3.5) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.33 | +3.33 (-2.4 to +9.07) | +4.67 (-2.92 to +12.3) | +7.33 (+3.54 to +11.1) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 200.7 | 199.1 | -0.8% (-2.2 to +0.6) | +0.6% (-1.5 to +2.7) | -1.3% (-3.5 to +0.9) | **the runs disagree** |
| the server's own CPU-seconds (mongod) | 198.1 | 196.0 | -1.0% (-2.5 to +0.4) | +0.2% (-1.8 to +2.3) | -1.6% (-3.9 to +0.6) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.09 | +21.2% (+19.4 to +23.0) | +22.8% (+18.6 to +27.1) | +21.6% (+19.2 to +24.0) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 363.6 | 326.6 | -10.2% (-38.2 to +17.9) | +6.1% (-12.5 to +24.7) | -13.0% (-29.5 to +3.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (5 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); run C: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); acting: 512 to 640 (5 trials, 2 allowed, 1 refused); acting: 512 to 576 (5 trials, 1 allowed, 0 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,884 | +0.0% (-0.1 to +0.1) | +4.4% (-33.2 to +42.0) | +0.0% (-0.1 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (operations a second) | 2,889 | 2,890 | +0.0% (-0.1 to +0.1) | +4.4% (-32.7 to +41.6) | +0.0% (-0.1 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 95th percentile (ms) | 0.422 | 0.422 | +0.0% (-3.3 to +3.3) | +1.1% (-20.2 to +22.4) | -1.2% (-10.3 to +8.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.565 | 0.566 | +0.2% (-3.1 to +3.6) | +5.6% (-65.0 to +76.2) | -2.1% (-14.4 to +10.2) | **the runs disagree** |
| latency, mean (ms) | 0.212 | 0.212 | -0.2% (-2.5 to +2.1) | -8.4% (-69.7 to +53.0) | -0.8% (-8.4 to +6.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 524.8 | +2.5% (-3.9 to +8.9) | +4.0% (-6.6 to +14.6) | -1.0% (-1.1 to -0.9) | **the runs disagree** |
| bytes in the cache, mean (MB) | 401.1 | 414.1 | +3.2% (-6.7 to +13.1) | +4.3% (-5.6 to +14.1) | -0.8% (-5.6 to +4.0) | **the runs disagree** |
| pages read into the cache (misses) | 267,079 | 267,174 | +0.0% (-5.9 to +5.9) | +11.9% (-60.3 to +84.1) | -2.2% (-10.2 to +5.7) | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.165 | -17.0% (-56.8 to +22.9) | +3.9% (-84.0 to +91.9) | +4.6% (-72.9 to +82.1) | **the runs disagree** |
| host CPU-seconds | 139.4 | 112.1 | -19.6% (-67.4 to +28.1) | +3.5% (-95.0 to +102.0) | +4.9% (-78.6 to +88.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.211 | -19.6% (-67.4 to +28.1) | -0.4% (-80.8 to +80.0) | +4.9% (-78.5 to +88.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 8 | +8 (+3.03 to +13) | +10.3 (+5.16 to +15.5) | +7.33 (+4.46 to +10.2) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80.0 | 80.5 | +0.6% (-2.0 to +3.3) | +4.5% (-28.4 to +37.4) | +0.2% (-4.1 to +4.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 79.0 | 79.4 | +0.4% (-2.3 to +3.1) | +4.2% (-28.8 to +37.3) | -0.4% (-4.9 to +4.1) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.993 | 1.18 | +19.1% (+15.3 to +22.9) | +24.7% (+1.8 to +47.5) | +22.9% (+17.3 to +28.6) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139.4 | 112.1 | -19.6% (-67.4 to +28.1) | +3.5% (-95.0 to +102.0) | +4.9% (-78.6 to +88.3) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); acting: 512 to 576 (5 trials, 1 allowed, 0 refused); acting: 512 to 576 (3 trials, 1 allowed, 0 refused); run B: left native (6 trials, 0 allowed, 0 refused); acting: 512 to 576 (6 trials, 1 allowed, 1 refused); acting: 512 to 640 (5 trials, 2 allowed, 0 refused); run C: left native (4 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,883 | -0.0% (-0.2 to +0.2) | +0.0% (-0.0 to +0.1) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 2,888 | 2,887 | -0.0% (-0.2 to +0.2) | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.321 | 0.32 | -0.5% (-4.9 to +3.9) | -0.5% (-1.5 to +0.6) | +1.0% (-3.1 to +5.1) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.49 | 0.488 | -0.4% (-4.2 to +3.4) | -1.2% (-1.8 to -0.5) | -0.3% (-2.7 to +2.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 0.197 | 0.193 | -1.7% (-6.4 to +2.9) | -0.6% (-3.4 to +2.2) | +1.5% (-2.4 to +5.4) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.3 | -0.9% (-2.4 to +0.6) | -0.6% (-1.2 to +0.1) | +1.3% (-5.8 to +8.4) | **the runs disagree** |
| bytes in the cache, mean (MB) | 419.1 | 416.1 | -0.7% (-4.6 to +3.1) | -0.7% (-2.9 to +1.6) | +1.9% (-5.1 to +8.8) | **the runs disagree** |
| pages read into the cache (misses) | 702,902 | 676,488 | -3.8% (-11.1 to +3.6) | -4.2% (-26.3 to +17.8) | +7.0% (-18.4 to +32.4) | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.191 | -8.6% (-12.3 to -4.9) | +12.8% (-69.3 to +94.9) | -16.7% (-57.7 to +24.3) | **the runs disagree** |
| host CPU-seconds | 370.5 | 331.7 | -10.5% (-15.6 to -5.3) | +15.5% (-84.5 to +115.5) | -19.9% (-66.9 to +27.1) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.249 | -10.5% (-15.6 to -5.4) | +15.5% (-84.5 to +115.5) | -19.9% (-67.0 to +27.1) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 6.33 | +6.33 (-3.71 to +16.4) | +4.33 (-0.838 to +9.5) | +3.67 (-3.51 to +10.8) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 194.9 | 190.3 | -2.3% (-8.0 to +3.3) | -0.3% (-3.8 to +3.1) | +2.5% (+0.3 to +4.7) | **the runs disagree** |
| the server's own CPU-seconds (mongod) | 192.2 | 187.0 | -2.7% (-8.4 to +3.0) | -0.7% (-4.2 to +2.8) | +2.3% (-0.1 to +4.6) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.67 | 3.29 | +23.5% (+11.1 to +36.0) | +20.3% (+18.5 to +22.2) | +22.1% (+15.9 to +28.2) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 370.5 | 331.7 | -10.5% (-15.6 to -5.3) | +15.5% (-84.5 to +115.5) | -19.9% (-66.9 to +27.1) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 448 to 512 (5 trials, 1 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused); run B: left native (4 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,713 | 5,709 | -0.1% (-0.5 to +0.3) | -0.1% (-0.4 to +0.2) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.07%) |
| throughput (operations a second) | 5,729 | 5,726 | -0.1% (-0.4 to +0.3) | -0.1% (-0.5 to +0.3) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.38 | 0.381 | +0.2% (-7.1 to +7.5) | +1.0% (-1.2 to +3.3) | +0.6% (-11.7 to +12.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.552 | 0.555 | +0.5% (-14.2 to +15.2) | +2.6% (-10.4 to +15.5) | -0.7% (-12.5 to +11.2) | **the runs disagree** |
| latency, mean (ms) | 0.212 | 0.213 | +0.4% (-6.9 to +7.8) | +1.7% (-1.8 to +5.1) | -0.0% (-9.7 to +9.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 512.9 | +0.2% (-0.1 to +0.5) | +11.2% (-2.3 to +24.6) | +3.0% (-9.0 to +15.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| bytes in the cache, mean (MB) | 416.9 | 418.4 | +0.4% (+0.1 to +0.6) | +10.0% (-4.0 to +24.0) | +3.1% (-8.3 to +14.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 687,410 | 683,616 | -0.6% (-1.8 to +0.7) | -8.3% (-17.7 to +1.2) | -2.9% (-14.5 to +8.7) | shown, not judged |
| host CPU busy (share of the run) | 0.291 | 0.296 | +1.7% (-3.8 to +7.1) | +3.9% (-8.7 to +16.5) | -12.3% (-70.3 to +45.6) | **the runs disagree** |
| host CPU-seconds | 527.3 | 537.5 | +1.9% (-6.0 to +9.9) | +5.0% (-12.0 to +22.0) | -14.9% (-80.8 to +51.0) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.202 | +2.0% (-5.8 to +9.8) | +5.0% (-12.0 to +22.0) | -14.9% (-80.7 to +50.9) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 8.33 | +8.33 (+4.54 to +12.1) | +10.3 (+8.9 to +11.8) | +7.33 (+4.46 to +10.2) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 321.7 | 324.5 | +0.9% (-5.8 to +7.5) | +1.1% (+0.4 to +1.8) | +0.8% (-8.1 to +9.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the server's own CPU-seconds (mongod) | 317.4 | 319.7 | +0.7% (-5.9 to +7.3) | +0.9% (+0.3 to +1.5) | +0.4% (-8.7 to +9.5) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.23 | 4.82 | +13.9% (+2.8 to +24.9) | +17.2% (+6.7 to +27.7) | +20.4% (+15.6 to +25.2) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 527.3 | 537.5 | +1.9% (-6.0 to +9.9) | +5.0% (-12.0 to +22.0) | -14.9% (-80.8 to +51.0) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (5 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 2 refused); run B: acting: 512 to 576 (6 trials, 1 allowed, 1 refused); acting: 512 to 640 (7 trials, 2 allowed, 0 refused); acting: 512 to 576 (6 trials, 1 allowed, 1 refused); run C: left native (4 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 1 refused); acting: 512 to 576 (4 trials, 1 allowed, 0 refused).

**Across 4 untouched workloads: 4 gauge-rows GAIN, 2 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 10 EVEN, 26 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
