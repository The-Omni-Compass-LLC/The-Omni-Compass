# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39108191914 | `6d871e2baad1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |
| B | 39116277778 | `f09db2756842` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |
| C | 39123595298 | `faaaff3142e1` | omni-v10 (digest 4bf39b0d707784de, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 46,379, 42,016, 16,770 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 20,082 | 20,341 | +1.3% (-4.7 to +7.2) | +0.2% (-0.6 to +0.9) | -0.0% (-0.2 to +0.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 20,408 | 20,406 | -0.0% (-0.1 to +0.0) | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| latency, 95th percentile (ms, lag included) | 10.6 | 2.62 | -75.2% (-409.3 to +258.9) | -25.5% (-145.1 to +94.0) | -10.5% (-27.6 to +6.5) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 90.8 | 22.5 | -75.2% (-413.4 to +262.9) | -26.7% (-127.0 to +73.6) | -11.6% (-33.1 to +9.8) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, median (ms) | 0.199 | 0.197 | -0.7% (-4.5 to +3.1) | +0.2% (-4.9 to +5.2) | -0.6% (-2.7 to +1.4) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 3.08 | 0.983 | -68.1% (-376.9 to +240.7) | -21.6% (-103.5 to +60.3) | -6.7% (-19.4 to +6.1) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 16.1 | -18.0% (-32.4 to -3.7) | -9.9% (-17.3 to -2.6) | -6.1% (-14.8 to +2.5) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (-7.4 to +17.4) | +5.0% (+5.0 to +5.0) | +0.0% (+0.0 to +0.0) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.461 | 0.461 | +0.2% (-2.1 to +2.4) | +0.2% (-2.0 to +2.4) | -0.8% (-3.9 to +2.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 796.6 | 799.0 | +0.3% (-2.1 to +2.7) | +0.2% (-2.1 to +2.5) | -0.9% (-4.6 to +2.7) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 0.0882 | 0.0873 | -1.0% (-6.2 to +4.2) | +0.0% (-2.7 to +2.7) | -0.9% (-4.5 to +2.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.74 | 4.15 | +11.0% (+5.9 to +16.0) | +13.6% (+9.9 to +17.4) | +25.7% (+18.4 to +32.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.5 | -17.6% (-32.2 to -3.0) | -9.2% (-15.9 to -2.5) | -5.6% (-6.5 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 14 to 22 (12 trials, 8 allowed, 2 refused); acting: 10 to 20 (13 trials, 10 allowed, 1 refused); acting: 11 to 21 (12 trials, 10 allowed, 1 refused); run B: acting: 15 to 20 (9 trials, 5 allowed, 4 refused); acting: 16 to 21 (10 trials, 5 allowed, 3 refused); acting: 17 to 21 (8 trials, 4 allowed, 4 refused); run C: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 7,615, 7,277, 3,812 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 3,149 | 3,150 | +0.0% (-4.2 to +4.3) | +1.4% (-6.5 to +9.3) | +0.4% (-2.4 to +3.2) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 3,350 | 3,350 | -0.0% (-0.4 to +0.3) | -0.0% (-0.8 to +0.8) | +0.0% (-0.4 to +0.5) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| latency, 95th percentile (ms, lag included) | 92.9 | 114.3 | +23.0% (-138.4 to +184.3) | -61.6% (-401.3 to +278.1) | -3.5% (-38.2 to +31.2) | **the runs disagree** |
| latency, 99th percentile (ms) | 596.7 | 577.1 | -3.3% (-13.9 to +7.4) | -7.2% (-93.3 to +78.9) | -2.1% (-76.5 to +72.3) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, median (ms) | 0.692 | 0.701 | +1.3% (-7.0 to +9.7) | -1.7% (-7.1 to +3.8) | +0.5% (-0.5 to +1.5) | **the runs disagree** |
| latency, mean (ms) | 21.8 | 21.8 | -0.1% (-45.5 to +45.4) | -20.5% (-169.5 to +128.5) | -6.2% (-79.7 to +67.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-6.5 to +6.4) | -1.9% (-6.4 to +2.6) | -3.9% (-6.2 to -1.6) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | +8.3% (+1.2 to +15.5) | +6.7% (-0.5 to +13.8) | **power given** (the same way in all three runs; 1 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.35 | 0.355 | +1.3% (-5.3 to +8.0) | -0.5% (-6.5 to +5.5) | +0.7% (-0.8 to +2.2) | **power given** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| host CPU-seconds | 596.4 | 604.7 | +1.4% (-4.9 to +7.7) | -0.5% (-6.4 to +5.4) | +0.7% (-0.8 to +2.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.421 | 0.427 | +1.3% (-6.8 to +9.5) | -1.9% (-6.6 to +2.7) | +0.3% (-1.1 to +1.7) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.873 | 1.41 | +62.0% (+51.6 to +72.4) | +46.8% (+42.3 to +51.2) | +78.4% (+73.8 to +83.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.2% (-6.0 to +6.4) | -1.5% (-6.2 to +3.1) | -3.3% (-5.1 to -1.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 19 to 21 (14 trials, 2 allowed, 4 refused); acting: 19 to 20 (16 trials, 1 allowed, 4 refused); acting: 20 to 22 (14 trials, 2 allowed, 5 refused); run B: acting: 18 to 21 (18 trials, 3 allowed, 3 refused); acting: 20 to 21 (19 trials, 1 allowed, 2 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused); run C: acting: 19 to 22 (12 trials, 3 allowed, 5 refused); acting: 18 to 20 (10 trials, 2 allowed, 6 refused); acting: 19 to 20 (11 trials, 1 allowed, 6 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,912, 1,898, 1,858 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 826.6 | 835.0 | +1.0% (-5.2 to +7.3) | -0.2% (-1.7 to +1.3) | +0.1% (-0.2 to +0.5) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| throughput (transactions a second) | 839.6 | 839.0 | -0.1% (-0.7 to +0.5) | -0.0% (-0.7 to +0.7) | +0.2% (-0.2 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.17%) |
| latency, 95th percentile (ms, lag included) | 6.84 | 5.42 | -20.8% (-106.6 to +64.9) | +11.6% (-21.5 to +44.7) | +9.4% (-13.1 to +31.8) | **the runs disagree** |
| latency, 99th percentile (ms) | 125.1 | 45.9 | -63.3% (-467.1 to +340.6) | +33.6% (-88.3 to +155.6) | +17.1% (-40.0 to +74.3) | **the runs disagree** |
| latency, median (ms) | 1.89 | 1.87 | -1.0% (-1.5 to -0.4) | +1.1% (-1.8 to +4.1) | +0.5% (-2.0 to +3.0) | **the runs disagree** |
| latency, mean (ms) | 5.99 | 3.23 | -46.0% (-277.5 to +185.4) | +34.5% (-107.9 to +177.0) | +5.2% (-7.3 to +17.8) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.2 | -6.7% (-10.2 to -3.3) | -10.2% (-13.5 to -6.9) | -5.7% (-7.8 to -3.6) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.232 | 0.23 | -1.1% (-2.1 to -0.1) | +1.3% (-1.3 to +4.0) | +0.7% (-1.3 to +2.7) | **the runs disagree** |
| host CPU-seconds | 362.7 | 358.5 | -1.2% (-2.4 to +0.1) | +1.4% (-1.6 to +4.3) | +0.7% (-1.1 to +2.6) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.975 | 0.954 | -2.2% (-9.7 to +5.3) | +1.6% (-2.8 to +5.9) | +0.6% (-1.4 to +2.6) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.759 | 1.48 | +94.6% (+88.9 to +100.3) | +97.0% (+90.2 to +103.7) | +96.2% (+83.1 to +109.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.6% (-6.5 to -4.7) | -8.2% (-16.7 to +0.4) | -4.6% (-6.5 to -2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 17 to 20 (9 trials, 3 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run B: acting: 14 to 20 (10 trials, 6 allowed, 2 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 14 to 20 (11 trials, 6 allowed, 2 refused); run C: acting: 17 to 20 (9 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused).

**Across 3 workloads: 15 gauge-rows GAIN (1 in all three of our runs), 0 LOSS (0 in all three of our runs), 3 power given (0 in all three of our runs), 7 EVEN, 11 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
