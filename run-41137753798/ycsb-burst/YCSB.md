# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,876 | -0.0% | -10.6 to 7.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -9.04 to 7.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.522 | 0.528 | +1.1% | -0.0128 to 0.0248 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.665 | 0.676 | +1.7% | -0.0191 to 0.0411 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.224 | 0.226 | +1.0% | -0.0125 to 0.0171 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,502 | 1,501 | -0.1% | -9.41 to 6.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,576 | 77,650 | +0.1% | -195 to 343 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.191 | +3.8% | -0.0369 to 0.0507 | EVEN, no difference beyond the noise |
| host CPU-seconds | 127 | 133 | +4.4% | -31.7 to 43 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.25 | +4.5% | -0.0604 to 0.0817 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 77.6 | 79.1 | +1.9% | -2.77 to 5.77 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 76.6 | 78 | +1.9% | -2.8 to 5.7 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 1.05 | 1.09 | +4.1% | -0.0358 to 0.123 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 127 | 133 | +4.4% | -31.7 to 43 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
