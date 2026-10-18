# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.51 to 2.13 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00344 to 0.00627 | same |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.00166 to 0.00142 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.0% | -0.0143 to 0.0121 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | +0.1% | -0.0124 to 0.021 | no difference beyond the noise |
| latency, mean (ms) | 1.74 | 1.75 | +0.3% | -0.00238 to 0.0118 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.1 | -4.6% | -3.41 to -2.49 | better |
| memory used, mean (MB) | 57.2 | 55.2 | -3.5% | -2.49 to -1.48 | better |
| keys evicted | 71,747 | 71,787 | +0.1% | -391 to 470 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.141 | +2.4% | -0.094 to 0.1 | no difference beyond the noise |
| host CPU-seconds | 92.5 | 94.7 | +2.4% | -74.2 to 78.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.478 | 0.489 | +2.4% | -0.384 to 0.407 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,294 | +2.1% | 25.6 to 28.2 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00139 to 0.00164 | same |
| cache hit rate | 0.845 | 0.863 | +2.1% | 0.0171 to 0.0188 | better |
| latency, 95th percentile (ms) | 5.63 | 5.61 | -0.4% | -0.032 to -0.0118 | better |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.1% | -0.0175 to 0.00328 | no difference beyond the noise |
| latency, mean (ms) | 0.987 | 0.888 | -10.1% | -0.107 to -0.0918 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.3 | +0.5% | -0.0666 to 0.647 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.3 | +0.0% | -0.708 to 0.715 | no difference beyond the noise |
| keys evicted | 103,397 | 91,719 | -11.3% | -12,322 to -11,036 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.0934 | -21.1% | -0.0436 to -0.00643 | better |
| host CPU-seconds | 211 | 162 | -23.1% | -85.8 to -11.6 | better |
| host CPU-seconds per 1,000 requests inside the line | 0.37 | 0.279 | -24.7% | -0.157 to -0.026 | better |
| ceiling changes written (the knob's moves) | 0 | 27 |  | 20.4 to 33.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 13.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 920 | -0.6% | -6.15 to -4.83 | **WORSE** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0149 to 0.00856 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.614 | -0.6% | -0.00392 to -0.00329 | **WORSE** |
| latency, 95th percentile (ms) | 5.51 | 5.52 | +0.1% | -0.0237 to 0.0318 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.59 | +0.1% | -0.0117 to 0.0269 | no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.17 | +1.1% | 0.00834 to 0.0378 | **WORSE** |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.4 | -0.9% | -0.684 to -0.451 | better |
| memory used, mean (MB) | 60.7 | 60 | -1.2% | -0.797 to -0.644 | better |
| keys evicted | 243,254 | 248,936 | +2.3% | 5,485 to 5,880 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.111 | +1.2% | -0.00734 to 0.0101 | no difference beyond the noise |
| host CPU-seconds | 192 | 194 | +1.2% | -15.6 to 20.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.46 | 0.469 | +1.8% | -0.0354 to 0.0523 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 25.7 |  | 22.8 to 28.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.5% | -24.2 to 36.1 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0112 to 0.0156 | no difference beyond the noise |
| cache hit rate | 0.789 | 0.793 | +0.5% | -0.0162 to 0.0242 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% | -0.00954 to 0.00284 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% | -0.00845 to 0.0161 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.5% | -0.128 to 0.0873 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -5.51 to 7.42 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.2 | +1.7% | -5.17 to 7.24 | no difference beyond the noise |
| keys evicted | 138,116 | 137,044 | -0.8% | -14,660 to 12,517 | shown, not judged |
| host CPU busy (share of the run) | 0.129 | 0.117 | -9.5% | -0.0473 to 0.0227 | no difference beyond the noise |
| host CPU-seconds | 217 | 194 | -10.8% | -89.5 to 42.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.408 | 0.362 | -11.2% | -0.178 to 0.0867 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 10.9 to 34.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
