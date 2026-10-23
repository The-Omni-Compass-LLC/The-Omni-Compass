# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,881 | -0.1% | -8.94 to 1.62 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,886 | -0.1% | -7.52 to 0.977 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.343 | 0.363 | +5.8% | -0.0321 to 0.0721 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.58 | 0.589 | +1.6% | -0.0107 to 0.0287 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.205 | +2.6% | 0.00414 to 0.00608 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.5% | -4.39 to -0.235 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.4% | -7.13 to 4.15 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,716 | 753,681 | +11.7% | -35,420 to 193,351 | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.218 | +11.0% | -0.0141 to 0.0572 | EVEN, no difference beyond the noise |
| host CPU-seconds | 340 | 386 | +13.4% | -34.9 to 126 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.29 | +13.4% | -0.026 to 0.0946 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,929 | -0.1% | -10.6 to 1.88 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,937 | 2,936 | -0.1% | -4.19 to 0.793 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.246 | 0.265 | +7.9% | -0.0304 to 0.0691 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.411 | 0.468 | +14.0% | -0.0873 to 0.203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0798 | 0.0872 | +9.3% | -0.00674 to 0.0215 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -19.5 to -1.46 | GAIN |
| bytes in the cache, mean (MB) | 405 | 400 | -1.1% | -19.1 to 10.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 259,091 | 271,478 | +4.8% | 5,004 to 19,769 | shown, not judged |
| host CPU busy (share of the run) | 0.0649 | 0.0776 | +19.6% | -0.0674 to 0.0929 | EVEN, no difference beyond the noise |
| host CPU-seconds | 45.7 | 55.5 | +21.5% | -52.4 to 72.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0854 | 0.104 | +21.7% | -0.0982 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% | -5.19 to 1.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -4.09 to -0.36 | LOSS |
| latency, 95th percentile (ms) | 0.312 | 0.309 | -0.9% | -0.0282 to 0.0228 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.506 | 0.509 | +0.5% | -0.0276 to 0.0323 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.193 | +1.7% | -0.00486 to 0.0114 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.1% | -20.1 to 9.23 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 416 | -0.5% | -17.2 to 13.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,663 | 710,310 | +3.7% | -108,498 to 159,792 | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.207 | -3.0% | -0.132 to 0.119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 387 | 369 | -4.6% | -301 to 266 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.291 | 0.278 | -4.6% | -0.227 to 0.2 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,685 | 5,671 | -0.2% | -48.8 to 22.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,702 | 5,689 | -0.2% | -47.8 to 21.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.428 | 0.429 | +0.2% | -0.00645 to 0.00845 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.655 | 0.657 | +0.3% | -0.0104 to 0.0144 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.246 | +0.1% | -0.00486 to 0.00528 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.4% | -46.1 to 22.1 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 408 | -2.0% | -35.6 to 18.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 685,076 | 701,742 | +2.4% | -43,646 to 76,978 | shown, not judged |
| host CPU busy (share of the run) | 0.319 | 0.322 | +0.9% | -0.00344 to 0.00915 | EVEN, no difference beyond the noise |
| host CPU-seconds | 573 | 580 | +1.2% | -6.71 to 20.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.219 | +1.3% | -0.00229 to 0.0079 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,875 | -0.1% | -25.2 to 16.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,883 | -0.1% | -25.5 to 17.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.345 | 0.343 | -0.7% | -0.00377 to -0.000899 | GAIN |
| latency, 99th percentile (ms) | 0.547 | 0.546 | -0.3% | -0.0228 to 0.0195 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.207 | 0.208 | +0.4% | -0.00152 to 0.00307 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -5.64 to -3.25 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.4% | -3.82 to 0.767 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,332 | 681,344 | +1.0% | -425 to 14,449 | shown, not judged |
| host CPU busy (share of the run) | 0.255 | 0.259 | +1.7% | -0.0401 to 0.0487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 458 | 468 | +2.1% | -101 to 120 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.345 | 0.352 | +2.1% | -0.076 to 0.0907 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
