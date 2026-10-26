# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -0.805 to 0.345 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0264 to -0.000113 | LOSS |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.000413 to 5.46e-05 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.56 | 5.56 | +0.0% | -0.00912 to 0.0103 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.1% | -0.014 to 0.022 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.62 | 1.63 | +0.2% | -0.0111 to 0.0171 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.5 | -2.4% | -1.99 to -1.11 | GAIN |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% | -0.988 to -0.107 | GAIN |
| keys evicted | 71,696 | 72,349 | +0.9% | 640 to 665 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.0959 | -10.7% | -0.0733 to 0.0503 | EVEN, no difference beyond the noise |
| host CPU-seconds | 75.3 | 66.3 | -12.0% | -57.1 to 39.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.342 | -12.0% | -0.295 to 0.202 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 81.7 | 82 | +0.4% | -2 to 2.58 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 10.3 | 10.4 | +0.6% | -0.406 to 0.54 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 71.4 | 71.3 | -0.1% | -2.15 to 1.99 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.301 |  | 0.274 to 0.328 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0658 | 0.0656 | -0.3% | -0.000658 to 0.000296 | shown, not judged |
| host CPU-seconds without steal | 75.3 | 66.3 | -12.0% | -57.1 to 39.1 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,289 | +1.7% | 20.2 to 23.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00122 to 0.0014 | EVEN, the same |
| cache hit rate | 0.844 | 0.859 | +1.7% | 0.0135 to 0.0159 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.63 | -0.1% | -0.0179 to 0.00391 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00371 to 0.0105 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.989 | 0.912 | -7.8% | -0.0837 to -0.0709 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | -0.629 to 2.44 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.9 | +1.0% | -0.483 to 1.73 | EVEN, no difference beyond the noise |
| keys evicted | 103,689 | 94,017 | -9.3% | -10,468 to -8,877 | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.116 | +16.6% | -0.00562 to 0.0387 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 207 | +18.9% | -10.5 to 76.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.357 | +16.8% | -0.023 to 0.126 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 207 | 207 | -0.1% | -5.04 to 4.49 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 25.6 | 25.5 | -0.2% | -0.302 to 0.188 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 182 | 181 | -0.5% | -5.49 to 3.54 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.757 |  | 0.738 to 0.776 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.205 | 0.204 | -0.6% | -0.0117 to 0.00909 | shown, not judged |
| host CPU-seconds without steal | 174 | 207 | +18.9% | -10.5 to 76.2 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 938 | +1.3% | 9.93 to 13.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00917 to 0.0153 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00662 to 0.00907 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% | -0.00206 to 0.00674 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% | 0.00578 to 0.0157 | LOSS |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% | -0.0457 to -0.0328 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.36 to 1.45 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.799 to 1.51 | power given |
| keys evicted | 243,110 | 236,807 | -2.6% | -14,737 to 2,131 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.153 | +9.7% | -0.00422 to 0.0313 | EVEN, no difference beyond the noise |
| host CPU-seconds | 233 | 260 | +11.4% | -8.46 to 61.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.559 | 0.615 | +10.1% | -0.0283 to 0.141 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 310 | 311 | +0.3% | -1.05 to 3.02 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.6 | 35.5 | -0.3% | -1.17 to 0.991 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 274 | 274 | +0.1% | -3.04 to 3.34 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.924 |  | 0.818 to 1.03 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.233 | 0.231 | -1.0% | -0.0106 to 0.00601 | shown, not judged |
| host CPU-seconds without steal | 233 | 260 | +11.4% | -8.46 to 61.7 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `796063486f34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,192 | +0.7% | 0.95 to 15.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0113 to 0.00291 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.795 | +0.7% | 0.00102 to 0.00971 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% | -0.0194 to 0.00987 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.0% | -0.0259 to 0.0302 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.32 | -2.2% | -0.0692 to 0.00985 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | 0.532 to 1.32 | power given |
| memory used, mean (MB) | 61.2 | 61.9 | +1.2% | 0.463 to 0.992 | power given |
| keys evicted | 138,192 | 135,396 | -2.0% | -5,723 to 131 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.116 | -7.1% | -0.0427 to 0.0248 | EVEN, no difference beyond the noise |
| host CPU-seconds | 209 | 192 | -7.9% | -79.6 to 46.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.392 | 0.359 | -8.6% | -0.154 to 0.0867 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 16.3 |  | 8.74 to 23.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 291 | 288 | -0.9% | -8.32 to 3.16 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 35.6 | 35.8 | +0.5% | -0.0359 to 0.363 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 255 | 251 | -1.4% | -9.23 to 1.88 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.935 |  | 0.877 to 0.994 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.235 | 0.231 | -1.7% | -0.0176 to 0.00966 | shown, not judged |
| host CPU-seconds without steal | 209 | 192 | -7.9% | -79.6 to 46.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 17.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
