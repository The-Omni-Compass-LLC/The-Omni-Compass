# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,891 | -0.1% | -4.99 to 0.774 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -5.42 to 2.37 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.425 | +0.7% | -0.00596 to 0.012 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.55 | 0.56 | +1.8% | -0.0177 to 0.037 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.218 | -0.1% | -0.000977 to 0.00047 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.4% | -7.88 to -6.88 | GAIN |
| bytes in the cache, mean (MB) | 403 | 398 | -1.3% | -13.4 to 2.84 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 277,575 | 275,604 | -0.7% | -22,385 to 18,443 | shown, not judged |
| host CPU busy (share of the run) | 0.188 | 0.177 | -5.9% | -0.101 to 0.0785 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 120 | -7.2% | -84.6 to 66.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.243 | 0.226 | -7.1% | -0.159 to 0.124 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | -0.1% | -4.02 to 0.583 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,900 | 2,898 | -0.0% | -3.02 to 0.216 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.316 | 0.316 | +0.0% | -0.00745 to 0.00745 | EVEN, the same |
| latency, 99th percentile (ms) | 0.502 | 0.508 | +1.3% | -0.0188 to 0.0322 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.199 | +1.3% | -0.00276 to 0.0077 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.5% | -32.3 to 6.79 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 408 | -2.4% | -27 to 6.91 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 704,656 | 690,279 | -2.0% | -159,592 to 130,839 | shown, not judged |
| host CPU busy (share of the run) | 0.196 | 0.178 | -9.5% | -0.0742 to 0.037 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 305 | -11.4% | -156 to 77.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.229 | -11.4% | -0.117 to 0.0582 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,815 | 5,809 | -0.1% | -28 to 15.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,826 | 5,821 | -0.1% | -27.9 to 16.9 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.229 | 0.234 | +2.0% | -0.0136 to 0.023 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.432 | 0.439 | +1.5% | -0.0192 to 0.0325 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.114 | 0.116 | +1.6% | -0.00725 to 0.011 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -0.9% | -6.53 to -3.03 | GAIN |
| bytes in the cache, mean (MB) | 418 | 416 | -0.6% | -5.35 to 0.403 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 699,152 | 710,603 | +1.6% | -23,488 to 46,391 | shown, not judged |
| host CPU busy (share of the run) | 0.147 | 0.166 | +13.2% | -0.0201 to 0.0589 | EVEN, no difference beyond the noise |
| host CPU-seconds | 263 | 304 | +15.4% | -41.2 to 122 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0984 | 0.114 | +15.4% | -0.0156 to 0.0459 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,881 | 2,884 | +0.1% | -25.3 to 30 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,893 | +0.1% | -24.9 to 30.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.357 | 0.358 | +0.3% | -0.0033 to 0.0053 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.55 | 0.561 | +2.1% | -0.00483 to 0.0275 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.221 | -0.0% | -0.00294 to 0.00279 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.9 to -1.36 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -5 to 0.0894 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 674,537 | 678,826 | +0.6% | -9,120 to 17,698 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.232 | +3.0% | -0.00302 to 0.0166 | EVEN, no difference beyond the noise |
| host CPU-seconds | 383 | 398 | +3.9% | -6.9 to 37 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.289 | 0.3 | +3.8% | -0.00835 to 0.0304 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
