# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | +0.0% | -0.16 to 0.241 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0317 to 0.0642 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00023 to 0.000223 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0188 to 0.0166 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.0161 to 0.0335 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.0% | -0.00801 to 0.00955 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.71 to -1.49 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% | -0.74 to -0.582 | GAIN |
| keys evicted | 71,778 | 71,793 | +0.0% | -15.1 to 45.1 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.131 | -5.8% | -0.0727 to 0.0567 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.1 | 86.9 | -6.7% | -56.9 to 44.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.481 | 0.449 | -6.7% | -0.294 to 0.23 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% | -14.2 to 38.5 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00281 to 0.00195 | EVEN, the same |
| cache hit rate | 0.845 | 0.853 | +1.0% | -0.00956 to 0.0259 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.00513 to 0.00681 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | 0.00635 to 0.0125 | LOSS |
| latency, mean (ms) | 1.05 | 1 | -3.9% | -0.138 to 0.0559 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.1 | +0.2% | -2.1 to 2.38 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.3 | -0.0% | -2.2 to 2.17 | EVEN, no difference beyond the noise |
| keys evicted | 103,208 | 97,902 | -5.1% | -17,228 to 6,616 | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.113 | -1.7% | -0.00891 to 0.00494 | EVEN, no difference beyond the noise |
| host CPU-seconds | 192 | 189 | -1.8% | -17.4 to 10.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.337 | 0.328 | -2.8% | -0.027 to 0.0084 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 12.7 to 27.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.8 to 11.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0311 to 0.0194 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00718 to 0.00787 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.68 | +0.0% | -0.00862 to 0.0121 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.73 | +0.2% | -0.0062 to 0.0235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0441 to -0.0331 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.34 to 1.47 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.19 to 1.27 | power given |
| keys evicted | 243,119 | 234,890 | -3.4% | -8,456 to -8,001 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.132 | -2.6% | -0.0306 to 0.0235 | EVEN, no difference beyond the noise |
| host CPU-seconds | 226 | 220 | -2.9% | -58.2 to 45.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.543 | 0.521 | -4.0% | -0.145 to 0.101 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 13 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +1.0% | 2.47 to 20.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00292 to 0.00448 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00155 to 0.0135 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.0126 to 0.0163 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.79 | +0.1% | -0.00348 to 0.0195 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.3 | -2.8% | -0.0708 to -0.00518 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.478 to 2.97 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | -0.237 to 2.18 | EVEN, no difference beyond the noise |
| keys evicted | 138,126 | 133,870 | -3.1% | -8,284 to -228 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.107 | -5.5% | -0.00696 to -0.00538 | GAIN |
| host CPU-seconds | 188 | 176 | -6.0% | -12.6 to -9.82 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.352 | 0.328 | -6.9% | -0.0248 to -0.0236 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
