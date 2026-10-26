# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 10.9 to 21.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00633 to 0.000996 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00752 to 0.014 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.2% | -0.0212 to -0.00243 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.00954 to 0.0097 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.959 | 0.901 | -6.0% | -0.0812 to -0.034 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.2 | -1.3% | -0.972 to -0.688 | GAIN |
| memory used, mean (MB) | 61.3 | 60.1 | -2.0% | -1.88 to -0.604 | GAIN |
| keys evicted | 103,401 | 96,558 | -6.6% | -9,021 to -4,665 | shown, not judged |
| host CPU busy (share of the run) | 0.099 | 0.0874 | -11.7% | -0.0555 to 0.0323 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 151 | -12.9% | -108 to 63.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.305 | 0.262 | -14.0% | -0.194 to 0.109 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 26.5 to 31.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 193 | 191 | -1.1% | -6.25 to 1.87 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 26.2 | 26.1 | -0.4% | -0.821 to 0.635 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 167 | 164 | -1.7% | -6.72 to 1.13 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.697 |  | 0.572 to 0.821 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.161 | -1.5% | -0.00619 to 0.00135 | shown, not judged |
| host CPU-seconds without steal | 174 | 151 | -12.9% | -108 to 63.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
