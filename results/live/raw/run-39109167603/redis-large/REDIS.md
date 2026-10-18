# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,289 | +1.7% | 19.3 to 23.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00432 to 0.00244 | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.7% | 0.0129 to 0.0157 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.3% | -0.0479 to 0.0768 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.67 | +0.2% | -0.023 to 0.0507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.941 | 0.871 | -7.4% | -0.0757 to -0.0638 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.06 to 1.73 | power given |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% | 0.959 to 1.25 | power given |
| keys evicted | 103,173 | 93,754 | -9.1% | -10,354 to -8,485 | shown, not judged |
| host CPU busy (share of the run) | 0.0904 | 0.0806 | -10.8% | -0.0641 to 0.0446 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 142 | -11.3% | -122 to 85.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.244 | -12.8% | -0.213 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 17.9 to 20.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
