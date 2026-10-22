# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.81 to 0.401 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0381 to 0.059 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00101 to 0.000113 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.0% | -0.00455 to 0.00242 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.78 | +0.2% | -0.0103 to 0.0305 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.73 | +0.3% | -0.00791 to 0.0186 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.2% | -4.53 to 0.444 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 56 | -2.0% | -3.66 to 1.33 | EVEN, no difference beyond the noise |
| keys evicted | 71,695 | 71,839 | +0.2% | 14.6 to 272 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.137 | -10.3% | -0.095 to 0.0635 | EVEN, no difference beyond the noise |
| host CPU-seconds | 106 | 94 | -11.3% | -71.9 to 48.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.547 | 0.485 | -11.2% | -0.372 to 0.249 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,280 | +1.1% | -3.07 to 31.8 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00169 to 0.00213 | EVEN, the same |
| cache hit rate | 0.845 | 0.854 | +1.1% | -0.00294 to 0.0223 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.7 | 5.68 | -0.4% | -0.126 to 0.0766 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.75 | -0.2% | -0.123 to 0.101 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.04 | 0.981 | -5.2% | -0.134 to 0.026 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.4 | +0.6% | -0.853 to 1.63 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -0.919 to 1.43 | EVEN, no difference beyond the noise |
| keys evicted | 103,468 | 97,176 | -6.1% | -14,762 to 2,178 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.138 | +8.7% | -0.029 to 0.0512 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 241 | +10.7% | -51.4 to 97.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.418 | +9.4% | -0.0929 to 0.165 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 9.32 to 30 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.1 to 14.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0384 to 0.0263 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00682 to 0.00949 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00523 to 0.00801 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.00699 to 0.0324 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.8% | -0.0471 to -0.0343 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.7% | 0.836 to 2.66 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.07 to 1.3 | power given |
| keys evicted | 243,132 | 236,386 | -2.8% | -10,054 to -3,438 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.143 | +2.7% | -0.0231 to 0.0307 | EVEN, no difference beyond the noise |
| host CPU-seconds | 232 | 240 | +3.4% | -47 to 62.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.558 | 0.569 | +2.0% | -0.12 to 0.143 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 11.5 to 17.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 0.833 to 18.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0958 to 0.157 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.000971 to 0.0122 | GAIN |
| latency, 95th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.00606 to 0.0122 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.78 | +0.2% | -0.00642 to 0.0336 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.3 | -2.3% | -0.0721 to 0.0107 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.278 to 2.14 | power given |
| memory used, mean (MB) | 61.2 | 62.1 | +1.4% | 0.203 to 1.55 | power given |
| keys evicted | 138,146 | 134,529 | -2.6% | -7,407 to 172 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.109 | -0.2% | -0.0588 to 0.0583 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 182 | +0.0% | -109 to 109 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.339 | -0.8% | -0.205 to 0.2 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
