# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,074 | 1,075 | +0.1% | -0.772 to 1.91 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0057 to 0.0028 | same |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.00122 to 0.00108 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% | -1.76e-05 to 0.00211 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.31 | 5.31 | -0.2% | -0.0906 to 0.0731 | no difference beyond the noise |
| latency, mean (ms) | 1.55 | 1.54 | -0.2% | -0.0157 to 0.00857 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.3 | -4.3% | -2.87 to -2.61 | better |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% | -1.96 to -1.7 | better |
| keys evicted | 71,745 | 71,777 | +0.0% | -254 to 317 | shown, not judged |
| host CPU busy (share of the run) | 0.0494 | 0.0532 | +7.6% | -0.0983 to 0.106 | no difference beyond the noise |
| host CPU-seconds | 34.4 | 37.4 | +8.8% | -71.8 to 77.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.178 | 0.194 | +8.8% | -0.372 to 0.403 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,342 | +5.9% | -21.7 to 171 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00234 to 0.0017 | same |
| cache hit rate | 0.845 | 0.895 | +5.9% | -0.0143 to 0.114 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.72 | -0.4% | -0.0703 to 0.0289 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.1% | -0.0318 to 0.0251 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.775 | -26.1% | -0.635 to 0.0868 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 73.1 | +14.2% | -5.72 to 24 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 67.6 | +10.3% | -5.37 to 18 | no difference beyond the noise |
| keys evicted | 103,236 | 70,109 | -32.1% | -76,806 to 10,551 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.107 | -10.2% | -0.0368 to 0.0127 | no difference beyond the noise |
| host CPU-seconds | 199 | 178 | -10.6% | -65.2 to 23.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.348 | 0.294 | -15.5% | -0.152 to 0.0436 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 45.3 |  | 25.1 to 65.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 926 | +0.0% | -8.76 to 9.44 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0271 to 0.00288 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.618 | +0.0% | -0.00559 to 0.0061 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% | -0.0116 to 0.0219 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.76 | +0.3% | -0.00734 to 0.0399 | no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.27 | +0.1% | -0.0368 to 0.0426 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.8 | +4.4% | -3.91 to 9.6 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 62 | +2.2% | -4.89 to 7.56 | no difference beyond the noise |
| keys evicted | 243,086 | 245,111 | +0.8% | -1,957 to 6,006 | shown, not judged |
| host CPU busy (share of the run) | 0.141 | 0.149 | +5.0% | -0.00866 to 0.0229 | no difference beyond the noise |
| host CPU-seconds | 237 | 250 | +5.6% | -16.6 to 43.3 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.569 | 0.6 | +5.6% | -0.0369 to 0.1 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | 18 to 28 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 18.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,242 | +4.9% | 45 to 72.1 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | 0.00094 to 0.00422 | better |
| cache hit rate | 0.79 | 0.829 | +5.0% | 0.0301 to 0.048 | better |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0191 to -0.000388 | better |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% | -0.0177 to 0.0132 | no difference beyond the noise |
| latency, mean (ms) | 1.35 | 1.13 | -16.0% | -0.271 to -0.161 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 80.4 | +25.7% | 5.37 to 27.5 | **WORSE** |
| memory used, mean (MB) | 61.2 | 73.8 | +20.7% | 4.81 to 20.5 | **WORSE** |
| keys evicted | 138,054 | 113,055 | -18.1% | -31,376 to -18,621 | shown, not judged |
| host CPU busy (share of the run) | 0.127 | 0.117 | -7.9% | -0.0414 to 0.0214 | no difference beyond the noise |
| host CPU-seconds | 213 | 195 | -8.2% | -77.7 to 42.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.399 | 0.349 | -12.5% | -0.164 to 0.0639 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 41.7 |  | 21 to 62.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 19.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
