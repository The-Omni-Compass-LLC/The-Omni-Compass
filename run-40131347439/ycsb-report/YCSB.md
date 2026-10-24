# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,882 | -0.1% | -4.01 to 0.857 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.1% | -2.01 to -0.902 | LOSS |
| latency, 95th percentile (ms) | 0.328 | 0.327 | -0.4% | -0.0258 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.646 | 0.647 | +0.1% | -0.0267 to 0.028 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.197 | -0.2% | -0.00207 to 0.00133 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.9 to -1.17 | GAIN |
| bytes in the cache, mean (MB) | 416 | 418 | +0.3% | -4.93 to 7.46 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 742,313 | 720,505 | -2.9% | -58,761 to 15,145 | shown, not judged |
| host CPU busy (share of the run) | 0.193 | 0.207 | +7.3% | -0.0154 to 0.0435 | EVEN, no difference beyond the noise |
| host CPU-seconds | 336 | 367 | +9.4% | -35.3 to 98.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.252 | 0.276 | +9.4% | -0.0263 to 0.0738 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,932 | 2,929 | -0.1% | -11.9 to 6.99 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,935 | 2,933 | -0.1% | -10.1 to 5.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.246 | 0.252 | +2.3% | -0.024 to 0.0353 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.424 | 0.436 | +2.8% | -0.0572 to 0.0806 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0841 | 0.0852 | +1.2% | -0.0164 to 0.0185 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 480 | -6.3% | -113 to 49 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 403 | 379 | -5.8% | -95.8 to 49.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 257,102 | 273,001 | +6.2% | -34,364 to 66,161 | shown, not judged |
| host CPU busy (share of the run) | 0.0919 | 0.106 | +15.0% | -0.166 to 0.194 | EVEN, no difference beyond the noise |
| host CPU-seconds | 68 | 77.4 | +13.8% | -137 to 156 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.127 | 0.145 | +13.8% | -0.256 to 0.292 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -6.14 to 4.49 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -5.31 to 3.68 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.324 | -0.1% | -0.00792 to 0.00726 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.508 | 0.507 | -0.3% | -0.0182 to 0.0156 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.199 | +1.3% | -0.00262 to 0.00785 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -20.6 to 10.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 419 | -0.0% | -21.3 to 21 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,001 | 695,688 | +2.3% | -5,747 to 37,121 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.231 | +12.5% | -0.0705 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 363 | 418 | +15.1% | -158 to 268 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.314 | +15.1% | -0.119 to 0.201 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,683 | 5,671 | -0.2% | -43.9 to 19.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,701 | 5,689 | -0.2% | -40.8 to 17.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.433 | +3.0% | -0.00846 to 0.0338 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.66 | +3.5% | -0.00423 to 0.0489 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.247 | +2.4% | -0.00759 to 0.0191 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.86 to -1.92 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.4% | -4.72 to 1.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 680,861 | 684,814 | +0.6% | -10,010 to 17,916 | shown, not judged |
| host CPU busy (share of the run) | 0.318 | 0.332 | +4.4% | -0.0139 to 0.0419 | EVEN, no difference beyond the noise |
| host CPU-seconds | 570 | 601 | +5.5% | -30 to 92.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.227 | +5.7% | -0.0118 to 0.0361 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,874 | -0.0% | -10.3 to 8.26 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -9.24 to 7.35 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.359 | -0.6% | -0.00448 to 0.000484 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.579 | 0.581 | +0.3% | -0.0228 to 0.0262 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.218 | -0.2% | -0.00279 to 0.0019 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -5.98 to -2.72 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -4.1 to -0.586 | GAIN |
| pages read into the cache (misses) | 675,000 | 674,158 | -0.1% | -35,298 to 33,615 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.24 | -5.5% | -0.0353 to 0.00765 | EVEN, no difference beyond the noise |
| host CPU-seconds | 450 | 417 | -7.3% | -91.1 to 25 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.34 | 0.315 | -7.4% | -0.0697 to 0.0197 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
