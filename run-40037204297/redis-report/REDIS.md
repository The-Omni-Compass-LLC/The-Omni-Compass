# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -2.55 to 0.574 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00987 to 0.0259 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00166 to 0.000426 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.0173 to 0.0219 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.2% | -0.0025 to 0.0204 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.74 | +0.5% | -0.00116 to 0.0192 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.9 | -1.7% | -2.21 to 0.0463 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 56.6 | -1.0% | -0.891 to -0.219 | GAIN |
| keys evicted | 71,629 | 71,807 | +0.2% | -129 to 486 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.142 | +2.0% | -0.053 to 0.0585 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.1 | 95.8 | +1.9% | -42.4 to 45.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.485 | 0.495 | +2.0% | -0.218 to 0.237 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,262 | 1,282 | +1.6% | 9.34 to 30.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00217 to 0.00281 | EVEN, the same |
| cache hit rate | 0.844 | 0.858 | +1.6% | 0.00603 to 0.0207 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.3% | -0.0474 to 0.02 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.25 | -0.7% | -0.146 to 0.0715 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.905 | 0.831 | -8.2% | -0.0994 to -0.0497 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66 | +3.2% | -1.44 to 5.53 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.5 | +1.9% | -0.746 to 3.1 | EVEN, no difference beyond the noise |
| keys evicted | 103,897 | 94,920 | -8.6% | -14,322 to -3,631 | shown, not judged |
| host CPU busy (share of the run) | 0.0675 | 0.062 | -8.1% | -0.0338 to 0.0228 | EVEN, no difference beyond the noise |
| host CPU-seconds | 119 | 110 | -8.3% | -62.5 to 42.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.21 | 0.19 | -9.7% | -0.111 to 0.0703 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16.7 to 25.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 9.48 to 13.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0264 to 0.0295 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00631 to 0.00924 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.53 | -0.0% | -0.0129 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.59 | 5.59 | +0.0% | -0.00463 to 0.00597 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.11 | -1.9% | -0.047 to -0.0362 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.00756 to 3.17 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.13 to 1.36 | power given |
| keys evicted | 243,117 | 235,515 | -3.1% | -10,030 to -5,174 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.114 | +5.3% | -0.0177 to 0.0291 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 200 | +6.0% | -32.8 to 55.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.452 | 0.474 | +4.7% | -0.0836 to 0.126 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 10 to 20 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 4.03 to 14.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00301 to 0.0106 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00271 to 0.00981 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.012 to 0.0126 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.00725 to 0.0209 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.3% | -0.0553 to -0.00752 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.9% | 0.651 to 1.76 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | 0.347 to 1.3 | power given |
| keys evicted | 138,068 | 134,948 | -2.3% | -4,352 to -1,889 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.125 | +5.1% | -0.0184 to 0.0305 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 211 | +5.9% | -35.2 to 58.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.374 | 0.393 | +5.1% | -0.0696 to 0.108 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 8.13 to 30.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
