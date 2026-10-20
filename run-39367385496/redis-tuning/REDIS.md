# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,192 | +0.7% | -0.434 to 16.4 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00838 to 0.0123 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.795 | +0.7% | -0.000402 to 0.0112 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.0405 to 0.0295 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | -0.0% | -0.0419 to 0.0417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.1% | -0.0731 to 0.0152 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | -0.0752 to 2.08 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | 0.234 to 1.33 | power given |
| keys evicted | 138,187 | 135,372 | -2.0% | -6,720 to 1,091 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.118 | -5.8% | -0.109 to 0.0945 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 196 | -6.6% | -206 to 178 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.394 | 0.365 | -7.3% | -0.39 to 0.333 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 7.06 to 26.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
