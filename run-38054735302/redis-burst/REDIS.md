# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.48 to 1.51 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00759 to 0.00717 | same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00154 to 0.000955 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% | -0.036 to 0.0344 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.77 | +0.1% | -0.0437 to 0.0581 | no difference beyond the noise |
| latency, mean (ms) | 1.68 | 1.68 | +0.2% | -0.023 to 0.0302 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.8 | -3.4% | -4.75 to 0.425 | no difference beyond the noise |
| memory used, mean (MB) | 57.1 | 55.7 | -2.6% | -3.29 to 0.375 | no difference beyond the noise |
| keys evicted | 71,705 | 71,778 | +0.1% | -278 to 425 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.117 | -5.9% | -0.0277 to 0.0131 | no difference beyond the noise |
| host CPU-seconds | 88 | 82.1 | -6.7% | -22.9 to 11.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.454 | 0.424 | -6.7% | -0.119 to 0.0583 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
