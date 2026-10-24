# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions, each with the paired difference's 95% interval. A change of 0.5% or more, the mean of the three runs, is a change (the founder's order of 24 October 2026): every run the same way and clear of zero reads **GAIN** or **LOSS in all three of our runs**, otherwise **GAIN** or **LOSS by the mean of our three runs** with the count of runs beyond the noise; the word is judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss). A mean under 0.5% reads **EVEN, under the floor**; runs that moved 0.5% or more in opposite directions read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 40062238903 | `bbf7e12f0467` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| B | 40068587953 | `dadeec62a61a` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |
| C | 40132491116 | `791ad0fd93b1` | omni-v18 (digest 1cb92edb64c4391d, 62 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,392 | 1,392 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.929 | 0.929 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.42 | 5.42 | +0.0% (-0.4 to +0.5) | -0.2% (-2.3 to +1.9) | +0.0% (-0.2 to +0.3) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, 99th percentile (ms) | 5.58 | 5.58 | +0.0% (-0.1 to +0.2) | +0.0% (-0.1 to +0.2) | +0.0% (-0.5 to +0.6) | EVEN, under the floor (the three runs' mean 0.02%) |
| latency, mean (ms) | 0.501 | 0.501 | +0.1% (-0.4 to +0.6) | +0.1% (-0.3 to +0.4) | -0.1% (-1.1 to +0.8) | EVEN, under the floor (the three runs' mean 0.00%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 333.0 | 333.1 | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0959 | 0.0981 | +2.3% (-14.3 to +18.9) | +23.5% (-18.2 to +65.2) | +0.8% (-80.6 to +82.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 169.6 | 173.9 | +2.5% (-15.8 to +20.8) | +26.3% (-20.5 to +73.1) | +1.1% (-84.9 to +87.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.271 | 0.278 | +2.5% (-15.8 to +20.8) | +26.3% (-20.5 to +73.1) | +1.1% (-84.9 to +87.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.885 | 0.885 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.63 | 5.63 | +0.1% (-0.1 to +0.3) | -0.1% (-2.2 to +2.0) | -0.2% (-0.6 to +0.1) | EVEN, under the floor (the three runs' mean 0.08%) |
| latency, 99th percentile (ms) | 5.71 | 5.71 | +0.1% (-0.2 to +0.4) | +0.1% (-0.4 to +0.5) | -0.1% (-0.4 to +0.2) | EVEN, under the floor (the three runs' mean 0.05%) |
| latency, mean (ms) | 0.771 | 0.772 | +0.2% (-0.6 to +1.0) | +0.2% (-1.4 to +1.8) | -0.3% (-0.8 to +0.3) | EVEN, under the floor (the three runs' mean 0.03%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 199.8 | 199.9 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.02%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.109 | 0.121 | +11.2% (-24.9 to +47.4) | +3.4% (-109.2 to +115.9) | +42.3% (-16.8 to +101.4) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 77.2 | 86.7 | +12.2% (-25.9 to +50.4) | +3.1% (-122.4 to +128.7) | +47.9% (-18.7 to +114.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.323 | 0.363 | +12.2% (-25.9 to +50.4) | +3.1% (-122.4 to +128.7) | +47.9% (-18.7 to +114.5) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,470 | 1,471 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.1) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, the same |
| cache hit rate | 0.981 | 0.981 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| latency, 95th percentile (ms) | 0.157 | 0.158 | +0.7% (-0.6 to +1.9) | -2.0% (-16.0 to +11.9) | +0.5% (-17.0 to +18.0) | **the runs disagree** |
| latency, 99th percentile (ms) | 5.45 | 5.45 | +0.0% (-0.0 to +0.1) | +0.0% (-0.1 to +0.1) | -0.1% (-0.7 to +0.6) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, mean (ms) | 0.229 | 0.228 | -0.3% (-1.3 to +0.7) | -0.8% (-2.7 to +1.1) | -0.2% (-5.0 to +4.6) | EVEN, under the floor (the three runs' mean 0.43%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 348.4 | 348.5 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0751 | 0.0904 | +20.4% (-28.7 to +69.6) | +2.7% (-174.4 to +179.8) | +7.8% (-54.5 to +70.1) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds | 130.4 | 160.1 | +22.8% (-32.0 to +77.6) | +3.7% (-182.3 to +189.6) | +8.5% (-60.5 to +77.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| host CPU-seconds per 1,000 requests inside the line | 0.197 | 0.242 | +22.8% (-32.0 to +77.5) | +3.6% (-182.3 to +189.5) | +8.5% (-60.5 to +77.6) | **power given by the mean of our three runs, beyond the noise in 0 of 3** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,173 | 1,173 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to -0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| cache hit rate | 0.782 | 0.782 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.00%) |
| latency, 95th percentile (ms) | 5.67 | 5.67 | -0.0% (-0.3 to +0.3) | -0.0% (-0.2 to +0.1) | -0.1% (-0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.03%) |
| latency, 99th percentile (ms) | 5.73 | 5.73 | -0.0% (-0.2 to +0.2) | -0.0% (-0.3 to +0.2) | -0.1% (-0.3 to +0.2) | EVEN, under the floor (the three runs' mean 0.04%) |
| latency, mean (ms) | 1.36 | 1.37 | +0.1% (-0.7 to +0.9) | -0.1% (-0.3 to +0.2) | -0.1% (-0.5 to +0.4) | EVEN, under the floor (the three runs' mean 0.01%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 257.3 | 257.3 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, under the floor (the three runs' mean 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.119 | 0.122 | +2.6% (-41.5 to +46.7) | -0.5% (-21.7 to +20.7) | +3.9% (+0.8 to +7.0) | **the runs disagree** |
| host CPU-seconds | 200.0 | 205.8 | +2.9% (-46.9 to +52.7) | -0.5% (-23.8 to +22.8) | +4.7% (+1.0 to +8.3) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.379 | 0.39 | +2.9% (-46.9 to +52.7) | -0.5% (-23.8 to +22.7) | +4.7% (+1.0 to +8.3) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 0 gauge-rows GAIN, 0 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 26 EVEN, 4 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
