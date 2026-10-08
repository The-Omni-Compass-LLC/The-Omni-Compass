# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,046 | 1,191 | +13.9% | 117 to 174 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0558 to 0.128 | no difference beyond the noise |
| cache hit rate | 0.698 | 0.794 | +13.9% | 0.0775 to 0.116 | better |
| latency, 95th percentile (ms) | 5.7 | 5.68 | -0.3% | -0.0225 to -0.0134 | better |
| latency, 99th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.00722 to -0.00531 | better |
| latency, mean (ms) | 1.83 | 1.29 | -29.4% | -0.648 to -0.429 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 195 | +204.9% | 89 to 173 | **WORSE** |
| memory used, mean (MB) | 56.9 | 154 | +171.1% | 77 to 118 | **WORSE** |
| keys evicted | 49,909 | 11,212 | -77.5% | -43,997 to -33,397 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.137 | -8.5% | -0.0575 to 0.0322 | no difference beyond the noise |
| host CPU-seconds | 69.2 | 63.7 | -8.0% | -29.7 to 18.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.551 | 0.446 | -19.2% | -0.28 to 0.0682 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.7 |  | 11.4 to 48 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 10.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,252 | 1,424 | +13.7% | 167 to 177 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00163 to 0.00132 | same |
| cache hit rate | 0.835 | 0.95 | +13.7% | 0.111 to 0.118 | better |
| latency, 95th percentile (ms) | 5.63 | 5.27 | -6.5% | -0.38 to -0.352 | better |
| latency, 99th percentile (ms) | 5.73 | 5.67 | -1.1% | -0.0783 to -0.0512 | better |
| latency, mean (ms) | 1.04 | 0.407 | -60.7% | -0.651 to -0.608 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 252 | +294.2% | 181 to 196 | **WORSE** |
| memory used, mean (MB) | 61.3 | 217 | +254.6% | 148 to 164 | **WORSE** |
| keys evicted | 73,077 | 17,809 | -75.6% | -57,067 to -53,468 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0913 | -17.4% | -0.0519 to 0.0133 | no difference beyond the noise |
| host CPU-seconds | 130 | 107 | -17.5% | -65 to 19.4 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.347 | 0.251 | -27.5% | -0.19 to 5.6e-05 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 161 |  | 160 to 163 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 30.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 831 | 1,051 | +26.6% | 207 to 234 | better |
| throughput (requests a second) | 1,499 | 1,499 | +0.0% | -0.0304 to 0.0401 | no difference beyond the noise |
| cache hit rate | 0.555 | 0.702 | +26.5% | 0.139 to 0.156 | better |
| latency, 95th percentile (ms) | 5.73 | 5.71 | -0.4% | -0.029 to -0.0172 | better |
| latency, 99th percentile (ms) | 6.68 | 6.35 | -4.9% | -0.809 to 0.156 | no difference beyond the noise |
| latency, mean (ms) | 2.65 | 1.84 | -30.7% | -0.874 to -0.75 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 272 | +325.0% | 197 to 219 | **WORSE** |
| memory used, mean (MB) | 60.3 | 212 | +250.8% | 148 to 155 | **WORSE** |
| keys evicted | 185,155 | 15,258 | -91.8% | -182,670 to -157,125 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.138 | -11.7% | -0.0434 to 0.00695 | no difference beyond the noise |
| host CPU-seconds | 174 | 154 | -11.4% | -52.7 to 13.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.698 | 0.488 | -30.0% | -0.348 to -0.0701 | better |
| ceiling changes written (the knob's moves) | 0 | 48 |  | 38.1 to 57.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `467f73eba7a6`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,131 | 1,304 | +15.3% | 162 to 184 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000687 to 0.00354 | same |
| cache hit rate | 0.754 | 0.869 | +15.3% | 0.108 to 0.123 | better |
| latency, 95th percentile (ms) | 5.55 | 5.48 | -1.3% | -0.0898 to -0.0582 | better |
| latency, 99th percentile (ms) | 5.61 | 5.59 | -0.3% | -0.0213 to -0.0163 | better |
| latency, mean (ms) | 1.43 | 0.814 | -43.2% | -0.66 to -0.577 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 297 | +364.0% | 231 to 235 | **WORSE** |
| memory used, mean (MB) | 61.1 | 267 | +337.7% | 204 to 209 | **WORSE** |
| keys evicted | 106,679 | 29,909 | -72.0% | -78,173 to -75,367 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0883 | -17.8% | -0.0797 to 0.0414 | no difference beyond the noise |
| host CPU-seconds | 126 | 103 | -18.3% | -101 to 54.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.371 | 0.263 | -29.1% | -0.324 to 0.107 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 98.7 |  | 97.2 to 100 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
