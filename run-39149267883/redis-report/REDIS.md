# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.71 to 0.927 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0102 to 0.0184 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00106 to 0.000596 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0156 to 0.0185 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.1% | -0.0158 to 0.0301 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.68 | 1.69 | +0.3% | -0.0176 to 0.0281 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.1 | -2.9% | -3.77 to 0.00637 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 56.2 | -1.7% | -2.93 to 1 | EVEN, no difference beyond the noise |
| keys evicted | 71,762 | 71,838 | +0.1% | -146 to 298 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.117 | -12.5% | -0.0434 to 0.0101 | EVEN, no difference beyond the noise |
| host CPU-seconds | 95.5 | 82.1 | -14.1% | -33.8 to 7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.493 | 0.424 | -14.0% | -0.174 to 0.0361 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,286 | +1.6% | 12.7 to 27 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0025 to 0.00313 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.6% | 0.00866 to 0.0179 | GAIN |
| latency, 95th percentile (ms) | 5.48 | 5.47 | -0.2% | -0.029 to 0.00334 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% | -0.00382 to -5.85e-05 | GAIN |
| latency, mean (ms) | 0.956 | 0.886 | -7.3% | -0.0947 to -0.045 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.2% | -3.15 to 2.92 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.8 | -0.8% | -3.72 to 2.76 | EVEN, no difference beyond the noise |
| keys evicted | 103,641 | 95,051 | -8.3% | -11,962 to -5,216 | shown, not judged |
| host CPU busy (share of the run) | 0.0917 | 0.104 | +13.2% | -0.0151 to 0.0393 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 184 | +14.9% | -28.9 to 76.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.317 | +13.2% | -0.0558 to 0.13 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 25.7 |  | 11.1 to 40.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 10.6 to 13.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0556 to 0.0357 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00673 to 0.00921 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.1% | -0.0314 to 0.0227 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.0306 to 0.0364 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% | -0.0654 to -0.0255 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.978 to 1.78 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.867 to 1.46 | power given |
| keys evicted | 243,123 | 236,726 | -2.6% | -14,894 to 2,100 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.136 | -2.6% | -0.00771 to 0.000427 | EVEN, no difference beyond the noise |
| host CPU-seconds | 234 | 227 | -2.9% | -14.9 to 1.23 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.538 | -4.1% | -0.0432 to -0.00334 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 9.08 to 21.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,192 | +0.7% | -0.963 to 16.4 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0174 to 0.0185 | EVEN, the same |
| cache hit rate | 0.79 | 0.795 | +0.7% | -0.00058 to 0.011 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00473 to 0.0168 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% | -0.000116 to 0.0311 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.7% | -0.0586 to 0.0138 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.161 to 1.66 | power given |
| memory used, mean (MB) | 61.2 | 61.8 | +1.0% | -0.0615 to 1.27 | EVEN, no difference beyond the noise |
| keys evicted | 138,050 | 135,913 | -1.5% | -5,486 to 1,214 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.131 | -1.5% | -0.0402 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 220 | -1.9% | -78.5 to 69.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.409 | -2.6% | -0.15 to 0.129 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 3.79 to 36.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
