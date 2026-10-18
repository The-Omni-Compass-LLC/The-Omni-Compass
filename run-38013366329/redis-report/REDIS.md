# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.1% | -1.87 to 0.422 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00909 to 0.0136 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.717 | -0.1% | -0.00118 to 0.000324 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.00888 to 0.0157 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% | 0.00563 to 0.0187 | **WORSE** |
| latency, mean (ms) | 1.74 | 1.75 | +0.5% | -0.00271 to 0.0203 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 60.9 | -4.8% | -3.22 to -2.88 | better |
| memory used, mean (MB) | 57.2 | 55 | -3.7% | -2.36 to -1.91 | better |
| keys evicted | 71,739 | 71,864 | +0.2% | -54.8 to 304 | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.136 | +9.0% | -0.0342 to 0.0568 | no difference beyond the noise |
| host CPU-seconds | 83.5 | 91.8 | +9.9% | -26.6 to 43.2 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.431 | 0.474 | +10.0% | -0.137 to 0.223 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 10 |  | 10 to 10 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,282 | +1.2% | -20.6 to 52.2 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000549 to 0.00183 | same |
| cache hit rate | 0.845 | 0.855 | +1.2% | -0.0135 to 0.0346 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% | -0.0162 to 0.0238 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% | -0.00784 to 0.0265 | no difference beyond the noise |
| latency, mean (ms) | 1.05 | 0.996 | -5.1% | -0.194 to 0.0857 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.4 | +0.6% | -4.29 to 5.02 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.2 | -0.1% | -5.25 to 5.1 | no difference beyond the noise |
| keys evicted | 103,490 | 96,724 | -6.5% | -22,893 to 9,361 | shown, not judged |
| host CPU busy (share of the run) | 0.11 | 0.121 | +9.7% | -0.0284 to 0.0497 | no difference beyond the noise |
| host CPU-seconds | 183 | 203 | +10.8% | -52.1 to 91.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.321 | 0.352 | +9.5% | -0.102 to 0.163 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 26.7 |  | 4.96 to 48.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 12.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 922 | -0.4% | -12.8 to 5.35 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00854 to 0.00271 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.615 | -0.4% | -0.00846 to 0.00356 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.54 | 5.54 | +0.0% | -0.00711 to 0.00958 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | +0.1% | -0.000539 to 0.00811 | no difference beyond the noise |
| latency, mean (ms) | 2.13 | 2.15 | +0.7% | -0.0156 to 0.0445 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.8 | -0.3% | -1.54 to 1.1 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.3 | -0.7% | -1.59 to 0.761 | no difference beyond the noise |
| keys evicted | 243,069 | 246,886 | +1.6% | -4,817 to 12,451 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.115 | +3.0% | -0.00573 to 0.0125 | no difference beyond the noise |
| host CPU-seconds | 200 | 206 | +3.2% | -12.5 to 25.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.48 | 0.497 | +3.7% | -0.0271 to 0.0622 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 4.76 to 38.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,199 | +1.3% | -16.6 to 48.4 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0118 to 0.00418 | no difference beyond the noise |
| cache hit rate | 0.789 | 0.8 | +1.4% | -0.0102 to 0.0318 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.2 | 5.2 | +0.0% | -0.00703 to 0.00715 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.23 | 5.24 | +0.1% | -0.0148 to 0.0232 | no difference beyond the noise |
| latency, mean (ms) | 1.16 | 1.11 | -4.4% | -0.181 to 0.0783 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 67.4 | +5.4% | -3.64 to 10.5 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 64.2 | +5.0% | -3.28 to 9.39 | no difference beyond the noise |
| keys evicted | 138,126 | 132,219 | -4.3% | -20,957 to 9,143 | shown, not judged |
| host CPU busy (share of the run) | 0.0567 | 0.0528 | -6.9% | -0.018 to 0.0102 | no difference beyond the noise |
| host CPU-seconds | 100 | 92.8 | -7.4% | -33.4 to 18.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.188 | 0.172 | -8.5% | -0.0671 to 0.035 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23 |  | -2.82 to 48.8 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 14.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
