# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

MongoDB as shipped with the operator's WiredTiger cache (512 MB) is native; omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39470845655 | `ac0eeaef8ecc` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39475514914 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39477842603 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning

> not in every run: C lack it.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,915 | 2,913 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.0) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.08%) |
| throughput (operations a second) | 2,918 | 2,916 | -0.0% (-0.1 to +0.1) | -0.1% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 0.268 | 0.267 | -0.4% (-4.6 to +3.9) | -0.7% (-12.5 to +11.1) | +2.9% (-6.4 to +12.3) | **the runs disagree** |
| latency, 99th percentile (ms) | 0.44 | 0.434 | -1.5% (-5.5 to +2.4) | -0.1% (-2.4 to +2.2) | +2.8% (-7.5 to +13.1) | **the runs disagree** |
| latency, mean (ms) | 0.119 | 0.119 | +0.0% (-5.8 to +5.9) | -1.4% (-6.9 to +4.1) | +1.4% (-0.1 to +2.8) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 508.5 | -0.7% (-1.2 to -0.1) | -0.6% (-1.0 to -0.2) | -0.7% (-0.8 to -0.6) | **GAIN in all three of our runs** |
| bytes in the cache, mean (MB) | 416.4 | 414.7 | -0.4% (-3.1 to +2.2) | -0.6% (-1.8 to +0.5) | -0.1% (-1.0 to +0.7) | EVEN, under the floor (the three runs' mean 0.39%) |
| pages read into the cache (misses) | 701,051 | 711,588 | +1.5% (-24.2 to +27.2) | -1.7% (-10.4 to +7.1) | +2.1% (-10.0 to +14.1) | shown, not judged |
| host CPU busy (share of the run) | 0.138 | 0.146 | +5.8% (-50.5 to +62.1) | -12.5% (-28.9 to +3.8) | -5.2% (-33.5 to +23.0) | **the runs disagree** |
| host CPU-seconds | 250.1 | 266.5 | +6.6% (-58.6 to +71.7) | -14.8% (-32.9 to +3.2) | -7.1% (-43.0 to +28.7) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.187 | 0.2 | +6.6% (-58.6 to +71.7) | -14.8% (-32.9 to +3.3) | -7.1% (-42.9 to +28.7) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 3 | +3 (+0.516 to +5.48) | +3.33 (+0.465 to +6.2) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 1 refused); left native (1 trials, 0 allowed, 1 refused); run B: left native (1 trials, 0 allowed, 1 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## burst: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 6 1 8 1 6 × 30.0 s; the operator's cache 512 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,899 | 2,899 | +0.0% (-0.3 to +0.3) | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (operations a second) | 2,905 | 2,906 | +0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to -0.0) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 0.426 | 0.432 | +1.4% (-8.5 to +11.3) | +0.2% (-1.8 to +2.2) | +0.4% (-0.4 to +1.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 0.622 | 0.634 | +1.9% (-5.8 to +9.6) | +0.1% (-6.4 to +6.5) | -1.0% (-8.2 to +6.3) | **the runs disagree** |
| latency, mean (ms) | 0.162 | 0.163 | +0.8% (-7.0 to +8.6) | +0.6% (-1.4 to +2.5) | -1.9% (-10.8 to +7.0) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 512.0 | 496.8 | -3.0% (-3.8 to -2.1) | -6.2% (-14.1 to +1.8) | -1.8% (-2.7 to -0.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| bytes in the cache, mean (MB) | 406.4 | 393.2 | -3.2% (-5.4 to -1.1) | -5.6% (-15.7 to +4.6) | -1.6% (-3.7 to +0.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| pages read into the cache (misses) | 261,304 | 276,274 | +5.7% (-16.9 to +28.3) | +8.1% (-12.4 to +28.5) | +0.4% (-2.7 to +3.4) | shown, not judged |
| host CPU busy (share of the run) | 0.173 | 0.191 | +10.1% (-7.2 to +27.4) | -20.5% (-36.0 to -5.0) | -9.5% (-46.5 to +27.6) | **the runs disagree** |
| host CPU-seconds | 127.1 | 142.8 | +12.4% (-6.9 to +31.7) | -24.2% (-41.2 to -7.3) | -11.9% (-57.8 to +33.9) | **the runs disagree** |
| host CPU-seconds per 1,000 operations inside the line | 0.239 | 0.268 | +12.3% (-7.2 to +31.8) | -24.2% (-41.2 to -7.3) | -12.0% (-57.8 to +33.8) | **the runs disagree** |
| cache size changes written (the knob's moves) | 0 | 4.33 | +4.33 (+1.46 to +7.2) | +4.67 (+3.23 to +6.1) | +4 (+4 to +4) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused); acting: 448 to 512 (2 trials, 1 allowed, 0 refused); run B: acting: 448 to 512 (3 trials, 1 allowed, 1 refused); acting: 448 to 512 (3 trials, 1 allowed, 1 refused); left native (2 trials, 0 allowed, 1 refused); run C: left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused); left native (2 trials, 0 allowed, 2 refused).

## c

> not in every run: B lack it.

## f

> not in every run: B lack it.

**Across 2 untouched workloads: 3 gauge-rows GAIN, 1 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 7 EVEN, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
