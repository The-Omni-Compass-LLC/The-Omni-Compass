# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,326 | +23.2% | 245 to 255 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.125 to 0.0708 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.885 | +23.3% | 0.164 to 0.17 | GAIN |
| latency, 95th percentile (ms) | 5.75 | 5.73 | -0.5% | -0.0397 to -0.0152 | GAIN |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.1% | -0.0237 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.74 | 0.82 | -53.0% | -0.939 to -0.908 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 245 | +282.2% | 163 to 198 | power given |
| memory used, mean (MB) | 57.1 | 200 | +250.7% | 142 to 145 | power given |
| keys evicted | 71,724 | 79.7 | -99.9% | -72,432 to -70,857 | shown, not judged |
| host CPU busy (share of the run) | 0.158 | 0.125 | -20.6% | -0.0423 to -0.0229 | GAIN |
| host CPU-seconds | 108 | 84.9 | -21.1% | -30.3 to -15 | GAIN |
| host CPU-seconds per 1,000 requests inside the line | 0.555 | 0.356 | -35.9% | -0.238 to -0.161 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 10.3 |  | -4.22 to 24.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 123 | 107 | -13.5% | -17.9 to -15.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 15.2 | 13.3 | -12.7% | -2.76 to -1.09 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 108 | 92.8 | -14.3% | -16.3 to -14.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.679 |  | 0.595 to 0.764 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0953 | 0.09 | -5.6% | -0.00897 to -0.00173 | shown, not judged |
| host CPU-seconds without steal | 108 | 84.9 | -21.1% | -30.3 to -14.9 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 7.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,466 | +15.7% | 197 to 200 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00367 to 0.00237 | EVEN, the same |
| cache hit rate | 0.845 | 0.977 | +15.7% | 0.131 to 0.134 | GAIN |
| latency, 95th percentile (ms) | 5.62 | 0.214 | -96.2% | -5.42 to -5.4 | GAIN |
| latency, 99th percentile (ms) | 5.72 | 5.58 | -2.5% | -0.157 to -0.125 | GAIN |
| latency, mean (ms) | 0.988 | 0.261 | -73.6% | -0.736 to -0.719 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 336 | +425.8% | 270 to 275 | power given |
| memory used, mean (MB) | 61.3 | 312 | +409.4% | 248 to 254 | power given |
| keys evicted | 103,318 | 2,753 | -97.3% | -101,372 to -99,758 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.112 | -8.0% | -0.0346 to 0.0152 | EVEN, no difference beyond the noise |
| host CPU-seconds | 217 | 202 | -7.1% | -65.1 to 34.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.381 | 0.306 | -19.7% | -0.149 to -0.000481 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 27.9 to 30.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 216 | 189 | -12.5% | -30.9 to -23.4 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.5 | 21.2 | -13.4% | -3.7 to -2.9 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 192 | 167 | -13.0% | -28.4 to -21.6 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.15 |  | 1.08 to 1.23 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.18 | 0.177 | -1.5% | -0.0101 to 0.00483 | shown, not judged |
| host CPU-seconds without steal | 217 | 202 | -7.1% | -65.1 to 34.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 1,173 | +26.7% | 246 to 249 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00246 to 0.0162 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.782 | +26.7% | 0.164 to 0.166 | GAIN |
| latency, 95th percentile (ms) | 5.7 | 5.67 | -0.5% | -0.0345 to -0.02 | GAIN |
| latency, 99th percentile (ms) | 5.76 | 5.75 | -0.1% | -0.0115 to 0.000801 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 1.36 | -39.7% | -0.911 to -0.889 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 313 | +388.8% | 243 to 254 | power given |
| memory used, mean (MB) | 60.7 | 258 | +324.5% | 196 to 198 | power given |
| keys evicted | 243,105 | 0 | -100.0% | -243,582 to -242,629 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.135 | -11.1% | -0.0584 to 0.0245 | EVEN, no difference beyond the noise |
| host CPU-seconds | 256 | 230 | -10.3% | -107 to 54 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.615 | 0.436 | -29.2% | -0.337 to -0.0219 | GAIN |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 17.2 to 20.1 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 315 | 280 | -11.0% | -37.6 to -31.9 | GAIN |
| the server's own CPU-seconds (redis-server) | 35.6 | 32.2 | -9.6% | -4.41 to -2.41 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 279 | 246 | -11.8% | -35.2 to -30.5 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.56 |  | 1.36 to 1.75 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.239 | 0.229 | -3.9% | -0.0197 to 0.000895 | shown, not judged |
| host CPU-seconds without steal | 256 | 230 | -10.3% | -107 to 54 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 9.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,387 | +17.1% | 198 to 207 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0374 to 0.0241 | EVEN, no difference beyond the noise |
| cache hit rate | 0.79 | 0.925 | +17.1% | 0.132 to 0.138 | GAIN |
| latency, 95th percentile (ms) | 5.53 | 5.43 | -1.9% | -0.12 to -0.0851 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.58 | -0.4% | -0.0339 to -0.0158 | GAIN |
| latency, mean (ms) | 1.24 | 0.521 | -58.0% | -0.739 to -0.702 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 347 | +442.0% | 271 to 295 | power given |
| memory used, mean (MB) | 61.2 | 319 | +420.7% | 250 to 265 | power given |
| keys evicted | 137,936 | 2,677 | -98.1% | -137,447 to -133,071 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.0959 | -10.9% | -0.0498 to 0.0262 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 170 | -10.5% | -93.3 to 53.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.272 | -23.6% | -0.198 to 0.0307 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 17.3 |  | 15.9 to 18.8 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 193 | 173 | -10.6% | -23.1 to -17.8 | GAIN |
| the server's own CPU-seconds (redis-server) | 24.3 | 21.5 | -11.5% | -3.03 to -2.56 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 169 | 150 | -11.1% | -21.4 to -16.2 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 1.17 |  | 0.992 to 1.34 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.165 | 0.16 | -3.1% | -0.00576 to -0.00458 | shown, not judged |
| host CPU-seconds without steal | 190 | 170 | -10.5% | -93.3 to 53.4 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 14.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
