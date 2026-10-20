# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -2.06 to 1.95 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0171 to 0.0174 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00115 to 0.000668 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0108 to 0.00727 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.0% | -0.0285 to 0.031 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.72 | -0.2% | -0.0237 to 0.0164 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.2% | -3.83 to -0.32 | GAIN |
| memory used, mean (MB) | 57.2 | 56 | -2.0% | -2.92 to 0.66 | EVEN, no difference beyond the noise |
| keys evicted | 71,728 | 71,811 | +0.1% | -195 to 360 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.153 | +5.7% | 0.00379 to 0.0126 | power given |
| host CPU-seconds | 99.5 | 106 | +6.8% | 3.97 to 9.47 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.514 | 0.549 | +6.8% | 0.0202 to 0.0493 | power given |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,279 | +1.0% | 10 to 14.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00195 to 0.00116 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | 0.00641 to 0.0106 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.1% | -0.00961 to 0.0012 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% | 0.000762 to 0.00248 | LOSS |
| latency, mean (ms) | 1.02 | 0.979 | -4.3% | -0.052 to -0.0359 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.8 | -0.3% | -2.02 to 1.67 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 60.6 | -1.1% | -1.9 to 0.505 | EVEN, no difference beyond the noise |
| keys evicted | 103,351 | 97,986 | -5.2% | -6,480 to -4,250 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.133 | +7.0% | -0.00879 to 0.0263 | EVEN, no difference beyond the noise |
| host CPU-seconds | 213 | 232 | +8.5% | -17.4 to 53.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.374 | 0.402 | +7.5% | -0.0333 to 0.0895 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24.3 |  | 12.6 to 36.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 11 to 12.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.028 to 0.0144 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00733 to 0.00824 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% | -0.0229 to 0.0267 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.58 | +0.1% | -0.0117 to 0.0207 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.1 | -1.9% | -0.0537 to -0.0286 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.16 to 1.6 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.19 to 1.31 | power given |
| keys evicted | 243,238 | 234,827 | -3.5% | -8,760 to -8,061 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.11 | +1.6% | -0.0401 to 0.0436 | EVEN, no difference beyond the noise |
| host CPU-seconds | 189 | 192 | +2.0% | -77.1 to 84.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.456 | +0.7% | -0.189 to 0.195 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 6.08 to 21.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.5% | 2.68 to 10.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00656 to 0.00481 | EVEN, the same |
| cache hit rate | 0.79 | 0.794 | +0.6% | 0.00185 to 0.00698 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.00389 to 0.0179 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | 0.00154 to 0.0248 | LOSS |
| latency, mean (ms) | 1.35 | 1.33 | -1.3% | -0.0313 to -0.00284 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.0% | 0.0608 to 1.27 | power given |
| memory used, mean (MB) | 61.2 | 61.7 | +0.8% | 0.0276 to 0.892 | power given |
| keys evicted | 138,029 | 136,417 | -1.2% | -4,474 to 1,249 | shown, not judged |
| host CPU busy (share of the run) | 0.117 | 0.137 | +16.9% | -0.00123 to 0.0409 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 232 | +19.4% | -1.42 to 76.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.365 | 0.434 | +18.7% | -0.00385 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 11.2 to 25.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
