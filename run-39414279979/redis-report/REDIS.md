# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.399 to 0.231 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00122 to 0.00454 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | -0.0% | -6.55e-06 to 4.08e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.1% | -0.0173 to 0.00932 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.77 | -0.1% | -0.0236 to 0.0121 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.808 | 0.808 | -0.1% | -0.00385 to 0.00215 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.0219 to 0.0895 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.0917 | -19.2% | -0.0739 to 0.0302 | EVEN, no difference beyond the noise |
| host CPU-seconds | 77.2 | 60.7 | -21.3% | -56.1 to 23.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.323 | 0.254 | -21.3% | -0.235 to 0.0973 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,471 | +0.0% | -0.4 to 0.761 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00311 to 0.0027 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -7.36e-06 to 7.36e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.167 | 0.165 | -1.5% | -0.00578 to 0.000871 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.49 | 5.48 | -0.1% | -0.0175 to 0.00379 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.233 | 0.232 | -0.6% | -0.0049 to 0.0023 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.000431 to 0.0572 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0967 | 0.0821 | -15.2% | -0.0501 to 0.0208 | EVEN, no difference beyond the noise |
| host CPU-seconds | 171 | 143 | -16.5% | -96.3 to 39.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.258 | 0.216 | -16.5% | -0.146 to 0.0603 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.192 to 0.149 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0175 to 0.0212 | EVEN, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | -5.88e-06 to 8.84e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.66 | 5.66 | +0.0% | -0.00695 to 0.00741 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.00743 to 0.00452 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.35 | -0.1% | -0.00236 to 0.000482 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.0125 to 0.0376 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.124 | -7.1% | -0.0205 to 0.00147 | EVEN, no difference beyond the noise |
| host CPU-seconds | 227 | 209 | -8.1% | -40.1 to 3.15 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.43 | 0.395 | -8.1% | -0.0759 to 0.00602 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | +0.0% | -1.07 to 1.09 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0104 to 0.0115 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | -0.0% | -4.74e-06 to 3.76e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.69 | 5.68 | -0.1% | -0.0153 to 0.00836 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.78 | -0.1% | -0.0182 to 0.00654 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.576 | 0.577 | +0.1% | -0.00549 to 0.00661 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0118 to 0.0365 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0971 | 0.102 | +4.6% | -0.0653 to 0.0743 | EVEN, no difference beyond the noise |
| host CPU-seconds | 163 | 170 | +4.8% | -122 to 137 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.26 | 0.272 | +4.8% | -0.194 to 0.219 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
