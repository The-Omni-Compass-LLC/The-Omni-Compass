# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -1.88 to 1.09 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -1.92 to 0.412 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.334 | 0.332 | -0.7% | -0.00859 to 0.00392 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.588 | 0.582 | -1.1% | -0.0135 to 0.000838 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.199 | -0.6% | -0.0113 to 0.00871 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.25 to -1.45 | GAIN |
| bytes in the cache, mean (MB) | 417 | 416 | -0.3% | -3.46 to 0.917 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 712,186 | 673,332 | -5.5% | -123,078 to 45,369 | shown, not judged |
| host CPU busy (share of the run) | 0.213 | 0.182 | -14.5% | -0.0513 to -0.0104 | GAIN |
| host CPU-seconds | 377 | 310 | -17.8% | -112 to -21.7 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.284 | 0.233 | -17.8% | -0.0845 to -0.0164 | GAIN |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 199 | 199 | -0.4% | -15.8 to 14.3 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 197 | 195 | -0.7% | -16.4 to 13.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.52 | 3.11 | +23.3% | 0.451 to 0.724 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 377 | 310 | -17.8% | -112 to -21.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,931 | -0.1% | -8.97 to 2.18 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,935 | -0.1% | -8.2 to 3.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.266 | +3.8% | -0.0176 to 0.0369 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.425 | 0.445 | +4.9% | 0.00413 to 0.0372 | LOSS |
| latency, mean (ms) | 0.0832 | 0.0883 | +6.2% | 0.00367 to 0.00658 | LOSS |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -11.4 to -0.519 | GAIN |
| bytes in the cache, mean (MB) | 406 | 407 | +0.1% | -4.23 to 5.33 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 271,839 | 274,828 | +1.1% | -28,054 to 34,032 | shown, not judged |
| host CPU busy (share of the run) | 0.081 | 0.1 | +23.6% | -0.0788 to 0.117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 58.2 | 73.5 | +26.3% | -62.5 to 93.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.109 | 0.137 | +26.4% | -0.117 to 0.174 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -2.92 to 12.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 26.4 | 28 | +6.1% | -1.91 to 5.12 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 25.7 | 27.1 | +5.3% | -2.21 to 4.92 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.67 | 0.924 | +37.9% | 0.163 to 0.345 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 58.2 | 73.5 | +26.3% | -62.5 to 93.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,889 | 2,889 | -0.0% | -3.87 to 3.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% | -3.59 to 3.56 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.308 | -0.2% | -0.00446 to 0.00313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.489 | 0.488 | -0.1% | -0.0204 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.19 | 0.189 | -0.2% | -0.00272 to 0.00206 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 517 | +1.0% | -35.4 to 45.6 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 422 | +0.9% | -24.6 to 31.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,996 | 663,759 | -3.5% | -224,790 to 176,316 | shown, not judged |
| host CPU busy (share of the run) | 0.182 | 0.182 | -0.2% | -0.051 to 0.0504 | EVEN, no difference beyond the noise |
| host CPU-seconds | 317 | 316 | -0.3% | -109 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.238 | 0.237 | -0.3% | -0.0817 to 0.0805 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | -2.45 to 12.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 186 | -0.0% | -1.74 to 1.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 184 | 183 | -0.3% | -2.13 to 0.987 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.38 | 2.89 | +21.1% | 0.378 to 0.628 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 317 | 316 | -0.3% | -109 to 107 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,686 | 5,691 | +0.1% | -18.4 to 28 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,700 | 5,705 | +0.1% | -18.9 to 28.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.411 | 0.41 | -0.2% | -0.00597 to 0.00397 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.599 | 0.595 | -0.6% | -0.0094 to 0.00207 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.231 | 0.231 | -0.3% | -0.00297 to 0.00145 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 534 | +4.2% | -31.5 to 75 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 435 | +4.2% | -25.7 to 60.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,520 | 664,630 | -3.9% | -85,928 to 32,148 | shown, not judged |
| host CPU busy (share of the run) | 0.311 | 0.311 | -0.3% | -0.0104 to 0.00876 | EVEN, no difference beyond the noise |
| host CPU-seconds | 565 | 563 | -0.5% | -27.1 to 21.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.213 | 0.212 | -0.5% | -0.0103 to 0.00796 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 11 |  | 8.52 to 13.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 346 | 346 | +0.0% | -2.9 to 2.94 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 342 | 341 | -0.2% | -3.67 to 2.49 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 4.31 | 4.92 | +14.1% | 0.261 to 0.958 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 565 | 563 | -0.5% | -27.1 to 21.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,873 | -0.1% | -16.8 to 10.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,883 | -0.1% | -17.9 to 12.5 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.363 | +0.6% | -0.0023 to 0.0063 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.578 | 0.582 | +0.7% | -0.0219 to 0.0299 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | +0.2% | -0.0012 to 0.00196 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 530 | +3.5% | -12.6 to 48.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 432 | +3.5% | -9.28 to 38.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,119 | 663,562 | -2.1% | -38,060 to 8,947 | shown, not judged |
| host CPU busy (share of the run) | 0.251 | 0.272 | +8.3% | -0.00852 to 0.0504 | EVEN, no difference beyond the noise |
| host CPU-seconds | 439 | 488 | +11.2% | -19.1 to 117 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.331 | 0.368 | +11.3% | -0.0124 to 0.0869 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 9 |  | 6.52 to 11.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 275 | 277 | +0.5% | -2.96 to 5.56 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 273 | 273 | +0.2% | -3.62 to 4.96 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.61 | 3.24 | +24.1% | 0.435 to 0.823 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 439 | 488 | +11.2% | -19 to 117 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
