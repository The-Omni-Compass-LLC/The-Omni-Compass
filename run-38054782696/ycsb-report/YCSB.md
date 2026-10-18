# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,892 | 2,892 | -0.0% | -4.88 to 4.83 | no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,896 | +0.0% | -3.91 to 4.05 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.356 | 0.35 | -1.7% | -0.0254 to 0.0134 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.519 | 0.519 | +0.1% | -0.0336 to 0.0342 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.204 | -1.1% | -0.00823 to 0.00376 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 450 | -12.1% | -63.5 to -60.7 | better |
| bytes in the cache, mean (MB) | 419 | 367 | -12.5% | -58.6 to -46.2 | better |
| pages read into the cache (misses) | 725,227 | 747,456 | +3.1% | -16,221 to 60,679 | shown, not judged |
| host CPU busy (share of the run) | 0.192 | 0.174 | -9.4% | -0.0748 to 0.0387 | no difference beyond the noise |
| host CPU-seconds | 328 | 292 | -11.0% | -153 to 80.6 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.247 | 0.22 | -11.0% | -0.115 to 0.0603 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,889 | -0.1% | -5.03 to 1.42 | no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,896 | -0.1% | -3.47 to 0.269 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.424 | 0.426 | +0.5% | -0.000484 to 0.00448 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.575 | 0.589 | +2.6% | 0.00293 to 0.0264 | **WORSE** |
| latency, mean (ms) | 0.219 | 0.219 | -0.1% | -0.00703 to 0.00668 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 448 | -12.5% | -76.4 to -52 | better |
| bytes in the cache, mean (MB) | 404 | 350 | -13.4% | -63.3 to -44.9 | better |
| pages read into the cache (misses) | 265,564 | 286,686 | +8.0% | -8,142 to 50,385 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.171 | -1.2% | -0.0548 to 0.0508 | no difference beyond the noise |
| host CPU-seconds | 117 | 116 | -1.2% | -44.8 to 41.9 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.217 | -1.2% | -0.0841 to 0.0788 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 1.52 to 6.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,870 | 2,870 | -0.0% | -206 to 205 | no difference beyond the noise |
| throughput (operations a second) | 2,875 | 2,875 | -0.0% | -204 to 203 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.243 | 0.248 | +1.9% | 0.0018 to 0.00754 | **WORSE** |
| latency, 99th percentile (ms) | 0.378 | 0.382 | +1.1% | -0.00817 to 0.0168 | no difference beyond the noise |
| latency, mean (ms) | 0.181 | 0.196 | +8.5% | -0.018 to 0.0486 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 487 | -5.0% | -106 to 54.6 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 393 | -5.0% | -85.9 to 44.5 | no difference beyond the noise |
| pages read into the cache (misses) | 697,486 | 706,826 | +1.3% | -157,972 to 176,652 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.14 | -6.1% | -0.0744 to 0.0564 | no difference beyond the noise |
| host CPU-seconds | 269 | 250 | -7.0% | -154 to 117 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.204 | 0.19 | -7.0% | -0.111 to 0.0828 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,751 | 5,748 | -0.0% | -13.7 to 8.42 | no difference beyond the noise |
| throughput (operations a second) | 5,770 | 5,767 | -0.0% | -13.7 to 8.4 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.348 | 0.35 | +0.6% | -0.00545 to 0.00945 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.64 | 0.64 | -0.1% | -0.00792 to 0.00726 | no difference beyond the noise |
| latency, mean (ms) | 0.167 | 0.168 | +0.8% | 0.000415 to 0.00219 | **WORSE** |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 437 | -14.7% | -103 to -48.2 | better |
| bytes in the cache, mean (MB) | 417 | 357 | -14.2% | -81.5 to -37.3 | better |
| pages read into the cache (misses) | 685,811 | 801,296 | +16.8% | 77,873 to 153,097 | shown, not judged |
| host CPU busy (share of the run) | 0.236 | 0.235 | -0.3% | -0.0491 to 0.0477 | no difference beyond the noise |
| host CPU-seconds | 433 | 430 | -0.7% | -116 to 110 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.162 | -0.7% | -0.0435 to 0.0412 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.32, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,876 | 2,844 | -1.1% | -290 to 224 | no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,854 | -1.2% | -287 to 220 | no difference beyond the noise |
| latency, 95th percentile (ms) | 0.275 | 0.281 | +2.1% | -0.00868 to 0.02 | no difference beyond the noise |
| latency, 99th percentile (ms) | 0.446 | 0.456 | +2.2% | -0.0313 to 0.0513 | no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.209 | +1.4% | -0.0601 to 0.0658 | no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | same |
| cache size held, mean (MB; the knob, the resource) | 512 | 465 | -9.3% | -126 to 31.4 | no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 379 | -8.6% | -88.3 to 17.2 | no difference beyond the noise |
| pages read into the cache (misses) | 675,083 | 719,478 | +6.6% | -80,923 to 169,713 | shown, not judged |
| host CPU busy (share of the run) | 0.202 | 0.196 | -2.9% | -0.0624 to 0.0508 | no difference beyond the noise |
| host CPU-seconds | 367 | 353 | -3.9% | -138 to 109 | no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.278 | 0.271 | -2.7% | -0.0792 to 0.0642 | no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | 1.23 to 4.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
