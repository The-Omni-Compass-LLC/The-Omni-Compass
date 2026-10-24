# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40005899721 | `b525b7a07a0c` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| B | 40022515018 | `6fcdf41aad34` | omni-v17 (digest 7c937d09e4031cc7, 55 files) | 4 |
| C | 40037204297 | `6e4b64630bfc` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

> **Warning:** A, B and C are not all on the same engine.

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,195 | +1.0% (+0.4 to +1.5) | +0.8% (+0.3 to +1.3) | +0.8% (+0.3 to +1.2) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.789 | 0.797 | +1.0% (+0.4 to +1.6) | +0.8% (+0.3 to +1.3) | +0.8% (+0.3 to +1.2) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.73 | 5.74 | +0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | +0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.02%) |
| latency, 99th percentile (ms) | 5.79 | 5.79 | +0.1% (-0.2 to +0.4) | +0.1% (-0.2 to +0.5) | +0.1% (-0.1 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.14%) |
| latency, mean (ms) | 1.34 | 1.3 | -2.8% (-4.9 to -0.8) | -2.4% (-4.5 to -0.3) | -2.3% (-4.1 to -0.6) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.3 | +2.1% (+0.3 to +3.8) | +1.2% (-0.0 to +2.5) | +1.9% (+1.0 to +2.7) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| memory used, mean (MB) | 61.2 | 62.2 | +1.6% (+0.1 to +3.2) | +0.9% (+0.4 to +1.4) | +1.3% (+0.6 to +2.1) | **power given in all three of our runs** |
| keys evicted | 138,139 | 133,815 | -3.1% (-5.5 to -0.8) | -2.1% (-3.3 to -0.9) | -2.3% (-3.2 to -1.4) | shown, not judged |
| host CPU busy (share of the run) | 0.114 | 0.129 | +12.7% (-16.8 to +42.1) | +19.8% (+1.0 to +38.7) | +5.1% (-15.4 to +25.6) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU-seconds | 189.9 | 218.0 | +14.8% (-19.1 to +48.8) | +22.6% (+3.2 to +42.0) | +5.9% (-17.7 to +29.5) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU-seconds per 1,000 requests inside the line | 0.356 | 0.405 | +13.8% (-20.4 to +47.9) | +21.6% (+1.6 to +41.6) | +5.1% (-18.6 to +28.8) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| ceiling changes written (the knob's moves) | 0 | 19.7 | +19.7 (+12.1 to +27.3) | +21.7 (+10.5 to +32.9) | +19.3 (+8.13 to +30.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); run B: acting: 56 to 72 (13 trials, 2 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 56 to 72 (13 trials, 2 allowed, 0 refused); run C: acting: 56 to 72 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.1% (-0.2 to +0.0) | -0.1% (-0.2 to -0.0) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.10%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | -0.1% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.1% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | +0.0% (-0.3 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| latency, 99th percentile (ms) | 5.8 | 5.8 | +0.1% (-0.3 to +0.4) | +0.3% (+0.3 to +0.4) | +0.2% (-0.0 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.31%) |
| latency, mean (ms) | 1.74 | 1.74 | +0.5% (-0.3 to +1.3) | +0.6% (-0.3 to +1.4) | +0.5% (-0.1 to +1.1) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.9 | -3.2% (-6.7 to +0.3) | -4.1% (-7.4 to -0.7) | -1.7% (-3.5 to +0.1) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| memory used, mean (MB) | 57.2 | 56.0 | -1.9% (-6.0 to +2.1) | -3.0% (-6.9 to +0.9) | -1.0% (-1.6 to -0.4) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| keys evicted | 71,747 | 71,875 | +0.2% (-0.1 to +0.5) | +0.2% (+0.0 to +0.4) | +0.2% (-0.2 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.14 | 0.135 | -3.0% (-38.3 to +32.3) | +15.0% (-1.8 to +31.9) | +2.0% (-38.2 to +42.2) | **the runs disagree** |
| host CPU-seconds | 94.4 | 90.8 | -3.8% (-44.3 to +36.6) | +17.5% (-1.9 to +36.9) | +1.9% (-45.1 to +48.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.488 | 0.469 | -3.8% (-44.4 to +36.8) | +17.6% (-1.8 to +37.0) | +2.0% (-44.9 to +48.8) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 7.33 | +7.33 (+1.6 to +13.1) | +8 (+3.03 to +13) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 1 refused); left native (3 trials, 0 allowed, 1 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,288 | +1.6% (+1.3 to +2.0) | +1.5% (+1.1 to +2.0) | +1.6% (+0.7 to +2.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.845 | 0.859 | +1.7% (+1.3 to +2.0) | +1.5% (+0.9 to +2.0) | +1.6% (+0.7 to +2.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.5 | 5.48 | -0.2% (-0.6 to +0.2) | +0.1% (-0.3 to +0.5) | -0.3% (-0.9 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.26%) |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% (-0.1 to +0.2) | +1.3% (-3.0 to +5.6) | -0.7% (-2.8 to +1.4) | **the runs disagree** |
| latency, mean (ms) | 0.956 | 0.883 | -7.6% (-10.1 to -5.2) | -7.2% (-9.2 to -5.1) | -8.2% (-11.0 to -5.5) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+1.4 to +3.0) | +3.1% (+1.9 to +4.2) | +3.2% (-2.2 to +8.6) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% (+1.7 to +1.9) | +2.0% (+1.4 to +2.5) | +1.9% (-1.2 to +5.1) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| keys evicted | 103,241 | 93,999 | -9.0% (-10.7 to -7.2) | -8.1% (-10.7 to -5.4) | -8.6% (-13.8 to -3.5) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.103 | -5.9% (-76.7 to +64.9) | -32.0% (-111.4 to +47.5) | -8.1% (-50.0 to +33.8) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds | 194.5 | 181.3 | -6.8% (-84.9 to +71.4) | -33.9% (-118.0 to +50.1) | -8.3% (-52.4 to +35.9) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 requests inside the line | 0.341 | 0.313 | -8.3% (-85.9 to +69.4) | -34.9% (-118.4 to +48.6) | -9.7% (-52.8 to +33.4) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| ceiling changes written (the knob's moves) | 0 | 19.7 | +19.7 (+16.8 to +22.5) | +19 (+14.7 to +23.3) | +21 (+16.7 to +25.3) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); run B: left native (14 trials, 0 allowed, 3 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); run C: left native (12 trials, 0 allowed, 3 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); acting: 64 to 72 (14 trials, 1 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.2 | 937.1 | +1.3% (+1.1 to +1.4) | +1.2% (+0.9 to +1.6) | +1.3% (+1.0 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.1 to +1.4) | +1.2% (+1.0 to +1.5) | +1.3% (+1.0 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.1) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.03%) |
| latency, 99th percentile (ms) | 5.57 | 5.58 | +0.1% (+0.1 to +0.1) | +0.1% (+0.0 to +0.3) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.13%) |
| latency, mean (ms) | 2.14 | 2.1 | -1.9% (-2.2 to -1.6) | -1.8% (-2.2 to -1.4) | -1.9% (-2.2 to -1.7) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | +2.5% (+0.7 to +4.3) | +2.6% (+0.5 to +4.8) | +2.5% (+0.0 to +5.0) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.1 to +2.7) | +2.0% (+1.8 to +2.2) | +2.0% (+1.9 to +2.2) | **power given in all three of our runs** |
| keys evicted | 243,285 | 236,617 | -2.7% (-5.9 to +0.4) | -3.1% (-4.0 to -2.2) | -3.1% (-4.1 to -2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.0997 | -4.4% (-27.6 to +18.7) | +0.9% (-24.0 to +25.8) | +5.3% (-16.3 to +26.8) | **the runs disagree** |
| host CPU-seconds | 181.8 | 172.9 | -4.9% (-30.5 to +20.7) | +1.0% (-27.3 to +29.3) | +6.0% (-17.4 to +29.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.437 | 0.41 | -6.1% (-31.4 to +19.1) | -0.3% (-28.3 to +27.7) | +4.7% (-18.5 to +27.9) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 15.0 | +15 (+1.85 to +28.1) | +14.3 (+3.99 to +24.7) | +15 (+10 to +20) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 56 to 80 (14 trials, 3 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 80 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run C: acting: 56 to 72 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (13 trials, 2 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN (6 in all three of our runs), 1 LOSS (0 in all three of our runs), 4 power given (2 in all three of our runs), 13 EVEN, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
