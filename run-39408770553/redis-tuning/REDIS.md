# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 11.8 to 16.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00384 to -0.00149 | LOSS |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00699 to 0.0115 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.23 | +0.1% | -0.00318 to 0.0141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.29 | +0.5% | -0.0474 to 0.0983 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.9% | -0.0537 to -0.0367 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.33 to 1.86 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 1.03 to 1.28 | power given |
| keys evicted | 138,329 | 132,929 | -3.9% | -6,920 to -3,881 | shown, not judged |
| host CPU busy (share of the run) | 0.0641 | 0.0616 | -3.8% | -0.0529 to 0.048 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 108 | -3.9% | -97.9 to 89 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.212 | 0.201 | -5.1% | -0.185 to 0.163 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
