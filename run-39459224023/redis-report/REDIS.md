# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.1% | -3.45 to 2.36 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00504 to 0.00527 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00206 to 0.00141 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.57 | 5.57 | +0.0% | -0.0063 to 0.00794 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.63 | +0.1% | -0.00403 to 0.0155 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.63 | +0.1% | -0.0134 to 0.0171 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.46 to -1.33 | GAIN |
| memory used, mean (MB) | 57.1 | 56.7 | -0.8% | -0.53 to -0.412 | GAIN |
| keys evicted | 71,668 | 71,772 | +0.1% | -404 to 613 | shown, not judged |
| host CPU busy (share of the run) | 0.128 | 0.116 | -9.5% | -0.0414 to 0.0171 | EVEN, no difference beyond the noise |
| host CPU-seconds | 91.1 | 81.2 | -10.8% | -33.6 to 13.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.47 | 0.419 | -10.8% | -0.172 to 0.0711 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% | 0.373 to 35.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000369 to 0.00136 | EVEN, the same |
| cache hit rate | 0.845 | 0.857 | +1.4% | 0.000364 to 0.0235 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.1% | -0.00805 to -0.000974 | GAIN |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.0% | -0.00207 to 0.00675 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.987 | -6.0% | -0.128 to 0.00169 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.5 | +0.8% | -1.1 to 2.18 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.4% | -0.919 to 1.42 | EVEN, no difference beyond the noise |
| keys evicted | 103,497 | 95,668 | -7.6% | -15,599 to -58.6 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.109 | +1.6% | -0.00879 to 0.0123 | EVEN, no difference beyond the noise |
| host CPU-seconds | 178 | 182 | +1.9% | -16.5 to 23.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.313 | 0.315 | +0.5% | -0.0297 to 0.0329 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 10.4 to 12.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0395 to 0.0244 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00712 to 0.00826 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0163 to 0.019 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | -0.00466 to 0.0275 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.23 | -1.7% | -0.05 to -0.0282 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.37 to 1.48 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.23 to 1.24 | power given |
| keys evicted | 243,207 | 234,877 | -3.4% | -8,714 to -7,947 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.146 | +2.0% | -0.0119 to 0.0177 | EVEN, no difference beyond the noise |
| host CPU-seconds | 239 | 245 | +2.5% | -23.2 to 35.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.573 | 0.581 | +1.2% | -0.0633 to 0.0776 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,198 | +1.2% | 12.5 to 15 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00134 to 0.0033 | EVEN, the same |
| cache hit rate | 0.79 | 0.799 | +1.2% | 0.00832 to 0.00998 | GAIN |
| latency, 95th percentile (ms) | 5.66 | 5.65 | -0.1% | -0.0422 to 0.0261 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.033 to 0.0275 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.28 | 1.23 | -4.0% | -0.0762 to -0.026 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 1.16 to 2.26 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.1% | 1.08 to 1.48 | power given |
| keys evicted | 138,058 | 132,706 | -3.9% | -5,902 to -4,802 | shown, not judged |
| host CPU busy (share of the run) | 0.102 | 0.0997 | -2.5% | -0.017 to 0.0118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 179 | 174 | -2.7% | -33.5 to 24 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.335 | 0.323 | -3.8% | -0.0669 to 0.0416 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
