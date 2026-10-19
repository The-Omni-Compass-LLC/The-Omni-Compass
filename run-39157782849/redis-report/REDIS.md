# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.23 to -0.348 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00857 to 0.00768 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00116 to 3.92e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.0139 to 0.0148 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.3% | -0.0255 to 0.0586 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.76 | +0.7% | -0.0109 to 0.0341 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.3 | -2.6% | -2.01 to -1.3 | GAIN |
| memory used, mean (MB) | 57.2 | 56.4 | -1.3% | -1.15 to -0.377 | GAIN |
| keys evicted | 71,770 | 71,934 | +0.2% | 52.5 to 276 | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.121 | -7.3% | -0.0395 to 0.0206 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.6 | 79.4 | -8.3% | -30.1 to 15.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.447 | 0.41 | -8.2% | -0.155 to 0.0818 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 0.343 to 34.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00246 to 0.00184 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.000309 to 0.0232 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.0147 to 0.0126 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.00788 to 0.0165 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.987 | -5.8% | -0.129 to 0.00637 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.5% | 0.069 to 1.79 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | 0.0793 to 1.22 | power given |
| keys evicted | 103,279 | 95,591 | -7.4% | -15,396 to 20.7 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.115 | -0.7% | -0.028 to 0.0264 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 193 | -0.6% | -54.1 to 52 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.34 | 0.333 | -1.9% | -0.0971 to 0.084 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 9.32 to 30 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 932 | +0.7% | -4.7 to 18.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0192 to 0.00933 | EVEN, no difference beyond the noise |
| cache hit rate | 0.618 | 0.622 | +0.7% | -0.00319 to 0.0122 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.19 | 5.2 | +0.0% | -0.00224 to 0.00411 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.1% | -0.00848 to 0.0232 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.04 | 2.01 | -1.1% | -0.0651 to 0.0217 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | -0.000298 to 2.44 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 61.5 | +1.4% | -0.257 to 1.95 | EVEN, no difference beyond the noise |
| keys evicted | 243,062 | 238,956 | -1.7% | -13,568 to 5,355 | shown, not judged |
| host CPU busy (share of the run) | 0.0493 | 0.0543 | +10.3% | -0.0138 to 0.024 | EVEN, no difference beyond the noise |
| host CPU-seconds | 86.2 | 95.5 | +10.8% | -25.8 to 44.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.207 | 0.228 | +10.0% | -0.0616 to 0.103 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16 |  | 5.17 to 26.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,193 | +0.9% | 5.13 to 16.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0244 to 0.0333 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.9% | 0.00317 to 0.0109 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.1% | -0.0197 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.27 | -0.2% | -0.0311 to 0.00718 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.14 | -3.6% | -0.0651 to -0.0201 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.783 to 1.84 | power given |
| memory used, mean (MB) | 61.2 | 62.1 | +1.5% | 0.42 to 1.37 | power given |
| keys evicted | 138,152 | 134,219 | -2.8% | -6,556 to -1,310 | shown, not judged |
| host CPU busy (share of the run) | 0.0725 | 0.0709 | -2.2% | -0.054 to 0.0508 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 126 | -2.0% | -103 to 97.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.242 | 0.235 | -2.8% | -0.194 to 0.181 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
