# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062231655 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40067530395 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40131350933 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,183 | 1,197 | +1.1% (+0.9 to +1.3) | +0.8% (+0.2 to +1.5) | +1.0% (+0.5 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.789 | 0.798 | +1.1% (+0.9 to +1.3) | +0.8% (+0.2 to +1.5) | +1.0% (+0.4 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.51 | 5.51 | -0.1% (-0.5 to +0.3) | -0.1% (-0.5 to +0.3) | -0.1% (-0.6 to +0.3) | EVEN, under the floor (the three runs' mean 0.11%) |
| latency, 99th percentile (ms) | 5.59 | 5.59 | -0.0% (-0.2 to +0.2) | +0.0% (-0.4 to +0.4) | -0.1% (-0.7 to +0.6) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, mean (ms) | 1.24 | 1.19 | -3.8% (-5.2 to -2.5) | -2.5% (-4.5 to -0.6) | -3.1% (-5.1 to -1.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 66.0 | +3.1% (+1.1 to +5.1) | +1.7% (-0.4 to +3.7) | +1.9% (-0.8 to +4.6) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% (+0.6 to +3.8) | +1.2% (-0.1 to +2.5) | +1.7% (-0.5 to +3.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 138,136 | 133,370 | -3.5% (-4.7 to -2.2) | -2.4% (-5.2 to +0.4) | -3.1% (-5.3 to -0.8) | shown, not judged |
| host CPU busy (share of the run) | 0.107 | 0.102 | -4.9% (-23.6 to +13.9) | -11.3% (-24.9 to +2.4) | -0.1% (-21.7 to +21.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 188.9 | 178.9 | -5.3% (-26.6 to +16.0) | -12.5% (-28.3 to +3.3) | +0.4% (-25.3 to +26.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.355 | 0.332 | -6.4% (-27.3 to +14.6) | -13.2% (-29.1 to +2.7) | -0.6% (-25.8 to +24.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 22.0 | +22 (+15.4 to +28.6) | +21.3 (+11.9 to +30.7) | +18.3 (+10.7 to +25.9) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 56 to 72 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 56 to 72 (14 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,074 | 1,075 | +0.1% (-0.1 to +0.2) | -0.0% (-0.1 to +0.0) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.0) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.1% (-0.2 to +0.1) | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 99th percentile (ms) | 5.24 | 5.25 | +0.1% (-0.7 to +0.9) | -0.0% (-0.1 to +0.1) | +0.1% (-0.2 to +0.5) | EVEN, under the floor (the three runs' mean 0.07%) |
| latency, mean (ms) | 1.53 | 1.54 | +0.1% (-1.0 to +1.1) | -0.1% (-0.7 to +0.6) | +0.4% (-0.5 to +1.3) | EVEN, under the floor (the three runs' mean 0.13%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.7 | -2.0% (-3.4 to -0.6) | -3.3% (-6.2 to -0.5) | -3.0% (-5.7 to -0.4) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.1 | 56.6 | -1.0% (-1.4 to -0.6) | -2.1% (-5.3 to +1.0) | -1.9% (-5.0 to +1.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,719 | 71,742 | +0.0% (-0.3 to +0.4) | +0.2% (-0.1 to +0.4) | +0.2% (+0.0 to +0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0571 | 0.0636 | +11.4% (-232.3 to +255.1) | -1.8% (-28.3 to +24.7) | -9.2% (-34.4 to +16.0) | **the runs disagree** |
| host CPU-seconds | 40.5 | 45.6 | +12.6% (-245.7 to +271.0) | -2.2% (-32.1 to +27.7) | -10.3% (-38.6 to +17.9) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.209 | 0.236 | +12.5% (-246.0 to +270.9) | -2.2% (-32.1 to +27.7) | -10.3% (-38.6 to +18.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 6.67 | +6.67 (+3.8 to +9.54) | +7.33 (+1.6 to +13.1) | +6.67 (+3.8 to +9.54) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (4 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,284 | +1.5% (+0.9 to +2.0) | +1.2% (-0.2 to +2.6) | +1.1% (+0.3 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.858 | +1.6% (+0.8 to +2.3) | +1.2% (-0.2 to +2.6) | +1.1% (+0.3 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% (-0.5 to +0.4) | +0.0% (-0.1 to +0.2) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.0% (-0.7 to +0.7) | +0.2% (+0.0 to +0.3) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 0.885 | 0.824 | -7.0% (-10.2 to -3.7) | -5.0% (-11.5 to +1.5) | -4.6% (-8.3 to -0.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 66.1 | +3.3% (+2.1 to +4.5) | +0.5% (-3.2 to +4.2) | +0.2% (-4.3 to +4.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 62.6 | +2.1% (+0.5 to +3.7) | -0.3% (-5.2 to +4.7) | -0.4% (-5.6 to +4.8) | EVEN, under the floor (the three runs' mean 0.50%) |
| keys evicted | 103,244 | 94,381 | -8.6% (-12.6 to -4.6) | -6.4% (-14.1 to +1.2) | -5.7% (-9.4 to -2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.0514 | 0.0575 | +11.8% (-75.7 to +99.3) | -2.9% (-34.4 to +28.6) | +8.0% (-19.7 to +35.7) | **the runs disagree** |
| host CPU-seconds | 90.0 | 101.2 | +12.5% (-80.0 to +104.9) | -3.1% (-38.8 to +32.6) | +9.4% (-22.0 to +40.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.158 | 0.175 | +10.9% (-81.6 to +103.4) | -4.2% (-40.6 to +32.2) | +8.2% (-23.7 to +40.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.3 | +21.3 (+18.5 to +24.2) | +24 (+6.61 to +41.4) | +23 (+5.79 to +40.2) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 80 (14 trials, 2 allowed, 1 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 2 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 2 refused); acting: 48 to 72 (15 trials, 3 allowed, 1 refused); acting: 56 to 72 (13 trials, 2 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.8 | 938.1 | +1.3% (+1.2 to +1.5) | +1.3% (+1.1 to +1.5) | +1.3% (+1.0 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.626 | +1.3% (+1.2 to +1.5) | +1.3% (+1.1 to +1.5) | +1.3% (+1.1 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.68 | 5.68 | -0.0% (-0.3 to +0.2) | -0.1% (-0.7 to +0.5) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.73 | 5.73 | +0.0% (-0.1 to +0.2) | +0.1% (-0.6 to +0.8) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 2.26 | 2.21 | -2.0% (-2.4 to -1.6) | -1.9% (-3.0 to -0.8) | -2.0% (-2.3 to -1.7) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | +2.5% (+1.4 to +3.6) | +2.3% (+2.1 to +2.5) | +2.6% (+1.6 to +3.6) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.8 | +1.7% (+1.1 to +2.4) | +1.8% (+1.3 to +2.3) | +2.2% (+2.1 to +2.2) | **power given in all three of our runs** |
| keys evicted | 243,128 | 238,495 | -1.9% (-5.2 to +1.4) | -1.8% (-5.2 to +1.6) | -3.1% (-4.6 to -1.5) | shown, not judged |
| host CPU busy (share of the run) | 0.136 | 0.128 | -6.0% (-30.1 to +18.1) | +2.2% (-32.6 to +36.9) | +6.1% (-17.5 to +29.7) | **the runs disagree** |
| host CPU-seconds | 228.5 | 213.0 | -6.8% (-35.0 to +21.4) | +2.9% (-36.4 to +42.2) | +6.5% (-18.6 to +31.7) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.548 | 0.504 | -8.0% (-36.3 to +20.3) | +1.6% (-37.6 to +40.8) | +5.2% (-19.1 to +29.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 16.0 | +16 (+8.55 to +23.5) | +15 (+10.7 to +19.3) | +15 (+10 to +20) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 80 (14 trials, 3 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); run B: acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run C: acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 0 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 EVEN, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
