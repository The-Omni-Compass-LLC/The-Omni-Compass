# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.15 to 0.782 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0393 to 0.0215 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00138 to 0.000474 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.62 | 5.63 | +0.2% | -0.0435 to 0.066 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.68 | +0.2% | -0.0306 to 0.0493 | no difference beyond the noise |
| latency, mean (ms) | 1.65 | 1.67 | +0.8% | -0.0316 to 0.0568 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -2.95 to -2.56 | better |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% | -1.95 to -1.69 | better |
| keys evicted | 71,660 | 71,788 | +0.2% | -159 to 415 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.107 | +5.3% | -0.0296 to 0.0404 | no difference beyond the noise |
| host CPU-seconds | 70 | 73.9 | +5.6% | -22.1 to 30 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.382 | +5.7% | -0.114 to 0.155 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,358 | +7.1% | 81.7 to 97.8 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00176 to 0.00147 | same |
| cache hit rate | 0.845 | 0.905 | +7.1% | 0.0545 to 0.0652 | better |
| latency, 95th percentile (ms) | 5.53 | 5.45 | -1.4% | -0.106 to -0.0477 | better |
| latency, 99th percentile (ms) | 5.65 | 5.62 | -0.5% | -0.0376 to -0.021 | better |
| latency, mean (ms) | 0.958 | 0.635 | -33.7% | -0.35 to -0.295 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 77.9 | +21.7% | 11 to 16.7 | **WORSE** |
| memory used, mean (MB) | 61.3 | 70.3 | +14.7% | 5.31 to 12.7 | **WORSE** |
| keys evicted | 103,134 | 63,197 | -38.7% | -43,810 to -36,064 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.102 | -2.6% | -0.0406 to 0.0352 | no difference beyond the noise |
| host CPU-seconds | 188 | 184 | -2.4% | -80.5 to 71.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.329 | 0.3 | -8.8% | -0.161 to 0.103 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 47.7 |  | 35.4 to 59.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 925 | -0.0% | -10.9 to 10.1 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0114 to 0.000292 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.617 | -0.0% | -0.00722 to 0.00672 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.52 | 5.51 | -0.2% | -0.0255 to 0.00138 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.58 | -0.1% | -0.0209 to 0.00622 | no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.14 | -0.2% | -0.0416 to 0.0331 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 69.2 | +8.2% | 0.512 to 9.94 | **WORSE** |
| memory used, mean (MB) | 60.7 | 63.5 | +4.6% | -3.16 to 8.7 | no difference beyond the noise |
| keys evicted | 243,151 | 247,083 | +1.6% | 977 to 6,888 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.109 | -2.4% | -0.0135 to 0.00811 | no difference beyond the noise |
| host CPU-seconds | 196 | 191 | -2.4% | -25.4 to 16 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.47 | 0.459 | -2.3% | -0.0601 to 0.0381 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.3 |  | 25.9 to 28.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,248 | +5.4% | 43.9 to 84.9 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0151 to 0.0196 | no difference beyond the noise |
| cache hit rate | 0.789 | 0.832 | +5.4% | 0.0292 to 0.0567 | better |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.2% | -0.0183 to -4.65e-05 | better |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.0108 to 0.0124 | no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.11 | -17.6% | -0.308 to -0.167 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 82.7 | +29.2% | 1.96 to 35.4 | **WORSE** |
| memory used, mean (MB) | 61.2 | 75.7 | +23.7% | 3.68 to 25.3 | **WORSE** |
| keys evicted | 138,098 | 110,491 | -20.0% | -37,995 to -17,219 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.114 | -6.2% | -0.0326 to 0.0176 | no difference beyond the noise |
| host CPU-seconds | 204 | 191 | -6.1% | -60.9 to 36 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.34 | -10.9% | -0.127 to 0.0432 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 46 |  | 17.3 to 74.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
