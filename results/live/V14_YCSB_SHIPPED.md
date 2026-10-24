# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39562510452 | `418f860a4da6` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |
| B | 39590117126 | `e997ca0d9f65` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |
| C | 39616239634 | `63a093f13de0` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7481 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,898 | 2,896 | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.2) | -0.0% (-0.0 to -0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,905 | 2,905 | -0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.3) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.353 | 0.359 | +1.7% (-7.4 to +10.8) | -0.2% (-5.3 to +4.9) | +1.7% (+0.6 to +2.8) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 0.618 | 0.631 | +2.0% (-3.1 to +7.2) | -1.8% (-5.8 to +2.1) | +1.5% (+0.5 to +2.5) | **the runs disagree** |
| latency, mean (ms) | 0.155 | 0.157 | +1.2% (-2.7 to +5.0) | -0.7% (-6.3 to +4.9) | -0.3% (-1.4 to +0.9) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,481 | 7,481 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,363 | 1,363 | +0.1% (-0.2 to +0.3) | +0.0% (-0.6 to +0.7) | -0.1% (-0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.00%) |
| pages read into the cache (misses) | 63,165 | 63,031 | -0.2% (-1.7 to +1.3) | -0.5% (-1.2 to +0.2) | +0.1% (-1.2 to +1.4) | shown, not judged |
| host CPU busy (share of the run) | 0.19 | 0.194 | +1.9% (-44.1 to +48.0) | -9.0% (-51.4 to +33.4) | +5.1% (-26.8 to +37.0) | **the runs disagree** |
| host CPU-seconds | 345.7 | 353.2 | +2.2% (-54.3 to +58.7) | -10.7% (-60.2 to +38.8) | +6.5% (-34.2 to +47.1) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.26 | 0.265 | +2.2% (-54.3 to +58.7) | -10.7% (-60.1 to +38.7) | +6.5% (-34.3 to +47.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,884 | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,890 | 2,890 | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.319 | 0.322 | +1.0% (-5.6 to +7.7) | +7.5% (-8.4 to +23.5) | -0.3% (-14.8 to +14.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.593 | 0.595 | +0.3% (-1.5 to +2.2) | +0.7% (-5.8 to +7.2) | -0.4% (-6.6 to +5.8) | EVEN, under the floor (the three runs' mean 0.21%) |
| latency, mean (ms) | 0.192 | 0.192 | +0.1% (-3.2 to +3.4) | +1.8% (-5.4 to +8.9) | -0.0% (-6.9 to +6.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,365 | 1,365 | +0.0% (-0.0 to +0.1) | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| pages read into the cache (misses) | 61,790 | 61,901 | +0.2% (-0.4 to +0.8) | +0.1% (-0.2 to +0.5) | +0.1% (-0.5 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.206 | 0.207 | +0.8% (-11.8 to +13.5) | -12.2% (-75.0 to +50.6) | -2.9% (-61.7 to +55.9) | **the runs disagree** |
| host CPU-seconds | 366.0 | 370.1 | +1.1% (-14.3 to +16.5) | -12.8% (-80.4 to +54.8) | -3.6% (-77.2 to +70.0) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.275 | 0.278 | +1.1% (-14.3 to +16.6) | -12.8% (-80.4 to +54.9) | -3.6% (-77.2 to +70.0) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,860 | 2,871 | +0.4% (-2.0 to +2.7) | +0.1% (-0.1 to +0.2) | -1.4% (-17.5 to +14.7) | EVEN, under the floor (the three runs' mean 0.32%) |
| throughput (operations a second) | 2,871 | 2,883 | +0.4% (-1.9 to +2.7) | +0.1% (-0.1 to +0.3) | -1.5% (-17.6 to +14.6) | EVEN, under the floor (the three runs' mean 0.34%) |
| latency, 95th percentile (ms) | 0.53 | 0.533 | +0.6% (-3.4 to +4.7) | -0.5% (-16.2 to +15.2) | +1.1% (-7.3 to +9.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.713 | 0.713 | +0.0% (-5.7 to +5.8) | -1.7% (-12.0 to +8.6) | -6.1% (-23.4 to +11.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.229 | 0.228 | -0.6% (-6.7 to +5.5) | -1.7% (-18.2 to +14.8) | +1.5% (-19.5 to +22.5) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,490 | 1,496 | +0.4% (-2.1 to +3.0) | +0.3% (+0.1 to +0.5) | -2.0% (-27.4 to +23.4) | EVEN, under the floor (the three runs' mean 0.43%) |
| pages read into the cache (misses) | 77,542 | 77,602 | +0.1% (-0.4 to +0.6) | +0.1% (-0.1 to +0.4) | -0.2% (-3.3 to +3.0) | shown, not judged |
| host CPU busy (share of the run) | 0.212 | 0.216 | +1.8% (-24.6 to +28.1) | +11.9% (-67.3 to +91.2) | -4.6% (-27.5 to +18.4) | **the runs disagree** |
| host CPU-seconds | 151.1 | 154.7 | +2.3% (-31.8 to +36.5) | +14.1% (-73.7 to +102.0) | -5.7% (-32.7 to +21.3) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.286 | 0.292 | +1.9% (-30.1 to +34.0) | +14.1% (-73.8 to +102.0) | -4.2% (-23.8 to +15.3) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,938 | 2,937 | -0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,939 | 2,938 | -0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.1) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.0967 | 0.099 | +2.4% (-10.5 to +15.3) | +0.8% (-10.9 to +12.4) | -0.9% (-2.1 to +0.4) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.303 | 0.309 | +1.9% (-8.4 to +12.1) | +0.8% (-6.3 to +8.0) | -0.1% (-3.7 to +3.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.0564 | 0.0576 | +2.2% (+1.0 to +3.3) | +0.8% (-6.1 to +7.6) | +0.9% (-3.1 to +4.9) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,351 | 1,350 | -0.1% (-0.1 to -0.0) | +0.0% (-0.1 to +0.1) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.01%) |
| pages read into the cache (misses) | 61,718 | 61,666 | -0.1% (-0.3 to +0.1) | +0.1% (-0.0 to +0.2) | +0.1% (-0.2 to +0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.0625 | 0.0829 | +32.7% (-16.9 to +82.2) | +7.8% (-74.1 to +89.7) | +6.6% (-13.1 to +26.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 111.3 | 150.9 | +35.6% (-19.8 to +90.9) | +8.4% (-79.6 to +96.5) | +7.8% (-17.3 to +32.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.0831 | 0.113 | +35.6% (-19.8 to +91.0) | +8.4% (-79.6 to +96.5) | +7.8% (-17.3 to +32.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,676 | 5,668 | -0.1% (-0.4 to +0.1) | +0.1% (-0.2 to +0.3) | +0.1% (-0.3 to +0.4) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 5,689 | 5,682 | -0.1% (-0.4 to +0.1) | +0.1% (-0.1 to +0.2) | +0.1% (-0.3 to +0.5) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.42 | 0.424 | +1.1% (-1.6 to +3.8) | +0.3% (-1.6 to +2.2) | +0.3% (-1.6 to +2.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.642 | 0.652 | +1.6% (+0.2 to +3.0) | -0.0% (-3.9 to +3.8) | -0.1% (-1.1 to +0.9) | EVEN, under the floor (the three runs' mean 0.47%) |
| latency, mean (ms) | 0.239 | 0.242 | +1.3% (-1.4 to +3.9) | +0.1% (-3.1 to +3.4) | +0.5% (-1.5 to +2.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,360 | 1,360 | +0.0% (-0.0 to +0.1) | -0.1% (-0.6 to +0.4) | +0.1% (+0.0 to +0.2) | EVEN, under the floor (the three runs' mean 0.03%) |
| pages read into the cache (misses) | 62,843 | 62,826 | -0.0% (-0.5 to +0.4) | -0.3% (-2.3 to +1.7) | +0.4% (+0.2 to +0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.307 | 0.311 | +1.3% (-6.1 to +8.6) | +0.3% (-4.6 to +5.2) | +1.2% (-1.0 to +3.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 556.4 | 562.9 | +1.2% (-9.0 to +11.3) | +0.4% (-7.1 to +7.9) | +1.6% (-2.3 to +5.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.21 | 0.213 | +1.3% (-8.9 to +11.4) | +0.4% (-7.0 to +7.7) | +1.6% (-2.1 to +5.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 4 untouched workloads: 1 gauge-rows GAIN, 6 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 22 EVEN, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
