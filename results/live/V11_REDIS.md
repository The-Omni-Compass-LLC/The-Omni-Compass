# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39149244903 | `d44261ca0c5c` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| B | 39157782849 | `5031411ae285` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |
| C | 39166371110 | `8472aaad2bf4` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,190 | +0.6% (+0.4 to +0.8) | +0.9% (+0.4 to +1.4) | +1.1% (+0.4 to +1.8) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.794 | +0.6% (+0.4 to +0.8) | +0.9% (+0.4 to +1.4) | +1.1% (+0.4 to +1.7) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% (-0.2 to +0.2) | -0.1% (-0.4 to +0.2) | +0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.03%) |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.1% (-0.1 to +0.2) | -0.2% (-0.6 to +0.1) | +0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 1.34 | 1.32 | -1.8% (-2.3 to -1.3) | -3.6% (-5.5 to -1.7) | -3.8% (-6.4 to -1.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.8 | +1.3% (+0.7 to +1.9) | +2.0% (+1.2 to +2.9) | +2.9% (+0.1 to +5.6) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 61.8 | +1.0% (+0.3 to +1.6) | +1.5% (+0.7 to +2.2) | +2.2% (+0.3 to +4.0) | **power given in all three of our runs** |
| keys evicted | 138,223 | 135,967 | -1.6% (-2.5 to -0.8) | -2.8% (-4.7 to -0.9) | -3.5% (-6.1 to -0.9) | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.108 | -9.2% (-50.8 to +32.5) | -2.2% (-74.5 to +70.2) | +16.7% (-127.3 to +160.8) | **the runs disagree** |
| host CPU-seconds | 198.8 | 178.9 | -10.0% (-56.4 to +36.4) | -2.0% (-79.6 to +75.7) | +17.8% (-131.9 to +167.4) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.373 | 0.334 | -10.6% (-56.5 to +35.4) | -2.8% (-80.2 to +74.5) | +16.6% (-132.3 to +165.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 16.3 | +16.3 (+8.74 to +23.9) | +21 (+16 to +26) | +21.7 (+15.9 to +27.4) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.4 to +0.3) | -0.1% (-0.2 to -0.0) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.07%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.4 to +0.3) | -0.1% (-0.2 to +0.0) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 5.66 | 5.65 | -0.2% (-0.7 to +0.3) | +0.0% (-0.2 to +0.3) | -0.0% (-0.3 to +0.3) | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 99th percentile (ms) | 5.73 | 5.72 | -0.1% (-0.4 to +0.3) | +0.3% (-0.4 to +1.0) | +0.1% (-0.3 to +0.6) | STEADY, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 1.66 | 1.65 | -0.3% (-1.9 to +1.3) | +0.7% (-0.6 to +2.0) | +0.2% (-0.1 to +0.6) | STEADY, under the floor (the three runs' mean 0.19%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.5 | -2.3% (-2.7 to -1.8) | -2.6% (-3.1 to -2.0) | -2.4% (-2.8 to -2.0) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% (-1.3 to -0.5) | -1.3% (-2.0 to -0.7) | -1.1% (-1.5 to -0.6) | **GAIN in all three of our runs** |
| keys evicted | 71,704 | 71,798 | +0.1% (-0.8 to +1.0) | +0.2% (+0.1 to +0.4) | +0.1% (-0.2 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.112 | 0.12 | +6.6% (-56.8 to +69.9) | -7.3% (-30.3 to +15.8) | +10.1% (-70.4 to +90.5) | **the runs disagree** |
| host CPU-seconds | 79.4 | 85.4 | +7.5% (-64.6 to +79.6) | -8.3% (-34.7 to +18.1) | +12.2% (-80.6 to +105.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.41 | 0.441 | +7.5% (-64.5 to +79.5) | -8.2% (-34.7 to +18.3) | +12.2% (-80.5 to +105.0) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,286 | +1.5% (+1.0 to +2.0) | +1.4% (+0.0 to +2.7) | +1.6% (+1.6 to +1.7) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.858 | +1.5% (+1.0 to +2.0) | +1.4% (+0.0 to +2.7) | +1.6% (+1.6 to +1.7) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.53 | 5.51 | -0.2% (-0.3 to -0.1) | -0.0% (-0.3 to +0.2) | -0.2% (-0.4 to +0.0) | STEADY, under the floor (the three runs' mean 0.14%) |
| latency, 99th percentile (ms) | 5.62 | 5.62 | -0.0% (-0.2 to +0.2) | +0.1% (-0.1 to +0.3) | +0.1% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 0.964 | 0.897 | -6.9% (-8.8 to -5.0) | -5.8% (-12.3 to +0.6) | -7.4% (-8.0 to -6.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.7 | +1.1% (-0.8 to +2.9) | +1.5% (+0.1 to +2.8) | +1.3% (-0.0 to +2.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 61.6 | +0.5% (-1.1 to +2.2) | +1.1% (+0.1 to +2.0) | +0.8% (+0.2 to +1.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 103,361 | 94,999 | -8.1% (-11.0 to -5.2) | -7.4% (-14.9 to +0.0) | -8.8% (-9.3 to -8.3) | shown, not judged |
| host CPU busy (share of the run) | 0.0999 | 0.107 | +6.9% (-8.8 to +22.7) | -0.7% (-24.2 to +22.8) | +6.5% (-38.5 to +51.5) | **the runs disagree** |
| host CPU-seconds | 174.5 | 188.3 | +7.9% (-9.2 to +25.0) | -0.6% (-27.9 to +26.8) | +7.4% (-42.4 to +57.2) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.306 | 0.325 | +6.3% (-10.3 to +22.9) | -1.9% (-28.6 to +24.7) | +5.7% (-43.4 to +54.8) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 23.0 | +23 (+18.7 to +27.3) | +19.7 (+9.32 to +30) | +22.3 (+19.5 to +25.2) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (13 trials, 0 allowed, 1 refused); left native (12 trials, 0 allowed, 2 refused); run B: acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.8 | 937.2 | +1.2% (+1.0 to +1.4) | +0.7% (-0.5 to +2.0) | +1.2% (+1.1 to +1.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.2% (+1.0 to +1.4) | +0.7% (-0.5 to +2.0) | +1.3% (+1.1 to +1.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.52 | 5.52 | +0.1% (-0.1 to +0.2) | +0.0% (-0.0 to +0.1) | +0.0% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.58 | 5.59 | +0.1% (+0.1 to +0.2) | +0.1% (-0.2 to +0.4) | +0.2% (-0.1 to +0.5) | STEADY, under the floor (the three runs' mean 0.14%) |
| latency, mean (ms) | 2.15 | 2.11 | -1.8% (-2.0 to -1.7) | -1.1% (-3.2 to +1.1) | -1.7% (-1.8 to -1.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.3% (+1.8 to +2.8) | +1.9% (-0.0 to +3.8) | +2.2% (+1.5 to +2.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.4 to +2.5) | +1.4% (-0.4 to +3.2) | +1.9% (+1.5 to +2.4) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 243,068 | 236,934 | -2.5% (-5.9 to +0.9) | -1.7% (-5.6 to +2.2) | -2.6% (-6.1 to +0.9) | shown, not judged |
| host CPU busy (share of the run) | 0.115 | 0.102 | -10.7% (-45.7 to +24.3) | +10.3% (-28.1 to +48.7) | +13.3% (+0.9 to +25.7) | **the runs disagree** |
| host CPU-seconds | 200.9 | 176.8 | -12.0% (-51.0 to +27.1) | +10.8% (-29.9 to +51.5) | +15.7% (+1.6 to +29.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.482 | 0.419 | -13.1% (-52.1 to +26.0) | +10.0% (-29.7 to +49.6) | +14.3% (+0.4 to +28.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 14.0 | +14 (+7.43 to +20.6) | +16 (+5.17 to +26.8) | +14.7 (+10.9 to +18.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run B: left native (10 trials, 0 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 56 to 72 (9 trials, 2 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 0 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 STEADY, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
