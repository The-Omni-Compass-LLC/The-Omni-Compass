# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | +0.0% | -1.74 to 2.24 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00789 to 0.00949 | EVEN, the same |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.00122 to 0.00148 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00633 to 0.00718 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.0111 to 0.0261 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.71 | 1.71 | +0.1% | -0.0179 to 0.023 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.1% | -3.84 to -0.133 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.9% | -3.19 to 1.03 | EVEN, no difference beyond the noise |
| keys evicted | 71,718 | 71,693 | -0.0% | -406 to 358 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.161 | +20.9% | -0.0293 to 0.0848 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.3 | 114 | +24.3% | -23 to 67.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.472 | 0.586 | +24.3% | -0.12 to 0.349 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 6.7 to 29.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00145 to 0.00222 | EVEN, the same |
| cache hit rate | 0.844 | 0.857 | +1.5% | 0.00456 to 0.0205 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00765 to 0.00826 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.26 | +0.1% | -0.00576 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.89 | 0.828 | -6.9% | -0.103 to -0.0206 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | -0.506 to 3.47 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62 | +1.2% | 0.398 to 1.02 | power given |
| keys evicted | 103,739 | 95,343 | -8.1% | -13,699 to -3,094 | shown, not judged |
| host CPU busy (share of the run) | 0.0702 | 0.0607 | -13.5% | -0.0354 to 0.0164 | EVEN, no difference beyond the noise |
| host CPU-seconds | 125 | 107 | -14.4% | -66.5 to 30.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.22 | 0.186 | -15.6% | -0.119 to 0.05 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 18.5 to 23.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.9 to 12.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0239 to 0.0128 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00732 to 0.00805 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.61 | -0.1% | -0.0197 to 0.00725 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0138 to 0.0137 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.19 | 2.15 | -2.0% | -0.0531 to -0.0348 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.17 to 1.48 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.23 to 1.29 | power given |
| keys evicted | 243,136 | 234,806 | -3.4% | -8,587 to -8,074 | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.135 | -1.0% | -0.0388 to 0.0361 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 242 | -0.8% | -78.2 to 74.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.585 | 0.572 | -2.1% | -0.194 to 0.17 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 6.39 to 23.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 0.877 to 17.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00114 to 0.00553 | GAIN |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00062 to 0.0121 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00956 to 0.0124 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.00974 to 0.0345 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.1% | -0.0562 to -0.000691 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.164 to 3.05 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% | -0.225 to 2.58 | EVEN, no difference beyond the noise |
| keys evicted | 138,076 | 134,058 | -2.9% | -9,172 to 1,136 | shown, not judged |
| host CPU busy (share of the run) | 0.132 | 0.14 | +5.7% | -0.0266 to 0.0417 | EVEN, no difference beyond the noise |
| host CPU-seconds | 221 | 236 | +6.7% | -53.4 to 83 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.415 | 0.439 | +5.9% | -0.106 to 0.155 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.7 |  | 2.54 to 30.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
