# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -3.31 to 2.24 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0204 to 0.00645 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00082 to 0.000249 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.1% | -0.00143 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.25 | +0.2% | -0.0217 to 0.0432 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.52 | 1.53 | +0.8% | -0.0344 to 0.0579 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.74 to -1.07 | GAIN |
| memory used, mean (MB) | 57.1 | 56.7 | -0.8% | -0.844 to -0.122 | GAIN |
| keys evicted | 71,639 | 71,734 | +0.1% | -83.6 to 274 | shown, not judged |
| host CPU busy (share of the run) | 0.0414 | 0.0435 | +5.0% | -0.0584 to 0.0626 | EVEN, no difference beyond the noise |
| host CPU-seconds | 28.7 | 30.2 | +5.2% | -42.2 to 45.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.148 | 0.156 | +5.3% | -0.218 to 0.234 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 18.3 to 22.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00281 to 0.00312 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0123 to 0.0153 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0193 to -0.00437 | GAIN |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.1% | -0.0249 to 0.0118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.983 | -7.2% | -0.0896 to -0.0625 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.2% | -0.169 to 1.77 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | 0.0297 to 0.981 | power given |
| keys evicted | 103,471 | 94,379 | -8.8% | -10,158 to -8,026 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.122 | -2.2% | -0.0196 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 206 | -2.0% | -37.4 to 28.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.356 | -3.6% | -0.0706 to 0.0442 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 27.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 10.2 to 13 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0368 to 0.0203 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00688 to 0.00872 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.00345 to 0.00213 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00272 to 0.0171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.8% | -0.0484 to -0.0337 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.38 to 1.48 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.781 to 1.52 | power given |
| keys evicted | 243,173 | 236,903 | -2.6% | -14,837 to 2,297 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.141 | +1.5% | -0.0457 to 0.0498 | EVEN, no difference beyond the noise |
| host CPU-seconds | 234 | 238 | +1.6% | -88.6 to 96.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.563 | +0.4% | -0.22 to 0.224 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,196 | +1.0% | 4.31 to 18.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0012 to 0.00446 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.797 | +1.0% | 0.00286 to 0.0126 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.00998 to 0.00881 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.00225 to 0.0136 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.3 | -3.0% | -0.0709 to -0.00838 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.372 to 2.57 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.177 to 2.05 | power given |
| keys evicted | 138,003 | 133,602 | -3.2% | -7,683 to -1,120 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.142 | +5.6% | -0.0482 to 0.0632 | EVEN, no difference beyond the noise |
| host CPU-seconds | 229 | 243 | +6.4% | -97.4 to 126 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.429 | 0.452 | +5.3% | -0.184 to 0.23 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 14.6 to 26.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
