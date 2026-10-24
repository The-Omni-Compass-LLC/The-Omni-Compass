# Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

Redis exactly as shipped (no memory ceiling, noeviction) is native: the knob is at its limit on native, and omni reads and writes nothing (`docs/REDIS_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the ceiling through Redis's own console inside [16, 512] MB, holding the application's own request latency at 40% of the 2 ms line, a hit inside and a miss with its store trip outside (`docs/REDIS_PREREGISTRATION.md`). Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by the sign of its number; a resource spent that rose reads **power given**, never a loss); a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed requests: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39826081107 | `611aad4666db` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| B | 39846960314 | `d27db5f66c71` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |
| C | 39866161041 | `5f430c111d90` | omni-v16 (digest 5c5502f12b1c0ce4, 55 files) | 4 |

## tuning: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run (the tuning workload, shown and not counted)

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,393 | 1,393 | +0.0% (-0.0 to +0.0) | -0.0% (-0.2 to +0.1) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.05%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.929 | 0.929 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| latency, 95th percentile (ms) | 5.68 | 5.67 | -0.2% (-0.4 to +0.0) | -0.1% (-0.2 to +0.1) | +0.1% (-0.1 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.20%) |
| latency, 99th percentile (ms) | 5.78 | 5.76 | -0.3% (-0.7 to +0.1) | +0.0% (-0.8 to +0.9) | +0.1% (-0.2 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.29%) |
| latency, mean (ms) | 0.568 | 0.564 | -0.7% (-1.8 to +0.5) | +0.3% (-5.4 to +6.1) | -0.0% (-1.4 to +1.3) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 333.1 | 333.1 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0883 | 0.0904 | +2.4% (-45.3 to +50.1) | -3.5% (-55.1 to +48.1) | -10.6% (-30.5 to +9.4) | **the runs disagree** |
| host CPU-seconds | 146.6 | 150.9 | +2.9% (-49.2 to +55.0) | -3.4% (-58.1 to +51.3) | -11.5% (-32.6 to +9.5) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.234 | 0.241 | +2.9% (-49.2 to +55.0) | -3.3% (-58.2 to +51.6) | -11.5% (-32.6 to +9.5) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## burst: 8192 B values, working set 2,500 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 6 1 8 1 6 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,327 | 1,327 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.1) | -0.0% (-0.2 to +0.2) | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.885 | 0.885 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| latency, 95th percentile (ms) | 5.74 | 5.75 | +0.2% (-0.4 to +0.8) | +0.0% (-0.3 to +0.4) | +0.0% (-0.3 to +0.3) | EVEN, under the floor (every run under 0.5%; the largest 0.18%) |
| latency, 99th percentile (ms) | 5.81 | 5.83 | +0.2% (-0.3 to +0.7) | +0.1% (-0.1 to +0.2) | +0.0% (-0.5 to +0.6) | EVEN, under the floor (every run under 0.5%; the largest 0.20%) |
| latency, mean (ms) | 0.819 | 0.823 | +0.5% (-0.1 to +1.1) | +0.1% (-0.5 to +0.7) | -0.7% (-3.4 to +2.0) | **GAIN** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 199.9 | 199.9 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.1) | +0.0% (-0.0 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.02%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.104 | 0.128 | +22.2% (-10.8 to +55.2) | +9.3% (-69.8 to +88.5) | -5.9% (-81.2 to +69.4) | **the runs disagree** |
| host CPU-seconds | 69.9 | 87.2 | +24.8% (-11.2 to +60.9) | +10.5% (-79.0 to +100.1) | -6.4% (-86.7 to +74.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.293 | 0.365 | +24.8% (-11.2 to +60.9) | +10.5% (-79.0 to +100.0) | -6.4% (-86.8 to +74.1) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## large: 32768 B values, working set 625 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,472 | 1,472 | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.981 | 0.981 | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| latency, 95th percentile (ms) | 0.165 | 0.167 | +1.4% (-5.8 to +8.5) | +1.7% (-3.4 to +6.7) | +1.2% (-1.0 to +3.4) | **LOSS** (the same way in all three runs; 0 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 5.48 | 5.48 | +0.0% (-0.4 to +0.5) | -0.0% (-0.2 to +0.1) | -0.1% (-0.2 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.07%) |
| latency, mean (ms) | 0.229 | 0.229 | +0.2% (-1.8 to +2.2) | +0.1% (-1.4 to +1.6) | -0.1% (-2.8 to +2.6) | EVEN, under the floor (every run under 0.5%; the largest 0.24%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 348.4 | 348.4 | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0816 | 0.0865 | +6.0% (-60.8 to +72.7) | -14.7% (-73.3 to +43.9) | +36.5% (+12.4 to +60.6) | **the runs disagree** |
| host CPU-seconds | 142.0 | 151.1 | +6.4% (-66.6 to +79.5) | -16.2% (-79.9 to +47.4) | +39.2% (+10.4 to +67.9) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.214 | 0.228 | +6.4% (-66.6 to +79.5) | -16.2% (-79.9 to +47.4) | +39.2% (+10.4 to +67.9) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

## small: 2048 B values, working set 10,000 keys × notch; line 2 ms, 3 paired repetitions a run

Redis 7.0.15; 1500 requests a second offered; a miss costs the declared 5 ms store trip; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's ceiling: none (as shipped), the cover 16 to 512 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (requests a second answered within the line) | 1,172 | 1,172 | +0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | +0.0% (-0.1 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.02%) |
| throughput (requests a second) | 1,500 | 1,500 | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | -0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.00%) |
| cache hit rate | 0.783 | 0.783 | -0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, the same |
| latency, 95th percentile (ms) | 5.21 | 5.2 | -0.1% (-0.1 to +0.0) | +0.0% (-0.3 to +0.4) | +0.1% (-0.2 to +0.4) | EVEN, under the floor (every run under 0.5%; the largest 0.06%) |
| latency, 99th percentile (ms) | 5.26 | 5.25 | -0.1% (-0.6 to +0.4) | +0.1% (-0.4 to +0.6) | +0.2% (-0.8 to +1.1) | EVEN, under the floor (every run under 0.5%; the largest 0.16%) |
| latency, mean (ms) | 1.2 | 1.2 | -0.2% (-1.3 to +1.0) | -0.0% (-0.2 to +0.2) | +0.1% (-0.8 to +1.1) | EVEN, under the floor (every run under 0.5%; the largest 0.16%) |
| failed requests | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory ceiling held, mean (MB; the knob, the resource) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| memory used, mean (MB) | 257.3 | 257.3 | +0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (-0.0 to +0.0) | EVEN, under the floor (every run under 0.5%; the largest 0.01%) |
| keys evicted | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |
| host CPU busy (share of the run) | 0.0677 | 0.0586 | -13.5% (-55.1 to +28.2) | +12.5% (-1.3 to +26.4) | -1.2% (-118.3 to +115.8) | **the runs disagree** |
| host CPU-seconds | 120.0 | 102.8 | -14.3% (-58.6 to +30.0) | +13.2% (-1.3 to +27.7) | -1.4% (-123.8 to +121.0) | **the runs disagree** |
| host CPU-seconds per 1,000 requests inside the line | 0.227 | 0.195 | -14.3% (-58.7 to +30.1) | +13.2% (-1.3 to +27.8) | -1.4% (-123.7 to +120.9) | **the runs disagree** |
| ceiling changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The ceiling handed back to native's and read back at the end of every omni arm in every run: yes.

**Across 3 untouched workloads: 1 gauge-rows GAIN (0 in all three of our runs), 1 LOSS (0 in all three of our runs), 0 power given (0 in all three of our runs), 25 EVEN, 9 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
