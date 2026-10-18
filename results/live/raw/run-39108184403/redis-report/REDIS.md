# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.13 to 0.0127 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0267 to 0.0134 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.000828 to -0.000291 | LOSS |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00807 to 0.0109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | 0.00392 to 0.018 | LOSS |
| latency, mean (ms) | 1.73 | 1.74 | +0.3% | -0.00177 to 0.0129 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.8 to -1.34 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% | -0.926 to -0.453 | GAIN |
| keys evicted | 71,693 | 71,860 | +0.2% | 109 to 225 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.142 | -7.7% | -0.0557 to 0.0319 | EVEN, no difference beyond the noise |
| host CPU-seconds | 106 | 96.3 | -9.2% | -45 to 25.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.547 | 0.497 | -9.1% | -0.231 to 0.132 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,281 | +1.1% | 7.43 to 21.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000692 to 0.00211 | EVEN, the same |
| cache hit rate | 0.845 | 0.855 | +1.1% | 0.00518 to 0.0142 | GAIN |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0146 to 0.0088 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.0% | -0.0151 to 0.0209 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 1.01 | -5.0% | -0.0734 to -0.0325 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -0.997 to 1.66 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.3 | +0.0% | -0.772 to 0.828 | EVEN, no difference beyond the noise |
| keys evicted | 103,421 | 97,098 | -6.1% | -9,374 to -3,272 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.116 | -6.5% | -0.0186 to 0.00258 | EVEN, no difference beyond the noise |
| host CPU-seconds | 208 | 193 | -7.2% | -35 to 5.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.334 | -8.2% | -0.0659 to 0.00587 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 21 to 21 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.6 to 12.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.015 to 0.00324 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00716 to 0.00844 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.49 | +0.0% | -0.00838 to 0.00887 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.56 | 5.56 | +0.1% | -0.00289 to 0.0113 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.13 | 2.09 | -1.9% | -0.0493 to -0.0306 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.37 to 1.64 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.19 to 1.38 | power given |
| keys evicted | 243,216 | 234,806 | -3.5% | -8,871 to -7,949 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.096 | -12.9% | -0.0223 to -0.00604 | GAIN |
| host CPU-seconds | 194 | 166 | -14.2% | -42.4 to -12.6 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.394 | -15.3% | -0.107 to -0.0354 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.0% | 3.37 to 20.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0094 to 0.00409 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.0% | 0.00278 to 0.0136 | GAIN |
| latency, 95th percentile (ms) | 5.52 | 5.52 | +0.0% | -0.0134 to 0.0172 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.6 | +0.1% | -0.0121 to 0.0185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.2 | -3.3% | -0.0835 to 0.000794 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 0.485 to 2.53 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% | 0.376 to 1.76 | power given |
| keys evicted | 138,152 | 133,440 | -3.4% | -8,385 to -1,041 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.105 | +1.0% | -0.0128 to 0.0149 | EVEN, no difference beyond the noise |
| host CPU-seconds | 183 | 185 | +1.0% | -25.1 to 28.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.343 | 0.343 | +0.0% | -0.0529 to 0.053 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
