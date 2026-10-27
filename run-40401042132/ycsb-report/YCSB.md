# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,846 | 2,847 | +0.0% | -2.12 to 4.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,855 | 2,856 | +0.0% | -0.00125 to 2.08 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.46 | 0.456 | -0.9% | -0.0171 to 0.00915 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.64 | 0.635 | -0.8% | -0.0348 to 0.0241 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.212 | 0.21 | -0.9% | -0.00726 to 0.00335 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 511 | -0.1% | -1.47 to 0.0953 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 412 | -0.5% | -9.29 to 5.32 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 447,243 | 472,178 | +5.6% | -84,119 to 133,989 | shown, not judged |
| host CPU busy (share of the run) | 0.232 | 0.228 | -1.7% | -0.0759 to 0.068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 273 | 268 | -1.7% | -115 to 105 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.31 | 0.304 | -1.8% | -0.131 to 0.12 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5.33 |  | -2.26 to 12.9 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 134 | 133 | -0.3% | -1.81 to 1.06 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 132 | 131 | -0.5% | -2.19 to 0.814 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.7 | 2.01 | +18.5% | 0.195 to 0.435 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 273 | 268 | -1.7% | -115 to 105 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | +0.0% | -3.89 to 4.19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,916 | +0.0% | -3.56 to 4.56 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.27 | 0.272 | +0.7% | -0.00297 to 0.00697 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.451 | 0.459 | +1.7% | -0.0111 to 0.0265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.091 | 0.0913 | +0.4% | -0.00111 to 0.00177 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.65 to -1.16 | GAIN |
| bytes in the cache, mean (MB) | 403 | 398 | -1.1% | -20.6 to 11.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 187,354 | 178,027 | -5.0% | -56,662 to 38,008 | shown, not judged |
| host CPU busy (share of the run) | 0.0789 | 0.0987 | +25.0% | -0.0378 to 0.0773 | EVEN, no difference beyond the noise |
| host CPU-seconds | 37.1 | 47.5 | +28.2% | -19.8 to 40.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.104 | 0.134 | +28.2% | -0.0556 to 0.114 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 18 | 18.1 | +0.4% | -0.919 to 1.07 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 17.6 | 17.5 | -0.3% | -1 to 0.907 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.453 | 0.575 | +26.9% | 0.08 to 0.164 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 37.1 | 47.5 | +28.2% | -19.8 to 40.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,852 | 2,851 | -0.0% | -3.39 to 1.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,858 | 2,857 | -0.0% | -3.07 to 2.01 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.392 | 0.393 | +0.2% | -0.00313 to 0.00446 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.542 | 0.55 | +1.4% | -0.0113 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.2 | +0.3% | -0.00253 to 0.00358 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 529 | +3.3% | -61.9 to 95.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 431 | +3.4% | -53 to 81.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 479,768 | 463,252 | -3.4% | -129,751 to 96,718 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.209 | -0.2% | -0.02 to 0.019 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 242 | -0.2% | -27.8 to 26.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.275 | -0.2% | -0.0314 to 0.0302 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 125 | 126 | +0.2% | -5.09 to 5.49 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 124 | 124 | -0.1% | -5.4 to 5.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.62 | 1.97 | +21.8% | 0.311 to 0.392 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 243 | 242 | -0.2% | -27.8 to 26.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,496 | 5,508 | +0.2% | -84.9 to 110 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,523 | 5,535 | +0.2% | -83.2 to 108 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.488 | 0.489 | +0.2% | -0.0193 to 0.0213 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.786 | 0.784 | -0.3% | -0.044 to 0.0386 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.259 | 0.258 | -0.2% | -0.0163 to 0.0154 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 550 | +7.5% | -117 to 193 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 413 | 442 | +7.2% | -89.2 to 148 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 452,928 | 426,075 | -5.9% | -139,620 to 85,913 | shown, not judged |
| host CPU busy (share of the run) | 0.355 | 0.358 | +0.6% | -0.0297 to 0.0342 | EVEN, no difference beyond the noise |
| host CPU-seconds | 433 | 437 | +0.7% | -46.2 to 52.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.252 | 0.253 | +0.5% | -0.0316 to 0.0341 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9 |  | 4.7 to 13.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 230 | 232 | +0.8% | -8.99 to 12.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 227 | 229 | +0.6% | -9.44 to 12.1 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.96 | 3.41 | +15.2% | 0.0617 to 0.838 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 433 | 437 | +0.7% | -46.2 to 52.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 2.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,831 | 2,827 | -0.1% | -9.44 to 2.71 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,843 | 2,840 | -0.1% | -10 to 5.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.425 | 0.434 | +2.1% | 4.26e-05 to 0.018 | LOSS |
| latency, 99th percentile (ms) | 0.653 | 0.678 | +3.8% | -0.0594 to 0.109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.234 | 0.239 | +2.1% | -0.0005 to 0.0102 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 573 | +11.9% | 35.2 to 86.4 | power given |
| bytes in the cache, mean (MB) | 415 | 462 | +11.4% | 30.3 to 64.1 | power given |
| pages read into the cache (misses) | 455,579 | 423,420 | -7.1% | -47,483 to -16,835 | shown, not judged |
| host CPU busy (share of the run) | 0.293 | 0.312 | +6.6% | 0.000402 to 0.0381 | power given |
| host CPU-seconds | 346 | 376 | +8.7% | -8.03 to 68 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.395 | 0.429 | +8.7% | -0.00894 to 0.0778 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9.33 |  | 5.54 to 13.1 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 190 | +2.2% | -3.83 to 11.9 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 187 | +1.9% | -4.37 to 11.4 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.78 | 2.29 | +28.9% | 0.449 to 0.578 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 346 | 376 | +8.7% | -8.03 to 68 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
