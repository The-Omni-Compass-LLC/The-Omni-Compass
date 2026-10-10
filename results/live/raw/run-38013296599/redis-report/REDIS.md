# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% | -2.71 to 1.01 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0251 to 0.0249 | same |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00167 to 0.000621 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.0% | -0.0229 to 0.026 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.1% | -0.0201 to 0.0366 | no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.4% | -0.00313 to 0.0172 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.7 | -3.7% | -5.47 to 0.791 | no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.6 | -2.7% | -3.66 to 0.544 | no difference beyond the noise |
| keys evicted | 71,725 | 71,882 | +0.2% | -146 to 460 | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.138 | +5.5% | -0.00731 to 0.0217 | no difference beyond the noise |
| host CPU-seconds | 87.3 | 92.8 | +6.4% | -5.12 to 16.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.45 | 0.479 | +6.4% | -0.0257 to 0.0837 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,308 | +3.2% | 13.6 to 67.4 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00171 to 0.000439 | same |
| cache hit rate | 0.845 | 0.872 | +3.2% | 0.00898 to 0.0447 | better |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% | -0.00737 to -0.000917 | better |
| latency, 99th percentile (ms) | 5.24 | 5.23 | -0.1% | -0.0199 to 0.0095 | no difference beyond the noise |
| latency, mean (ms) | 0.869 | 0.731 | -15.9% | -0.233 to -0.0431 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.3 | +3.6% | -1.59 to 6.19 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 63.2 | +3.1% | -1.4 to 5.24 | no difference beyond the noise |
| keys evicted | 103,266 | 85,544 | -17.2% | -29,842 to -5,602 | shown, not judged |
| host CPU busy (share of the run) | 0.0452 | 0.0601 | +33.0% | -0.0183 to 0.0482 | no difference beyond the noise |
| host CPU-seconds | 79 | 107 | +35.4% | -34.2 to 90.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.139 | 0.182 | +31.0% | -0.0601 to 0.146 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 29.3 |  | 25.5 to 33.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 922 | -0.4% | -5.45 to -2.31 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.039 to 0.0173 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.615 | -0.4% | -0.00347 to -0.00156 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.00526 to 0.00276 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.75 | 5.76 | +0.1% | 0.00159 to 0.0122 | **WORSE** |
| latency, mean (ms) | 2.26 | 2.28 | +0.7% | 0.00903 to 0.0211 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.1% | -0.492 to 0.327 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.4 | -0.4% | -0.78 to 0.26 | no difference beyond the noise |
| keys evicted | 243,201 | 246,020 | +1.2% | -1,822 to 7,458 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.131 | -8.3% | -0.023 to -0.000643 | better |
| host CPU-seconds | 240 | 217 | -9.5% | -44.3 to -1.51 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.577 | 0.524 | -9.1% | -0.103 to -0.00206 | better |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 13.6 to 31.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,203 | +1.5% | 8.15 to 28.5 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00211 to 0.00351 | same |
| cache hit rate | 0.79 | 0.802 | +1.5% | 0.00544 to 0.019 | better |
| latency, 95th percentile (ms) | 5.53 | 5.52 | -0.2% | -0.0616 to 0.0367 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.65 | 5.65 | -0.0% | -0.029 to 0.0252 | no difference beyond the noise |
| latency, mean (ms) | 1.22 | 1.16 | -5.3% | -0.0887 to -0.0415 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.1 | +4.8% | 0.311 to 5.88 | **WORSE** |
| memory used, mean (MB) | 61.2 | 64.3 | +5.1% | 0.29 to 5.94 | **WORSE** |
| keys evicted | 137,942 | 131,053 | -5.0% | -10,711 to -3,067 | shown, not judged |
| host CPU busy (share of the run) | 0.0864 | 0.0926 | +7.2% | -0.0161 to 0.0285 | no difference beyond the noise |
| host CPU-seconds | 152 | 164 | +8.2% | -31.4 to 56.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.285 | 0.304 | +6.5% | -0.0641 to 0.101 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 17.9 to 25.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
