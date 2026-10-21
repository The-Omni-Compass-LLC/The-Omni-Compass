# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.94 to 2.11 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0336 to 0.0567 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00177 to 0.00126 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% | -0.00884 to 0.0211 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.3% | 0.01 to 0.0225 | LOSS |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00504 to 0.0204 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.8 | -3.4% | -4.09 to -0.262 | GAIN |
| memory used, mean (MB) | 57.2 | 55.9 | -2.2% | -3.16 to 0.667 | EVEN, no difference beyond the noise |
| keys evicted | 71,755 | 71,829 | +0.1% | -283 to 431 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.153 | +5.5% | -0.058 to 0.0739 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98 | 104 | +6.0% | -46.4 to 58.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.506 | 0.536 | +6.0% | -0.24 to 0.301 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 13.1 to 26 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00236 to 0.00283 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.00903 to 0.0171 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.5 | -0.2% | -0.0278 to 0.00602 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.0022 to 0.00761 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.959 | 0.891 | -7.1% | -0.0932 to -0.0427 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -2.71 to 4.16 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.6% | -2.77 to 3.55 | EVEN, no difference beyond the noise |
| keys evicted | 103,376 | 94,864 | -8.2% | -11,507 to -5,518 | shown, not judged |
| host CPU busy (share of the run) | 0.0913 | 0.0901 | -1.3% | -0.0177 to 0.0153 | EVEN, no difference beyond the noise |
| host CPU-seconds | 158 | 156 | -1.4% | -33.3 to 29 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.278 | 0.27 | -2.9% | -0.0635 to 0.0476 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 9.85 to 36.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.2 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0183 to 0.00699 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00681 to 0.00829 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.65 | +0.1% | -0.00395 to 0.0176 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.72 | +0.2% | 0.0102 to 0.0177 | LOSS |
| latency, mean (ms) | 2.21 | 2.18 | -1.5% | -0.0515 to -0.016 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.06 to 1.57 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.14 to 1.31 | power given |
| keys evicted | 243,139 | 234,908 | -3.4% | -8,723 to -7,737 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.13 | +4.3% | -0.0367 to 0.0473 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 228 | +4.9% | -72.2 to 93.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.522 | 0.54 | +3.6% | -0.178 to 0.216 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 8.03 to 18 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +0.9% | 5.81 to 15.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00405 to 0.00634 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +0.9% | 0.00378 to 0.0105 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.00197 to 0.00311 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.00146 to 0.0141 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.6% | -0.0503 to -0.0185 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.156 to 2.42 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.0215 to 1.91 | power given |
| keys evicted | 138,111 | 134,108 | -2.9% | -6,276 to -1,730 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.13 | +6.2% | -0.037 to 0.0522 | EVEN, no difference beyond the noise |
| host CPU-seconds | 206 | 220 | +7.2% | -71.4 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.386 | 0.41 | +6.2% | -0.137 to 0.185 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
