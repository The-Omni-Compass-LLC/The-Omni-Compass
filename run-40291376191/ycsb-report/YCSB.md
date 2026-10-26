# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | -0.0% | -6.94 to 4.49 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,907 | 2,907 | -0.0% | -5.53 to 3.63 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.317 | 0.322 | +1.5% | -0.013 to 0.0223 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.499 | 0.508 | +1.9% | -0.0358 to 0.0545 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.159 | 0.159 | +0.6% | -0.00206 to 0.0038 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.38 to -1.33 | GAIN |
| bytes in the cache, mean (MB) | 418 | 418 | +0.0% | -6.23 to 6.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 695,880 | 696,097 | +0.0% | -71,383 to 71,817 | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.174 | +5.1% | -0.0166 to 0.0335 | EVEN, no difference beyond the noise |
| host CPU-seconds | 295 | 312 | +6.1% | -36.8 to 72.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.234 | +6.1% | -0.0274 to 0.0544 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | -2.92 to 12.3 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 154 | 155 | +0.6% | -2.3 to 4.13 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 152 | 152 | +0.2% | -2.77 to 3.45 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 3.09 | +22.8% | 0.467 to 0.682 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 295 | 312 | +6.1% | -36.8 to 72.6 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,629 | 2,744 | +4.4% | -873 to 1,103 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,644 | 2,761 | +4.4% | -865 to 1,100 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.312 | 0.315 | +1.1% | -0.0632 to 0.0698 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.574 | 0.606 | +5.6% | -0.373 to 0.437 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.237 | 0.217 | -8.4% | -0.165 to 0.125 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 532 | +4.0% | -33.7 to 74.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 394 | 410 | +4.3% | -22 to 55.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 219,531 | 245,677 | +11.9% | -132,269 to 184,561 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.156 | +3.9% | -0.126 to 0.138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 113 | +3.5% | -104 to 112 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.225 | 0.224 | -0.4% | -0.182 to 0.18 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 10.3 |  | 5.16 to 15.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 56.7 | 59.3 | +4.5% | -16.1 to 21.2 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 56 | 58.4 | +4.2% | -16.1 to 20.9 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.766 | 0.955 | +24.7% | 0.0141 to 0.364 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 109 | 113 | +3.5% | -104 to 112 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,907 | +0.0% | -1.12 to 2.86 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,908 | 2,909 | +0.0% | -1.22 to 2.89 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.276 | 0.274 | -0.5% | -0.0042 to 0.00154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.449 | 0.444 | -1.2% | -0.0082 to -0.00246 | GAIN |
| latency, mean (ms) | 0.149 | 0.148 | -0.6% | -0.00506 to 0.00331 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.27 to 0.318 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 417 | -0.7% | -12.3 to 6.57 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 707,383 | 677,481 | -4.2% | -185,887 to 126,083 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.174 | +12.8% | -0.107 to 0.146 | EVEN, no difference beyond the noise |
| host CPU-seconds | 276 | 319 | +15.5% | -233 to 319 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.239 | +15.5% | -0.175 to 0.239 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | -0.838 to 9.5 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 141 | 141 | -0.3% | -5.36 to 4.39 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 139 | 138 | -0.7% | -5.83 to 3.85 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.46 | 2.97 | +20.3% | 0.456 to 0.547 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 276 | 319 | +15.5% | -233 to 319 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,751 | 5,745 | -0.1% | -25.3 to 13.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,767 | 5,763 | -0.1% | -26.9 to 18.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.321 | +1.0% | -0.00384 to 0.0105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.482 | 0.494 | +2.6% | -0.05 to 0.0747 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.191 | +1.7% | -0.00338 to 0.00964 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 569 | +11.2% | -11.6 to 126 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 457 | +10.0% | -16.6 to 99.7 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 688,498 | 631,501 | -8.3% | -121,924 to 7,929 | shown, not judged |
| host CPU busy (share of the run) | 0.248 | 0.258 | +3.9% | -0.0217 to 0.041 | EVEN, no difference beyond the noise |
| host CPU-seconds | 452 | 474 | +5.0% | -54.1 to 99.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.169 | 0.178 | +5.0% | -0.0203 to 0.0372 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 10.3 |  | 8.9 to 11.8 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 271 | 274 | +1.1% | 1.1 to 4.8 | power given |
| the server's own CPU-seconds (mongod) | 267 | 270 | +0.9% | 0.742 to 3.97 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 3.42 | 4.02 | +17.2% | 0.231 to 0.95 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 452 | 474 | +5.0% | -54.1 to 99.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `f70084ae1bb3`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,934 | -0.0% | -5.39 to 4.85 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,937 | -0.0% | -4.54 to 3.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.152 | 0.15 | -1.1% | -0.0415 to 0.0382 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.345 | 0.345 | -0.1% | -0.044 to 0.0433 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0801 | 0.079 | -1.3% | -0.00888 to 0.00684 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.31 to -1.52 | GAIN |
| bytes in the cache, mean (MB) | 419 | 419 | -0.0% | -3.56 to 3.31 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 694,123 | 702,215 | +1.2% | -29,225 to 45,410 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.119 | -2.3% | -0.124 to 0.119 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 218 | -3.0% | -259 to 245 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.168 | 0.163 | -3.0% | -0.193 to 0.183 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 106 | 106 | +0.1% | -6.34 to 6.54 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 104 | 104 | -0.3% | -6.64 to 5.94 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.69 | 2.14 | +26.6% | 0.227 to 0.672 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 224 | 218 | -3.0% | -259 to 245 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
