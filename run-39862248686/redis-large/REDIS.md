# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,289 | +1.8% | 21.3 to 23.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00154 to 0.0022 | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.8% | 0.0142 to 0.0156 | GAIN |
| latency, 95th percentile (ms) | 5.59 | 5.58 | -0.2% | -0.0536 to 0.0281 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0384 to 0.0349 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.984 | 0.903 | -8.2% | -0.0995 to -0.0626 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.05 to 1.93 | power given |
| memory used, mean (MB) | 61.3 | 62.4 | +1.9% | 1.07 to 1.23 | power given |
| keys evicted | 103,542 | 93,733 | -9.5% | -10,267 to -9,351 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.113 | +10.4% | -0.00803 to 0.0293 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 202 | +11.9% | -13.7 to 56.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.349 | +10.0% | -0.0306 to 0.0938 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 17.5 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
