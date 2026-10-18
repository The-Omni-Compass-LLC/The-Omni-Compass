# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -2.48 to 1.51 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00759 to 0.00717 | same |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.00154 to 0.000955 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% | -0.036 to 0.0344 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 5.77 | +0.1% | -0.0437 to 0.0581 | no difference beyond the noise |
| latency, mean (ms) | 1.68 | 1.68 | +0.2% | -0.023 to 0.0302 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.8 | -3.4% | -4.75 to 0.425 | no difference beyond the noise |
| memory used, mean (MB) | 57.1 | 55.7 | -2.6% | -3.29 to 0.375 | no difference beyond the noise |
| keys evicted | 71,705 | 71,778 | +0.1% | -278 to 425 | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.117 | -5.9% | -0.0277 to 0.0131 | no difference beyond the noise |
| host CPU-seconds | 88 | 82.1 | -6.7% | -22.9 to 11.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.454 | 0.424 | -6.7% | -0.119 to 0.0583 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,299 | +2.6% | 27.5 to 38.2 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00362 to 0.00166 | same |
| cache hit rate | 0.845 | 0.867 | +2.6% | 0.0183 to 0.0256 | better |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.2% | -0.0148 to -0.00745 | better |
| latency, 99th percentile (ms) | 5.81 | 5.81 | -0.0% | -0.0128 to 0.00951 | no difference beyond the noise |
| latency, mean (ms) | 1.06 | 0.935 | -11.6% | -0.137 to -0.108 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 66.2 | +3.4% | -2.24 to 6.65 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.6 | +2.2% | -2.92 to 5.62 | no difference beyond the noise |
| keys evicted | 103,312 | 89,028 | -13.8% | -16,531 to -12,035 | shown, not judged |
| host CPU busy (share of the run) | 0.116 | 0.108 | -7.0% | -0.0228 to 0.00651 | no difference beyond the noise |
| host CPU-seconds | 193 | 179 | -7.4% | -41 to 12.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.339 | 0.307 | -9.7% | -0.0782 to 0.0123 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 28 |  | 14.9 to 41.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 924 | -0.1% | -2.89 to 0.318 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0556 to 0.0724 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.616 | -0.1% | -0.0018 to -1.66e-05 | **WORSE** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% | -0.0123 to 0.012 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.1% | -0.0117 to 0.0231 | no difference beyond the noise |
| latency, mean (ms) | 2.26 | 2.27 | +0.2% | -0.00839 to 0.0184 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.5% | -0.0382 to 2 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.8 | +0.2% | 0.0561 to 0.184 | **WORSE** |
| keys evicted | 243,159 | 244,886 | +0.7% | -2,359 to 5,812 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.148 | +8.1% | -0.0232 to 0.0453 | no difference beyond the noise |
| host CPU-seconds | 228 | 249 | +9.4% | -44.9 to 87.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.547 | 0.599 | +9.6% | -0.108 to 0.212 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.7 |  | 18.9 to 26.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 22.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,241 | +4.8% | 47.8 to 65.3 | better |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0136 to 0.0152 | same |
| cache hit rate | 0.79 | 0.827 | +4.8% | 0.0318 to 0.0435 | better |
| latency, 95th percentile (ms) | 5.56 | 5.54 | -0.2% | -0.131 to 0.106 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.66 | 5.67 | +0.0% | -0.0585 to 0.064 | no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.04 | -15.9% | -0.231 to -0.161 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 78.9 | +23.3% | 9.11 to 20.7 | **WORSE** |
| memory used, mean (MB) | 61.2 | 73.2 | +19.5% | 9.9 to 14 | **WORSE** |
| keys evicted | 137,972 | 114,195 | -17.2% | -26,056 to -21,500 | shown, not judged |
| host CPU busy (share of the run) | 0.0974 | 0.0853 | -12.4% | -0.0291 to 0.00507 | no difference beyond the noise |
| host CPU-seconds | 173 | 150 | -13.4% | -54.6 to 8.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.324 | 0.268 | -17.4% | -0.113 to -7.46e-05 | better |
| ceiling changes written (the knob's moves) | 0 | 38.7 |  | 28.6 to 48.7 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 20.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
