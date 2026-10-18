# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | -13.3 to 55 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0027 to 0.00285 | same |
| cache hit rate | 0.845 | 0.859 | +1.7% | -0.00892 to 0.0369 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.00456 to 0.00447 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | 0.00166 to 0.00708 | **WORSE** |
| latency, mean (ms) | 1.05 | 0.975 | -7.1% | -0.202 to 0.0536 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -5.21 to 6.49 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | -5.52 to 6.39 | no difference beyond the noise |
| keys evicted | 103,555 | 94,503 | -8.7% | -24,642 to 6,538 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.112 | +4.4% | -0.0348 to 0.0443 | no difference beyond the noise |
| host CPU-seconds | 179 | 188 | +5.1% | -65.3 to 83.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.314 | 0.324 | +3.4% | -0.114 to 0.135 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 8.49 to 39.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
