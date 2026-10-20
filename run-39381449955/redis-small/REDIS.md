# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.11 to 13.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0154 to 0.00746 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00605 to 0.00965 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0156 to 0.0119 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.81 | +1.2% | -0.209 to 0.343 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.6% | -0.0597 to -0.0149 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.3 to 1.47 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.864 to 1.47 | power given |
| keys evicted | 243,186 | 236,889 | -2.6% | -14,371 to 1,776 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.131 | -9.4% | -0.0316 to 0.00442 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 217 | -10.6% | -61.5 to 10.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.583 | 0.515 | -11.6% | -0.152 to 0.0164 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 6.08 to 21.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
