# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,880 | -0.1% | -6.67 to 0.663 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,887 | -0.1% | -5.4 to 0.293 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.346 | +2.6% | -0.0355 to 0.0529 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.587 | 0.589 | +0.2% | -0.018 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.201 | +0.2% | -0.0156 to 0.0164 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -16.5 to 4.78 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 414 | -0.4% | -13.5 to 10.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 728,939 | 739,337 | +1.4% | -120,862 to 141,659 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.214 | +1.1% | -0.0403 to 0.0451 | EVEN, no difference beyond the noise |
| host CPU-seconds | 374 | 378 | +1.2% | -92.7 to 102 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.285 | +1.3% | -0.0694 to 0.0766 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,919 | 2,918 | -0.0% | -2.72 to 0.12 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,923 | 2,922 | -0.0% | -2.77 to 0.435 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.302 | 0.314 | +3.9% | -0.0174 to 0.0408 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.49 | 0.497 | +1.5% | -0.0366 to 0.0512 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.117 | 0.119 | +1.9% | -0.000499 to 0.00503 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -17.8 to -4.88 | GAIN |
| bytes in the cache, mean (MB) | 406 | 398 | -2.1% | -26.8 to 10 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 265,633 | 265,193 | -0.2% | -53,029 to 52,149 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.117 | +5.4% | -0.0106 to 0.0226 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.4 | 83.9 | +5.7% | -8.39 to 17.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.149 | 0.157 | +5.7% | -0.0156 to 0.0326 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,911 | 2,908 | -0.1% | -5.73 to -1.44 | LOSS |
| throughput (operations a second) | 2,915 | 2,912 | -0.1% | -6.16 to 0.109 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.189 | 0.189 | -0.4% | -0.00584 to 0.0045 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.36 | 0.365 | +1.4% | -0.0261 to 0.0361 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.142 | 0.147 | +3.6% | -0.00336 to 0.0135 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.3% | -15.8 to 3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 412 | -1.5% | -11.7 to -0.84 | GAIN |
| pages read into the cache (misses) | 716,767 | 668,430 | -6.7% | -134,942 to 38,268 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.153 | -0.7% | -0.0344 to 0.0324 | EVEN, no difference beyond the noise |
| host CPU-seconds | 278 | 277 | -0.5% | -71.8 to 69.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.208 | -0.4% | -0.0537 to 0.0518 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,745 | 5,739 | -0.1% | -20.7 to 9.55 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,764 | 5,757 | -0.1% | -23.8 to 11.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.355 | 0.353 | -0.5% | -0.0111 to 0.00774 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.635 | 0.63 | -0.8% | -0.0312 to 0.0212 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.17 | 0.168 | -1.0% | -0.00596 to 0.00248 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -7.26 to -1.87 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.6% | -6.98 to 1.65 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 689,036 | 691,948 | +0.4% | -18,861 to 24,686 | shown, not judged |
| host CPU busy (share of the run) | 0.252 | 0.239 | -5.3% | -0.0719 to 0.0454 | EVEN, no difference beyond the noise |
| host CPU-seconds | 467 | 435 | -6.8% | -171 to 108 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.164 | -6.8% | -0.0642 to 0.0403 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,902 | 2,900 | -0.1% | -5.69 to 1.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.0% | -7.13 to 5.42 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.223 | 0.23 | +3.1% | -0.00383 to 0.0178 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.459 | 0.476 | +3.7% | -0.0159 to 0.0499 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.17 | 0.17 | +0.1% | -0.017 to 0.0173 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -17 to 4.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 414 | -0.5% | -12.7 to 8.67 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 676,110 | 683,556 | +1.1% | -4,323 to 19,216 | shown, not judged |
| host CPU busy (share of the run) | 0.216 | 0.205 | -5.2% | -0.0148 to -0.0076 | GAIN |
| host CPU-seconds | 398 | 371 | -7.0% | -40.4 to -15.3 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.299 | 0.278 | -7.0% | -0.03 to -0.0116 | GAIN |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
