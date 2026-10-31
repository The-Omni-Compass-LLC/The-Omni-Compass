# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.125 to 0.0708 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.5% | -0.0397 to -0.0152 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.1% | -0.0237 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.82 | -53.0% | -0.939 to -0.908 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,724 | 79.7 | -99.9% | -72,432 to -70,857 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.125 | -20.6% | -0.0423 to -0.0229 | GAIN |
| host CPU-seconds | 108 | 84.9 | -21.1% | -30.3 to -15 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.555 | 0.356 | -35.9% | -0.238 to -0.161 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 107 | -13.5% | -17.9 to -15.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.2 | 13.3 | -12.7% | -2.76 to -1.09 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 92.8 | -14.3% | -16.3 to -14.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.679 |  | 0.595 to 0.764 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0953 | 0.09 | -5.6% | -0.00897 to -0.00173 | shown, not judged |
| host CPU-seconds without steal | 108 | 84.9 | -21.1% | -30.3 to -14.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
