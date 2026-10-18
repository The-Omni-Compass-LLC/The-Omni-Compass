# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% | -1.07 to 0.478 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0342 to 0.0227 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.0% | -0.000674 to 0.000351 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | +0.0% | -0.0144 to 0.0159 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | -0.00896 to 0.0204 | no difference beyond the noise |
| latency, mean (ms) | 1.73 | 1.74 | +0.2% | -0.0041 to 0.0117 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 61.2 | -4.3% | -3.48 to -2.03 | better |
| memory used, mean (MB) | 57.2 | 55.3 | -3.2% | -2.62 to -1.06 | better |
| keys evicted | 71,743 | 71,798 | +0.1% | -150 to 260 | shown, not judged |
| host CPU busy (share of the run) | 0.134 | 0.139 | +3.6% | -0.00899 to 0.0186 | no difference beyond the noise |
| host CPU-seconds | 90.2 | 93.8 | +4.0% | -6.78 to 14 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.465 | 0.484 | +4.0% | -0.035 to 0.0726 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,295 | +2.3% | 20.7 to 37 | better |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00281 to 0.000242 | same |
| cache hit rate | 0.845 | 0.864 | +2.3% | 0.014 to 0.0241 | better |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.1% | -0.0272 to 0.0382 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.81 | +0.3% | -0.0195 to 0.0496 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.948 | -9.6% | -0.136 to -0.0665 | better |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | -2.1 to 4.87 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 62.3 | +1.6% | -3.33 to 5.28 | no difference beyond the noise |
| keys evicted | 103,554 | 91,070 | -12.1% | -15,470 to -9,498 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | -0.2% | -0.0179 to 0.0175 | no difference beyond the noise |
| host CPU-seconds | 206 | 205 | -0.2% | -35.2 to 34.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.361 | 0.353 | -2.4% | -0.0691 to 0.0514 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 27.7 |  | 8.86 to 46.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 927 | +0.3% | -23.8 to 29.9 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0163 to -0.00549 | **WORSE** |
| cache hit rate | 0.617 | 0.619 | +0.3% | -0.016 to 0.0196 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% | -0.0119 to 0.0116 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.26 | +0.1% | -0.0433 to 0.0527 | no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.03 | -0.6% | -0.11 to 0.0841 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.7% | -6.2 to 9.67 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 62.3 | +2.6% | -6.64 to 9.8 | no difference beyond the noise |
| keys evicted | 243,120 | 241,958 | -0.5% | -21,058 to 18,735 | shown, not judged |
| host CPU busy (share of the run) | 0.0597 | 0.0638 | +7.0% | -0.0461 to 0.0544 | no difference beyond the noise |
| host CPU-seconds | 105 | 113 | +7.8% | -85 to 101 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.253 | 0.271 | +7.2% | -0.204 to 0.241 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 19 |  | 1.61 to 36.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,194 | +0.8% | -19.9 to 39.7 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000273 to 0.00699 | no difference beyond the noise |
| cache hit rate | 0.79 | 0.796 | +0.8% | -0.0131 to 0.0264 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.73 | 5.73 | -0.1% | -0.0143 to 0.0076 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.0% | -0.0103 to 0.0131 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.31 | -2.5% | -0.146 to 0.0779 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.3 | +2.0% | -4.12 to 6.67 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% | -3.75 to 6.4 | no difference beyond the noise |
| keys evicted | 137,957 | 135,118 | -2.1% | -16,156 to 10,478 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.116 | -4.6% | -0.0586 to 0.0474 | no difference beyond the noise |
| host CPU-seconds | 204 | 193 | -5.2% | -112 to 91.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.382 | 0.359 | -6.1% | -0.205 to 0.159 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 12.3 to 31.1 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 15.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
