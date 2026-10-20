# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,913 | -0.0% | -4.2 to 1.56 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,918 | 2,916 | -0.0% | -4.22 to 1.47 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.268 | 0.267 | -0.4% | -0.0124 to 0.0104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.434 | -1.5% | -0.0241 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.119 | 0.119 | +0.0% | -0.00688 to 0.00698 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.7% | -6.27 to -0.716 | GAIN |
| bytes in the cache, mean (MB) | 416 | 415 | -0.4% | -12.7 to 9.26 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 701,051 | 711,588 | +1.5% | -169,692 to 190,766 | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.146 | +5.8% | -0.0698 to 0.0858 | EVEN, no difference beyond the noise |
| host CPU-seconds | 250 | 266 | +6.6% | -146 to 179 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.2 | +6.6% | -0.11 to 0.134 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,899 | +0.0% | -7.67 to 8.12 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,905 | 2,906 | +0.0% | -5.37 to 6.95 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.426 | 0.432 | +1.4% | -0.0362 to 0.0482 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.622 | 0.634 | +1.9% | -0.036 to 0.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.162 | 0.163 | +0.8% | -0.0114 to 0.014 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 497 | -3.0% | -19.5 to -10.9 | GAIN |
| bytes in the cache, mean (MB) | 406 | 393 | -3.2% | -21.9 to -4.48 | GAIN |
| pages read into the cache (misses) | 261,304 | 276,274 | +5.7% | -44,044 to 73,983 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.191 | +10.1% | -0.0124 to 0.0474 | EVEN, no difference beyond the noise |
| host CPU-seconds | 127 | 143 | +12.4% | -8.8 to 40.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.268 | +12.3% | -0.0173 to 0.076 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 1.46 to 7.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,896 | -0.1% | -5.14 to 0.0287 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% | -4.72 to 0.101 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.306 | 0.306 | +0.1% | -0.00346 to 0.00413 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.492 | 0.495 | +0.5% | -0.00113 to 0.00646 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.194 | 0.193 | -0.4% | -0.00599 to 0.00444 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.89 to -1.06 | GAIN |
| bytes in the cache, mean (MB) | 421 | 419 | -0.5% | -16.8 to 12.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 721,537 | 691,339 | -4.2% | -108,748 to 48,353 | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.198 | +12.5% | -0.0137 to 0.0577 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 351 | +15.6% | -31.4 to 126 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.228 | 0.263 | +15.6% | -0.0237 to 0.0947 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | -0.128 to 7.46 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,698 | 5,697 | -0.0% | -17.5 to 15.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,714 | 5,713 | -0.0% | -17.1 to 16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.435 | 0.436 | +0.3% | -0.0252 to 0.0279 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.643 | 0.644 | +0.1% | -0.0216 to 0.0229 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.253 | 0.254 | +0.4% | -0.0164 to 0.0184 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -21.5 to 0.543 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 410 | -1.8% | -16.8 to 2.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,956 | 691,489 | +2.0% | -6,298 to 33,363 | shown, not judged |
| host CPU busy (share of the run) | 0.277 | 0.288 | +3.8% | 0.00475 to 0.0163 | power given |
| host CPU-seconds | 467 | 491 | +5.0% | 6.32 to 40.7 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.185 | +5.0% | 0.00283 to 0.0147 | power given |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,930 | 2,928 | -0.1% | -3.76 to 0.075 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,936 | 2,935 | -0.1% | -3.63 to 0.157 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.234 | 0.235 | +0.7% | -0.019 to 0.0224 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.397 | 0.403 | +1.6% | -0.0361 to 0.0488 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.103 | 0.103 | +0.0% | -0.00476 to 0.00477 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.7% | -8.89 to 1.22 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 417 | -0.6% | -5.4 to 0.0944 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,142 | 698,977 | +0.4% | -20,581 to 26,251 | shown, not judged |
| host CPU busy (share of the run) | 0.133 | 0.144 | +8.3% | -0.0964 to 0.118 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 266 | +9.7% | -202 to 249 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.199 | +9.7% | -0.151 to 0.186 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
