# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% | -0.237 to 0.442 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00304 to 0.000507 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% | -1.31e-05 to 8.16e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.2% | -0.0255 to 0.0458 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.83 | +0.2% | -0.0173 to 0.0405 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.819 | 0.823 | +0.5% | -0.00117 to 0.00935 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0294 to 0.0522 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.128 | +22.2% | -0.0112 to 0.0576 | EVEN, no difference beyond the noise |
| host CPU-seconds | 69.9 | 87.2 | +24.8% | -7.82 to 42.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.293 | 0.365 | +24.8% | -0.0328 to 0.178 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% | -0.15 to 0.344 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00437 to 0.00442 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -3.68e-06 to 3.68e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.165 | 0.167 | +1.4% | -0.00949 to 0.014 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.48 | 5.48 | +0.0% | -0.0244 to 0.0255 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.229 | 0.229 | +0.2% | -0.00402 to 0.00513 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00458 to 0.0398 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0816 | 0.0865 | +6.0% | -0.0496 to 0.0593 | EVEN, no difference beyond the noise |
| host CPU-seconds | 142 | 151 | +6.4% | -94.5 to 113 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.228 | +6.4% | -0.143 to 0.17 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | +0.0% | -0.914 to 1.37 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00456 to 0.00537 | EVEN, the same |
| cache hit rate | 0.783 | 0.783 | -0.0% | -3.68e-06 to 3.68e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.21 | 5.2 | -0.1% | -0.00628 to 0.000869 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.25 | -0.1% | -0.0326 to 0.0236 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | -0.2% | -0.0159 to 0.012 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.03 to 0.0792 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0677 | 0.0586 | -13.5% | -0.0373 to 0.0191 | EVEN, no difference beyond the noise |
| host CPU-seconds | 120 | 103 | -14.3% | -70.3 to 36 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.227 | 0.195 | -14.3% | -0.133 to 0.0684 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% | -0.0522 to 0.058 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00331 to 0.00637 | EVEN, no difference beyond the noise |
| cache hit rate | 0.929 | 0.929 | -0.0% | -3.11e-06 to 1.14e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.67 | -0.2% | -0.0239 to 0.00145 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.76 | -0.3% | -0.0383 to 0.0045 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.568 | 0.564 | -0.7% | -0.0104 to 0.00283 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.0163 to 0.0599 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0883 | 0.0904 | +2.4% | -0.04 to 0.0442 | EVEN, no difference beyond the noise |
| host CPU-seconds | 147 | 151 | +2.9% | -72.1 to 80.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.234 | 0.241 | +2.9% | -0.115 to 0.129 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
