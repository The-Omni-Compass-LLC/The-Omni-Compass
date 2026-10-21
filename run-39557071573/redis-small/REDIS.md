# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 8.74 to 14.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.036 to 0.0175 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00649 to 0.00933 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0161 to 0.0178 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.0422 to 0.082 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.6% | -0.0643 to -0.0102 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.3% | 1.25 to 1.65 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.886 to 1.46 | power given |
| keys evicted | 243,163 | 236,821 | -2.6% | -14,707 to 2,022 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.141 | -6.9% | -0.0236 to 0.00289 | EVEN, no difference beyond the noise |
| host CPU-seconds | 256 | 236 | -8.0% | -46.1 to 5.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.615 | 0.559 | -9.1% | -0.119 to 0.00711 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.3 |  | 7.08 to 19.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
