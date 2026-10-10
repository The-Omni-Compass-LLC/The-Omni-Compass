# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -3.39 to 3.1 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0483 to 0.023 | no difference beyond the noise |
| cache hit rate | 0.718 | 0.718 | -0.0% | -0.0014 to 0.0013 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.22 | 5.21 | -0.1% | -0.0103 to 0.00261 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 5.28 | +0.0% | -0.149 to 0.149 | no difference beyond the noise |
| latency, mean (ms) | 1.54 | 1.54 | +0.1% | -0.0288 to 0.0308 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62 | -3.1% | -4.69 to 0.687 | no difference beyond the noise |
| memory used, mean (MB) | 57.2 | 55.9 | -2.2% | -3.04 to 0.531 | no difference beyond the noise |
| keys evicted | 71,704 | 71,735 | +0.0% | -313 to 375 | shown, not judged |
| host CPU busy (share of the run) | 0.0669 | 0.0671 | +0.3% | -0.0462 to 0.0466 | no difference beyond the noise |
| host CPU-seconds | 47.5 | 47.7 | +0.4% | -35.4 to 35.8 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.245 | 0.247 | +0.5% | -0.182 to 0.184 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 8.67 |  | 2.93 to 14.4 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 8.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,287 | +1.6% | -13.3 to 55 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0027 to 0.00285 | same |
| cache hit rate | 0.845 | 0.859 | +1.7% | -0.00892 to 0.0369 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.00456 to 0.00447 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% | 0.00166 to 0.00708 | **WORSE** |
| latency, mean (ms) | 1.05 | 0.975 | -7.1% | -0.202 to 0.0536 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.6 | +1.0% | -5.21 to 6.49 | no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61.7 | +0.7% | -5.52 to 6.39 | no difference beyond the noise |
| keys evicted | 103,555 | 94,503 | -8.7% | -24,642 to 6,538 | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.112 | +4.4% | -0.0348 to 0.0443 | no difference beyond the noise |
| host CPU-seconds | 179 | 188 | +5.1% | -65.3 to 83.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.314 | 0.324 | +3.4% | -0.114 to 0.135 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 24 |  | 8.49 to 39.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 9.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924 | 920 | -0.5% | -8.62 to 0.269 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0587 to 0.0847 | no difference beyond the noise |
| cache hit rate | 0.617 | 0.614 | -0.5% | -0.00518 to -0.000828 | **WORSE** |
| latency, 95th percentile (ms) | 5.2 | 5.2 | -0.0% | -0.0119 to 0.0106 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.26 | 5.28 | +0.4% | -0.017 to 0.0571 | no difference beyond the noise |
| latency, mean (ms) | 2.05 | 2.06 | +0.7% | -0.00621 to 0.0365 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.5 | -0.7% | -0.96 to 0.0596 | no difference beyond the noise |
| memory used, mean (MB) | 60.7 | 60.1 | -1.0% | -1.21 to 0.0572 | no difference beyond the noise |
| keys evicted | 243,216 | 247,401 | +1.7% | -1,862 to 10,231 | shown, not judged |
| host CPU busy (share of the run) | 0.0657 | 0.0554 | -15.7% | -0.0373 to 0.0166 | no difference beyond the noise |
| host CPU-seconds | 117 | 97 | -16.8% | -70.2 to 31.1 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.234 | -16.4% | -0.167 to 0.075 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 23.7 |  | 17.4 to 29.9 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,189 | +0.4% | -18.7 to 27.7 | no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00234 to 0.00178 | same |
| cache hit rate | 0.79 | 0.793 | +0.4% | -0.0125 to 0.0186 | no difference beyond the noise |
| latency, 95th percentile (ms) | 5.72 | 5.72 | -0.0% | -0.00659 to 0.00641 | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.78 | 5.78 | +0.1% | -0.00335 to 0.0143 | no difference beyond the noise |
| latency, mean (ms) | 1.34 | 1.32 | -1.0% | -0.102 to 0.0752 | no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 64.9 | +1.4% | -2.81 to 4.62 | no difference beyond the noise |
| memory used, mean (MB) | 61.2 | 61.9 | +1.2% | -2.68 to 4.17 | no difference beyond the noise |
| keys evicted | 138,050 | 137,364 | -0.5% | -10,388 to 9,016 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.116 | +4.9% | -0.0794 to 0.0902 | no difference beyond the noise |
| host CPU-seconds | 184 | 194 | +5.4% | -149 to 169 | no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.346 | 0.364 | +5.1% | -0.287 to 0.322 | no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 25.3 |  | 19.1 to 31.6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 17.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
