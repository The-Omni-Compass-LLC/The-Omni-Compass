# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,908 | 2,909 | +0.1% | -8.93 to 12.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,914 | +0.1% | -8.56 to 12.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.199 | 0.205 | +3.0% | 0.00352 to 0.00848 | LOSS |
| latency, 99th percentile (ms) | 0.392 | 0.402 | +2.7% | -0.0142 to 0.0356 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.142 | -2.3% | -0.0289 to 0.0222 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,365 | +0.1% | -12.7 to 16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,799 | 61,859 | +0.1% | -1.05 to 120 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.164 | +16.8% | -0.0216 to 0.0689 | EVEN, no difference beyond the noise |
| host CPU-seconds | 251 | 301 | +20.0% | -44.6 to 145 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.188 | 0.225 | +20.0% | -0.0331 to 0.108 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -2.73 to 2.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -2.51 to 1.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.506 | 0.507 | +0.2% | -0.0121 to 0.0141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.632 | 0.629 | -0.4% | -0.0235 to 0.0188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.215 | -0.4% | -0.00683 to 0.00508 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,506 | 1,505 | -0.1% | -6.05 to 4.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,583 | 77,602 | +0.0% | -237 to 276 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.211 | +11.9% | -0.0898 to 0.135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 133 | 152 | +14.2% | -79.6 to 117 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.285 | +14.1% | -0.15 to 0.22 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -2.29 to 1.14 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -2.56 to 1.48 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.306 | 0.303 | -1.0% | -0.00548 to -0.000516 | GAIN |
| latency, 99th percentile (ms) | 0.521 | 0.519 | -0.3% | -0.00965 to 0.00632 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.186 | +0.2% | -0.00424 to 0.00514 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.0% | -1.88 to 2.31 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,658 | 61,674 | +0.0% | -136 to 168 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.198 | +1.0% | -0.116 to 0.12 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 351 | +0.9% | -262 to 269 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.261 | 0.264 | +0.9% | -0.197 to 0.202 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,670 | 5,529 | -2.5% | -230 to -51.9 | LOSS |
| throughput (operations a second) | 5,683 | 5,544 | -2.4% | -223 to -54 | LOSS |
| latency, 95th percentile (ms) | 0.309 | 0.309 | +0.1% | -0.0142 to 0.0149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.467 | 0.492 | +5.4% | -0.0491 to 0.0991 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.198 | +4.0% | 0.00172 to 0.0134 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,355 | 1,352 | -0.2% | -15.8 to 10.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,020 | 63,031 | +0.0% | -558 to 579 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.216 | -7.8% | -0.074 to 0.0374 | EVEN, no difference beyond the noise |
| host CPU-seconds | 429 | 389 | -9.4% | -162 to 81.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.151 | -7.2% | -0.06 to 0.0365 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,938 | -0.0% | -7.34 to 7.34 | EVEN, the same |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -6.37 to 6.12 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.129 | 0.136 | +5.4% | -0.00811 to 0.0221 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.338 | 0.35 | +3.6% | -0.00311 to 0.0271 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0714 | 0.0724 | +1.3% | -0.00528 to 0.00718 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.0% | -6.42 to 7.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,386 | 63,223 | -0.3% | -472 to 147 | shown, not judged |
| host CPU busy (share of the run) | 0.0888 | 0.105 | +18.4% | -0.0625 to 0.0951 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 192 | +20.0% | -127 to 190 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.143 | +20.0% | -0.0946 to 0.142 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
