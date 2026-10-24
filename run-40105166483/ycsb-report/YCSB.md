# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -2.4 to 1.85 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -3.52 to 2.02 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.321 | +1.2% | -0.00432 to 0.0117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.578 | 0.568 | -1.8% | -0.0296 to 0.00831 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.197 | +0.1% | -0.0034 to 0.00367 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -7.14 to -1.56 | GAIN |
| bytes in the cache, mean (MB) | 416 | 416 | -0.0% | -5.72 to 5.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 690,444 | 688,640 | -0.3% | -51,521 to 47,913 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.199 | -3.5% | -0.0888 to 0.0744 | EVEN, no difference beyond the noise |
| host CPU-seconds | 365 | 348 | -4.7% | -202 to 167 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.274 | 0.262 | -4.7% | -0.152 to 0.126 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,935 | -0.0% | -3.3 to 2.79 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,938 | -0.0% | -4.29 to 3.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.234 | 0.239 | +2.3% | -0.00226 to 0.0129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.406 | 0.415 | +2.1% | -0.0321 to 0.0488 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.08 | 0.0813 | +1.6% | -0.000744 to 0.00337 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -12.7 to -2.49 | GAIN |
| bytes in the cache, mean (MB) | 408 | 401 | -1.6% | -19.1 to 6.36 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,170 | 275,392 | +4.6% | -5,516 to 29,961 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.0824 | -25.3% | -0.171 to 0.115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 82.4 | 59.5 | -27.9% | -139 to 92.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.111 | -27.9% | -0.259 to 0.173 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,911 | 2,909 | -0.0% | -13.6 to 10.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,914 | 2,913 | -0.0% | -13.3 to 11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.187 | 0.19 | +1.6% | 0.000516 to 0.00548 | LOSS |
| latency, 99th percentile (ms) | 0.359 | 0.362 | +0.8% | -0.00838 to 0.0144 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.136 | 0.138 | +0.8% | -0.00848 to 0.0107 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.42 to -1.21 | GAIN |
| bytes in the cache, mean (MB) | 419 | 419 | +0.1% | -11.7 to 12.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,367 | 739,183 | +8.6% | -26,115 to 143,746 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.149 | -4.2% | -0.0485 to 0.0353 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 266 | -5.3% | -102 to 72.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.199 | -5.3% | -0.0765 to 0.0544 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,665 | 5,673 | +0.2% | -40.6 to 57.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,683 | 5,691 | +0.1% | -40.1 to 55.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.436 | -0.4% | -0.0111 to 0.00774 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.673 | 0.668 | -0.7% | -0.0226 to 0.0133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.25 | 0.249 | -0.4% | -0.00878 to 0.00691 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -20.5 to 6.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 412 | -1.0% | -13.6 to 5.38 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,202 | 692,171 | +1.5% | -3,868 to 23,807 | shown, not judged |
| host CPU busy (share of the run) | 0.333 | 0.329 | -1.3% | -0.0186 to 0.0103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 604 | 593 | -1.9% | -47.2 to 24.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.224 | -2.1% | -0.0177 to 0.00823 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,931 | -0.0% | -5.34 to 3.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.0% | -3.52 to 1.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.157 | 0.162 | +3.0% | -0.00537 to 0.0147 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.371 | 0.38 | +2.4% | -0.0158 to 0.0338 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0835 | 0.0831 | -0.5% | -0.00979 to 0.00902 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -7.21 to -1.77 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.5% | -5.33 to 1.19 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,563 | 692,262 | +1.7% | -16,807 to 40,205 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.112 | -10.6% | -0.0638 to 0.0372 | EVEN, no difference beyond the noise |
| host CPU-seconds | 228 | 202 | -11.5% | -128 to 75.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.151 | -11.5% | -0.0958 to 0.0566 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
