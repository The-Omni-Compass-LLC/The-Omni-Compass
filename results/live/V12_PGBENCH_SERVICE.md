# PostgreSQL behind PgBouncer, the untouched workloads: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

PostgreSQL as shipped behind PgBouncer's shipped pool of 20 is native; omni is the compass law on the pool size through PgBouncer's own console (`docs/POSTGRES_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed transactions: any rise in any run reads **LOSS in at least one of our runs**. Every row is shown, LOSS included. The host's CPU-seconds are measured on GitHub's shared runner; no energy is claimed.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39473169216 | `ac0eeaef8ecc` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| B | 39477818906 | `fb90309cad0d` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39491674383 | `de8da62736d4` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |

## select (-S, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 15,231, 46,624, 44,401 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 6,700 | 6,703 | +0.1% (-0.1 to +0.2) | -0.5% (-4.7 to +3.8) | -0.4% (-1.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.27%) |
| throughput (transactions a second) | 6,700 | 6,703 | +0.1% (-0.1 to +0.2) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 95th percentile (ms, lag included) | 0.819 | 0.817 | -0.3% (-7.3 to +6.7) | +86.0% (-260.9 to +433.0) | -6.1% (-104.2 to +92.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 1.49 | 1.54 | +3.3% (-19.9 to +26.6) | +1.6% (-105.2 to +108.4) | +91.3% (-201.3 to +383.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 0.339 | 0.338 | -0.2% (-3.7 to +3.3) | +0.7% (-1.2 to +2.6) | +0.2% (-4.3 to +4.6) | EVEN, under the floor (the three runs' mean 0.21%) |
| latency, mean (ms) | 0.422 | 0.43 | +1.8% (-12.6 to +16.3) | +25.8% (-101.2 to +152.7) | +36.0% (-74.0 to +145.9) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.2 | 16.7 | -12.9% (-23.0 to -2.7) | -17.3% (-29.6 to -4.9) | -13.8% (-20.4 to -7.2) | **GAIN in all three of our runs** |
| server connections alive, most at once | 20.0 | 19.0 | -5.0% (-26.5 to +16.5) | +5.0% (+5.0 to +5.0) | +0.0% (+0.0 to +0.0) | **the runs disagree** |
| host CPU busy (share of the run) | 0.37 | 0.369 | -0.1% (-2.8 to +2.7) | +0.3% (-0.7 to +1.3) | -0.0% (-0.9 to +0.9) | EVEN, under the floor (the three runs' mean 0.08%) |
| host CPU-seconds | 619.8 | 619.1 | -0.1% (-2.7 to +2.5) | +0.3% (-0.7 to +1.4) | -0.0% (-0.7 to +0.6) | EVEN, under the floor (the three runs' mean 0.07%) |
| host CPU-seconds per 1,000 transactions inside the line | 0.206 | 0.205 | -0.2% (-2.9 to +2.6) | +0.9% (-2.9 to +4.6) | +0.4% (+0.1 to +0.6) | EVEN, under the floor (the three runs' mean 0.35%) |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.16 | +29.0% (+24.7 to +33.4) | +10.8% (+8.1 to +13.5) | +9.9% (+3.8 to +16.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.3 | -13.6% (-36.0 to +8.7) | -16.0% (-29.4 to -2.7) | -13.5% (-22.8 to -4.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 20 (7 trials, 2 allowed, 5 refused); acting: 14 to 20 (10 trials, 6 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused); run B: acting: 13 to 20 (13 trials, 7 allowed, 3 refused); acting: 16 to 21 (9 trials, 5 allowed, 4 refused); acting: 15 to 21 (10 trials, 6 allowed, 3 refused); run C: acting: 16 to 20 (8 trials, 4 allowed, 4 refused); acting: 15 to 20 (9 trials, 5 allowed, 3 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 4,069, 5,952, 5,663 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,742 | 1,749 | +0.4% (-2.2 to +3.0) | -2.0% (-14.1 to +10.0) | -0.2% (-3.5 to +3.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,789 | 1,790 | +0.1% (-0.4 to +0.5) | -0.2% (-0.7 to +0.3) | +0.0% (-0.5 to +0.5) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms, lag included) | 8.53 | 8.35 | -2.1% (-45.0 to +40.8) | +166.8% (-822.2 to +1155.8) | +6.6% (-88.3 to +101.5) | **the runs disagree** |
| latency, 99th percentile (ms) | 172.5 | 173.3 | +0.5% (-96.7 to +97.6) | +175.1% (-650.5 to +1000.6) | +10.9% (-70.0 to +91.8) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, median (ms) | 1.48 | 1.49 | +0.4% (-1.8 to +2.7) | +4.5% (-7.5 to +16.5) | -0.5% (-6.2 to +5.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 6.27 | 6.13 | -2.2% (-94.7 to +90.3) | +169.7% (-664.9 to +1004.3) | +13.2% (-97.1 to +123.5) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.8 | -5.8% (-8.3 to -3.4) | -0.8% (-10.6 to +9.0) | -2.9% (-8.4 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | +11.7% (-7.3 to +30.6) | +8.3% (+1.2 to +15.5) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.43 | 0.432 | +0.4% (-0.9 to +1.8) | +3.7% (-3.9 to +11.3) | -0.2% (-3.9 to +3.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 734.6 | 738.1 | +0.5% (-0.9 to +1.8) | +3.7% (-4.0 to +11.4) | -0.3% (-4.0 to +3.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 transactions inside the line | 0.937 | 0.938 | +0.1% (-3.8 to +4.0) | +6.0% (-12.8 to +24.8) | -0.1% (-4.2 to +4.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.05 | 1.86 | +76.9% (+74.7 to +79.1) | +75.6% (+69.0 to +82.1) | +56.3% (+49.8 to +62.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-7.8 to -1.9) | -0.6% (-9.3 to +8.0) | -2.0% (-7.4 to +3.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 18 to 20 (15 trials, 2 allowed, 4 refused); acting: 19 to 21 (11 trials, 2 allowed, 5 refused); acting: 19 to 20 (15 trials, 1 allowed, 4 refused); run B: acting: 19 to 21 (18 trials, 2 allowed, 3 refused); acting: 19 to 23 (20 trials, 4 allowed, 3 refused); acting: 19 to 21 (16 trials, 2 allowed, 4 refused); run C: acting: 20 to 21 (17 trials, 1 allowed, 5 refused); acting: 19 to 20 (14 trials, 1 allowed, 4 refused); acting: 19 to 21 (14 trials, 2 allowed, 4 refused).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions a run

Native capacity, unlimited, per run: 3,606, 2,206, 2,291 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (transactions a second answered within the line) | 1,535 | 1,501 | -2.2% (-21.9 to +17.6) | -1.4% (-5.5 to +2.7) | +0.1% (-1.8 to +2.1) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| throughput (transactions a second) | 1,587 | 1,568 | -1.2% (-6.3 to +3.9) | +0.0% (-0.3 to +0.3) | -0.1% (-0.9 to +0.7) | EVEN, under the floor (the three runs' mean 0.43%) |
| latency, 95th percentile (ms, lag included) | 117.1 | 76.2 | -34.9% (-637.7 to +568.0) | +988.5% (-3327.8 to +5304.7) | -3.0% (-22.0 to +16.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 1,334 | 688.7 | -48.4% (-544.6 to +447.8) | +1016.4% (-3143.7 to +5176.6) | -77.4% (-422.4 to +267.6) | **the runs disagree** |
| latency, median (ms) | 0.774 | 0.788 | +1.9% (-3.1 to +6.8) | -1.8% (-6.7 to +3.1) | -0.1% (-1.5 to +1.3) | **the runs disagree** |
| latency, mean (ms) | 44.1 | 24.3 | -45.0% (-548.1 to +458.1) | +592.0% (-1812.4 to +2996.3) | -13.7% (-113.5 to +86.1) | **the runs disagree** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.0 | -4.9% (-6.8 to -3.0) | -8.7% (-18.5 to +1.1) | -15.8% (-27.9 to -3.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (-6.0 to +22.7) | +5.0% (+5.0 to +5.0) | +1.7% (-5.5 to +8.8) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| host CPU busy (share of the run) | 0.226 | 0.228 | +0.9% (+0.2 to +1.6) | -2.0% (-10.4 to +6.4) | -0.2% (-2.4 to +2.1) | **the runs disagree** |
| host CPU-seconds | 390.2 | 393.5 | +0.9% (+0.4 to +1.3) | -1.9% (-10.2 to +6.5) | -0.2% (-2.5 to +2.2) | **the runs disagree** |
| host CPU-seconds per 1,000 transactions inside the line | 0.565 | 0.584 | +3.3% (-17.9 to +24.4) | -0.4% (-11.6 to +10.8) | -0.3% (-4.2 to +3.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.6 | 1.11 | +85.1% (+82.5 to +87.7) | +90.5% (+69.6 to +111.4) | +83.3% (+79.7 to +86.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -4.2% (-6.7 to -1.8) | -6.8% (-16.0 to +2.4) | -14.8% (-21.2 to -8.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 19 to 20 (18 trials, 1 allowed, 4 refused); acting: 17 to 22 (15 trials, 5 allowed, 4 refused); acting: 19 to 20 (9 trials, 1 allowed, 5 refused); run B: acting: 16 to 21 (14 trials, 5 allowed, 3 refused); acting: 18 to 21 (13 trials, 3 allowed, 3 refused); acting: 19 to 20 (11 trials, 1 allowed, 4 refused); run C: acting: 15 to 20 (11 trials, 5 allowed, 4 refused); acting: 16 to 21 (9 trials, 5 allowed, 4 refused); acting: 16 to 20 (8 trials, 4 allowed, 4 refused).

**Across 3 workloads: 3 gauge-rows GAIN, 6 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 11 EVEN, 10 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
