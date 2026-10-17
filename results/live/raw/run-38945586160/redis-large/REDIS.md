# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 7.67 to 27.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0332 to 0.0201 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.856 | +1.4% | 0.00504 to 0.0186 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% | -0.0139 to 0.00654 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.1% | -0.0385 to 0.024 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.897 | 0.836 | -6.8% | -0.0894 to -0.0327 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -0.754 to 1.99 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.3% | -1.13 to 1.52 | EVEN, no difference beyond the noise |
| keys evicted | 103,647 | 95,891 | -7.5% | -12,313 to -3,199 | shown, not judged |
| host CPU busy (share of the run) | 0.062 | 0.0569 | -8.1% | -0.0379 to 0.0279 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 99.9 | -8.2% | -69.6 to 51.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.191 | 0.173 | -9.5% | -0.123 to 0.0862 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
