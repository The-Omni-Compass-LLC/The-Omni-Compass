# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39823811507 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39842363997 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39862241743 | `681ff70efadd` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,878 | 2,877 | -0.0% (-0.6 to +0.5) | -0.1% (-0.2 to +0.1) | +0.0% (-0.4 to +0.4) | STEADY, under the floor (the three runs' mean 0.04%) |
| throughput (operations a second) | 2,888 | 2,887 | -0.0% (-0.5 to +0.5) | -0.0% (-0.2 to +0.2) | +0.0% (-0.3 to +0.4) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms) | 0.358 | 0.358 | +0.2% (-2.6 to +3.0) | +3.1% (-1.7 to +8.0) | +0.5% (-4.3 to +5.3) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.569 | 0.579 | +1.7% (-4.2 to +7.6) | +3.7% (-3.5 to +10.9) | +2.6% (-10.0 to +15.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.217 | 0.216 | -0.4% (-4.2 to +3.4) | +0.1% (-10.0 to +10.2) | +0.1% (-6.6 to +6.9) | STEADY, under the floor (the three runs' mean 0.06%) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 505.5 | -1.3% (-3.6 to +1.0) | -1.2% (-3.3 to +0.9) | -0.7% (-1.0 to -0.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 417.0 | 414.3 | -0.7% (-2.8 to +1.5) | -0.5% (-3.0 to +2.1) | -0.6% (-1.1 to -0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 672,793 | 686,980 | +2.1% (-1.7 to +5.9) | +1.1% (-0.6 to +2.8) | +0.1% (-3.4 to +3.6) | shown, not judged |
| host CPU busy (share of the run) | 0.241 | 0.259 | +7.8% (-32.1 to +47.7) | -5.2% (-6.9 to -3.5) | -8.4% (-30.5 to +13.8) | **the runs disagree** |
| host CPU-seconds | 420.0 | 463.6 | +10.4% (-43.5 to +64.3) | -7.0% (-10.1 to -3.8) | -11.2% (-38.9 to +16.4) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.316 | 0.349 | +10.4% (-43.1 to +63.8) | -7.0% (-10.0 to -3.9) | -11.2% (-39.1 to +16.7) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (+2.23 to +5.1) | +3.67 (+2.23 to +5.1) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,884 | 2,881 | -0.1% (-0.3 to +0.2) | -0.1% (-0.2 to +0.0) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.08%) |
| throughput (operations a second) | 2,889 | 2,887 | -0.1% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | -0.1% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 0.35 | 0.361 | +3.2% (-9.0 to +15.5) | +2.6% (-10.5 to +15.7) | +5.5% (-25.8 to +36.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.538 | 0.554 | +3.0% (-8.3 to +14.2) | +0.2% (-3.1 to +3.5) | +2.1% (-4.3 to +8.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.201 | 0.205 | +2.1% (-2.8 to +6.9) | +0.2% (-7.8 to +8.2) | +2.1% (-3.0 to +7.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.2 | -0.9% (-3.7 to +1.9) | -1.1% (-3.2 to +0.9) | -0.7% (-1.4 to -0.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 416.7 | 415.4 | -0.3% (-3.1 to +2.4) | -0.4% (-3.3 to +2.5) | -0.2% (-1.2 to +0.8) | STEADY, under the floor (the three runs' mean 0.29%) |
| pages read into the cache (misses) | 691,831 | 724,988 | +4.8% (+1.3 to +8.3) | +1.4% (-16.6 to +19.4) | +1.1% (-11.9 to +14.2) | shown, not judged |
| host CPU busy (share of the run) | 0.201 | 0.211 | +4.7% (-27.8 to +37.2) | +1.1% (-19.1 to +21.4) | +12.5% (-58.4 to +83.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 350.6 | 368.8 | +5.2% (-35.1 to +45.5) | +1.2% (-24.8 to +27.3) | +13.5% (-65.1 to +92.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.264 | 0.277 | +5.3% (-35.2 to +45.7) | +1.3% (-24.7 to +27.3) | +13.5% (-65.1 to +92.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 2.33 | +2.33 (+0.899 to +3.77) | +3 (+0.516 to +5.48) | +2.67 (+1.23 to +4.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 0 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,925 | 2,926 | +0.0% (-0.1 to +0.2) | -0.0% (-0.1 to +0.0) | +0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (operations a second) | 2,929 | 2,929 | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | +0.0% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.356 | 0.358 | +0.6% (-0.6 to +1.8) | +3.9% (-5.8 to +13.5) | -1.0% (-4.5 to +2.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.502 | 0.5 | -0.3% (-1.5 to +0.8) | +1.5% (-7.5 to +10.5) | +0.9% (-6.1 to +7.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.14 | 0.139 | -0.1% (-2.5 to +2.3) | +1.9% (-0.4 to +4.3) | -1.4% (-5.0 to +2.2) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 503.4 | -1.7% (-2.8 to -0.6) | -2.2% (-3.5 to -1.0) | -2.0% (-2.2 to -1.9) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 406.5 | 401.3 | -1.3% (-1.4 to -1.1) | -2.1% (-6.6 to +2.5) | -1.2% (-3.0 to +0.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 269,181 | 265,850 | -1.2% (-3.4 to +1.0) | -0.2% (-20.0 to +19.6) | -2.0% (-11.9 to +8.0) | shown, not judged |
| host CPU busy (share of the run) | 0.13 | 0.105 | -19.0% (-106.5 to +68.4) | +5.4% (-9.5 to +20.3) | +1.1% (-61.7 to +63.9) | **the runs disagree** |
| host CPU-seconds | 95.8 | 74.3 | -22.4% (-123.3 to +78.5) | +5.7% (-10.6 to +21.9) | +1.1% (-78.9 to +81.2) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.179 | 0.139 | -22.4% (-123.2 to +78.4) | +5.7% (-10.5 to +21.9) | +1.1% (-79.0 to +81.2) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4.67 (+1.8 to +7.54) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,906 | 2,905 | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to -0.0) | -0.2% (-0.3 to +0.0) | STEADY, under the floor (the three runs' mean 0.11%) |
| throughput (operations a second) | 2,908 | 2,907 | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to +0.0) | -0.1% (-0.3 to +0.0) | STEADY, under the floor (the three runs' mean 0.10%) |
| latency, 95th percentile (ms) | 0.28 | 0.28 | -0.2% (-2.5 to +2.0) | -0.4% (-3.1 to +2.4) | +8.1% (-9.2 to +25.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.446 | 0.445 | -0.4% (-1.0 to +0.3) | +1.4% (-7.3 to +10.0) | +1.5% (-16.5 to +19.6) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 0.147 | 0.149 | +1.1% (-0.6 to +2.8) | +3.6% (-2.4 to +9.6) | +7.0% (-4.6 to +18.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.4 | -0.7% (-1.4 to -0.0) | -1.3% (-3.1 to +0.6) | -8.3% (-24.7 to +8.1) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| bytes in the cache, mean (MB) | 417.6 | 417.8 | +0.0% (-0.3 to +0.4) | -1.5% (-2.8 to -0.2) | -7.5% (-24.5 to +9.4) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 663,721 | 691,274 | +4.2% (-2.6 to +10.9) | -6.7% (-18.8 to +5.3) | +16.7% (-18.4 to +51.8) | shown, not judged |
| host CPU busy (share of the run) | 0.153 | 0.188 | +22.8% (-35.9 to +81.5) | -0.7% (-22.3 to +21.0) | +20.4% (-16.5 to +57.2) | **the runs disagree** |
| host CPU-seconds | 274.5 | 348.8 | +27.1% (-42.6 to +96.7) | -0.5% (-25.8 to +24.9) | +21.6% (-18.0 to +61.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 operations inside the line | 0.206 | 0.261 | +27.1% (-42.6 to +96.8) | -0.4% (-25.8 to +24.9) | +21.6% (-18.0 to +61.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| cache size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+0.465 to +6.2) | +4.33 (+2.9 to +5.77) | +2.33 (-1.46 to +6.13) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run C: acting: 448 to 512 (2 trials, 1 allowed, 0 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (1 trials, 1 allowed, 0 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,749 | 5,748 | -0.0% (-0.1 to +0.0) | -0.1% (-0.4 to +0.2) | -0.3% (-0.5 to +0.0) | STEADY, under the floor (the three runs' mean 0.13%) |
| throughput (operations a second) | 5,765 | 5,765 | -0.0% (-0.1 to +0.1) | -0.1% (-0.4 to +0.2) | -0.2% (-0.5 to -0.0) | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, 95th percentile (ms) | 0.318 | 0.319 | +0.3% (-1.8 to +2.4) | -0.5% (-3.1 to +2.2) | +11.6% (-30.1 to +53.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.485 | 0.497 | +2.5% (-8.3 to +13.2) | -0.8% (-4.9 to +3.3) | +7.7% (-16.8 to +32.2) | **the runs disagree** |
| latency, mean (ms) | 0.19 | 0.188 | -1.1% (-5.8 to +3.6) | -1.0% (-3.5 to +1.5) | +7.1% (-23.1 to +37.3) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 507.9 | -0.8% (-1.2 to -0.4) | -0.9% (-1.4 to -0.4) | -1.0% (-1.7 to -0.3) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 415.2 | 413.7 | -0.4% (-1.7 to +1.0) | -0.6% (-1.7 to +0.4) | -0.9% (-2.1 to +0.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| pages read into the cache (misses) | 688,711 | 692,936 | +0.6% (-1.0 to +2.2) | +0.4% (-2.7 to +3.6) | -1.1% (-5.3 to +3.0) | shown, not judged |
| host CPU busy (share of the run) | 0.237 | 0.247 | +4.1% (-4.9 to +13.2) | -5.3% (-28.5 to +18.0) | +11.6% (-63.3 to +86.4) | **the runs disagree** |
| host CPU-seconds | 426.5 | 448.7 | +5.2% (-5.9 to +16.3) | -6.8% (-36.6 to +23.0) | +13.1% (-72.3 to +98.6) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.16 | 0.168 | +5.2% (-5.8 to +16.2) | -6.8% (-36.5 to +22.9) | +13.2% (-72.4 to +98.8) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

**Across 4 untouched workloads: 7 gauge-rows GAIN, 8 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 STEADY, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
