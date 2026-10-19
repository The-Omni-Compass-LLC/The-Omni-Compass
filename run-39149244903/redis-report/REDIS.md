# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -3.95 to 3.15 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.02 to 0.0354 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00259 to 0.00207 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.66 | 5.65 | -0.2% | -0.0401 to 0.0186 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.0256 to 0.0197 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.66 | 1.65 | -0.3% | -0.0317 to 0.0208 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.76 to -1.17 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.747 to -0.283 | GAIN |
| keys evicted | 71,704 | 71,798 | +0.1% | -560 to 750 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.12 | +6.6% | -0.0637 to 0.0784 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.4 | 85.4 | +7.5% | -51.3 to 63.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.41 | 0.441 | +7.5% | -0.264 to 0.326 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 12.7 to 24.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00238 to 0.00337 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.00845 to 0.0168 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.51 | -0.2% | -0.0178 to -0.00464 | GAIN |
| latency, 99th percentile (ms) | 5.62 | 5.62 | -0.0% | -0.0132 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.964 | 0.897 | -6.9% | -0.0848 to -0.0485 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.493 to 1.88 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.6 | +0.5% | -0.695 to 1.34 | EVEN, no difference beyond the noise |
| keys evicted | 103,361 | 94,999 | -8.1% | -11,355 to -5,369 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.107 | +6.9% | -0.00883 to 0.0227 | EVEN, no difference beyond the noise |
| host CPU-seconds | 175 | 188 | +7.9% | -16.1 to 43.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.325 | +6.3% | -0.0316 to 0.0703 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 18.7 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.49 to 13.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0182 to 0.00963 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00631 to 0.00888 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | +0.1% | -0.00438 to 0.0109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.59 | +0.1% | 0.00317 to 0.0102 | LOSS |
| latency, mean (ms) | 2.15 | 2.11 | -1.8% | -0.0426 to -0.0366 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.15 to 1.81 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.844 to 1.51 | power given |
| keys evicted | 243,068 | 236,934 | -2.5% | -14,403 to 2,136 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.102 | -10.7% | -0.0524 to 0.0278 | EVEN, no difference beyond the noise |
| host CPU-seconds | 201 | 177 | -12.0% | -102 to 54.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.482 | 0.419 | -13.1% | -0.251 to 0.125 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 7.43 to 20.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.6% | 4.19 to 9.69 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000198 to 0.00288 | EVEN, the same |
| cache hit rate | 0.789 | 0.794 | +0.6% | 0.00281 to 0.00632 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% | -0.0135 to 0.011 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.0039 to 0.0115 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.8% | -0.0308 to -0.0177 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.8 | +1.3% | 0.436 to 1.19 | power given |
| memory used, mean (MB) | 61.2 | 61.8 | +1.0% | 0.187 to 0.996 | power given |
| keys evicted | 138,223 | 135,967 | -1.6% | -3,450 to -1,063 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.108 | -9.2% | -0.0606 to 0.0387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 179 | -10.0% | -112 to 72.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.373 | 0.334 | -10.6% | -0.211 to 0.132 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 8.74 to 23.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
