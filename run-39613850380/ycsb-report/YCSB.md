# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,885 | -0.1% | -3.49 to -0.401 | LOSS |
| throughput (operations a second) | 2,891 | 2,890 | -0.1% | -2.54 to -0.829 | LOSS |
| latency, 95th percentile (ms) | 0.327 | 0.33 | +0.8% | -0.0117 to 0.017 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.491 | 0.496 | +1.2% | -0.0179 to 0.0293 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.3% | -0.00409 to 0.00274 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -21 to 9.14 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 413 | -0.9% | -19.8 to 12.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 704,718 | 713,234 | +1.2% | -83,828 to 100,860 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.18 | -9.3% | -0.0715 to 0.0348 | EVEN, no difference beyond the noise |
| host CPU-seconds | 345 | 306 | -11.3% | -155 to 76.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.23 | -11.2% | -0.116 to 0.0579 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,871 | 2,872 | +0.0% | -13.2 to 14.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,883 | +0.0% | -11.5 to 12.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.529 | 0.526 | -0.6% | -0.017 to 0.0103 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.707 | 0.706 | -0.1% | -0.041 to 0.039 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.232 | 0.232 | +0.4% | -0.00768 to 0.00959 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 494 | -3.5% | -58.5 to 22.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 390 | -2.6% | -47.1 to 26.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,847 | 273,168 | +2.4% | -6,645 to 19,287 | shown, not judged |
| host CPU busy (share of the run) | 0.204 | 0.208 | +1.8% | -0.126 to 0.133 | EVEN, no difference beyond the noise |
| host CPU-seconds | 143 | 147 | +2.7% | -112 to 119 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.27 | 0.277 | +2.6% | -0.21 to 0.224 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,944 | 2,940 | -0.1% | -9.05 to 2.32 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,945 | 2,942 | -0.1% | -8.97 to 2.36 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0863 | 0.091 | +5.4% | -0.00784 to 0.0172 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.285 | 0.291 | +2.1% | -0.0245 to 0.0365 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0546 | 0.0565 | +3.5% | -0.00249 to 0.00629 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -9.42 to 1.73 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 418 | -0.8% | -13.8 to 7.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 711,520 | 680,249 | -4.4% | -166,917 to 104,376 | shown, not judged |
| host CPU busy (share of the run) | 0.0641 | 0.0839 | +30.8% | -0.0633 to 0.103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 116 | 153 | +32.4% | -125 to 200 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0864 | 0.114 | +32.4% | -0.0928 to 0.149 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,681 | 5,676 | -0.1% | -7.41 to -3.58 | LOSS |
| throughput (operations a second) | 5,698 | 5,693 | -0.1% | -5.29 to -4.36 | LOSS |
| latency, 95th percentile (ms) | 0.424 | 0.43 | +1.3% | -0.0118 to 0.0231 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.646 | 0.656 | +1.5% | -0.0335 to 0.0535 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.243 | 0.246 | +1.2% | -0.00331 to 0.00901 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.79 to -1.46 | GAIN |
| bytes in the cache, mean (MB) | 417 | 414 | -0.5% | -5.46 to 0.964 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 685,823 | 690,012 | +0.6% | -23,883 to 32,263 | shown, not judged |
| host CPU busy (share of the run) | 0.326 | 0.33 | +1.1% | -0.0181 to 0.0256 | EVEN, no difference beyond the noise |
| host CPU-seconds | 593 | 599 | +1.1% | -45 to 57.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.224 | 0.226 | +1.1% | -0.017 to 0.0217 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,878 | +0.0% | -7.56 to 7.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | +0.0% | -6.1 to 6.84 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.35 | 0.348 | -0.7% | -0.0198 to 0.0151 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.536 | 0.539 | +0.6% | -0.0207 to 0.0267 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.216 | 0.214 | -0.9% | -0.00849 to 0.00478 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -1.9% | -24.9 to 5.22 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 411 | -1.5% | -16.3 to 3.37 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,346 | 689,251 | +1.8% | -6,197 to 30,007 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.236 | -6.0% | -0.03 to 5.85e-08 | EVEN, no difference beyond the noise |
| host CPU-seconds | 441 | 407 | -7.9% | -64.4 to -5.13 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.332 | 0.306 | -7.9% | -0.0493 to -0.00334 | GAIN |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
