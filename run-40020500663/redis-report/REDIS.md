# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,076 | +0.1% | -0.403 to 1.95 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00668 to 0.00109 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | +0.0% | -0.000731 to 0.00106 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.00952 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.34 | 5.31 | -0.5% | -0.233 to 0.18 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.54 | -0.4% | -0.0243 to 0.0117 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.65 to -1.31 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.751 to -0.384 | GAIN |
| keys evicted | 71,730 | 71,700 | -0.0% | -252 to 191 | shown, not judged |
| host CPU busy (share of the run) | 0.0669 | 0.0752 | +12.4% | -0.0808 to 0.0974 | EVEN, no difference beyond the noise |
| host CPU-seconds | 47.6 | 53.5 | +12.5% | -61.8 to 73.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.246 | 0.276 | +12.4% | -0.319 to 0.38 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 18.7 to 23.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00174 to 0.00268 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0124 to 0.0159 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 5.59 | -0.6% | -0.0679 to 0.00279 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.2% | -0.0377 to 0.0135 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.981 | 0.898 | -8.5% | -0.0935 to -0.073 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | 0.579 to 1.4 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | 0.249 to 1.08 | power given |
| keys evicted | 103,420 | 94,114 | -9.0% | -10,456 to -8,156 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.105 | +1.5% | -0.0614 to 0.0644 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 186 | +2.5% | -120 to 129 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.319 | 0.321 | +0.8% | -0.213 to 0.218 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.54 to 12.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0877 to 0.0213 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.625 | +1.2% | 0.00644 to 0.00822 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.65 | +0.1% | 0.000403 to 0.00655 | LOSS |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.2% | 0.00437 to 0.0209 | LOSS |
| latency, mean (ms) | 2.22 | 2.18 | -1.6% | -0.0427 to -0.0296 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.32 to 1.5 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.21 to 1.27 | power given |
| keys evicted | 242,995 | 234,914 | -3.3% | -8,712 to -7,450 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.14 | -2.4% | -0.0279 to 0.021 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 243 | -2.9% | -56.6 to 42.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.599 | 0.575 | -4.0% | -0.142 to 0.094 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12.3 |  | 9.46 to 15.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,181 | 1,195 | +1.1% | 9.63 to 16.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00907 to 0.00179 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.0064 to 0.0111 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.0% | -0.00504 to 0.00228 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.32 | 5.32 | -0.1% | -0.0422 to 0.0335 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.14 | -3.8% | -0.0589 to -0.0318 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.17 to 2.01 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 0.985 to 1.32 | power given |
| keys evicted | 138,312 | 133,229 | -3.7% | -6,694 to -3,472 | shown, not judged |
| host CPU busy (share of the run) | 0.0649 | 0.0679 | +4.6% | -0.0367 to 0.0426 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 120 | +5.1% | -68.4 to 80 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.215 | 0.223 | +4.0% | -0.13 to 0.147 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
