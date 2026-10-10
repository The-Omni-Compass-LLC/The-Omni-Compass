# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.0% | -1.34 to 0.441 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0128 to 0.022 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000887 to 0.000304 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.56 | -0.2% | -0.0426 to 0.0199 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% | -0.0219 to 0.0209 | no difference beyond the noise |
| latency, mean (ms) | 1.6 | 1.6 | -0.1% | -0.0184 to 0.0155 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -3.53 to -1.98 | better |
| memory used, mean (MB) | 57.1 | 55.3 | -3.2% | -2.49 to -1.14 | better |
| keys evicted | 71,668 | 71,754 | +0.1% | -86.4 to 258 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.109 | +6.7% | -0.0894 to 0.103 | no difference beyond the noise |
| host CPU-seconds | 72.8 | 78.5 | +7.8% | -70.8 to 82.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.405 | +7.8% | -0.365 to 0.424 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | -17.4 to 58.5 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00675 to 0.00574 | same |
| cache hit rate | 0.845 | 0.859 | +1.6% | -0.0113 to 0.0388 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.0218 to 0.0371 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.82 | +0.3% | -0.0164 to 0.0526 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.984 | -6.5% | -0.212 to 0.0741 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64 | +0.0% | -3.34 to 3.38 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.9 | -0.7% | -3.47 to 2.62 | no difference beyond the noise |
| keys evicted | 103,325 | 94,452 | -8.6% | -25,245 to 7,500 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.122 | +3.4% | -0.029 to 0.037 | no difference beyond the noise |
| host CPU-seconds | 197 | 205 | +3.8% | -54.9 to 69.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.354 | +2.1% | -0.11 to 0.125 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.7 |  | 20.1 to 35.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 926 | +0.1% | -27.5 to 29.7 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0546 to 0.00937 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.618 | +0.1% | -0.0183 to 0.0196 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.1% | -0.00912 to 0.0145 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.33 | +1.1% | -0.049 to 0.17 | no difference beyond the noise |
| latency, mean (ms) | 2.04 | 2.04 | +0.0% | -0.0913 to 0.0924 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | -7.17 to 10.2 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 62.1 | +2.4% | -7.19 to 10.1 | no difference beyond the noise |
| keys evicted | 243,056 | 242,642 | -0.2% | -20,330 to 19,503 | shown, not judged |
| host CPU busy (share of the run) | 0.0646 | 0.0718 | +11.1% | -0.019 to 0.0334 | no difference beyond the noise |
| host CPU-seconds | 114 | 128 | +11.8% | -35.4 to 62.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.275 | 0.306 | +11.6% | -0.076 to 0.14 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 7.85 to 34.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,181 | -0.2% | -3.85 to -1.01 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00401 to 0.00271 | same |
| cache hit rate | 0.789 | 0.788 | -0.2% | -0.00248 to -0.000786 | **WORSE** |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00107 to 0.011 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | -0.00333 to 0.0275 | no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.36 | +1.0% | 0.00682 to 0.0191 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.5 | -0.8% | -2.41 to 1.4 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 60.8 | -0.7% | -1.95 to 1.07 | no difference beyond the noise |
| keys evicted | 138,149 | 140,340 | +1.6% | 469 to 3,913 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.122 | -5.9% | -0.031 to 0.0157 | no difference beyond the noise |
| host CPU-seconds | 218 | 203 | -6.9% | -60.2 to 30 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.382 | -6.7% | -0.112 to 0.0569 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 15.4 to 28.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
