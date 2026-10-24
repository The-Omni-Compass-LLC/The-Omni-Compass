# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062224314 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40067523758 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40130173076 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,193 | +0.8% (+0.1 to +1.5) | +1.2% (+1.0 to +1.3) | +0.8% (+0.2 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.796 | +0.8% (+0.1 to +1.5) | +1.1% (+1.0 to +1.3) | +0.8% (+0.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.0% (-0.2 to +0.2) | +0.3% (-0.5 to +1.0) | +0.1% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.12%) |
| latency, 99th percentile (ms) | 5.81 | 5.82 | +0.2% (-0.0 to +0.4) | +1.1% (-1.9 to +4.0) | +0.1% (-0.1 to +0.3) | EVEN, under the floor (the three runs' mean 0.46%) |
| latency, mean (ms) | 1.35 | 1.32 | -2.3% (-4.7 to +0.1) | -3.7% (-4.9 to -2.6) | -2.2% (-4.1 to -0.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.0 | +1.6% (-0.7 to +4.0) | +2.3% (+1.1 to +3.4) | +1.5% (-0.7 to +3.7) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.2 | 62.0 | +1.3% (-0.1 to +2.8) | +1.9% (+1.6 to +2.2) | +1.2% (-0.1 to +2.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 138,215 | 134,753 | -2.5% (-5.0 to +0.0) | -3.8% (-4.2 to -3.3) | -2.3% (-4.7 to +0.0) | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.125 | +0.5% (-23.8 to +24.7) | +28.5% (-40.5 to +97.5) | +4.5% (-26.4 to +35.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 207.4 | 208.7 | +0.6% (-27.0 to +28.2) | +30.1% (-42.7 to +102.8) | +5.2% (-29.4 to +39.7) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.389 | 0.389 | -0.2% (-28.1 to +27.8) | +28.5% (-43.8 to +100.9) | +4.4% (-30.4 to +39.3) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 17.7 | +17.7 (+6.19 to +29.1) | +21 (+16 to +26) | +17.7 (+6.19 to +29.1) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% (-0.4 to +0.3) | -0.1% (-0.2 to -0.0) | -0.1% (-0.1 to -0.1) | EVEN, under the floor (the three runs' mean 0.08%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.4 to +0.3) | -0.1% (-0.2 to -0.0) | -0.1% (-0.1 to -0.1) | EVEN, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 5.55 | 5.55 | -0.0% (-0.1 to +0.0) | +0.1% (-0.1 to +0.2) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% (-0.1 to +0.1) | +0.1% (-0.0 to +0.3) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 1.62 | 1.62 | +0.0% (-0.9 to +1.0) | +0.5% (-0.4 to +1.4) | +0.1% (-0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.22%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.4 | -2.6% (-3.1 to -2.1) | -2.4% (-3.3 to -1.4) | -2.4% (-2.7 to -2.0) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.1 | 56.5 | -1.2% (-1.9 to -0.6) | -1.1% (-2.1 to -0.0) | -1.0% (-1.4 to -0.6) | **GAIN in all three of our runs** |
| keys evicted | 71,742 | 71,804 | +0.1% (-0.9 to +1.0) | +0.3% (+0.1 to +0.6) | +0.2% (+0.1 to +0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.0941 | -10.2% (-111.9 to +91.6) | +3.5% (-97.6 to +104.6) | -1.8% (-50.2 to +46.6) | **the runs disagree** |
| host CPU-seconds | 73.6 | 65.3 | -11.3% (-122.7 to +100.0) | +2.8% (-108.6 to +114.3) | -1.8% (-56.0 to +52.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.38 | 0.337 | -11.3% (-122.4 to +99.7) | +3.0% (-108.6 to +114.5) | -1.8% (-55.9 to +52.4) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% (+0.1 to +2.4) | +1.5% (+0.3 to +2.6) | +1.2% (+0.0 to +2.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.845 | 0.855 | +1.2% (+0.1 to +2.4) | +1.5% (+0.3 to +2.7) | +1.2% (+0.1 to +2.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.75 | 5.74 | -0.1% (-0.3 to +0.2) | -0.1% (-0.6 to +0.3) | +0.0% (-0.4 to +0.5) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.82 | 5.81 | -0.0% (-0.5 to +0.4) | +0.0% (-0.4 to +0.4) | +0.2% (-0.4 to +0.8) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, mean (ms) | 1.06 | 0.998 | -5.5% (-10.0 to -0.9) | -6.2% (-12.0 to -0.5) | -4.7% (-10.7 to +1.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.3 | +0.5% (-0.0 to +1.1) | +0.7% (-1.5 to +2.9) | +0.4% (-0.3 to +1.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| memory used, mean (MB) | 61.3 | 61.4 | +0.1% (-1.1 to +1.3) | +0.4% (-1.5 to +2.3) | +0.2% (-0.6 to +1.0) | EVEN, under the floor (the three runs' mean 0.21%) |
| keys evicted | 103,447 | 96,580 | -6.6% (-12.8 to -0.4) | -7.9% (-14.6 to -1.2) | -6.7% (-12.7 to -0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.113 | 0.123 | +8.8% (-15.4 to +33.0) | -2.2% (-44.8 to +40.5) | +0.0% (-23.3 to +23.4) | **the runs disagree** |
| host CPU-seconds | 187.9 | 207.2 | +10.3% (-17.5 to +38.0) | -2.0% (-50.6 to +46.5) | -0.2% (-26.5 to +26.1) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.33 | 0.359 | +8.9% (-19.1 to +36.9) | -3.4% (-52.6 to +45.8) | -1.4% (-28.1 to +25.4) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.7 | +21.7 (+15.9 to +27.4) | +22 (+19.5 to +24.5) | +21.7 (+18.8 to +24.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (12 trials, 0 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 1 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 926.0 | 937.6 | +1.2% (+1.2 to +1.3) | +1.2% (+1.0 to +1.4) | +1.3% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.2 to +1.3) | +1.2% (+1.0 to +1.4) | +1.3% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.48 | 5.48 | -0.1% (-0.7 to +0.6) | -0.0% (-0.2 to +0.2) | +0.2% (-0.2 to +0.6) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.56 | 5.56 | -0.0% (-0.4 to +0.3) | +0.0% (-0.1 to +0.2) | +0.5% (+0.2 to +0.9) | EVEN, under the floor (the three runs' mean 0.20%) |
| latency, mean (ms) | 2.12 | 2.08 | -1.9% (-2.7 to -1.2) | -1.9% (-2.3 to -1.4) | -1.5% (-1.8 to -1.1) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.3% (+1.7 to +3.0) | +2.3% (+1.9 to +2.7) | +2.2% (+2.1 to +2.3) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 62.0 | +2.2% (+2.0 to +2.3) | +2.1% (+1.9 to +2.2) | +2.0% (+2.0 to +2.0) | **power given in all three of our runs** |
| keys evicted | 243,080 | 234,720 | -3.4% (-3.6 to -3.3) | -3.4% (-3.7 to -3.1) | -3.5% (-3.8 to -3.3) | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.105 | +4.4% (-52.1 to +60.9) | -11.7% (-27.6 to +4.3) | -3.3% (-32.6 to +26.0) | **the runs disagree** |
| host CPU-seconds | 176.1 | 184.5 | +4.8% (-56.8 to +66.4) | -13.0% (-30.6 to +4.5) | -4.4% (-39.9 to +31.2) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.422 | 0.437 | +3.5% (-57.9 to +64.9) | -14.1% (-31.4 to +3.3) | -5.6% (-41.0 to +29.8) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 15.0 | +15 (+15 to +15) | +13 (+8.03 to +18) | +13 (+13 to +13) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 0 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 EVEN, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
