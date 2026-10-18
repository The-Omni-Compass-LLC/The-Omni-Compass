# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,916 | 2,918 | +0.1% | -11 to 14.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,920 | 2,921 | +0.1% | -10.9 to 14.7 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.251 | 0.25 | -0.3% | -0.00692 to 0.00559 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.382 | 0.382 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, mean (ms) | 0.15 | 0.151 | +0.5% | -0.00427 to 0.00591 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -9.34 to 1.5 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 418 | 418 | +0.1% | -6.59 to 7.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 709,392 | 732,075 | +3.2% | -49,964 to 95,329 | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.184 | +17.8% | -0.0194 to 0.075 | EVEN, no difference beyond the noise |
| host CPU-seconds | 283 | 342 | +21.0% | -43.1 to 162 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.212 | 0.256 | +21.0% | -0.033 to 0.122 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,891 | 2,890 | -0.1% | -4.26 to 1.21 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,898 | 2,896 | -0.1% | -4.05 to -0.409 | LOSS |
| latency, 95th percentile (ms) | 0.428 | 0.427 | -0.2% | -0.0152 to 0.0139 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.587 | 0.565 | -3.7% | -0.0668 to 0.0234 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.22 | 0.221 | +0.5% | -0.0069 to 0.00928 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 501 | -2.2% | -19.3 to -3.32 | GAIN |
| bytes in the cache, mean (MB) | 401 | 395 | -1.4% | -20.3 to 8.69 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 273,008 | 271,852 | -0.4% | -43,642 to 41,330 | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.175 | +17.6% | -0.0116 to 0.0642 | EVEN, no difference beyond the noise |
| host CPU-seconds | 98.5 | 119 | +20.7% | -8.53 to 49.2 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.185 | 0.223 | +20.6% | -0.016 to 0.0924 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.67 |  | 2.23 to 5.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,917 | 2,916 | -0.1% | -7.88 to 4.43 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,921 | 2,919 | -0.1% | -7.4 to 4.33 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.237 | 0.236 | -0.3% | -0.00446 to 0.00313 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.387 | 0.386 | -0.2% | -0.0064 to 0.00507 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.155 | 0.157 | +1.3% | -0.00832 to 0.0123 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.3% | -20.3 to 7.35 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 411 | -1.4% | -24.2 to 12.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 728,397 | 700,664 | -3.8% | -232,284 to 176,816 | shown, not judged |
| host CPU busy (share of the run) | 0.137 | 0.171 | +24.9% | -0.0313 to 0.0994 | EVEN, no difference beyond the noise |
| host CPU-seconds | 242 | 315 | +30.0% | -66.3 to 212 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.181 | 0.236 | +30.0% | -0.0498 to 0.159 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3 |  | 0.516 to 5.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,699 | 5,711 | +0.2% | -116 to 139 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,716 | 5,727 | +0.2% | -117 to 139 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.325 | 0.325 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, 99th percentile (ms) | 0.504 | 0.501 | -0.6% | -0.0138 to 0.00783 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.204 | -2.6% | -0.0111 to 0.000173 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -21.8 to 1.54 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 414 | 409 | -1.3% | -11.9 to 1.48 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 692,274 | 701,426 | +1.3% | -22,885 to 41,189 | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.239 | +0.8% | -0.0326 to 0.0364 | EVEN, no difference beyond the noise |
| host CPU-seconds | 428 | 431 | +0.8% | -79.5 to 86 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.163 | +0.5% | -0.0331 to 0.0348 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% | -18.1 to 19.1 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,893 | 2,894 | +0.0% | -17.8 to 19.1 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.371 | 0.371 | -0.2% | -0.0101 to 0.00874 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.558 | 0.559 | +0.3% | -0.00837 to 0.0117 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.223 | 0.224 | +0.3% | -0.00366 to 0.00518 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -5.08 to -3.64 | GAIN |
| bytes in the cache, mean (MB) | 418 | 415 | -0.6% | -5.51 to 0.584 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 679,185 | 678,707 | -0.1% | -24,246 to 23,288 | shown, not judged |
| host CPU busy (share of the run) | 0.225 | 0.235 | +4.5% | -0.039 to 0.0592 | EVEN, no difference beyond the noise |
| host CPU-seconds | 384 | 405 | +5.5% | -85.6 to 128 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.289 | 0.305 | +5.4% | -0.0659 to 0.0972 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
