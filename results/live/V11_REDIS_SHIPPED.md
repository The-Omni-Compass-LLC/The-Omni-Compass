# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150490855 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39159008310 | `3cb376bb3284` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39167582853 | `e2d5958834f5` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,392 | -0.1% (-0.4 to +0.3) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.929 | 0.929 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.52 | 5.55 | +0.5% (-1.6 to +2.5) | -0.1% (-0.2 to +0.1) | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.69 | 5.8 | +2.0% (-6.4 to +10.3) | +0.0% (-0.1 to +0.1) | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.514 | 0.539 | +4.9% (-14.3 to +24.1) | +0.2% (-0.0 to +0.4) | -0.2% (-1.0 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 333.1 | 333.1 | +0.0% (-0.0 to +0.1) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0897 | 0.107 | +19.0% (-45.7 to +83.7) | -13.6% (-32.8 to +5.5) | +9.2% (-10.7 to +29.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 157.9 | 190.2 | +20.5% (-51.3 to +92.3) | -15.2% (-36.8 to +6.5) | +10.2% (-11.3 to +31.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.252 | 0.304 | +20.6% (-51.2 to +92.4) | -15.2% (-36.8 to +6.5) | +10.1% (-11.3 to +31.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.885 | 0.885 | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.71 | 5.71 | +0.1% (-0.1 to +0.2) | -0.1% (-0.5 to +0.2) | +0.1% (-0.3 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.77 | 5.77 | +0.1% (-0.0 to +0.2) | -0.2% (-0.7 to +0.3) | +0.2% (-0.3 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.809 | 0.81 | +0.1% (-0.9 to +1.0) | -0.2% (-1.0 to +0.7) | +0.4% (-1.3 to +2.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 199.9 | 199.9 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0993 | 0.0949 | -4.4% (-43.0 to +34.1) | +14.8% (-28.8 to +58.4) | -9.0% (-72.7 to +54.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 66.4 | 63.4 | -4.6% (-47.0 to +37.9) | +17.2% (-32.5 to +67.0) | -9.9% (-79.3 to +59.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.278 | 0.265 | -4.6% (-47.0 to +37.9) | +17.2% (-32.5 to +67.0) | -9.9% (-79.3 to +59.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.981 | 0.981 | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.159 | 0.168 | +5.1% (-6.4 to +16.6) | -1.2% (-3.3 to +0.9) | -3.7% (-16.0 to +8.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.42 | 5.46 | +0.8% (-1.6 to +3.1) | -0.1% (-0.4 to +0.2) | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.214 | 0.218 | +1.9% (-2.9 to +6.6) | -0.5% (-3.0 to +2.0) | +0.1% (-2.7 to +2.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 348.4 | 348.4 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0768 | 0.078 | +1.5% (-20.6 to +23.6) | -6.5% (-52.0 to +39.0) | +51.0% (-20.7 to +122.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 136.2 | 137.9 | +1.2% (-21.9 to +24.3) | -6.8% (-56.9 to +43.2) | +55.3% (-22.6 to +133.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.206 | 0.208 | +1.2% (-21.9 to +24.3) | -6.8% (-56.9 to +43.3) | +55.3% (-22.6 to +133.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,174 | 1,174 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.783 | 0.783 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.54 | 5.55 | +0.2% (-0.8 to +1.2) | -0.1% (-0.4 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.63 | 5.64 | +0.2% (-0.7 to +1.1) | -0.0% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.29 | 1.29 | +0.4% (-0.9 to +1.7) | -0.1% (-0.5 to +0.3) | +0.0% (-0.4 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 257.3 | 257.3 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given in all three of our runs** |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.111 | 0.109 | -1.5% (-32.6 to +29.5) | -1.4% (-14.8 to +12.1) | +0.6% (-36.5 to +37.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 198.5 | 194.6 | -2.0% (-36.1 to +32.1) | -1.5% (-16.9 to +13.9) | +0.5% (-41.6 to +42.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.368 | -2.0% (-36.1 to +32.1) | -1.5% (-16.9 to +13.9) | +0.5% (-41.6 to +42.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 1 power given, 35 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
