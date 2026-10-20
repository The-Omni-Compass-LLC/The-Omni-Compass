# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,287 | +1.6% | 17.3 to 24.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0124 to 0.0227 | EVEN, no difference beyond the noise |
| cache hit rate | 0.846 | 0.859 | +1.6% | 0.0118 to 0.0158 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% | -0.0156 to 0.00936 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.27 | -0.1% | -0.0344 to 0.0268 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.891 | 0.817 | -8.4% | -0.0891 to -0.0601 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.4% | 0.0726 to 3.06 | power given |
| memory used, mean (MB) | 61.3 | 62.5 | +1.9% | 0.678 to 1.66 | power given |
| keys evicted | 102,969 | 93,778 | -8.9% | -10,330 to -8,052 | shown, not judged |
| host CPU busy (share of the run) | 0.0668 | 0.0733 | +9.7% | -0.00916 to 0.0221 | EVEN, no difference beyond the noise |
| host CPU-seconds | 118 | 130 | +10.6% | -16.9 to 41.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.207 | 0.225 | +8.8% | -0.0322 to 0.0684 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 16.9 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
