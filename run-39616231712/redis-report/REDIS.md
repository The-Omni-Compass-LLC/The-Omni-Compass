# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.0544 to 0.0407 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0243 to 0.0135 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | -8.62e-06 to 1.33e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.54 | 5.52 | -0.4% | -0.0539 to 0.0143 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.67 | -0.2% | -0.0249 to 0.00699 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.736 | 0.732 | -0.5% | -0.0145 to 0.00687 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0114 to 0.0497 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0871 | -13.2% | -0.125 to 0.0981 | EVEN, no difference beyond the noise |
| host CPU-seconds | 71.9 | 62.1 | -13.7% | -98.4 to 78.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.301 | 0.26 | -13.7% | -0.412 to 0.329 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.361 to 0.271 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00326 to 0.00207 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% | -6.12e-06 to 5.13e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.205 | 0.207 | +1.2% | -0.0056 to 0.0105 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | +0.0% | -0.00393 to 0.00484 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.265 | 0.265 | +0.2% | -0.00222 to 0.00353 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.00282 to 0.0713 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.12 | -0.6% | -0.0394 to 0.038 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 211 | -0.8% | -80 to 76.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.321 | 0.319 | -0.8% | -0.121 to 0.116 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0784 to 0.0921 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0198 to 0.0335 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.783 | +0.0% | -4.89e-06 to 7.86e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.66 | -0.0% | -0.0109 to 0.00747 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.012 to 0.0117 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.36 | +0.0% | -0.00576 to 0.00585 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.00646 to 0.0562 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.127 | +1.1% | -0.0296 to 0.0322 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 216 | +1.1% | -57 to 61.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.408 | +1.1% | -0.108 to 0.117 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `63a093f13de0`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0718 to 0.0878 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00167 to 0.00451 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.76e-06 to 4.74e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0457 to 0.023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0145 to 0.00897 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.514 | 0.514 | -0.0% | -0.00234 to 0.00192 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.00609 to 0.0626 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0887 | 0.108 | +22.2% | -0.0469 to 0.0863 | EVEN, no difference beyond the noise |
| host CPU-seconds | 156 | 194 | +24.5% | -94.5 to 171 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.249 | 0.31 | +24.5% | -0.151 to 0.273 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
