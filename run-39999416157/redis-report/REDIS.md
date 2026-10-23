# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `9678c8ad4325`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,074 | -0.1% | -2.09 to 0.161 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0295 to 0.0382 | EVEN, no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00181 to 0.00109 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.25 | 5.22 | -0.5% | -0.0856 to 0.038 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.49 | 5.34 | -2.7% | -0.402 to 0.109 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.55 | 1.55 | -0.5% | -0.0188 to 0.00305 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.61 to -1.27 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.692 to -0.365 | GAIN |
| keys evicted | 71,719 | 71,808 | +0.1% | -349 to 527 | shown, not judged |
| host CPU busy (share of the run) | 0.0713 | 0.0494 | -30.7% | -0.0732 to 0.0295 | EVEN, no difference beyond the noise |
| host CPU-seconds | 50.3 | 34.3 | -31.9% | -54.8 to 22.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.26 | 0.177 | -31.9% | -0.283 to 0.117 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `9678c8ad4325`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% | -6.24 to 31.7 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00162 to 0.00381 | EVEN, the same |
| cache hit rate | 0.845 | 0.854 | +1.0% | -0.00415 to 0.0213 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% | -0.0133 to 0.00824 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% | -0.0143 to 0.0225 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1 | -4.2% | -0.112 to 0.0231 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64 | +0.0% | -1.18 to 1.22 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.1 | -0.3% | -1.31 to 0.985 | EVEN, no difference beyond the noise |
| keys evicted | 103,288 | 97,706 | -5.4% | -14,136 to 2,972 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.112 | +2.9% | -0.0321 to 0.0384 | EVEN, no difference beyond the noise |
| host CPU-seconds | 181 | 187 | +3.3% | -59.5 to 71.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.324 | +2.3% | -0.11 to 0.125 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 20.3 |  | 14.6 to 26.1 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 23.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `9678c8ad4325`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 936 | +1.1% | 4.37 to 16.3 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.137 to 0.0918 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00747 to 0.00852 | GAIN |
| latency, 95th percentile (ms) | 5.69 | 5.95 | +4.5% | -0.858 to 1.38 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 6.66 | +16.0% | -3 to 4.83 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.28 | +0.6% | -0.229 to 0.258 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 1.36 to 1.46 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.844 to 1.47 | power given |
| keys evicted | 243,204 | 236,799 | -2.6% | -15,207 to 2,397 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.141 | +0.5% | -0.0798 to 0.0811 | EVEN, no difference beyond the noise |
| host CPU-seconds | 234 | 233 | -0.3% | -148 to 147 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.553 | -1.4% | -0.362 to 0.346 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 14 |  | 9.7 to 18.3 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 15.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `9678c8ad4325`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 11.3 to 17.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.015 to 0.01 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.799 | +1.2% | 0.00836 to 0.0102 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -0.0181 to 0.0206 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.3 | +0.4% | -0.13 to 0.171 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -4.3% | -0.0772 to -0.0231 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.9 | +2.9% | 1.58 to 2.14 | power given |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | 1.1 to 1.56 | power given |
| keys evicted | 138,185 | 132,746 | -3.9% | -6,056 to -4,822 | shown, not judged |
| host CPU busy (share of the run) | 0.058 | 0.0692 | +19.4% | -0.0654 to 0.0879 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 123 | +20.6% | -123 to 165 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.192 | 0.229 | +19.1% | -0.232 to 0.306 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 23 to 23 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 24.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
