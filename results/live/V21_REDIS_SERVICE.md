# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40236922598 | `23c7e8eb27be` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40259308169 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40281475145 | `fa6da97bbaa6` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,184 | 1,191 | +0.6% (-0.1 to +1.3) | +1.2% (+1.0 to +1.4) | +0.9% (+0.3 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.79 | 0.794 | +0.6% (-0.1 to +1.3) | +1.2% (+1.0 to +1.4) | +0.9% (+0.3 to +1.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.74 | 5.74 | +0.1% (-0.2 to +0.3) | -0.0% (-0.3 to +0.2) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 99th percentile (ms) | 5.79 | 5.8 | +0.2% (-0.2 to +0.5) | +0.0% (-0.1 to +0.2) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.08%) |
| latency, mean (ms) | 1.34 | 1.32 | -1.6% (-4.6 to +1.5) | -4.0% (-4.7 to -3.3) | -2.7% (-4.3 to -1.2) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.0 | +1.5% (-0.6 to +3.6) | +2.6% (+2.6 to +2.7) | +1.7% (+0.0 to +3.5) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 61.2 | 61.9 | +1.1% (-0.5 to +2.7) | +1.9% (+1.9 to +2.0) | +1.3% (-0.6 to +3.2) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 138,050 | 135,880 | -1.6% (-4.9 to +1.7) | -4.0% (-4.7 to -3.3) | -2.6% (-5.2 to -0.1) | shown, not judged |
| host CPU busy (share of the run) | 0.105 | 0.134 | +27.5% (-38.5 to +93.5) | -1.9% (-16.4 to +12.5) | -2.8% (-14.8 to +9.1) | **the runs disagree** |
| host CPU-seconds | 173.0 | 227.9 | +31.7% (-44.2 to +107.7) | -2.1% (-18.1 to +13.9) | -3.1% (-16.8 to +10.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.325 | 0.425 | +30.9% (-45.6 to +107.5) | -3.2% (-19.1 to +12.6) | -4.0% (-17.2 to +9.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 18.7 | +18.7 (+6.41 to +30.9) | +23 (+23 to +23) | +20 (+11 to +29) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 282.8 | 285.9 | +1.1% (-1.4 to +3.5) | -0.2% (-0.8 to +0.4) | -0.3% (-1.4 to +0.8) | EVEN, under the floor (the three runs' mean 0.20%) |
| the server's own CPU-seconds (redis-server) | 34.6 | 35.1 | +1.3% (-2.0 to +4.6) | +0.1% (-1.9 to +2.1) | -0.2% (-5.6 to +5.2) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 247.9 | 249.6 | +0.7% (-1.7 to +3.1) | -0.7% (-1.0 to -0.4) | -0.7% (-1.3 to -0.0) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.929 | +0.929 (+0.881 to +0.977) | +0.725 (+0.626 to +0.824) | +0.897 (+0.839 to +0.954) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.231 | 0.229 | -0.6% (-2.8 to +1.5) | -1.9% (-4.9 to +1.1) | -1.3% (-2.6 to -0.0) | shown, not judged |
| host CPU-seconds without steal | 173.0 | 227.9 | +31.7% (-44.2 to +107.7) | -2.1% (-18.1 to +13.9) | -3.1% (-16.8 to +10.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 1 refused); acting: 56 to 72 (13 trials, 2 allowed, 0 refused); run B: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (13 trials, 1 allowed, 0 refused); run C: acting: 56 to 72 (14 trials, 2 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,075 | -0.0% (-0.2 to +0.1) | +0.1% (-0.6 to +0.8) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.1% (-0.3 to +0.2) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.02%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 95th percentile (ms) | 5.74 | 5.74 | -0.0% (-0.3 to +0.2) | -0.0% (-0.3 to +0.2) | +0.1% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.1% (-0.4 to +0.5) | -5.5% (-52.8 to +41.8) | +0.1% (-0.0 to +0.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 1.75 | 1.75 | +0.2% (-1.1 to +1.5) | +0.2% (-5.4 to +5.9) | +0.5% (+0.1 to +0.9) | EVEN, under the floor (the three runs' mean 0.32%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.3 | -2.6% (-3.4 to -1.8) | -4.2% (-7.5 to -0.9) | -2.9% (-5.3 to -0.6) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.1 | 56.5 | -1.1% (-2.0 to -0.2) | -3.0% (-6.7 to +0.7) | -1.6% (-4.4 to +1.2) | **GAIN by the mean of our three runs, beyond the noise in 1 of 3** |
| keys evicted | 71,770 | 72,401 | +0.9% (+0.6 to +1.2) | +0.3% (-0.4 to +1.1) | +0.8% (-0.5 to +2.1) | shown, not judged |
| host CPU busy (share of the run) | 0.12 | 0.137 | +14.8% (-22.7 to +52.3) | -2.1% (-29.0 to +24.8) | -14.8% (-49.9 to +20.4) | **the runs disagree** |
| host CPU-seconds | 79.1 | 92.5 | +16.9% (-24.6 to +58.5) | -2.5% (-35.2 to +30.1) | -16.9% (-56.5 to +22.6) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.409 | 0.478 | +16.9% (-24.5 to +58.3) | -2.6% (-35.1 to +29.8) | -16.9% (-56.3 to +22.6) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +8 (+3.03 to +13) | +6.67 (+3.8 to +9.54) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 119.9 | 120.7 | +0.7% (-2.4 to +3.8) | +0.0% (-3.9 to +3.9) | +0.8% (-1.5 to +3.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (redis-server) | 14.7 | 14.7 | +0.0% (-4.0 to +4.1) | +0.8% (-2.5 to +4.1) | +1.5% (-4.5 to +7.5) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 105.2 | 105.6 | +0.4% (-2.6 to +3.4) | -0.5% (-4.5 to +3.6) | +0.4% (-1.6 to +2.3) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.379 | +0.379 (+0.319 to +0.44) | +0.398 (+0.355 to +0.442) | +0.312 (+0.297 to +0.328) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0934 | 0.0916 | -1.9% (-11.0 to +7.2) | -2.1% (-14.4 to +10.3) | +0.5% (-1.0 to +2.1) | shown, not judged |
| host CPU-seconds without steal | 79.1 | 92.5 | +16.9% (-24.6 to +58.5) | -2.5% (-35.2 to +30.1) | -16.9% (-56.5 to +22.6) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); acting: 56 to 64 (4 trials, 1 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,283 | +1.3% (+0.9 to +1.7) | +1.2% (+0.1 to +2.2) | +1.2% (-0.1 to +2.4) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.856 | +1.3% (+0.9 to +1.7) | +1.2% (+0.1 to +2.3) | +1.2% (-0.1 to +2.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.5 | 5.49 | -0.2% (-0.4 to -0.0) | -0.0% (-0.3 to +0.2) | -0.1% (-0.1 to +0.0) | EVEN, under the floor (the three runs' mean 0.10%) |
| latency, 99th percentile (ms) | 5.6 | 5.6 | +0.0% (-0.2 to +0.2) | +0.0% (-0.0 to +0.1) | +0.0% (-0.3 to +0.3) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 0.959 | 0.901 | -6.0% (-8.5 to -3.5) | -5.0% (-9.9 to -0.2) | -4.9% (-10.0 to +0.1) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 63.2 | -1.3% (-1.5 to -1.1) | +1.5% (-0.8 to +3.9) | +0.5% (-3.8 to +4.7) | **the runs disagree** |
| memory used, mean (MB) | 61.3 | 60.1 | -2.0% (-3.1 to -1.0) | +1.1% (-0.3 to +2.6) | -0.2% (-4.6 to +4.2) | **the runs disagree** |
| keys evicted | 103,401 | 96,558 | -6.6% (-8.7 to -4.5) | -6.4% (-12.3 to -0.4) | -6.3% (-13.4 to +0.9) | shown, not judged |
| host CPU busy (share of the run) | 0.099 | 0.0874 | -11.7% (-56.0 to +32.6) | -10.7% (-40.6 to +19.2) | -7.8% (-31.9 to +16.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 173.7 | 151.3 | -12.9% (-62.4 to +36.6) | -11.7% (-44.5 to +21.1) | -8.7% (-35.9 to +18.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.305 | 0.262 | -14.0% (-63.7 to +35.7) | -12.7% (-45.1 to +19.6) | -9.8% (-35.9 to +16.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 29.0 | +29 (+26.5 to +31.5) | +19.3 (+13.1 to +25.6) | +24 (+10.2 to +37.8) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 193.2 | 191.0 | -1.1% (-3.2 to +1.0) | -0.5% (-1.8 to +0.8) | -0.5% (-1.7 to +0.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (redis-server) | 26.2 | 26.1 | -0.4% (-3.1 to +2.4) | -0.5% (-4.9 to +4.0) | -1.4% (-4.5 to +1.7) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 166.9 | 164.1 | -1.7% (-4.0 to +0.7) | -0.8% (-2.4 to +0.7) | -0.8% (-2.0 to +0.5) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.697 | +0.697 (+0.572 to +0.821) | +0.918 (+0.865 to +0.97) | +0.957 (+0.923 to +0.991) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.161 | -1.5% (-3.8 to +0.8) | -2.0% (-4.3 to +0.3) | -0.7% (-2.9 to +1.6) | shown, not judged |
| host CPU-seconds without steal | 173.7 | 151.3 | -12.9% (-62.4 to +36.6) | -11.7% (-44.5 to +21.1) | -8.7% (-35.9 to +18.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 48 to 72 (13 trials, 3 allowed, 2 refused); acting: 56 to 72 (12 trials, 2 allowed, 3 refused); acting: 48 to 72 (15 trials, 3 allowed, 1 refused); run B: acting: 64 to 72 (11 trials, 1 allowed, 3 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 56 to 72 (11 trials, 2 allowed, 2 refused); run C: acting: 64 to 72 (11 trials, 1 allowed, 2 refused); acting: 56 to 72 (13 trials, 2 allowed, 3 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.3 | 936.8 | +1.2% (+1.2 to +1.3) | +1.2% (+0.9 to +1.6) | +1.2% (+1.1 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.625 | +1.3% (+1.1 to +1.4) | +1.2% (+1.0 to +1.4) | +1.2% (+1.1 to +1.4) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.64 | 5.64 | +0.1% (-0.1 to +0.2) | +0.1% (-0.5 to +0.6) | +0.0% (+0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.69 | 5.71 | +0.4% (-0.7 to +1.5) | +1.0% (-2.2 to +4.2) | +0.2% (-0.0 to +0.5) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, mean (ms) | 2.24 | 2.2 | -1.7% (-2.2 to -1.1) | -1.7% (-2.8 to -0.5) | -1.7% (-1.9 to -1.5) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.4 | +2.2% (+2.1 to +2.2) | +2.3% (+1.8 to +2.8) | +2.2% (+2.1 to +2.2) | **power given in all three of our runs** |
| memory used, mean (MB) | 60.7 | 61.9 | +2.0% (+2.0 to +2.1) | +2.1% (+1.8 to +2.3) | +2.0% (+2.0 to +2.0) | **power given in all three of our runs** |
| keys evicted | 243,176 | 234,804 | -3.4% (-3.7 to -3.2) | -3.0% (-4.6 to -1.4) | -3.4% (-3.6 to -3.1) | shown, not judged |
| host CPU busy (share of the run) | 0.152 | 0.15 | -1.1% (-16.9 to +14.7) | +7.8% (-70.1 to +85.7) | -2.0% (-7.5 to +3.5) | **the runs disagree** |
| host CPU-seconds | 262.4 | 259.2 | -1.2% (-19.7 to +17.3) | +7.8% (-74.7 to +90.3) | -2.2% (-8.8 to +4.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.63 | 0.615 | -2.4% (-20.6 to +15.7) | +6.5% (-75.8 to +88.7) | -3.4% (-10.0 to +3.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 13.0 | +13 (+8.03 to +18) | +13.3 (+7.08 to +19.6) | +12.3 (+9.46 to +15.2) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 284.1 | 285.2 | +0.4% (-2.0 to +2.8) | +2.9% (-13.3 to +19.1) | -0.3% (-0.7 to +0.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (redis-server) | 32.4 | 32.3 | -0.3% (-3.7 to +3.1) | +1.7% (-13.0 to +16.4) | -1.0% (-2.0 to -0.1) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 251.5 | 251.8 | +0.1% (-2.2 to +2.4) | +2.6% (-13.8 to +18.9) | -0.5% (-0.9 to -0.1) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.926 | +0.926 (+0.838 to +1.01) | +0.599 (+0.455 to +0.742) | +0.921 (+0.838 to +1) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.22 | 0.219 | -0.3% (-3.6 to +3.0) | +1.1% (-9.1 to +11.3) | -1.5% (-5.7 to +2.6) | shown, not judged |
| host CPU-seconds without steal | 262.4 | 259.2 | -1.2% (-19.7 to +17.3) | +7.8% (-74.7 to +90.3) | -2.2% (-8.8 to +4.3) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: service): run A: acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 13 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 13 EVEN, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
