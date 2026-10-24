# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40008048292 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| B | 40024485005 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 5 |
| C | 40038808111 | `d02c7052ae50` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 5 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7481 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,904 | 2,903 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (operations a second) | 2,909 | 2,909 | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.317 | 0.318 | +0.5% (-2.4 to +3.5) | +5.4% (-6.3 to +17.1) | +2.3% (-1.2 to +5.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.541 | 0.537 | -0.7% (-3.4 to +2.0) | +3.6% (-0.9 to +8.0) | +0.4% (-0.9 to +1.8) | **the runs disagree** |
| latency, mean (ms) | 0.143 | 0.142 | -0.7% (-1.3 to -0.1) | +1.3% (-7.4 to +10.0) | +0.4% (-1.5 to +2.3) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,362 | 1,363 | +0.0% (-0.3 to +0.4) | +0.0% (-0.5 to +0.5) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.00%) |
| pages read into the cache (misses) | 63,122 | 63,014 | -0.2% (-1.3 to +1.0) | -0.3% (-0.7 to +0.2) | +0.5% (-1.6 to +2.6) | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.172 | -1.8% (-9.6 to +6.1) | +18.4% (-70.3 to +107.1) | -11.0% (-37.9 to +15.9) | **the runs disagree** |
| host CPU-seconds | 316.2 | 309.9 | -2.0% (-11.1 to +7.2) | +20.0% (-79.2 to +119.2) | -14.4% (-49.4 to +20.6) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.237 | 0.233 | -1.9% (-11.1 to +7.2) | +20.0% (-79.3 to +119.3) | -14.4% (-49.3 to +20.5) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,910 | 2,873 | -1.3% (-6.6 to +4.1) | +0.1% (-0.3 to +0.4) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.39%) |
| throughput (operations a second) | 2,915 | 2,879 | -1.2% (-6.5 to +4.0) | +0.1% (-0.3 to +0.4) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.38%) |
| latency, 95th percentile (ms) | 0.199 | 0.204 | +2.5% (-4.1 to +9.1) | +3.0% (+1.8 to +4.3) | +0.1% (-8.9 to +9.1) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 0.379 | 0.389 | +2.7% (-3.5 to +8.9) | +2.7% (-3.6 to +9.1) | +0.3% (-3.7 to +4.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.145 | 0.153 | +5.9% (-18.4 to +30.2) | -2.3% (-19.9 to +15.3) | +0.6% (-3.1 to +4.2) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,361 | -0.4% (-1.5 to +0.7) | +0.1% (-0.9 to +1.2) | +0.0% (-0.3 to +0.3) | EVEN, under the floor (the three runs' mean 0.08%) |
| pages read into the cache (misses) | 61,806 | 61,852 | +0.1% (-0.5 to +0.6) | +0.1% (-0.0 to +0.2) | +0.1% (-0.6 to +0.8) | shown, not judged |
| host CPU busy (share of the run) | 0.142 | 0.153 | +7.8% (-24.2 to +39.8) | +16.8% (-15.4 to +48.9) | -3.9% (-12.6 to +4.8) | **the runs disagree** |
| host CPU-seconds | 252.8 | 276.6 | +9.4% (-28.2 to +47.1) | +20.0% (-17.8 to +57.8) | -5.0% (-17.2 to +7.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.189 | 0.21 | +10.7% (-26.2 to +47.5) | +20.0% (-17.6 to +57.6) | -5.0% (-17.2 to +7.2) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,880 | 2,878 | -0.0% (-0.2 to +0.1) | +0.0% (-0.1 to +0.1) | -0.2% (-0.5 to +0.1) | EVEN, under the floor (the three runs' mean 0.08%) |
| throughput (operations a second) | 2,886 | 2,885 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | -0.1% (-0.5 to +0.2) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, 95th percentile (ms) | 0.424 | 0.43 | +1.3% (-8.2 to +10.9) | +0.2% (-2.4 to +2.8) | +3.6% (-7.8 to +14.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.582 | 0.597 | +2.5% (-7.7 to +12.8) | -0.4% (-3.7 to +3.0) | +6.6% (-1.3 to +14.4) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.212 | 0.214 | +1.0% (-7.7 to +9.6) | -0.4% (-3.2 to +2.4) | +8.0% (-9.7 to +25.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,512 | 1,511 | -0.1% (-0.3 to +0.2) | -0.1% (-0.4 to +0.3) | -0.6% (-2.1 to +0.9) | EVEN, under the floor (the three runs' mean 0.23%) |
| pages read into the cache (misses) | 77,615 | 77,649 | +0.0% (-0.1 to +0.2) | +0.0% (-0.3 to +0.4) | +0.1% (-0.6 to +0.8) | shown, not judged |
| host CPU busy (share of the run) | 0.215 | 0.215 | -0.2% (-25.2 to +24.8) | +11.9% (-47.7 to +71.5) | +13.0% (-35.2 to +61.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 154.3 | 153.0 | -0.8% (-33.6 to +31.9) | +14.2% (-59.9 to +88.3) | +15.5% (-43.9 to +74.9) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.288 | -0.8% (-33.4 to +31.8) | +14.1% (-60.0 to +88.2) | +15.6% (-43.7 to +75.0) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,943 | 2,940 | -0.1% (-0.2 to -0.0) | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,945 | 2,942 | -0.1% (-0.1 to -0.1) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 0.075 | 0.0873 | +16.4% (-28.5 to +61.4) | -1.0% (-1.8 to -0.2) | +1.7% (-5.9 to +9.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.258 | 0.278 | +7.7% (-20.2 to +35.7) | -0.3% (-1.9 to +1.2) | +0.1% (-3.5 to +3.7) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.0497 | 0.0535 | +7.7% (-12.2 to +27.7) | +0.2% (-2.3 to +2.8) | +0.7% (-1.6 to +3.0) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,350 | 1,350 | +0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.00%) |
| pages read into the cache (misses) | 61,661 | 61,666 | +0.0% (-0.3 to +0.3) | +0.0% (-0.2 to +0.3) | -0.1% (-0.3 to +0.2) | shown, not judged |
| host CPU busy (share of the run) | 0.079 | 0.0673 | -14.9% (-76.3 to +46.5) | +1.0% (-59.0 to +61.1) | -4.1% (-15.6 to +7.4) | **the runs disagree** |
| host CPU-seconds | 145.3 | 121.0 | -16.7% (-82.0 to +48.6) | +0.9% (-75.5 to +77.3) | -5.1% (-18.7 to +8.4) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.108 | 0.0904 | -16.6% (-82.0 to +48.7) | +0.9% (-75.5 to +77.3) | -5.1% (-18.6 to +8.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7483 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,725 | 5,729 | +0.1% (-0.2 to +0.3) | -2.5% (-4.1 to -0.9) | +0.1% (-0.0 to +0.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| throughput (operations a second) | 5,740 | 5,742 | +0.0% (-0.3 to +0.3) | -2.4% (-3.9 to -1.0) | +0.1% (-0.0 to +0.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 95th percentile (ms) | 0.372 | 0.37 | -0.5% (-6.2 to +5.2) | +0.1% (-4.6 to +4.8) | +0.3% (-1.0 to +1.6) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 0.645 | 0.637 | -1.3% (-7.2 to +4.6) | +5.4% (-10.5 to +21.2) | +0.3% (-1.8 to +2.4) | **the runs disagree** |
| latency, mean (ms) | 0.191 | 0.191 | -0.2% (-5.1 to +4.8) | +4.0% (+0.9 to +7.1) | -0.7% (-3.3 to +1.9) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,483 | 7,483 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,362 | -0.0% (-0.6 to +0.5) | -0.2% (-1.2 to +0.8) | -0.1% (-0.4 to +0.3) | EVEN, under the floor (the three runs' mean 0.11%) |
| pages read into the cache (misses) | 62,970 | 62,955 | -0.0% (-2.1 to +2.1) | +0.0% (-0.9 to +0.9) | +0.2% (-1.5 to +1.9) | shown, not judged |
| host CPU busy (share of the run) | 0.254 | 0.248 | -2.4% (-4.5 to -0.4) | -7.8% (-31.6 to +16.0) | -5.0% (-9.3 to -0.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds | 467.4 | 451.9 | -3.3% (-6.1 to -0.5) | -9.4% (-37.8 to +18.9) | -6.4% (-12.0 to -0.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.176 | 0.17 | -3.4% (-6.3 to -0.5) | -7.2% (-36.8 to +22.4) | -6.4% (-11.9 to -0.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 3 gauge-rows GAIN, 9 LOSS, 1 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 19 EVEN, 12 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
