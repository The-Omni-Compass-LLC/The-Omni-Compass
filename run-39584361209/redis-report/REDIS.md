# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -2.55 to 1.49 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0375 to 0.0185 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00169 to 0.000991 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% | -0.00254 to 0.0094 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.83 | +0.3% | -0.0145 to 0.0461 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.2% | -0.0117 to 0.0203 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -2.07 to -1.07 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.1% | -1.15 to -0.146 | GAIN |
| keys evicted | 71,745 | 71,858 | +0.2% | -248 to 474 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.129 | +6.2% | -0.0564 to 0.0714 | EVEN, no difference beyond the noise |
| host CPU-seconds | 80.4 | 86.1 | +7.1% | -43.1 to 54.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.415 | 0.445 | +7.1% | -0.223 to 0.282 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 10.3 to 24.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00402 to 0.00231 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.00682 to 0.0161 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.00868 to 0.00815 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.24 | +0.0% | -0.0101 to 0.0151 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.87 | 0.812 | -6.7% | -0.0832 to -0.0332 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -0.167 to 1.71 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | -0.811 to 1.84 | EVEN, no difference beyond the noise |
| keys evicted | 103,176 | 95,658 | -7.3% | -10,641 to -4,394 | shown, not judged |
| host CPU busy (share of the run) | 0.0586 | 0.0603 | +2.9% | -0.00925 to 0.0127 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 107 | +3.2% | -17.4 to 23.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.181 | 0.185 | +1.8% | -0.032 to 0.0386 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 16.8 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.4 to 13.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0356 to 0.0256 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00688 to 0.00932 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0165 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.0115 to 0.0312 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.058 to -0.0209 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 0.694 to 2.76 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.933 to 1.38 | power given |
| keys evicted | 243,176 | 237,519 | -2.3% | -12,905 to 1,590 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.14 | -0.3% | -0.0347 to 0.0339 | EVEN, no difference beyond the noise |
| host CPU-seconds | 236 | 235 | -0.2% | -64.8 to 63.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.566 | 0.558 | -1.5% | -0.162 to 0.145 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 10.2 to 20.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 5.71 to 14.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00517 to 0.0114 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00405 to 0.00925 | GAIN |
| latency, 95th percentile (ms) | 5.72 | 5.72 | +0.0% | -0.00341 to 0.00354 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.79 | +0.1% | -0.0018 to 0.0149 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.6% | -0.0529 to -0.0163 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.129 to 2.3 | power given |
| memory used, mean (MB) | 61.2 | 62.1 | +1.6% | 0.274 to 1.63 | power given |
| keys evicted | 138,124 | 134,463 | -2.7% | -5,404 to -1,919 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.134 | +13.0% | -0.0388 to 0.0696 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 228 | +15.1% | -73.9 to 134 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.372 | 0.425 | +14.1% | -0.142 to 0.247 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 12.6 to 24.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
