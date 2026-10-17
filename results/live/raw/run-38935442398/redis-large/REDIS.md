# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 16.6 to 23.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00063 to 0.00146 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0126 to 0.0144 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.49 | -0.0% | -0.0215 to 0.0193 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.1% | -0.00608 to 0.0161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.955 | 0.887 | -7.1% | -0.0854 to -0.0512 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.237 to 2.97 | power given |
| memory used, mean (MB) | 61.3 | 62.1 | +1.3% | 0.403 to 1.25 | power given |
| keys evicted | 103,115 | 94,196 | -8.6% | -9,548 to -8,288 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.105 | +5.5% | -0.069 to 0.08 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 186 | +6.0% | -134 to 155 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.321 | +4.3% | -0.239 to 0.265 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
