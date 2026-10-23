# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,904 | -0.1% | -6.48 to 1.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,907 | -0.1% | -6.4 to 1.81 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.293 | 0.296 | +1.3% | -0.00432 to 0.0117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.464 | 0.463 | -0.2% | -0.0184 to 0.0164 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.156 | 0.158 | +0.8% | -0.000704 to 0.00326 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -15.9 to 6.51 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -11.8 to 6.97 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 730,752 | 709,670 | -2.9% | -95,074 to 52,910 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.176 | -0.9% | -0.0255 to 0.0223 | EVEN, no difference beyond the noise |
| host CPU-seconds | 322 | 318 | -1.4% | -56.9 to 47.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.238 | -1.4% | -0.0425 to 0.0357 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,883 | -0.5% | -51.9 to 22.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,897 | -0.5% | -53.9 to 26.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.329 | +1.6% | -0.0147 to 0.0254 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.526 | 0.53 | +0.8% | -0.0768 to 0.0855 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.177 | 0.187 | +5.6% | -0.00308 to 0.0228 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -22.3 to -0.651 | GAIN |
| bytes in the cache, mean (MB) | 400 | 393 | -1.7% | -23.1 to 9.49 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,214 | 266,972 | +1.4% | -1,700 to 9,217 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.147 | +1.8% | -0.0916 to 0.0969 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 104 | +1.1% | -76.8 to 79.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.193 | 0.197 | +1.6% | -0.146 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,941 | -0.1% | -4.28 to 0.822 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,945 | 2,943 | -0.1% | -4.32 to 0.768 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.083 | 0.0827 | -0.4% | -0.00413 to 0.00346 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.267 | 0.265 | -0.9% | -0.0075 to 0.00284 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0547 | 0.0545 | -0.4% | -0.00207 to 0.00162 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.93 to -1.08 | GAIN |
| bytes in the cache, mean (MB) | 425 | 419 | -1.3% | -15.5 to 4.47 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 727,262 | 707,392 | -2.7% | -74,798 to 35,057 | shown, not judged |
| host CPU busy (share of the run) | 0.0633 | 0.0776 | +22.6% | -0.0177 to 0.0463 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 141 | +24.5% | -35.4 to 90.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0846 | 0.105 | +24.5% | -0.0263 to 0.0677 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,683 | 5,681 | -0.0% | -21.4 to 18.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,702 | 5,700 | -0.0% | -22.3 to 19.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.427 | 0.427 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.685 | 0.685 | +0.0% | -0.0155 to 0.0155 | EVEN, the same |
| latency, mean (ms) | 0.242 | 0.242 | -0.1% | -0.0013 to 0.0008 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -20.4 to 6.6 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 412 | -1.1% | -16.3 to 7.25 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 682,239 | 685,989 | +0.5% | -9,244 to 16,743 | shown, not judged |
| host CPU busy (share of the run) | 0.319 | 0.318 | -0.3% | -0.0104 to 0.00876 | EVEN, no difference beyond the noise |
| host CPU-seconds | 576 | 574 | -0.3% | -27.4 to 23.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.217 | 0.216 | -0.4% | -0.0108 to 0.00917 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,933 | -0.0% | -1.74 to 1.57 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,938 | -0.0% | -1.53 to 1.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.148 | 0.151 | +2.3% | -0.011 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.366 | 0.37 | +1.2% | -0.0242 to 0.0329 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0805 | 0.0806 | +0.2% | -0.000381 to 0.00073 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -7.97 to -2.04 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.5% | -6.86 to 2.71 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,237 | 691,698 | +1.2% | 3,107 to 13,816 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.124 | +14.2% | -0.0773 to 0.108 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 226 | +16.8% | -160 to 225 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.145 | 0.169 | +16.7% | -0.119 to 0.168 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
