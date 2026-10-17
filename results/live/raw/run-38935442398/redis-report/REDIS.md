# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -1.16 to -0.321 | LOSS |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00268 to 0.00253 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.000709 to -0.000142 | LOSS |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00403 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | -3.1e-05 to 0.0235 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.74 | +0.5% | 0.00451 to 0.0131 | LOSS |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.5 | -4.0% | -4.5 to -0.597 | GAIN |
| memory used, mean (MB) | 57.2 | 55.5 | -2.9% | -3.6 to 0.328 | EVEN, no difference beyond the noise |
| keys evicted | 71,737 | 71,873 | +0.2% | 94.8 to 179 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.128 | -2.2% | -0.06 to 0.0542 | EVEN, no difference beyond the noise |
| host CPU-seconds | 87.7 | 85.5 | -2.5% | -45.7 to 41.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.453 | 0.442 | -2.4% | -0.236 to 0.214 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | 16.6 to 23.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00063 to 0.00146 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.6% | 0.0126 to 0.0144 | GAIN |
| latency, 95th percentile (ms) | 5.49 | 5.49 | -0.0% | -0.0215 to 0.0193 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.1% | -0.00608 to 0.0161 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.955 | 0.887 | -7.1% | -0.0854 to -0.0512 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 0.237 to 2.97 | power given |
| memory used, mean (MB) | 61.3 | 62.1 | +1.3% | 0.403 to 1.25 | power given |
| keys evicted | 103,115 | 94,196 | -8.6% | -9,548 to -8,288 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.105 | +5.5% | -0.069 to 0.08 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 186 | +6.0% | -134 to 155 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.321 | +4.3% | -0.239 to 0.265 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.3% | 10.1 to 13.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0155 to 0.0122 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00681 to 0.00912 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.015 to 0.015 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | -0.00111 to 0.0185 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.27 | 2.22 | -1.9% | -0.0554 to -0.0286 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.98 to 1.63 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.579 to 1.64 | power given |
| keys evicted | 243,232 | 237,910 | -2.2% | -18,311 to 7,667 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.144 | -0.6% | -0.0311 to 0.0293 | EVEN, no difference beyond the noise |
| host CPU-seconds | 243 | 241 | -0.6% | -61.3 to 58.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.583 | 0.572 | -1.8% | -0.153 to 0.131 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14.7 |  | 7.49 to 21.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,194 | +1.1% | 6.84 to 18.6 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00454 to 0.00206 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +1.0% | 0.00314 to 0.0131 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.0162 to 0.0194 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.29 | 5.28 | -0.1% | -0.0696 to 0.0571 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.18 | 1.13 | -4.0% | -0.0682 to -0.027 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 0.975 to 2.43 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.798 to 1.65 | power given |
| keys evicted | 138,150 | 133,510 | -3.4% | -7,971 to -1,310 | shown, not judged |
| host CPU busy (share of the run) | 0.0645 | 0.0558 | -13.4% | -0.0419 to 0.0246 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 97.7 | -14.2% | -78.5 to 46.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.182 | -15.1% | -0.149 to 0.0846 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 16 to 26 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
