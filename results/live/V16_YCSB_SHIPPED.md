# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39826088859 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39846968680 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39866167058 | `5f430c111d90` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,886 | 2,885 | -0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.3) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,890 | 2,890 | -0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.324 | 0.325 | +0.4% (-5.2 to +6.1) | -0.2% (-13.8 to +13.4) | +2.4% (-7.2 to +11.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.474 | 0.474 | -0.1% (-3.0 to +2.9) | +0.8% (-7.0 to +8.7) | +1.1% (-7.0 to +9.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.192 | 0.192 | +0.3% (-1.3 to +1.8) | -0.9% (-3.5 to +1.6) | +0.7% (-1.4 to +2.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% (-0.1 to +0.2) | +0.0% (-0.4 to +0.4) | +0.0% (-0.7 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 62,971 | 63,263 | +0.5% (-1.8 to +2.7) | +0.1% (-1.4 to +1.5) | -0.5% (-2.7 to +1.7) | shown, not judged |
| host CPU busy (share of the run) | 0.228 | 0.216 | -5.1% (-52.2 to +42.0) | +2.4% (-32.8 to +37.6) | -2.1% (-37.1 to +33.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 409.8 | 383.9 | -6.3% (-67.1 to +54.5) | +2.3% (-36.3 to +40.9) | -2.7% (-44.4 to +39.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.308 | 0.288 | -6.3% (-67.0 to +54.4) | +2.3% (-36.2 to +40.8) | -2.7% (-44.4 to +39.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7481 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,914 | +0.1% (-0.1 to +0.2) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,915 | 2,917 | +0.1% (-0.1 to +0.2) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.208 | 0.207 | -0.6% (-19.2 to +17.9) | +0.8% (-34.8 to +36.3) | +2.1% (-6.6 to +10.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.44 | 0.444 | +0.8% (-18.4 to +20.1) | -1.1% (-14.0 to +11.8) | +0.9% (-1.8 to +3.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.11 | 0.108 | -1.8% (-11.4 to +7.8) | -0.6% (-11.7 to +10.5) | +1.1% (-3.7 to +6.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | +0.0% (-0.3 to +0.3) | -0.1% (-0.3 to +0.2) | -0.1% (-0.2 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 61,768 | 61,844 | +0.1% (-0.4 to +0.6) | +0.0% (-0.6 to +0.6) | -0.0% (-0.6 to +0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.126 | -13.0% (-74.7 to +48.8) | -16.4% (-82.2 to +49.4) | +1.5% (-8.8 to +11.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 266.7 | 227.0 | -14.9% (-86.3 to +56.5) | -18.2% (-91.9 to +55.4) | +1.6% (-9.8 to +13.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.2 | 0.17 | -14.9% (-86.3 to +56.5) | -18.2% (-91.9 to +55.5) | +1.6% (-9.8 to +13.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,879 | +0.0% (-0.2 to +0.2) | -0.1% (-0.5 to +0.4) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,887 | 2,888 | +0.0% (-0.1 to +0.2) | -0.1% (-0.4 to +0.3) | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.468 | 0.474 | +1.2% (-1.5 to +3.9) | +3.6% (-12.3 to +19.6) | +0.9% (-7.0 to +8.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.644 | 0.654 | +1.5% (-2.8 to +5.8) | +5.2% (-23.9 to +34.2) | +0.1% (-7.6 to +7.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.215 | 0.217 | +0.8% (-0.3 to +1.8) | +2.3% (-30.7 to +35.3) | -0.0% (-3.3 to +3.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,508 | 1,508 | +0.0% (-0.3 to +0.3) | +0.3% (-0.0 to +0.6) | +0.2% (-0.1 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 77,635 | 77,725 | +0.1% (-0.1 to +0.3) | +0.1% (-0.1 to +0.4) | +0.0% (-0.1 to +0.2) | shown, not judged |
| host CPU busy (share of the run) | 0.168 | 0.203 | +20.9% (-14.8 to +56.5) | +38.2% (-55.3 to +131.6) | -47.2% (-71.6 to -22.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 114.0 | 143.5 | +25.9% (-19.5 to +71.4) | +41.7% (-62.5 to +145.9) | -50.1% (-76.7 to -23.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.215 | 0.27 | +25.9% (-19.6 to +71.4) | +41.8% (-62.7 to +146.3) | -50.1% (-76.7 to -23.6) | EVEN, no difference beyond the noise (2 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,936 | 2,938 | +0.1% (-0.0 to +0.1) | -0.1% (-0.5 to +0.4) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,938 | 2,940 | +0.1% (-0.0 to +0.1) | -0.1% (-0.4 to +0.3) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.092 | 0.0923 | +0.4% (-10.6 to +11.3) | +1.6% (-7.6 to +10.9) | +0.0% (-1.4 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.301 | 0.315 | +4.8% (-4.3 to +13.9) | +0.0% (-15.4 to +15.4) | +1.3% (-5.8 to +8.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.0566 | 0.0571 | +0.9% (-1.2 to +2.9) | +2.5% (-7.0 to +12.1) | +0.2% (-4.1 to +4.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | -0.0% (-0.1 to +0.1) | -0.0% (-0.3 to +0.2) | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 61,695 | 61,697 | +0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | +0.1% (-0.3 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0737 | 0.0811 | +10.1% (-9.4 to +29.7) | +8.0% (-14.5 to +30.5) | -0.6% (-116.5 to +115.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 132.8 | 147.6 | +11.1% (-10.9 to +33.1) | +9.3% (-19.6 to +38.3) | -1.2% (-132.8 to +130.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.0992 | 0.11 | +11.1% (-10.8 to +33.0) | +9.4% (-19.4 to +38.1) | -1.1% (-132.7 to +130.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,681 | 5,682 | +0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.3) | +0.2% (-0.4 to +0.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,694 | 5,695 | +0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | +0.2% (-0.4 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.414 | 0.415 | +0.1% (-1.2 to +1.3) | -0.1% (-1.0 to +0.8) | -1.2% (-6.6 to +4.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.635 | 0.641 | +0.9% (-2.6 to +4.4) | +2.6% (-9.5 to +14.8) | -2.7% (-11.8 to +6.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.236 | 0.236 | -0.1% (-0.7 to +0.6) | -0.2% (-4.4 to +4.0) | -1.0% (-5.2 to +3.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,361 | 1,361 | +0.0% (+0.0 to +0.1) | +0.2% (-0.7 to +1.1) | -0.2% (-0.7 to +0.3) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 62,753 | 62,987 | +0.4% (-0.8 to +1.5) | +0.1% (-0.6 to +0.7) | +0.1% (-1.4 to +1.6) | shown, not judged |
| host CPU busy (share of the run) | 0.297 | 0.299 | +0.9% (-5.9 to +7.6) | +2.6% (-28.8 to +34.0) | -6.3% (-22.1 to +9.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 531.9 | 539.1 | +1.4% (-8.5 to +11.3) | +3.7% (-37.3 to +44.6) | -8.4% (-29.4 to +12.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.201 | 0.203 | +1.3% (-8.6 to +11.2) | +3.7% (-37.4 to +44.7) | -8.5% (-29.8 to +12.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 44 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
