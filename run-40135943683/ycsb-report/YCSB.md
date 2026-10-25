# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,883 | 2,882 | -0.0% | -5.74 to 3.71 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,890 | 2,889 | -0.0% | -5.08 to 3.19 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.342 | 0.341 | -0.4% | -0.0173 to 0.0146 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.591 | 0.588 | -0.5% | -0.0168 to 0.0108 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.201 | +0.0% | -0.00344 to 0.00362 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.6% | -7.61 to 1.13 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 415 | -0.4% | -7.32 to 3.88 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 715,036 | 706,228 | -1.2% | -63,308 to 45,694 | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.205 | +18.3% | -0.0293 to 0.0926 | EVEN, no difference beyond the noise |
| host CPU-seconds | 292 | 359 | +22.9% | -63.3 to 197 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.22 | 0.27 | +22.9% | -0.0477 to 0.148 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 0.465 to 6.2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,882 | 2,882 | -0.0% | -3.45 to 2.62 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -4.04 to 2.66 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.437 | 0.435 | -0.5% | -0.0235 to 0.0188 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.591 | 0.591 | +0.0% | -0.024 to 0.024 | EVEN, the same |
| latency, mean (ms) | 0.218 | 0.216 | -1.0% | -0.013 to 0.00872 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 502 | -2.0% | -22.6 to 2.26 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 400 | 394 | -1.3% | -16.9 to 6.53 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 263,402 | 272,507 | +3.5% | -20,209 to 38,418 | shown, not judged |
| host CPU busy (share of the run) | 0.187 | 0.198 | +6.2% | -0.0279 to 0.0509 | EVEN, no difference beyond the noise |
| host CPU-seconds | 129 | 138 | +7.4% | -21.8 to 41 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.242 | 0.26 | +7.4% | -0.0411 to 0.0771 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 1.8 to 7.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,885 | -0.0% | -2.39 to 1.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,889 | 2,889 | -0.0% | -2.53 to 1.94 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.315 | 0.315 | -0.2% | -0.00826 to 0.00692 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.494 | -0.1% | -0.00906 to 0.00839 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.193 | 0.192 | -0.7% | -0.00879 to 0.00615 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 486 | -5.1% | -110 to 57.8 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 421 | 401 | -4.8% | -99.7 to 59.2 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 690,477 | 722,378 | +4.6% | -179,482 to 243,284 | shown, not judged |
| host CPU busy (share of the run) | 0.199 | 0.195 | -2.0% | -0.0774 to 0.0696 | EVEN, no difference beyond the noise |
| host CPU-seconds | 350 | 340 | -2.6% | -169 to 151 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.263 | 0.256 | -2.7% | -0.127 to 0.113 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 3.33 |  | 1.9 to 4.77 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,684 | 5,686 | +0.0% | -27.8 to 31.2 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,701 | 5,703 | +0.0% | -29.1 to 32.3 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.428 | 0.428 | +0.0% | -0.0043 to 0.0043 | EVEN, the same |
| latency, 99th percentile (ms) | 0.656 | 0.654 | -0.3% | -0.0134 to 0.00938 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.245 | 0.245 | +0.2% | -0.00132 to 0.00252 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -3.7 to -1.71 | GAIN |
| bytes in the cache, mean (MB) | 417 | 415 | -0.5% | -2.35 to -1.53 | GAIN |
| pages read into the cache (misses) | 679,750 | 684,928 | +0.8% | -11,761 to 22,116 | shown, not judged |
| host CPU busy (share of the run) | 0.317 | 0.324 | +2.2% | 0.000747 to 0.0129 | power given |
| host CPU-seconds | 568 | 585 | +3.0% | 7.02 to 27.5 | power given |
| host CPU-seconds per 1,000 operations inside the line | 0.214 | 0.22 | +2.9% | 0.00133 to 0.0111 | power given |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,935 | -0.1% | -5.04 to 0.523 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,942 | 2,939 | -0.1% | -5.59 to 0.687 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.128 | 0.134 | +4.4% | -0.0112 to 0.0226 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.354 | 0.364 | +2.7% | -0.0379 to 0.0572 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0761 | 0.0766 | +0.7% | -0.00573 to 0.00677 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 507 | -1.0% | -5.51 to -4.32 | GAIN |
| bytes in the cache, mean (MB) | 420 | 418 | -0.6% | -3.41 to -1.75 | GAIN |
| pages read into the cache (misses) | 680,968 | 682,634 | +0.2% | -16,747 to 20,078 | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.106 | -6.7% | -0.0798 to 0.0645 | EVEN, no difference beyond the noise |
| host CPU-seconds | 207 | 190 | -7.8% | -164 to 132 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.154 | 0.142 | -7.8% | -0.123 to 0.0987 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
