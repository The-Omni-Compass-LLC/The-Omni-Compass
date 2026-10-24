# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -4.2 to 3.3 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00983 to 0.00975 | EVEN, the same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00259 to 0.0021 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.55 | 5.55 | -0.0% | -0.00389 to 0.0027 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% | -0.00373 to 0.0062 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.62 | +0.0% | -0.0153 to 0.0162 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.6% | -1.98 to -1.31 | GAIN |
| memory used, mean (MB) | 57.1 | 56.5 | -1.2% | -1.08 to -0.315 | GAIN |
| keys evicted | 71,742 | 71,804 | +0.1% | -627 to 751 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.0941 | -10.2% | -0.117 to 0.0959 | EVEN, no difference beyond the noise |
| host CPU-seconds | 73.6 | 65.3 | -11.3% | -90.3 to 73.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.38 | 0.337 | -11.3% | -0.465 to 0.379 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 1.65 to 30.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0104 to 0.0125 | EVEN, the same |
| cache hit rate | 0.845 | 0.855 | +1.2% | 0.000947 to 0.0201 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0174 to 0.00999 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.0% | -0.0301 to 0.0255 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.998 | -5.5% | -0.106 to -0.00989 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -0.0101 to 0.709 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.4 | +0.1% | -0.695 to 0.798 | EVEN, no difference beyond the noise |
| keys evicted | 103,447 | 96,580 | -6.6% | -13,289 to -445 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.123 | +8.8% | -0.0175 to 0.0374 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 207 | +10.3% | -32.8 to 71.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.33 | 0.359 | +8.9% | -0.063 to 0.122 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 15.9 to 27.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.2% | 10.7 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0108 to 0.00171 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00715 to 0.00828 | GAIN |
| latency, 95th percentile (ms) | 5.48 | 5.48 | -0.1% | -0.0393 to 0.0336 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.56 | 5.56 | -0.0% | -0.0195 to 0.0194 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.12 | 2.08 | -1.9% | -0.057 to -0.0253 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.09 to 1.9 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | 1.22 to 1.39 | power given |
| keys evicted | 243,080 | 234,720 | -3.4% | -8,750 to -7,970 | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.105 | +4.4% | -0.0525 to 0.0614 | EVEN, no difference beyond the noise |
| host CPU-seconds | 176 | 184 | +4.8% | -100 to 117 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.422 | 0.437 | +3.5% | -0.245 to 0.274 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 15 |  | 15 to 15 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% | 1.46 to 17.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00155 to 0.00299 | EVEN, the same |
| cache hit rate | 0.789 | 0.796 | +0.8% | 0.00117 to 0.0116 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.0% | -0.00884 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% | -0.0011 to 0.0204 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.3% | -0.064 to 0.00118 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | -0.479 to 2.58 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62 | +1.3% | -0.0483 to 1.69 | EVEN, no difference beyond the noise |
| keys evicted | 138,215 | 134,753 | -2.5% | -6,960 to 34.7 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.125 | +0.5% | -0.0295 to 0.0307 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 209 | +0.6% | -55.9 to 58.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.389 | -0.2% | -0.109 to 0.108 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.7 |  | 6.19 to 29.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 19.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
