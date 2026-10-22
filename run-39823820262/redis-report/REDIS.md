# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.69 to 0.693 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0235 to 0.019 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00177 to 0.000448 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.59 | 5.58 | -0.0% | -0.0267 to 0.0212 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.68 | +0.1% | -0.00416 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.6 | 1.61 | +0.2% | -0.0056 to 0.0116 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.71 to -1.13 | GAIN |
| memory used, mean (MB) | 57.2 | 56.7 | -0.9% | -0.809 to -0.17 | GAIN |
| keys evicted | 71,590 | 71,774 | +0.3% | -122 to 490 | shown, not judged |
| host CPU busy (share of the run) | 0.082 | 0.0943 | +14.9% | -0.0188 to 0.0433 | EVEN, no difference beyond the noise |
| host CPU-seconds | 57.3 | 66.6 | +16.3% | -14.8 to 33.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.295 | 0.344 | +16.4% | -0.076 to 0.173 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 13.3 to 22 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0247 to 0.0163 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00957 to 0.015 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.0% | -0.012 to 0.00894 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.29 | -0.1% | -0.0603 to 0.0527 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.901 | 0.842 | -6.5% | -0.0749 to -0.0425 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | -0.263 to 3.51 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.2 | +1.5% | 0.0446 to 1.81 | power given |
| keys evicted | 103,499 | 95,271 | -7.9% | -10,193 to -6,263 | shown, not judged |
| host CPU busy (share of the run) | 0.0732 | 0.0753 | +2.8% | -0.0191 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 130 | 133 | +2.9% | -36.6 to 44.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.228 | 0.231 | +1.5% | -0.0672 to 0.0739 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 13.4 to 25.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 11 to 12.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0461 to 0.0242 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00754 to 0.00872 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.0121 to 0.0237 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.33 | 5.45 | +2.2% | 0.0716 to 0.167 | LOSS |
| latency, mean (ms) | 2.06 | 2.02 | -1.7% | -0.0405 to -0.0309 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.48 to 1.71 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.23 to 1.4 | power given |
| keys evicted | 243,278 | 235,724 | -3.1% | -12,202 to -2,906 | shown, not judged |
| host CPU busy (share of the run) | 0.0699 | 0.0674 | -3.5% | -0.032 to 0.027 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 118 | -4.1% | -59.6 to 49.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.296 | 0.281 | -5.3% | -0.146 to 0.115 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 10.9 to 18.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,193 | +1.0% | 6.81 to 16.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00396 to 0.0185 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00472 to 0.0107 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.0% | -0.0187 to 0.0157 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.31 | -0.1% | -0.18 to 0.174 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.14 | -3.3% | -0.0638 to -0.0143 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.19 to 2.13 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 1.02 to 1.34 | power given |
| keys evicted | 138,213 | 133,839 | -3.2% | -6,406 to -2,342 | shown, not judged |
| host CPU busy (share of the run) | 0.0557 | 0.0714 | +28.2% | 0.00106 to 0.0303 | power given |
| host CPU-seconds | 96.9 | 126 | +30.5% | 1.49 to 57.7 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.182 | 0.235 | +29.2% | 0.00202 to 0.105 | power given |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
