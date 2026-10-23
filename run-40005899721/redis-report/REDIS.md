# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.88 to 0.443 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00651 to 0.00381 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00123 to 0.000443 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.0184 to 0.0108 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0158 to 0.0241 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.74 | +0.5% | -0.00577 to 0.0226 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.9 | -3.2% | -4.3 to 0.177 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 56 | -1.9% | -3.4 to 1.19 | EVEN, no difference beyond the noise |
| keys evicted | 71,747 | 71,875 | +0.2% | -93.1 to 349 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.135 | -3.0% | -0.0535 to 0.045 | EVEN, no difference beyond the noise |
| host CPU-seconds | 94.4 | 90.8 | -3.8% | -41.8 to 34.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.488 | 0.469 | -3.8% | -0.216 to 0.179 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.6% | 16.3 to 25.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0491 to 0.0808 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0113 to 0.0167 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.48 | -0.2% | -0.0351 to 0.0104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.00622 to 0.0103 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.956 | 0.883 | -7.6% | -0.0965 to -0.0495 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.904 to 1.93 | power given |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% | 1.07 to 1.15 | power given |
| keys evicted | 103,241 | 93,999 | -9.0% | -11,045 to -7,438 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.103 | -5.9% | -0.0839 to 0.071 | EVEN, no difference beyond the noise |
| host CPU-seconds | 194 | 181 | -6.8% | -165 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.313 | -8.3% | -0.293 to 0.237 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 16.8 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.5 to 13.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0183 to 0.0045 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00706 to 0.00892 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% | -0.000487 to 0.00362 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.57 | 5.58 | +0.1% | 0.00361 to 0.0055 | LOSS |
| latency, mean (ms) | 2.14 | 2.1 | -1.9% | -0.0464 to -0.0345 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.446 to 2.73 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.697 to 1.62 | power given |
| keys evicted | 243,285 | 236,617 | -2.7% | -14,264 to 927 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.0997 | -4.4% | -0.0288 to 0.0195 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 173 | -4.9% | -55.4 to 37.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.41 | -6.1% | -0.137 to 0.0835 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 1.85 to 28.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +1.0% | 4.34 to 18.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00443 to 0.0107 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00286 to 0.0124 | GAIN |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.0% | -0.0116 to 0.014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.0123 to 0.0233 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.3 | -2.8% | -0.0661 to -0.0105 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 0.219 to 2.45 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.0419 to 1.96 | power given |
| keys evicted | 138,139 | 133,815 | -3.1% | -7,559 to -1,088 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.129 | +12.7% | -0.0192 to 0.0481 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 218 | +14.8% | -36.3 to 92.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.405 | +13.8% | -0.0725 to 0.171 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.7 |  | 12.1 to 27.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
