# Redis: Omni-Compass on top of a cache's operator-set memory ceiling

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis as shipped with the operator's ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% | -0.92 to 0.222 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0117 to 0.0136 | EVEN, the same |
| cache hit rate | 0.717 | 0.717 | -0.0% | -0.00071 to 0.0003 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.76 | 5.77 | +0.1% | 0.000309 to 0.013 | LOSS |
| latency, 99th percentile (ms) | 5.83 | 5.85 | +0.5% | 0.0177 to 0.0351 | LOSS |
| latency, mean (ms) | 1.75 | 1.76 | +0.3% | -0.000344 to 0.0125 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 62.6 | -2.2% | -1.56 to -1.31 | GAIN |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% | -0.581 to -0.468 | GAIN |
| keys evicted | 71,805 | 71,860 | +0.1% | -76 to 186 | shown, not judged |
| host CPU busy (share of the run) | 0.15 | 0.142 | -5.4% | -0.0741 to 0.0579 | EVEN, no difference beyond the noise |
| host CPU-seconds | 102 | 94.2 | -7.2% | -60.5 to 45.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.525 | 0.487 | -7.2% | -0.312 to 0.237 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 6 |  | 6 to 6 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 6.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,278 | +0.9% | -14.9 to 37.2 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.0028 to 0.00305 | EVEN, the same |
| cache hit rate | 0.845 | 0.852 | +0.9% | -0.00974 to 0.0247 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.75 | 5.75 | -0.1% | -0.013 to 0.00685 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.82 | 5.82 | +0.1% | -0.0139 to 0.0265 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.05 | 1.01 | -3.6% | -0.134 to 0.0582 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 63.9 | -0.1% | -1.78 to 1.62 | EVEN, no difference beyond the noise |
| memory used, mean (MB) | 61.3 | 61 | -0.4% | -1.95 to 1.44 | EVEN, no difference beyond the noise |
| keys evicted | 103,421 | 98,561 | -4.7% | -16,466 to 6,746 | shown, not judged |
| host CPU busy (share of the run) | 0.143 | 0.143 | -0.5% | -0.0472 to 0.0458 | EVEN, no difference beyond the noise |
| host CPU-seconds | 244 | 243 | -0.4% | -92.4 to 90.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.428 | 0.423 | -1.3% | -0.161 to 0.15 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 22.3 |  | 19.5 to 25.2 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 26.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926 | 937 | +1.3% | 9.52 to 13.8 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.0076 to 0.00329 | EVEN, no difference beyond the noise |
| cache hit rate | 0.617 | 0.625 | +1.3% | 0.00629 to 0.00925 | GAIN |
| latency, 95th percentile (ms) | 5.51 | 5.52 | +0.1% | -0.0168 to 0.025 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | +0.1% | -0.0106 to 0.0226 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.14 | 2.1 | -1.8% | -0.0609 to -0.0169 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.4 | +2.2% | 0.926 to 1.9 | power given |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% | 0.906 to 1.43 | power given |
| keys evicted | 243,113 | 236,851 | -2.6% | -14,784 to 2,259 | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.108 | -2.6% | -0.0121 to 0.00626 | EVEN, no difference beyond the noise |
| host CPU-seconds | 193 | 187 | -3.0% | -24.3 to 12.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.463 | 0.444 | -4.2% | -0.0657 to 0.0263 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 12.7 |  | 4.68 to 20.7 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 13.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% | 11.8 to 16.4 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.00384 to -0.00149 | LOSS |
| cache hit rate | 0.789 | 0.798 | +1.2% | 0.00699 to 0.0115 | GAIN |
| latency, 95th percentile (ms) | 5.22 | 5.23 | +0.1% | -0.00318 to 0.0141 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.27 | 5.29 | +0.5% | -0.0474 to 0.0983 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.17 | 1.13 | -3.9% | -0.0537 to -0.0367 | GAIN |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64 | 65.6 | +2.5% | 1.33 to 1.86 | power given |
| memory used, mean (MB) | 61.2 | 62.3 | +1.9% | 1.03 to 1.28 | power given |
| keys evicted | 138,329 | 132,929 | -3.9% | -6,920 to -3,881 | shown, not judged |
| host CPU busy (share of the run) | 0.0641 | 0.0616 | -3.8% | -0.0529 to 0.048 | EVEN, no difference beyond the noise |
| host CPU-seconds | 113 | 108 | -3.9% | -97.9 to 89 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.212 | 0.201 | -5.1% | -0.185 to 0.163 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 21.7 |  | 18.8 to 24.5 | shown, not judged |

Every omni arm handed back to native's ceiling (64 MB): yes; another writer seen: no; fail-ups: 22.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
