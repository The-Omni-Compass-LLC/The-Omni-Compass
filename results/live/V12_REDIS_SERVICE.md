# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39381449955 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39412421481 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39461515383 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,197 | +1.1% (+0.8 to +1.4) | +0.5% (+0.2 to +0.9) | +0.8% (+0.2 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.79 | 0.798 | +1.1% (+0.7 to +1.4) | +0.6% (+0.2 to +0.9) | +0.8% (+0.2 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.65 | 5.66 | +0.2% (-0.5 to +0.9) | +0.1% (-0.1 to +0.3) | -0.2% (-0.9 to +0.5) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.71 | 5.73 | +0.2% (-0.1 to +0.6) | +0.2% (+0.0 to +0.4) | -0.1% (-1.0 to +0.9) | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 1.29 | 1.25 | -2.9% (-5.3 to -0.4) | -1.3% (-2.3 to -0.2) | -2.7% (-5.9 to +0.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 66.0 | +3.1% (+1.1 to +5.1) | +1.0% (+0.1 to +2.0) | +2.3% (-0.5 to +5.1) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.2 | 62.5 | +2.2% (+0.7 to +3.6) | +0.8% (+0.0 to +1.5) | +1.7% (-0.1 to +3.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 137,977 | 133,161 | -3.5% (-4.8 to -2.2) | -1.2% (-3.2 to +0.9) | -2.7% (-5.1 to -0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.122 | 0.122 | +0.1% (-38.6 to +38.7) | +16.9% (-1.0 to +34.9) | -5.4% (-9.8 to -0.9) | **the runs disagree** |
| host CPU-seconds | 213.0 | 212.1 | -0.4% (-43.4 to +42.6) | +19.4% (-0.7 to +39.5) | -5.7% (-11.1 to -0.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.4 | 0.394 | -1.5% (-44.1 to +41.2) | +18.7% (-1.1 to +38.5) | -6.5% (-11.5 to -1.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+16 to +26) | +18.3 (+11.2 to +25.5) | +18.3 (+12.6 to +24.1) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run B: acting: 56 to 72 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 56 to 72 (13 trials, 2 allowed, 0 refused); run C: acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.2 to +0.1) | -0.0% (-0.2 to +0.2) | -0.1% (-0.2 to +0.0) | STEADY, under the floor (the three runs' mean 0.05%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.718 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | -0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 5.76 | 5.76 | -0.0% (-0.1 to +0.0) | -0.0% (-0.2 to +0.1) | +0.1% (-0.0 to +0.2) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.82 | 5.83 | +0.2% (+0.1 to +0.4) | +0.0% (-0.5 to +0.5) | +1.7% (-0.6 to +3.9) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 1.75 | 1.75 | +0.3% (-0.4 to +1.0) | -0.2% (-1.4 to +0.9) | +0.8% (-0.7 to +2.2) | STEADY, under the floor (the three runs' mean 0.29%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 61.4 | -4.0% (-7.9 to -0.1) | -3.2% (-6.0 to -0.5) | -2.5% (-2.8 to -2.2) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 55.5 | -3.0% (-7.3 to +1.4) | -2.0% (-5.1 to +1.2) | -1.2% (-1.6 to -0.7) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,738 | 71,792 | +0.1% (-0.3 to +0.4) | +0.1% (-0.3 to +0.5) | +0.1% (-0.1 to +0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.142 | -1.8% (-74.2 to +70.6) | +5.7% (+2.6 to +8.7) | -1.6% (-90.1 to +86.8) | **the runs disagree** |
| host CPU-seconds | 98.1 | 95.7 | -2.5% (-88.0 to +83.0) | +6.8% (+4.0 to +9.5) | -2.0% (-96.7 to +92.7) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.507 | 0.494 | -2.5% (-87.9 to +82.9) | +6.8% (+3.9 to +9.6) | -1.9% (-96.9 to +93.0) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 8 | +8 (+3.03 to +13) | +7.33 (+1.6 to +13.1) | +6 (+6 to +6) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,266 | 1,287 | +1.6% (+1.4 to +1.9) | +1.0% (+0.8 to +1.2) | +1.0% (+0.4 to +1.6) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.846 | 0.859 | +1.6% (+1.4 to +1.9) | +1.0% (+0.8 to +1.2) | +1.0% (+0.4 to +1.6) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.1% (-0.3 to +0.2) | -0.1% (-0.2 to +0.0) | -0.1% (-0.1 to +0.0) | STEADY, under the floor (the three runs' mean 0.06%) |
| latency, 99th percentile (ms) | 5.27 | 5.27 | -0.1% (-0.7 to +0.5) | +0.0% (+0.0 to +0.0) | +0.1% (-0.0 to +0.2) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 0.891 | 0.817 | -8.4% (-10.0 to -6.7) | -4.3% (-5.1 to -3.5) | -4.1% (-6.6 to -1.5) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | +2.4% (+0.1 to +4.8) | -0.3% (-3.2 to +2.6) | -0.1% (-4.6 to +4.4) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 62.5 | +1.9% (+1.1 to +2.7) | -1.1% (-3.1 to +0.8) | -0.9% (-5.1 to +3.3) | **the runs disagree** |
| keys evicted | 102,969 | 93,778 | -8.9% (-10.0 to -7.8) | -5.2% (-6.3 to -4.1) | -5.2% (-8.5 to -1.9) | shown, not judged |
| host CPU busy (share of the run) | 0.0668 | 0.0733 | +9.7% (-13.7 to +33.1) | +7.0% (-7.1 to +21.2) | +4.9% (-7.7 to +17.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 117.8 | 130.2 | +10.6% (-14.3 to +35.4) | +8.5% (-8.2 to +25.3) | +5.6% (-8.7 to +19.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.207 | 0.225 | +8.8% (-15.6 to +33.1) | +7.5% (-8.9 to +23.9) | +4.5% (-9.2 to +18.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 20.7 | +20.7 (+16.9 to +24.5) | +24.3 (+12.6 to +36.1) | +24.7 (+16.7 to +32.7) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (12 trials, 0 allowed, 3 refused); left native (14 trials, 0 allowed, 3 refused); acting: 64 to 72 (14 trials, 1 allowed, 1 refused); run B: acting: 56 to 72 (14 trials, 2 allowed, 1 refused); acting: 56 to 72 (11 trials, 2 allowed, 3 refused); acting: 56 to 72 (15 trials, 2 allowed, 0 refused); run C: acting: 56 to 72 (11 trials, 2 allowed, 3 refused); acting: 48 to 72 (14 trials, 3 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.6 | 936.7 | +1.2% (+1.0 to +1.4) | +1.3% (+1.2 to +1.3) | +1.3% (+1.2 to +1.5) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.0 to +1.6) | +1.3% (+1.2 to +1.3) | +1.3% (+1.2 to +1.5) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | -0.0% (-0.3 to +0.2) | +0.0% (-0.4 to +0.5) | -0.0% (-0.2 to +0.1) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.74 | 5.81 | +1.2% (-3.6 to +6.0) | +0.1% (-0.2 to +0.4) | +0.1% (-0.1 to +0.3) | STEADY, under the floor (the three runs' mean 0.45%) |
| latency, mean (ms) | 2.26 | 2.23 | -1.6% (-2.6 to -0.7) | -1.9% (-2.5 to -1.3) | -2.0% (-2.3 to -1.6) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+2.0 to +2.3) | +2.2% (+1.8 to +2.5) | +2.2% (+1.9 to +2.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +1.9% (+1.4 to +2.4) | +2.1% (+2.0 to +2.2) | +1.8% (+1.3 to +2.3) | **power given in all three of our runs** |
| keys evicted | 243,186 | 236,889 | -2.6% (-5.9 to +0.7) | -3.5% (-3.6 to -3.3) | -1.8% (-5.4 to +1.7) | shown, not judged |
| host CPU busy (share of the run) | 0.145 | 0.131 | -9.4% (-21.8 to +3.1) | +1.6% (-37.2 to +40.4) | -0.8% (-16.5 to +14.8) | **the runs disagree** |
| host CPU-seconds | 242.9 | 217.2 | -10.6% (-25.3 to +4.2) | +2.0% (-40.8 to +44.8) | -0.9% (-19.2 to +17.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.583 | 0.515 | -11.6% (-26.1 to +2.8) | +0.7% (-41.7 to +43.0) | -2.2% (-20.6 to +16.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 13.7 | +13.7 (+6.08 to +21.3) | +13.7 (+6.08 to +21.3) | +15.3 (+10.2 to +20.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 56 to 80 (12 trials, 3 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 0 refused); run C: acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 56 to 80 (13 trials, 3 allowed, 0 refused).

**Across 3 untouched workloads: 8 gauge-rows GAIN, 1 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
