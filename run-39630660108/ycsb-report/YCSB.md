# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2048] MB, holding the server's own read latency at 40% of the 1 ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## b: YCSB workloadb, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,941 | 2,938 | -0.1% | -6.25 to 0.64 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,943 | 2,940 | -0.1% | -3.77 to -0.777 | LOSS |
| latency, 95th percentile (ms) | 0.125 | 0.133 | +6.7% | -0.0333 to 0.05 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.321 | 0.342 | +6.5% | -0.056 to 0.098 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0634 | 0.0656 | +3.4% | -0.00724 to 0.0115 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -4.34 to -1.29 | GAIN |
| bytes in the cache, mean (MB) | 417 | 419 | +0.5% | -9.82 to 13.8 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 691,617 | 741,790 | +7.3% | 4,414 to 95,932 | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0833 | -19.0% | -0.0559 to 0.0167 | EVEN, no difference beyond the noise |
| host CPU-seconds | 190 | 151 | -20.8% | -112 to 33.1 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.142 | 0.112 | -20.8% | -0.0836 to 0.0247 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 2 |  | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## burst: YCSB workloadb, 250,000 records × notch, steps 1 6 1 8 1 6 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,810 | 2,828 | +0.6% | -71.4 to 107 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,824 | 2,842 | +0.6% | -73.7 to 110 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.304 | 0.308 | +1.1% | -0.0128 to 0.0195 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.5 | 0.508 | +1.7% | -0.0199 to 0.0372 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.196 | 0.189 | -3.5% | -0.0247 to 0.0109 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 492 | -3.8% | -58.1 to 18.9 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 397 | 384 | -3.4% | -32.9 to 5.76 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 251,330 | 261,227 | +3.9% | -65,310 to 85,103 | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.16 | +13.9% | -0.0628 to 0.102 | EVEN, no difference beyond the noise |
| host CPU-seconds | 99.9 | 116 | +16.2% | -55.5 to 87.8 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.192 | 0.223 | +15.8% | -0.104 to 0.165 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 5 |  | 2.52 to 7.48 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## c: YCSB workloadc, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,887 | 2,886 | -0.0% | -4.56 to 2.61 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 2,891 | 2,890 | -0.0% | -4.26 to 2.16 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.318 | 0.318 | +0.1% | -0.0011 to 0.00177 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.494 | 0.489 | -1.0% | -0.00748 to -0.00252 | GAIN |
| latency, mean (ms) | 0.193 | 0.19 | -1.5% | -0.00883 to 0.0032 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 509 | -0.5% | -5.38 to 0.196 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 419 | 414 | -1.1% | -14.6 to 5.46 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 690,904 | 707,275 | +2.4% | -102,225 to 134,968 | shown, not judged |
| host CPU busy (share of the run) | 0.208 | 0.172 | -17.6% | -0.0797 to 0.0065 | EVEN, no difference beyond the noise |
| host CPU-seconds | 371 | 294 | -20.7% | -152 to -1.58 | GAIN |
| host CPU-seconds per 1,000 operations inside the line | 0.279 | 0.221 | -20.7% | -0.114 to -0.00125 | GAIN |
| cache size changes written (the knob's moves) | 0 | 2.67 |  | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## f: YCSB workloadf, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,691 | 5,687 | -0.1% | -61.1 to 52.9 | EVEN, no difference beyond the noise |
| throughput (operations a second) | 5,708 | 5,704 | -0.1% | -61.3 to 52.2 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 0.422 | 0.427 | +1.3% | 0.00423 to 0.0071 | LOSS |
| latency, 99th percentile (ms) | 0.646 | 0.646 | -0.1% | -0.00659 to 0.00592 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.242 | 0.246 | +1.4% | -0.00166 to 0.00839 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 506 | -1.2% | -21.1 to 9.02 | EVEN, no difference beyond the noise |
| bytes in the cache, mean (MB) | 417 | 413 | -1.0% | -14.3 to 6.33 | EVEN, no difference beyond the noise |
| pages read into the cache (misses) | 684,628 | 691,955 | +1.1% | -22,536 to 37,189 | shown, not judged |
| host CPU busy (share of the run) | 0.323 | 0.328 | +1.3% | -0.0134 to 0.0216 | EVEN, no difference beyond the noise |
| host CPU-seconds | 586 | 593 | +1.2% | -40.2 to 53.7 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.223 | +1.1% | -0.0174 to 0.0225 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4.67 |  | 3.23 to 6.1 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

## tuning: YCSB workloada, 250,000 records × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; 3 paired repetitions; engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,935 | 2,933 | -0.1% | -3.43 to -0.584 | LOSS |
| throughput (operations a second) | 2,939 | 2,937 | -0.1% | -2.69 to -1.21 | LOSS |
| latency, 95th percentile (ms) | 0.153 | 0.158 | +2.8% | -0.0294 to 0.0381 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.367 | 0.37 | +0.7% | -0.0547 to 0.06 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.0789 | 0.0787 | -0.2% | -0.00474 to 0.00437 | EVEN, no difference beyond the noise |
| failed operations | 0 | 0 |  | 0 to 0 | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512 | 508 | -0.9% | -6.01 to -2.79 | GAIN |
| bytes in the cache, mean (MB) | 419 | 417 | -0.4% | -2.98 to -0.708 | GAIN |
| pages read into the cache (misses) | 687,277 | 690,320 | +0.4% | -29,545 to 35,631 | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.104 | -14.5% | -0.0416 to 0.00621 | EVEN, no difference beyond the noise |
| host CPU-seconds | 223 | 187 | -16.2% | -85.6 to 13.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 operations inside the line | 0.166 | 0.139 | -16.2% | -0.0639 to 0.0101 | EVEN, no difference beyond the noise |
| cache size changes written (the knob's moves) | 0 | 4 |  | 4 to 4 | shown, not judged |

Every omni arm handed back to the operator's cache size: yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
