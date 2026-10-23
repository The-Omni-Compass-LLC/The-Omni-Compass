# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -2.71 to 1.81 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0238 to 0.0173 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00167 to 0.00118 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.76 | +0.1% | -0.014 to 0.0264 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.83 | +0.4% | -0.0334 to 0.075 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.76 | +0.5% | -0.0129 to 0.0311 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.1% | -3.78 to -0.19 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.8% | -2.81 to 0.699 | EVEN, no difference beyond the noise |
| keys evicted | 71,774 | 71,854 | +0.1% | -335 to 495 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.143 | +19.3% | -0.0218 to 0.068 | EVEN, no difference beyond the noise |
| host CPU-seconds | 78.6 | 96 | +22.2% | -16.6 to 51.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.406 | 0.496 | +22.3% | -0.0848 to 0.266 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,289 | +1.8% | 21.3 to 23.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00154 to 0.0022 | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.8% | 0.0142 to 0.0156 | GAIN |
| latency, 95th percentile (ms) | 5.59 | 5.58 | -0.2% | -0.0536 to 0.0281 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | -0.0% | -0.0384 to 0.0349 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.984 | 0.903 | -8.2% | -0.0995 to -0.0626 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.05 to 1.93 | power given |
| memory used, mean (MB) | 61.3 | 62.4 | +1.9% | 1.07 to 1.23 | power given |
| keys evicted | 103,542 | 93,733 | -9.5% | -10,267 to -9,351 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.113 | +10.4% | -0.00803 to 0.0293 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 202 | +11.9% | -13.7 to 56.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.349 | +10.0% | -0.0306 to 0.0938 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20 |  | 17.5 to 22.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 9.8 to 12.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0199 to -0.00974 | LOSS |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00658 to 0.00867 | GAIN |
| latency, 95th percentile (ms) | 5.65 | 5.65 | -0.0% | -0.00551 to 0.00422 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.7 | +0.1% | -0.00151 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.24 | 2.2 | -1.8% | -0.0451 to -0.0364 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.1% | 1.04 to 1.59 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.812 to 1.49 | power given |
| keys evicted | 243,132 | 236,975 | -2.5% | -14,626 to 2,313 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.141 | -7.7% | -0.0276 to 0.00401 | EVEN, no difference beyond the noise |
| host CPU-seconds | 265 | 242 | -8.8% | -54.3 to 7.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.637 | 0.574 | -9.9% | -0.138 to 0.0123 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 11.5 to 16.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `681ff70efadd`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 1.26 to 17.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00794 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.000872 to 0.0114 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.7 | +0.1% | -0.0315 to 0.0428 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.2% | -0.0369 to 0.0633 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.3 | -2.3% | -0.0685 to 0.00796 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.1 | +1.7% | 0.256 to 1.88 | power given |
| memory used, mean (MB) | 61.2 | 62 | +1.2% | 0.273 to 1.25 | power given |
| keys evicted | 138,130 | 135,085 | -2.2% | -6,246 to 157 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.113 | -2.0% | -0.0108 to 0.00622 | EVEN, no difference beyond the noise |
| host CPU-seconds | 195 | 190 | -2.4% | -22.6 to 13.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.365 | 0.354 | -3.1% | -0.0433 to 0.0205 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 5.85 to 32.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
