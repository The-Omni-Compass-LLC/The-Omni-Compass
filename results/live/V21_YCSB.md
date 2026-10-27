# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40259304209 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40281469940 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40401042132 | `5e222aa21371` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,881 | -0.1% (-0.2 to +0.1) | -0.1% (-0.7 to +0.4) | -0.1% (-0.3 to +0.1) | EVEN, under the floor (the three runs' mean 0.10%) |
| throughput (operations a second) | 2,891 | 2,889 | -0.1% (-0.2 to +0.1) | -0.1% (-0.7 to +0.5) | -0.1% (-0.4 to +0.2) | EVEN, under the floor (the three runs' mean 0.09%) |
| latency, 95th percentile (ms) | 0.335 | 0.337 | +0.5% (-1.2 to +2.2) | +0.0% (-3.1 to +3.1) | +2.1% (+0.0 to +4.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 0.512 | 0.517 | +0.8% (-0.6 to +2.3) | -0.3% (-4.9 to +4.2) | +3.8% (-9.1 to +16.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.207 | 0.208 | +0.5% (-1.4 to +2.3) | -0.5% (-1.9 to +0.8) | +2.1% (-0.2 to +4.3) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 535.0 | +4.5% (-6.2 to +15.2) | +7.2% (-8.2 to +22.6) | +11.9% (+6.9 to +16.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 417.6 | 435.5 | +4.3% (-6.1 to +14.7) | +7.0% (-7.6 to +21.6) | +11.4% (+7.3 to +15.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 673,795 | 650,602 | -3.4% (-13.0 to +6.1) | -5.2% (-19.9 to +9.6) | -7.1% (-10.4 to -3.7) | shown, not judged |
| host CPU busy (share of the run) | 0.253 | 0.262 | +3.6% (-24.3 to +31.5) | +0.4% (-34.0 to +34.8) | +6.6% (+0.1 to +13.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU-seconds | 454.5 | 476.2 | +4.8% (-33.6 to +43.1) | +0.5% (-44.1 to +45.0) | +8.7% (-2.3 to +19.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.342 | 0.358 | +4.8% (-33.5 to +43.2) | +0.6% (-44.4 to +45.6) | +8.7% (-2.3 to +19.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 11.7 | +11.7 (+7.87 to +15.5) | +11 (+8.52 to +13.5) | +9.33 (+5.54 to +13.1) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 268.8 | 271.2 | +0.9% (+0.2 to +1.7) | -0.1% (-1.6 to +1.4) | +2.2% (-2.1 to +6.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the server's own CPU-seconds (mongod) | 266.3 | 268.1 | +0.7% (-0.1 to +1.4) | -0.3% (-1.9 to +1.2) | +1.9% (-2.4 to +6.2) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 3.11 | +25.8% (+23.0 to +28.5) | +22.2% (+16.4 to +28.0) | +28.9% (+25.2 to +32.5) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 454.5 | 476.2 | +4.8% (-33.6 to +43.1) | +0.5% (-44.1 to +45.0) | +8.7% (-2.3 to +19.7) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 640 (8 trials, 2 allowed, 1 refused); acting: 512 to 576 (6 trials, 1 allowed, 1 refused); left native (5 trials, 0 allowed, 1 refused); run B: acting: 512 to 640 (7 trials, 2 allowed, 0 refused); acting: 512 to 640 (6 trials, 2 allowed, 0 refused); left native (7 trials, 0 allowed, 1 refused); run C: acting: 512 to 640 (6 trials, 2 allowed, 1 refused); acting: 512 to 576 (4 trials, 1 allowed, 1 refused); acting: 512 to 640 (5 trials, 2 allowed, 0 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,892 | 2,892 | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.321 | 0.326 | +1.5% (-2.0 to +4.9) | +2.3% (-6.7 to +11.4) | -0.9% (-3.7 to +2.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.488 | 0.494 | +1.2% (-1.8 to +4.3) | +2.4% (-4.5 to +9.3) | -0.8% (-5.4 to +3.8) | **the runs disagree** |
| latency, mean (ms) | 0.193 | 0.195 | +0.7% (-1.8 to +3.2) | +1.4% (-3.4 to +6.3) | -0.9% (-3.4 to +1.6) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 510.3 | -0.3% (-0.4 to -0.3) | -0.3% (-0.4 to -0.2) | -0.1% (-0.3 to +0.0) | EVEN, under the floor (the three runs' mean 0.26%) |
| bytes in the cache, mean (MB) | 418.9 | 419.8 | +0.2% (-0.6 to +1.0) | +0.5% (-1.2 to +2.1) | -0.5% (-2.2 to +1.3) | EVEN, under the floor (the three runs' mean 0.06%) |
| pages read into the cache (misses) | 721,546 | 741,544 | +2.8% (-19.2 to +24.7) | +5.6% (-5.6 to +16.8) | +5.6% (-18.8 to +30.0) | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.205 | -2.5% (-17.6 to +12.7) | -1.6% (-38.9 to +35.7) | -1.7% (-32.7 to +29.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 374.2 | 362.2 | -3.2% (-21.2 to +14.8) | -2.3% (-48.8 to +44.1) | -1.7% (-42.1 to +38.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.272 | -3.2% (-21.2 to +14.8) | -2.3% (-48.8 to +44.1) | -1.8% (-42.1 to +38.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +2 (+2 to +2) | +5.33 (-2.26 to +12.9) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 196.7 | 199.4 | +1.3% (-1.9 to +4.6) | +2.0% (-3.5 to +7.6) | -0.3% (-1.4 to +0.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 194.2 | 196.3 | +1.1% (-2.2 to +4.4) | +1.8% (-3.9 to +7.5) | -0.5% (-1.7 to +0.6) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.04 | +21.7% (+17.3 to +26.1) | +23.8% (+16.6 to +31.0) | +18.5% (+11.5 to +25.6) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 374.2 | 362.2 | -3.2% (-21.2 to +14.8) | -2.3% (-48.8 to +44.1) | -1.7% (-42.1 to +38.6) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (4 trials, 0 allowed, 0 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% (-0.2 to +0.1) | +0.1% (-0.4 to +0.7) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% (-0.1 to +0.1) | +0.1% (-0.4 to +0.7) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.408 | 0.409 | +0.2% (-2.9 to +3.2) | +5.4% (-7.8 to +18.6) | +0.7% (-1.1 to +2.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.577 | 0.579 | +0.4% (-4.4 to +5.2) | +2.5% (-0.4 to +5.5) | +1.7% (-2.5 to +5.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.211 | 0.21 | -0.2% (-2.3 to +1.9) | -4.0% (-10.7 to +2.7) | +0.4% (-1.2 to +2.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 514.9 | +0.6% (-3.3 to +4.5) | +2.9% (-9.2 to +15.0) | -0.4% (-0.5 to -0.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 405.0 | 408.2 | +0.8% (-4.5 to +6.1) | +4.2% (-6.8 to +15.3) | -1.1% (-5.1 to +2.9) | **the runs disagree** |
| pages read into the cache (misses) | 256,907 | 272,467 | +6.1% (+1.3 to +10.8) | -0.3% (-14.2 to +13.6) | -5.0% (-30.2 to +20.3) | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.178 | -14.6% (-46.2 to +17.1) | -9.0% (-74.5 to +56.4) | +25.0% (-47.9 to +98.0) | **the runs disagree** |
| host CPU-seconds | 147.6 | 121.5 | -17.7% (-57.0 to +21.6) | -10.6% (-86.3 to +65.2) | +28.2% (-53.3 to +109.8) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.229 | -17.7% (-56.9 to +21.6) | -10.6% (-86.3 to +65.1) | +28.2% (-53.3 to +109.7) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 7.33 | +7.33 (+4.46 to +10.2) | +7 (+0.427 to +13.6) | +6 (+6 to +6) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80.0 | 80.0 | -0.0% (-3.4 to +3.4) | +1.0% (-2.2 to +4.1) | +0.4% (-5.1 to +5.9) | EVEN, under the floor (the three runs' mean 0.45%) |
| the server's own CPU-seconds (mongod) | 79.0 | 78.7 | -0.3% (-3.6 to +3.1) | +0.7% (-2.4 to +3.8) | -0.3% (-5.7 to +5.2) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.22 | +21.2% (+12.6 to +29.9) | +20.0% (+12.3 to +27.6) | +26.9% (+17.7 to +36.1) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 147.6 | 121.5 | -17.7% (-57.0 to +21.7) | -10.6% (-86.3 to +65.2) | +28.2% (-53.4 to +109.8) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); run B: acting: 512 to 576 (4 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 1 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,889 | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,892 | 2,893 | +0.0% (-0.0 to +0.1) | -0.0% (-0.0 to +0.0) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.303 | 0.302 | -0.3% (-2.0 to +1.3) | -0.9% (-3.5 to +1.7) | +0.2% (-0.8 to +1.1) | EVEN, under the floor (the three runs' mean 0.34%) |
| latency, 99th percentile (ms) | 0.487 | 0.487 | +0.0% (-1.3 to +1.3) | -0.9% (-3.6 to +1.8) | +1.4% (-2.1 to +4.8) | **the runs disagree** |
| latency, mean (ms) | 0.188 | 0.189 | +0.6% (-2.2 to +3.4) | -0.6% (-5.9 to +4.7) | +0.3% (-1.3 to +1.8) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.9 | -0.4% (-0.8 to -0.1) | -0.6% (-1.3 to +0.1) | +3.3% (-12.1 to +18.6) | **the runs disagree** |
| bytes in the cache, mean (MB) | 418.5 | 419.6 | +0.3% (-0.7 to +1.2) | -0.3% (-2.1 to +1.6) | +3.4% (-12.7 to +19.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 679,735 | 714,771 | +5.2% (-14.8 to +25.1) | +1.8% (-12.6 to +16.2) | -3.4% (-27.0 to +20.2) | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.191 | -3.8% (-18.2 to +10.6) | -3.1% (-24.4 to +18.1) | -0.2% (-9.5 to +9.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 351.0 | 334.5 | -4.7% (-23.2 to +13.8) | -3.6% (-28.6 to +21.5) | -0.2% (-11.4 to +11.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.251 | -4.7% (-23.2 to +13.7) | -3.6% (-28.7 to +21.5) | -0.2% (-11.4 to +11.0) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +4.33 (-0.838 to +9.5) | +3.67 (+2.23 to +5.1) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 183.5 | 185.6 | +1.1% (-2.5 to +4.8) | +0.2% (-7.9 to +8.4) | +0.2% (-4.1 to +4.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 181.0 | 182.6 | +0.9% (-2.9 to +4.6) | -0.1% (-8.3 to +8.1) | -0.1% (-4.4 to +4.1) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 2.97 | +19.9% (+17.1 to +22.8) | +22.9% (+18.8 to +26.9) | +21.8% (+19.3 to +24.3) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 351.0 | 334.5 | -4.7% (-23.2 to +13.8) | -3.6% (-28.6 to +21.5) | -0.2% (-11.5 to +11.0) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); left native (4 trials, 0 allowed, 0 refused); run C: left native (2 trials, 0 allowed, 0 refused); acting: 512 to 576 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 0 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,677 | 5,686 | +0.1% (-0.3 to +0.6) | -0.1% (-0.4 to +0.2) | +0.2% (-1.5 to +2.0) | EVEN, under the floor (the three runs' mean 0.09%) |
| throughput (operations a second) | 5,695 | 5,703 | +0.2% (-0.3 to +0.6) | -0.1% (-0.4 to +0.2) | +0.2% (-1.5 to +1.9) | EVEN, under the floor (the three runs' mean 0.09%) |
| latency, 95th percentile (ms) | 0.431 | 0.428 | -0.7% (-3.0 to +1.6) | +4.5% (-16.8 to +25.8) | +0.2% (-4.0 to +4.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.656 | 0.657 | +0.2% (-1.8 to +2.1) | +1.4% (-8.3 to +11.1) | -0.3% (-5.6 to +4.9) | EVEN, under the floor (the three runs' mean 0.41%) |
| latency, mean (ms) | 0.247 | 0.244 | -0.9% (-4.0 to +2.3) | +2.6% (-8.7 to +13.9) | -0.2% (-6.3 to +6.0) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 540.0 | +5.5% (-7.1 to +18.0) | +2.6% (-11.1 to +16.3) | +7.5% (-22.8 to +37.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| bytes in the cache, mean (MB) | 416.7 | 439.0 | +5.4% (-6.9 to +17.6) | +2.8% (-9.5 to +15.1) | +7.2% (-21.6 to +35.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 679,148 | 654,260 | -3.7% (-16.0 to +8.6) | -0.8% (-12.2 to +10.6) | -5.9% (-30.8 to +19.0) | shown, not judged |
| host CPU busy (share of the run) | 0.325 | 0.321 | -1.4% (-11.8 to +9.0) | +17.2% (-29.8 to +64.3) | +0.6% (-8.3 to +9.6) | **the runs disagree** |
| host CPU-seconds | 588.6 | 577.3 | -1.9% (-16.4 to +12.5) | +19.5% (-33.1 to +72.0) | +0.7% (-10.7 to +12.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.217 | -2.0% (-16.8 to +12.7) | +19.6% (-33.1 to +72.2) | +0.5% (-12.6 to +13.6) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 11.0 | +11 (+6.03 to +16) | +6.67 (+3.8 to +9.54) | +9 (+4.7 to +13.3) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 354.1 | 351.6 | -0.7% (-4.1 to +2.7) | +4.1% (-12.0 to +20.2) | +0.8% (-3.9 to +5.5) | **the runs disagree** |
| the server's own CPU-seconds (mongod) | 349.7 | 346.7 | -0.9% (-4.2 to +2.5) | +3.7% (-12.5 to +19.9) | +0.6% (-4.2 to +5.3) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.35 | 4.91 | +12.9% (+1.9 to +23.8) | +24.3% (+10.7 to +38.0) | +15.2% (+2.1 to +28.3) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 588.6 | 577.3 | -1.9% (-16.4 to +12.5) | +19.5% (-33.1 to +72.0) | +0.7% (-10.7 to +12.1) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (5 trials, 0 allowed, 2 refused); acting: 512 to 640 (9 trials, 2 allowed, 1 refused); acting: 512 to 640 (6 trials, 2 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 0 refused); acting: 512 to 576 (4 trials, 1 allowed, 0 refused); run C: left native (6 trials, 0 allowed, 1 refused); acting: 512 to 704 (7 trials, 3 allowed, 1 refused); left native (5 trials, 0 allowed, 0 refused).

**Across 4 untouched workloads: 7 gauge-rows GAIN, 2 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 EVEN, 16 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
