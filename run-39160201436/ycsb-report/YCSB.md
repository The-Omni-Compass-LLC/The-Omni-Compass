# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7482 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,893 | 2,894 | +0.0% | -5.16 to 6.21 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,898 | +0.0% | -4.93 to 6.24 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.338 | 0.333 | -1.4% | -0.0345 to 0.0252 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.493 | 0.49 | -0.6% | -0.0353 to 0.0293 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.197 | 0.196 | -0.8% | -0.0109 to 0.00792 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | -0.0% | -2.56 to 2.03 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,790 | 61,849 | +0.1% | -176 to 294 | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.172 | -3.7% | -0.0563 to 0.0431 | EVEN, no difference beyond the noise |
| host CPU-seconds | 304 | 291 | -4.3% | -112 to 85.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.219 | -4.3% | -0.084 to 0.0642 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,922 | 2,922 | +0.0% | -7.54 to 8.33 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,925 | 2,925 | +0.0% | -7.01 to 8.27 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.364 | 0.367 | +0.6% | -0.0185 to 0.0232 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.518 | 0.528 | +2.1% | -0.0325 to 0.0539 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.133 | 0.134 | +0.9% | -0.00659 to 0.00894 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,517 | 1,517 | -0.0% | -5.88 to 5.08 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,609 | 77,667 | +0.1% | -306 to 422 | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.104 | -15.4% | -0.143 to 0.105 | EVEN, no difference beyond the noise |
| host CPU-seconds | 90.7 | 75.5 | -16.7% | -116 to 85.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.17 | 0.142 | -16.7% | -0.217 to 0.16 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,933 | 2,934 | +0.0% | -4.87 to 7.45 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,935 | 2,936 | +0.0% | -5.14 to 7.47 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.202 | 0.201 | -0.7% | -0.0136 to 0.0109 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.348 | 0.341 | -2.0% | -0.0264 to 0.0124 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0748 | 0.0748 | -0.0% | -0.00445 to 0.00443 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,349 | -0.1% | -2.78 to 1.16 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,630 | 61,632 | +0.0% | -115 to 119 | shown, not judged |
| host CPU busy (share of the run) | 0.108 | 0.0964 | -10.3% | -0.0368 to 0.0145 | EVEN, no difference beyond the noise |
| host CPU-seconds | 199 | 176 | -11.5% | -73.8 to 28.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.148 | 0.131 | -11.5% | -0.0552 to 0.0211 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,707 | 5,708 | +0.0% | -22.3 to 23.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,720 | 5,721 | +0.0% | -23 to 24.6 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.439 | +0.4% | -0.00213 to 0.00546 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.688 | 0.688 | -0.1% | -0.00692 to 0.00559 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.247 | 0.248 | +0.2% | -0.00177 to 0.00253 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,360 | -0.0% | -4.25 to 3.01 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,991 | 62,860 | -0.2% | -559 to 297 | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.257 | +1.2% | -0.00109 to 0.00738 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 434 | +1.5% | -0.498 to 13.3 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.164 | +1.5% | -0.000226 to 0.00507 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `773cd59cfdd2`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,772 | 2,789 | +0.6% | -191 to 225 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,781 | 2,797 | +0.6% | -193 to 226 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.28 | 0.276 | -1.4% | -0.0234 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.457 | 0.452 | -1.1% | -0.0181 to 0.00815 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.222 | -2.9% | -0.0316 to 0.0185 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,337 | 1,327 | -0.7% | -108 to 89.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,527 | 61,864 | -1.1% | -7,566 to 6,240 | shown, not judged |
| host CPU busy (share of the run) | 0.178 | 0.168 | -5.5% | -0.11 to 0.0903 | EVEN, no difference beyond the noise |
| host CPU-seconds | 326 | 304 | -6.7% | -233 to 189 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.237 | -7.5% | -0.174 to 0.135 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
