# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,886 | -0.0% | -2.14 to 1.89 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | +0.0% | -1.11 to 1.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.326 | 0.325 | -0.4% | -0.0101 to 0.00739 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.496 | 0.499 | +0.6% | -0.00357 to 0.00957 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.5% | -0.00353 to 0.00152 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -2.16 to -1.35 | GAIN |
| bytes in the cache, mean (MB) | 418 | 419 | +0.3% | -4.42 to 6.83 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 710,378 | 705,496 | -0.7% | -66,840 to 57,076 | shown, not judged |
| host CPU busy (share of the run) | 0.207 | 0.189 | -8.4% | -0.0635 to 0.0289 | EVEN, no difference beyond the noise |
| host CPU-seconds | 364 | 327 | -10.2% | -139 to 65 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.273 | 0.245 | -10.2% | -0.104 to 0.0488 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | -2.4 to 9.07 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 201 | 199 | -0.8% | -4.34 to 1.27 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 198 | 196 | -1.0% | -4.87 to 0.722 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.55 | 3.09 | +21.2% | 0.494 to 0.587 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 364 | 327 | -10.2% | -139 to 65 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,884 | +0.0% | -1.77 to 3.25 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,890 | +0.0% | -1.82 to 3.59 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.422 | +0.0% | -0.0138 to 0.0138 | EVEN, the same |
| latency, 99th percentile (ms) | 0.565 | 0.566 | +0.2% | -0.0176 to 0.0203 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.212 | -0.2% | -0.00534 to 0.00446 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 525 | +2.5% | -19.9 to 45.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 414 | +3.2% | -26.8 to 52.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 267,079 | 267,174 | +0.0% | -15,690 to 15,880 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.165 | -17.0% | -0.113 to 0.0457 | EVEN, no difference beyond the noise |
| host CPU-seconds | 139 | 112 | -19.6% | -94 to 39.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.262 | 0.211 | -19.6% | -0.177 to 0.0737 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80 | 80.5 | +0.6% | -1.62 to 2.64 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79 | 79.4 | +0.4% | -1.82 to 2.46 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.993 | 1.18 | +19.1% | 0.152 to 0.227 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 139 | 112 | -19.6% | -93.9 to 39.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,883 | -0.0% | -5.2 to 5.07 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,887 | -0.0% | -4.87 to 4.83 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.32 | -0.5% | -0.0158 to 0.0125 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.49 | 0.488 | -0.4% | -0.0208 to 0.0168 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.193 | -1.7% | -0.0126 to 0.00575 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -12.3 to 2.93 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 416 | -0.7% | -19.2 to 13.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 702,902 | 676,488 | -3.8% | -77,958 to 25,130 | shown, not judged |
| host CPU busy (share of the run) | 0.209 | 0.191 | -8.6% | -0.0257 to -0.0103 | GAIN |
| host CPU-seconds | 371 | 332 | -10.5% | -57.9 to -19.8 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.249 | -10.5% | -0.0433 to -0.0151 | GAIN |
| cache size changes written (the knob's moves) | 0 | 6.33 |  | -3.71 to 16.4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 195 | 190 | -2.3% | -15.6 to 6.52 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 192 | 187 | -2.7% | -16.2 to 5.79 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.67 | 3.29 | +23.5% | 0.296 to 0.959 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 371 | 332 | -10.5% | -57.9 to -19.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,713 | 5,709 | -0.1% | -27 to 18.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,729 | 5,726 | -0.1% | -21.5 to 15.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.38 | 0.381 | +0.2% | -0.027 to 0.0284 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.552 | 0.555 | +0.5% | -0.0785 to 0.0838 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.213 | +0.4% | -0.0146 to 0.0165 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 513 | +0.2% | -0.741 to 2.48 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 418 | +0.4% | 0.266 to 2.68 | power given |
| pages read into the cache (misses) | 687,410 | 683,616 | -0.6% | -12,625 to 5,037 | shown, not judged |
| host CPU busy (share of the run) | 0.291 | 0.296 | +1.7% | -0.0112 to 0.0208 | EVEN, no difference beyond the noise |
| host CPU-seconds | 527 | 537 | +1.9% | -31.7 to 52.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.198 | 0.202 | +2.0% | -0.0115 to 0.0194 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 8.33 |  | 4.54 to 12.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 322 | 324 | +0.9% | -18.5 to 24.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 317 | 320 | +0.7% | -18.6 to 23.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.23 | 4.82 | +13.9% | 0.12 to 1.05 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 527 | 538 | +1.9% | -31.6 to 52.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,903 | +1.0% | -91.6 to 149 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,883 | 2,913 | +1.0% | -90.4 to 149 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.223 | 0.227 | +1.8% | -0.00738 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.461 | 0.465 | +0.9% | -0.0394 to 0.0481 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.18 | 0.176 | -2.6% | -0.0238 to 0.0145 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 556 | +8.6% | -70.7 to 159 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 448 | +8.1% | -49.2 to 116 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,391 | 641,786 | -5.5% | -180,757 to 105,547 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.199 | -2.2% | -0.0707 to 0.0617 | EVEN, no difference beyond the noise |
| host CPU-seconds | 370 | 360 | -2.6% | -155 to 136 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.28 | 0.27 | -3.6% | -0.11 to 0.0901 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6.67 |  | -1.32 to 14.7 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 209 | 212 | +1.4% | -7.49 to 13.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 207 | 210 | +1.1% | -7.91 to 12.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.05 | 2.58 | +25.9% | 0.415 to 0.645 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 370 | 360 | -2.6% | -155 to 136 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
