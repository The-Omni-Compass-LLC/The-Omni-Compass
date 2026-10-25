# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the words were read again, and this rule replaces the one the text below describes.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **STEADY, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39382995467 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| B | 39414279979 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |
| C | 39461540163 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% (-0.0 to +0.0) | +0.0% (-0.1 to +0.1) | -0.0% (-0.0 to -0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.929 | 0.929 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.69 | 5.69 | +0.1% (-0.0 to +0.2) | -0.1% (-0.3 to +0.1) | -0.0% (-0.6 to +0.6) | STEADY, under the floor (the three runs' mean 0.01%) |
| latency, 99th percentile (ms) | 5.8 | 5.81 | +0.2% (+0.0 to +0.3) | -0.1% (-0.3 to +0.1) | -0.0% (-0.7 to +0.7) | STEADY, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 0.576 | 0.575 | -0.1% (-1.3 to +1.2) | +0.1% (-1.0 to +1.1) | -0.3% (-1.4 to +0.8) | STEADY, under the floor (the three runs' mean 0.09%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory used, mean (MB) | 333.1 | 333.1 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0933 | 0.095 | +1.8% (-11.1 to +14.6) | +4.6% (-67.2 to +76.5) | -6.1% (-29.2 to +17.0) | **the runs disagree** |
| host CPU-seconds | 155.8 | 158.6 | +1.8% (-12.4 to +16.1) | +4.8% (-74.9 to +84.5) | -6.8% (-32.7 to +19.1) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.249 | 0.253 | +1.8% (-12.4 to +16.0) | +4.8% (-74.9 to +84.5) | -6.8% (-32.7 to +19.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% (-0.1 to +0.1) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | +0.0% (+0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.5 | 5.5 | +0.0% (-0.8 to +0.8) | -0.1% (-0.3 to +0.2) | -1.8% (-5.5 to +1.9) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| latency, 99th percentile (ms) | 5.61 | 5.61 | +0.0% (-0.3 to +0.4) | -0.1% (-0.4 to +0.2) | -0.3% (-1.1 to +0.4) | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 0.738 | 0.74 | +0.2% (-1.9 to +2.4) | -0.1% (-0.5 to +0.3) | -0.7% (-3.2 to +1.7) | STEADY, under the floor (the three runs' mean 0.21%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory used, mean (MB) | 199.8 | 199.9 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.02%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0876 | 0.101 | +15.2% (-22.0 to +52.5) | -19.2% (-65.1 to +26.6) | -10.7% (-105.3 to +83.9) | **the runs disagree** |
| host CPU-seconds | 61.2 | 71.4 | +16.7% (-24.7 to +58.0) | -21.3% (-72.8 to +30.1) | -11.7% (-111.5 to +88.2) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.256 | 0.299 | +16.7% (-24.7 to +58.1) | -21.3% (-72.7 to +30.1) | -11.7% (-111.5 to +88.2) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,471 | 1,470 | -0.1% (-0.5 to +0.4) | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.981 | 0.981 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 0.236 | 0.257 | +8.7% (-42.5 to +59.9) | -1.5% (-3.5 to +0.5) | +0.8% (-0.2 to +1.7) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.73 | 5.76 | +0.5% (-2.0 to +2.9) | -0.1% (-0.3 to +0.1) | +0.1% (-0.1 to +0.2) | STEADY, under the floor (the three runs' mean 0.13%) |
| latency, mean (ms) | 0.288 | 0.302 | +4.8% (-25.0 to +34.5) | -0.6% (-2.1 to +1.0) | -0.1% (-0.1 to -0.1) | **the runs disagree** |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory used, mean (MB) | 348.5 | 348.5 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.115 | -3.4% (-67.9 to +61.2) | -15.2% (-51.8 to +21.5) | -11.5% (-43.8 to +20.8) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 204.1 | 196.3 | -3.8% (-74.8 to +67.1) | -16.5% (-56.3 to +23.3) | -12.8% (-48.9 to +23.4) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.308 | 0.297 | -3.7% (-74.9 to +67.4) | -16.5% (-56.3 to +23.3) | -12.8% (-48.9 to +23.3) | **GAIN by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.783 | 0.783 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.65 | 5.65 | -0.0% (-0.3 to +0.3) | +0.0% (-0.1 to +0.1) | -0.0% (-0.5 to +0.5) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, 99th percentile (ms) | 5.72 | 5.72 | +0.0% (-0.1 to +0.2) | -0.0% (-0.1 to +0.1) | +0.0% (-0.4 to +0.4) | STEADY, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 1.35 | 1.35 | +0.1% (-0.2 to +0.4) | -0.1% (-0.2 to +0.0) | -0.0% (-0.6 to +0.6) | STEADY, under the floor (the three runs' mean 0.01%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | STEADY, the same |
| memory used, mean (MB) | 257.3 | 257.3 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | STEADY, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.126 | 0.131 | +4.1% (-20.6 to +28.8) | -7.1% (-15.3 to +1.1) | -7.2% (-28.4 to +13.9) | **the runs disagree** |
| host CPU-seconds | 213.4 | 223.6 | +4.8% (-24.0 to +33.6) | -8.1% (-17.7 to +1.4) | -8.1% (-32.0 to +15.8) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.404 | 0.424 | +4.8% (-24.0 to +33.6) | -8.1% (-17.7 to +1.4) | -8.1% (-32.0 to +15.8) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 4 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 24 STEADY, 8 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
