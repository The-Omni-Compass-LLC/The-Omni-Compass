# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,913 | 2,910 | -0.1% | -7.53 to 1.62 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,917 | 2,914 | -0.1% | -6.62 to 1.23 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.204 | 0.206 | +1.1% | -0.0104 to 0.0151 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.39 | 0.392 | +0.7% | -0.016 to 0.0213 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.141 | 0.144 | +1.6% | -0.00633 to 0.011 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 488 | -4.7% | -106 to 58.2 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 401 | -4.6% | -89.8 to 51.4 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 748,011 | 732,717 | -2.0% | -263,333 to 232,745 | shown, not judged |
| host CPU busy (share of the run) | 0.166 | 0.169 | +2.1% | -0.107 to 0.114 | EVEN, no difference beyond the noise |
| host CPU-seconds | 305 | 309 | +1.1% | -245 to 251 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.229 | 0.231 | +1.1% | -0.183 to 0.188 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,938 | -0.0% | -2.2 to 0.335 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,941 | 2,941 | -0.0% | -2.01 to 0.321 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.251 | 0.251 | -0.1% | -0.0248 to 0.0242 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.396 | 0.391 | -1.4% | -0.0256 to 0.0143 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0785 | 0.0774 | -1.4% | -0.00517 to 0.00293 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.1% | -19.9 to -1.81 | GAIN |
| bytes in the cache, mean (MB) | 406 | 400 | -1.5% | -23.8 to 11.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 264,661 | 269,322 | +1.8% | -19,403 to 28,724 | shown, not judged |
| host CPU busy (share of the run) | 0.0666 | 0.0753 | +13.0% | -0.0783 to 0.0957 | EVEN, no difference beyond the noise |
| host CPU-seconds | 47.3 | 54.2 | +14.5% | -59.7 to 73.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0884 | 0.101 | +14.5% | -0.111 to 0.137 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,890 | 2,888 | -0.1% | -1.89 to -1.12 | LOSS |
| throughput (operations a second) | 2,893 | 2,892 | -0.1% | -1.93 to -1.07 | LOSS |
| latency, 95th percentile (ms) | 0.3 | 0.3 | +0.0% | -0.00248 to 0.00248 | EVEN, the same |
| latency, 99th percentile (ms) | 0.506 | 0.504 | -0.3% | -0.012 to 0.00868 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.188 | 0.188 | -0.1% | -0.00749 to 0.00719 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -8.94 to 0.234 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 419 | +0.3% | -11.8 to 14.1 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 710,904 | 691,550 | -2.7% | -161,196 to 122,488 | shown, not judged |
| host CPU busy (share of the run) | 0.194 | 0.16 | -17.6% | -0.153 to 0.0847 | EVEN, no difference beyond the noise |
| host CPU-seconds | 344 | 272 | -21.0% | -322 to 177 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.258 | 0.204 | -21.0% | -0.241 to 0.133 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,670 | 5,674 | +0.1% | -73.2 to 81.6 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,689 | 5,693 | +0.1% | -70.1 to 77.8 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.443 | 0.445 | +0.5% | -0.0113 to 0.016 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.707 | 0.708 | +0.1% | -0.0253 to 0.0273 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.246 | 0.247 | +0.5% | -0.00855 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -4.55 to -3.51 | GAIN |
| bytes in the cache, mean (MB) | 416 | 414 | -0.5% | -4.07 to -0.405 | GAIN |
| pages read into the cache (misses) | 679,496 | 688,618 | +1.3% | -15,191 to 33,435 | shown, not judged |
| host CPU busy (share of the run) | 0.324 | 0.324 | -0.0% | -0.024 to 0.0237 | EVEN, no difference beyond the noise |
| host CPU-seconds | 586 | 584 | -0.4% | -59.7 to 54.5 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.222 | 0.22 | -0.6% | -0.0261 to 0.0232 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,934 | -0.0% | -6.89 to 4.41 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,938 | -0.0% | -5.74 to 3.21 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.154 | 0.16 | +4.3% | -0.00559 to 0.0189 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.364 | 0.372 | +2.3% | -0.00392 to 0.0206 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0795 | 0.0791 | -0.5% | -0.00301 to 0.00219 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -14.7 to 2.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 416 | -0.7% | -10.1 to 4.55 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 683,443 | 696,048 | +1.8% | -19,843 to 45,053 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.101 | -9.8% | -0.0772 to 0.0554 | EVEN, no difference beyond the noise |
| host CPU-seconds | 202 | 180 | -10.7% | -154 to 111 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.151 | 0.135 | -10.8% | -0.115 to 0.0829 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
