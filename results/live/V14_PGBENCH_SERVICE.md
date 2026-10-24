# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39625603596 | `e32bbb605501` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 3 |
| B | 39628245625 | `990711a99dc4` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 3 |
| C | 39630669154 | `67b7cd6bf1e8` | omni-v14 (digest 7afba44615fcff8f, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 15,805, 16,528, 33,899 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6,950 | 6,949 | -0.0% (-0.3 to +0.3) | -0.0% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.05%) |
| throughput (transactions a second) | 6,950 | 6,949 | -0.0% (-0.3 to +0.3) | -0.0% (-0.3 to +0.2) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.05%) |
| latency, 95th percentile (ms, lag included) | 0.852 | 0.894 | +4.9% (-10.9 to +20.8) | -9.4% (-16.3 to -2.4) | +13.6% (-7.4 to +34.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 1.63 | 1.92 | +17.9% (-44.7 to +80.6) | +8.0% (-21.0 to +37.0) | +54.6% (-25.4 to +134.7) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, median (ms) | 0.339 | 0.341 | +0.7% (-1.2 to +2.5) | -1.4% (-2.5 to -0.4) | +2.1% (-3.1 to +7.2) | **the runs disagree** |
| latency, mean (ms) | 0.425 | 0.449 | +5.6% (-4.5 to +15.7) | +8.0% (-7.9 to +23.9) | +17.0% (-5.3 to +39.4) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 16.8 | -15.1% (-29.2 to -1.1) | -9.7% (-23.7 to +4.2) | -12.1% (-37.6 to +13.4) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.378 | 0.379 | +0.4% (-0.8 to +1.6) | -2.2% (-3.8 to -0.6) | +3.1% (-3.8 to +10.0) | **the runs disagree** |
| host CPU-seconds | 633.4 | 635.8 | +0.4% (-0.8 to +1.5) | -2.5% (-4.2 to -0.8) | +3.2% (-3.6 to +10.1) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.203 | 0.203 | +0.4% (-0.5 to +1.2) | -2.4% (-4.4 to -0.5) | +3.2% (-3.5 to +9.9) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.48 | 3.22 | +29.5% (+26.6 to +32.5) | +26.4% (+24.4 to +28.3) | +23.2% (+14.8 to +31.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.5% (-31.8 to +8.8) | -10.0% (-23.9 to +4.0) | -11.2% (-35.4 to +13.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 12 to 20 (12 trials, 8 allowed, 3 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run C: acting: 17 to 20 (8 trials, 3 allowed, 4 refused); acting: 19 to 20 (7 trials, 1 allowed, 5 refused); acting: 13 to 20 (10 trials, 7 allowed, 3 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,704, 4,590, 3,809 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,590 | 1,589 | -0.1% (-2.4 to +2.2) | +0.4% (-1.8 to +2.6) | -0.0% (-4.3 to +4.2) | EVEN, under the floor (every run under 0.5%; the largest 0.43%) |
| throughput (transactions a second) | 1,631 | 1,629 | -0.1% (-0.3 to +0.1) | +0.0% (-0.2 to +0.3) | -0.1% (-0.8 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| latency, 95th percentile (ms, lag included) | 7.11 | 6.5 | -8.5% (-57.1 to +40.0) | -7.8% (-34.5 to +18.9) | +2.6% (-102.9 to +108.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 180.9 | 181.9 | +0.5% (-54.1 to +55.2) | -7.6% (-71.6 to +56.5) | -5.0% (-111.4 to +101.3) | **the runs disagree** |
| latency, median (ms) | 1.52 | 1.53 | +0.7% (+0.4 to +1.0) | -0.2% (-2.9 to +2.5) | +0.1% (-1.5 to +1.8) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| latency, mean (ms) | 6.22 | 6.18 | -0.6% (-67.0 to +65.9) | -10.8% (-73.1 to +51.5) | -0.4% (-123.0 to +122.2) | **GAIN** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 0 of 3 clear of the noise) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.0 | -4.6% (-8.7 to -0.5) | -3.7% (-7.4 to +0.1) | -5.4% (-7.1 to -3.6) | **GAIN** (the same way in all three runs; 2 of 3 clear of the noise) |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | +8.3% (+1.2 to +15.5) | +6.7% (-0.5 to +13.8) | **power given** (the same way in all three runs; 2 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.33 | 0.333 | +0.9% (+0.2 to +1.7) | -0.0% (-2.1 to +2.0) | -0.1% (-1.2 to +1.1) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| host CPU-seconds | 496.7 | 501.4 | +0.9% (+0.2 to +1.7) | -0.0% (-2.1 to +2.1) | -0.1% (-1.5 to +1.3) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 1 of 3 clear of the noise) |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.701 | +1.0% (-0.7 to +2.7) | -0.4% (-1.5 to +0.6) | -0.1% (-5.7 to +5.5) | **power given** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | +78.3% (+73.2 to +83.4) | +69.4% (+68.6 to +70.2) | +79.3% (+74.4 to +84.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -3.9% (-6.5 to -1.2) | -2.7% (-6.5 to +1.1) | -4.3% (-5.7 to -2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 22 (17 trials, 4 allowed, 2 refused); acting: 19 to 21 (13 trials, 2 allowed, 3 refused); acting: 19 to 20 (14 trials, 1 allowed, 4 refused); run B: acting: 18 to 21 (16 trials, 3 allowed, 3 refused); acting: 19 to 21 (13 trials, 2 allowed, 3 refused); left native (13 trials, 0 allowed, 4 refused); run C: acting: 18 to 21 (16 trials, 3 allowed, 3 refused); acting: 18 to 20 (13 trials, 2 allowed, 4 refused); acting: 18 to 20 (15 trials, 2 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,912, 1,906, 3,284 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 840.8 | 839.7 | -0.1% (-0.7 to +0.4) | -0.1% (-0.8 to +0.5) | +0.4% (-0.1 to +1.0) | EVEN, under the floor (every run under 0.5%; the largest 0.41%) |
| throughput (transactions a second) | 841.6 | 841.1 | -0.1% (-0.3 to +0.1) | -0.1% (-0.5 to +0.3) | +0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.09%) |
| latency, 95th percentile (ms, lag included) | 5.94 | 6.19 | +4.1% (-38.9 to +47.1) | +12.2% (+9.5 to +14.9) | -20.4% (-54.8 to +13.9) | **the runs disagree** |
| latency, 99th percentile (ms) | 23.7 | 24.8 | +4.4% (-47.0 to +55.7) | +26.6% (-15.9 to +69.0) | -57.2% (-141.1 to +26.7) | **the runs disagree** |
| latency, median (ms) | 1.89 | 1.9 | +0.3% (-0.7 to +1.3) | +1.0% (-0.1 to +2.1) | -1.2% (-2.8 to +0.3) | **the runs disagree** |
| latency, mean (ms) | 2.85 | 2.96 | +4.0% (-21.6 to +29.6) | +6.6% (-4.9 to +18.2) | -23.3% (-56.6 to +10.1) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 16.9 | -14.9% (-26.9 to -2.8) | -10.7% (-24.8 to +3.3) | -5.2% (-11.2 to +0.7) | **GAIN** (the same way in all three runs; 1 of 3 clear of the noise) |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | +1.7% (-5.5 to +8.8) | +10.0% (-2.4 to +22.4) | **power given** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU busy (share of the run) | 0.233 | 0.235 | +0.7% (-1.8 to +3.1) | +1.5% (+0.3 to +2.6) | -1.5% (-3.7 to +0.6) | **the runs disagree** |
| host CPU-seconds | 363.5 | 366.1 | +0.7% (-1.8 to +3.2) | +1.5% (+0.4 to +2.7) | -1.5% (-3.5 to +0.5) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.961 | 0.969 | +0.8% (-1.8 to +3.4) | +1.7% (+0.9 to +2.4) | -1.9% (-3.7 to -0.1) | **the runs disagree** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.771 | 1.56 | +102.2% (+96.4 to +108.0) | +96.5% (+89.2 to +103.8) | +77.8% (+68.6 to +87.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.4 | -12.8% (-26.4 to +0.9) | -8.6% (-23.7 to +6.4) | -4.3% (-9.7 to +1.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 13 to 21 (12 trials, 8 allowed, 2 refused); acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 17 to 20 (8 trials, 3 allowed, 4 refused); run B: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 19 to 21 (8 trials, 2 allowed, 5 refused); run C: acting: 18 to 22 (12 trials, 4 allowed, 3 refused); acting: 19 to 20 (10 trials, 1 allowed, 5 refused); acting: 17 to 22 (11 trials, 5 allowed, 5 refused).

**Across 3 workloads: 4 gauge-rows GAIN (0 in all three of our runs), 3 LOSS (0 in all three of our runs), 5 power given (0 in all three of our runs), 10 EVEN, 14 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
