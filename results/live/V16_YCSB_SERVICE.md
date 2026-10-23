# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39869906902 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| B | 39871660953 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |
| C | 39871685303 | `464fb9e27535` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,873 | 2,875 | +0.1% (-0.8 to +1.0) | -0.0% (-0.1 to +0.1) | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,884 | 2,885 | +0.1% (-0.8 to +0.9) | -0.0% (-0.1 to +0.0) | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.366 | 0.364 | -0.5% (-2.3 to +1.3) | +2.3% (-7.4 to +11.9) | +0.3% (-1.1 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.581 | 0.574 | -1.1% (-4.9 to +2.8) | +1.2% (-6.6 to +9.0) | +0.7% (-1.7 to +3.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.218 | 0.217 | -0.8% (-3.3 to +1.8) | +0.2% (-0.5 to +0.9) | +0.9% (-0.8 to +2.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.0 | -0.8% (-1.5 to -0.1) | -1.0% (-1.6 to -0.4) | -0.8% (-1.4 to -0.3) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 417.4 | 416.0 | -0.3% (-0.9 to +0.3) | -0.5% (-1.6 to +0.6) | -0.4% (-1.2 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 674,907 | 683,763 | +1.3% (-2.0 to +4.6) | +1.2% (+0.5 to +2.0) | +1.0% (+0.7 to +1.4) | shown, not judged |
| host CPU busy (share of the run) | 0.24 | 0.247 | +2.8% (-25.2 to +30.8) | +14.2% (-71.4 to +99.9) | +8.1% (-17.7 to +34.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 416.4 | 433.1 | +4.0% (-33.0 to +41.0) | +16.8% (-82.3 to +115.9) | +10.6% (-23.6 to +44.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.314 | 0.326 | +3.9% (-32.4 to +40.2) | +16.7% (-82.4 to +115.9) | +10.5% (-23.3 to +44.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +4 (+4 to +4) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,885 | 2,883 | -0.1% (-0.1 to -0.0) | -0.1% (-0.2 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| throughput (operations a second) | 2,890 | 2,888 | -0.1% (-0.1 to -0.0) | -0.1% (-0.2 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| latency, 95th percentile (ms) | 0.338 | 0.34 | +0.6% (-0.1 to +1.3) | +1.3% (-1.5 to +4.0) | -0.2% (-1.5 to +1.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.526 | 0.525 | -0.2% (-1.1 to +0.8) | -0.2% (-4.0 to +3.5) | -0.9% (-2.9 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.199 | 0.2 | +0.2% (-1.8 to +2.1) | +0.8% (-0.5 to +2.1) | +0.1% (-3.1 to +3.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 506.2 | -1.1% (-3.0 to +0.7) | -0.9% (-3.1 to +1.3) | -0.8% (-1.7 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| bytes in the cache, mean (MB) | 417.7 | 415.8 | -0.5% (-1.9 to +1.0) | -0.6% (-2.8 to +1.7) | -0.1% (-3.3 to +3.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 698,860 | 717,724 | +2.7% (-15.9 to +21.3) | -2.9% (-13.0 to +7.2) | -0.4% (-22.7 to +22.0) | shown, not judged |
| host CPU busy (share of the run) | 0.217 | 0.203 | -6.8% (-30.1 to +16.5) | -0.9% (-14.3 to +12.6) | +6.0% (-28.4 to +40.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 386.2 | 353.3 | -8.5% (-38.5 to +21.5) | -1.4% (-17.6 to +14.8) | +7.4% (-34.6 to +49.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.29 | 0.266 | -8.5% (-38.5 to +21.5) | -1.4% (-17.6 to +14.8) | +7.4% (-34.6 to +49.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3 | +3 (+0.516 to +5.48) | +2.33 (+0.899 to +3.77) | +3.33 (+0.465 to +6.2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 1 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,939 | 2,937 | -0.1% (-0.2 to +0.0) | -0.5% (-1.8 to +0.8) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,942 | 2,940 | -0.1% (-0.2 to +0.0) | -0.5% (-1.8 to +0.9) | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.24 | 0.246 | +2.4% (-4.3 to +9.0) | +1.6% (-4.6 to +7.9) | -0.5% (-3.2 to +2.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.396 | 0.41 | +3.5% (-2.6 to +9.5) | +0.8% (-14.6 to +16.3) | +0.7% (-0.9 to +2.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.0759 | 0.0773 | +1.9% (-6.3 to +10.1) | +5.6% (-1.7 to +12.9) | +0.2% (-3.5 to +4.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 503.3 | -1.7% (-1.9 to -1.5) | -2.2% (-4.4 to -0.1) | -1.7% (-2.5 to -0.9) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 406.9 | 396.5 | -2.6% (-5.6 to +0.5) | -1.7% (-5.8 to +2.4) | -1.6% (-5.1 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 262,150 | 268,127 | +2.3% (-10.6 to +15.2) | +1.4% (-0.6 to +3.5) | +5.3% (-10.0 to +20.5) | shown, not judged |
| host CPU busy (share of the run) | 0.0935 | 0.0856 | -8.5% (-143.0 to +126.1) | +1.8% (-63.5 to +67.2) | +3.8% (-30.9 to +38.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 68.7 | 62.3 | -9.2% (-154.1 to +135.6) | +1.1% (-74.6 to +76.8) | +4.2% (-39.0 to +47.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.128 | 0.116 | -9.2% (-154.0 to +135.5) | +1.6% (-75.6 to +78.8) | +4.2% (-39.0 to +47.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +5.33 (+2.46 to +8.2) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,903 | 2,902 | -0.0% (-0.2 to +0.1) | -0.1% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,908 | 2,907 | -0.0% (-0.2 to +0.1) | -0.1% (-0.1 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.301 | 0.301 | -0.1% (-4.7 to +4.4) | -0.4% (-5.0 to +4.2) | +0.3% (-3.2 to +3.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.484 | 0.484 | +0.1% (-9.9 to +10.2) | -0.9% (-2.8 to +1.1) | +0.4% (-5.9 to +6.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.154 | 0.154 | +0.1% (-1.9 to +2.2) | -0.4% (-3.8 to +3.0) | -0.0% (-1.8 to +1.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.7 | -0.6% (-1.2 to -0.1) | -0.6% (-1.0 to -0.2) | -0.7% (-1.4 to +0.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 418.7 | 417.3 | -0.3% (-3.2 to +2.6) | -1.3% (-3.7 to +1.1) | -0.9% (-3.1 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 695,062 | 696,672 | +0.2% (-12.5 to +13.0) | -2.7% (-10.3 to +4.8) | +5.4% (-8.3 to +19.1) | shown, not judged |
| host CPU busy (share of the run) | 0.167 | 0.176 | +5.9% (-21.6 to +33.4) | +22.6% (-28.0 to +73.1) | +5.2% (+3.7 to +6.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 301.0 | 322.0 | +7.0% (-25.7 to +39.6) | +24.5% (-31.2 to +80.1) | +6.3% (+4.9 to +7.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.226 | 0.242 | +7.0% (-25.6 to +39.5) | +24.5% (-31.1 to +80.0) | +6.3% (+4.9 to +7.8) | EVEN, no difference beyond the noise (2 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3.33 | +3.33 (+0.465 to +6.2) | +3.33 (+0.465 to +6.2) | +3.67 (+2.23 to +5.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,757 | 5,747 | -0.2% (-0.4 to +0.0) | -0.0% (-0.4 to +0.3) | +0.1% (-0.1 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,772 | 5,764 | -0.1% (-0.3 to -0.0) | -0.0% (-0.4 to +0.3) | +0.1% (-0.1 to +0.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.321 | 0.321 | +0.2% (-1.0 to +1.4) | +0.0% (-0.6 to +0.6) | -0.2% (-2.3 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.473 | 0.488 | +3.2% (-5.1 to +11.4) | +0.0% (-2.3 to +2.3) | +0.0% (-1.3 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.183 | 0.185 | +0.9% (-1.2 to +3.0) | -0.1% (-0.5 to +0.3) | -0.4% (-2.5 to +1.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 504.1 | -1.5% (-4.0 to +0.9) | -1.4% (-4.0 to +1.3) | -0.6% (-1.2 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 417.7 | 413.0 | -1.1% (-3.0 to +0.8) | -1.1% (-3.9 to +1.7) | -0.6% (-1.3 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 687,488 | 693,772 | +0.9% (-1.7 to +3.5) | +0.5% (-1.4 to +2.5) | +0.5% (-1.5 to +2.5) | shown, not judged |
| host CPU busy (share of the run) | 0.242 | 0.251 | +3.7% (-13.6 to +20.9) | -0.3% (-3.3 to +2.7) | +0.9% (-4.2 to +6.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 435.4 | 457.4 | +5.1% (-18.4 to +28.5) | -0.3% (-4.8 to +4.1) | +1.2% (-5.9 to +8.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.163 | 0.172 | +5.2% (-18.4 to +28.7) | -0.4% (-5.0 to +4.2) | +1.0% (-5.9 to +8.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +4.33 (+2.9 to +5.77) | +4.33 (+2.9 to +5.77) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 2 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run C: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 2 refused).

**Across 4 untouched workloads: 1 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 43 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
