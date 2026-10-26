# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; EVEN is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40238126261 | `2d40c4c64109` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| B | 40260615533 | `b659f0eebc58` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |
| C | 40283020884 | `b11b4d3825b1` | omni-v21 (digest b658f05d43c1e602, 63 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.1 to +0.0) | EVEN, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.929 | 0.929 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.2) | +0.1% (-0.2 to +0.4) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.77 | 5.77 | -0.0% (-0.1 to +0.1) | +0.1% (-0.1 to +0.2) | +0.5% (+0.4 to +0.6) | EVEN, under the floor (the three runs' mean 0.17%) |
| latency, mean (ms) | 0.568 | 0.568 | +0.0% (-0.4 to +0.5) | +0.1% (-0.8 to +1.0) | +1.8% (-0.6 to +4.2) | **LOSS by the mean of our three runs, beyond the noise in 0 of 3** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 333.1 | 333.1 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.1 | 0.0896 | -10.7% (-18.1 to -3.2) | +8.2% (-40.4 to +56.8) | +8.7% (-78.5 to +95.9) | **the runs disagree** |
| host CPU-seconds | 169.4 | 149.4 | -11.8% (-20.0 to -3.6) | +9.0% (-44.4 to +62.3) | +9.3% (-83.1 to +101.6) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.27 | 0.238 | -11.8% (-20.0 to -3.6) | +9.0% (-44.4 to +62.3) | +9.3% (-83.1 to +101.7) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 243.4 | 244.2 | +0.3% (+0.0 to +0.7) | +0.2% (-0.6 to +0.9) | +4.7% (-0.4 to +9.9) | **power given by the mean of our three runs, beyond the noise in 1 of 3** |
| the server's own CPU-seconds (redis-server) | 30.9 | 30.6 | -1.0% (-2.8 to +0.8) | +0.6% (-3.5 to +4.7) | +4.7% (-0.2 to +9.7) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 212.3 | 213.4 | +0.5% (+0.4 to +0.7) | +0.1% (-0.9 to +1.1) | +4.7% (-0.5 to +9.9) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.227 | -0.7% (-1.2 to -0.1) | -0.7% (-3.5 to +2.2) | +0.9% (-6.0 to +7.8) | shown, not judged |
| host CPU-seconds without steal | 169.4 | 149.4 | -11.8% (-20.0 to -3.6) | +9.0% (-44.4 to +62.3) | +9.3% (-83.1 to +101.6) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | +0.0% (+0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.71 | 5.71 | -0.1% (-0.3 to +0.0) | -0.1% (-0.3 to +0.2) | +0.1% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, 99th percentile (ms) | 5.78 | 5.78 | -0.1% (-0.3 to +0.1) | -0.1% (-0.1 to -0.0) | +0.0% (-0.1 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 0.81 | 0.808 | -0.2% (-1.0 to +0.6) | +0.2% (-1.0 to +1.3) | +0.1% (-1.5 to +1.7) | EVEN, under the floor (the three runs' mean 0.03%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 199.8 | 199.9 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.0999 | -15.3% (-40.5 to +9.8) | -4.1% (-62.5 to +54.3) | -8.3% (-86.3 to +69.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 80.6 | 66.9 | -17.0% (-45.2 to +11.2) | -4.4% (-70.2 to +61.4) | -9.6% (-95.7 to +76.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.337 | 0.28 | -17.0% (-45.2 to +11.2) | -4.4% (-70.2 to +61.4) | -9.6% (-95.7 to +76.5) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 102.8 | 101.9 | -0.9% (-2.9 to +1.0) | -0.3% (-0.8 to +0.2) | -0.6% (-1.7 to +0.6) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| the server's own CPU-seconds (redis-server) | 12.7 | 12.8 | +0.7% (-1.9 to +3.3) | -0.7% (-3.5 to +2.1) | -1.8% (-3.6 to -0.1) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 90.0 | 89.0 | -1.2% (-3.0 to +0.7) | -0.2% (-0.9 to +0.4) | -0.4% (-1.9 to +1.1) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.0857 | 0.0857 | +0.0% (-1.4 to +1.5) | +0.4% (-3.1 to +3.8) | -1.0% (-3.8 to +1.8) | shown, not judged |
| host CPU-seconds without steal | 80.6 | 66.9 | -17.0% (-45.2 to +11.2) | -4.4% (-70.2 to +61.4) | -9.6% (-95.7 to +76.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | -0.0% (-0.0 to +0.0) | -0.0% (-0.1 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.981 | 0.981 | +0.0% (+0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| latency, 95th percentile (ms) | 0.255 | 0.253 | -0.9% (-4.9 to +3.1) | -3.4% (-10.0 to +3.2) | -2.2% (-12.7 to +8.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.75 | 5.75 | -0.0% (-0.2 to +0.2) | +0.1% (-0.5 to +0.6) | +0.1% (-0.0 to +0.2) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 0.303 | 0.303 | -0.2% (-0.8 to +0.5) | +0.5% (-5.4 to +6.4) | -0.5% (-2.5 to +1.5) | EVEN, under the floor (the three runs' mean 0.06%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 348.5 | 348.5 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0949 | 0.103 | +8.4% (-16.0 to +32.9) | -19.5% (-63.5 to +24.6) | +2.5% (-29.2 to +34.3) | **the runs disagree** |
| host CPU-seconds | 158.2 | 172.9 | +9.3% (-17.5 to +36.1) | -20.6% (-67.3 to +26.2) | +2.9% (-31.8 to +37.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.239 | 0.261 | +9.3% (-17.5 to +36.1) | -20.5% (-67.3 to +26.2) | +2.9% (-31.8 to +37.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 255.9 | 256.6 | +0.3% (-1.2 to +1.8) | -0.8% (-8.9 to +7.3) | -0.2% (-4.6 to +4.1) | EVEN, under the floor (the three runs' mean 0.25%) |
| the server's own CPU-seconds (redis-server) | 34.8 | 34.7 | -0.2% (-5.1 to +4.7) | -1.1% (-10.8 to +8.5) | -1.0% (-3.8 to +1.9) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 220.8 | 221.6 | +0.4% (-1.0 to +1.8) | -0.8% (-8.6 to +7.1) | -0.1% (-4.7 to +4.6) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.301 | 0.29 | -3.7% (-21.7 to +14.4) | -0.9% (-17.0 to +15.2) | -0.3% (-1.6 to +1.0) | shown, not judged |
| host CPU-seconds without steal | 158.2 | 172.9 | +9.3% (-17.5 to +36.1) | -20.6% (-67.3 to +26.2) | +2.9% (-31.8 to +37.5) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.782 | 0.782 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.67 | 5.67 | +0.0% (-0.2 to +0.2) | +0.1% (-0.9 to +1.0) | -0.0% (-0.6 to +0.5) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, 99th percentile (ms) | 5.74 | 5.74 | +0.0% (-0.2 to +0.3) | +0.1% (-0.7 to +0.8) | -0.1% (-0.6 to +0.5) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 1.36 | 1.36 | -0.0% (-0.6 to +0.5) | +0.2% (-1.5 to +1.9) | -0.1% (-1.0 to +0.9) | EVEN, under the floor (the three runs' mean 0.04%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 257.3 | 257.3 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.118 | 0.119 | +0.6% (-34.1 to +35.4) | +4.2% (-31.1 to +39.5) | -15.6% (-70.6 to +39.4) | **the runs disagree** |
| host CPU-seconds | 198.2 | 199.5 | +0.6% (-38.9 to +40.2) | +4.6% (-33.9 to +43.0) | -16.9% (-76.7 to +42.9) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.375 | 0.378 | +0.6% (-38.9 to +40.1) | +4.5% (-33.8 to +42.9) | -16.9% (-76.6 to +42.8) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded) | 275.1 | 273.7 | -0.5% (-1.8 to +0.8) | +1.0% (-6.7 to +8.7) | -1.5% (-5.9 to +2.8) | **the runs disagree** |
| the server's own CPU-seconds (redis-server) | 32.5 | 32.6 | +0.4% (-0.9 to +1.7) | +0.8% (-8.1 to +9.8) | -1.9% (-11.2 to +7.4) | shown, not judged |
| the application's own CPU-seconds (its request threads) | 242.3 | 240.8 | -0.6% (-1.9 to +0.7) | +1.0% (-6.6 to +8.6) | -1.5% (-5.2 to +2.2) | shown, not judged |
| the compass's own CPU-seconds (the brain's thread; none in the native arm) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| the sampler's own CPU-seconds (both arms) | 0.228 | 0.227 | -0.3% (-4.7 to +4.0) | +0.6% (-9.7 to +10.9) | -2.4% (-4.6 to -0.2) | shown, not judged |
| host CPU-seconds without steal | 198.2 | 199.5 | +0.6% (-38.9 to +40.2) | +4.6% (-33.9 to +43.0) | -16.9% (-76.7 to +42.9) | shown, not judged |
| CPU-seconds the hypervisor took (steal), host-wide | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 5 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 27 EVEN, 7 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
