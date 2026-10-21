# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39182911063 | `bc2eb38f4ca8` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| B | 39184161631 | `75478eb28444` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |
| C | 39184179710 | `75478eb28444` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 5 |

## tuning: YCSB workloada, 250,000 records × notch; line 1 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,926 | 2,925 | -0.0% (-0.2 to +0.1) | +0.0% (-0.7 to +0.8) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,932 | 2,932 | -0.0% (-0.1 to +0.1) | +0.0% (-0.6 to +0.7) | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.257 | 0.255 | -0.5% (-3.5 to +2.4) | -1.1% (-5.7 to +3.5) | -0.5% (-2.9 to +1.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.432 | 0.429 | -0.7% (-5.6 to +4.2) | -0.8% (-5.0 to +3.5) | +0.7% (-1.5 to +2.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.112 | 0.11 | -1.8% (-5.6 to +1.9) | -1.2% (-4.4 to +2.0) | +0.1% (-4.7 to +4.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 506.2 | -1.1% (-2.7 to +0.4) | -1.3% (-4.2 to +1.6) | -0.7% (-0.7 to -0.7) | EVEN, no difference beyond the noise (2 of 3 runs) |
| bytes in the cache, mean (MB) | 418.4 | 415.3 | -0.8% (-2.7 to +1.2) | -1.1% (-3.8 to +1.6) | -0.3% (-0.6 to -0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 692,291 | 705,918 | +2.0% (-3.1 to +7.0) | -0.0% (-3.0 to +2.9) | +1.2% (+0.3 to +2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.151 | 0.135 | -10.4% (-36.1 to +15.3) | -3.5% (-9.7 to +2.8) | +2.9% (-44.2 to +50.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 277.0 | 244.9 | -11.6% (-40.4 to +17.2) | -4.2% (-11.4 to +3.0) | +4.4% (-53.5 to +62.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.207 | 0.183 | -11.6% (-40.3 to +17.1) | -4.3% (-11.9 to +3.3) | +4.4% (-53.5 to +62.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 3.67 | +3.67 (+2.23 to +5.1) | +4.33 (+2.9 to +5.77) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused).

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,895 | 2,895 | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,900 | 2,899 | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | -0.1% (-0.1 to -0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.332 | 0.329 | -1.0% (-6.8 to +4.8) | -0.2% (-2.6 to +2.2) | +3.0% (-6.8 to +12.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.509 | 0.502 | -1.4% (-8.3 to +5.5) | -0.5% (-1.1 to +0.0) | +0.7% (-0.8 to +2.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.203 | 0.203 | -0.1% (-3.8 to +3.5) | -0.9% (-4.4 to +2.5) | +0.3% (-3.4 to +3.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.7 | -0.7% (-0.7 to -0.7) | -0.8% (-1.4 to -0.3) | -0.4% (-0.5 to -0.2) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 416.1 | 415.1 | -0.2% (-0.8 to +0.3) | -1.4% (-3.9 to +1.2) | -0.7% (-2.5 to +1.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 701,175 | 714,965 | +2.0% (-13.6 to +17.5) | +1.7% (-11.6 to +15.1) | +6.4% (-6.7 to +19.4) | shown, not judged |
| host CPU busy (share of the run) | 0.175 | 0.192 | +9.7% (+1.2 to +18.3) | +9.8% (-39.2 to +58.7) | +1.4% (-21.3 to +24.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds | 294.8 | 330.5 | +12.1% (+1.6 to +22.6) | +11.9% (-48.5 to +72.3) | +1.3% (-25.4 to +28.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.221 | 0.248 | +12.1% (+1.6 to +22.6) | +11.9% (-48.5 to +72.3) | +1.4% (-25.3 to +28.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4 | +4 (+4 to +4) | +3.67 (+2.23 to +5.1) | +2 (+2 to +2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run B: left native (3 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 0 refused); left native (1 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,912 | 2,912 | -0.0% (-0.2 to +0.1) | -0.1% (-0.3 to +0.2) | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 2,919 | 2,918 | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.1) | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.325 | 0.326 | +0.4% (-1.8 to +2.6) | -0.1% (-2.1 to +1.9) | -0.4% (-1.2 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.439 | 0.441 | +0.5% (-11.9 to +12.9) | +0.0% (-3.5 to +3.5) | +0.2% (-1.5 to +1.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.176 | 0.181 | +2.9% (-17.3 to +23.0) | -0.2% (-5.1 to +4.7) | +0.1% (-1.4 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 492.5 | -3.8% (-13.7 to +6.1) | -8.1% (-10.0 to -6.2) | -3.0% (-3.9 to -2.0) | EVEN, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 405.6 | 390.6 | -3.7% (-14.7 to +7.3) | -7.9% (-9.7 to -6.1) | -2.4% (-5.2 to +0.5) | EVEN, no difference beyond the noise (2 of 3 runs) |
| pages read into the cache (misses) | 263,641 | 276,899 | +5.0% (-12.4 to +22.5) | +2.4% (+0.1 to +4.7) | +3.9% (-8.8 to +16.6) | shown, not judged |
| host CPU busy (share of the run) | 0.164 | 0.165 | +0.4% (-31.6 to +32.3) | +17.4% (-15.2 to +50.0) | +3.6% (-32.8 to +39.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 119.3 | 119.6 | +0.3% (-37.0 to +37.6) | +21.4% (-16.7 to +59.6) | +3.6% (-40.6 to +47.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.224 | 0.224 | +0.2% (-37.1 to +37.6) | +21.5% (-16.5 to +59.5) | +3.6% (-40.8 to +47.9) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +5 (+5 to +5) | +4.67 (+3.23 to +6.1) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 448 to 512 (4 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused).

## c: YCSB workloadc, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,897 | 2,896 | -0.0% (-0.1 to +0.0) | -0.1% (-0.1 to -0.0) | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| throughput (operations a second) | 2,902 | 2,900 | -0.1% (-0.1 to +0.0) | -0.1% (-0.1 to -0.0) | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms) | 0.307 | 0.306 | -0.2% (-2.8 to +2.4) | -0.4% (-2.2 to +1.4) | -2.5% (-3.7 to -1.2) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 99th percentile (ms) | 0.534 | 0.517 | -3.1% (-7.8 to +1.6) | -0.8% (-1.9 to +0.3) | -4.2% (-11.0 to +2.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.193 | 0.191 | -1.3% (-3.3 to +0.7) | -0.2% (-2.5 to +2.1) | -0.2% (-5.3 to +5.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 509.4 | -0.5% (-0.9 to -0.0) | -5.2% (-20.6 to +10.2) | -0.4% (-0.7 to -0.2) | EVEN, no difference beyond the noise (1 of 3 runs) |
| bytes in the cache, mean (MB) | 417.3 | 419.6 | +0.6% (-1.5 to +2.6) | -4.8% (-21.8 to +12.2) | -0.2% (-3.2 to +2.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| pages read into the cache (misses) | 687,294 | 728,080 | +5.9% (-10.1 to +21.9) | +1.5% (-19.9 to +22.9) | +1.3% (-14.2 to +16.8) | shown, not judged |
| host CPU busy (share of the run) | 0.176 | 0.147 | -16.3% (-55.3 to +22.7) | -10.4% (-87.1 to +66.3) | -6.1% (-117.6 to +105.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 302.2 | 245.4 | -18.8% (-63.6 to +26.0) | -12.2% (-101.3 to +76.9) | -7.1% (-128.8 to +114.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.227 | 0.184 | -18.8% (-63.7 to +26.0) | -12.2% (-101.4 to +76.9) | -7.1% (-128.7 to +114.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 2.67 | +2.67 (-0.202 to +5.54) | +3.67 (+0.798 to +6.54) | +2 (+2 to +2) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (1 trials, 0 allowed, 1 refused); run B: acting: 448 to 512 (2 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 2 refused); run C: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused).

## f: YCSB workloadf, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 5,818 | 5,812 | -0.1% (-0.3 to +0.1) | -2.2% (-7.0 to +2.6) | -0.3% (-0.9 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (operations a second) | 5,829 | 5,824 | -0.1% (-0.3 to +0.2) | -2.2% (-7.0 to +2.7) | -0.3% (-0.9 to +0.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms) | 0.223 | 0.224 | +0.7% (-1.0 to +2.5) | +0.8% (-1.5 to +3.2) | -0.2% (-2.3 to +2.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 0.416 | 0.427 | +2.6% (-2.5 to +7.8) | +0.9% (-2.5 to +4.3) | -0.9% (-4.3 to +2.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 0.112 | 0.112 | +0.1% (-2.2 to +2.3) | +2.7% (-8.2 to +13.7) | -0.1% (-1.9 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.0 | -0.8% (-0.9 to -0.6) | -0.6% (-0.9 to -0.4) | -0.8% (-1.3 to -0.2) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 418.1 | 416.9 | -0.3% (-0.5 to -0.1) | -0.7% (-1.3 to -0.1) | -0.5% (-1.1 to +0.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| pages read into the cache (misses) | 697,229 | 702,949 | +0.8% (-1.7 to +3.3) | -0.9% (-2.4 to +0.6) | +0.2% (-2.3 to +2.7) | shown, not judged |
| host CPU busy (share of the run) | 0.156 | 0.147 | -5.3% (-32.1 to +21.4) | +3.5% (-8.3 to +15.2) | +0.0% (-12.3 to +12.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 281.3 | 263.9 | -6.2% (-37.8 to +25.4) | +4.8% (-10.3 to +19.9) | +0.1% (-16.6 to +16.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 operations inside the line | 0.105 | 0.0986 | -6.2% (-37.7 to +25.3) | +7.0% (-4.8 to +18.8) | +0.2% (-17.2 to +17.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+2.9 to +5.77) | +4 (+4 to +4) | +4.33 (+2.9 to +5.77) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); run B: left native (2 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 2 refused); left native (3 trials, 0 allowed, 1 refused).

**Across 4 untouched workloads: 2 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 42 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
