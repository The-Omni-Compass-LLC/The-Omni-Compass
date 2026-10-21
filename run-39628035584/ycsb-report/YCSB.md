# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,907 | 2,906 | -0.1% | -6.14 to 2.65 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,910 | -0.1% | -5.2 to 1.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.295 | 0.301 | +2.0% | -0.00261 to 0.0146 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.506 | +0.9% | -0.0105 to 0.0198 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.129 | 0.129 | +0.1% | -0.0031 to 0.00345 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.12 to -2.03 | GAIN |
| bytes in the cache, mean (MB) | 416 | 417 | +0.2% | -3.5 to 5.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,664 | 714,644 | +2.0% | -33,187 to 61,147 | shown, not judged |
| host CPU busy (share of the run) | 0.148 | 0.145 | -1.5% | -0.057 to 0.0525 | EVEN, no difference beyond the noise |
| host CPU-seconds | 266 | 262 | -1.8% | -122 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.196 | -1.8% | -0.0913 to 0.0841 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -9.57 to 9.24 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,909 | 2,909 | +0.0% | -3.21 to 3.34 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.321 | +1.2% | -0.039 to 0.0463 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.504 | 0.505 | +0.2% | -0.128 to 0.13 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.177 | -2.5% | -0.0284 to 0.0191 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -10.3 to 0.549 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 400 | +0.2% | -3.25 to 4.59 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 266,591 | 274,502 | +3.0% | -21,557 to 37,380 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.161 | -8.0% | -0.0732 to 0.0452 | EVEN, no difference beyond the noise |
| host CPU-seconds | 128 | 116 | -9.6% | -62.7 to 38.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.241 | 0.218 | -9.7% | -0.118 to 0.0713 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,910 | -0.1% | -15.7 to 12.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,913 | -0.1% | -14.8 to 11.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.185 | 0.184 | -0.9% | -0.00546 to 0.00213 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.352 | 0.349 | -0.9% | -0.0375 to 0.0315 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.133 | 0.132 | -0.4% | -0.00495 to 0.00391 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.5% | -3.07 to -1.67 | GAIN |
| bytes in the cache, mean (MB) | 421 | 420 | -0.2% | -3.75 to 2.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 715,445 | 725,210 | +1.4% | -75,066 to 94,598 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.155 | +5.8% | -0.0468 to 0.0638 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 281 | +6.8% | -101 to 137 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.197 | 0.21 | +6.8% | -0.0762 to 0.103 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,680 | 5,674 | -0.1% | -10.6 to 0.0558 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,696 | 5,692 | -0.1% | -15.4 to 6.53 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.43 | 0.432 | +0.5% | -0.0152 to 0.0192 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.647 | 0.655 | +1.2% | -0.0493 to 0.0653 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.247 | +0.3% | -0.00814 to 0.00971 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.1% | -18.3 to 7.36 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 413 | -1.0% | -13 to 4.83 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,862 | 690,035 | +1.6% | -14,739 to 37,084 | shown, not judged |
| host CPU busy (share of the run) | 0.325 | 0.325 | -0.0% | -0.00617 to 0.00611 | EVEN, no difference beyond the noise |
| host CPU-seconds | 586 | 586 | -0.1% | -8.83 to 8.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.221 | -0.0% | -0.00295 to 0.0028 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,881 | -0.1% | -8.86 to 4.34 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,890 | -0.1% | -7.43 to 3.15 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.346 | 0.348 | +0.7% | -0.00707 to 0.0117 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.533 | 0.538 | +0.9% | -0.0248 to 0.0348 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.213 | +0.2% | -0.0101 to 0.0111 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.75 to -1.76 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.3% | -4.2 to 1.51 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,368 | 684,554 | +1.5% | -18,371 to 38,742 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.247 | +5.7% | -0.0865 to 0.113 | EVEN, no difference beyond the noise |
| host CPU-seconds | 403 | 435 | +7.7% | -194 to 256 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.303 | 0.327 | +7.7% | -0.147 to 0.193 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
