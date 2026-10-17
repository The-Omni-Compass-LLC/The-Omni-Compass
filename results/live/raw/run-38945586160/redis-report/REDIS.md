# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.56 to 2.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00556 to 0.00736 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00169 to 0.00161 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.0% | -0.0071 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | 0.00425 to 0.0159 | LOSS |
| latency, mean (ms) | 1.74 | 1.74 | +0.2% | -0.0118 to 0.0199 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.86 to -1.31 | GAIN |
| memory used, mean (MB) | 57.2 | 56.5 | -1.2% | -0.965 to -0.381 | GAIN |
| keys evicted | 71,762 | 71,788 | +0.0% | -401 to 453 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.137 | +22.3% | -0.00284 to 0.0527 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.4 | 92 | +25.3% | -0.0651 to 37.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.379 | 0.475 | +25.3% | -0.000911 to 0.193 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% | 7.67 to 27.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0332 to 0.0201 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.856 | +1.4% | 0.00504 to 0.0186 | GAIN |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% | -0.0139 to 0.00654 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.27 | -0.1% | -0.0385 to 0.024 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.897 | 0.836 | -6.8% | -0.0894 to -0.0327 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -0.754 to 1.99 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.5 | +0.3% | -1.13 to 1.52 | EVEN, no difference beyond the noise |
| keys evicted | 103,647 | 95,891 | -7.5% | -12,313 to -3,199 | shown, not judged |
| host CPU busy (share of the run) | 0.062 | 0.0569 | -8.1% | -0.0379 to 0.0279 | EVEN, no difference beyond the noise |
| host CPU-seconds | 109 | 99.9 | -8.2% | -69.6 to 51.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.191 | 0.173 | -9.5% | -0.123 to 0.0862 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.4% | 11.1 to 14.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.029 to 0.00761 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.626 | +1.4% | 0.00753 to 0.00965 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.71 | +0.1% | -0.00732 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.77 | +0.3% | 0.0139 to 0.0164 | LOSS |
| latency, mean (ms) | 2.27 | 2.23 | -1.9% | -0.0498 to -0.0362 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.4% | 1.23 to 1.88 | power given |
| memory used, mean (MB) | 60.7 | 61.8 | +1.8% | 0.833 to 1.33 | power given |
| keys evicted | 243,182 | 239,557 | -1.5% | -8,593 to 1,342 | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.143 | +0.5% | -0.0142 to 0.0155 | EVEN, no difference beyond the noise |
| host CPU-seconds | 237 | 238 | +0.7% | -27.9 to 31 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.568 | 0.564 | -0.7% | -0.0733 to 0.0652 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15.7 |  | 14.2 to 17.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,194 | +0.9% | 5.53 to 16.9 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00924 to 0.00789 | EVEN, the same |
| cache hit rate | 0.789 | 0.797 | +0.9% | 0.00317 to 0.0115 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.015 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.84 | 5.9 | +1.0% | -0.0947 to 0.216 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.32 | -2.9% | -0.0655 to -0.014 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | 0.0567 to 2.65 | power given |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% | 0.0173 to 1.95 | power given |
| keys evicted | 138,228 | 133,811 | -3.2% | -7,823 to -1,011 | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.133 | +5.4% | -0.0185 to 0.0323 | EVEN, no difference beyond the noise |
| host CPU-seconds | 211 | 225 | +6.5% | -34.8 to 62.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.397 | 0.419 | +5.5% | -0.0696 to 0.113 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 10.4 to 27.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 21.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
