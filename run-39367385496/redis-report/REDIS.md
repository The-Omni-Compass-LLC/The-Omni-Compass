# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.477 to -0.22 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0209 to 0.0145 | EVEN, no difference beyond the noise |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.000336 to -1.23e-05 | LOSS |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% | -0.0158 to 0.0149 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.84 | +0.2% | -0.0114 to 0.0319 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% | -0.00632 to 0.0157 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.91 to -1.03 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.931 to -0.129 | GAIN |
| keys evicted | 71,797 | 71,849 | +0.1% | 28.1 to 75.3 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.121 | -1.5% | -0.0729 to 0.0691 | EVEN, no difference beyond the noise |
| host CPU-seconds | 81.4 | 79.8 | -2.0% | -55 to 51.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.412 | -2.0% | -0.284 to 0.267 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 5.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 18.4 to 24.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000341 to 0.00146 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0123 to 0.0162 | GAIN |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.1% | -0.0108 to 0.000923 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.72 | +0.0% | -0.00474 to 0.00601 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.01 | 0.937 | -7.7% | -0.0925 to -0.0631 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.5% | 0.636 to 1.24 | power given |
| memory used, mean (MB) | 61.3 | 62.1 | +1.3% | 0.481 to 1.09 | power given |
| keys evicted | 103,450 | 94,081 | -9.1% | -10,657 to -8,080 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.114 | -8.3% | -0.032 to 0.0113 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 195 | -9.2% | -62.1 to 22.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.336 | -10.7% | -0.115 to 0.0344 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 21 to 21 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 921 | 934 | +1.4% | 11.3 to 14.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0976 to 0.119 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.4% | 0.00766 to 0.00943 | GAIN |
| latency, 95th percentile (ms) | 5.87 | 5.85 | -0.4% | -0.166 to 0.115 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.61 | 7.46 | -2.0% | -0.589 to 0.291 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.36 | 2.3 | -2.3% | -0.0882 to -0.0224 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 0.711 to 2.35 | power given |
| memory used, mean (MB) | 60.7 | 61.7 | +1.7% | 0.889 to 1.16 | power given |
| keys evicted | 243,398 | 239,575 | -1.6% | -9,473 to 1,827 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.149 | -0.0% | -0.0248 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 260 | 261 | +0.3% | -50.1 to 51.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.628 | 0.621 | -1.1% | -0.13 to 0.115 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 11.7 |  | 7.87 to 15.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `15654388e112`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,192 | +0.7% | -0.434 to 16.4 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00838 to 0.0123 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.795 | +0.7% | -0.000402 to 0.0112 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.0405 to 0.0295 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | -0.0% | -0.0419 to 0.0417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.1% | -0.0731 to 0.0152 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | -0.0752 to 2.08 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | 0.234 to 1.33 | power given |
| keys evicted | 138,187 | 135,372 | -2.0% | -6,720 to 1,091 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.118 | -5.8% | -0.109 to 0.0945 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 196 | -6.6% | -206 to 178 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.394 | 0.365 | -7.3% | -0.39 to 0.333 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17 |  | 7.06 to 26.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
