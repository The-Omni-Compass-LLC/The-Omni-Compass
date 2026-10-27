# Redis, a cache's operator-set memory ceiling: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis as shipped with the operator's memory ceiling (64 MB, allkeys-lru) is native; omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40254205224 | `babd7a2ceac0` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40276907808 | `796063486f34` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40400989005 | `5e222aa21371` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,182 | 1,196 | +1.2% (+0.9 to +1.5) | +0.7% (+0.1 to +1.3) | +0.8% (+0.5 to +1.1) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.789 | 0.799 | +1.2% (+1.1 to +1.3) | +0.7% (+0.1 to +1.2) | +0.8% (+0.4 to +1.1) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.22 | 5.22 | -0.0% (-0.2 to +0.2) | -0.1% (-0.3 to +0.2) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 99th percentile (ms) | 5.28 | 5.29 | +0.2% (-0.4 to +0.8) | +0.0% (-0.4 to +0.5) | +0.2% (-2.1 to +2.4) | EVEN, under the floor (the three runs' mean 0.12%) |
| latency, mean (ms) | 1.17 | 1.13 | -3.8% (-5.7 to -1.9) | -2.2% (-5.1 to +0.7) | -2.6% (-3.5 to -1.8) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 66.1 | +3.2% (+1.9 to +4.5) | +1.4% (+0.8 to +2.1) | +2.0% (+0.3 to +3.7) | **power given in all three of our runs** |
| memory used, mean (MB) | 61.2 | 62.7 | +2.4% (+1.4 to +3.5) | +1.2% (+0.8 to +1.6) | +1.6% (+0.4 to +2.8) | **power given in all three of our runs** |
| keys evicted | 138,258 | 132,610 | -4.1% (-4.5 to -3.6) | -2.0% (-4.1 to +0.1) | -2.7% (-4.9 to -0.4) | shown, not judged |
| host CPU busy (share of the run) | 0.0606 | 0.0636 | +4.9% (-57.0 to +66.8) | -7.1% (-34.1 to +19.8) | -8.4% (-59.6 to +42.7) | **the runs disagree** |
| host CPU-seconds | 106.9 | 112.2 | +5.0% (-60.5 to +70.4) | -7.9% (-38.1 to +22.3) | -9.2% (-63.5 to +45.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.201 | 0.208 | +3.7% (-61.8 to +69.3) | -8.6% (-39.2 to +22.1) | -9.9% (-64.0 to +44.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 22.3 | +22.3 (+19.5 to +25.2) | +16.3 (+8.74 to +23.9) | +14.7 (+11.8 to +17.5) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 122.0 | 123.7 | +1.4% (-3.5 to +6.2) | -0.9% (-2.9 to +1.1) | -0.0% (-5.0 to +5.0) | **the runs disagree** |
| the server's own CPU-seconds (redis-server) | 17.1 | 17.2 | +0.5% (-1.9 to +2.9) | +0.5% (-0.1 to +1.0) | -1.0% (-6.9 to +4.9) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 104.8 | 105.8 | +1.0% (-4.6 to +6.6) | -1.4% (-3.6 to +0.7) | -0.4% (-5.2 to +4.5) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.563 | +0.563 (+0.433 to +0.694) | +0.935 (+0.877 to +0.994) | +0.372 (+0.292 to +0.452) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.126 | 0.123 | -2.7% (-16.2 to +10.8) | -1.7% (-7.5 to +4.1) | -6.6% (-15.4 to +2.2) | shown, not judged |
| host CPU-seconds without steal | 106.9 | 112.2 | +5.0% (-60.5 to +70.4) | -7.9% (-38.1 to +22.3) | -9.2% (-63.5 to +45.0) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (14 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (14 trials, 1 allowed, 0 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (11 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (10 trials, 1 allowed, 0 refused).

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,076 | 1,076 | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | -0.0% (-0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.718 | 0.717 | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.0) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 95th percentile (ms) | 5.55 | 5.55 | -0.0% (-0.2 to +0.1) | +0.0% (-0.2 to +0.2) | -0.0% (-0.1 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.6 | 5.61 | +0.0% (-0.1 to +0.1) | +0.1% (-0.3 to +0.4) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 1.62 | 1.62 | +0.1% (-0.5 to +0.7) | +0.2% (-0.7 to +1.1) | -0.1% (-0.8 to +0.6) | EVEN, under the floor (the three runs' mean 0.04%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 62.6 | -2.2% (-2.4 to -1.9) | -2.4% (-3.1 to -1.7) | -1.3% (-1.3 to -1.3) | **GAIN in all three of our runs** |
| memory used, mean (MB) | 57.1 | 56.7 | -0.7% (-1.0 to -0.4) | -1.0% (-1.7 to -0.2) | +0.1% (+0.1 to +0.2) | **GAIN by the mean of our three runs, beyond the noise in 3 of 3** |
| keys evicted | 71,708 | 72,371 | +0.9% (+0.7 to +1.1) | +0.9% (+0.9 to +0.9) | +1.3% (+1.0 to +1.7) | shown, not judged |
| host CPU busy (share of the run) | 0.0937 | 0.0915 | -2.3% (-42.3 to +37.8) | -10.7% (-68.3 to +46.9) | -10.3% (-64.8 to +44.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 64.9 | 63.5 | -2.2% (-46.8 to +42.5) | -12.0% (-75.8 to +51.9) | -10.9% (-67.9 to +46.1) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.335 | 0.328 | -2.1% (-46.8 to +42.5) | -12.0% (-75.8 to +51.9) | -10.8% (-68.0 to +46.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 6 | +6 (+6 to +6) | +6 (+6 to +6) | +2 (+2 to +2) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 79.9 | 80.0 | +0.1% (-0.8 to +1.1) | +0.4% (-2.5 to +3.2) | +0.1% (-2.0 to +2.2) | EVEN, under the floor (the three runs' mean 0.18%) |
| the server's own CPU-seconds (redis-server) | 10.1 | 10.2 | +0.7% (-0.0 to +1.4) | +0.6% (-3.9 to +5.2) | +0.1% (-2.2 to +2.5) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 69.7 | 69.5 | -0.4% (-1.5 to +0.8) | -0.1% (-3.0 to +2.8) | -0.5% (-3.3 to +2.2) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.283 | +0.283 (+0.238 to +0.329) | +0.301 (+0.274 to +0.328) | +0.16 (+0.141 to +0.179) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0653 | 0.0634 | -2.9% (-5.0 to -0.9) | -0.3% (-1.0 to +0.5) | -4.0% (-17.1 to +9.0) | shown, not judged |
| host CPU-seconds without steal | 64.9 | 63.5 | -2.2% (-46.8 to +42.5) | -12.0% (-75.8 to +51.9) | -10.9% (-67.9 to +46.1) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run B: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); run C: left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused); left native (3 trials, 0 allowed, 0 refused).

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,267 | 1,285 | +1.4% (+0.5 to +2.3) | +1.7% (+1.6 to +1.9) | +0.7% (+0.0 to +1.3) | **GAIN in all three of our runs** |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.845 | 0.857 | +1.4% (+0.5 to +2.3) | +1.7% (+1.6 to +1.9) | +0.7% (+0.1 to +1.3) | **GAIN in all three of our runs** |
| latency, 95th percentile (ms) | 5.49 | 5.48 | -0.3% (-0.5 to +0.0) | -0.1% (-0.3 to +0.1) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.12%) |
| latency, 99th percentile (ms) | 5.6 | 5.6 | -0.0% (-0.3 to +0.2) | +0.1% (-0.1 to +0.2) | +0.1% (-0.1 to +0.4) | EVEN, under the floor (the three runs' mean 0.06%) |
| latency, mean (ms) | 0.956 | 0.891 | -6.7% (-10.3 to -3.2) | -7.8% (-8.5 to -7.2) | -2.7% (-5.1 to -0.3) | **GAIN in all three of our runs** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 64.5 | +0.8% (-1.1 to +2.7) | +1.4% (-1.0 to +3.8) | +1.7% (+0.1 to +3.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| memory used, mean (MB) | 61.3 | 61.6 | +0.5% (-1.4 to +2.4) | +1.0% (-0.8 to +2.8) | +0.8% (-0.6 to +2.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| keys evicted | 103,441 | 95,579 | -7.6% (-12.4 to -2.8) | -9.3% (-10.1 to -8.6) | -3.4% (-6.5 to -0.3) | shown, not judged |
| host CPU busy (share of the run) | 0.103 | 0.0917 | -11.2% (-24.8 to +2.4) | +16.6% (-5.6 to +38.7) | -13.3% (-26.1 to -0.4) | **the runs disagree** |
| host CPU-seconds | 182.2 | 160.2 | -12.1% (-26.5 to +2.3) | +18.9% (-6.0 to +43.7) | -14.9% (-29.1 to -0.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.32 | 0.277 | -13.4% (-27.0 to +0.3) | +16.8% (-7.5 to +41.2) | -15.5% (-30.0 to -1.0) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 21.0 | +21 (+16 to +26) | +22.3 (+19.5 to +25.2) | +21 (+14.4 to +27.6) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 189.9 | 187.9 | -1.0% (-1.2 to -0.9) | -0.1% (-2.4 to +2.2) | +0.3% (-0.3 to +0.8) | EVEN, under the floor (the three runs' mean 0.30%) |
| the server's own CPU-seconds (redis-server) | 25.9 | 25.6 | -1.1% (-3.6 to +1.5) | -0.2% (-1.2 to +0.7) | -0.1% (-1.8 to +1.6) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 163.8 | 161.4 | -1.5% (-1.7 to -1.2) | -0.5% (-3.0 to +1.9) | -0.1% (-0.5 to +0.4) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.698 | +0.698 (+0.66 to +0.735) | +0.757 (+0.738 to +0.776) | +0.6 (+0.574 to +0.626) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.164 | 0.16 | -2.8% (-6.0 to +0.5) | -0.6% (-5.7 to +4.4) | -1.2% (-3.9 to +1.5) | shown, not judged |
| host CPU-seconds without steal | 182.2 | 160.2 | -12.1% (-26.5 to +2.3) | +18.9% (-6.0 to +43.7) | -14.9% (-29.1 to -0.8) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 72 (13 trials, 1 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 2 refused); left native (11 trials, 0 allowed, 2 refused); run B: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); acting: 64 to 72 (12 trials, 1 allowed, 1 refused); acting: 64 to 72 (11 trials, 1 allowed, 1 refused); run C: acting: 64 to 72 (12 trials, 1 allowed, 0 refused); left native (12 trials, 0 allowed, 0 refused); acting: 64 to 72 (11 trials, 1 allowed, 0 refused).

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; the operator's ceiling 64 MB, the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 925.6 | 934.8 | +1.0% (-0.7 to +2.7) | +1.3% (+1.1 to +1.5) | +0.6% (+0.6 to +0.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.617 | 0.623 | +1.0% (-0.7 to +2.7) | +1.3% (+1.1 to +1.5) | +0.7% (+0.6 to +0.7) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.0% (-0.2 to +0.3) | +0.0% (-0.0 to +0.1) | +0.1% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.74 | 5.75 | +0.2% (-0.3 to +0.6) | +0.2% (+0.1 to +0.3) | +1.7% (+0.4 to +3.1) | **LOSS by the mean of our three runs, beyond the noise in 2 of 3** |
| latency, mean (ms) | 2.26 | 2.23 | -1.4% (-3.4 to +0.7) | -1.7% (-2.0 to -1.4) | -0.6% (-0.8 to -0.5) | **GAIN by the mean of our three runs, beyond the noise in 2 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 64.0 | 65.2 | +1.8% (-0.4 to +4.1) | +2.2% (+2.1 to +2.3) | +0.8% (+0.8 to +0.8) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| memory used, mean (MB) | 60.7 | 61.5 | +1.3% (-0.3 to +3.0) | +1.9% (+1.3 to +2.5) | +1.1% (+1.1 to +1.2) | **power given by the mean of our three runs, beyond the noise in 2 of 3** |
| keys evicted | 243,212 | 241,242 | -0.8% (-1.8 to +0.2) | -2.6% (-6.1 to +0.9) | -2.6% (-2.7 to -2.5) | shown, not judged |
| host CPU busy (share of the run) | 0.146 | 0.148 | +1.0% (-17.5 to +19.6) | +9.7% (-3.0 to +22.4) | +11.4% (-50.1 to +72.9) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 246.5 | 249.5 | +1.2% (-21.4 to +23.8) | +11.4% (-3.6 to +26.5) | +11.8% (-54.6 to +78.2) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.592 | 0.593 | +0.3% (-23.8 to +24.3) | +10.1% (-5.1 to +25.2) | +11.1% (-55.2 to +77.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 15.3 | +15.3 (+12.5 to +18.2) | +14 (+9.7 to +18.3) | +3 (+3 to +3) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 308.9 | 309.7 | +0.3% (-2.4 to +3.0) | +0.3% (-0.3 to +1.0) | +2.4% (+0.6 to +4.3) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the server's own CPU-seconds (redis-server) | 35.2 | 35.7 | +1.2% (-2.8 to +5.2) | -0.3% (-3.3 to +2.8) | +1.5% (-1.1 to +4.0) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 273.4 | 272.9 | -0.2% (-2.7 to +2.4) | +0.1% (-1.1 to +1.2) | +2.0% (+0.3 to +3.8) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0.943 | +0.943 (+0.899 to +0.986) | +0.924 (+0.818 to +1.03) | +0.413 (+0.391 to +0.435) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.237 | 0.233 | -1.8% (-16.1 to +12.5) | -1.0% (-4.5 to +2.6) | -2.5% (-9.1 to +4.1) | shown, not judged |
| host CPU-seconds without steal | 246.5 | 249.5 | +1.2% (-21.4 to +23.8) | +11.4% (-3.6 to +26.5) | +11.8% (-54.6 to +78.2) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

The brain's own verdict on the knob in the omni arms, one trial at a time on the stack itself (the objective: resource): run A: acting: 64 to 80 (11 trials, 2 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); left native (9 trials, 0 allowed, 1 refused); run B: acting: 64 to 72 (9 trials, 1 allowed, 0 refused); acting: 64 to 80 (10 trials, 2 allowed, 0 refused); acting: 64 to 72 (9 trials, 1 allowed, 0 refused); run C: acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused); acting: 64 to 72 (8 trials, 1 allowed, 0 refused).

**Across 3 untouched workloads: 11 gauge-rows GAIN, 1 LOSS, 8 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 16 EVEN, 3 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
