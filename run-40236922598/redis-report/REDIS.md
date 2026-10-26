# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -1.9 to 1.1 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0684 to 0.04 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000919 to 0.000472 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% | -0.017 to 0.0134 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% | -0.0206 to 0.0311 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.75 | +0.2% | -0.0196 to 0.0267 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.3 | -2.6% | -2.16 to -1.14 | GAIN |
| memory used, mean (MB) | 57.1 | 56.5 | -1.1% | -1.15 to -0.141 | GAIN |
| keys evicted | 71,770 | 72,401 | +0.9% | 419 to 843 | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.137 | +14.8% | -0.0271 to 0.0626 | EVEN, no difference beyond the noise |
| host CPU-seconds | 79.1 | 92.5 | +16.9% | -19.5 to 46.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.478 | +16.9% | -0.1 to 0.238 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 120 | 121 | +0.7% | -2.87 to 4.5 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 14.7 | 14.7 | +0.0% | -0.586 to 0.599 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105 | 106 | +0.4% | -2.7 to 3.57 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.379 |  | 0.319 to 0.44 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0934 | 0.0916 | -1.9% | -0.0103 to 0.00671 | shown, not judged |
| host CPU-seconds without steal | 79.1 | 92.5 | +16.9% | -19.5 to 46.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% | 10.9 to 21.7 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00633 to 0.000996 | EVEN, no difference beyond the noise |
| cache hit rate | 0.845 | 0.856 | +1.3% | 0.00752 to 0.014 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.2% | -0.0212 to -0.00243 | GAIN |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% | -0.00954 to 0.0097 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.959 | 0.901 | -6.0% | -0.0812 to -0.034 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.2 | -1.3% | -0.972 to -0.688 | GAIN |
| memory used, mean (MB) | 61.3 | 60.1 | -2.0% | -1.88 to -0.604 | GAIN |
| keys evicted | 103,401 | 96,558 | -6.6% | -9,021 to -4,665 | shown, not judged |
| host CPU busy (share of the run) | 0.099 | 0.0874 | -11.7% | -0.0555 to 0.0323 | EVEN, no difference beyond the noise |
| host CPU-seconds | 174 | 151 | -12.9% | -108 to 63.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.305 | 0.262 | -14.0% | -0.194 to 0.109 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29 |  | 26.5 to 31.5 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 193 | 191 | -1.1% | -6.25 to 1.87 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 26.2 | 26.1 | -0.4% | -0.821 to 0.635 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 167 | 164 | -1.7% | -6.72 to 1.13 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.697 |  | 0.572 to 0.821 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.161 | -1.5% | -0.00619 to 0.00135 | shown, not judged |
| host CPU-seconds without steal | 174 | 151 | -12.9% | -108 to 63.5 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 10.8 to 12.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0483 to 0.0521 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00694 to 0.00857 | GAIN |
| latency, 95th percentile (ms) | 5.64 | 5.64 | +0.1% | -0.00716 to 0.0132 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.69 | 5.71 | +0.4% | -0.0398 to 0.0835 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.24 | 2.2 | -1.7% | -0.0495 to -0.0254 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.37 to 1.42 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% | 1.2 to 1.28 | power given |
| keys evicted | 243,176 | 234,804 | -3.4% | -8,919 to -7,825 | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.15 | -1.1% | -0.0255 to 0.0223 | EVEN, no difference beyond the noise |
| host CPU-seconds | 262 | 259 | -1.2% | -51.7 to 45.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.63 | 0.615 | -2.4% | -0.13 to 0.0992 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13 |  | 8.03 to 18 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284 | 285 | +0.4% | -5.61 to 7.83 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 32.4 | 32.3 | -0.3% | -1.21 to 1.01 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 252 | 252 | +0.1% | -5.54 to 6.11 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.926 |  | 0.838 to 1.01 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.22 | 0.219 | -0.3% | -0.00783 to 0.00656 | shown, not judged |
| host CPU-seconds without steal | 262 | 259 | -1.2% | -51.7 to 45.3 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v21 (digest b658f05d43c1e602, 63 files) at `23c7e8eb27be`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,191 | +0.6% | -1.62 to 16 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0034 to 0.00417 | EVEN, the same |
| cache hit rate | 0.79 | 0.794 | +0.6% | -0.000974 to 0.0106 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.0121 to 0.0181 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | -0.0106 to 0.0283 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.6% | -0.0624 to 0.0199 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -0.382 to 2.33 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.9 | +1.1% | -0.308 to 1.67 | EVEN, no difference beyond the noise |
| keys evicted | 138,050 | 135,880 | -1.6% | -6,734 to 2,395 | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.134 | +27.5% | -0.0405 to 0.0984 | EVEN, no difference beyond the noise |
| host CPU-seconds | 173 | 228 | +31.7% | -76.5 to 186 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.325 | 0.425 | +30.9% | -0.148 to 0.349 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 18.7 |  | 6.41 to 30.9 | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 283 | 286 | +1.1% | -3.9 to 10 | EVEN, no difference beyond the noise |
| the server's own CPU-seconds (redis-server) | 34.6 | 35.1 | +1.3% | -0.681 to 1.59 | shown, not judged |
| the application's own CPU-seconds (its request threads) | 248 | 250 | +0.7% | -4.23 to 7.58 | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.929 |  | 0.881 to 0.977 | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.229 | -0.6% | -0.00635 to 0.00346 | shown, not judged |
| host CPU-seconds without steal | 173 | 228 | +31.7% | -76.5 to 186 | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 20.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
