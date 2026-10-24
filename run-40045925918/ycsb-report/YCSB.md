# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,888 | -0.1% | -3.19 to -0.0189 | LOSS |
| throughput (operations a second) | 2,893 | 2,891 | -0.1% | -3.74 to 0.324 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.311 | 0.315 | +1.3% | -0.00496 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.469 | 0.47 | +0.1% | -0.0118 to 0.0132 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | +0.4% | -7.51e-05 to 0.00151 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.44 to -0.85 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -7.52 to 5.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,218 | 697,457 | +0.3% | -81,534 to 86,012 | shown, not judged |
| host CPU busy (share of the run) | 0.191 | 0.211 | +10.9% | -0.0163 to 0.0579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 332 | 376 | +13.2% | -35.8 to 124 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.249 | 0.282 | +13.2% | -0.027 to 0.0931 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% | -3.42 to -0.402 | LOSS |
| throughput (operations a second) | 2,892 | 2,890 | -0.1% | -3.27 to -0.972 | LOSS |
| latency, 95th percentile (ms) | 0.4 | 0.401 | +0.1% | -0.00346 to 0.00413 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.539 | 0.535 | -0.7% | -0.0277 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.21 | +0.7% | -0.00144 to 0.00441 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.4% | -68.4 to 23 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 408 | 388 | -4.9% | -59 to 18.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,236 | 269,150 | +1.1% | -17,582 to 23,412 | shown, not judged |
| host CPU busy (share of the run) | 0.195 | 0.209 | +7.3% | -0.0935 to 0.122 | EVEN, no difference beyond the noise |
| host CPU-seconds | 136 | 148 | +9.1% | -81.7 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.279 | +9.1% | -0.153 to 0.2 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,882 | -0.2% | -8.95 to 0.104 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,887 | -0.1% | -8.22 to -0.0629 | LOSS |
| latency, 95th percentile (ms) | 0.31 | 0.316 | +2.0% | 0.00116 to 0.0115 | LOSS |
| latency, 99th percentile (ms) | 0.508 | 0.515 | +1.3% | -0.0192 to 0.0325 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.196 | +2.1% | -0.000185 to 0.00814 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.2% | -107 to 63.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 406 | -3.1% | -79.2 to 53.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,407 | 747,594 | +7.0% | -134,891 to 233,265 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.194 | -4.4% | -0.0274 to 0.00976 | EVEN, no difference beyond the noise |
| host CPU-seconds | 360 | 338 | -6.0% | -66.1 to 23.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.254 | -5.9% | -0.0494 to 0.0173 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,686 | 5,674 | -0.2% | -44 to 20.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,703 | 5,691 | -0.2% | -43.9 to 20.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.429 | 0.428 | -0.4% | -0.00792 to 0.00459 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.641 | 0.638 | -0.4% | -0.0192 to 0.0139 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.246 | -0.6% | -0.00245 to -0.000646 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -6.06 to -1.27 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.4% | -4.77 to 1.67 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 685,858 | 684,401 | -0.2% | -19,787 to 16,873 | shown, not judged |
| host CPU busy (share of the run) | 0.33 | 0.325 | -1.6% | -0.0409 to 0.0303 | EVEN, no difference beyond the noise |
| host CPU-seconds | 598 | 585 | -2.2% | -101 to 74.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.221 | -2.1% | -0.0371 to 0.0277 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,902 | -0.1% | -7.66 to 3.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,911 | -0.1% | -5.37 to 1.25 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.22 | 0.223 | +1.2% | -0.011 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.422 | 0.425 | +0.8% | -0.0411 to 0.0478 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.166 | 0.167 | +0.8% | -0.0035 to 0.00605 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -7.02 to -1.35 | GAIN |
| bytes in the cache, mean (MB) | 418 | 416 | -0.5% | -3.38 to -0.844 | GAIN |
| pages read into the cache (misses) | 675,963 | 684,895 | +1.3% | -14,214 to 32,077 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.182 | -2.8% | -0.0519 to 0.0414 | EVEN, no difference beyond the noise |
| host CPU-seconds | 334 | 321 | -3.9% | -115 to 89.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.25 | 0.241 | -3.8% | -0.0867 to 0.0676 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
