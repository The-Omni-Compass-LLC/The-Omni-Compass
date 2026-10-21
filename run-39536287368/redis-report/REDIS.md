# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.11 to 1.65 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0121 to 0.0121 | EVEN, the same |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00128 to 0.00107 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% | -0.00184 to 0.0164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.82 | +0.3% | 0.00282 to 0.0286 | LOSS |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00269 to 0.0164 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.3 | -2.6% | -1.83 to -1.49 | GAIN |
| memory used, mean (MB) | 57.2 | 56.4 | -1.3% | -0.868 to -0.664 | GAIN |
| keys evicted | 71,723 | 71,769 | +0.1% | -283 to 374 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.132 | +5.4% | -0.0482 to 0.0618 | EVEN, no difference beyond the noise |
| host CPU-seconds | 83.7 | 88.2 | +5.3% | -37.8 to 46.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.432 | 0.455 | +5.4% | -0.195 to 0.241 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 8.55 to 30.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00163 to 0.000334 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.00575 to 0.0203 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.0126 to 0.0116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.0152 to 0.0282 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.98 | -6.5% | -0.111 to -0.0257 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.575 to 2.02 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | -0.46 to 1.26 | EVEN, no difference beyond the noise |
| keys evicted | 103,514 | 94,962 | -8.3% | -13,441 to -3,663 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.137 | -3.3% | -0.0413 to 0.0321 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 233 | -3.7% | -81.5 to 63.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.424 | 0.402 | -5.2% | -0.15 to 0.106 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.2 to 12.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0158 to 0.0128 | EVEN, the same |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00682 to 0.00837 | GAIN |
| latency, 95th percentile (ms) | 5.61 | 5.6 | -0.1% | -0.0167 to 0.00606 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.0124 to 0.013 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.17 | 2.13 | -2.1% | -0.0556 to -0.036 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.34 to 1.65 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.2 to 1.33 | power given |
| keys evicted | 243,054 | 234,788 | -3.4% | -8,764 to -7,768 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.107 | -13.8% | -0.0525 to 0.0181 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 187 | -15.2% | -105 to 37.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.53 | 0.444 | -16.2% | -0.257 to 0.0851 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 7.93 to 19.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 1.06 to 18.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.007 to 0.00324 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.000699 to 0.0125 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.0145 to 0.0152 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0116 to 0.0226 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -2.5% | -0.0738 to 0.00745 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | -0.529 to 2.75 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62 | +1.4% | -0.181 to 1.88 | EVEN, no difference beyond the noise |
| keys evicted | 138,237 | 134,612 | -2.6% | -7,611 to 359 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.118 | -4.4% | -0.0845 to 0.0735 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 198 | -4.9% | -159 to 138 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.39 | 0.368 | -5.7% | -0.302 to 0.258 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 7.99 to 28.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
