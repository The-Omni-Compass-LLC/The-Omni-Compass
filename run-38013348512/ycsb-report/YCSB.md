# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,896 | 2,894 | -0.1% | -3.25 to -1.08 | **WORSE** |
| throughput (operations a second) | 2,900 | 2,898 | -0.1% | -3.22 to -0.829 | **WORSE** |
| latency, 95th percentile (ms) | 0.33 | 0.337 | +2.1% | -0.00811 to 0.0221 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.489 | 0.496 | +1.5% | -0.00207 to 0.0167 | no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.202 | +0.3% | -0.00752 to 0.0089 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 469 | -8.3% | -125 to 39.6 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 386 | -7.5% | -95.9 to 33 | no difference beyond the noise |
| pages read into the cache (misses) | 690,302 | 764,770 | +10.8% | -99,700 to 248,636 | shown, not judged |
| host CPU busy (share of the run) | 0.181 | 0.205 | +12.9% | -0.00747 to 0.0544 | no difference beyond the noise |
| host CPU-seconds | 308 | 357 | +16.0% | -12.5 to 111 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.268 | +16.0% | -0.00934 to 0.0832 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,890 | -0.0% | -2.24 to 0.918 | no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,896 | -0.0% | -2.7 to 1.46 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.405 | 0.406 | +0.2% | -0.0104 to 0.0124 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.557 | 0.555 | -0.4% | -0.0158 to 0.0118 | no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.218 | +0.2% | -0.00199 to 0.00268 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 463 | -9.5% | -95 to -2.28 | better |
| bytes in the cache, mean (MB) | 405 | 364 | -10.2% | -72 to -10.2 | better |
| pages read into the cache (misses) | 265,105 | 282,698 | +6.6% | -8,457 to 43,643 | shown, not judged |
| host CPU busy (share of the run) | 0.177 | 0.162 | -8.8% | -0.107 to 0.0752 | no difference beyond the noise |
| host CPU-seconds | 121 | 107 | -11.2% | -89.1 to 62 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.202 | -11.2% | -0.167 to 0.116 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,917 | 2,917 | -0.0% | -5.75 to 4.74 | no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,920 | -0.0% | -4.62 to 3.95 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.233 | 0.231 | -1.0% | -0.0095 to 0.00484 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.383 | 0.38 | -0.8% | -0.00797 to 0.00197 | no difference beyond the noise |
| latency, mean (ms) | 0.154 | 0.162 | +5.2% | -0.0152 to 0.0314 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 490 | -4.3% | -109 to 64.8 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 400 | -4.8% | -86 to 46.1 | no difference beyond the noise |
| pages read into the cache (misses) | 696,621 | 722,119 | +3.7% | -105,183 to 156,180 | shown, not judged |
| host CPU busy (share of the run) | 0.139 | 0.156 | +12.1% | -0.0663 to 0.1 | no difference beyond the noise |
| host CPU-seconds | 247 | 283 | +14.4% | -137 to 209 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.185 | 0.212 | +14.3% | -0.103 to 0.156 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,774 | 5,769 | -0.1% | -17.2 to 5.84 | no difference beyond the noise |
| throughput (operations a second) | 5,788 | 5,784 | -0.1% | -20.7 to 11.8 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.325 | +0.2% | -0.00651 to 0.00784 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.5 | 0.502 | +0.5% | -0.0122 to 0.0169 | no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.19 | +0.8% | -0.00844 to 0.0115 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 443 | -13.4% | -81.1 to -56.1 | better |
| bytes in the cache, mean (MB) | 418 | 365 | -12.7% | -62.7 to -43.7 | better |
| pages read into the cache (misses) | 699,679 | 787,955 | +12.6% | 62,986 to 113,566 | shown, not judged |
| host CPU busy (share of the run) | 0.239 | 0.245 | +2.6% | -0.0347 to 0.047 | no difference beyond the noise |
| host CPU-seconds | 433 | 445 | +2.9% | -80.1 to 105 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.167 | +2.9% | -0.0301 to 0.0396 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,880 | -0.0% | -26.5 to 25.3 | no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -26.3 to 24.2 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.374 | 0.378 | +1.1% | -0.0181 to 0.0261 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.644 | 0.641 | -0.6% | -0.0298 to 0.0224 | no difference beyond the noise |
| latency, mean (ms) | 0.226 | 0.23 | +2.0% | -0.00704 to 0.0162 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 447 | -12.6% | -74 to -55.3 | better |
| bytes in the cache, mean (MB) | 417 | 367 | -12.2% | -58.3 to -43.2 | better |
| pages read into the cache (misses) | 679,732 | 766,408 | +12.8% | 76,144 to 97,207 | shown, not judged |
| host CPU busy (share of the run) | 0.231 | 0.23 | -0.5% | -0.0218 to 0.0196 | no difference beyond the noise |
| host CPU-seconds | 396 | 391 | -1.4% | -50.1 to 38.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.299 | 0.295 | -1.5% | -0.0367 to 0.028 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
