# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,354 | +6.9% | 78.7 to 95.7 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00268 to 0.00286 | same |
| cache hit rate | 0.845 | 0.903 | +6.9% | 0.053 to 0.0635 | better |
| latency, 95th percentile (ms) | 5.51 | 5.45 | -1.1% | -0.0815 to -0.0404 | better |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.4% | -0.0297 to -0.0145 | better |
| latency, mean (ms) | 0.961 | 0.649 | -32.4% | -0.345 to -0.278 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 77 | +20.4% | 9.12 to 16.9 | **WORSE** |
| memory used, mean (MB) | 61.3 | 69.3 | +13.1% | 6.6 to 9.4 | **WORSE** |
| keys evicted | 103,348 | 64,594 | -37.5% | -42,600 to -34,909 | shown, not judged |
| host CPU busy (share of the run) | 0.0944 | 0.102 | +8.3% | -0.00626 to 0.0218 | no difference beyond the noise |
| host CPU-seconds | 164 | 181 | +9.9% | -10.1 to 42.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.289 | 0.297 | +2.8% | -0.0419 to 0.0581 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 49.3 |  | 44.2 to 54.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
