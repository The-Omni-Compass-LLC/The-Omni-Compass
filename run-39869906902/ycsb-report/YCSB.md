# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,883 | -0.1% | -2.57 to -1.26 | LOSS |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -2.29 to -1.33 | LOSS |
| latency, 95th percentile (ms) | 0.338 | 0.34 | +0.6% | -0.000484 to 0.00448 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.526 | 0.525 | -0.2% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.199 | 0.2 | +0.2% | -0.00353 to 0.00426 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -15.2 to 3.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 416 | -0.5% | -7.94 to 4.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 698,860 | 717,724 | +2.7% | -110,863 to 148,590 | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.203 | -6.8% | -0.0653 to 0.0359 | EVEN, no difference beyond the noise |
| host CPU-seconds | 386 | 353 | -8.5% | -149 to 83.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.266 | -8.5% | -0.112 to 0.0624 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,937 | -0.1% | -5.9 to 1.34 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,940 | -0.1% | -5.59 to 1.32 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.24 | 0.246 | +2.4% | -0.0103 to 0.0216 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.396 | 0.41 | +3.5% | -0.0102 to 0.0375 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0759 | 0.0773 | +1.9% | -0.00477 to 0.0077 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -9.61 to -7.87 | GAIN |
| bytes in the cache, mean (MB) | 407 | 396 | -2.6% | -22.8 to 1.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,150 | 268,127 | +2.3% | -27,909 to 39,864 | shown, not judged |
| host CPU busy (share of the run) | 0.0935 | 0.0856 | -8.5% | -0.134 to 0.118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 68.7 | 62.3 | -9.2% | -106 to 93.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.128 | 0.116 | -9.2% | -0.197 to 0.174 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,902 | -0.0% | -6.14 to 3.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,907 | -0.0% | -6.03 to 3.96 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.301 | 0.301 | -0.1% | -0.014 to 0.0133 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.484 | 0.484 | +0.1% | -0.0478 to 0.0491 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.154 | +0.1% | -0.00294 to 0.00331 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.92 to -0.677 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.3% | -13.5 to 10.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,062 | 696,672 | +0.2% | -86,856 to 90,076 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.176 | +5.9% | -0.036 to 0.0557 | EVEN, no difference beyond the noise |
| host CPU-seconds | 301 | 322 | +7.0% | -77.2 to 119 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.242 | +7.0% | -0.0577 to 0.0892 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,757 | 5,747 | -0.2% | -21.7 to 0.923 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,772 | 5,764 | -0.1% | -16.8 to -0.0361 | LOSS |
| latency, 95th percentile (ms) | 0.321 | 0.321 | +0.2% | -0.00313 to 0.00446 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.473 | 0.488 | +3.2% | -0.024 to 0.054 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.183 | 0.185 | +0.9% | -0.00218 to 0.00548 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.5% | -20.4 to 4.63 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 413 | -1.1% | -12.7 to 3.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,488 | 693,772 | +0.9% | -11,719 to 24,287 | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.251 | +3.7% | -0.0329 to 0.0507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 435 | 457 | +5.1% | -80 to 124 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.172 | +5.2% | -0.0301 to 0.0469 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,873 | 2,875 | +0.1% | -23.8 to 27.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,884 | 2,885 | +0.1% | -23.5 to 27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.366 | 0.364 | -0.5% | -0.00857 to 0.00457 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.581 | 0.574 | -1.1% | -0.0287 to 0.0161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.217 | -0.8% | -0.00718 to 0.00388 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -7.67 to -0.292 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.3% | -3.8 to 1.09 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,907 | 683,763 | +1.3% | -13,323 to 31,035 | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.247 | +2.8% | -0.0606 to 0.074 | EVEN, no difference beyond the noise |
| host CPU-seconds | 416 | 433 | +4.0% | -138 to 171 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.314 | 0.326 | +3.9% | -0.102 to 0.126 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
