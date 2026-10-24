# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.79 to 0.0645 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.031 to 0.0536 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.1% | -0.00106 to -4.48e-05 | LOSS |
| latency, 95th percentile (ms) | 5.65 | 5.65 | +0.0% | -0.0116 to 0.0155 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.1% | -0.0139 to 0.0297 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.67 | 1.68 | +0.4% | -0.00888 to 0.0213 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.1 | -3.0% | -3.63 to -0.251 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.9% | -2.85 to 0.706 | EVEN, no difference beyond the noise |
| keys evicted | 71,615 | 71,774 | +0.2% | 24.9 to 294 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.114 | -9.2% | -0.0433 to 0.0201 | EVEN, no difference beyond the noise |
| host CPU-seconds | 89.1 | 79.9 | -10.3% | -34.4 to 16 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.413 | -10.3% | -0.177 to 0.0831 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6.67 |  | 3.8 to 9.54 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,281 | +1.1% | 3.95 to 23.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00227 to 0.0013 | EVEN, the same |
| cache hit rate | 0.845 | 0.854 | +1.1% | 0.00296 to 0.0157 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.0121 to 0.00112 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.00847 to 0.00876 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1 | -4.6% | -0.0873 to -0.00875 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.1 | +0.2% | -2.78 to 3.03 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.1 | -0.4% | -3.44 to 2.96 | EVEN, no difference beyond the noise |
| keys evicted | 103,352 | 97,416 | -5.7% | -9,680 to -2,191 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.129 | +8.0% | -0.0234 to 0.0425 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 219 | +9.4% | -44.1 to 81.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.35 | 0.379 | +8.2% | -0.0832 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 5.79 to 40.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 9.71 to 14 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0169 to 0.00441 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00661 to 0.00922 | GAIN |
| latency, 95th percentile (ms) | 5.19 | 5.19 | -0.0% | -0.000333 to 0.000291 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00415 to 0.00682 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.03 | 1.99 | -2.0% | -0.0459 to -0.0342 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.6% | 1.01 to 2.27 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.29 to 1.35 | power given |
| keys evicted | 243,081 | 235,639 | -3.1% | -11,278 to -3,607 | shown, not judged |
| host CPU busy (share of the run) | 0.0485 | 0.0515 | +6.1% | -0.00849 to 0.0144 | EVEN, no difference beyond the noise |
| host CPU-seconds | 85.1 | 90.6 | +6.5% | -15.9 to 27 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.204 | 0.215 | +5.2% | -0.039 to 0.0602 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10 to 20 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +1.0% | 5.43 to 17.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0168 to 0.0194 | EVEN, the same |
| cache hit rate | 0.79 | 0.797 | +1.0% | 0.00296 to 0.0121 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0368 to 0.02 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.1% | -0.0423 to 0.0339 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.31 | -3.1% | -0.0687 to -0.0164 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.519 to 2.93 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | -0.308 to 2.35 | EVEN, no difference beyond the noise |
| keys evicted | 138,031 | 133,777 | -3.1% | -7,357 to -1,151 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.124 | -0.1% | -0.0269 to 0.0266 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 207 | +0.4% | -52.3 to 53.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.388 | 0.385 | -0.6% | -0.0999 to 0.0954 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.3 |  | 10.7 to 25.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
