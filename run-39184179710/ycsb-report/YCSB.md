# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,890 | -0.1% | -4.71 to -1.41 | LOSS |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -4.32 to -0.963 | LOSS |
| latency, 95th percentile (ms) | 0.344 | 0.354 | +3.0% | -0.0234 to 0.0441 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.588 | 0.592 | +0.7% | -0.00496 to 0.013 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.208 | 0.209 | +0.3% | -0.00714 to 0.00822 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.71 to -1.27 | GAIN |
| bytes in the cache, mean (MB) | 419 | 416 | -0.7% | -10.7 to 5.17 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 706,284 | 751,298 | +6.4% | -47,068 to 137,097 | shown, not judged |
| host CPU busy (share of the run) | 0.18 | 0.183 | +1.4% | -0.0384 to 0.0434 | EVEN, no difference beyond the noise |
| host CPU-seconds | 307 | 311 | +1.3% | -77.9 to 86.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.234 | +1.4% | -0.0584 to 0.0646 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,879 | +0.1% | -2.09 to 5.35 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,892 | +0.1% | -3.73 to 7.47 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.512 | 0.51 | -0.4% | -0.0063 to 0.0023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.714 | 0.715 | +0.2% | -0.0104 to 0.0131 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.235 | 0.236 | +0.1% | -0.00337 to 0.00384 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 497 | -3.0% | -20.1 to -10.1 | GAIN |
| bytes in the cache, mean (MB) | 400 | 391 | -2.4% | -21 to 2.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 265,735 | 276,117 | +3.9% | -23,458 to 44,221 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.183 | +3.6% | -0.0581 to 0.0707 | EVEN, no difference beyond the noise |
| host CPU-seconds | 121 | 126 | +3.6% | -49.3 to 58.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.237 | +3.6% | -0.0932 to 0.11 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,934 | -0.1% | -7.64 to 2.74 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,936 | -0.1% | -7.83 to 2.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.203 | 0.198 | -2.5% | -0.00748 to -0.00252 | GAIN |
| latency, 99th percentile (ms) | 0.34 | 0.325 | -4.2% | -0.0374 to 0.00875 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0777 | 0.0776 | -0.2% | -0.00411 to 0.00388 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -3.52 to -0.879 | GAIN |
| bytes in the cache, mean (MB) | 421 | 420 | -0.2% | -13.5 to 11.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 720,420 | 729,810 | +1.3% | -102,388 to 121,168 | shown, not judged |
| host CPU busy (share of the run) | 0.0913 | 0.0857 | -6.1% | -0.107 to 0.0962 | EVEN, no difference beyond the noise |
| host CPU-seconds | 166 | 154 | -7.1% | -214 to 190 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.124 | 0.115 | -7.1% | -0.159 to 0.142 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,715 | 5,701 | -0.3% | -51.6 to 22.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,733 | 5,718 | -0.3% | -51.1 to 21.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.404 | 0.403 | -0.2% | -0.00939 to 0.00806 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.659 | 0.653 | -0.9% | -0.0284 to 0.0164 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.218 | -0.1% | -0.00417 to 0.00357 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.66 to -1.07 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -4.62 to 0.455 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 689,260 | 690,616 | +0.2% | -15,767 to 18,479 | shown, not judged |
| host CPU busy (share of the run) | 0.301 | 0.301 | +0.0% | -0.0372 to 0.0373 | EVEN, no difference beyond the noise |
| host CPU-seconds | 549 | 550 | +0.1% | -91.2 to 92.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.207 | +0.2% | -0.0356 to 0.0365 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,902 | 2,901 | -0.0% | -2.86 to 0.776 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,911 | -0.0% | -2.05 to 0.916 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.318 | -0.5% | -0.00926 to 0.00592 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.547 | 0.551 | +0.7% | -0.00807 to 0.0154 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.148 | 0.148 | +0.1% | -0.00698 to 0.00719 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -3.74 to -3.34 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.3% | -2.56 to -0.305 | GAIN |
| pages read into the cache (misses) | 679,332 | 687,216 | +1.2% | 1,707 to 14,061 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.194 | +2.9% | -0.0832 to 0.0943 | EVEN, no difference beyond the noise |
| host CPU-seconds | 341 | 356 | +4.4% | -182 to 213 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.268 | +4.4% | -0.137 to 0.16 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
