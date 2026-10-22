# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,881 | -0.1% | -9.24 to 4.66 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,887 | -0.1% | -5.27 to 2.26 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.35 | 0.361 | +3.2% | -0.0315 to 0.0542 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.538 | 0.554 | +3.0% | -0.0447 to 0.0767 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.205 | +2.1% | -0.00559 to 0.0139 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -19 to 9.48 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.3% | -12.7 to 10.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,831 | 724,988 | +4.8% | 9,160 to 57,154 | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.211 | +4.7% | -0.056 to 0.0748 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 369 | +5.2% | -123 to 159 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.277 | +5.3% | -0.0927 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,925 | 2,926 | +0.0% | -3.69 to 5.31 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,929 | 2,929 | +0.0% | -2.61 to 4.04 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.356 | 0.358 | +0.6% | -0.0023 to 0.0063 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.5 | -0.3% | -0.0074 to 0.00407 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.14 | 0.139 | -0.1% | -0.00353 to 0.00317 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -14.1 to -3.11 | GAIN |
| bytes in the cache, mean (MB) | 406 | 401 | -1.3% | -5.81 to -4.57 | GAIN |
| pages read into the cache (misses) | 269,181 | 265,850 | -1.2% | -9,266 to 2,604 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.105 | -19.0% | -0.139 to 0.0891 | EVEN, no difference beyond the noise |
| host CPU-seconds | 95.8 | 74.3 | -22.4% | -118 to 75.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.139 | -22.4% | -0.221 to 0.14 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,905 | -0.0% | -3.98 to 1.44 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,907 | -0.0% | -3.97 to 1.45 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.28 | -0.2% | -0.00692 to 0.00559 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.446 | 0.445 | -0.4% | -0.00454 to 0.0012 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.147 | 0.149 | +1.1% | -0.000884 to 0.00409 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -7.05 to -0.109 | GAIN |
| bytes in the cache, mean (MB) | 418 | 418 | +0.0% | -1.36 to 1.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 663,721 | 691,274 | +4.2% | -17,453 to 72,559 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.188 | +22.8% | -0.055 to 0.125 | EVEN, no difference beyond the noise |
| host CPU-seconds | 274 | 349 | +27.1% | -117 to 265 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.206 | 0.261 | +27.1% | -0.0876 to 0.199 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,749 | 5,748 | -0.0% | -3.98 to 1.19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,765 | 5,765 | -0.0% | -6.31 to 5.43 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.319 | +0.3% | -0.00557 to 0.00757 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.485 | 0.497 | +2.5% | -0.0402 to 0.0642 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.188 | -1.1% | -0.0109 to 0.0069 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6 to -2.2 | GAIN |
| bytes in the cache, mean (MB) | 415 | 414 | -0.4% | -7.19 to 4.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,711 | 692,936 | +0.6% | -6,646 to 15,096 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.247 | +4.1% | -0.0118 to 0.0313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 427 | 449 | +5.2% | -25 to 69.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.16 | 0.168 | +5.2% | -0.00935 to 0.0259 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.0% | -15.9 to 13.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,887 | -0.0% | -15.3 to 14.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.358 | 0.358 | +0.2% | -0.00937 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.569 | 0.579 | +1.7% | -0.0241 to 0.0434 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.217 | 0.216 | -0.4% | -0.00917 to 0.00743 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.3% | -18.2 to 5.29 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 414 | -0.7% | -11.7 to 6.25 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 672,793 | 686,980 | +2.1% | -11,157 to 39,532 | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.259 | +7.8% | -0.0773 to 0.115 | EVEN, no difference beyond the noise |
| host CPU-seconds | 420 | 464 | +10.4% | -183 to 270 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.316 | 0.349 | +10.4% | -0.136 to 0.202 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
