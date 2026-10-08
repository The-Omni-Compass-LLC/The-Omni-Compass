# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,726 | 2,757 | +1.1% | -33.4 to 94.5 | no difference beyond the noise |
| throughput (operations a second) | 2,735 | 2,765 | +1.1% | -32.6 to 93.9 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.308 | 0.312 | +1.4% | -0.00192 to 0.0106 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.477 | 0.48 | +0.5% | -0.0191 to 0.0238 | no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.235 | -2.6% | -0.0284 to 0.0157 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 377 | -26.5% | -318 to 46.8 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 412 | 310 | -24.9% | -253 to 47.8 | no difference beyond the noise |
| pages read into the cache (misses) | 479,449 | 586,126 | +22.2% | -9,698 to 223,053 | shown, not judged |
| host CPU busy (share of the run) | 0.183 | 0.181 | -0.9% | -0.0508 to 0.0475 | no difference beyond the noise |
| host CPU-seconds | 225 | 221 | -1.8% | -74 to 65.7 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.268 | 0.26 | -2.8% | -0.0856 to 0.0707 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,852 | 2,849 | -0.1% | -8.62 to 3.02 | no difference beyond the noise |
| throughput (operations a second) | 2,861 | 2,859 | -0.1% | -6.87 to 2.75 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.457 | 0.458 | +0.1% | -0.0121 to 0.0134 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.669 | 0.67 | +0.1% | -0.0446 to 0.0466 | no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.246 | +2.2% | 0.00195 to 0.0087 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 263 | -48.7% | -249 to -249 | better |
| bytes in the cache, mean (MB) | 399 | 210 | -47.2% | -203 to -174 | better |
| pages read into the cache (misses) | 175,012 | 277,156 | +58.4% | 88,846 to 115,442 | shown, not judged |
| host CPU busy (share of the run) | 0.203 | 0.196 | -3.5% | -0.0585 to 0.0444 | no difference beyond the noise |
| host CPU-seconds | 91.3 | 87 | -4.7% | -32.4 to 23.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.259 | 0.247 | -4.7% | -0.0917 to 0.0674 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% | -2.29 to -0.391 | **WORSE** |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -2.92 to 0.332 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.359 | +0.6% | -0.00883 to 0.0128 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.537 | 0.536 | -0.2% | -0.00348 to 0.00148 | no difference beyond the noise |
| latency, mean (ms) | 0.127 | 0.133 | +4.9% | 0.00434 to 0.0082 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 259 | -49.4% | -253 to -253 | better |
| bytes in the cache, mean (MB) | 416 | 216 | -48.0% | -213 to -186 | better |
| pages read into the cache (misses) | 468,164 | 727,442 | +55.4% | 202,949 to 315,607 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.185 | +13.1% | -0.00867 to 0.0515 | no difference beyond the noise |
| host CPU-seconds | 200 | 229 | +14.7% | -15.3 to 74 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.259 | +14.7% | -0.0173 to 0.0837 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,767 | 5,769 | +0.0% | -8.94 to 12.9 | no difference beyond the noise |
| throughput (operations a second) | 5,781 | 5,781 | +0.0% | -12.8 to 13.6 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.255 | 0.259 | +1.4% | -0.00637 to 0.0137 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.434 | 0.435 | +0.4% | -0.02 to 0.0234 | no difference beyond the noise |
| latency, mean (ms) | 0.118 | 0.117 | -0.7% | -0.00609 to 0.00455 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -63.8 to -63.8 | better |
| bytes in the cache, mean (MB) | 415 | 370 | -11.0% | -47.9 to -43.5 | better |
| pages read into the cache (misses) | 465,847 | 531,465 | +14.1% | 38,965 to 92,271 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.161 | -6.3% | -0.0563 to 0.0346 | no difference beyond the noise |
| host CPU-seconds | 210 | 194 | -7.8% | -82.4 to 49.5 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.119 | 0.109 | -7.9% | -0.0466 to 0.0279 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1 |  | 1 to 1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 20.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `7ee471b4098e`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,833 | 2,841 | +0.3% | -40.5 to 57.2 | no difference beyond the noise |
| throughput (operations a second) | 2,847 | 2,854 | +0.2% | -39.6 to 53.7 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.488 | 0.485 | -0.6% | -0.0161 to 0.0101 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.693 | 0.679 | -2.0% | -0.059 to 0.0316 | no difference beyond the noise |
| latency, mean (ms) | 0.241 | 0.239 | -0.8% | -0.0123 to 0.00823 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 436 | -14.9% | -108 to -44.9 | better |
| bytes in the cache, mean (MB) | 416 | 357 | -14.1% | -81.5 to -35.8 | better |
| pages read into the cache (misses) | 458,716 | 533,512 | +16.3% | 23,234 to 126,357 | shown, not judged |
| host CPU busy (share of the run) | 0.256 | 0.258 | +0.7% | -0.0881 to 0.0919 | no difference beyond the noise |
| host CPU-seconds | 293 | 296 | +1.0% | -130 to 136 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.335 | 0.337 | +0.7% | -0.145 to 0.149 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 1.67 |  | 0.232 to 3.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
