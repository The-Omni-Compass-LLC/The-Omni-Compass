# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | +0.0% | -3.53 to 3.67 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0147 to 0.013 | EVEN, the same |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.00182 to 0.00203 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% | -0.0124 to 0.00729 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | -0.1% | -0.0291 to 0.0225 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.53 | -0.1% | -0.0224 to 0.0187 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.94 to -1.02 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -1.0% | -1.03 to -0.104 | GAIN |
| keys evicted | 71,722 | 71,703 | -0.0% | -542 to 504 | shown, not judged |
| host CPU busy (share of the run) | 0.0435 | 0.0428 | -1.7% | -0.043 to 0.0416 | EVEN, no difference beyond the noise |
| host CPU-seconds | 30.1 | 29.6 | -1.4% | -30.7 to 29.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.155 | 0.153 | -1.4% | -0.158 to 0.154 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,284 | +1.4% | 13.6 to 22.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00226 to 0.00189 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.5% | 0.00675 to 0.0179 | GAIN |
| latency, 95th percentile (ms) | 5.77 | 5.73 | -0.6% | -0.15 to 0.0825 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.92 | 5.81 | -1.8% | -0.519 to 0.308 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.07 | 0.992 | -7.3% | -0.104 to -0.0516 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.5% | 0.158 to 1.71 | power given |
| memory used, mean (MB) | 61.3 | 61.8 | +0.8% | 0.00204 to 1.02 | power given |
| keys evicted | 103,631 | 95,490 | -7.9% | -12,156 to -4,127 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.131 | +8.1% | -0.0036 to 0.0233 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 223 | +10.4% | -5.11 to 47 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.354 | 0.385 | +8.8% | -0.0145 to 0.077 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 17.7 to 26.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.8 to 11.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0196 to -0.00428 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00726 to 0.00781 | GAIN |
| latency, 95th percentile (ms) | 5.56 | 5.56 | +0.0% | -0.0117 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.64 | 5.65 | +0.1% | -0.005 to 0.0153 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.11 | -1.8% | -0.0493 to -0.0278 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.19 to 1.72 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.19 to 1.33 | power given |
| keys evicted | 243,168 | 234,940 | -3.4% | -8,422 to -8,036 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.112 | -2.0% | -0.0409 to 0.0363 | EVEN, no difference beyond the noise |
| host CPU-seconds | 203 | 199 | -2.2% | -81.7 to 72.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.487 | 0.471 | -3.3% | -0.2 to 0.167 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 8.03 to 18 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.1% | 10.7 to 15.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0277 to 0.0263 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00704 to 0.0111 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0128 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | +0.0% | -0.023 to 0.027 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -3.7% | -0.0501 to -0.0359 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.8 | +2.8% | 1.66 to 1.87 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 1.15 to 1.34 | power given |
| keys evicted | 138,193 | 132,884 | -3.8% | -6,703 to -3,917 | shown, not judged |
| host CPU busy (share of the run) | 0.0571 | 0.0655 | +14.8% | -0.0329 to 0.0498 | EVEN, no difference beyond the noise |
| host CPU-seconds | 101 | 116 | +15.4% | -60.3 to 91.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.189 | 0.216 | +14.1% | -0.116 to 0.17 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
