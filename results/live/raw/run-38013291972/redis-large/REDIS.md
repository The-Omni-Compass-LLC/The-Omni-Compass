# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,294 | +2.1% | 25.6 to 28.2 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00139 to 0.00164 | same |
| cache hit rate | 0.845 | 0.863 | +2.1% | 0.0171 to 0.0188 | better |
| latency, 95th percentile (ms) | 5.63 | 5.61 | -0.4% | -0.032 to -0.0118 | better |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.0175 to 0.00328 | no difference beyond the noise |
| latency, mean (ms) | 0.987 | 0.888 | -10.1% | -0.107 to -0.0918 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -0.0666 to 0.647 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.3 | +0.0% | -0.708 to 0.715 | no difference beyond the noise |
| keys evicted | 103,397 | 91,719 | -11.3% | -12,322 to -11,036 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.0934 | -21.1% | -0.0436 to -0.00643 | better |
| host CPU-seconds | 211 | 162 | -23.1% | -85.8 to -11.6 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.37 | 0.279 | -24.7% | -0.157 to -0.026 | better |
| ceiling changes written (the knob's moves) | 0 | 27 |  | 20.4 to 33.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 13.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
