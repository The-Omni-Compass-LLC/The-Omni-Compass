# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% | -3.16 to 2.16 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0228 to 0.0143 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00201 to 0.00132 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | +0.0% | -0.00989 to 0.0156 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.83 | +0.2% | 0.0082 to 0.014 | **WORSE** |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% | -0.00437 to 0.015 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.4% | -3.35 to -2.25 | better |
| memory used, mean (MB) | 57.2 | 55.3 | -3.3% | -2.45 to -1.29 | better |
| keys evicted | 71,654 | 71,773 | +0.2% | -305 to 542 | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.143 | -2.1% | -0.0695 to 0.0635 | no difference beyond the noise |
| host CPU-seconds | 98.9 | 96.6 | -2.3% | -54.8 to 50.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.51 | 0.499 | -2.3% | -0.283 to 0.26 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

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

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 927 | +0.1% | -10.3 to 12.5 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0121 to 0.0128 | same |
| cache hit rate | 0.617 | 0.618 | +0.1% | -0.00684 to 0.00842 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.0% | -0.00336 to 0.00663 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.2% | 0.00197 to 0.0178 | **WORSE** |
| latency, mean (ms) | 2.26 | 2.26 | -0.1% | -0.0453 to 0.0409 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.266 to 2.74 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.9 | +0.4% | -0.351 to 0.832 | no difference beyond the noise |
| keys evicted | 243,257 | 243,837 | +0.2% | 52.2 to 1,108 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.148 | +7.7% | 0.00339 to 0.0177 | **WORSE** |
| host CPU-seconds | 229 | 250 | +9.1% | 7.03 to 34.5 | **WORSE** |
| host CPU-seconds per 1,000 requests inside the line | 0.55 | 0.599 | +9.0% | 0.00922 to 0.0893 | **WORSE** |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 20.5 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,254 | +5.9% | 59.5 to 80.7 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00184 to 0.00183 | same |
| cache hit rate | 0.79 | 0.836 | +5.9% | 0.0397 to 0.0539 | better |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.1% | -0.00567 to -0.000714 | better |
| latency, 99th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.00695 to 0.00475 | no difference beyond the noise |
| latency, mean (ms) | 1.14 | 0.902 | -21.0% | -0.273 to -0.205 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 86.1 | +34.5% | 16.8 to 27.4 | **WORSE** |
| memory used, mean (MB) | 61.2 | 79.6 | +30.1% | 12.3 to 24.5 | **WORSE** |
| keys evicted | 137,987 | 107,544 | -22.1% | -35,718 to -25,169 | shown, not judged |
| host CPU busy (share of the run) | 0.0416 | 0.0517 | +24.3% | -0.023 to 0.0432 | no difference beyond the noise |
| host CPU-seconds | 72.8 | 91.5 | +25.8% | -41.8 to 79.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.137 | 0.162 | +18.7% | -0.0833 to 0.134 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 38.7 |  | 22.9 to 54.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
