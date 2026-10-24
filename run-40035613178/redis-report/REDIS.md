# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.5 to 0.648 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00377 to 0.00438 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000921 to 0.000508 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.00263 to 0.00178 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | 0.00306 to 0.0168 | LOSS |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00248 to 0.0163 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.85 to -1.14 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -1.0% | -1.02 to -0.125 | GAIN |
| keys evicted | 71,748 | 71,810 | +0.1% | -113 to 237 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.132 | -8.4% | -0.0587 to 0.0346 | EVEN, no difference beyond the noise |
| host CPU-seconds | 97.7 | 88.1 | -9.7% | -46.3 to 27.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.504 | 0.455 | -9.7% | -0.239 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 17.3 to 23.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00453 to 0.00292 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.6% | 0.0118 to 0.0153 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.48 | -0.2% | -0.0508 to 0.0291 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.014 to 0.014 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.955 | 0.884 | -7.5% | -0.0856 to -0.0577 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.186 to 1.58 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.6% | 0.00459 to 0.775 | power given |
| keys evicted | 103,421 | 94,503 | -8.6% | -10,104 to -7,732 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0946 | -6.3% | -0.041 to 0.0284 | EVEN, no difference beyond the noise |
| host CPU-seconds | 177 | 166 | -6.6% | -78.4 to 55 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.311 | 0.286 | -8.1% | -0.14 to 0.0901 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 27.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 10.5 to 12.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0143 to 0.00354 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00704 to 0.0085 | GAIN |
| latency, 95th percentile (ms) | 5.54 | 5.55 | +0.3% | -0.0638 to 0.0929 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.64 | +0.3% | -0.0368 to 0.0675 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.12 | 2.08 | -1.6% | -0.0658 to -0.0014 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 1.38 to 1.7 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.27 to 1.32 | power given |
| keys evicted | 243,175 | 234,790 | -3.4% | -8,876 to -7,894 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.1 | -7.4% | -0.0269 to 0.0109 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 177 | -8.5% | -55.6 to 22.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.42 | -9.6% | -0.138 to 0.0491 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 3.7 to 16 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0047 to 0.00618 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00249 to 0.0106 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.00606 to 0.00205 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.00309 to 0.0114 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.5% | -0.0539 to -0.0142 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.129 to 2.3 | power given |
| memory used, mean (MB) | 61.2 | 62.1 | +1.4% | 0.0884 to 1.68 | power given |
| keys evicted | 138,129 | 134,517 | -2.6% | -6,359 to -866 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.109 | -9.8% | -0.0342 to 0.0104 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 180 | -11.0% | -65.2 to 20.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.38 | 0.336 | -11.7% | -0.124 to 0.0345 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
