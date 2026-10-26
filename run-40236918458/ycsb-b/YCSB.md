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

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
