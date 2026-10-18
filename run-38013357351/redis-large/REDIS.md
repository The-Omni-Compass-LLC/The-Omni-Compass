# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,295 | +2.3% | 20.7 to 37 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00281 to 0.000242 | same |
| cache hit rate | 0.845 | 0.864 | +2.3% | 0.014 to 0.0241 | better |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.0272 to 0.0382 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% | -0.0195 to 0.0496 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.948 | -9.6% | -0.136 to -0.0665 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | -2.1 to 4.87 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.3 | +1.6% | -3.33 to 5.28 | no difference beyond the noise |
| keys evicted | 103,554 | 91,070 | -12.1% | -15,470 to -9,498 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | -0.2% | -0.0179 to 0.0175 | no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.2% | -35.2 to 34.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.353 | -2.4% | -0.0691 to 0.0514 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.7 |  | 8.86 to 46.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
