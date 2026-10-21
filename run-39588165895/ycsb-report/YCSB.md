# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,885 | -0.1% | -5.19 to -0.827 | LOSS |
| throughput (operations a second) | 2,892 | 2,889 | -0.1% | -4.24 to -1.51 | LOSS |
| latency, 95th percentile (ms) | 0.323 | 0.33 | +2.3% | -0.000653 to 0.0153 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.476 | 0.481 | +1.0% | -0.0113 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.185 | +0.9% | -0.000139 to 0.00344 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -7.68 to 0.371 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -14.7 to 10.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 675,547 | 689,675 | +2.1% | -5,865 to 34,122 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.237 | +3.6% | -0.0199 to 0.0365 | EVEN, no difference beyond the noise |
| host CPU-seconds | 421 | 440 | +4.4% | -49 to 86.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.316 | 0.33 | +4.5% | -0.0366 to 0.0649 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -4.23 to 3.53 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -3.43 to 2.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.37 | 0.37 | +0.0% | -0.0203 to 0.0203 | EVEN, the same |
| latency, 99th percentile (ms) | 0.521 | 0.519 | -0.5% | -0.0252 to 0.0199 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.0% | -0.00494 to 0.00482 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -58.3 to 22.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 394 | -1.8% | -59.7 to 45.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,331 | 273,888 | +2.8% | -10,443 to 25,557 | shown, not judged |
| host CPU busy (share of the run) | 0.226 | 0.211 | -6.5% | -0.0533 to 0.0242 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 153 | -8.0% | -47.2 to 20.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.312 | 0.287 | -8.0% | -0.0886 to 0.0388 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,936 | -0.1% | -4.55 to -0.379 | LOSS |
| throughput (operations a second) | 2,940 | 2,938 | -0.1% | -4.55 to -0.383 | LOSS |
| latency, 95th percentile (ms) | 0.098 | 0.0983 | +0.3% | -0.01 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.299 | 0.301 | +0.7% | -0.000484 to 0.00448 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0597 | 0.0591 | -0.9% | -0.0016 to 0.000532 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -24.4 to 6.92 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 412 | -1.7% | -30.6 to 16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,267 | 674,432 | -1.4% | -104,010 to 84,340 | shown, not judged |
| host CPU busy (share of the run) | 0.083 | 0.0674 | -18.8% | -0.0775 to 0.0464 | EVEN, no difference beyond the noise |
| host CPU-seconds | 151 | 121 | -19.9% | -150 to 89.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.113 | 0.0902 | -19.9% | -0.112 to 0.0668 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,679 | 5,668 | -0.2% | -54.8 to 32.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,698 | 5,687 | -0.2% | -53.5 to 31 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.434 | +0.5% | -0.00992 to 0.0146 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.662 | 0.661 | -0.2% | -0.0227 to 0.0207 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.249 | +0.6% | -0.00409 to 0.00702 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -4.44 to -3.25 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.4% | -2.94 to -0.0569 | GAIN |
| pages read into the cache (misses) | 681,458 | 690,884 | +1.4% | -7,536 to 26,389 | shown, not judged |
| host CPU busy (share of the run) | 0.327 | 0.33 | +0.7% | -0.0279 to 0.0328 | EVEN, no difference beyond the noise |
| host CPU-seconds | 590 | 595 | +0.8% | -63.7 to 73.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.225 | +0.9% | -0.0224 to 0.0264 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,911 | 2,908 | -0.1% | -11.9 to 4.16 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,914 | -0.1% | -11 to 4.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.24 | 0.243 | +1.5% | -0.0199 to 0.0273 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.481 | 0.489 | +1.7% | -0.0364 to 0.0531 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.129 | 0.133 | +2.8% | -0.000925 to 0.0081 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -16 to 1.92 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 415 | -1.0% | -12.2 to 3.94 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,485 | 690,548 | +1.0% | -14,233 to 28,359 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.197 | +22.5% | 0.0117 to 0.0607 | power given |
| host CPU-seconds | 286 | 365 | +27.6% | 25.1 to 133 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.274 | +27.7% | 0.0185 to 0.1 | power given |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
