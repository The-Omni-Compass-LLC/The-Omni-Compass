# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.934 to 0.56 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0075 to 0.0082 | EVEN, the same |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000856 to 0.000708 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% | -0.0136 to 0.021 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.0106 to 0.0379 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.3% | -0.00376 to 0.0144 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.4% | -1.96 to -1.12 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.1% | -1.01 to -0.242 | GAIN |
| keys evicted | 71,754 | 71,790 | +0.0% | -155 to 226 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.147 | -2.9% | -0.0128 to 0.00406 | EVEN, no difference beyond the noise |
| host CPU-seconds | 103 | 99.1 | -3.5% | -10.8 to 3.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.53 | 0.512 | -3.4% | -0.0552 to 0.0188 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,265 | 1,282 | +1.4% | 9.87 to 24.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00127 to 0.00243 | EVEN, the same |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00683 to 0.0159 | GAIN |
| latency, 95th percentile (ms) | 5.24 | 5.22 | -0.2% | -0.0613 to 0.0365 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.39 | 5.28 | -2.1% | -0.594 to 0.368 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.9 | 0.831 | -7.6% | -0.0985 to -0.0384 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.3% | 0.211 to 1.45 | power given |
| memory used, mean (MB) | 61.3 | 61.6 | +0.6% | -0.591 to 1.29 | EVEN, no difference beyond the noise |
| keys evicted | 103,523 | 96,008 | -7.3% | -10,344 to -4,688 | shown, not judged |
| host CPU busy (share of the run) | 0.0658 | 0.0681 | +3.6% | -0.00196 to 0.00668 | EVEN, no difference beyond the noise |
| host CPU-seconds | 116 | 121 | +4.5% | -2.34 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.203 | 0.21 | +3.1% | -0.00671 to 0.0195 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 17.5 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 11.2 to 12.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.154 to 0.248 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00729 to 0.00864 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00142 to 0.00661 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.000737 to 0.0308 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0478 to -0.0313 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.34 to 1.44 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.784 to 1.52 | power given |
| keys evicted | 243,183 | 236,802 | -2.6% | -15,282 to 2,520 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.142 | +3.8% | -0.0579 to 0.0682 | EVEN, no difference beyond the noise |
| host CPU-seconds | 229 | 239 | +4.5% | -113 to 133 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.549 | 0.566 | +3.2% | -0.276 to 0.311 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.3 |  | 11.9 to 14.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,194 | +0.9% | 9.85 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0185 to 0.0131 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00697 to 0.00803 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.64 | -0.1% | -0.0135 to 0.00575 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.75 | +0.2% | -0.0139 to 0.0357 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.31 | 1.27 | -3.0% | -0.0466 to -0.0327 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.9 | +2.9% | 1.05 to 2.68 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.891 to 1.62 | power given |
| keys evicted | 138,199 | 133,964 | -3.1% | -4,598 to -3,873 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.127 | +1.0% | -0.0207 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 222 | 225 | +1.2% | -42.6 to 48.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.417 | 0.418 | +0.3% | -0.0845 to 0.0869 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 17.5 to 23.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
