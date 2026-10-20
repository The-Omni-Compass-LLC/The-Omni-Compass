# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,896 | -0.1% | -6.9 to 0.996 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,899 | -0.1% | -6.14 to 0.548 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.307 | 0.316 | +2.9% | -0.0197 to 0.0377 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.439 | 0.451 | +2.8% | -0.0328 to 0.0575 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.184 | +1.4% | -0.000169 to 0.00515 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -3.96 to -2.9 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.1% | -4.09 to 3.07 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,271 | 701,365 | +2.1% | -68,677 to 96,865 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.2 | -5.2% | -0.0708 to 0.0487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 384 | 357 | -7.1% | -165 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.288 | 0.268 | -7.1% | -0.124 to 0.0827 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,897 | -0.0% | -5.88 to 5.03 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,900 | -0.0% | -2.41 to -0.219 | LOSS |
| latency, 95th percentile (ms) | 0.362 | 0.363 | +0.4% | -0.00154 to 0.0042 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.486 | 0.481 | -1.0% | -0.04 to 0.0307 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.196 | -1.9% | -0.0217 to 0.014 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.8% | -14 to -4.49 | GAIN |
| bytes in the cache, mean (MB) | 405 | 398 | -1.6% | -15.1 to 1.95 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,964 | 263,921 | +0.4% | -7,087 to 9,002 | shown, not judged |
| host CPU busy (share of the run) | 0.219 | 0.198 | -9.5% | -0.102 to 0.0603 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 141 | -11.9% | -92.7 to 54.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.301 | 0.265 | -12.0% | -0.174 to 0.102 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,892 | -0.0% | -7.17 to 5.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,898 | -0.0% | -4.11 to 2.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.315 | -1.1% | -0.0108 to 0.00351 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.565 | -0.5% | -0.0251 to 0.0191 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.201 | -0.5% | -0.00946 to 0.0073 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -8.98 to 0.452 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 423 | 415 | -1.9% | -16.5 to 0.106 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 708,275 | 677,582 | -4.3% | -96,721 to 35,337 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.174 | -2.3% | -0.152 to 0.143 | EVEN, no difference beyond the noise |
| host CPU-seconds | 306 | 297 | -3.0% | -307 to 289 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.23 | 0.223 | -3.0% | -0.231 to 0.217 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,719 | 5,714 | -0.1% | -42.6 to 33.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,733 | 5,728 | -0.1% | -40.7 to 31.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.413 | 0.412 | -0.2% | -0.00446 to 0.00313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.591 | 0.587 | -0.7% | -0.0298 to 0.0218 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.234 | -0.4% | -0.00326 to 0.00159 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.8 to -1.66 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.3% | -4.85 to 1.96 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,386 | 691,081 | +1.0% | -7,469 to 20,860 | shown, not judged |
| host CPU busy (share of the run) | 0.315 | 0.311 | -1.3% | -0.0156 to 0.00766 | EVEN, no difference beyond the noise |
| host CPU-seconds | 574 | 563 | -1.9% | -41 to 19.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.212 | -1.8% | -0.0148 to 0.00683 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
