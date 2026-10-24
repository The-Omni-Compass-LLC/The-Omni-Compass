# YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (`tools/reread_key.py`; the one rule, `tools/readings.py` judge_runs): a change of 0.5% or more either way is a change and never reads EVEN. It reads its word by what the gauge is for, written "in all three of our runs" when all three runs moved 0.5% or more the same way with every interval clear of zero, and otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three were clear of the noise); under 0.5% in every run it reads EVEN, under the floor. Only the Reading cells and the counts under them were rewritten, from the JSON twin's exact values; every row, run and number is as first written. Where a paragraph below states the rule this table was first written by (a run whose interval included zero read EVEN whatever its size), this rule replaces it.
<!-- end: read again -->

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

MongoDB exactly as shipped, its WiredTiger cache at the server's own default, is native: above the cover the knob is at its limit on native, and omni reads and writes nothing (`docs/YCSB_PREREGISTRATION.md`, amendment 4); otherwise omni is the compass law on the cache size through the server's own console inside [256, 2,048] MB, holding the server's own mean read latency at 40% of the 1 ms line(`docs/YCSB_PREREGISTRATION.md`). YCSB's published core workloads ask for records from a key space that steps through the cache and past it, the same operations in both arms. Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with every interval clear of zero across the three runs, make a reading **GAIN** or **LOSS in all three of our runs** (judged by what the gauge is for, never by its sign; a resource spent that rose reads **power given**) a run whose interval includes zero reads **EVEN, no difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs disagree**. Failed operations: any rise in any run reads **LOSS in at least one of our runs**. Memory held is the resource; the host's CPU-seconds, the compass's own cost included, are measured on GitHub's shared runner, and no energy is claimed beyond them. The tuning workload is shown and not counted. Every row is shown, LOSS included.

| Run | GitHub run | Commit | Engine | Workloads |
|---|---|---|---|---:|
| A | 39383000915 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 5 |
| B | 39414286889 | `690b955b1c2a` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 3 |
| C | 39463721089 | `6f4be24ffb43` | omni-v12 (digest d38b58fbe28939b8, 47 files) | 2 |

## tuning

> not in every run: C lack it.

## b: YCSB workloadb, 250,000 records × notch; line 1 ms, 3 paired repetitions a run

MongoDB 8.0.34, YCSB 0.17.0; 3,000 operations a second offered from 32 threads; steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s; native's cache as shipped 7482 MB, the cover 256 to 2048 MB.

| Gauge | native (A) | omni (A) | A | B | C | Reading |
|---|---:|---:|---:|---:|---:|---|
| work inside the response line (operations a second answered within the line) | 2,929 | 2,928 | -0.1% (-0.1 to -0.0) | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.05%) |
| throughput (operations a second) | 2,931 | 2,930 | -0.0% (-0.1 to -0.0) | +0.0% (-0.1 to +0.1) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.04%) |
| latency, 95th percentile (ms) | 0.245 | 0.25 | +1.9% (+0.7 to +3.1) | +2.3% (-5.0 to +9.6) | -0.4% (-2.6 to +1.7) | **LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the floor; 1 of 3 clear of the noise) |
| latency, 99th percentile (ms) | 0.391 | 0.396 | +1.3% (-1.5 to +4.0) | -0.2% (-0.7 to +0.3) | -0.2% (-4.8 to +4.4) | **LOSS** (1 of 3 runs moved 0.5% or more, 2 under the floor; 0 of 3 clear of the noise) |
| latency, mean (ms) | 0.0854 | 0.0878 | +2.8% (-0.9 to +6.5) | +0.3% (-1.3 to +1.8) | -0.8% (-2.6 to +1.1) | **the runs disagree** |
| failed operations | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | EVEN, the same |
| cache size held, mean (MB; the knob, the resource) | 7,482 | 7,482 | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | EVEN, the same |
| bytes in the cache, mean (MB) | 1,366 | 1,367 | +0.1% (-0.1 to +0.2) | +0.0% (-0.0 to +0.1) | -0.0% (-0.2 to +0.1) | EVEN, under the floor (every run under 0.5%; the largest 0.05%) |
| pages read into the cache (misses) | 61,784 | 61,887 | +0.2% (-0.2 to +0.5) | +0.1% (-0.3 to +0.5) | +0.1% (-0.6 to +0.7) | shown, not judged |
| host CPU busy (share of the run) | 0.101 | 0.0988 | -2.2% (-15.2 to +10.9) | -12.7% (-25.4 to +0.0) | -16.1% (-54.1 to +21.8) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds | 182.5 | 177.5 | -2.7% (-17.6 to +12.1) | -14.8% (-30.0 to +0.5) | -17.7% (-58.5 to +23.2) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| host CPU-seconds per 1,000 operations inside the line | 0.136 | 0.133 | -2.7% (-17.6 to +12.2) | -14.8% (-30.0 to +0.5) | -17.6% (-58.6 to +23.3) | **GAIN** (the same way in all three runs; 0 of 3 clear of the noise) |
| cache size changes written (the knob's moves) | 0 | 0 | +0 (+0 to +0) | +0 (+0 to +0) | +0 (+0 to +0) | shown, not judged |

The cache size handed back to native's and read back at the end of every omni arm in every run: yes.

## burst

> not in every run: C lack it.

## c

> not in every run: B lack it.

## f

> not in every run: B, C lack it.

**Across 4 untouched workloads: 3 gauge-rows GAIN (0 in all three of our runs), 2 LOSS (0 in all three of our runs), 0 power given (0 in all three of our runs), 5 EVEN, 1 where the runs disagree.**

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
