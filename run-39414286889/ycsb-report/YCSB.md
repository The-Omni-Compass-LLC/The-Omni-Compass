# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,910 | +0.0% | -2.33 to 3.36 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,913 | 2,914 | +0.0% | -2.33 to 3.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.286 | 0.293 | +2.3% | -0.0142 to 0.0275 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.495 | 0.494 | -0.2% | -0.00348 to 0.00148 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.118 | 0.119 | +0.3% | -0.0015 to 0.00214 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,364 | 1,365 | +0.0% | -0.387 to 1.56 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,778 | 61,846 | +0.1% | -202 to 337 | shown, not judged |
| host CPU busy (share of the run) | 0.16 | 0.14 | -12.7% | -0.0407 to 6.29e-05 | EVEN, no difference beyond the noise |
| host CPU-seconds | 297 | 253 | -14.8% | -89.1 to 1.43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.223 | 0.19 | -14.8% | -0.0668 to 0.00103 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -9.24 to 9.75 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,894 | +0.0% | -6.52 to 7.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.511 | 0.51 | -0.3% | -0.0042 to 0.00154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.675 | 0.675 | +0.0% | -0.0179 to 0.0179 | EVEN, the same |
| latency, mean (ms) | 0.227 | 0.228 | +0.2% | -0.00286 to 0.00381 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,503 | 1,503 | -0.0% | -2.29 to 1.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,668 | 77,673 | +0.0% | -269 to 279 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.185 | +3.1% | -0.138 to 0.149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 124 | 128 | +3.5% | -116 to 124 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.233 | 0.241 | +3.5% | -0.218 to 0.234 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,890 | +0.1% | -12.2 to 19.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,896 | +0.1% | -12.9 to 20 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.349 | +0.2% | -0.00937 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.551 | 0.543 | -1.4% | -0.0202 to 0.00484 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.214 | 0.214 | -0.3% | -0.00261 to 0.00145 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,363 | +0.1% | -1.17 to 4.01 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,013 | 62,976 | -0.1% | -787 to 712 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.184 | -12.5% | -0.069 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 361 | 306 | -15.3% | -147 to 36.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.272 | 0.23 | -15.4% | -0.111 to 0.0278 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
