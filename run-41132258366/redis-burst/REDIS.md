# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.3% | 246 to 254 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0206 to 0.0406 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.165 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.72 | -0.5% | -0.0668 to 0.0081 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.2% | -0.0451 to 0.0266 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.817 | -53.0% | -0.945 to -0.899 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 244 | +281.4% | 163 to 197 | power given |
| memory used, mean (MB) | 57.1 | 200 | +249.9% | 141 to 145 | power given |
| keys evicted | 71,754 | 76 | -99.9% | -72,546 to -70,809 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.142 | +2.2% | -0.0183 to 0.0245 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.3 | 98.6 | +5.7% | -11.4 to 22 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.482 | 0.413 | -14.3% | -0.151 to 0.0131 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | -5.11 to 25.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 121 | 106 | -12.8% | -20.8 to -10.1 | GAIN |
| the server's own CPU-seconds (redis-server) | 14.7 | 13.2 | -10.2% | -2 to -0.984 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 106 | 91.7 | -13.7% | -19.4 to -9.84 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.64 |  | 0.43 to 0.849 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0943 | 0.091 | -3.5% | -0.00863 to 0.00193 | shown, not judged |
| host CPU-seconds without steal | 93.3 | 98.6 | +5.7% | -11.4 to 22 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
