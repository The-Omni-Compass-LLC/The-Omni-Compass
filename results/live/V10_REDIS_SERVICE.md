# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39109167603 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| B | 39116289213 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |
| C | 39124638850 | `8b902df8d857` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,195 | +1.1% (+0.5 to +1.6) | +1.1% (+0.8 to +1.3) | +1.1% (+0.9 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.789 | 0.798 | +1.1% (+0.5 to +1.6) | +1.1% (+0.8 to +1.4) | +1.1% (+0.8 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.21 | 5.21 | -0.0% (-0.4 to +0.4) | -0.2% (-0.5 to +0.1) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.22%) |
| latency, 99th percentile (ms) | 5.25 | 5.25 | -0.0% (-0.8 to +0.7) | -0.1% (-0.2 to +0.0) | +0.1% (+0.0 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.11%) |
| latency, mean (ms) | 1.17 | 1.12 | -4.2% (-6.1 to -2.2) | -3.9% (-5.2 to -2.6) | -3.7% (-4.4 to -3.0) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.5 | +2.4% (+1.6 to +3.2) | +2.5% (+1.4 to +3.7) | +2.5% (+0.5 to +4.6) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.3 | +1.7% (+1.1 to +2.4) | +1.8% (+0.5 to +3.0) | +1.9% (+0.4 to +3.4) | **power given in all three of our runs** |
| keys evicted | 138,229 | 133,460 | -3.5% (-5.6 to -1.3) | -3.2% (-5.0 to -1.4) | -3.5% (-4.5 to -2.5) | shown, not judged |
| host CPU busy (share of the run) | 0.0676 | 0.0636 | -5.9% (-90.4 to +78.5) | +9.1% (-9.0 to +27.1) | -11.7% (-69.6 to +46.3) | **the runs disagree** |
| host CPU-seconds | 120.7 | 112.7 | -6.6% (-96.5 to +83.3) | +10.3% (-9.6 to +30.2) | -12.6% (-74.2 to +49.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.227 | 0.21 | -7.6% (-97.0 to +81.8) | +9.1% (-10.6 to +28.8) | -13.5% (-74.9 to +47.8) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+16 to +26) | +24 (+21.5 to +26.5) | +21 (+21 to +21) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 1 refused); run B: acting: 56 to 72 (15 trials, 2 allowed, 0 refused); acting: 56 to 72 (12 trials, 2 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (15 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.1% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | -0.1% (-0.4 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.11%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | -0.1% (-0.4 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| latency, 95th percentile (ms) | 5.75 | 5.75 | +0.1% (-0.3 to +0.5) | +0.0% (-0.5 to +0.6) | +0.4% (-1.1 to +1.9) | EVEN, under the floor (every run under 0.5%; the largest 0.38%) |
| latency, 99th percentile (ms) | 5.8 | 5.82 | +0.3% (-0.7 to +1.3) | +0.1% (-1.1 to +1.4) | +0.7% (-1.6 to +3.0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 1.74 | 1.75 | +0.6% (-0.3 to +1.5) | -0.0% (-0.5 to +0.4) | +0.9% (-2.8 to +4.7) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.2 | -2.9% (-7.9 to +2.2) | -2.2% (-3.2 to -1.3) | -2.3% (-2.6 to -1.9) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| memory used, mean (MB) | 57.2 | 56.0 | -2.0% (-6.8 to +2.9) | -0.8% (-2.1 to +0.5) | -0.9% (-1.4 to -0.4) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| keys evicted | 71,703 | 71,795 | +0.1% (-0.3 to +0.6) | +0.1% (-0.3 to +0.4) | +0.3% (-0.5 to +1.1) | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.132 | +0.4% (-14.4 to +15.2) | +0.2% (-95.5 to +95.9) | -4.2% (-17.9 to +9.4) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 87.6 | 87.8 | +0.2% (-16.4 to +16.9) | +0.7% (-101.8 to +103.1) | -5.4% (-20.9 to +10.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.452 | 0.453 | +0.3% (-16.2 to +16.8) | +0.7% (-101.7 to +103.1) | -5.3% (-20.9 to +10.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 7.33 | +7.33 (+1.6 to +13.1) | +5.33 (+2.46 to +8.2) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 1 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,268 | 1,289 | +1.7% (+1.5 to +1.9) | +1.7% (+1.6 to +1.8) | +1.3% (+0.5 to +2.1) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.845 | 0.86 | +1.7% (+1.5 to +1.9) | +1.7% (+1.6 to +1.8) | +1.3% (+0.5 to +2.1) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.49 | 5.5 | +0.3% (-0.9 to +1.4) | -0.1% (-0.6 to +0.3) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.26%) |
| latency, 99th percentile (ms) | 5.65 | 5.67 | +0.2% (-0.4 to +0.9) | +0.0% (-0.1 to +0.2) | +0.1% (-0.1 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.24%) |
| latency, mean (ms) | 0.941 | 0.871 | -7.4% (-8.0 to -6.8) | -7.8% (-8.4 to -7.3) | -5.4% (-8.2 to -2.5) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+1.7 to +2.7) | +2.7% (-0.0 to +5.4) | -0.6% (-7.4 to +6.2) | **the runs disagree** |
| memory used, mean (MB) | 61.3 | 62.4 | +1.8% (+1.6 to +2.0) | +1.9% (-0.0 to +3.8) | -1.3% (-8.2 to +5.6) | **the runs disagree** |
| keys evicted | 103,173 | 93,754 | -9.1% (-10.0 to -8.2) | -9.2% (-9.6 to -8.9) | -6.8% (-11.7 to -1.9) | shown, not judged |
| host CPU busy (share of the run) | 0.0904 | 0.0806 | -10.8% (-70.9 to +49.3) | -9.5% (-71.5 to +52.4) | +9.5% (-25.9 to +44.9) | **the runs disagree** |
| host CPU-seconds | 159.9 | 141.8 | -11.3% (-76.0 to +53.3) | -10.5% (-78.6 to +57.5) | +11.0% (-29.0 to +51.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.28 | 0.244 | -12.8% (-76.1 to +50.5) | -12.0% (-79.4 to +55.4) | +9.5% (-29.1 to +48.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 19.3 | +19.3 (+17.9 to +20.8) | +20.7 (+15.5 to +25.8) | +28.3 (+12.6 to +44.1) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (11 trials, 1 allowed, 3 refused); acting: 64 to 72 (10 trials, 1 allowed, 3 refused); acting: 64 to 72 (12 trials, 1 allowed, 2 refused); run B: acting: 56 to 72 (12 trials, 2 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 2 refused); acting: 56 to 72 (14 trials, 2 allowed, 1 refused); run C: acting: 48 to 64 (16 trials, 2 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 48 to 64 (16 trials, 2 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.8 | 937.3 | +1.2% (+1.1 to +1.4) | +1.3% (+1.0 to +1.5) | +1.2% (+1.2 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.2% (+1.1 to +1.4) | +1.3% (+1.2 to +1.4) | +1.2% (+1.2 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.68 | 5.68 | +0.0% (-0.0 to +0.1) | -0.0% (-0.4 to +0.4) | +0.2% (-0.5 to +1.0) | EVEN, under the floor (every run under 0.5%; the largest 0.23%) |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.2% (+0.1 to +0.2) | +2.7% (-3.5 to +8.8) | +0.3% (-0.3 to +1.0) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| latency, mean (ms) | 2.26 | 2.22 | -1.7% (-1.8 to -1.6) | -1.7% (-3.1 to -0.3) | -1.2% (-3.0 to +0.6) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+1.8 to +2.5) | +2.1% (+1.6 to +2.5) | +2.1% (+1.8 to +2.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.8 | +1.9% (+1.5 to +2.3) | +2.0% (+1.6 to +2.3) | +2.0% (+1.9 to +2.2) | **power given in all three of our runs** |
| keys evicted | 243,066 | 237,940 | -2.1% (-5.2 to +0.9) | -3.1% (-5.1 to -1.0) | -3.4% (-3.5 to -3.4) | shown, not judged |
| host CPU busy (share of the run) | 0.131 | 0.15 | +14.1% (-0.8 to +29.0) | -19.4% (-105.1 to +66.2) | -1.4% (-27.7 to +25.0) | **the runs disagree** |
| host CPU-seconds | 218.0 | 254.5 | +16.7% (-0.6 to +34.0) | -20.7% (-110.9 to +69.6) | -2.2% (-33.6 to +29.2) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.523 | 0.603 | +15.3% (-1.7 to +32.3) | -21.7% (-111.6 to +68.3) | -3.4% (-34.7 to +27.9) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 14.3 | +14.3 (+10.5 to +18.1) | +12 (+9.52 to +14.5) | +13.7 (+7.93 to +19.4) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 80 (11 trials, 2 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 9 gauge-rows GAIN (5 in all three of our runs), 3 LOSS (0 in all three of our runs), 2 power given (2 in all three of our runs), 12 EVEN, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
