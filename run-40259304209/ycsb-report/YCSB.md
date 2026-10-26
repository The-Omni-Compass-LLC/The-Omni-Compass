# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,887 | -0.0% | -3.19 to 2.43 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,892 | -0.0% | -3.69 to 2.82 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.321 | 0.326 | +1.5% | -0.00654 to 0.0159 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.488 | 0.494 | +1.2% | -0.00891 to 0.0209 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.195 | +0.7% | -0.00356 to 0.00624 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.3% | -1.91 to -1.51 | GAIN |
| bytes in the cache, mean (MB) | 419 | 420 | +0.2% | -2.41 to 4.18 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 721,546 | 741,544 | +2.8% | -138,277 to 178,273 | shown, not judged |
| host CPU busy (share of the run) | 0.211 | 0.205 | -2.5% | -0.037 to 0.0267 | EVEN, no difference beyond the noise |
| host CPU-seconds | 374 | 362 | -3.2% | -79.5 to 55.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.272 | -3.2% | -0.0596 to 0.0417 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 197 | 199 | +1.3% | -3.7 to 9.01 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 194 | 196 | +1.1% | -4.23 to 8.45 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.5 | 3.04 | +21.7% | 0.432 to 0.651 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 374 | 362 | -3.2% | -79.5 to 55.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,881 | -0.0% | -4.64 to 2.88 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -3.44 to 2.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.408 | 0.409 | +0.2% | -0.0118 to 0.0132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.577 | 0.579 | +0.4% | -0.0254 to 0.03 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.211 | 0.21 | -0.2% | -0.00485 to 0.00406 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 515 | +0.6% | -17 to 22.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 405 | 408 | +0.8% | -18.1 to 24.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 256,907 | 272,467 | +6.1% | 3,337 to 27,783 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.178 | -14.6% | -0.0963 to 0.0356 | EVEN, no difference beyond the noise |
| host CPU-seconds | 148 | 122 | -17.7% | -84.1 to 31.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.229 | -17.7% | -0.158 to 0.06 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7.33 |  | 4.46 to 10.2 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 80 | 80 | -0.0% | -2.73 to 2.72 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 79 | 78.7 | -0.3% | -2.86 to 2.42 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.01 | 1.22 | +21.2% | 0.127 to 0.301 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 148 | 122 | -17.7% | -84.2 to 32 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,889 | +0.0% | -0.411 to 3.27 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,893 | +0.0% | -0.274 to 2.99 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.303 | 0.302 | -0.3% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 0.487 | +0.0% | -0.00657 to 0.00657 | EVEN, the same |
| latency, mean (ms) | 0.188 | 0.189 | +0.6% | -0.00406 to 0.00646 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -3.87 to -0.29 | GAIN |
| bytes in the cache, mean (MB) | 419 | 420 | +0.3% | -2.81 to 4.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,735 | 714,771 | +5.2% | -100,464 to 170,537 | shown, not judged |
| host CPU busy (share of the run) | 0.198 | 0.191 | -3.8% | -0.0361 to 0.0211 | EVEN, no difference beyond the noise |
| host CPU-seconds | 351 | 335 | -4.7% | -81.5 to 48.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.251 | -4.7% | -0.0612 to 0.0362 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 183 | 186 | +1.1% | -4.65 to 8.81 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 181 | 183 | +0.9% | -5.19 to 8.37 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 2.97 | +19.9% | 0.423 to 0.566 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 351 | 335 | -4.7% | -81.6 to 48.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,677 | 5,686 | +0.1% | -17.9 to 34.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,695 | 5,703 | +0.2% | -18.3 to 35.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.431 | 0.428 | -0.7% | -0.0129 to 0.00694 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.656 | 0.657 | +0.2% | -0.0119 to 0.0139 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.244 | -0.9% | -0.00979 to 0.00555 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 540 | +5.5% | -36.2 to 92.3 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 439 | +5.4% | -28.7 to 73.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,148 | 654,260 | -3.7% | -108,492 to 58,716 | shown, not judged |
| host CPU busy (share of the run) | 0.325 | 0.321 | -1.4% | -0.0385 to 0.0294 | EVEN, no difference beyond the noise |
| host CPU-seconds | 589 | 577 | -1.9% | -96.3 to 73.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.217 | -2.0% | -0.0373 to 0.0283 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 6.03 to 16 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 354 | 352 | -0.7% | -14.4 to 9.41 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 350 | 347 | -0.9% | -14.8 to 8.68 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.35 | 4.91 | +12.9% | 0.0835 to 1.04 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 589 | 577 | -1.9% | -96.3 to 73.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,881 | -0.1% | -5.76 to 2.11 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,889 | -0.1% | -5.45 to 1.55 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.335 | 0.337 | +0.5% | -0.00407 to 0.0074 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.512 | 0.517 | +0.8% | -0.00326 to 0.0119 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.207 | 0.208 | +0.5% | -0.00284 to 0.00477 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 535 | +4.5% | -31.9 to 78 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 436 | +4.3% | -25.5 to 61.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 673,795 | 650,602 | -3.4% | -87,557 to 41,171 | shown, not judged |
| host CPU busy (share of the run) | 0.253 | 0.262 | +3.6% | -0.0614 to 0.0797 | EVEN, no difference beyond the noise |
| host CPU-seconds | 454 | 476 | +4.8% | -153 to 196 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.342 | 0.358 | +4.8% | -0.115 to 0.148 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11.7 |  | 7.87 to 15.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 269 | 271 | +0.9% | 0.446 to 4.46 | power given |
| the server's own CPU-seconds (mongod) | 266 | 268 | +0.7% | -0.171 to 3.8 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.48 | 3.11 | +25.8% | 0.57 to 0.705 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 454 | 476 | +4.8% | -153 to 196 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
