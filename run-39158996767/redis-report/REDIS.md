# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.71 to -0.257 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0378 to 0.0229 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00109 to 2.07e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | +0.0% | -0.00456 to 0.00755 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.84 | +0.3% | 0.00257 to 0.0268 | LOSS |
| latency, mean (ms) | 1.75 | 1.76 | +0.5% | 0.000874 to 0.0159 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.3% | -3.95 to -0.316 | GAIN |
| memory used, mean (MB) | 57.2 | 56 | -2.1% | -3.04 to 0.66 | EVEN, no difference beyond the noise |
| keys evicted | 71,740 | 71,902 | +0.2% | -8.44 to 332 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.12 | +3.6% | -0.0664 to 0.0747 | EVEN, no difference beyond the noise |
| host CPU-seconds | 75.3 | 78.7 | +4.6% | -49.6 to 56.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.407 | +4.7% | -0.255 to 0.292 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 11 to 29.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000191 to 0.00152 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.6% | 0.00732 to 0.0202 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0138 to 0.00217 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.00907 to 0.00969 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.975 | -7.0% | -0.11 to -0.036 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.0994 to 2.27 | power given |
| memory used, mean (MB) | 61.3 | 62.2 | +1.4% | 0.304 to 1.41 | power given |
| keys evicted | 103,524 | 94,462 | -8.8% | -13,391 to -4,734 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.117 | -1.5% | -0.0219 to 0.0183 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 196 | -1.6% | -42.3 to 36.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.35 | 0.339 | -3.1% | -0.0767 to 0.0549 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 16.9 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 11.2 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0159 to 0.00648 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.0075 to 0.00832 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.69 | +0.1% | 0.00103 to 0.00561 | LOSS |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.00419 to 0.0221 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0407 to -0.0368 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.26 to 2.01 | power given |
| memory used, mean (MB) | 60.7 | 61.7 | +1.7% | 0.559 to 1.5 | power given |
| keys evicted | 243,132 | 238,693 | -1.8% | -12,947 to 4,070 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.145 | +6.4% | -0.0176 to 0.0351 | EVEN, no difference beyond the noise |
| host CPU-seconds | 228 | 245 | +7.7% | -32.7 to 67.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.546 | 0.581 | +6.4% | -0.0841 to 0.154 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 10.2 to 20.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,191 | +0.6% | 2.23 to 13 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00332 to 0.00316 | EVEN, the same |
| cache hit rate | 0.789 | 0.794 | +0.6% | 0.0011 to 0.00904 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.0% | -0.00362 to 0.00614 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | 0.00495 to 0.0129 | LOSS |
| latency, mean (ms) | 1.35 | 1.33 | -1.9% | -0.0516 to 0.000528 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -0.349 to 1.59 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.6 | +0.6% | -0.42 to 1.21 | EVEN, no difference beyond the noise |
| keys evicted | 138,331 | 136,283 | -1.5% | -5,230 to 1,133 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.13 | +6.8% | -0.0567 to 0.0732 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 219 | +7.5% | -109 to 140 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.408 | +6.8% | -0.209 to 0.262 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 8.46 to 30.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
