# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39182915425 | `bc2eb38f4ca8` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| B | 39184166001 | `75478eb28444` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |
| C | 39185403353 | `ce92ff888e73` | omni-v11 (digest 745aa53ec8eeb67b, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 26,433, 26,132, 39,585 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 11,537 | 11,625 | +0.8% (-2.6 to +4.1) | -0.0% (-0.1 to +0.1) | -0.5% (-1.8 to +0.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 11,625 | 11,625 | +0.0% (-0.1 to +0.1) | -0.0% (-0.1 to +0.1) | +0.0% (-0.0 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 3.99 | 2.83 | -29.0% (-258.1 to +200.0) | -1.2% (-34.8 to +32.5) | +5.5% (-37.6 to +48.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 59.8 | 7.7 | -87.1% (-478.8 to +304.6) | +8.4% (-63.0 to +79.8) | +1884.6% (-4534.3 to +8303.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 0.255 | 0.254 | -0.4% (-3.8 to +3.0) | +0.1% (-0.4 to +0.7) | +0.9% (-4.9 to +6.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 1.89 | 0.644 | -66.0% (-375.3 to +243.4) | +15.2% (-37.3 to +67.7) | +255.7% (-313.9 to +825.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.3 | 15.8 | -18.3% (-30.4 to -6.1) | -19.8% (-26.8 to -12.9) | -21.8% (-30.3 to -13.3) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | +5.0% (+5.0 to +5.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (2 of 3 runs) |
| host CPU busy (share of the run) | 0.439 | 0.437 | -0.3% (-3.5 to +2.9) | -0.0% (-0.3 to +0.2) | +0.9% (-5.6 to +7.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 753.3 | 751.2 | -0.3% (-4.1 to +3.5) | -0.0% (-0.1 to +0.1) | +0.9% (-5.3 to +7.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.144 | -1.0% (-7.9 to +5.8) | +0.0% (-0.1 to +0.1) | +1.4% (-4.0 to +6.8) | EVEN, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.96 | 3.63 | +22.5% (+11.9 to +33.1) | +17.6% (+15.0 to +20.2) | +19.1% (+14.5 to +23.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.4 | -18.0% (-23.8 to -12.2) | -19.1% (-25.2 to -13.0) | -22.0% (-36.6 to -7.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 13 to 20 (11 trials, 7 allowed, 4 refused); acting: 15 to 20 (10 trials, 5 allowed, 4 refused); acting: 14 to 20 (10 trials, 6 allowed, 4 refused); run B: acting: 12 to 21 (13 trials, 9 allowed, 3 refused); acting: 13 to 21 (12 trials, 8 allowed, 4 refused); acting: 15 to 21 (11 trials, 6 allowed, 3 refused); run C: acting: 15 to 20 (11 trials, 5 allowed, 3 refused); acting: 12 to 20 (11 trials, 8 allowed, 2 refused); acting: 14 to 20 (11 trials, 6 allowed, 3 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,847, 3,938, 3,861 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,641 | 1,637 | -0.2% (-6.1 to +5.6) | -0.1% (-4.2 to +4.0) | +0.1% (-2.1 to +2.2) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 1,692 | 1,691 | -0.1% (-0.7 to +0.6) | -0.1% (-0.1 to +0.0) | -0.1% (-0.4 to +0.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 13.9 | 18.5 | +33.0% (-427.7 to +493.7) | +16.0% (-128.1 to +160.1) | -6.7% (-33.9 to +20.4) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 197.9 | 216.3 | +9.3% (-109.8 to +128.5) | -3.9% (-112.3 to +104.6) | -10.3% (-72.9 to +52.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.58 | 1.58 | +0.4% (-4.0 to +4.7) | -0.5% (-2.7 to +1.8) | +0.1% (-1.3 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 7.46 | 8.12 | +8.8% (-169.0 to +186.7) | +5.2% (-120.6 to +131.0) | -5.8% (-57.6 to +46.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.5% (-6.7 to -0.2) | -7.2% (-10.6 to -3.8) | -3.9% (-8.0 to +0.1) | EVEN, no difference beyond the noise (1 of 3 runs) |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +5.0% (+5.0 to +5.0) | +8.3% (+1.2 to +15.5) | EVEN, no difference beyond the noise (1 of 3 runs) |
| host CPU busy (share of the run) | 0.349 | 0.351 | +0.4% (-3.9 to +4.7) | -0.3% (-1.3 to +0.7) | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 526.7 | 529.3 | +0.5% (-4.4 to +5.4) | -0.3% (-1.3 to +0.6) | +0.1% (-0.3 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.713 | 0.719 | +0.7% (-8.6 to +10.0) | -0.2% (-3.8 to +3.4) | +0.1% (-2.5 to +2.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.82 | +77.3% (+76.5 to +78.1) | +75.7% (+72.8 to +78.5) | +76.8% (+72.1 to +81.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -2.8% (-6.6 to +0.9) | -5.8% (-10.4 to -1.2) | -2.5% (-6.2 to +1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 21 (14 trials, 2 allowed, 6 refused); acting: 19 to 21 (16 trials, 2 allowed, 4 refused); acting: 19 to 20 (13 trials, 1 allowed, 5 refused); run B: acting: 17 to 21 (17 trials, 4 allowed, 4 refused); acting: 19 to 20 (12 trials, 1 allowed, 5 refused); acting: 19 to 20 (14 trials, 1 allowed, 3 refused); run C: acting: 18 to 21 (16 trials, 3 allowed, 4 refused); acting: 19 to 21 (11 trials, 2 allowed, 5 refused); left native (12 trials, 0 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 1,914, 1,923, 1,874 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 840.5 | 840.3 | -0.0% (-1.0 to +0.9) | +0.2% (-0.1 to +0.4) | +0.2% (-0.7 to +1.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| throughput (transactions a second) | 841.9 | 841.0 | -0.1% (-0.6 to +0.4) | +0.2% (+0.0 to +0.4) | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| latency, 95th percentile (ms, lag included) | 6.02 | 5.63 | -6.5% (-94.9 to +82.0) | +1.2% (-4.0 to +6.5) | -3.9% (-70.4 to +62.7) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, 99th percentile (ms) | 18.4 | 15.3 | -16.8% (-219.5 to +185.9) | +4.2% (-8.0 to +16.4) | -18.7% (-271.5 to +234.1) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, median (ms) | 1.93 | 1.94 | +0.8% (-6.0 to +7.6) | +0.8% (-1.3 to +2.9) | -0.2% (-1.0 to +0.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| latency, mean (ms) | 2.78 | 2.72 | -2.3% (-50.1 to +45.5) | +2.4% (+0.4 to +4.5) | -4.3% (-60.1 to +51.4) | EVEN, no difference beyond the noise (2 of 3 runs) |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 17.5 | -9.9% (-14.4 to -5.3) | -11.9% (-19.9 to -4.0) | -15.6% (-23.4 to -7.8) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU busy (share of the run) | 0.239 | 0.241 | +0.9% (-7.2 to +9.1) | +0.8% (-1.1 to +2.7) | -0.2% (-1.6 to +1.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds | 372.8 | 376.5 | +1.0% (-7.6 to +9.5) | +0.8% (-1.2 to +2.8) | -0.2% (-2.1 to +1.6) | EVEN, no difference beyond the noise (3 of 3 runs) |
| host CPU-seconds per 1,000 transactions inside the line | 0.986 | 0.996 | +1.0% (-8.5 to +10.5) | +0.6% (-1.6 to +2.9) | -0.4% (-3.1 to +2.3) | EVEN, no difference beyond the noise (3 of 3 runs) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.772 | 1.51 | +96.1% (+85.6 to +106.5) | +97.0% (+96.5 to +97.6) | +97.2% (+87.8 to +106.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.1% (-19.3 to +1.1) | -11.7% (-17.2 to -6.2) | -13.5% (-22.8 to -4.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 17 to 21 (9 trials, 4 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 18 to 20 (7 trials, 2 allowed, 5 refused); run B: acting: 17 to 21 (9 trials, 4 allowed, 5 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 17 to 20 (7 trials, 3 allowed, 4 refused); run C: acting: 15 to 20 (10 trials, 5 allowed, 3 refused); acting: 18 to 20 (8 trials, 2 allowed, 4 refused); acting: 16 to 20 (9 trials, 4 allowed, 3 refused).

**Across 3 workloads: 2 gauge-rows GAIN in all three of our runs, 0 LOSS, 0 power given, 34 EVEN, 0 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
