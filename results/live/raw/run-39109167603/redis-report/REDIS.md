# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.1% | -2.46 to 1.33 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0466 to 0.072 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00169 to 0.00107 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% | -0.018 to 0.0295 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.82 | +0.3% | -0.0383 to 0.0769 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.6% | -0.00473 to 0.0261 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.2 | -2.9% | -5.08 to 1.41 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 56 | -2.0% | -3.89 to 1.64 | EVEN, no difference beyond the noise |
| keys evicted | 71,703 | 71,795 | +0.1% | -232 to 417 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.132 | +0.4% | -0.019 to 0.02 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.6 | 87.8 | +0.2% | -14.4 to 14.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.452 | 0.453 | +0.3% | -0.0734 to 0.0759 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,289 | +1.7% | 19.3 to 23.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00432 to 0.00244 | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.7% | 0.0129 to 0.0157 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.3% | -0.0479 to 0.0768 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.67 | +0.2% | -0.023 to 0.0507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.941 | 0.871 | -7.4% | -0.0757 to -0.0638 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.06 to 1.73 | power given |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% | 0.959 to 1.25 | power given |
| keys evicted | 103,173 | 93,754 | -9.1% | -10,354 to -8,485 | shown, not judged |
| host CPU busy (share of the run) | 0.0904 | 0.0806 | -10.8% | -0.0641 to 0.0446 | EVEN, no difference beyond the noise |
| host CPU-seconds | 160 | 142 | -11.3% | -122 to 85.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.244 | -12.8% | -0.213 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19.3 |  | 17.9 to 20.8 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.1 to 12.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0164 to -0.00186 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00691 to 0.00847 | GAIN |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.0% | -0.00259 to 0.00638 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.2% | 0.00371 to 0.0135 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0406 to -0.037 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.17 to 1.62 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.9% | 0.897 to 1.39 | power given |
| keys evicted | 243,066 | 237,940 | -2.1% | -12,540 to 2,287 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.15 | +14.1% | -0.00104 to 0.0381 | EVEN, no difference beyond the noise |
| host CPU-seconds | 218 | 254 | +16.7% | -1.31 to 74.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.523 | 0.603 | +15.3% | -0.00895 to 0.169 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.3 |  | 10.5 to 18.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,195 | +1.1% | 6.32 to 18.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0298 to 0.0327 | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% | 0.00387 to 0.0127 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% | -0.0223 to 0.0222 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.0% | -0.0429 to 0.0393 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -4.2% | -0.0714 to -0.026 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 0.996 to 2.05 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% | 0.649 to 1.47 | power given |
| keys evicted | 138,229 | 133,460 | -3.5% | -7,752 to -1,786 | shown, not judged |
| host CPU busy (share of the run) | 0.0676 | 0.0636 | -5.9% | -0.0611 to 0.0531 | EVEN, no difference beyond the noise |
| host CPU-seconds | 121 | 113 | -6.6% | -116 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.227 | 0.21 | -7.6% | -0.22 to 0.186 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
