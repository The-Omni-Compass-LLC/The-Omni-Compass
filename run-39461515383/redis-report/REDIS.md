# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,074 | -0.1% | -2.58 to 0.403 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0107 to 0.0012 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000624 to 0.000369 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% | -0.00167 to 0.0101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.35 | +1.7% | -0.0335 to 0.208 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.55 | +0.8% | -0.0105 to 0.0342 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.79 to -1.41 | GAIN |
| memory used, mean (MB) | 57.1 | 56.5 | -1.2% | -0.922 to -0.421 | GAIN |
| keys evicted | 71,690 | 71,744 | +0.1% | -99.1 to 207 | shown, not judged |
| host CPU busy (share of the run) | 0.0713 | 0.0701 | -1.6% | -0.0642 to 0.0619 | EVEN, no difference beyond the noise |
| host CPU-seconds | 50.8 | 49.8 | -2.0% | -49.1 to 47.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.263 | 0.258 | -1.9% | -0.254 to 0.244 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% | 5.27 to 20 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00317 to 0.00404 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | 0.0036 to 0.0133 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.00768 to 0.00155 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.0004 to 0.0122 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.01 | -4.1% | -0.0695 to -0.0159 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.1% | -2.96 to 2.83 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.7 | -0.9% | -3.15 to 2.04 | EVEN, no difference beyond the noise |
| keys evicted | 103,319 | 97,971 | -5.2% | -8,737 to -1,959 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.12 | +4.9% | -0.00879 to 0.0199 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 201 | +5.6% | -16.6 to 37.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.334 | 0.349 | +4.5% | -0.0306 to 0.0608 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24.7 |  | 16.7 to 32.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 11.1 to 13.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0071 to -0.000558 | LOSS |
| cache hit rate | 0.617 | 0.626 | +1.3% | 0.00744 to 0.0092 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.00853 to 0.00473 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.00637 to 0.0159 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% | -0.0514 to -0.0368 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.2 to 1.62 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.818 to 1.39 | power given |
| keys evicted | 243,244 | 238,747 | -1.8% | -13,177 to 4,183 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.132 | -0.8% | -0.0219 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 219 | -0.9% | -42.6 to 38.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.532 | 0.52 | -2.2% | -0.109 to 0.0862 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.3 |  | 10.2 to 20.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | 2.32 to 17.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00846 to 0.00831 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00177 to 0.0116 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0493 to 0.03 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.8 | -0.1% | -0.0599 to 0.0524 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -2.7% | -0.0799 to 0.00601 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | -0.323 to 3.25 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% | -0.045 to 2.17 | EVEN, no difference beyond the noise |
| keys evicted | 138,252 | 134,561 | -2.7% | -7,014 to -369 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.121 | -5.4% | -0.0126 to -0.0012 | GAIN |
| host CPU-seconds | 215 | 202 | -5.7% | -23.8 to -0.736 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.403 | 0.377 | -6.5% | -0.0462 to -0.00622 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 12.6 to 24.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
