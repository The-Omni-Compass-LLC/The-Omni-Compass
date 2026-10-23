# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,325 | 1,325 | -0.0% | -2.24 to 2.19 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0144 to 0.00335 | EVEN, no difference beyond the noise |
| cache hit rate | 0.885 | 0.885 | +0.0% | -9.2e-06 to 9.2e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.0144 to 0.016 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.0% | -0.0281 to 0.0305 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.68 | 0.675 | -0.7% | -0.0229 to 0.0138 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | -0.075 to 0.112 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0719 | 0.0677 | -5.9% | -0.0584 to 0.0499 | EVEN, no difference beyond the noise |
| host CPU-seconds | 51.6 | 48.3 | -6.4% | -44.8 to 38.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.216 | 0.203 | -6.4% | -0.188 to 0.16 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,470 | 1,470 | -0.0% | -0.291 to 0.174 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00503 to 0.00196 | EVEN, no difference beyond the noise |
| cache hit rate | 0.981 | 0.981 | +0.0% | -8.77e-06 to 9.76e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.113 | 0.114 | +1.2% | -0.00113 to 0.00379 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.22 | 5.22 | -0.1% | -0.00949 to 0.00177 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.182 | 0.181 | -0.1% | -0.00506 to 0.0047 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | -0.0604 to 0.0886 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0472 | 0.0644 | +36.5% | 0.00584 to 0.0286 | power given |
| host CPU-seconds | 82.7 | 115 | +39.2% | 8.64 to 56.1 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.125 | 0.174 | +39.2% | 0.013 to 0.0848 | power given |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | +0.0% | -0.631 to 0.752 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0933 to 0.0604 | EVEN, no difference beyond the noise |
| cache hit rate | 0.783 | 0.783 | +0.0% | -8.43e-06 to 9.67e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.2 | 5.21 | +0.1% | -0.0117 to 0.0184 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.2% | -0.0426 to 0.059 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.2 | 1.2 | +0.1% | -0.0101 to 0.0132 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | -0.00436 to 0.0788 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0549 | 0.0543 | -1.2% | -0.065 to 0.0637 | EVEN, no difference beyond the noise |
| host CPU-seconds | 96.5 | 95.2 | -1.4% | -119 to 117 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.183 | 0.18 | -1.4% | -0.226 to 0.221 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `5f430c111d90`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% | -0.228 to 0.217 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0117 to 0.0107 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -1.75e-06 to 2.66e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.1% | -0.00752 to 0.0156 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% | -0.0139 to 0.0257 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.569 | 0.569 | -0.0% | -0.0077 to 0.00766 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | 0.0191 to 0.0385 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.106 | 0.0944 | -10.6% | -0.0322 to 0.00993 | EVEN, no difference beyond the noise |
| host CPU-seconds | 179 | 158 | -11.5% | -58.2 to 16.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.285 | 0.252 | -11.5% | -0.0928 to 0.027 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
