# YCSB on MongoDB: Omni-Compass on top of a database's cache as shipped

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB exactly as shipped, its WiredTiger cache at the server's own default (7481 MB on this machine), is native; a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,914 | +0.1% | -2.25 to 5.37 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,915 | 2,917 | +0.1% | -1.46 to 4.69 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.208 | 0.207 | -0.6% | -0.0399 to 0.0373 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.44 | 0.444 | +0.8% | -0.0811 to 0.0884 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.11 | 0.108 | -1.8% | -0.0126 to 0.0086 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | +0.0% | -4.01 to 4.45 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,768 | 61,844 | +0.1% | -219 to 372 | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.126 | -13.0% | -0.108 to 0.0708 | EVEN, no difference beyond the noise |
| host CPU-seconds | 267 | 227 | -14.9% | -230 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.17 | -14.9% | -0.172 to 0.113 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,879 | +0.0% | -4.46 to 5.52 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,887 | 2,888 | +0.0% | -4.02 to 5.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.468 | 0.474 | +1.2% | -0.00684 to 0.0182 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.644 | 0.654 | +1.5% | -0.0178 to 0.0371 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.215 | 0.217 | +0.8% | -0.000664 to 0.00395 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,508 | +0.0% | -4.44 to 5.12 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 77,635 | 77,725 | +0.1% | -81.6 to 262 | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.203 | +20.9% | -0.0248 to 0.095 | EVEN, no difference beyond the noise |
| host CPU-seconds | 114 | 144 | +25.9% | -22.3 to 81.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.27 | +25.9% | -0.042 to 0.153 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,938 | +0.1% | -0.74 to 4.23 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,938 | 2,940 | +0.1% | -0.5 to 4.03 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.092 | 0.0923 | +0.4% | -0.00971 to 0.0104 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.301 | 0.315 | +4.8% | -0.013 to 0.0417 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0566 | 0.0571 | +0.9% | -0.000657 to 0.00164 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | -0.0% | -1.67 to 1.61 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 61,695 | 61,697 | +0.0% | -138 to 142 | shown, not judged |
| host CPU busy (share of the run) | 0.0737 | 0.0811 | +10.1% | -0.00691 to 0.0218 | EVEN, no difference beyond the noise |
| host CPU-seconds | 133 | 148 | +11.1% | -14.4 to 44 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.0992 | 0.11 | +11.1% | -0.0108 to 0.0328 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,681 | 5,682 | +0.0% | -9.3 to 12.3 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,694 | 5,695 | +0.0% | -9.9 to 13.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.414 | 0.415 | +0.1% | -0.00484 to 0.0055 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.635 | 0.641 | +0.9% | -0.0167 to 0.0281 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.236 | 0.236 | -0.1% | -0.00167 to 0.00132 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,361 | +0.0% | 0.326 to 1 | power given |
| pages read into the cache (misses) | 62,753 | 62,987 | +0.4% | -476 to 945 | shown, not judged |
| host CPU busy (share of the run) | 0.297 | 0.299 | +0.9% | -0.0175 to 0.0225 | EVEN, no difference beyond the noise |
| host CPU-seconds | 532 | 539 | +1.4% | -45.5 to 59.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.203 | +1.3% | -0.0172 to 0.0225 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% | -3.77 to 2.5 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% | -3.8 to 2.86 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.324 | 0.325 | +0.4% | -0.017 to 0.0196 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.474 | 0.474 | -0.1% | -0.0145 to 0.0138 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.192 | 0.192 | +0.3% | -0.0024 to 0.00353 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% | 0 to 0 | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% | -1.49 to 2.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 62,971 | 63,263 | +0.5% | -1,115 to 1,698 | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.216 | -5.1% | -0.119 to 0.0957 | EVEN, no difference beyond the noise |
| host CPU-seconds | 410 | 384 | -6.3% | -275 to 223 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.288 | -6.3% | -0.206 to 0.168 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
