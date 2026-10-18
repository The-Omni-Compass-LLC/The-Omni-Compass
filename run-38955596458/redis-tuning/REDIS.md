# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% | 10.7 to 16.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0128 to 0.0172 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00795 to 0.0103 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.0184 to 0.0185 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.1% | -0.0424 to 0.0484 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -3.8% | -0.066 to -0.0226 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 0.99 to 2.4 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.869 to 1.62 | power given |
| keys evicted | 138,227 | 132,886 | -3.9% | -6,120 to -4,561 | shown, not judged |
| host CPU busy (share of the run) | 0.0531 | 0.0645 | +21.5% | -0.00108 to 0.0239 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.2 | 115 | +23.0% | -1.17 to 44 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.175 | 0.213 | +21.6% | -0.00513 to 0.0808 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
