# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% | -2.9 to 1.39 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,899 | -0.0% | -2.58 to 0.92 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.332 | 0.329 | -1.0% | -0.0226 to 0.016 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.509 | 0.502 | -1.4% | -0.042 to 0.028 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.203 | 0.203 | -0.1% | -0.00763 to 0.00716 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -3.34 to -3.34 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.2% | -3.39 to 1.32 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,175 | 714,965 | +2.0% | -95,244 to 122,825 | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.192 | +9.7% | 0.00204 to 0.032 | power given |
| host CPU-seconds | 295 | 330 | +12.1% | 4.71 to 66.6 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.248 | +12.1% | 0.00356 to 0.0499 | power given |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | -0.0% | -4.71 to 2.83 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,919 | 2,918 | -0.0% | -2.46 to 0.902 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.326 | +0.4% | -0.00584 to 0.00851 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.439 | 0.441 | +0.5% | -0.0525 to 0.0565 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.176 | 0.181 | +2.9% | -0.0305 to 0.0406 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 493 | -3.8% | -70.4 to 31.4 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 406 | 391 | -3.7% | -59.5 to 29.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,641 | 276,899 | +5.0% | -32,693 to 59,209 | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.165 | +0.4% | -0.0517 to 0.053 | EVEN, no difference beyond the noise |
| host CPU-seconds | 119 | 120 | +0.3% | -44.2 to 44.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.224 | 0.224 | +0.2% | -0.0831 to 0.0841 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% | -3.23 to 0.627 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% | -3.99 to 0.337 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.307 | 0.306 | -0.2% | -0.00865 to 0.00732 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.534 | 0.517 | -3.1% | -0.0417 to 0.00834 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.191 | -1.3% | -0.00635 to 0.00134 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -4.86 to -0.25 | GAIN |
| bytes in the cache, mean (MB) | 417 | 420 | +0.6% | -6.1 to 10.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 687,294 | 728,080 | +5.9% | -69,182 to 150,754 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.147 | -16.3% | -0.0972 to 0.0399 | EVEN, no difference beyond the noise |
| host CPU-seconds | 302 | 245 | -18.8% | -192 to 78.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.184 | -18.8% | -0.144 to 0.059 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,818 | 5,812 | -0.1% | -19.8 to 8.22 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,829 | 5,824 | -0.1% | -20.1 to 9.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.223 | 0.224 | +0.7% | -0.00213 to 0.00546 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.416 | 0.427 | +2.6% | -0.0102 to 0.0322 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.112 | 0.112 | +0.1% | -0.00245 to 0.00261 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -4.71 to -3.27 | GAIN |
| bytes in the cache, mean (MB) | 418 | 417 | -0.3% | -2.19 to -0.312 | GAIN |
| pages read into the cache (misses) | 697,229 | 702,949 | +0.8% | -11,841 to 23,280 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.147 | -5.3% | -0.0499 to 0.0333 | EVEN, no difference beyond the noise |
| host CPU-seconds | 281 | 264 | -6.2% | -106 to 71.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.105 | 0.0986 | -6.2% | -0.0397 to 0.0266 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,925 | -0.0% | -4.53 to 3.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,932 | 2,932 | -0.0% | -2.73 to 1.87 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.257 | 0.255 | -0.5% | -0.00892 to 0.00626 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.429 | -0.7% | -0.0242 to 0.0182 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.112 | 0.11 | -1.8% | -0.00626 to 0.00213 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.1% | -13.6 to 2.11 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 415 | -0.8% | -11.5 to 5.14 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 692,291 | 705,918 | +2.0% | -21,416 to 48,670 | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.135 | -10.4% | -0.0544 to 0.023 | EVEN, no difference beyond the noise |
| host CPU-seconds | 277 | 245 | -11.6% | -112 to 47.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.183 | -11.6% | -0.0836 to 0.0355 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
