# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39150495654 | `c1c1b59711b1` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39160201436 | `773cd59cfdd2` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39169863638 | `2b4c11e3aee0` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,865 | 2,843 | -0.8% (-7.1 to +5.6) | +0.6% (-6.9 to +8.1) | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,874 | 2,851 | -0.8% (-7.1 to +5.5) | +0.6% (-6.9 to +8.1) | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.267 | 0.266 | -0.6% (-3.9 to +2.6) | -1.4% (-8.3 to +5.5) | +0.0% (-1.4 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.43 | 0.428 | -0.5% (-2.6 to +1.5) | -1.1% (-4.0 to +1.8) | +0.1% (-1.0 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.214 | 0.209 | -2.1% (-18.2 to +14.0) | -2.9% (-13.9 to +8.1) | +0.4% (-0.9 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,338 | -0.8% (-5.2 to +3.5) | -0.7% (-8.1 to +6.7) | +0.1% (-0.3 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 63,011 | 62,028 | -1.6% (-8.8 to +5.7) | -1.1% (-12.1 to +10.0) | +0.5% (-0.3 to +1.3) | shown, not judged |
| host CPU busy (share of the run) | 0.172 | 0.174 | +1.1% (-53.3 to +55.5) | -5.5% (-61.8 to +50.7) | +2.8% (-16.1 to +21.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 310.9 | 315.7 | +1.5% (-63.3 to +66.4) | -6.7% (-71.4 to +58.1) | +3.2% (-21.3 to +27.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.242 | +2.0% (-62.0 to +65.9) | -7.5% (-67.9 to +52.8) | +3.2% (-21.3 to +27.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,894 | -0.0% (-0.1 to +0.0) | +0.0% (-0.2 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,899 | 2,899 | -0.0% (-0.1 to +0.0) | +0.0% (-0.2 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.337 | 0.343 | +1.7% (-8.6 to +12.0) | -1.4% (-10.2 to +7.4) | +1.8% (-9.7 to +13.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.517 | 0.521 | +0.7% (-1.5 to +2.9) | -0.6% (-7.2 to +5.9) | -0.1% (-3.5 to +3.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.195 | 0.197 | +1.2% (-3.3 to +5.7) | -0.8% (-5.5 to +4.0) | +1.0% (-8.0 to +9.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,366 | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 61,772 | 61,888 | +0.2% (-0.3 to +0.6) | +0.1% (-0.3 to +0.5) | +0.1% (-0.4 to +0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.179 | 0.185 | +3.0% (-5.0 to +11.1) | -3.7% (-31.5 to +24.1) | -8.4% (-72.0 to +55.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 308.0 | 318.2 | +3.3% (-7.7 to +14.4) | -4.3% (-36.7 to +28.0) | -10.1% (-83.2 to +63.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.231 | 0.239 | +3.4% (-7.7 to +14.4) | -4.3% (-36.8 to +28.1) | -10.1% (-83.2 to +63.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,884 | -0.0% (-0.3 to +0.2) | +0.0% (-0.3 to +0.3) | +0.3% (-0.4 to +1.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,893 | 2,893 | -0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.3) | +0.3% (-0.3 to +1.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.505 | 0.504 | -0.1% (-2.8 to +2.6) | +0.6% (-5.1 to +6.4) | +1.0% (-4.0 to +6.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.667 | 0.665 | -0.3% (-8.7 to +8.0) | +2.1% (-6.3 to +10.4) | +5.8% (-11.1 to +22.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.225 | 0.228 | +1.1% (-2.7 to +4.9) | +0.9% (-5.0 to +6.7) | -0.2% (-17.5 to +17.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,506 | 1,507 | +0.1% (-0.5 to +0.7) | -0.0% (-0.4 to +0.3) | +0.1% (-1.1 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 77,632 | 77,724 | +0.1% (-0.2 to +0.4) | +0.1% (-0.4 to +0.5) | +0.2% (-0.2 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.197 | +4.1% (-34.2 to +42.3) | -15.4% (-116.1 to +85.3) | +0.9% (-43.4 to +45.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 131.7 | 137.8 | +4.6% (-42.4 to +51.7) | -16.7% (-127.5 to +94.1) | +1.1% (-51.3 to +53.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.248 | 0.259 | +4.6% (-42.1 to +51.4) | -16.7% (-127.7 to +94.3) | +0.8% (-51.1 to +52.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,897 | -0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.3) | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,902 | 2,901 | -0.0% (-0.1 to +0.0) | +0.0% (-0.2 to +0.3) | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.301 | 0.302 | +0.3% (-2.6 to +3.3) | -0.7% (-6.7 to +5.4) | +0.9% (-2.1 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.512 | 0.514 | +0.3% (-4.1 to +4.6) | -2.0% (-7.6 to +3.6) | +0.7% (-3.6 to +4.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.187 | 0.189 | +1.2% (-3.2 to +5.6) | -0.0% (-5.9 to +5.9) | +0.3% (-1.6 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,348 | 1,349 | +0.0% (-0.2 to +0.3) | -0.1% (-0.2 to +0.1) | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 61,636 | 61,673 | +0.1% (-0.2 to +0.3) | +0.0% (-0.2 to +0.2) | -0.1% (-0.3 to +0.2) | shown, not judged |
| host CPU busy (share of the run) | 0.165 | 0.166 | +0.7% (-18.2 to +19.6) | -10.3% (-34.2 to +13.5) | -10.4% (-97.7 to +76.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 280.8 | 283.1 | +0.8% (-21.9 to +23.5) | -11.5% (-37.1 to +14.2) | -11.9% (-110.9 to +87.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.211 | 0.213 | +0.8% (-21.9 to +23.6) | -11.5% (-37.2 to +14.2) | -11.9% (-110.9 to +87.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,605 | 5,582 | -0.4% (-1.8 to +1.0) | +0.0% (-0.4 to +0.4) | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,620 | 5,598 | -0.4% (-1.8 to +1.0) | +0.0% (-0.4 to +0.4) | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.462 | 0.464 | +0.6% (-1.8 to +3.0) | +0.4% (-0.5 to +1.2) | +0.4% (-0.7 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.679 | 0.691 | +1.7% (-2.6 to +6.0) | -0.1% (-1.0 to +0.8) | +0.6% (-1.8 to +3.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.269 | 0.27 | +0.4% (-1.6 to +2.5) | +0.2% (-0.7 to +1.0) | +0.5% (-0.3 to +1.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,354 | 1,354 | -0.0% (-0.5 to +0.4) | -0.0% (-0.3 to +0.2) | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 62,550 | 62,641 | +0.1% (-1.3 to +1.6) | -0.2% (-0.9 to +0.5) | +0.2% (-0.3 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.298 | 0.304 | +2.1% (-7.7 to +11.9) | +1.2% (-0.4 to +2.9) | +6.3% (-3.4 to +16.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 505.9 | 517.0 | +2.2% (-9.2 to +13.6) | +1.5% (-0.1 to +3.1) | +8.4% (-5.8 to +22.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.193 | 0.198 | +2.6% (-10.0 to +15.2) | +1.5% (-0.1 to +3.1) | +8.3% (-5.8 to +22.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 0 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 44 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
