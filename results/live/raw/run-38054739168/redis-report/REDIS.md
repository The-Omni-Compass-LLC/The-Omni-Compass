# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% | -1.7 to 1.06 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00782 to 0.00149 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.0011 to 0.000718 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.63 | 5.63 | +0.0% | -0.00662 to 0.00917 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | 0.00216 to 0.0119 | **WORSE** |
| latency, mean (ms) | 1.65 | 1.66 | +0.3% | -0.0059 to 0.0151 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.2% | -4.59 to 0.53 | no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.9 | -2.2% | -2.84 to 0.364 | no difference beyond the noise |
| keys evicted | 71,692 | 71,755 | +0.1% | -179 to 305 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.125 | +8.0% | -0.0401 to 0.0587 | no difference beyond the noise |
| host CPU-seconds | 82.4 | 89.7 | +8.7% | -33.6 to 48 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.425 | 0.463 | +8.8% | -0.173 to 0.248 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,301 | +2.9% | 23.4 to 49.3 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000312 to 0.00271 | same |
| cache hit rate | 0.844 | 0.868 | +2.9% | 0.0166 to 0.0321 | better |
| latency, 95th percentile (ms) | 5.65 | 5.61 | -0.6% | -0.0887 to 0.0154 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.76 | -0.9% | -0.259 to 0.156 | no difference beyond the noise |
| latency, mean (ms) | 1.04 | 0.898 | -13.4% | -0.214 to -0.0648 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.7% | -0.237 to 3.75 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +0.9% | -0.981 to 2.1 | no difference beyond the noise |
| keys evicted | 103,930 | 88,150 | -15.2% | -21,020 to -10,540 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.13 | +6.2% | -0.0147 to 0.0299 | no difference beyond the noise |
| host CPU-seconds | 215 | 232 | +8.0% | -31.7 to 66.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.377 | 0.396 | +5.0% | -0.0653 to 0.103 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33 |  | 30.5 to 35.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 927 | +0.1% | -9.45 to 11 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.024 to 0.00966 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.618 | +0.1% | -0.00623 to 0.00739 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00103 to 0.00632 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.2% | 0.00191 to 0.0212 | **WORSE** |
| latency, mean (ms) | 2.26 | 2.26 | -0.0% | -0.0396 to 0.039 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.8% | -0.601 to 2.86 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.9 | +0.4% | -0.342 to 0.834 | no difference beyond the noise |
| keys evicted | 243,139 | 243,876 | +0.3% | 391 to 1,084 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.134 | -8.7% | -0.0446 to 0.0192 | no difference beyond the noise |
| host CPU-seconds | 247 | 222 | -10.1% | -86.2 to 36.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.592 | 0.532 | -10.2% | -0.211 to 0.0901 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,236 | +4.4% | 31.1 to 72.4 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00293 to 0.00249 | same |
| cache hit rate | 0.789 | 0.824 | +4.4% | 0.0208 to 0.0483 | better |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0179 to 0.00753 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0107 to 0.0177 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.15 | -14.0% | -0.27 to -0.107 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.3 | +19.2% | 4.38 to 20.2 | **WORSE** |
| memory used, mean (MB) | 61.2 | 71.2 | +16.3% | 2.74 to 17.2 | **WORSE** |
| keys evicted | 138,104 | 116,177 | -15.9% | -30,035 to -13,819 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.113 | -8.1% | -0.0401 to 0.0203 | no difference beyond the noise |
| host CPU-seconds | 205 | 187 | -8.6% | -76 to 40.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.385 | 0.337 | -12.5% | -0.151 to 0.0551 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 36.7 |  | 27.9 to 45.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
