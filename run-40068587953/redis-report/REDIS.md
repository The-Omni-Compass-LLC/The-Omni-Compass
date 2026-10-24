# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.0874 to 0.0669 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00778 to 0.00555 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | -9.2e-06 to 9.2e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.47 | 5.46 | -0.1% | -0.118 to 0.11 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.64 | +0.1% | -0.02 to 0.0293 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.721 | 0.722 | +0.2% | -0.0102 to 0.013 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.00353 to 0.0686 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.094 | 0.0972 | +3.4% | -0.103 to 0.109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 67.8 | 69.9 | +3.1% | -83 to 87.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.284 | 0.293 | +3.1% | -0.347 to 0.365 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | +0.0% | -0.351 to 0.816 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00226 to 0.00164 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -1.63e-06 to 2.62e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.0965 | 0.0945 | -2.0% | -0.0154 to 0.0115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.2 | 5.21 | +0.0% | -0.00503 to 0.0078 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.173 | 0.172 | -0.8% | -0.00463 to 0.00186 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0059 to 0.0531 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.059 | 0.0605 | +2.7% | -0.103 to 0.106 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 109 | +3.7% | -192 to 200 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.159 | 0.165 | +3.6% | -0.29 to 0.302 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,174 | +0.0% | -0.425 to 0.657 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00223 to -0.000245 | EVEN, the same |
| cache hit rate | 0.783 | 0.783 | -0.0% | -5.24e-06 to 3.26e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.46 | 5.45 | -0.0% | -0.01 to 0.00508 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.55 | 5.55 | -0.0% | -0.0139 to 0.0099 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.26 | 1.26 | -0.1% | -0.00415 to 0.00265 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.0093 to 0.0555 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0907 | 0.0902 | -0.5% | -0.0197 to 0.0187 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 158 | -0.5% | -37.7 to 36.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.3 | 0.298 | -0.5% | -0.0713 to 0.0681 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.33 to 0.453 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00253 to 0.00376 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -1.75e-06 to 2.81e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.39 | 5.38 | -0.2% | -0.123 to 0.102 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.57 | +0.0% | -0.00633 to 0.00986 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.498 | 0.499 | +0.1% | -0.00152 to 0.00216 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.00631 to 0.0482 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0831 | 0.103 | +23.5% | -0.0152 to 0.0542 | EVEN, no difference beyond the noise |
| host CPU-seconds | 145 | 183 | +26.3% | -29.8 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.232 | 0.293 | +26.3% | -0.0474 to 0.169 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
