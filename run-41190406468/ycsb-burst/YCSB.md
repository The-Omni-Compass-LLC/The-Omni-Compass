# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
