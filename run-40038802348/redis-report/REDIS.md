# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.285 to 0.266 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00291 to 0.00702 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | 0 to 0 | EVEN, the same |
| latency, 95th percentile (ms) | 5.72 | 5.71 | -0.0% | -0.0159 to 0.0128 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.0% | -0.0258 to 0.0216 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.811 | 0.812 | +0.1% | -0.00854 to 0.00935 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.00354 to 0.0269 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.127 | +12.7% | -0.0476 to 0.0763 | EVEN, no difference beyond the noise |
| host CPU-seconds | 76.3 | 87.3 | +14.5% | -36.4 to 58.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.319 | 0.365 | +14.5% | -0.152 to 0.245 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% | -0.0254 to 0.0182 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00108 to 0.00129 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.68e-06 to 3.68e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.194 | 0.218 | +12.3% | -0.0268 to 0.0745 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.53 | 5.52 | -0.1% | -0.0137 to -0.00084 | GAIN |
| latency, mean (ms) | 0.244 | 0.247 | +1.2% | -5.59e-05 to 0.00601 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.0194 to 0.0578 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0893 | 0.0986 | +10.5% | -0.0461 to 0.0647 | EVEN, no difference beyond the noise |
| host CPU-seconds | 157 | 175 | +11.4% | -90.7 to 127 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.237 | 0.264 | +11.4% | -0.137 to 0.191 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% | -0.289 to 0.404 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00542 to 0.00527 | EVEN, the same |
| cache hit rate | 0.783 | 0.783 | +0.0% | -3.15e-06 to 8.09e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.46 | 5.46 | +0.0% | -0.00543 to 0.00901 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.56 | 5.56 | +0.0% | -0.00592 to 0.00765 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.27 | -0.0% | -0.0039 to 0.00303 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0145 to 0.0386 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.09 | 0.097 | +7.8% | -0.0172 to 0.0312 | EVEN, no difference beyond the noise |
| host CPU-seconds | 157 | 171 | +8.6% | -33.8 to 61 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.297 | 0.323 | +8.6% | -0.064 to 0.115 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `d02c7052ae50`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -0.733 to 0.986 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0128 to 0.0139 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -3.76e-06 to 4.74e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.008 to 0.00819 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.76 | -0.1% | -0.0161 to 0.00677 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.57 | 0.568 | -0.3% | -0.00453 to 0.00145 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.00826 to 0.067 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0868 | 0.0903 | +4.1% | -0.0176 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 144 | 151 | +4.8% | -32.3 to 46.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.229 | 0.24 | +4.8% | -0.0515 to 0.0734 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
