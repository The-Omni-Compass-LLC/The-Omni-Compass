# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,925 | 2,923 | -0.1% | -3.52 to -0.611 | LOSS |
| throughput (operations a second) | 2,928 | 2,926 | -0.1% | -3.24 to -0.836 | LOSS |
| latency, 95th percentile (ms) | 0.244 | 0.248 | +1.6% | -0.00738 to 0.0154 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.431 | 0.433 | +0.3% | -0.017 to 0.0196 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.126 | 0.127 | +1.2% | -0.00376 to 0.00688 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 510 | -0.4% | -2.82 to -1.76 | GAIN |
| bytes in the cache, mean (MB) | 419 | 420 | +0.3% | -4.03 to 6.28 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 700,229 | 741,772 | +5.9% | 6,308 to 76,778 | shown, not judged |
| host CPU busy (share of the run) | 0.121 | 0.133 | +10.2% | -0.133 to 0.157 | EVEN, no difference beyond the noise |
| host CPU-seconds | 216 | 240 | +11.3% | -272 to 321 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.162 | 0.18 | +11.3% | -0.203 to 0.24 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | -0.0% | -3.69 to 2.87 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,888 | 2,888 | -0.0% | -3.58 to 3.21 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.421 | 0.422 | +0.3% | -0.00384 to 0.0065 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.571 | 0.57 | -0.1% | -0.0344 to 0.0331 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.21 | 0.214 | +1.9% | -0.00503 to 0.013 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 499 | -2.6% | -26.2 to -0.331 | GAIN |
| bytes in the cache, mean (MB) | 400 | 394 | -1.6% | -20.2 to 7.5 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 272,631 | 273,811 | +0.4% | -12,024 to 14,384 | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.232 | +12.6% | -0.102 to 0.154 | EVEN, no difference beyond the noise |
| host CPU-seconds | 147 | 169 | +15.3% | -93.9 to 139 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.276 | 0.318 | +15.3% | -0.177 to 0.261 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,908 | +0.1% | -12 to 16.7 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,911 | 2,912 | +0.1% | -9.4 to 12.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.188 | 0.187 | -0.7% | -0.0065 to 0.00384 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.357 | 0.357 | -0.1% | -0.0126 to 0.0119 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.146 | 0.141 | -3.8% | -0.0194 to 0.00835 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -9.07 to 2.93 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 416 | -0.6% | -12.7 to 7.79 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 714,025 | 675,732 | -5.4% | -140,308 to 63,722 | shown, not judged |
| host CPU busy (share of the run) | 0.144 | 0.156 | +8.0% | -0.0498 to 0.0729 | EVEN, no difference beyond the noise |
| host CPU-seconds | 258 | 282 | +9.2% | -103 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.194 | 0.211 | +9.1% | -0.0772 to 0.112 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,736 | 5,733 | -0.1% | -31.5 to 25 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,751 | 5,748 | -0.1% | -30.2 to 24.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.377 | 0.375 | -0.4% | -0.0065 to 0.00384 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.595 | 0.596 | +0.2% | -0.00557 to 0.00757 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.204 | 0.203 | -0.3% | -0.00491 to 0.00382 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.8% | -6.77 to -1.62 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -3.93 to -0.0723 | GAIN |
| pages read into the cache (misses) | 688,625 | 692,655 | +0.6% | -35,761 to 43,820 | shown, not judged |
| host CPU busy (share of the run) | 0.273 | 0.276 | +1.2% | -0.0452 to 0.0517 | EVEN, no difference beyond the noise |
| host CPU-seconds | 496 | 504 | +1.6% | -111 to 126 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.19 | +1.6% | -0.0409 to 0.0468 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,931 | -0.1% | -12.9 to 8.48 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,939 | 2,936 | -0.1% | -12.4 to 7.07 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.162 | 0.163 | +0.2% | -0.0751 to 0.0757 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.396 | 0.391 | -1.3% | -0.103 to 0.0924 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0819 | 0.0823 | +0.5% | -0.0143 to 0.0152 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -6.31 to -3.8 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.6% | -4 to -0.926 | GAIN |
| pages read into the cache (misses) | 690,618 | 693,348 | +0.4% | -13,472 to 18,933 | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.107 | -9.1% | -0.05 to 0.0286 | EVEN, no difference beyond the noise |
| host CPU-seconds | 215 | 192 | -10.5% | -103 to 58 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.161 | 0.144 | -10.5% | -0.077 to 0.0432 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
