# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39823820262 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39844642925 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39862248686 | `681ff70efadd` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,193 | +1.0% (+0.6 to +1.4) | +1.1% (+0.6 to +1.6) | +0.8% (+0.1 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.797 | +1.0% (+0.6 to +1.4) | +1.1% (+0.6 to +1.6) | +0.8% (+0.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.23 | 5.22 | -0.0% (-0.4 to +0.3) | -0.3% (-1.3 to +0.7) | +0.1% (-0.6 to +0.8) | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 99th percentile (ms) | 5.31 | 5.31 | -0.1% (-3.4 to +3.3) | -5.1% (-26.9 to +16.7) | +0.2% (-0.6 to +1.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.18 | 1.14 | -3.3% (-5.4 to -1.2) | -4.9% (-9.5 to -0.2) | -2.3% (-5.2 to +0.6) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.7 | +2.6% (+1.9 to +3.3) | +2.3% (+0.4 to +4.2) | +1.7% (+0.4 to +2.9) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.4 | +1.9% (+1.7 to +2.2) | +1.8% (+0.3 to +3.3) | +1.2% (+0.4 to +2.0) | **power given in all three of our runs** |
| keys evicted | 138,213 | 133,839 | -3.2% (-4.6 to -1.7) | -3.6% (-5.5 to -1.7) | -2.2% (-4.5 to +0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.0557 | 0.0714 | +28.2% (+1.9 to +54.4) | +7.0% (-15.5 to +29.5) | -2.0% (-9.3 to +5.4) | **the runs disagree** |
| host CPU-seconds | 96.9 | 126.5 | +30.5% (+1.5 to +59.5) | +7.9% (-16.5 to +32.3) | -2.4% (-11.6 to +6.9) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.182 | 0.235 | +29.2% (+1.1 to +57.4) | +6.7% (-17.7 to +31.1) | -3.1% (-11.9 to +5.6) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 20.3 | +20.3 (+12.7 to +27.9) | +21 (+16 to +26) | +19 (+5.85 to +32.1) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 56 to 72 (11 trials, 2 allowed, 1 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,077 | 1,076 | -0.1% (-0.3 to +0.1) | -0.1% (-0.2 to +0.1) | -0.0% (-0.3 to +0.2) | STEADY, under the floor (the three runs' mean 0.07%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.1% (-0.2 to +0.1) | -0.1% (-0.2 to +0.1) | -0.0% (-0.2 to +0.2) | STEADY, under the floor (the three runs' mean 0.07%) |
| latency, 95th percentile (ms) | 5.59 | 5.58 | -0.0% (-0.5 to +0.4) | +0.0% (-0.1 to +0.1) | +0.1% (-0.2 to +0.5) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.68 | 5.68 | +0.1% (-0.1 to +0.2) | +0.2% (+0.1 to +0.2) | +0.4% (-0.6 to +1.3) | STEADY, under the floor (the three runs' mean 0.19%) |
| latency, mean (ms) | 1.6 | 1.61 | +0.2% (-0.3 to +0.7) | +0.4% (+0.1 to +0.7) | +0.5% (-0.7 to +1.8) | STEADY, under the floor (the three runs' mean 0.38%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.6 | -2.2% (-2.7 to -1.8) | -3.2% (-6.0 to -0.5) | -3.1% (-5.9 to -0.3) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.2 | 56.7 | -0.9% (-1.4 to -0.3) | -2.1% (-5.3 to +1.2) | -1.8% (-4.9 to +1.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,590 | 71,774 | +0.3% (-0.2 to +0.7) | +0.2% (-0.1 to +0.6) | +0.1% (-0.5 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.082 | 0.0943 | +14.9% (-22.9 to +52.8) | +8.5% (-25.9 to +43.0) | +19.3% (-18.2 to +56.8) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 57.3 | 66.6 | +16.3% (-25.9 to +58.5) | +9.6% (-29.6 to +48.9) | +22.2% (-21.1 to +65.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.295 | 0.344 | +16.4% (-25.7 to +58.6) | +9.7% (-29.6 to +49.0) | +22.3% (-20.9 to +65.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6.67 (+3.8 to +9.54) | +7.33 (+1.6 to +13.1) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,264 | 1,282 | +1.4% (+1.0 to +1.7) | +1.8% (+1.5 to +2.0) | +1.8% (+1.7 to +1.8) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.857 | +1.5% (+1.1 to +1.8) | +1.8% (+1.5 to +2.0) | +1.8% (+1.7 to +1.8) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.23 | 5.23 | -0.0% (-0.2 to +0.2) | -0.3% (-0.4 to -0.1) | -0.2% (-1.0 to +0.5) | STEADY, under the floor (the three runs' mean 0.17%) |
| latency, 99th percentile (ms) | 5.29 | 5.29 | -0.1% (-1.1 to +1.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.7 to +0.6) | STEADY, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 0.901 | 0.842 | -6.5% (-8.3 to -4.7) | -8.3% (-8.6 to -8.1) | -8.2% (-10.1 to -6.4) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | +2.5% (-0.4 to +5.5) | +2.4% (-1.1 to +5.9) | +2.3% (+1.6 to +3.0) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 62.2 | +1.5% (+0.1 to +3.0) | +1.8% (-0.4 to +4.0) | +1.9% (+1.7 to +2.0) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 103,499 | 95,271 | -7.9% (-9.8 to -6.1) | -9.6% (-11.2 to -8.0) | -9.5% (-9.9 to -9.0) | shown, not judged |
| host CPU busy (share of the run) | 0.0732 | 0.0753 | +2.8% (-26.1 to +31.8) | -5.6% (-39.7 to +28.5) | +10.4% (-7.8 to +28.5) | **the runs disagree** |
| host CPU-seconds | 129.7 | 133.5 | +2.9% (-28.2 to +34.0) | -6.0% (-43.9 to +31.9) | +11.9% (-7.6 to +31.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.228 | 0.231 | +1.5% (-29.5 to +32.4) | -7.7% (-45.1 to +29.7) | +10.0% (-9.6 to +29.6) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 19.7 | +19.7 (+13.4 to +25.9) | +20 (+17.5 to +22.5) | +20 (+17.5 to +22.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (13 trials, 0 allowed, 4 refused); acting: 64 to 72 (14 trials, 1 allowed, 2 refused); left native (13 trials, 0 allowed, 3 refused); run B: acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 2 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); run C: acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 64 to 72 (11 trials, 1 allowed, 3 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 924.4 | 936.2 | +1.3% (+1.2 to +1.4) | +1.3% (+1.2 to +1.4) | +1.2% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.2 to +1.4) | +1.3% (+1.2 to +1.4) | +1.2% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | +0.1% (-0.2 to +0.5) | +0.0% (-0.3 to +0.3) | -0.0% (-0.1 to +0.1) | STEADY, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.33 | 5.45 | +2.2% (+1.3 to +3.1) | +0.2% (-0.2 to +0.5) | +0.1% (-0.0 to +0.2) | **LOSS by the mean of our three runs, beyond the noise in 1 of 3** |
| latency, mean (ms) | 2.06 | 2.02 | -1.7% (-2.0 to -1.5) | -1.9% (-2.2 to -1.5) | -1.8% (-2.0 to -1.6) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.6 | +2.5% (+2.3 to +2.7) | +2.8% (+1.5 to +4.0) | +2.1% (+1.6 to +2.5) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 62.0 | +2.2% (+2.0 to +2.3) | +1.6% (+0.8 to +2.5) | +1.9% (+1.3 to +2.5) | **power given in all three of our runs** |
| keys evicted | 243,278 | 235,724 | -3.1% (-5.0 to -1.2) | -2.1% (-5.2 to +1.1) | -2.5% (-6.0 to +1.0) | shown, not judged |
| host CPU busy (share of the run) | 0.0699 | 0.0674 | -3.5% (-45.8 to +38.7) | -1.2% (-33.0 to +30.5) | -7.7% (-18.0 to +2.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 123.3 | 118.2 | -4.1% (-48.3 to +40.2) | -1.3% (-38.1 to +35.5) | -8.8% (-20.5 to +2.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.296 | 0.281 | -5.3% (-49.4 to +38.7) | -2.6% (-39.2 to +34.0) | -9.9% (-21.7 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 14.7 | +14.7 (+10.9 to +18.5) | +17 (+8.39 to +25.6) | +14 (+11.5 to +16.5) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 56 to 80 (12 trials, 3 allowed, 0 refused); acting: 56 to 80 (13 trials, 3 allowed, 0 refused); run C: acting: 64 to 80 (12 trials, 2 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 56 to 72 (10 trials, 2 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 1 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 STEADY, 3 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
