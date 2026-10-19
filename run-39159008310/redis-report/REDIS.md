# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.0954 to 0.0621 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00649 to 0.00652 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 5.72 | 5.71 | -0.1% | -0.0277 to 0.0126 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.77 | -0.2% | -0.0396 to 0.018 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.811 | 0.81 | -0.2% | -0.00844 to 0.00586 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00613 to 0.0592 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.095 | 0.109 | +14.8% | -0.0274 to 0.0555 | EVEN, no difference beyond the noise |
| host CPU-seconds | 63 | 73.8 | +17.2% | -20.5 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.264 | 0.309 | +17.2% | -0.0858 to 0.177 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.165 to 0.156 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000229 to 0.000834 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 0.231 | 0.228 | -1.2% | -0.00754 to 0.0021 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | -0.1% | -0.0222 to 0.0133 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.287 | 0.285 | -0.5% | -0.00872 to 0.0057 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0161 to 0.0596 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0918 | 0.0858 | -6.5% | -0.0477 to 0.0358 | EVEN, no difference beyond the noise |
| host CPU-seconds | 154 | 143 | -6.8% | -87.5 to 66.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.232 | 0.216 | -6.8% | -0.132 to 0.1 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.0708 to 0.16 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00404 to 0.00885 | EVEN, no difference beyond the noise |
| cache hit rate | 0.783 | 0.782 | -0.0% | -6.61e-06 to 4.63e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.65 | 5.65 | -0.1% | -0.0209 to 0.0136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.0% | -0.0176 to 0.0123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.35 | -0.1% | -0.00725 to 0.00455 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.016 to 0.0299 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.113 | -1.4% | -0.0171 to 0.0139 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 191 | -1.5% | -32.7 to 26.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.366 | 0.361 | -1.5% | -0.0621 to 0.051 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `3cb376bb3284`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% | -0.0224 to 0.0141 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000958 to 0.00312 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -2.62e-06 to 1.63e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.5 | 5.5 | -0.1% | -0.0125 to 0.00414 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.66 | +0.0% | -0.00434 to 0.00739 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.523 | 0.524 | +0.2% | -0.000222 to 0.00187 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0247 to 0.0435 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.0955 | -13.6% | -0.0363 to 0.00612 | EVEN, no difference beyond the noise |
| host CPU-seconds | 198 | 168 | -15.2% | -73 to 12.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.316 | 0.268 | -15.2% | -0.116 to 0.0205 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
