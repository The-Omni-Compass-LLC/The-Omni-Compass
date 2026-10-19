# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.0598 to 0.0132 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0122 to 0.00979 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | -4.08e-06 to 6.55e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.72 | +0.1% | -0.0167 to 0.0264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.79 | +0.2% | -0.0202 to 0.0377 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.811 | 0.814 | +0.4% | -0.0105 to 0.0173 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.00188 to 0.0511 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.107 | -9.0% | -0.0852 to 0.0641 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.6 | 71.7 | -9.9% | -63.1 to 47.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.333 | 0.3 | -9.9% | -0.264 to 0.198 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,469 | 1,470 | +0.0% | -0.0159 to 0.295 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0327 to 0.0226 | EVEN, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | +0.0% | -4.77e-06 to 7.66e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.107 | 0.103 | -3.7% | -0.017 to 0.00916 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0204 to 0.0162 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.18 | 0.181 | +0.1% | -0.00482 to 0.0052 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0227 to 0.0791 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0482 | 0.0728 | +51.0% | -0.00998 to 0.0591 | EVEN, no difference beyond the noise |
| host CPU-seconds | 84.6 | 131 | +55.3% | -19.1 to 113 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.128 | 0.199 | +55.3% | -0.0289 to 0.17 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.139 to 0.097 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0366 to 0.0362 | EVEN, the same |
| cache hit rate | 0.782 | 0.783 | +0.0% | -1.08e-05 to 1.17e-05 | EVEN, the same |
| latency, 95th percentile (ms) | 5.66 | 5.66 | +0.0% | -0.0082 to 0.0132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00845 to 0.0138 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.0% | -0.0056 to 0.00637 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0227 to 0.0257 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.115 | +0.6% | -0.0419 to 0.0432 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 193 | +0.5% | -79.8 to 81.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.366 | +0.5% | -0.151 to 0.155 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `e2d5958834f5`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,393 | +0.0% | -0.294 to 0.706 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00865 to 0.00855 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% | -0.015 to 0.0125 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.76 | +0.0% | -0.019 to 0.0236 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.567 | 0.565 | -0.2% | -0.00592 to 0.0031 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.00699 to 0.0595 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0939 | 0.103 | +9.2% | -0.01 to 0.0273 | EVEN, no difference beyond the noise |
| host CPU-seconds | 157 | 173 | +10.2% | -17.8 to 49.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.251 | 0.276 | +10.1% | -0.0284 to 0.0793 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
