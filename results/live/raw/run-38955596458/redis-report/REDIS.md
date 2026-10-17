# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,075 | -0.0% | -1.69 to 1.27 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00759 to 0.00653 | EVEN, the same |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.00036 to 0.000283 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.56 | 5.56 | -0.1% | -0.0183 to 0.0123 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.62 | 5.62 | +0.1% | -0.00716 to 0.0129 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.63 | 1.64 | +0.2% | -0.0206 to 0.0259 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.4 | -2.5% | -1.91 to -1.35 | GAIN |
| memory used, mean (MB) | 57.2 | 56.4 | -1.3% | -0.948 to -0.482 | GAIN |
| keys evicted | 71,769 | 71,782 | +0.0% | -65.5 to 90.2 | shown, not judged |
| host CPU busy (share of the run) | 0.0879 | 0.105 | +19.0% | -0.0193 to 0.0528 | EVEN, no difference beyond the noise |
| host CPU-seconds | 60.3 | 73 | +20.9% | -14.8 to 40 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.312 | 0.377 | +21.0% | -0.0759 to 0.207 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% | 19.2 to 23.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00164 to 0.0026 | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% | 0.0131 to 0.0155 | GAIN |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.3% | -0.045 to 0.016 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.0% | -0.0181 to 0.0166 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.958 | 0.883 | -7.9% | -0.0912 to -0.0599 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65 | +1.6% | 0.131 to 1.9 | power given |
| memory used, mean (MB) | 61.3 | 62 | +1.1% | -0.0734 to 1.47 | EVEN, no difference beyond the noise |
| keys evicted | 103,535 | 94,111 | -9.1% | -10,216 to -8,631 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.107 | +11.2% | 0.00367 to 0.0178 | power given |
| host CPU-seconds | 167 | 189 | +12.7% | 6.85 to 35.6 | power given |
| host CPU-seconds per 1,000 requests inside the line | 0.294 | 0.325 | +10.8% | 0.00781 to 0.0556 | power given |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 25.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925 | 937 | +1.2% | 10.4 to 12.5 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0223 to 0.00644 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.2% | 0.00671 to 0.0085 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.51 | -0.0% | -0.0323 to 0.0322 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | +0.0% | -0.0163 to 0.0172 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.15 | 2.1 | -2.0% | -0.0538 to -0.0306 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.5 | +2.4% | 1.4 to 1.62 | power given |
| memory used, mean (MB) | 60.7 | 62 | +2.1% | 1.27 to 1.3 | power given |
| keys evicted | 243,135 | 234,852 | -3.4% | -8,881 to -7,685 | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.115 | +2.8% | -0.026 to 0.0322 | EVEN, no difference beyond the noise |
| host CPU-seconds | 197 | 203 | +3.2% | -51 to 63.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.472 | 0.481 | +1.9% | -0.129 to 0.147 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 13.7 |  | 10.8 to 16.5 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 16.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.1% | 10.7 to 16.2 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0128 to 0.0172 | EVEN, no difference beyond the noise |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00795 to 0.0103 | GAIN |
| latency, 95th percentile (ms) | 5.21 | 5.21 | +0.0% | -0.0184 to 0.0185 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.24 | 5.24 | +0.1% | -0.0424 to 0.0484 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.12 | -3.8% | -0.066 to -0.0226 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.7 | +2.6% | 0.99 to 2.4 | power given |
| memory used, mean (MB) | 61.2 | 62.4 | +2.0% | 0.869 to 1.62 | power given |
| keys evicted | 138,227 | 132,886 | -3.9% | -6,120 to -4,561 | shown, not judged |
| host CPU busy (share of the run) | 0.0531 | 0.0645 | +21.5% | -0.00108 to 0.0239 | EVEN, no difference beyond the noise |
| host CPU-seconds | 93.2 | 115 | +23.0% | -1.17 to 44 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.175 | 0.213 | +21.6% | -0.00513 to 0.0808 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to the operator's ceiling: yes; another writer seen: no; fail-ups: 23.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
