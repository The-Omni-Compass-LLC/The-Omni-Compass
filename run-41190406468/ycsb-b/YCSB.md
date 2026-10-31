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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
