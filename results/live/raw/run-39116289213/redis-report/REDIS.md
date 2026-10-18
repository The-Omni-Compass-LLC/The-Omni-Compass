# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -0.927 to 0.78 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.049 to 0.024 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000882 to 0.000613 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.0268 to 0.0296 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.27 | +0.1% | -0.0575 to 0.0731 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.54 | -0.0% | -0.00796 to 0.00682 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -2.04 to -0.807 | GAIN |
| memory used, mean (MB) | 57.2 | 56.7 | -0.8% | -1.21 to 0.26 | EVEN, no difference beyond the noise |
| keys evicted | 71,713 | 71,756 | +0.1% | -198 to 284 | shown, not judged |
| host CPU busy (share of the run) | 0.0537 | 0.0538 | +0.2% | -0.0512 to 0.0515 | EVEN, no difference beyond the noise |
| host CPU-seconds | 37.5 | 37.8 | +0.7% | -38.2 to 38.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.194 | 0.195 | +0.7% | -0.197 to 0.2 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 5.33 |  | 2.46 to 8.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 5.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 19.9 to 22.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000514 to 0.00154 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0134 to 0.0153 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.5 | -0.1% | -0.032 to 0.0171 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.00835 to 0.00885 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.96 | 0.884 | -7.8% | -0.0806 to -0.07 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | -0.0215 to 3.43 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.5 | +1.9% | -0.000725 to 2.3 | EVEN, no difference beyond the noise |
| keys evicted | 103,486 | 93,949 | -9.2% | -9,894 to -9,180 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.0947 | -9.5% | -0.0748 to 0.0548 | EVEN, no difference beyond the noise |
| host CPU-seconds | 185 | 166 | -10.5% | -145 to 106 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.324 | 0.285 | -12.0% | -0.258 to 0.18 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.7 |  | 15.5 to 25.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 936 | +1.3% | 9.55 to 13.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0581 to 0.024 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00721 to 0.00867 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0216 to 0.0199 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.36 | 5.51 | +2.7% | -0.186 to 0.473 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.06 | 2.02 | -1.7% | -0.0641 to -0.0065 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.05 to 1.61 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 0.982 to 1.41 | power given |
| keys evicted | 243,246 | 235,808 | -3.1% | -12,333 to -2,542 | shown, not judged |
| host CPU busy (share of the run) | 0.0742 | 0.0598 | -19.4% | -0.078 to 0.0492 | EVEN, no difference beyond the noise |
| host CPU-seconds | 132 | 105 | -20.7% | -147 to 92 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.318 | 0.249 | -21.7% | -0.355 to 0.217 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12 |  | 9.52 to 14.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 9.82 to 15.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00602 to 0.00469 | EVEN, the same |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.0065 to 0.0107 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0281 to 0.00359 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.1% | -0.0122 to 0.00264 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.24 | 1.19 | -3.9% | -0.0644 to -0.0318 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.876 to 2.37 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.332 to 1.86 | power given |
| keys evicted | 137,998 | 133,566 | -3.2% | -6,957 to -1,905 | shown, not judged |
| host CPU busy (share of the run) | 0.0992 | 0.108 | +9.1% | -0.0089 to 0.0269 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 192 | +10.3% | -16.8 to 52.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.326 | 0.356 | +9.1% | -0.0347 to 0.094 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 21.5 to 26.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 27.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
