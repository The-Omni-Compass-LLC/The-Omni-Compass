# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39367385496 | `15654388e112` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39408770553 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39459224023 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,192 | +0.7% (-0.0 to +1.4) | +1.2% (+1.0 to +1.4) | +1.2% (+1.1 to +1.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.795 | +0.7% (-0.1 to +1.4) | +1.2% (+0.9 to +1.5) | +1.2% (+1.1 to +1.3) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% (-0.7 to +0.5) | +0.1% (-0.1 to +0.3) | -0.1% (-0.7 to +0.5) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.8 | 5.8 | -0.0% (-0.7 to +0.7) | +0.5% (-0.9 to +1.9) | -0.0% (-0.6 to +0.5) | EVEN, under the floor (the three runs' mean 0.14%) |
| latency, mean (ms) | 1.35 | 1.32 | -2.1% (-5.4 to +1.1) | -3.9% (-4.6 to -3.1) | -4.0% (-6.0 to -2.0) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.0 | +1.6% (-0.1 to +3.2) | +2.5% (+2.1 to +2.9) | +2.7% (+1.8 to +3.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.2 | 62.0 | +1.3% (+0.4 to +2.2) | +1.9% (+1.7 to +2.1) | +2.1% (+1.8 to +2.4) | **power given in all three of our runs** |
| keys evicted | 138,187 | 135,372 | -2.0% (-4.9 to +0.8) | -3.9% (-5.0 to -2.8) | -3.9% (-4.3 to -3.5) | shown, not judged |
| host CPU busy (share of the run) | 0.125 | 0.118 | -5.8% (-87.3 to +75.7) | -3.8% (-82.5 to +74.9) | -2.5% (-16.6 to +11.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 209.8 | 195.9 | -6.6% (-98.0 to +84.7) | -3.9% (-86.8 to +78.9) | -2.7% (-18.8 to +13.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.394 | 0.365 | -7.3% (-99.0 to +84.5) | -5.1% (-87.0 to +76.9) | -3.8% (-20.0 to +12.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 17.0 | +17 (+7.06 to +26.9) | +21.7 (+18.8 to +24.5) | +22.3 (+19.5 to +25.2) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.0 to -0.0) | -0.0% (-0.1 to +0.0) | -0.1% (-0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.717 | 0.717 | -0.0% (-0.0 to -0.0) | -0.0% (-0.1 to +0.0) | -0.0% (-0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% (-0.3 to +0.3) | +0.1% (+0.0 to +0.2) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.82 | 5.84 | +0.2% (-0.2 to +0.5) | +0.5% (+0.3 to +0.6) | +0.1% (-0.1 to +0.3) | EVEN, under the floor (the three runs' mean 0.24%) |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% (-0.4 to +0.9) | +0.3% (-0.0 to +0.7) | +0.1% (-0.8 to +1.1) | EVEN, under the floor (the three runs' mean 0.24%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.5 | -2.3% (-3.0 to -1.6) | -2.2% (-2.4 to -2.0) | -2.2% (-2.3 to -2.1) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.6 | -0.9% (-1.6 to -0.2) | -0.9% (-1.0 to -0.8) | -0.8% (-0.9 to -0.7) | **GAIN in all three of our runs** |
| keys evicted | 71,797 | 71,849 | +0.1% (+0.0 to +0.1) | +0.1% (-0.1 to +0.3) | +0.1% (-0.6 to +0.9) | shown, not judged |
| host CPU busy (share of the run) | 0.123 | 0.121 | -1.5% (-59.1 to +56.0) | -5.4% (-49.5 to +38.7) | -9.5% (-32.4 to +13.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 81.4 | 79.8 | -2.0% (-67.5 to +63.4) | -7.2% (-59.6 to +45.1) | -10.8% (-36.9 to +15.2) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.42 | 0.412 | -2.0% (-67.5 to +63.5) | -7.2% (-59.5 to +45.1) | -10.8% (-36.7 to +15.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 5.33 | +5.33 (+2.46 to +8.2) | +6 (+6 to +6) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (2 trials, 0 allowed, 1 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.7% (+1.4 to +1.9) | +0.9% (-1.2 to +2.9) | +1.4% (+0.0 to +2.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.845 | 0.859 | +1.7% (+1.5 to +1.9) | +0.9% (-1.2 to +2.9) | +1.4% (+0.0 to +2.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.66 | 5.66 | -0.1% (-0.2 to +0.0) | -0.1% (-0.2 to +0.1) | -0.1% (-0.1 to -0.0) | EVEN, under the floor (the three runs' mean 0.07%) |
| latency, 99th percentile (ms) | 5.72 | 5.72 | +0.0% (-0.1 to +0.1) | +0.1% (-0.2 to +0.5) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 1.01 | 0.937 | -7.7% (-9.1 to -6.2) | -3.6% (-12.7 to +5.5) | -6.0% (-12.2 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.9 | +1.5% (+1.0 to +1.9) | -0.1% (-2.8 to +2.5) | +0.8% (-1.7 to +3.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 62.1 | +1.3% (+0.8 to +1.8) | -0.4% (-3.2 to +2.3) | +0.4% (-1.5 to +2.3) | EVEN, under the floor (the three runs' mean 0.42%) |
| keys evicted | 103,450 | 94,081 | -9.1% (-10.3 to -7.8) | -4.7% (-15.9 to +6.5) | -7.6% (-15.1 to -0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.124 | 0.114 | -8.3% (-25.7 to +9.1) | -0.5% (-33.0 to +32.0) | +1.6% (-8.2 to +11.4) | **the runs disagree** |
| host CPU-seconds | 214.7 | 195.0 | -9.2% (-28.9 to +10.6) | -0.4% (-37.8 to +37.0) | +1.9% (-9.2 to +13.1) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.376 | 0.336 | -10.7% (-30.5 to +9.1) | -1.3% (-37.5 to +35.0) | +0.5% (-9.5 to +10.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+21 to +21) | +22.3 (+19.5 to +25.2) | +21.7 (+15.9 to +27.4) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); run B: left native (12 trials, 0 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (11 trials, 0 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 920.9 | 933.9 | +1.4% (+1.2 to +1.6) | +1.3% (+1.0 to +1.5) | +1.2% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.626 | +1.4% (+1.2 to +1.5) | +1.3% (+1.0 to +1.5) | +1.2% (+1.2 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.87 | 5.85 | -0.4% (-2.8 to +2.0) | +0.1% (-0.3 to +0.5) | +0.0% (-0.3 to +0.3) | EVEN, under the floor (the three runs' mean 0.11%) |
| latency, 99th percentile (ms) | 7.61 | 7.46 | -2.0% (-7.7 to +3.8) | +0.1% (-0.2 to +0.4) | +0.2% (-0.1 to +0.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 2.36 | 2.3 | -2.3% (-3.7 to -1.0) | -1.8% (-2.8 to -0.8) | -1.7% (-2.2 to -1.2) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.4% (+1.1 to +3.7) | +2.2% (+1.4 to +3.0) | +2.2% (+2.1 to +2.3) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.7 | +1.7% (+1.5 to +1.9) | +1.9% (+1.5 to +2.4) | +2.0% (+2.0 to +2.1) | **power given in all three of our runs** |
| keys evicted | 243,398 | 239,575 | -1.6% (-3.9 to +0.8) | -2.6% (-6.1 to +0.9) | -3.4% (-3.6 to -3.3) | shown, not judged |
| host CPU busy (share of the run) | 0.149 | 0.149 | -0.0% (-16.6 to +16.6) | -2.6% (-10.9 to +5.7) | +2.0% (-8.3 to +12.4) | **the runs disagree** |
| host CPU-seconds | 260.2 | 260.9 | +0.3% (-19.2 to +19.8) | -3.0% (-12.6 to +6.5) | +2.5% (-9.7 to +14.7) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.628 | 0.621 | -1.1% (-20.6 to +18.3) | -4.2% (-14.2 to +5.7) | +1.2% (-11.0 to +13.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 11.7 | +11.7 (+7.87 to +15.5) | +12.7 (+4.68 to +20.7) | +13.7 (+10.8 to +16.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 80 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 12 gauge-rows GAIN, 0 LOSS, 3 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 15 EVEN, 6 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
