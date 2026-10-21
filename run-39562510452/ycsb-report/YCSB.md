# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `418f860a4da6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -2.8 to 2.81 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% | -2.29 to 2.62 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.319 | 0.322 | +1.0% | -0.0178 to 0.0245 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.593 | 0.595 | +0.3% | -0.00883 to 0.0128 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.192 | +0.1% | -0.00611 to 0.00658 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -0.522 to 0.723 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,790 | 61,901 | +0.2% | -242 to 465 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.207 | +0.8% | -0.0243 to 0.0277 | EVEN, no difference beyond the noise |
| host CPU-seconds | 366 | 370 | +1.1% | -52.2 to 60.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.275 | 0.278 | +1.1% | -0.0395 to 0.0457 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `418f860a4da6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,860 | 2,871 | +0.4% | -56 to 78.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,871 | 2,883 | +0.4% | -54.2 to 76.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.53 | 0.533 | +0.6% | -0.0181 to 0.0248 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.713 | 0.713 | +0.0% | -0.0407 to 0.0413 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.229 | 0.228 | -0.6% | -0.0153 to 0.0126 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,490 | 1,496 | +0.4% | -31.3 to 44 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,542 | 77,602 | +0.1% | -339 to 460 | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.216 | +1.8% | -0.0522 to 0.0597 | EVEN, no difference beyond the noise |
| host CPU-seconds | 151 | 155 | +2.3% | -48.1 to 55.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.286 | 0.292 | +1.9% | -0.0861 to 0.0972 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `418f860a4da6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,937 | -0.0% | -6.07 to 4.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,938 | -0.0% | -6.19 to 4.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.0967 | 0.099 | +2.4% | -0.0102 to 0.0148 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.303 | 0.309 | +1.9% | -0.0254 to 0.0367 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0564 | 0.0576 | +2.2% | 0.000569 to 0.00188 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,351 | 1,350 | -0.1% | -1.63 to -0.604 | GAIN |
| pages read into the cache (misses) | 61,718 | 61,666 | -0.1% | -196 to 92.1 | shown, not judged |
| host CPU busy (share of the run) | 0.0625 | 0.0829 | +32.7% | -0.0106 to 0.0514 | EVEN, no difference beyond the noise |
| host CPU-seconds | 111 | 151 | +35.6% | -22 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0831 | 0.113 | +35.6% | -0.0165 to 0.0756 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `418f860a4da6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,676 | 5,668 | -0.1% | -22.1 to 7.11 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,689 | 5,682 | -0.1% | -22 to 7.73 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.42 | 0.424 | +1.1% | -0.00654 to 0.0159 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.642 | 0.652 | +1.6% | 0.00104 to 0.019 | LOSS |
| latency, mean (ms) | 0.239 | 0.242 | +1.3% | -0.00329 to 0.00933 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,360 | 1,360 | +0.0% | -0.0183 to 1.37 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,843 | 62,826 | -0.0% | -285 to 250 | shown, not judged |
| host CPU busy (share of the run) | 0.307 | 0.311 | +1.3% | -0.0187 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 556 | 563 | +1.2% | -49.9 to 62.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.213 | +1.3% | -0.0186 to 0.0239 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `418f860a4da6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.0% | -6.25 to 3.65 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,905 | -0.0% | -6.09 to 5.27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.353 | 0.359 | +1.7% | -0.0263 to 0.0383 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.618 | 0.631 | +2.0% | -0.0193 to 0.0446 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.157 | +1.2% | -0.00419 to 0.00783 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.1% | -2.71 to 4.28 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,165 | 63,031 | -0.2% | -1,098 to 830 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +1.9% | -0.0839 to 0.0912 | EVEN, no difference beyond the noise |
| host CPU-seconds | 346 | 353 | +2.2% | -188 to 203 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.265 | +2.2% | -0.141 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
