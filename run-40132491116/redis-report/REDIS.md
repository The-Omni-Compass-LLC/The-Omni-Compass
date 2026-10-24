# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.065 to 0.039 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0117 to 0.00752 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -1.53e-05 to 1.28e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0327 to 0.00508 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.67 | -0.1% | -0.0202 to 0.0107 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.734 | 0.732 | -0.3% | -0.00607 to 0.00197 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00406 to 0.0671 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0822 | 0.117 | +42.3% | -0.0138 to 0.0834 | EVEN, no difference beyond the noise |
| host CPU-seconds | 57.8 | 85.4 | +47.9% | -10.8 to 66.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.242 | 0.358 | +47.9% | -0.0452 to 0.277 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.661 to 0.541 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00187 to 0.00127 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 0.232 | 0.233 | +0.5% | -0.0394 to 0.0418 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.1% | -0.0414 to 0.034 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.287 | 0.286 | -0.2% | -0.0145 to 0.0133 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.00769 to 0.0761 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0848 | 0.0914 | +7.8% | -0.0463 to 0.0595 | EVEN, no difference beyond the noise |
| host CPU-seconds | 141 | 153 | +8.5% | -85.5 to 110 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.213 | 0.232 | +8.5% | -0.129 to 0.166 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.053 to 0.0546 | EVEN, the same |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0133 to 0.0191 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | +0.0% | -9.74e-06 to 9.74e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.1% | -0.0174 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.1% | -0.0183 to 0.0121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.35 | -0.1% | -0.00678 to 0.00494 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00921 to 0.036 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.121 | +3.9% | 0.000971 to 0.00818 | power given |
| host CPU-seconds | 195 | 204 | +4.7% | 2.01 to 16.2 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.369 | 0.386 | +4.7% | 0.00379 to 0.0307 | power given |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,391 | 1,391 | +0.0% | -0.279 to 0.392 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00498 to 0.00323 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -1.14e-06 to 3.11e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.0119 to 0.0134 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.23 | +0.0% | -0.0282 to 0.0307 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.449 | 0.448 | -0.1% | -0.00484 to 0.00351 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.011 to 0.035 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0521 | 0.0525 | +0.8% | -0.042 to 0.0428 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.7 | 92.7 | +1.1% | -77.9 to 79.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.146 | 0.148 | +1.1% | -0.124 to 0.128 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
