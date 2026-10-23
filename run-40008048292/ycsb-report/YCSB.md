# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,873 | -1.3% | -193 to 120 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,879 | -1.2% | -189 to 118 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.199 | 0.204 | +2.5% | -0.00815 to 0.0181 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.379 | 0.389 | +2.7% | -0.0131 to 0.0338 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.145 | 0.153 | +5.9% | -0.0267 to 0.0437 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,361 | -0.4% | -20 to 9.92 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,806 | 61,852 | +0.1% | -292 to 385 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.153 | +7.8% | -0.0344 to 0.0564 | EVEN, no difference beyond the noise |
| host CPU-seconds | 253 | 277 | +9.4% | -71.4 to 119 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.189 | 0.21 | +10.7% | -0.0495 to 0.09 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,878 | -0.0% | -5.84 to 3.53 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% | -4.25 to 2.44 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.43 | +1.3% | -0.0347 to 0.0461 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.582 | 0.597 | +2.5% | -0.045 to 0.0743 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.214 | +1.0% | -0.0163 to 0.0204 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,511 | -0.1% | -3.97 to 2.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,615 | 77,649 | +0.0% | -80.4 to 149 | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.215 | -0.2% | -0.0543 to 0.0534 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 153 | -0.8% | -51.8 to 49.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.288 | -0.8% | -0.0971 to 0.0924 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,940 | -0.1% | -5.4 to -0.332 | LOSS |
| throughput (operations a second) | 2,945 | 2,942 | -0.1% | -2.48 to -2 | LOSS |
| latency, 95th percentile (ms) | 0.075 | 0.0873 | +16.4% | -0.0214 to 0.0461 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.258 | 0.278 | +7.7% | -0.0522 to 0.0922 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0497 | 0.0535 | +7.7% | -0.00607 to 0.0138 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | +0.0% | -1.26 to 1.48 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,661 | 61,666 | +0.0% | -203 to 214 | shown, not judged |
| host CPU busy (share of the run) | 0.079 | 0.0673 | -14.9% | -0.0603 to 0.0368 | EVEN, no difference beyond the noise |
| host CPU-seconds | 145 | 121 | -16.7% | -119 to 70.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.108 | 0.0904 | -16.6% | -0.0889 to 0.0528 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,725 | 5,729 | +0.1% | -9.34 to 16.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,740 | 5,742 | +0.0% | -14.5 to 18.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.372 | 0.37 | -0.5% | -0.0232 to 0.0192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.645 | 0.637 | -1.3% | -0.0467 to 0.0294 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | -0.2% | -0.00969 to 0.00909 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,483 | 7,483 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% | -8.21 to 7.34 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,970 | 62,955 | -0.0% | -1,348 to 1,319 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.248 | -2.4% | -0.0113 to -0.000952 | GAIN |
| host CPU-seconds | 467 | 452 | -3.3% | -28.5 to -2.44 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.17 | -3.4% | -0.011 to -0.000842 | GAIN |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | -0.0% | -2.92 to 2.44 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,909 | +0.0% | -3.1 to 3.27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.318 | +0.5% | -0.00774 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.541 | 0.537 | -0.7% | -0.0182 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.143 | 0.142 | -0.7% | -0.0018 to -0.000171 | GAIN |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,363 | +0.0% | -3.55 to 4.86 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,122 | 63,014 | -0.2% | -838 to 622 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.172 | -1.8% | -0.0168 to 0.0106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 316 | 310 | -2.0% | -35.1 to 22.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.233 | -1.9% | -0.0264 to 0.0171 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
