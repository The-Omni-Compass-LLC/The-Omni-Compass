# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `86b4d987fa63`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 246 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0857 to 0.0778 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.885 | +23.3% | 0.164 to 0.171 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.6% | -0.0559 to -0.0122 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.79 | -0.3% | -0.0448 to 0.00588 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.814 | -53.3% | -0.94 to -0.917 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.0% | 163 to 198 | power given |
| memory used, mean (MB) | 57.2 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,790 | 75 | -99.9% | -72,753 to -70,677 | shown, not judged |
| host CPU busy (share of the run) | 0.161 | 0.129 | -19.7% | -0.0682 to 0.0049 | EVEN, no difference beyond the noise |
| host CPU-seconds | 110 | 88 | -20.1% | -52.3 to 8.04 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.568 | 0.368 | -35.2% | -0.36 to -0.0405 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122 | 105 | -14.1% | -20.1 to -14.5 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.3 | 13.2 | -13.9% | -3.08 to -1.17 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 107 | 91 | -14.8% | -17.8 to -13.9 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.691 |  | 0.518 to 0.864 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0944 | 0.0907 | -4.0% | -0.0115 to 0.004 | shown, not judged |
| host CPU-seconds without steal | 110 | 88 | -20.1% | -52.3 to 8.04 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
