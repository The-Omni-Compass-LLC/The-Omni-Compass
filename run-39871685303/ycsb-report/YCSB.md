# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,890 | -0.1% | -2.6 to -0.996 | LOSS |
| throughput (operations a second) | 2,894 | 2,892 | -0.1% | -2.57 to -0.848 | LOSS |
| latency, 95th percentile (ms) | 0.302 | 0.301 | -0.2% | -0.00446 to 0.00313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.436 | -0.9% | -0.013 to 0.00496 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.177 | 0.177 | +0.1% | -0.00552 to 0.00601 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -8.48 to 0.522 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 417 | -0.1% | -13.7 to 12.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,071 | 698,577 | -0.4% | -159,064 to 154,076 | shown, not judged |
| host CPU busy (share of the run) | 0.185 | 0.196 | +6.0% | -0.0525 to 0.0746 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 350 | +7.4% | -113 to 161 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.245 | 0.263 | +7.4% | -0.0846 to 0.121 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,880 | +0.0% | -0.497 to 1.39 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | +0.0% | -0.829 to 1.37 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.444 | 0.442 | -0.5% | -0.0141 to 0.00941 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.634 | 0.639 | +0.7% | -0.00568 to 0.015 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | +0.2% | -0.00781 to 0.00875 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 503 | -1.7% | -12.6 to -4.71 | GAIN |
| bytes in the cache, mean (MB) | 401 | 395 | -1.6% | -20.3 to 7.44 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 262,772 | 276,604 | +5.3% | -26,316 to 53,980 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.2 | +3.8% | -0.0595 to 0.0743 | EVEN, no difference beyond the noise |
| host CPU-seconds | 133 | 139 | +4.2% | -51.9 to 63.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.251 | 0.261 | +4.2% | -0.0979 to 0.119 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,888 | -0.0% | -1.49 to 0.725 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,891 | -0.0% | -1.25 to 0.435 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.309 | 0.31 | +0.3% | -0.00983 to 0.0118 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.457 | 0.459 | +0.4% | -0.027 to 0.0304 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.187 | 0.187 | -0.0% | -0.00335 to 0.00326 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -7.34 to 0.0321 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 413 | -0.9% | -12.9 to 5.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 651,281 | 686,531 | +5.4% | -53,738 to 124,239 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.188 | +5.2% | 0.00658 to 0.0119 | power given |
| host CPU-seconds | 309 | 328 | +6.3% | 15.1 to 24 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.232 | 0.246 | +6.3% | 0.0113 to 0.018 | power given |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,684 | 5,690 | +0.1% | -7.23 to 20.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,700 | 5,707 | +0.1% | -6.87 to 21.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.425 | 0.424 | -0.2% | -0.00996 to 0.00796 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.639 | 0.639 | +0.0% | -0.00861 to 0.00861 | EVEN, the same |
| latency, mean (ms) | 0.243 | 0.242 | -0.4% | -0.00612 to 0.00435 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -6.31 to -0.192 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.6% | -5.25 to 0.305 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,057 | 686,354 | +0.5% | -10,332 to 16,926 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.326 | +0.9% | -0.0136 to 0.0196 | EVEN, no difference beyond the noise |
| host CPU-seconds | 583 | 590 | +1.2% | -34.2 to 48.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.222 | +1.0% | -0.013 to 0.0175 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,874 | -0.0% | -9.4 to 8.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,884 | -0.0% | -9.92 to 8.56 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.361 | 0.362 | +0.3% | -0.00397 to 0.00597 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.583 | 0.587 | +0.7% | -0.00983 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.22 | +0.9% | -0.00177 to 0.00557 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -7.13 to -1.39 | GAIN |
| bytes in the cache, mean (MB) | 418 | 416 | -0.4% | -5.19 to 1.73 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 678,175 | 685,223 | +1.0% | 4,480 to 9,618 | shown, not judged |
| host CPU busy (share of the run) | 0.23 | 0.249 | +8.1% | -0.0408 to 0.0781 | EVEN, no difference beyond the noise |
| host CPU-seconds | 394 | 436 | +10.6% | -93 to 176 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.297 | 0.328 | +10.5% | -0.0693 to 0.132 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
