# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,194 | +0.9% | 5.53 to 16.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00924 to 0.00789 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +0.9% | 0.00317 to 0.0115 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.015 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.84 | 5.9 | +1.0% | -0.0947 to 0.216 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.32 | -2.9% | -0.0655 to -0.014 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 0.0567 to 2.65 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.0173 to 1.95 | power given |
| keys evicted | 138,228 | 133,811 | -3.2% | -7,823 to -1,011 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.133 | +5.4% | -0.0185 to 0.0323 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 225 | +6.5% | -34.8 to 62.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.397 | 0.419 | +5.5% | -0.0696 to 0.113 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 10.4 to 27.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
