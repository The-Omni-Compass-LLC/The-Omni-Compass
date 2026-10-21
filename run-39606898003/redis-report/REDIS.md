# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2 to 0.896 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -1.7e-05 to 0.00968 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00109 to 0.000619 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.00908 to 0.00155 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | +0.1% | -0.00769 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.2% | -0.000565 to 0.00876 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.82 to -1.38 | GAIN |
| memory used, mean (MB) | 57.2 | 56.4 | -1.3% | -0.951 to -0.493 | GAIN |
| keys evicted | 71,780 | 71,854 | +0.1% | -97.7 to 245 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.122 | -9.9% | -0.0802 to 0.0536 | EVEN, no difference beyond the noise |
| host CPU-seconds | 90.2 | 80.1 | -11.2% | -61.9 to 41.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.466 | 0.414 | -11.2% | -0.319 to 0.215 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% | 11.7 to 27.1 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00206 to 0.00357 | EVEN, the same |
| cache hit rate | 0.845 | 0.858 | +1.5% | 0.0079 to 0.0182 | GAIN |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.0126 to 0.00225 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.00402 to 0.011 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.983 | -6.7% | -0.102 to -0.0391 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.7 | +1.1% | -0.482 to 1.83 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.6% | -0.413 to 1.13 | EVEN, no difference beyond the noise |
| keys evicted | 103,561 | 95,008 | -8.3% | -11,995 to -5,112 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.115 | -7.7% | -0.0501 to 0.0309 | EVEN, no difference beyond the noise |
| host CPU-seconds | 210 | 192 | -8.3% | -94.7 to 59.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.368 | 0.332 | -9.7% | -0.169 to 0.0975 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 10.7 to 12.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0127 to 0.00485 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00709 to 0.00849 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.7 | +0.0% | -0.00369 to 0.00768 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.77 | +0.2% | 0.00698 to 0.0214 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0436 to -0.0342 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.34 to 1.52 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.85 to 1.47 | power given |
| keys evicted | 243,165 | 236,906 | -2.6% | -14,973 to 2,456 | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.153 | -0.1% | -0.0114 to 0.011 | EVEN, no difference beyond the noise |
| host CPU-seconds | 257 | 257 | -0.0% | -21.7 to 21.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.617 | 0.61 | -1.2% | -0.0587 to 0.0433 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% | 6.15 to 19.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00413 to 0.00314 | EVEN, the same |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00442 to 0.0125 | GAIN |
| latency, 95th percentile (ms) | 5.59 | 5.58 | -0.2% | -0.0347 to 0.0107 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.68 | 5.69 | +0.0% | -0.0249 to 0.0289 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.27 | 1.22 | -3.7% | -0.0672 to -0.0269 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | 1.15 to 2.27 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.8% | 0.286 to 1.94 | power given |
| keys evicted | 138,051 | 133,443 | -3.3% | -8,507 to -709 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.104 | -3.6% | -0.0172 to 0.00932 | EVEN, no difference beyond the noise |
| host CPU-seconds | 188 | 181 | -3.9% | -33.2 to 18.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.353 | 0.335 | -4.9% | -0.0668 to 0.0322 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 21.2 to 24.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
