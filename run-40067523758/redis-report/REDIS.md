# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.78 to -0.528 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0317 to 0.047 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00146 to -8.48e-05 | LOSS |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.1% | -0.00398 to 0.013 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | +0.1% | -0.00101 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.64 | +0.5% | -0.00675 to 0.0223 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.4% | -2.13 to -0.918 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.1% | -1.21 to -0.00782 | GAIN |
| keys evicted | 71,619 | 71,840 | +0.3% | 39.4 to 403 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.116 | +3.5% | -0.11 to 0.118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.9 | 82.1 | +2.8% | -86.8 to 91.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.412 | 0.424 | +3.0% | -0.448 to 0.472 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.5% | 3.81 to 33 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0057 to 0.00361 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00222 to 0.0225 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.1% | -0.0333 to 0.0193 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.0% | -0.0211 to 0.0254 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.993 | -6.2% | -0.127 to -0.00497 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.7% | -0.928 to 1.83 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -0.938 to 1.38 | EVEN, no difference beyond the noise |
| keys evicted | 103,481 | 95,317 | -7.9% | -15,135 to -1,194 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.121 | -2.2% | -0.0555 to 0.0501 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 203 | -2.0% | -105 to 96.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.364 | 0.351 | -3.4% | -0.191 to 0.167 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 19.5 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.57 to 13.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.025 to 0.00477 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.0064 to 0.00871 | GAIN |
| latency, 95th percentile (ms) | 5.57 | 5.57 | -0.0% | -0.0121 to 0.0111 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.64 | +0.0% | -0.00696 to 0.0118 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.16 | 2.12 | -1.9% | -0.05 to -0.0312 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.22 to 1.71 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.17 to 1.36 | power given |
| keys evicted | 243,059 | 234,812 | -3.4% | -9,032 to -7,462 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.109 | -11.7% | -0.0341 to 0.00527 | EVEN, no difference beyond the noise |
| host CPU-seconds | 222 | 193 | -13.0% | -67.9 to 10 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.533 | 0.458 | -14.1% | -0.167 to 0.0173 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 8.03 to 18 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 12.3 to 15.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0149 to 0.00407 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00804 to 0.00993 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.23 | +0.3% | -0.0238 to 0.0525 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.33 | +1.1% | -0.0993 to 0.213 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.7% | -0.0571 to -0.03 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 0.723 to 2.18 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | 1.01 to 1.32 | power given |
| keys evicted | 138,233 | 132,994 | -3.8% | -5,869 to -4,608 | shown, not judged |
| host CPU busy (share of the run) | 0.0553 | 0.0711 | +28.5% | -0.0224 to 0.0539 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.7 | 126 | +30.1% | -41.2 to 99.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.182 | 0.234 | +28.5% | -0.0796 to 0.183 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
