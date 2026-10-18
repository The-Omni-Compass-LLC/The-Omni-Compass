# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 19.2 to 23.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00164 to 0.0026 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0131 to 0.0155 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.3% | -0.045 to 0.016 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.0% | -0.0181 to 0.0166 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.958 | 0.883 | -7.9% | -0.0912 to -0.0599 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | 0.131 to 1.9 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | -0.0734 to 1.47 | EVEN, no difference beyond the noise |
| keys evicted | 103,535 | 94,111 | -9.1% | -10,216 to -8,631 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.107 | +11.2% | 0.00367 to 0.0178 | power given |
| host CPU-seconds | 167 | 189 | +12.7% | 6.85 to 35.6 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.294 | 0.325 | +10.8% | 0.00781 to 0.0556 | power given |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
