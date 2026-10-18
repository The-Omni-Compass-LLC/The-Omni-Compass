# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.4% | 11.1 to 14.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.029 to 0.00761 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.4% | 0.00753 to 0.00965 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.71 | +0.1% | -0.00732 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.77 | +0.3% | 0.0139 to 0.0164 | LOSS |
| latency, mean (ms) | 2.27 | 2.23 | -1.9% | -0.0498 to -0.0362 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.4% | 1.23 to 1.88 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.833 to 1.33 | power given |
| keys evicted | 243,182 | 239,557 | -1.5% | -8,593 to 1,342 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.143 | +0.5% | -0.0142 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 238 | +0.7% | -27.9 to 31 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.568 | 0.564 | -0.7% | -0.0733 to 0.0652 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.7 |  | 14.2 to 17.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
