# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,886 | -0.1% | -5.06 to -0.258 | LOSS |
| throughput (operations a second) | 2,895 | 2,893 | -0.1% | -4.01 to -0.439 | LOSS |
| latency, 95th percentile (ms) | 0.378 | 0.38 | +0.6% | -0.0136 to 0.0183 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.572 | 0.575 | +0.6% | -0.0563 to 0.063 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.213 | 0.215 | +0.9% | -0.00539 to 0.00908 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 487 | -4.9% | -103 to 52.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 399 | -4.6% | -77 to 38.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 722,947 | 741,624 | +2.6% | -126,563 to 163,917 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.189 | -6.2% | -0.0877 to 0.0629 | EVEN, no difference beyond the noise |
| host CPU-seconds | 348 | 320 | -8.1% | -188 to 132 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.241 | -8.1% | -0.142 to 0.0994 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | -0.535 to 5.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | +0.0% | -7.4 to 7.65 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,895 | 2,895 | -0.0% | -4.1 to 2.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.44 | +0.6% | -0.0246 to 0.0299 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.637 | 0.63 | -1.1% | -0.115 to 0.101 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.225 | +1.3% | -0.00158 to 0.00721 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 480 | -6.3% | -84.3 to 20 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 398 | 379 | -4.7% | -75.7 to 38.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,183 | 290,018 | +9.0% | -38,111 to 85,781 | shown, not judged |
| host CPU busy (share of the run) | 0.157 | 0.206 | +31.3% | -0.0126 to 0.111 | EVEN, no difference beyond the noise |
| host CPU-seconds | 104 | 144 | +37.7% | -8.43 to 87.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.196 | 0.27 | +37.7% | -0.0157 to 0.164 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,892 | -0.0% | -5.69 to 3.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,897 | 2,896 | -0.0% | -5.27 to 3.05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.323 | +1.1% | -0.0138 to 0.0211 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.503 | 0.506 | +0.6% | -0.0191 to 0.0251 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.203 | +0.3% | -0.00276 to 0.00413 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.74 to 0.714 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 422 | 419 | -0.5% | -12.5 to 8.22 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 661,866 | 725,456 | +9.6% | 24,210 to 102,969 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.19 | -2.8% | -0.0374 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 327 | -3.4% | -79.3 to 56.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.246 | -3.4% | -0.0595 to 0.0422 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,701 | 5,699 | -0.0% | -50.3 to 46.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,717 | 5,715 | -0.0% | -51.1 to 47 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.435 | 0.435 | +0.0% | -0.0203 to 0.0203 | EVEN, the same |
| latency, 99th percentile (ms) | 0.629 | 0.629 | +0.0% | -0.0138 to 0.0138 | EVEN, the same |
| latency, mean (ms) | 0.253 | 0.254 | +0.2% | -0.0113 to 0.0122 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.7 to -1.77 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.7% | -4.25 to -1.8 | GAIN |
| pages read into the cache (misses) | 675,579 | 684,015 | +1.2% | -1,985 to 18,857 | shown, not judged |
| host CPU busy (share of the run) | 0.285 | 0.286 | +0.1% | -0.0231 to 0.0234 | EVEN, no difference beyond the noise |
| host CPU-seconds | 484 | 485 | +0.2% | -50 to 52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.183 | 0.183 | +0.1% | -0.0205 to 0.021 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,924 | 2,924 | +0.0% | -0.122 to 0.915 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,932 | 2,931 | -0.0% | -8.81 to 6.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.253 | 0.236 | -6.7% | -0.0536 to 0.0196 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.475 | 0.421 | -11.4% | -0.234 to 0.126 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.114 | 0.109 | -5.0% | -0.0225 to 0.0111 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -6.05 to -2.74 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.4% | -3.94 to 0.701 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,674 | 696,351 | +1.3% | -5,542 to 22,897 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.137 | +9.7% | -0.0895 to 0.114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 249 | +12.5% | -179 to 234 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.165 | 0.186 | +12.5% | -0.134 to 0.175 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
