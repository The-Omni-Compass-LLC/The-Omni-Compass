# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% | -4.6 to 0.134 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% | -4.4 to -0.00657 | LOSS |
| latency, 95th percentile (ms) | 0.336 | 0.338 | +0.6% | -0.0174 to 0.0214 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.52 | 0.523 | +0.7% | -0.0105 to 0.0178 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.197 | +0.5% | -0.0105 to 0.0125 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -5.39 to -1.18 | GAIN |
| bytes in the cache, mean (MB) | 419 | 415 | -0.8% | -8.23 to 1.9 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 685,960 | 691,854 | +0.9% | -55,290 to 67,078 | shown, not judged |
| host CPU busy (share of the run) | 0.184 | 0.193 | +4.8% | -0.0115 to 0.0292 | EVEN, no difference beyond the noise |
| host CPU-seconds | 316 | 333 | +5.5% | -23.8 to 58.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.25 | +5.5% | -0.0178 to 0.0439 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,873 | 2,872 | -0.0% | -6.5 to 4.91 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,886 | -0.0% | -5.18 to 3.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.508 | 0.512 | +0.9% | -0.0159 to 0.0246 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.719 | 0.736 | +2.4% | -0.0368 to 0.0708 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.228 | 0.227 | -0.4% | -0.00268 to 0.00101 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -20.8 to 0.529 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 401 | 394 | -1.7% | -11.8 to -2.01 | GAIN |
| pages read into the cache (misses) | 271,757 | 275,222 | +1.3% | -50,244 to 57,174 | shown, not judged |
| host CPU busy (share of the run) | 0.21 | 0.2 | -4.6% | -0.0983 to 0.079 | EVEN, no difference beyond the noise |
| host CPU-seconds | 149 | 140 | -6.1% | -88 to 69.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.281 | 0.264 | -6.1% | -0.166 to 0.131 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.33 |  | 0.538 to 8.13 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,888 | 2,887 | -0.0% | -3.81 to 1.76 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,892 | 2,891 | -0.0% | -3.43 to 1.23 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.31 | 0.313 | +1.0% | -0.0108 to 0.0168 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.502 | 0.499 | -0.6% | -0.027 to 0.021 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.189 | 0.192 | +1.4% | -0.000366 to 0.00564 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 489 | -4.4% | -110 to 65.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 420 | 403 | -4.0% | -93.7 to 60.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,480 | 726,469 | +6.9% | -3,236 to 97,216 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.165 | -1.8% | -0.0479 to 0.0419 | EVEN, no difference beyond the noise |
| host CPU-seconds | 286 | 280 | -2.1% | -99.3 to 87.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.21 | -2.1% | -0.0747 to 0.0657 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.33 |  | 0.899 to 3.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,729 | 5,745 | +0.3% | -64.6 to 95.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,745 | 5,762 | +0.3% | -62.8 to 96.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.327 | +0.6% | -0.0023 to 0.0063 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.496 | 0.508 | +2.4% | -0.0214 to 0.0447 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.191 | 0.191 | +0.2% | -0.0164 to 0.017 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 500 | -2.3% | -45 to 21.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 416 | 409 | -1.8% | -37.7 to 22.6 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 697,996 | 700,741 | +0.4% | -19,744 to 25,234 | shown, not judged |
| host CPU busy (share of the run) | 0.245 | 0.244 | -0.6% | -0.0201 to 0.0174 | EVEN, no difference beyond the noise |
| host CPU-seconds | 443 | 439 | -0.9% | -47.8 to 39.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.167 | 0.165 | -1.3% | -0.0196 to 0.0152 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,874 | 2,876 | +0.1% | -8.67 to 13.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,885 | 2,887 | +0.1% | -9.59 to 13.4 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.373 | 0.377 | +1.0% | -0.00781 to 0.0151 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.638 | 0.639 | +0.1% | -0.00968 to 0.011 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.221 | 0.223 | +0.6% | -0.00817 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 505 | -1.3% | -20.3 to 6.65 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 413 | -0.9% | -16 to 8.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 676,658 | 689,756 | +1.9% | -3,204 to 29,399 | shown, not judged |
| host CPU busy (share of the run) | 0.246 | 0.256 | +3.8% | -0.0507 to 0.0692 | EVEN, no difference beyond the noise |
| host CPU-seconds | 431 | 449 | +4.2% | -116 to 152 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.325 | 0.338 | +4.1% | -0.0876 to 0.114 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
