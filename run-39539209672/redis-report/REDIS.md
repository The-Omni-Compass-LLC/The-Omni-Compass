# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.28 to 0.208 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.227 to 0.147 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -3.45e-06 to 2.15e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.1% | -0.0149 to 0.00624 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.77 | -0.1% | -0.0194 to 0.00874 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.808 | 0.807 | -0.1% | -0.00449 to 0.00327 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0052 to 0.0611 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0965 | 0.101 | +4.6% | -0.0474 to 0.0562 | EVEN, no difference beyond the noise |
| host CPU-seconds | 64.2 | 67.7 | +5.4% | -35.3 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.269 | 0.283 | +5.4% | -0.148 to 0.177 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,472 | +0.0% | 0.0327 to 0.438 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00199 to 0.00265 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.76e-06 to 4.74e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.229 | 0.232 | +1.2% | -0.0137 to 0.0193 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.0142 to 0.0314 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.286 | 0.286 | +0.1% | -0.00719 to 0.00753 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 349 | +0.0% | -0.0122 to 0.0666 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.0977 | -17.7% | -0.0586 to 0.0165 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 163 | -19.7% | -109 to 29.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.307 | 0.246 | -19.7% | -0.165 to 0.0446 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.496 to 0.731 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0193 to 0.0226 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | +0.0% | -5.88e-06 to 8.84e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.66 | 5.65 | -0.1% | -0.0136 to 0.00454 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.00836 to 0.00176 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.35 | -0.3% | -0.00883 to 0.00195 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.00519 to 0.0489 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.132 | -4.6% | -0.0266 to 0.014 | EVEN, no difference beyond the noise |
| host CPU-seconds | 236 | 224 | -5.2% | -52.1 to 27.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.447 | 0.424 | -5.2% | -0.0988 to 0.0521 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,393 | +0.0% | -0.919 to 1.45 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00111 to 0.0033 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.68e-06 to 3.68e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.0% | -0.00723 to 0.00876 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | -0.0% | -0.0125 to 0.00704 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.571 | 0.568 | -0.4% | -0.0115 to 0.00646 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.00248 to 0.0673 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0971 | -12.9% | -0.0677 to 0.0389 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 163 | -14.0% | -126 to 72.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.303 | 0.261 | -14.0% | -0.201 to 0.116 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
