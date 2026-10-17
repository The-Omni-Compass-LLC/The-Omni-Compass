# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.1% | -3.19 to -0.41 | LOSS |
| throughput (operations a second) | 2,901 | 2,899 | -0.1% | -3.06 to -0.305 | LOSS |
| latency, 95th percentile (ms) | 0.321 | 0.326 | +1.6% | -0.00361 to 0.0136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.483 | 0.492 | +2.0% | -0.0224 to 0.0417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.202 | +2.5% | -0.00323 to 0.0132 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -22.4 to 4.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 411 | -1.7% | -21.6 to 7.13 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 697,708 | 688,177 | -1.4% | -152,316 to 133,255 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.189 | +6.3% | -0.0511 to 0.0733 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 325 | +6.9% | -107 to 149 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.244 | +6.9% | -0.0801 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,889 | -0.0% | -4.62 to 2.72 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,897 | -0.0% | -3.76 to 1.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.5 | 0.498 | -0.3% | -0.00277 to 0.000101 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.636 | 0.637 | +0.1% | -0.00907 to 0.00974 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.228 | -0.1% | -0.00494 to 0.0047 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 504 | -1.6% | -13.4 to -3.46 | GAIN |
| bytes in the cache, mean (MB) | 402 | 400 | -0.4% | -16.9 to 13.3 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,592 | 272,124 | +2.8% | -4,409 to 19,474 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.147 | -12.0% | -0.0774 to 0.0373 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 96.9 | -14.1% | -61.1 to 29.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.182 | -14.1% | -0.115 to 0.0555 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,893 | -0.1% | -5.4 to 1.65 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -5.32 to 1.64 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.32 | 0.319 | -0.4% | -0.00759 to 0.00492 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.491 | 0.488 | -0.5% | -0.0127 to 0.00801 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.202 | +0.2% | -0.00216 to 0.00314 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -10.6 to 2.99 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 419 | +0.2% | -3.57 to 5.11 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,013 | 704,742 | +3.0% | -172,878 to 214,336 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.17 | -1.5% | -0.0218 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 292 | 286 | -2.0% | -43.2 to 31.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.219 | 0.215 | -2.0% | -0.0325 to 0.0236 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,741 | 5,740 | -0.0% | -15.3 to 12.4 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,761 | 5,760 | -0.0% | -12.4 to 10.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.356 | 0.357 | +0.4% | -0.0112 to 0.0138 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.656 | 0.655 | -0.2% | -0.0273 to 0.0253 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.171 | 0.171 | +0.3% | -0.00484 to 0.00577 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -41.9 to 19.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 409 | -1.7% | -30 to 15.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 692,812 | 706,764 | +2.0% | -31,966 to 59,868 | shown, not judged |
| host CPU busy (share of the run) | 0.233 | 0.237 | +1.9% | -0.0264 to 0.0352 | EVEN, no difference beyond the noise |
| host CPU-seconds | 419 | 430 | +2.5% | -56.8 to 77.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.158 | 0.162 | +2.5% | -0.0219 to 0.0297 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,905 | 2,902 | -0.1% | -28.2 to 22.8 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,912 | -0.1% | -27.6 to 20.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.279 | 0.28 | +0.5% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.462 | 0.456 | -1.4% | -0.0328 to 0.0194 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.195 | +0.6% | -0.019 to 0.0212 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -4.54 to -2.54 | GAIN |
| bytes in the cache, mean (MB) | 417 | 413 | -0.9% | -10.5 to 2.61 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,673 | 679,772 | +0.0% | -7,652 to 7,850 | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.185 | +7.4% | -0.0442 to 0.0698 | EVEN, no difference beyond the noise |
| host CPU-seconds | 303 | 330 | +8.7% | -93.3 to 146 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.248 | +8.8% | -0.0686 to 0.109 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
