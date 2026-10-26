# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,939 | -0.0% | -4 to 3.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -4.58 to 4.58 | EVEN, the same |
| latency, 95th percentile (ms) | 0.242 | 0.252 | +4.3% | -0.0155 to 0.0362 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.381 | 0.4 | +4.8% | -0.00937 to 0.046 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0718 | 0.0752 | +4.7% | -0.00278 to 0.00955 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,521 | 1,522 | +0.1% | -4.6 to 6.57 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,695 | 77,745 | +0.1% | -421 to 521 | shown, not judged |
| host CPU busy (share of the run) | 0.0684 | 0.0769 | +12.5% | -0.1 to 0.117 | EVEN, no difference beyond the noise |
| host CPU-seconds | 49.1 | 56.2 | +14.6% | -78.5 to 92.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0916 | 0.105 | +14.6% | -0.147 to 0.173 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 21.2 | 22 | +3.9% | 0.335 to 1.33 | power given |
| the server's own CPU-seconds (mongod) | 20.6 | 21.4 | +3.9% | 0.267 to 1.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.616 | 0.646 | +4.8% | -0.0394 to 0.0981 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 49.1 | 56.2 | +14.6% | -78.5 to 92.8 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
