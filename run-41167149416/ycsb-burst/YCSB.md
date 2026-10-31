# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `cafcbf0d065d`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,901 | 2,835 | -2.3% | -344 to 212 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,912 | 2,848 | -2.2% | -335 to 207 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.312 | 0.321 | +2.8% | -0.0139 to 0.0312 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.467 | 0.496 | +6.2% | -0.103 to 0.161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.166 | 0.168 | +1.0% | -0.0216 to 0.025 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,466 | -2.8% | -214 to 129 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,723 | 77,391 | -0.4% | -1,437 to 773 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.111 | +2.6% | -0.0711 to 0.0768 | EVEN, no difference beyond the noise |
| host CPU-seconds | 74.3 | 76.7 | +3.2% | -54.2 to 59 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.139 | 0.146 | +5.1% | -0.0945 to 0.109 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 58.2 | 57.2 | -1.7% | -5.44 to 3.44 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 57.4 | 56.4 | -1.7% | -5.4 to 3.42 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.81 | 0.798 | -1.5% | -0.0646 to 0.0399 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 74.3 | 76.7 | +3.2% | -54.2 to 59 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
