# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -3.02 to 1.77 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.183 to 0.294 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00201 to 0.00109 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.56 | 5.56 | -0.0% | -0.00358 to 0.00341 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.62 | +0.0% | -0.00457 to 0.00823 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.63 | +0.3% | -0.00769 to 0.0168 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.76 to -1.5 | GAIN |
| memory used, mean (MB) | 57.1 | 56.5 | -1.2% | -0.889 to -0.474 | GAIN |
| keys evicted | 71,648 | 71,782 | +0.2% | -243 to 512 | shown, not judged |
| host CPU busy (share of the run) | 0.092 | 0.105 | +13.8% | -0.0797 to 0.105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63.6 | 73.1 | +15.1% | -60.9 to 80.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.328 | 0.378 | +15.2% | -0.314 to 0.413 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% | 7.73 to 17.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00281 to 0.00505 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | 0.00503 to 0.0121 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.00754 to 0.00157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | 0.000736 to 0.00555 | LOSS |
| latency, mean (ms) | 1.05 | 1 | -4.3% | -0.0635 to -0.0269 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.3 | -1.1% | -2.35 to 0.991 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 59.7 | -2.6% | -2.87 to -0.295 | GAIN |
| keys evicted | 103,529 | 98,185 | -5.2% | -8,154 to -2,533 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.118 | -0.5% | -0.0422 to 0.041 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 199 | -0.4% | -79.5 to 78.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.35 | 0.345 | -1.4% | -0.143 to 0.133 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 31 |  | 22.4 to 39.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 24.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 936 | +1.2% | 10.4 to 11.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00951 to 0.0173 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00712 to 0.00791 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | -0.0% | -0.00593 to 0.00442 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | +0.1% | -0.00427 to 0.0189 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.11 | -1.8% | -0.0393 to -0.0365 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 1.14 to 1.57 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.12 to 1.37 | power given |
| keys evicted | 243,137 | 235,991 | -2.9% | -11,967 to -2,324 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.116 | +0.9% | -0.0229 to 0.0251 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 203 | +1.2% | -45.4 to 50.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.481 | 0.482 | +0.0% | -0.113 to 0.113 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.3 |  | 3.93 to 22.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 4.59 to 13.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0133 to 0.0132 | EVEN, the same |
| cache hit rate | 0.79 | 0.796 | +0.8% | 0.00314 to 0.00885 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.0% | -0.0163 to 0.011 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.0175 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.3% | -0.0465 to -0.0145 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.117 to 2.06 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | -0.254 to 1.8 | EVEN, no difference beyond the noise |
| keys evicted | 138,058 | 135,106 | -2.1% | -5,185 to -720 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.12 | -0.6% | -0.0712 to 0.0698 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 200 | -0.4% | -132 to 131 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.377 | 0.373 | -1.1% | -0.251 to 0.242 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 13.1 to 25.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
