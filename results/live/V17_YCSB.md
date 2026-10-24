# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40003734350 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| B | 40022507977 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| C | 40037199208 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,879 | 2,875 | -0.1% (-0.9 to +0.6) | +0.1% (-0.3 to +0.5) | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,888 | 2,883 | -0.1% (-0.9 to +0.6) | +0.1% (-0.3 to +0.5) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.345 | 0.343 | -0.7% (-1.1 to -0.3) | +1.0% (-2.1 to +4.1) | +4.3% (-3.6 to +12.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 0.547 | 0.546 | -0.3% (-4.2 to +3.6) | +0.1% (-1.5 to +1.7) | +2.3% (-1.1 to +5.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.207 | 0.208 | +0.4% (-0.7 to +1.5) | +0.6% (-3.7 to +4.9) | -0.5% (-3.8 to +2.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.6 | -0.9% (-1.1 to -0.6) | -1.3% (-4.0 to +1.3) | -1.2% (-2.9 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 417.4 | 415.9 | -0.4% (-0.9 to +0.2) | -0.9% (-3.8 to +2.0) | -0.7% (-2.4 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 674,332 | 681,344 | +1.0% (-0.1 to +2.1) | +1.9% (-0.5 to +4.3) | +1.8% (-2.9 to +6.6) | shown, not judged |
| host CPU busy (share of the run) | 0.255 | 0.259 | +1.7% (-15.8 to +19.1) | +3.8% (-20.6 to +28.1) | -9.8% (-69.1 to +49.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 458.4 | 467.9 | +2.1% (-22.0 to +26.1) | +4.2% (-26.9 to +35.3) | -10.7% (-76.4 to +54.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.345 | 0.352 | +2.1% (-22.0 to +26.3) | +4.1% (-27.0 to +35.1) | -10.8% (-76.4 to +54.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,881 | -0.1% (-0.3 to +0.1) | -0.1% (-0.2 to +0.0) | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,889 | 2,886 | -0.1% (-0.3 to +0.0) | -0.1% (-0.2 to -0.0) | -0.1% (-0.2 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.343 | 0.363 | +5.8% (-9.4 to +21.0) | +0.6% (-5.2 to +6.4) | +1.1% (-5.1 to +7.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.58 | 0.589 | +1.6% (-1.8 to +5.0) | +0.7% (-2.0 to +3.4) | +0.7% (-4.1 to +5.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.2 | 0.205 | +2.6% (+2.1 to +3.0) | +0.5% (-5.4 to +6.4) | +1.6% (-4.5 to +7.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.7 | -0.5% (-0.9 to -0.0) | -0.6% (-1.1 to -0.2) | -4.7% (-20.8 to +11.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 416.2 | 414.7 | -0.4% (-1.7 to +1.0) | -0.8% (-2.0 to +0.5) | -4.6% (-21.4 to +12.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 674,716 | 753,681 | +11.7% (-5.2 to +28.7) | +0.9% (-8.1 to +9.8) | -2.0% (-35.2 to +31.1) | shown, not judged |
| host CPU busy (share of the run) | 0.197 | 0.218 | +11.0% (-7.2 to +29.1) | +4.8% (-6.2 to +15.8) | +2.1% (-64.6 to +68.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 340.2 | 385.7 | +13.4% (-10.3 to +37.0) | +5.5% (-7.5 to +18.6) | +1.1% (-80.1 to +82.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.256 | 0.29 | +13.4% (-10.2 to +37.0) | +5.5% (-7.5 to +18.5) | +1.1% (-80.2 to +82.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2 | +2 (+2 to +2) | +3.33 (+0.465 to +6.2) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run C: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,934 | 2,929 | -0.1% (-0.4 to +0.1) | -0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,937 | 2,936 | -0.1% (-0.1 to +0.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.246 | 0.265 | +7.9% (-12.4 to +28.1) | +0.9% (-3.1 to +4.8) | -0.1% (-9.9 to +9.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.411 | 0.468 | +14.0% (-21.3 to +49.3) | +2.4% (-5.1 to +9.8) | -1.4% (-6.5 to +3.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.0798 | 0.0872 | +9.3% (-8.4 to +27.0) | -0.4% (-1.2 to +0.4) | -1.4% (-6.6 to +3.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 501.5 | -2.0% (-3.8 to -0.3) | -2.0% (-4.1 to +0.1) | -2.1% (-3.9 to -0.4) | EVEN, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 404.7 | 400.2 | -1.1% (-4.7 to +2.5) | -1.7% (-2.9 to -0.5) | -1.5% (-5.9 to +2.9) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 259,091 | 271,478 | +4.8% (+1.9 to +7.6) | +1.3% (-18.5 to +21.0) | +1.8% (-7.3 to +10.9) | shown, not judged |
| host CPU busy (share of the run) | 0.0649 | 0.0776 | +19.6% (-104.0 to +143.2) | -4.6% (-46.9 to +37.6) | +13.0% (-117.6 to +143.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 45.7 | 55.5 | +21.5% (-114.6 to +157.6) | -6.1% (-59.0 to +46.8) | +14.5% (-126.2 to +155.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.0854 | 0.104 | +21.7% (-115.0 to +158.4) | -6.1% (-58.9 to +46.7) | +14.5% (-126.2 to +155.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4.33 (+0.538 to +8.13) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,884 | -0.1% (-0.2 to +0.0) | -0.0% (-0.1 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% (-0.1 to -0.0) | -0.0% (-0.1 to +0.0) | -0.1% (-0.1 to -0.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| latency, 95th percentile (ms) | 0.312 | 0.309 | -0.9% (-9.0 to +7.3) | +1.0% (-3.5 to +5.4) | +0.0% (-0.8 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.506 | 0.509 | +0.5% (-5.5 to +6.4) | -0.6% (-5.4 to +4.2) | -0.3% (-2.4 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.19 | 0.193 | +1.7% (-2.6 to +6.0) | +1.4% (-0.2 to +3.0) | -0.1% (-4.0 to +3.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 506.6 | -1.1% (-3.9 to +1.8) | -4.4% (-21.6 to +12.7) | -0.8% (-1.7 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| bytes in the cache, mean (MB) | 417.9 | 416.0 | -0.5% (-4.1 to +3.2) | -4.0% (-22.3 to +14.4) | +0.3% (-2.8 to +3.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 684,663 | 710,310 | +3.7% (-15.8 to +23.3) | +6.9% (-0.5 to +14.3) | -2.7% (-22.7 to +17.2) | shown, not judged |
| host CPU busy (share of the run) | 0.214 | 0.207 | -3.0% (-61.7 to +55.7) | -1.8% (-28.6 to +25.0) | -17.6% (-78.8 to +43.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 387.2 | 369.4 | -4.6% (-77.8 to +68.6) | -2.1% (-34.8 to +30.6) | -21.0% (-93.5 to +51.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.291 | 0.278 | -4.6% (-77.9 to +68.7) | -2.1% (-34.8 to +30.6) | -21.0% (-93.5 to +51.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +2.33 (+0.899 to +3.77) | +3 (+0.516 to +5.48) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,685 | 5,671 | -0.2% (-0.9 to +0.4) | +0.3% (-1.1 to +1.7) | +0.1% (-1.3 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,702 | 5,689 | -0.2% (-0.8 to +0.4) | +0.3% (-1.1 to +1.7) | +0.1% (-1.2 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.428 | 0.429 | +0.2% (-1.5 to +2.0) | +0.6% (-0.7 to +1.9) | +0.5% (-2.6 to +3.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.655 | 0.657 | +0.3% (-1.6 to +2.2) | +2.4% (-4.3 to +9.0) | +0.1% (-3.6 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.245 | 0.246 | +0.1% (-2.0 to +2.2) | +0.2% (-8.6 to +8.9) | +0.5% (-3.5 to +4.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 500.0 | -2.4% (-9.0 to +4.3) | -2.3% (-8.8 to +4.3) | -0.8% (-0.9 to -0.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 416.8 | 408.5 | -2.0% (-8.5 to +4.5) | -1.8% (-9.1 to +5.4) | -0.5% (-1.0 to -0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 685,076 | 701,742 | +2.4% (-6.4 to +11.2) | +0.4% (-2.8 to +3.6) | +1.3% (-2.2 to +4.9) | shown, not judged |
| host CPU busy (share of the run) | 0.319 | 0.322 | +0.9% (-1.1 to +2.9) | -0.6% (-8.2 to +7.1) | -0.0% (-7.4 to +7.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 573.2 | 580.0 | +1.2% (-1.2 to +3.5) | -0.9% (-10.8 to +8.9) | -0.4% (-10.2 to +9.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.216 | 0.219 | +1.3% (-1.1 to +3.7) | -1.3% (-11.7 to +9.1) | -0.6% (-11.8 to +10.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run B: acting: 384 to 512 (3 trials, 2 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 44 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
