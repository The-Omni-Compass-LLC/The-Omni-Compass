# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% | -1.19 to -0.163 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0201 to 0.0298 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.000735 to -0.000127 | LOSS |
| latency, 95th percentile (ms) | 5.71 | 5.71 | +0.0% | -0.0152 to 0.02 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.00193 to 0.0163 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.72 | 1.72 | +0.3% | -0.00181 to 0.0137 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.3% | -1.66 to -1.33 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -1.0% | -0.662 to -0.432 | GAIN |
| keys evicted | 71,672 | 71,802 | +0.2% | 28.3 to 232 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.129 | +9.1% | -0.0101 to 0.0316 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79 | 86.9 | +10.0% | -7.84 to 23.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.407 | 0.449 | +10.1% | -0.0403 to 0.123 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 16 to 22.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00147 to 0.00268 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.0108 to 0.015 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0239 to 0.00691 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | -0.0% | -0.0118 to 0.00728 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.985 | -6.6% | -0.0815 to -0.0584 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.2 | +1.8% | 0.23 to 2.13 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | -0.279 to 1.59 | EVEN, no difference beyond the noise |
| keys evicted | 103,442 | 94,973 | -8.2% | -9,920 to -7,017 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.12 | +0.2% | -0.0394 to 0.0399 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 201 | +0.5% | -75.6 to 77.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.352 | 0.348 | -1.0% | -0.137 to 0.13 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 10.6 to 13.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0251 to 0.00369 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00715 to 0.00886 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00559 to 0.00745 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.0045 to 0.0189 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.8% | -0.0468 to -0.0337 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.26 to 1.65 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.892 to 1.45 | power given |
| keys evicted | 243,233 | 236,824 | -2.6% | -15,320 to 2,503 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.142 | +5.8% | -0.0242 to 0.0397 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 238 | +6.6% | -46.1 to 75.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.535 | 0.563 | +5.3% | -0.117 to 0.173 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 5.93 to 12 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.000519 to 0.00231 | EVEN, the same |
| cache hit rate | 0.79 | 0.796 | +0.8% | 0.00389 to 0.00809 | GAIN |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% | -0.00261 to 0.00264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.72 | 5.73 | +0.1% | -0.00116 to 0.00802 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.31 | 1.28 | -2.4% | -0.0459 to -0.0161 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.8% | 0.439 to 1.85 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.4% | 0.486 to 1.21 | power given |
| keys evicted | 138,020 | 134,806 | -2.3% | -4,641 to -1,786 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.134 | -2.1% | -0.0722 to 0.0663 | EVEN, no difference beyond the noise |
| host CPU-seconds | 241 | 234 | -2.7% | -145 to 132 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.452 | 0.436 | -3.4% | -0.275 to 0.244 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 10.1 to 25.3 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
