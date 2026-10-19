# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,895 | -0.0% | -2.84 to 0.0789 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,901 | 2,900 | -0.0% | -3.16 to 0.281 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.318 | -0.2% | -0.00826 to 0.00692 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.495 | 0.492 | -0.5% | -0.00554 to 0.000202 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.2 | 0.198 | -0.9% | -0.00875 to 0.00501 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.92 to -1.7 | GAIN |
| bytes in the cache, mean (MB) | 419 | 414 | -1.4% | -16.4 to 4.99 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 686,945 | 698,947 | +1.7% | -79,662 to 103,666 | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.184 | +9.8% | -0.0656 to 0.0983 | EVEN, no difference beyond the noise |
| host CPU-seconds | 282 | 316 | +11.9% | -137 to 204 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.237 | +11.9% | -0.103 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% | -8.29 to 5.24 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,896 | 2,895 | -0.0% | -4.65 to 2.52 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.506 | 0.505 | -0.1% | -0.0107 to 0.00937 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.675 | 0.675 | +0.0% | -0.0237 to 0.0237 | EVEN, the same |
| latency, mean (ms) | 0.231 | 0.231 | -0.2% | -0.0118 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 470 | -8.1% | -51.3 to -31.8 | GAIN |
| bytes in the cache, mean (MB) | 400 | 369 | -7.9% | -38.9 to -24.3 | GAIN |
| pages read into the cache (misses) | 268,519 | 275,012 | +2.4% | 316 to 12,670 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.211 | +17.4% | -0.0273 to 0.0896 | EVEN, no difference beyond the noise |
| host CPU-seconds | 123 | 149 | +21.4% | -20.5 to 73.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.281 | +21.5% | -0.0383 to 0.138 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 5 to 5 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,894 | 2,892 | -0.1% | -2.48 to -1.29 | LOSS |
| throughput (operations a second) | 2,899 | 2,897 | -0.1% | -3.39 to -0.465 | LOSS |
| latency, 95th percentile (ms) | 0.315 | 0.313 | -0.4% | -0.00707 to 0.0044 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.568 | 0.563 | -0.8% | -0.0106 to 0.00192 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.202 | 0.201 | -0.2% | -0.00505 to 0.00419 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.2% | -105 to 52.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 400 | -4.8% | -91.5 to 51.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 696,286 | 706,566 | +1.5% | -138,711 to 159,271 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.174 | -10.4% | -0.169 to 0.129 | EVEN, no difference beyond the noise |
| host CPU-seconds | 339 | 298 | -12.2% | -344 to 261 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.255 | 0.224 | -12.2% | -0.258 to 0.196 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 0.798 to 6.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,727 | 5,601 | -2.2% | -401 to 151 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,742 | 5,618 | -2.2% | -404 to 155 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.328 | +0.8% | -0.00492 to 0.0103 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.497 | 0.502 | +0.9% | -0.0126 to 0.0212 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.206 | 0.211 | +2.7% | -0.0168 to 0.0281 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -4.82 to -1.82 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.7% | -5.27 to -0.543 | GAIN |
| pages read into the cache (misses) | 692,284 | 686,082 | -0.9% | -16,431 to 4,026 | shown, not judged |
| host CPU busy (share of the run) | 0.234 | 0.243 | +3.5% | -0.0194 to 0.0357 | EVEN, no difference beyond the noise |
| host CPU-seconds | 422 | 442 | +4.8% | -43.5 to 84.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.159 | 0.171 | +7.0% | -0.00766 to 0.03 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,875 | 2,876 | +0.0% | -20.1 to 22.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,886 | 2,888 | +0.0% | -18.6 to 21.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.388 | 0.384 | -1.1% | -0.0223 to 0.0136 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.648 | 0.643 | -0.8% | -0.0327 to 0.0227 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.23 | 0.227 | -1.2% | -0.0101 to 0.00454 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -21.5 to 8.43 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 413 | -1.1% | -15.8 to 6.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 677,616 | 677,387 | -0.0% | -20,265 to 19,807 | shown, not judged |
| host CPU busy (share of the run) | 0.243 | 0.235 | -3.5% | -0.0235 to 0.00672 | EVEN, no difference beyond the noise |
| host CPU-seconds | 421 | 403 | -4.2% | -48.1 to 12.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.318 | 0.304 | -4.3% | -0.0379 to 0.0106 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 2.9 to 5.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
