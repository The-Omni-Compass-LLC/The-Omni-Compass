# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.8 to 12.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0199 to -0.00974 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00658 to 0.00867 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.65 | -0.0% | -0.00551 to 0.00422 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | +0.1% | -0.00151 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.24 | 2.2 | -1.8% | -0.0451 to -0.0364 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.04 to 1.59 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.812 to 1.49 | power given |
| keys evicted | 243,132 | 236,975 | -2.5% | -14,626 to 2,313 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.141 | -7.7% | -0.0276 to 0.00401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 265 | 242 | -8.8% | -54.3 to 7.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.637 | 0.574 | -9.9% | -0.138 to 0.0123 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 11.5 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
