# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40238131083 | `2d40c4c64109` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| B | 40260620209 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |
| C | 40284624594 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,878 | -0.0% (-0.3 to +0.2) | +0.0% (-0.2 to +0.3) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% (-0.3 to +0.3) | +0.0% (-0.2 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.344 | 0.348 | +1.2% (+0.4 to +1.9) | -0.6% (-3.2 to +2.0) | +0.6% (-6.1 to +7.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.62 | 0.621 | +0.2% (-1.3 to +1.7) | -1.0% (-4.7 to +2.8) | +0.1% (-2.4 to +2.6) | EVEN, under the floor (the three runs' mean 0.21%) |
| latency, mean (ms) | 0.21 | 0.21 | +0.0% (-2.2 to +2.3) | -2.0% (-4.5 to +0.5) | -0.2% (-6.7 to +6.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,361 | -0.1% (-0.4 to +0.1) | +0.0% (-0.5 to +0.6) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| pages read into the cache (misses) | 62,862 | 62,903 | +0.1% (-1.2 to +1.4) | +0.0% (-0.8 to +0.8) | +0.6% (-0.9 to +2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.232 | 0.21 | -9.3% (-20.1 to +1.5) | -9.1% (-32.9 to +14.8) | -7.4% (-36.0 to +21.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 409.5 | 361.2 | -11.8% (-25.5 to +1.9) | -11.5% (-43.1 to +20.1) | -9.8% (-45.2 to +25.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.272 | -11.8% (-25.4 to +1.9) | -11.5% (-42.9 to +19.9) | -9.8% (-45.2 to +25.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 233.5 | 234.7 | +0.5% (-0.9 to +2.0) | -2.2% (-4.9 to +0.6) | +0.1% (-7.5 to +7.7) | **the runs disagree** |
| the server's own CPU-seconds (mongod) | 230.9 | 232.1 | +0.5% (-1.0 to +2.0) | -2.2% (-4.9 to +0.5) | +0.0% (-7.7 to +7.7) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 2.59 | +2.7% (+1.0 to +4.3) | +1.9% (-6.0 to +9.8) | +3.0% (+0.5 to +5.5) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 409.5 | 361.2 | -11.8% (-25.5 to +1.9) | -11.5% (-43.1 to +20.1) | -9.8% (-45.2 to +25.6) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,887 | -0.0% (-0.2 to +0.1) | -0.1% (-0.4 to +0.2) | -0.7% (-3.4 to +2.0) | EVEN, under the floor (the three runs' mean 0.27%) |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% (-0.2 to +0.1) | -0.1% (-0.3 to +0.2) | -0.7% (-3.4 to +2.0) | EVEN, under the floor (the three runs' mean 0.26%) |
| latency, 95th percentile (ms) | 0.31 | 0.328 | +5.8% (-8.1 to +19.7) | +22.6% (-26.5 to +71.7) | +1.9% (-9.9 to +13.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.505 | 0.515 | +2.0% (-5.1 to +9.2) | +5.2% (-2.2 to +12.6) | +2.2% (-10.4 to +14.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.187 | 0.189 | +1.6% (-2.4 to +5.5) | +4.2% (-17.6 to +26.0) | +6.5% (-8.3 to +21.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,365 | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | -0.2% (-0.7 to +0.4) | EVEN, under the floor (the three runs' mean 0.05%) |
| pages read into the cache (misses) | 61,796 | 61,828 | +0.1% (-0.2 to +0.3) | +0.2% (-0.4 to +0.7) | +0.2% (-0.4 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.179 | -1.2% (-32.8 to +30.5) | -18.1% (-46.4 to +10.3) | +8.0% (-28.2 to +44.1) | **the runs disagree** |
| host CPU-seconds | 313.6 | 307.8 | -1.9% (-40.1 to +36.4) | -19.9% (-49.2 to +9.3) | +10.3% (-33.0 to +53.6) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.236 | 0.231 | -1.8% (-40.1 to +36.5) | -19.9% (-49.3 to +9.5) | +11.1% (-31.9 to +54.1) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 181.9 | 184.1 | +1.2% (-3.2 to +5.6) | +5.7% (-12.3 to +23.6) | -0.2% (-5.1 to +4.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 179.4 | 181.5 | +1.2% (-3.1 to +5.4) | +5.4% (-12.5 to +23.3) | -0.3% (-5.1 to +4.4) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.45 | 2.58 | +5.3% (-8.3 to +18.8) | +14.3% (-6.6 to +35.3) | +5.0% (-4.0 to +14.1) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 313.6 | 307.8 | -1.9% (-40.2 to +36.4) | -19.9% (-49.2 to +9.3) | +10.3% (-33.0 to +53.6) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7481 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,920 | 2,918 | -0.1% (-0.4 to +0.3) | -0.1% (-1.8 to +1.6) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.07%) |
| throughput (operations a second) | 2,924 | 2,923 | -0.1% (-0.4 to +0.3) | -0.1% (-1.2 to +0.9) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 0.378 | 0.385 | +1.9% (-2.7 to +6.5) | +0.1% (-17.5 to +17.7) | +4.3% (-6.4 to +15.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.535 | 0.559 | +4.6% (-6.6 to +15.7) | +0.6% (-49.8 to +50.9) | +4.8% (-2.5 to +12.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.139 | 0.142 | +2.5% (-1.5 to +6.5) | +0.6% (-16.5 to +17.7) | +4.7% (-3.9 to +13.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,515 | 1,518 | +0.2% (-0.3 to +0.7) | -0.3% (-2.3 to +1.7) | +0.1% (-0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.01%) |
| pages read into the cache (misses) | 77,655 | 77,726 | +0.1% (-0.6 to +0.8) | +0.0% (-0.8 to +0.9) | +0.1% (-0.5 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.147 | +14.4% (-33.9 to +62.7) | +2.2% (-44.7 to +49.1) | +12.5% (-146.5 to +171.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 94.9 | 109.5 | +15.3% (-42.0 to +72.6) | +3.3% (-59.3 to +66.0) | +14.6% (-160.0 to +189.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.178 | 0.205 | +15.4% (-41.6 to +72.4) | +3.4% (-57.9 to +64.7) | +14.6% (-160.0 to +189.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 38.2 | 39.2 | +2.4% (-0.2 to +5.0) | +0.9% (-8.2 to +9.9) | +3.9% (+1.6 to +6.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the server's own CPU-seconds (mongod) | 37.4 | 38.3 | +2.3% (-0.2 to +4.9) | +0.8% (-8.2 to +9.8) | +3.9% (+1.3 to +6.5) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.817 | 0.868 | +6.2% (-1.1 to +13.6) | +2.6% (-12.3 to +17.6) | +4.8% (-6.4 to +15.9) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 94.9 | 109.5 | +15.3% (-42.0 to +72.6) | +3.3% (-59.3 to +66.0) | +14.6% (-160.0 to +189.1) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,910 | -0.1% (-0.1 to -0.0) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% (-0.1 to -0.0) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 0.178 | 0.179 | +0.7% (-2.2 to +3.7) | +0.2% (-2.2 to +2.7) | +2.7% (-8.8 to +14.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.347 | 0.338 | -2.6% (-7.3 to +2.1) | -0.2% (-5.4 to +5.1) | +3.3% (-9.6 to +16.2) | **the runs disagree** |
| latency, mean (ms) | 0.131 | 0.132 | +0.3% (-2.5 to +3.1) | +1.2% (-3.7 to +6.0) | +1.2% (-2.3 to +4.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,349 | 1,349 | +0.0% (-0.2 to +0.2) | +0.0% (-0.3 to +0.3) | -0.1% (-0.2 to -0.0) | EVEN, under the floor (the three runs' mean 0.02%) |
| pages read into the cache (misses) | 61,625 | 61,688 | +0.1% (+0.0 to +0.2) | +0.0% (-0.3 to +0.3) | -0.1% (-0.3 to +0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.144 | -0.4% (-60.1 to +59.2) | +5.3% (-6.2 to +16.9) | +3.2% (-126.7 to +133.0) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 263.3 | 259.5 | -1.4% (-69.6 to +66.7) | +5.9% (-6.8 to +18.6) | +3.1% (-134.9 to +141.0) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.194 | -1.4% (-69.5 to +66.7) | +5.9% (-6.8 to +18.6) | +3.1% (-134.9 to +141.0) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 128.0 | 129.0 | +0.8% (-1.7 to +3.2) | +2.2% (-8.0 to +12.4) | +1.1% (-0.7 to +2.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (mongod) | 125.9 | 126.8 | +0.7% (-1.8 to +3.2) | +2.2% (-8.2 to +12.5) | +1.0% (-0.7 to +2.7) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.05 | 2.14 | +4.1% (-8.2 to +16.5) | +4.7% (+1.0 to +8.4) | +5.1% (-3.6 to +13.9) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 263.3 | 259.5 | -1.4% (-69.6 to +66.7) | +5.9% (-6.8 to +18.6) | +3.1% (-134.9 to +141.0) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,669 | 5,669 | +0.0% (-0.4 to +0.4) | -0.0% (-0.3 to +0.3) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.02%) |
| throughput (operations a second) | 5,682 | 5,683 | +0.0% (-0.4 to +0.4) | -0.0% (-0.3 to +0.3) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.416 | 0.418 | +0.6% (-2.2 to +3.3) | +2.3% (-1.6 to +6.1) | +0.3% (-1.0 to +1.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.635 | 0.64 | +0.8% (-1.9 to +3.6) | +1.9% (-10.0 to +13.8) | -0.6% (-2.0 to +0.9) | **the runs disagree** |
| latency, mean (ms) | 0.237 | 0.238 | +0.4% (-2.2 to +3.0) | +0.5% (-0.1 to +1.1) | +0.1% (-1.2 to +1.3) | EVEN, under the floor (the three runs' mean 0.34%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,360 | -0.1% (-0.1 to +0.0) | -0.1% (-0.9 to +0.7) | +0.0% (-0.5 to +0.6) | EVEN, under the floor (the three runs' mean 0.04%) |
| pages read into the cache (misses) | 62,957 | 63,226 | +0.4% (-0.5 to +1.3) | +0.4% (-0.5 to +1.3) | +0.1% (-0.8 to +1.0) | shown, not judged |
| host CPU busy (share of the run) | 0.304 | 0.308 | +1.1% (-4.2 to +6.3) | -4.7% (-62.0 to +52.6) | -3.7% (-8.0 to +0.6) | **the runs disagree** |
| host CPU-seconds | 551.7 | 558.1 | +1.2% (-6.1 to +8.4) | -5.5% (-71.1 to +60.0) | -5.2% (-10.8 to +0.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.211 | +1.2% (-6.5 to +8.9) | -5.5% (-70.9 to +59.8) | -5.3% (-10.9 to +0.4) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 313.7 | 315.1 | +0.5% (-3.1 to +4.0) | +1.1% (-1.1 to +3.3) | -0.3% (-1.9 to +1.4) | EVEN, under the floor (the three runs' mean 0.44%) |
| the server's own CPU-seconds (mongod) | 309.3 | 310.6 | +0.4% (-3.1 to +3.9) | +1.0% (-1.5 to +3.5) | -0.3% (-1.8 to +1.3) | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.37 | 4.48 | +2.6% (-4.3 to +9.4) | +4.7% (-7.3 to +16.7) | +0.6% (-5.8 to +7.1) | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 551.7 | 558.1 | +1.2% (-6.1 to +8.4) | -5.5% (-71.1 to +60.0) | -5.2% (-10.8 to +0.3) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 0 gauge-rows GAIN, 9 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 22 EVEN, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
