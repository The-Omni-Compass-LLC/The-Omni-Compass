# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39999416157 | `9678c8ad4325` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40020500663 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40035613178 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% (+1.0 to +1.5) | +1.1% (+0.8 to +1.4) | +0.8% (+0.3 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.799 | +1.2% (+1.1 to +1.3) | +1.1% (+0.8 to +1.4) | +0.8% (+0.3 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.0% (-0.3 to +0.4) | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.28 | 5.3 | +0.4% (-2.5 to +3.2) | -0.1% (-0.8 to +0.6) | +0.1% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 1.17 | 1.12 | -4.3% (-6.6 to -2.0) | -3.8% (-5.0 to -2.7) | -2.5% (-4.0 to -1.1) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.9 | +2.9% (+2.5 to +3.3) | +2.5% (+1.8 to +3.1) | +1.9% (+0.2 to +3.6) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% (+1.8 to +2.5) | +1.9% (+1.6 to +2.2) | +1.4% (+0.1 to +2.7) | **power given in all three of our runs** |
| keys evicted | 138,185 | 132,746 | -3.9% (-4.4 to -3.5) | -3.7% (-4.8 to -2.5) | -2.6% (-4.6 to -0.6) | shown, not judged |
| host CPU busy (share of the run) | 0.058 | 0.0692 | +19.4% (-112.9 to +151.6) | +4.6% (-56.5 to +65.6) | -9.8% (-28.3 to +8.6) | **the runs disagree** |
| host CPU-seconds | 102.1 | 123.0 | +20.6% (-120.3 to +161.5) | +5.1% (-59.9 to +70.1) | -11.0% (-32.2 to +10.2) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.192 | 0.229 | +19.1% (-121.0 to +159.3) | +4.0% (-60.5 to +68.4) | -11.7% (-32.5 to +9.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 23.0 | +23 (+23 to +23) | +21.7 (+18.8 to +24.5) | +19.7 (+12.1 to +27.3) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (15 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,075 | 1,074 | -0.1% (-0.2 to +0.0) | +0.1% (-0.0 to +0.2) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.3 to +0.2) | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 5.25 | 5.22 | -0.5% (-1.6 to +0.7) | +0.0% (-0.2 to +0.2) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.15%) |
| latency, 99th percentile (ms) | 5.49 | 5.34 | -2.7% (-7.3 to +2.0) | -0.5% (-4.4 to +3.4) | +0.2% (+0.1 to +0.3) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 1.55 | 1.55 | -0.5% (-1.2 to +0.2) | -0.4% (-1.6 to +0.8) | +0.4% (-0.1 to +0.9) | EVEN, under the floor (the three runs' mean 0.17%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.6 | -2.2% (-2.5 to -2.0) | -2.3% (-2.6 to -2.1) | -2.3% (-2.9 to -1.8) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% (-1.2 to -0.6) | -1.0% (-1.3 to -0.7) | -1.0% (-1.8 to -0.2) | **GAIN in all three of our runs** |
| keys evicted | 71,719 | 71,808 | +0.1% (-0.5 to +0.7) | -0.0% (-0.4 to +0.3) | +0.1% (-0.2 to +0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.0713 | 0.0494 | -30.7% (-102.7 to +41.3) | +12.4% (-120.8 to +145.6) | -8.4% (-40.7 to +24.0) | **the runs disagree** |
| host CPU-seconds | 50.3 | 34.3 | -31.9% (-108.9 to +45.0) | +12.5% (-130.0 to +155.0) | -9.7% (-47.4 to +28.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.26 | 0.177 | -31.9% (-108.8 to +45.1) | +12.4% (-129.8 to +154.7) | -9.7% (-47.4 to +28.0) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,280 | +1.0% (-0.5 to +2.5) | +1.7% (+1.5 to +1.9) | +1.6% (+1.4 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.845 | 0.854 | +1.0% (-0.5 to +2.5) | +1.7% (+1.5 to +1.9) | +1.6% (+1.4 to +1.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.74 | 5.73 | -0.0% (-0.2 to +0.1) | -0.6% (-1.2 to +0.0) | -0.2% (-0.9 to +0.5) | EVEN, under the floor (the three runs' mean 0.27%) |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% (-0.2 to +0.4) | -0.2% (-0.7 to +0.2) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 1.05 | 1 | -4.2% (-10.7 to +2.2) | -8.5% (-9.5 to -7.4) | -7.5% (-9.0 to -6.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.0 | +0.0% (-1.8 to +1.9) | +1.5% (+0.9 to +2.2) | +1.1% (-0.3 to +2.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 61.1 | -0.3% (-2.1 to +1.6) | +1.1% (+0.4 to +1.8) | +0.6% (+0.0 to +1.3) | EVEN, under the floor (the three runs' mean 0.49%) |
| keys evicted | 103,288 | 97,706 | -5.4% (-13.7 to +2.9) | -9.0% (-10.1 to -7.9) | -8.6% (-9.8 to -7.5) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.112 | +2.9% (-29.5 to +35.3) | +1.5% (-59.3 to +62.3) | -6.3% (-40.7 to +28.1) | **the runs disagree** |
| host CPU-seconds | 180.7 | 186.6 | +3.3% (-33.0 to +39.5) | +2.5% (-65.7 to +70.6) | -6.6% (-44.2 to +31.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.317 | 0.324 | +2.3% (-34.8 to +39.4) | +0.8% (-66.8 to +68.3) | -8.1% (-45.1 to +29.0) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 20.3 | +20.3 (+14.6 to +26.1) | +21.7 (+18.8 to +24.5) | +23 (+23 to +23) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (11 trials, 0 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); run B: acting: 56 to 64 (13 trials, 1 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); left native (12 trials, 0 allowed, 1 refused); run C: left native (12 trials, 0 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.5 | 935.8 | +1.1% (+0.5 to +1.8) | +1.2% (+1.0 to +1.3) | +1.3% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.2 to +1.4) | +1.2% (+1.0 to +1.3) | +1.3% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.95 | +4.5% (-15.1 to +24.2) | +0.1% (+0.0 to +0.1) | +0.3% (-1.2 to +1.7) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, 99th percentile (ms) | 5.75 | 6.66 | +16.0% (-52.2 to +84.1) | +0.2% (+0.1 to +0.4) | +0.3% (-0.7 to +1.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 2.26 | 2.28 | +0.6% (-10.1 to +11.4) | -1.6% (-1.9 to -1.3) | -1.6% (-3.1 to -0.1) | **the runs disagree** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+2.1 to +2.3) | +2.2% (+2.1 to +2.4) | +2.4% (+2.2 to +2.7) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.4 to +2.4) | +2.0% (+2.0 to +2.1) | +2.1% (+2.1 to +2.2) | **power given in all three of our runs** |
| keys evicted | 243,204 | 236,799 | -2.6% (-6.3 to +1.0) | -3.3% (-3.6 to -3.1) | -3.4% (-3.7 to -3.2) | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.141 | +0.5% (-57.0 to +58.0) | -2.4% (-19.4 to +14.6) | -7.4% (-24.9 to +10.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 233.7 | 233.0 | -0.3% (-63.4 to +62.8) | -2.9% (-22.6 to +16.9) | -8.5% (-28.7 to +11.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.561 | 0.553 | -1.4% (-64.6 to +61.7) | -4.0% (-23.7 to +15.7) | -9.6% (-29.8 to +10.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 14.0 | +14 (+9.7 to +18.3) | +12.3 (+9.46 to +15.2) | +13.7 (+10.8 to +16.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 2 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 EVEN, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
