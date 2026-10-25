# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,878 | -0.1% | -9.44 to 3.85 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,886 | -0.1% | -8.82 to 2.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.347 | 0.36 | +3.7% | -0.0415 to 0.0675 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.626 | 0.625 | -0.1% | -0.0168 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.202 | +1.1% | -0.00637 to 0.0108 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -4.94 to -0.244 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.2% | -3.64 to 2.26 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 720,790 | 713,789 | -1.0% | -49,108 to 35,107 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.192 | -3.7% | -0.0965 to 0.0819 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 330 | -5.8% | -217 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.249 | -5.8% | -0.164 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,806 | -3.0% | -293 to 121 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,821 | -2.9% | -288 to 121 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.316 | +3.7% | -0.03 to 0.0527 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.528 | +5.9% | -0.0773 to 0.137 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.186 | 0.202 | +8.8% | -0.0151 to 0.0478 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 498 | -2.7% | -23.4 to -3.88 | GAIN |
| bytes in the cache, mean (MB) | 397 | 392 | -1.4% | -31.9 to 20.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,941 | 268,202 | +1.2% | -15,323 to 21,845 | shown, not judged |
| host CPU busy (share of the run) | 0.163 | 0.169 | +3.8% | -0.103 to 0.116 | EVEN, no difference beyond the noise |
| host CPU-seconds | 119 | 125 | +5.3% | -90.3 to 103 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.242 | +8.8% | -0.18 to 0.219 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,907 | -0.1% | -10.3 to 5.85 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,911 | -0.1% | -7.86 to 3.54 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.192 | 0.195 | +1.7% | -0.011 to 0.0177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.365 | 0.367 | +0.7% | -0.0212 to 0.0265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.139 | 0.139 | -0.3% | -0.0169 to 0.016 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -9.58 to 0.645 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 417 | -0.2% | -12.4 to 10.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 714,578 | 670,590 | -6.2% | -119,660 to 31,685 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.18 | +16.8% | -0.0919 to 0.144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 279 | 335 | +20.1% | -202 to 314 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.209 | 0.251 | +20.1% | -0.152 to 0.235 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,838 | 5,833 | -0.1% | -10.6 to 1.41 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,847 | 5,842 | -0.1% | -10.5 to 0.358 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.169 | 0.167 | -1.2% | -0.0244 to 0.0204 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.398 | 0.383 | -3.7% | -0.06 to 0.0306 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0864 | 0.0857 | -0.9% | -0.00398 to 0.00251 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -19.1 to 3.63 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 414 | -1.4% | -15.1 to 3.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,666 | 704,012 | +1.1% | -24,756 to 39,447 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.131 | -2.3% | -0.0804 to 0.0743 | EVEN, no difference beyond the noise |
| host CPU-seconds | 245 | 238 | -2.9% | -171 to 157 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0914 | 0.0888 | -2.9% | -0.0639 to 0.0587 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,897 | +0.1% | -6.08 to 9.04 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,903 | 2,904 | +0.1% | -5.78 to 8.97 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.317 | -1.1% | -0.0149 to 0.00754 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.509 | 0.504 | -1.0% | -0.0116 to 0.000919 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.175 | 0.175 | +0.0% | -0.00331 to 0.00346 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.44 to -1.67 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -3.18 to -2.16 | GAIN |
| pages read into the cache (misses) | 674,097 | 687,328 | +2.0% | -5,512 to 31,975 | shown, not judged |
| host CPU busy (share of the run) | 0.218 | 0.229 | +4.9% | -0.0613 to 0.0828 | EVEN, no difference beyond the noise |
| host CPU-seconds | 396 | 422 | +6.6% | -147 to 199 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.298 | 0.317 | +6.5% | -0.111 to 0.15 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
