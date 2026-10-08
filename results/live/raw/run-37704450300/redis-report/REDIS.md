# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,200 | +14.7% | 118 to 190 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0744 to 0.127 | no difference beyond the noise |
| cache hit rate | 0.698 | 0.8 | +14.7% | 0.0796 to 0.126 | better |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0172 to -0.00676 | better |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.0% | -0.0301 to 0.0243 | no difference beyond the noise |
| latency, mean (ms) | 1.86 | 1.3 | -30.5% | -0.711 to -0.426 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 201 | +214.6% | 93.3 to 181 | **WORSE** |
| memory used, mean (MB) | 56.9 | 156 | +173.6% | 76.8 to 121 | **WORSE** |
| keys evicted | 49,913 | 9,703 | -80.6% | -46,280 to -34,140 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.129 | -8.7% | -0.055 to 0.0305 | no difference beyond the noise |
| host CPU-seconds | 63.2 | 58.1 | -8.1% | -27.5 to 17.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.504 | 0.404 | -19.9% | -0.269 to 0.068 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 33 |  | 12.7 to 53.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 11.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,251 | 1,425 | +13.9% | 172 to 176 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00208 to 0.00477 | same |
| cache hit rate | 0.834 | 0.95 | +13.9% | 0.115 to 0.117 | better |
| latency, 95th percentile (ms) | 5.75 | 2.52 | -56.1% | -9.76 to 3.31 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.78 | -0.6% | -0.0367 to -0.0319 | better |
| latency, mean (ms) | 1.11 | 0.469 | -57.9% | -0.647 to -0.641 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 256 | +300.7% | 190 to 195 | **WORSE** |
| memory used, mean (MB) | 61.2 | 222 | +262.0% | 158 to 163 | **WORSE** |
| keys evicted | 73,285 | 17,277 | -76.4% | -56,757 to -55,259 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.0928 | -15.6% | -0.0289 to -0.00544 | better |
| host CPU-seconds | 121 | 103 | -15.0% | -32.7 to -3.66 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.322 | 0.24 | -25.4% | -0.118 to -0.0454 | better |
| ceiling changes written (the knob's moves) | 0 | 159 |  | 157 to 161 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 30.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 832 | 1,049 | +26.0% | 214 to 220 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00375 to 0.00706 | better |
| cache hit rate | 0.555 | 0.7 | +26.1% | 0.143 to 0.147 | better |
| latency, 95th percentile (ms) | 5.64 | 5.6 | -0.6% | -0.046 to -0.0214 | better |
| latency, 99th percentile (ms) | 5.7 | 5.68 | -0.3% | -0.0294 to -0.00766 | better |
| latency, mean (ms) | 2.54 | 1.75 | -31.1% | -0.79 to -0.787 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 270 | +322.5% | 198 to 215 | **WORSE** |
| memory used, mean (MB) | 60.3 | 211 | +249.2% | 150 to 151 | **WORSE** |
| keys evicted | 185,038 | 16,311 | -91.2% | -173,975 to -163,478 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.125 | -12.5% | -0.0218 to -0.0141 | better |
| host CPU-seconds | 170 | 148 | -12.7% | -26.4 to -16.6 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.68 | 0.471 | -30.7% | -0.235 to -0.183 | better |
| ceiling changes written (the knob's moves) | 0 | 50.3 |  | 34.4 to 66.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,304 | +15.3% | 161 to 186 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00538 to 0.00855 | no difference beyond the noise |
| cache hit rate | 0.754 | 0.87 | +15.3% | 0.107 to 0.124 | better |
| latency, 95th percentile (ms) | 5.62 | 5.57 | -1.0% | -0.092 to -0.018 | better |
| latency, 99th percentile (ms) | 5.69 | 5.67 | -0.3% | -0.0433 to 0.00656 | no difference beyond the noise |
| latency, mean (ms) | 1.46 | 0.836 | -42.9% | -0.674 to -0.584 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 299 | +366.6% | 233 to 236 | **WORSE** |
| memory used, mean (MB) | 61.1 | 269 | +340.6% | 207 to 209 | **WORSE** |
| keys evicted | 106,700 | 28,696 | -73.1% | -80,859 to -75,148 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.097 | -18.4% | -0.0402 to -0.00364 | better |
| host CPU-seconds | 141 | 114 | -19.1% | -52.2 to -1.44 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.414 | 0.29 | -29.9% | -0.191 to -0.0561 | better |
| ceiling changes written (the knob's moves) | 0 | 97 |  | 92.7 to 101 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
