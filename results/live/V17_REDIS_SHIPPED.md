# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005925354 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40024478954 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40038802348 | `d02c7052ae50` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,391 | 1,392 | +0.1% (-0.0 to +0.1) | -0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.929 | 0.929 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| latency, 95th percentile (ms) | 5.61 | 5.61 | +0.0% (-0.3 to +0.4) | -0.2% (-0.9 to +0.5) | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.7 | 5.7 | +0.0% (-0.2 to +0.2) | -0.0% (-0.3 to +0.3) | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.547 | 0.544 | -0.6% (-1.1 to -0.1) | -0.1% (-1.4 to +1.2) | -0.3% (-0.8 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 333.1 | 333.1 | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.118 | +8.3% (-57.4 to +74.0) | +3.4% (-47.1 to +53.9) | +4.1% (-20.3 to +28.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 189.1 | 207.3 | +9.6% (-65.8 to +85.0) | +3.8% (-51.8 to +59.3) | +4.8% (-22.5 to +32.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.302 | 0.331 | +9.6% (-65.8 to +85.0) | +3.8% (-51.8 to +59.3) | +4.8% (-22.5 to +32.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,328 | 1,327 | -0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.2) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.885 | 0.885 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.57 | 5.55 | -0.3% (-0.8 to +0.3) | +0.1% (-0.4 to +0.6) | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.68 | 5.67 | -0.2% (-0.9 to +0.5) | -0.2% (-2.1 to +1.8) | -0.0% (-0.4 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.752 | 0.746 | -0.9% (-3.2 to +1.5) | -0.9% (-7.3 to +5.5) | +0.1% (-1.1 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 199.8 | 199.8 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0995 | 0.0786 | -21.0% (-93.5 to +51.5) | +22.6% (-82.0 to +127.1) | +12.7% (-42.3 to +67.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 71.0 | 54.7 | -22.9% (-103.5 to +57.6) | +26.3% (-91.5 to +144.1) | +14.5% (-47.7 to +76.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.297 | 0.229 | -22.9% (-103.5 to +57.6) | +26.3% (-91.4 to +144.0) | +14.5% (-47.7 to +76.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.204 | 0.202 | -0.8% (-1.9 to +0.3) | +0.6% (-2.8 to +4.0) | +12.3% (-13.8 to +38.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.66 | 5.66 | -0.0% (-0.3 to +0.2) | +0.0% (-0.2 to +0.3) | -0.1% (-0.2 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, mean (ms) | 0.264 | 0.263 | -0.4% (-1.3 to +0.5) | +0.1% (-1.5 to +1.7) | +1.2% (-0.0 to +2.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 348.4 | 348.5 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | **power given in all three of our runs** |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.0988 | -11.7% (-26.2 to +2.8) | +13.7% (-37.0 to +64.4) | +10.5% (-51.6 to +72.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 195.5 | 170.2 | -12.9% (-28.7 to +2.9) | +15.1% (-41.1 to +71.3) | +11.4% (-57.7 to +80.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.295 | 0.257 | -12.9% (-28.7 to +2.9) | +15.1% (-41.1 to +71.3) | +11.4% (-57.7 to +80.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache hit rate | 0.782 | 0.782 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 5.66 | 5.65 | -0.1% (-0.6 to +0.3) | -0.1% (-0.4 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 5.72 | 5.71 | -0.1% (-0.4 to +0.1) | -0.1% (-0.4 to +0.2) | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.36 | 1.35 | -0.3% (-1.0 to +0.3) | -0.2% (-0.5 to +0.0) | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 257.3 | 257.3 | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.116 | +1.1% (-4.6 to +6.9) | -5.5% (-60.7 to +49.7) | +7.8% (-19.1 to +34.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 191.3 | 194.4 | +1.6% (-4.7 to +8.0) | -5.8% (-66.7 to +55.0) | +8.6% (-21.5 to +38.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 requests inside the line | 0.362 | 0.368 | +1.6% (-4.7 to +8.0) | -5.8% (-66.7 to +55.0) | +8.6% (-21.5 to +38.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 1 power given, 35 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
