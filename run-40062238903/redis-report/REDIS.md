# Redis: Omni-Compass on top of a cache's memory as shipped (no ceiling)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line (a hit is inside, a miss and its 5 ms store trip outside). The same requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, losses included.

## burst: 8192 B values, working set 2,500 keys × notch, steps 1 6 1 8 1 6 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% | -0.0807 to 0.0665 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00687 to 0.00755 | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | +0.0% | -2.84e-06 to 7.78e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.63 | 5.63 | +0.1% | -0.00687 to 0.0164 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% | -0.00929 to 0.0252 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.771 | 0.772 | +0.2% | -0.005 to 0.00775 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 200 | 200 | +0.0% | 0.0201 to 0.0531 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.121 | +11.2% | -0.0272 to 0.0517 | EVEN, no difference beyond the noise |
| host CPU-seconds | 77.2 | 86.7 | +12.2% | -20 to 38.9 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.323 | 0.363 | +12.2% | -0.0839 to 0.163 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## large: 32768 B values, working set 625 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,470 | 1,471 | +0.0% | 0.185 to 0.653 | GAIN |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.00573 to 0.00644 | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% | -6.35e-06 to 6.36e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 0.157 | 0.158 | +0.7% | -0.000929 to 0.00301 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.45 | 5.45 | +0.0% | -0.00225 to 0.00647 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.229 | 0.228 | -0.3% | -0.0029 to 0.00154 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 348 | 348 | +0.0% | 0.00199 to 0.0547 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0751 | 0.0904 | +20.4% | -0.0216 to 0.0523 | EVEN, no difference beyond the noise |
| host CPU-seconds | 130 | 160 | +22.8% | -41.7 to 101 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.197 | 0.242 | +22.8% | -0.0631 to 0.153 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## small: 2048 B values, working set 10,000 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% | -0.0935 to 0.0633 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% | -0.023 to 0.0113 | EVEN, no difference beyond the noise |
| cache hit rate | 0.782 | 0.782 | -0.0% | -5.81e-06 to 3.62e-06 | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% | -0.0176 to 0.0173 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% | -0.0125 to 0.00956 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.36 | 1.37 | +0.1% | -0.00925 to 0.012 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 257 | 257 | +0.0% | 0.03 to 0.0471 | power given |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.122 | +2.6% | -0.0494 to 0.0557 | EVEN, no difference beyond the noise |
| host CPU-seconds | 200 | 206 | +2.9% | -93.7 to 105 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.379 | 0.39 | +2.9% | -0.177 to 0.2 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

## tuning: 8192 B values, working set 2,500 keys × notch, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s (the tuning workload)

Redis 7.0.15; 1500 requests a second offered; 3 paired repetitions; engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `bbf7e12f0467`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% | -0.507 to 0.424 | EVEN, no difference beyond the noise |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% | -0.000889 to 0.0024 | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% | -5.13e-06 to 6.12e-06 | EVEN, the same |
| latency, 95th percentile (ms) | 5.42 | 5.42 | +0.0% | -0.0235 to 0.0271 | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.58 | 5.58 | +0.0% | -0.0071 to 0.00851 | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.501 | 0.501 | +0.1% | -0.0021 to 0.00291 | EVEN, no difference beyond the noise |
| failed requests | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 |  | 0 to 0 | EVEN, the same |
| memory used, mean (MB) | 333 | 333 | +0.0% | -0.00861 to 0.0619 | EVEN, no difference beyond the noise |
| keys evicted | 0 | 0 |  | 0 to 0 | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.0981 | +2.3% | -0.0137 to 0.0182 | EVEN, no difference beyond the noise |
| host CPU-seconds | 170 | 174 | +2.5% | -26.8 to 35.4 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 requests inside the line | 0.271 | 0.278 | +2.5% | -0.0428 to 0.0564 | EVEN, no difference beyond the noise |
| ceiling changes written (the knob's moves) | 0 | 0 |  | 0 to 0 | shown, not judged |

Every omni arm handed back to native's ceiling (none MB): yes; another writer seen: no; fail-ups: 0.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
