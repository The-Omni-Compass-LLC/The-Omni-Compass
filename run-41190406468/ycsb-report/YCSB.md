# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% | -2.4 to -0.0247 | LOSS |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -2.29 to 0.519 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.322 | +1.2% | -0.00574 to 0.0131 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.594 | 0.598 | +0.6% | -0.00259 to 0.00992 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.194 | +0.6% | -0.00295 to 0.00528 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,364 | -0.1% | -3.53 to 1.59 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,792 | 61,811 | +0.0% | -228 to 264 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.192 | +4.2% | -0.0638 to 0.0794 | EVEN, no difference beyond the noise |
| host CPU-seconds | 321 | 336 | +4.6% | -142 to 172 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.253 | +4.6% | -0.107 to 0.129 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 186 | 186 | +0.1% | -1.61 to 1.83 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 183 | 183 | +0.0% | -1.57 to 1.67 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 2.59 | +2.2% | -0.04 to 0.151 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 321 | 336 | +4.6% | -142 to 171 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,883 | -0.0% | -3.81 to 2.22 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -3.58 to 2.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.406 | 0.409 | +0.7% | -0.00854 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.541 | 0.55 | +1.8% | -0.0065 to 0.0258 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.209 | 0.208 | -0.5% | -0.00793 to 0.00591 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,516 | 1,514 | -0.1% | -3.43 to -0.651 | GAIN |
| pages read into the cache (misses) | 77,664 | 77,631 | -0.0% | -356 to 289 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.181 | -1.5% | -0.135 to 0.13 | EVEN, no difference beyond the noise |
| host CPU-seconds | 127 | 125 | -1.4% | -110 to 107 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.235 | -1.4% | -0.207 to 0.201 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 78.3 | 77.2 | -1.4% | -4.99 to 2.82 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 77.3 | 76.2 | -1.5% | -4.95 to 2.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.997 | 1.04 | +4.2% | -0.0365 to 0.12 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 127 | 125 | -1.4% | -110 to 107 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,902 | 2,901 | -0.0% | -2.13 to 0.598 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,906 | 2,905 | -0.0% | -1.46 to 0.228 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.289 | 0.291 | +0.6% | -0.00954 to 0.0129 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.485 | 0.485 | +0.0% | -0.0361 to 0.0361 | EVEN, the same |
| latency, mean (ms) | 0.149 | 0.149 | -0.2% | -0.00347 to 0.00297 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,348 | -0.1% | -5.02 to 2.63 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,696 | 61,631 | -0.1% | -306 to 177 | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.163 | -13.8% | -0.0683 to 0.016 | EVEN, no difference beyond the noise |
| host CPU-seconds | 353 | 294 | -16.5% | -152 to 35.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.265 | 0.221 | -16.5% | -0.114 to 0.0268 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 134 | 134 | -0.3% | -2.86 to 2.11 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 132 | 131 | -0.4% | -2.9 to 1.91 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.53 | 2.65 | +4.7% | 0.0261 to 0.21 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 353 | 294 | -16.5% | -152 to 35.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,851 | 5,852 | +0.0% | -10 to 12.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,856 | 5,858 | +0.0% | -9.3 to 12.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.146 | 0.146 | -0.0% | -0.0155 to 0.0155 | EVEN, the same |
| latency, 99th percentile (ms) | 0.332 | 0.338 | +1.9% | -0.0691 to 0.0818 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0739 | 0.0746 | +1.0% | -0.00205 to 0.00359 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -3.99 to 4.37 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,297 | 63,176 | -0.2% | -797 to 555 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.115 | -1.5% | -0.0918 to 0.0882 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 210 | -2.1% | -192 to 183 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0801 | 0.0784 | -2.1% | -0.0717 to 0.0682 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 93.2 | 92.7 | -0.5% | -0.78 to -0.134 | GAIN |
| the server's own CPU-seconds (mongod) | 90.9 | 90.4 | -0.5% | -0.812 to -0.134 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.32 | 2.34 | +0.7% | -0.0634 to 0.0965 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 215 | 210 | -2.1% | -192 to 183 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `ebf98fa29775`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,881 | +0.0% | -1.37 to 2.19 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,887 | +0.0% | -1.76 to 2.11 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.34 | 0.343 | +0.9% | -0.00783 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.541 | 0.539 | -0.5% | -0.0186 to 0.0133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.205 | 0.207 | +0.5% | -0.00827 to 0.0103 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.1% | -4 to 2.02 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 63,104 | 63,022 | -0.1% | -396 to 232 | shown, not judged |
| host CPU busy (share of the run) | 0.232 | 0.232 | -0.2% | -0.0164 to 0.0153 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 409 | -0.3% | -38.3 to 36.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.309 | 0.308 | -0.3% | -0.0291 to 0.0275 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 232 | 234 | +0.8% | -9.1 to 12.6 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 230 | 232 | +0.7% | -9.17 to 12.5 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 2.51 | 2.62 | +4.2% | 0.0594 to 0.154 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 410 | 409 | -0.3% | -38.3 to 36.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
