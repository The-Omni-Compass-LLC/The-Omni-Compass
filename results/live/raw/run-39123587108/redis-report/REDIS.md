# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.34 to 1.03 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0472 to 0.0295 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00108 to 0.000861 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0183 to 0.0126 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.1% | -0.0157 to 0.0298 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.2% | -0.00188 to 0.00863 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.77 to -1.22 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.77 to -0.389 | GAIN |
| keys evicted | 71,766 | 71,797 | +0.0% | -218 to 279 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.128 | -7.9% | -0.0667 to 0.0448 | EVEN, no difference beyond the noise |
| host CPU-seconds | 92.9 | 84.5 | -9.0% | -50 to 33.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.48 | 0.436 | -9.0% | -0.258 to 0.171 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 19.7 to 21.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00096 to 0.00263 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0134 to 0.0145 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.51 | -0.0% | -0.0419 to 0.0389 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.1% | -0.0148 to 0.0292 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.962 | 0.892 | -7.3% | -0.0744 to -0.0661 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.105 to 1.7 | power given |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | 0.103 to 1.13 | power given |
| keys evicted | 103,484 | 94,291 | -8.9% | -9,538 to -8,849 | shown, not judged |
| host CPU busy (share of the run) | 0.0993 | 0.103 | +4.1% | -0.00573 to 0.0138 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 181 | +4.5% | -12 to 27.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.305 | 0.313 | +2.8% | -0.0262 to 0.0434 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 938 | +1.3% | 10.2 to 14.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0413 to 0.019 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00714 to 0.00937 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0128 to 0.0116 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.3% | -0.00366 to 0.0363 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.8% | -0.0559 to -0.0272 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.34 to 1.63 | power given |
| memory used, mean (MB) | 60.7 | 61.7 | +1.7% | 0.938 to 1.11 | power given |
| keys evicted | 243,138 | 240,817 | -1.0% | -3,090 to -1,552 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.142 | +2.4% | -0.022 to 0.0287 | EVEN, no difference beyond the noise |
| host CPU-seconds | 231 | 238 | +2.9% | -41.7 to 55.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.556 | 0.564 | +1.5% | -0.108 to 0.125 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16 |  | 16 to 16 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,193 | +0.8% | 5.46 to 14.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0144 to 0.00573 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00378 to 0.00968 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.0294 to 0.0297 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.85 | +0.7% | -0.0465 to 0.123 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.33 | -2.1% | -0.0444 to -0.0127 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.219 to 2.67 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.1 | +1.5% | 0.0863 to 1.73 | power given |
| keys evicted | 138,220 | 134,500 | -2.7% | -5,706 to -1,734 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.132 | -2.3% | -0.0202 to 0.0139 | EVEN, no difference beyond the noise |
| host CPU-seconds | 228 | 221 | -2.7% | -38 to 25.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.427 | 0.412 | -3.5% | -0.0733 to 0.0435 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 14 to 24 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
