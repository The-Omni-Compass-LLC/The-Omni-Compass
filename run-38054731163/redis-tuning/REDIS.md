# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,242 | +4.9% | 45 to 72.1 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00094 to 0.00422 | better |
| cache hit rate | 0.79 | 0.829 | +5.0% | 0.0301 to 0.048 | better |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0191 to -0.000388 | better |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% | -0.0177 to 0.0132 | no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.13 | -16.0% | -0.271 to -0.161 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 80.4 | +25.7% | 5.37 to 27.5 | **WORSE** |
| memory used, mean (MB) | 61.2 | 73.8 | +20.7% | 4.81 to 20.5 | **WORSE** |
| keys evicted | 138,054 | 113,055 | -18.1% | -31,376 to -18,621 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.117 | -7.9% | -0.0414 to 0.0214 | no difference beyond the noise |
| host CPU-seconds | 213 | 195 | -8.2% | -77.7 to 42.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.399 | 0.349 | -12.5% | -0.164 to 0.0639 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 41.7 |  | 21 to 62.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
