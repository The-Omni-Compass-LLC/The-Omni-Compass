# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.906 to 0.00283 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00269 to 0.00796 | GAIN |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000551 to 0.000104 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.76 | +0.1% | -0.00205 to 0.0113 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.3% | 0.002 to 0.0335 | LOSS |
| latency, mean (ms) | 1.74 | 1.75 | +0.5% | -2.82e-05 to 0.0174 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.1% | -3.86 to -0.0825 | GAIN |
| memory used, mean (MB) | 57.2 | 56.1 | -1.8% | -3.02 to 0.943 | EVEN, no difference beyond the noise |
| keys evicted | 71,722 | 71,802 | +0.1% | -1.76 to 162 | shown, not judged |
| host CPU busy (share of the run) | 0.154 | 0.147 | -4.8% | -0.117 to 0.103 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 99.2 | -5.7% | -93 to 81.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.543 | 0.512 | -5.6% | -0.48 to 0.419 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 7.33 |  | 1.6 to 13.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,289 | +1.7% | 17.8 to 24.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00212 to 0.00331 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0119 to 0.0163 | GAIN |
| latency, 95th percentile (ms) | 5.58 | 5.55 | -0.6% | -0.0871 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.7 | 5.69 | -0.2% | -0.0421 to 0.0217 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.966 | 0.886 | -8.2% | -0.107 to -0.0515 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | 0.733 to 1.89 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.2% | -0.934 to 2.43 | EVEN, no difference beyond the noise |
| keys evicted | 103,396 | 94,170 | -8.9% | -11,010 to -7,442 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.105 | +2.5% | -0.0847 to 0.0899 | EVEN, no difference beyond the noise |
| host CPU-seconds | 182 | 188 | +3.6% | -163 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.319 | 0.325 | +1.9% | -0.288 to 0.3 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22 |  | 9.09 to 34.9 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 936 | +1.3% | 10 to 13.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0389 to 0.00738 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00736 to 0.0081 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.0277 to 0.028 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.36 | 5.34 | -0.4% | -0.232 to 0.188 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.01 | -2.1% | -0.0566 to -0.0284 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.3% | 1.38 to 1.59 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.21 to 1.31 | power given |
| keys evicted | 243,076 | 234,709 | -3.4% | -8,615 to -8,119 | shown, not judged |
| host CPU busy (share of the run) | 0.0599 | 0.0612 | +2.1% | -0.0461 to 0.0487 | EVEN, no difference beyond the noise |
| host CPU-seconds | 105 | 108 | +2.4% | -84.1 to 89.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.255 | +1.1% | -0.203 to 0.209 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 13 to 13 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e997ca0d9f65`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,192 | +0.7% | -1.29 to 18.5 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00142 to 0.0018 | EVEN, the same |
| cache hit rate | 0.789 | 0.795 | +0.7% | -0.000706 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% | -0.00649 to 0.00644 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.00731 to 0.0158 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.32 | 1.29 | -2.3% | -0.0767 to 0.0154 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.1% | -1.9 to 4.62 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.1 | +1.6% | -1.42 to 3.33 | EVEN, no difference beyond the noise |
| keys evicted | 138,243 | 134,878 | -2.4% | -10,330 to 3,600 | shown, not judged |
| host CPU busy (share of the run) | 0.135 | 0.146 | +8.7% | -0.0264 to 0.0499 | EVEN, no difference beyond the noise |
| host CPU-seconds | 234 | 257 | +10.0% | -52.7 to 99.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.439 | 0.48 | +9.2% | -0.105 to 0.186 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 6.29 to 26.4 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 18.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
