# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.74 to 0.653 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0057 to -0.000311 | **WORSE** |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00104 to 0.000435 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% | -0.0157 to 0.0195 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.63 | +0.1% | -0.0102 to 0.0218 | no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.63 | +0.2% | 0.00117 to 0.00682 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.3 | -4.1% | -2.99 to -2.31 | better |
| memory used, mean (MB) | 57.1 | 55.5 | -3.0% | -2.13 to -1.27 | better |
| keys evicted | 71,650 | 71,741 | +0.1% | -115 to 297 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.114 | +2.8% | -0.0698 to 0.076 | no difference beyond the noise |
| host CPU-seconds | 78.5 | 80.8 | +2.9% | -56.3 to 60.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.405 | 0.417 | +2.9% | -0.29 to 0.314 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,348 | +6.7% | 64.1 to 105 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0127 to 0.00179 | no difference beyond the noise |
| cache hit rate | 0.844 | 0.901 | +6.7% | 0.0421 to 0.0707 | better |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.2% | -0.0255 to 0.00311 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.24 | -0.2% | -0.0292 to 0.00909 | no difference beyond the noise |
| latency, mean (ms) | 0.894 | 0.601 | -32.7% | -0.368 to -0.217 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 76.4 | +19.4% | 4.31 to 20.6 | **WORSE** |
| memory used, mean (MB) | 61.3 | 69.5 | +13.4% | 5.2 to 11.2 | **WORSE** |
| keys evicted | 103,742 | 66,177 | -36.2% | -46,844 to -28,287 | shown, not judged |
| host CPU busy (share of the run) | 0.0581 | 0.0594 | +2.3% | -0.00875 to 0.0114 | no difference beyond the noise |
| host CPU-seconds | 102 | 105 | +2.9% | -16.1 to 22 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.18 | 0.174 | -3.7% | -0.0303 to 0.017 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 45.3 |  | 15 to 75.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 924 | -0.2% | -1.94 to -1.18 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.131 to 0.059 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.2% | -0.00114 to -0.000788 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0126 to 0.0182 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.00655 to 0.0294 | no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.27 | +0.4% | -0.00277 to 0.021 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.3% | 0.504 to 1.1 | **WORSE** |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.101 to 0.129 | **WORSE** |
| keys evicted | 243,197 | 243,905 | +0.3% | 597 to 819 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.155 | +14.7% | -0.0145 to 0.0542 | no difference beyond the noise |
| host CPU-seconds | 225 | 264 | +17.3% | -27.1 to 105 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.54 | 0.634 | +17.5% | -0.064 to 0.253 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,252 | +5.9% | 60 to 78.8 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00364 to 0.00546 | same |
| cache hit rate | 0.789 | 0.835 | +5.9% | 0.0397 to 0.0526 | better |
| latency, 95th percentile (ms) | 5.52 | 5.49 | -0.6% | -0.0559 to -0.0114 | better |
| latency, 99th percentile (ms) | 5.6 | 5.59 | -0.2% | -0.0285 to 0.00721 | no difference beyond the noise |
| latency, mean (ms) | 1.24 | 0.996 | -20.0% | -0.287 to -0.21 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 85.7 | +33.9% | 17.3 to 26.1 | **WORSE** |
| memory used, mean (MB) | 61.2 | 78.8 | +28.8% | 13.5 to 21.8 | **WORSE** |
| keys evicted | 138,277 | 107,939 | -21.9% | -34,681 to -25,995 | shown, not judged |
| host CPU busy (share of the run) | 0.0929 | 0.102 | +10.3% | 0.000434 to 0.0187 | **WORSE** |
| host CPU-seconds | 162 | 181 | +12.1% | 3.18 to 35.9 | **WORSE** |
| host CPU-seconds per 1,000 requests inside the line | 0.304 | 0.322 | +5.9% | -0.0158 to 0.0516 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 54.3 |  | 48.1 to 60.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 25.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
