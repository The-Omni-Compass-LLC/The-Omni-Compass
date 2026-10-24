# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -0.916 to 0.103 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00677 to 0.00847 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00103 to 0.000326 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | -0.0% | -0.00859 to 0.00425 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | -0.0% | -0.00829 to 0.00758 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.64 | 1.64 | -0.1% | -0.0113 to 0.00929 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.3% | -3.95 to -0.316 | GAIN |
| memory used, mean (MB) | 57.1 | 55.9 | -2.1% | -3.01 to 0.589 | EVEN, no difference beyond the noise |
| keys evicted | 71,742 | 71,850 | +0.2% | -77.3 to 293 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.109 | -1.8% | -0.0314 to 0.0274 | EVEN, no difference beyond the noise |
| host CPU-seconds | 78.1 | 76.4 | -2.2% | -25.1 to 21.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.403 | 0.395 | -2.2% | -0.129 to 0.112 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,282 | +1.2% | -2.31 to 32.8 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000208 to 0.00298 | EVEN, the same |
| cache hit rate | 0.845 | 0.855 | +1.2% | -0.00128 to 0.0219 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.00809 to 0.00955 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% | 0.00273 to 0.018 | LOSS |
| latency, mean (ms) | 1.06 | 1 | -5.0% | -0.122 to 0.0158 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -2.04 to 2.71 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.1 | -0.3% | -3.16 to 2.86 | EVEN, no difference beyond the noise |
| keys evicted | 103,532 | 96,863 | -6.4% | -14,583 to 1,245 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.118 | -2.9% | -0.0417 to 0.0347 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 196 | -3.1% | -78.6 to 66.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.34 | -4.2% | -0.144 to 0.114 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 6.61 to 41.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 9.75 to 14.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.033 to 0.0116 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00666 to 0.00939 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.1% | -0.039 to 0.0294 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.75 | +0.1% | -0.0351 to 0.0432 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.22 | -1.9% | -0.0685 to -0.0185 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.32 to 1.61 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.814 to 1.38 | power given |
| keys evicted | 243,128 | 238,830 | -1.8% | -12,526 to 3,928 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.146 | +2.2% | -0.0465 to 0.0528 | EVEN, no difference beyond the noise |
| host CPU-seconds | 240 | 247 | +2.9% | -87.3 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.575 | 0.584 | +1.6% | -0.216 to 0.235 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10.7 to 19.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `dadeec62a61a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,193 | +0.8% | 1.82 to 17.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00731 to 0.00658 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00167 to 0.0115 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0286 to 0.017 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.0209 to 0.026 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.5% | -0.0607 to -0.00802 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | -0.25 to 2.38 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.9 | +1.2% | -0.0536 to 1.54 | EVEN, no difference beyond the noise |
| keys evicted | 138,257 | 134,915 | -2.4% | -7,211 to 527 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.118 | -11.3% | -0.0331 to 0.00313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 224 | 196 | -12.5% | -63.3 to 7.46 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.364 | -13.2% | -0.122 to 0.0113 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.3 |  | 11.9 to 30.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
