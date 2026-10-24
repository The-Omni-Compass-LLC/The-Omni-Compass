# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,935 | -0.1% | -9.22 to 3.32 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,940 | 2,937 | -0.1% | -8.53 to 2.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.149 | 0.166 | +11.4% | -0.0392 to 0.0732 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.354 | 0.364 | +2.8% | -0.0205 to 0.0405 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0681 | 0.0697 | +2.3% | -0.00595 to 0.0091 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.83 to -1.76 | GAIN |
| bytes in the cache, mean (MB) | 418 | 419 | +0.2% | -10 to 12.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 712,552 | 738,240 | +3.6% | -33,898 to 85,274 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.083 | -13.5% | -0.0827 to 0.0567 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 149 | -15.2% | -165 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.131 | 0.111 | -15.1% | -0.123 to 0.0834 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,877 | -0.1% | -7.11 to 1.29 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,886 | -0.1% | -5.24 to 1.91 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.503 | 0.507 | +0.7% | -0.00384 to 0.0105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.652 | 0.668 | +2.5% | -0.0185 to 0.0505 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.224 | +0.7% | 0.000728 to 0.00237 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -18.8 to -3.34 | GAIN |
| bytes in the cache, mean (MB) | 397 | 397 | -0.0% | -13.8 to 13.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 260,515 | 271,870 | +4.4% | -1,269 to 23,979 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.191 | -8.9% | -0.0722 to 0.0348 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 132 | -11.6% | -67.6 to 33 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.249 | -11.5% | -0.127 to 0.062 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.0% | -3.88 to 1.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,892 | -0.0% | -3.88 to 1.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.306 | +1.3% | 0.00152 to 0.00648 | LOSS |
| latency, 99th percentile (ms) | 0.471 | 0.463 | -1.7% | -0.0218 to 0.00583 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.189 | -0.5% | -0.0021 to 0.000357 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 478 | -6.7% | -108 to 40 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 396 | -5.1% | -79.6 to 36.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 650,187 | 796,726 | +22.5% | 74,537 to 218,540 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.179 | -12.2% | -0.0809 to 0.031 | EVEN, no difference beyond the noise |
| host CPU-seconds | 363 | 309 | -14.9% | -175 to 66.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.272 | 0.232 | -14.9% | -0.131 to 0.0499 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | -0.484 to 4.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,752 | 5,744 | -0.1% | -23.7 to 9.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,770 | 5,763 | -0.1% | -23.6 to 8.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.349 | +0.3% | -0.00148 to 0.00348 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.628 | 0.626 | -0.3% | -0.0111 to 0.00774 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.165 | 0.165 | -0.2% | -0.00411 to 0.00361 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -38 to 16.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 410 | -1.5% | -28.2 to 15.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 693,007 | 708,353 | +2.2% | -37,901 to 68,594 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.243 | +3.6% | -0.00783 to 0.0247 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 447 | +4.6% | -16.8 to 56.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.168 | +4.7% | -0.0062 to 0.0212 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,875 | +0.0% | -8.31 to 8.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,886 | +0.0% | -8.36 to 9.18 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.37 | 0.367 | -0.8% | -0.00548 to -0.000516 | GAIN |
| latency, 99th percentile (ms) | 0.598 | 0.597 | -0.3% | -0.0153 to 0.012 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.222 | 0.223 | +0.3% | -0.0029 to 0.00427 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.07 to -2.09 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -4.31 to 0.158 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,081 | 682,938 | +0.6% | -11,254 to 18,968 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.261 | +7.4% | -0.0612 to 0.0972 | EVEN, no difference beyond the noise |
| host CPU-seconds | 422 | 463 | +9.7% | -141 to 223 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.318 | 0.349 | +9.6% | -0.107 to 0.168 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
