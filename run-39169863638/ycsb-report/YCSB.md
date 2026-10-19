# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `2b4c11e3aee0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,911 | +0.0% | -1.74 to 4.54 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,916 | 2,917 | +0.0% | -3.49 to 5.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.262 | +1.8% | -0.025 to 0.0343 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.414 | 0.414 | -0.1% | -0.0145 to 0.0138 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.178 | 0.18 | +1.0% | -0.0142 to 0.0177 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,361 | -0.1% | -2.13 to 0.216 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,802 | 61,837 | +0.1% | -271 to 343 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.141 | -8.4% | -0.111 to 0.0851 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 253 | -10.1% | -234 to 177 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.189 | -10.1% | -0.175 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `2b4c11e3aee0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,903 | +0.3% | -11.3 to 27.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,909 | +0.3% | -9.92 to 29.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.328 | 0.331 | +1.0% | -0.0132 to 0.0199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.438 | 0.464 | +5.8% | -0.0485 to 0.0992 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.175 | 0.175 | -0.2% | -0.0306 to 0.0297 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,509 | +0.1% | -16.7 to 18.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,496 | 77,680 | +0.2% | -153 to 523 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.148 | +0.9% | -0.0637 to 0.0664 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 106 | +1.1% | -53.8 to 56.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.2 | +0.8% | -0.101 to 0.104 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `2b4c11e3aee0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,933 | -0.0% | -3.17 to 1.89 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,936 | 2,935 | -0.0% | -2.99 to 1.75 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.22 | 0.222 | +0.9% | -0.00457 to 0.00857 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.398 | 0.401 | +0.7% | -0.0142 to 0.0196 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.105 | 0.106 | +0.3% | -0.00171 to 0.00241 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,349 | -0.0% | -4.28 to 2.99 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,692 | 61,655 | -0.1% | -204 to 129 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.115 | -10.4% | -0.126 to 0.0987 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 211 | -11.9% | -266 to 209 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.158 | -11.9% | -0.199 to 0.156 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `2b4c11e3aee0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,738 | 5,740 | +0.0% | -3.58 to 7.34 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,748 | 5,751 | +0.0% | -3.03 to 7.61 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.359 | 0.36 | +0.4% | -0.00246 to 0.00513 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.57 | 0.574 | +0.6% | -0.0105 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.197 | +0.5% | -0.000682 to 0.0028 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,364 | -0.0% | -2.81 to 1.83 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,887 | 63,033 | +0.2% | -159 to 451 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.267 | +6.3% | -0.0086 to 0.0402 | EVEN, no difference beyond the noise |
| host CPU-seconds | 454 | 492 | +8.4% | -26.1 to 102 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.171 | 0.185 | +8.3% | -0.00986 to 0.0383 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `2b4c11e3aee0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | +0.0% | -6.2 to 7.54 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,900 | +0.0% | -6.41 to 7.88 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.314 | 0.314 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, 99th percentile (ms) | 0.454 | 0.455 | +0.1% | -0.0045 to 0.00584 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.195 | +0.4% | -0.00176 to 0.00332 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,365 | +0.1% | -3.95 to 7.22 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,889 | 63,211 | +0.5% | -188 to 833 | shown, not judged |
| host CPU busy (share of the run) | 0.227 | 0.234 | +2.8% | -0.0367 to 0.0494 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 423 | +3.2% | -87.1 to 113 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.307 | 0.317 | +3.2% | -0.0654 to 0.085 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
