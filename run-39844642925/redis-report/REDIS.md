# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.37 to 0.713 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0173 to 0.0103 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00142 to 0.000431 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.72 | +0.0% | -0.00366 to 0.00386 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.78 | +0.2% | 0.00656 to 0.0122 | LOSS |
| latency, mean (ms) | 1.73 | 1.73 | +0.4% | 0.00257 to 0.0119 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.2% | -3.83 to -0.32 | GAIN |
| memory used, mean (MB) | 57.2 | 56 | -2.1% | -3.05 to 0.695 | EVEN, no difference beyond the noise |
| keys evicted | 71,683 | 71,834 | +0.2% | -97.3 to 401 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.13 | +8.5% | -0.031 to 0.0515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.8 | 87.5 | +9.6% | -23.6 to 39 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.412 | 0.452 | +9.7% | -0.122 to 0.202 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,290 | +1.8% | 19.4 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00263 to 0.00267 | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.8% | 0.0129 to 0.0169 | GAIN |
| latency, 95th percentile (ms) | 5.6 | 5.58 | -0.3% | -0.0232 to -0.00567 | GAIN |
| latency, 99th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0108 to 0.00518 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.981 | 0.899 | -8.3% | -0.0839 to -0.0793 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | -0.684 to 3.77 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% | -0.262 to 2.44 | EVEN, no difference beyond the noise |
| keys evicted | 103,178 | 93,244 | -9.6% | -11,592 to -8,277 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.107 | -5.6% | -0.045 to 0.0324 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 190 | -6.0% | -89 to 64.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.328 | -7.7% | -0.16 to 0.106 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 17.5 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 938 | +1.3% | 11.5 to 12.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0234 to 0.0181 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00768 to 0.00872 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.0% | -0.0157 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.77 | +0.2% | -0.00874 to 0.0285 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.9% | -0.0499 to -0.0347 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.8% | 0.972 to 2.58 | power given |
| memory used, mean (MB) | 60.7 | 61.7 | +1.6% | 0.481 to 1.51 | power given |
| keys evicted | 243,273 | 238,280 | -2.1% | -12,565 to 2,579 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.151 | -1.2% | -0.0505 to 0.0467 | EVEN, no difference beyond the noise |
| host CPU-seconds | 258 | 255 | -1.3% | -98.3 to 91.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.62 | 0.604 | -2.6% | -0.243 to 0.211 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 8.39 to 25.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.1% | 7.03 to 19 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0353 to 0.0566 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.0046 to 0.0125 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.21 | -0.3% | -0.0658 to 0.0374 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.53 | 5.25 | -5.1% | -1.49 to 0.923 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.12 | -4.9% | -0.112 to -0.00262 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.268 to 2.66 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.206 to 2.04 | power given |
| keys evicted | 138,082 | 133,144 | -3.6% | -7,578 to -2,298 | shown, not judged |
| host CPU busy (share of the run) | 0.0566 | 0.0605 | +7.0% | -0.00878 to 0.0167 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99 | 107 | +7.9% | -16.4 to 32 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.186 | 0.199 | +6.7% | -0.0328 to 0.0579 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
