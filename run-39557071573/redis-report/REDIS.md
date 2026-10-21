# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.43 to 0.885 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0216 to 0.0335 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000713 to 0.000535 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.76 | +0.1% | -0.0153 to 0.025 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.3% | -0.00389 to 0.0395 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.5% | -0.0108 to 0.028 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.8 | -3.4% | -3.86 to -0.554 | GAIN |
| memory used, mean (MB) | 57.2 | 55.8 | -2.3% | -3.12 to 0.473 | EVEN, no difference beyond the noise |
| keys evicted | 71,762 | 71,806 | +0.1% | -94.3 to 182 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.137 | -8.1% | -0.069 to 0.045 | EVEN, no difference beyond the noise |
| host CPU-seconds | 101 | 91.5 | -9.1% | -51.4 to 33.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.519 | 0.472 | -9.0% | -0.266 to 0.172 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8 |  | 3.03 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,282 | +1.2% | -0.0633 to 30.7 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00176 to 0.00529 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.855 | +1.2% | 2.73e-05 to 0.0204 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0285 to 0.00423 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | -0.1% | -0.0235 to 0.0109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.998 | -5.4% | -0.108 to -0.00591 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.4 | +0.6% | -2.68 to 3.43 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.4 | +0.2% | -3.44 to 3.66 | EVEN, no difference beyond the noise |
| keys evicted | 103,413 | 96,819 | -6.4% | -13,724 to 536 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.132 | +0.5% | -0.0461 to 0.0475 | EVEN, no difference beyond the noise |
| host CPU-seconds | 220 | 223 | +1.1% | -86.6 to 91.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.387 | 0.386 | -0.1% | -0.152 to 0.151 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21 |  | 7.85 to 34.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.2% | 8.74 to 14.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.036 to 0.0175 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00649 to 0.00933 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.0161 to 0.0178 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.0422 to 0.082 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.23 | -1.6% | -0.0643 to -0.0102 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.3% | 1.25 to 1.65 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.886 to 1.46 | power given |
| keys evicted | 243,163 | 236,821 | -2.6% | -14,707 to 2,022 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.141 | -6.9% | -0.0236 to 0.00289 | EVEN, no difference beyond the noise |
| host CPU-seconds | 256 | 236 | -8.0% | -46.1 to 5.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.615 | 0.559 | -9.1% | -0.119 to 0.00711 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.3 |  | 7.08 to 19.6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,196 | +1.1% | 8.17 to 18.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00574 to 0.00169 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.798 | +1.1% | 0.00534 to 0.0122 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0147 to 0.0045 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.24 | -0.2% | -0.0413 to 0.0187 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.11 | -4.2% | -0.0749 to -0.0221 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 1.17 to 2.15 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.873 to 1.61 | power given |
| keys evicted | 138,061 | 132,973 | -3.7% | -7,414 to -2,762 | shown, not judged |
| host CPU busy (share of the run) | 0.0566 | 0.0432 | -23.7% | -0.0664 to 0.0396 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.6 | 75 | -24.7% | -123 to 73.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.187 | 0.139 | -25.6% | -0.232 to 0.136 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
