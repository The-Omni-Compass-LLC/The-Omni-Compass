# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,902 | +0.1% | -11.5 to 19.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,910 | 2,914 | +0.1% | -11 to 19.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.305 | 0.321 | +5.4% | -0.0239 to 0.0566 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.462 | 0.474 | +2.5% | -0.00202 to 0.0253 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.168 | 0.161 | -4.0% | -0.018 to 0.00451 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 527 | +2.9% | -47.1 to 77 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 418 | +4.2% | -27.5 to 61.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 275,871 | 274,953 | -0.3% | -39,253 to 37,418 | shown, not judged |
| host CPU busy (share of the run) | 0.155 | 0.141 | -9.0% | -0.115 to 0.0874 | EVEN, no difference beyond the noise |
| host CPU-seconds | 111 | 99.1 | -10.6% | -95.6 to 72.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.208 | 0.186 | -10.6% | -0.179 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 7 |  | 0.427 to 13.6 | shown, not judged |
| the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded) | 62.5 | 63.1 | +1.0% | -1.36 to 2.56 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (mongod) | 61.7 | 62.1 | +0.7% | -1.48 to 2.34 | shown, not judged |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both) | 0.83 | 0.996 | +20.0% | 0.102 to 0.229 | shown, not judged |
| host CPU-seconds without steal (the load generator included) | 111 | 99.1 | -10.6% | -95.7 to 72.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
