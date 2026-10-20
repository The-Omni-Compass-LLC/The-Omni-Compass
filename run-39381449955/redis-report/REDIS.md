# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.69 to 1.04 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0361 to 0.0548 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00106 to 0.000791 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.00394 to 0.00252 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% | 0.00349 to 0.0228 | LOSS |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% | -0.00731 to 0.0177 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.4 | -4.0% | -5.03 to -0.0932 | GAIN |
| memory used, mean (MB) | 57.2 | 55.5 | -3.0% | -4.17 to 0.791 | EVEN, no difference beyond the noise |
| keys evicted | 71,738 | 71,792 | +0.1% | -205 to 313 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.142 | -1.8% | -0.107 to 0.102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.1 | 95.7 | -2.5% | -86.4 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.494 | -2.5% | -0.445 to 0.42 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,287 | +1.6% | 17.3 to 24.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0124 to 0.0227 | EVEN, no difference beyond the noise |
| cache hit rate | 0.846 | 0.859 | +1.6% | 0.0118 to 0.0158 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% | -0.0156 to 0.00936 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.27 | -0.1% | -0.0344 to 0.0268 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.891 | 0.817 | -8.4% | -0.0891 to -0.0601 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.4% | 0.0726 to 3.06 | power given |
| memory used, mean (MB) | 61.3 | 62.5 | +1.9% | 0.678 to 1.66 | power given |
| keys evicted | 102,969 | 93,778 | -8.9% | -10,330 to -8,052 | shown, not judged |
| host CPU busy (share of the run) | 0.0668 | 0.0733 | +9.7% | -0.00916 to 0.0221 | EVEN, no difference beyond the noise |
| host CPU-seconds | 118 | 130 | +10.6% | -16.9 to 41.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.207 | 0.225 | +8.8% | -0.0322 to 0.0684 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 16.9 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.11 to 13.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0154 to 0.00746 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00605 to 0.00965 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0156 to 0.0119 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.81 | +1.2% | -0.209 to 0.343 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.6% | -0.0597 to -0.0149 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.3 to 1.47 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.864 to 1.47 | power given |
| keys evicted | 243,186 | 236,889 | -2.6% | -14,371 to 1,776 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.131 | -9.4% | -0.0316 to 0.00442 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 217 | -10.6% | -61.5 to 10.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.583 | 0.515 | -11.6% | -0.152 to 0.0164 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 6.08 to 21.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 8.96 to 16.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.024 to 0.00684 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00573 to 0.011 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.66 | +0.2% | -0.0289 to 0.0526 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.73 | +0.2% | -0.00758 to 0.0338 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.29 | 1.25 | -2.9% | -0.0684 to -0.00553 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66 | +3.1% | 0.713 to 3.25 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 0.455 to 2.22 | power given |
| keys evicted | 137,977 | 133,161 | -3.5% | -6,582 to -3,051 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | +0.1% | -0.0472 to 0.0473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 212 | -0.4% | -92.5 to 90.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.4 | 0.394 | -1.5% | -0.176 to 0.165 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
