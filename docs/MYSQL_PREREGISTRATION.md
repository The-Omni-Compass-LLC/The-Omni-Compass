# sysbench on MySQL: Omni-Compass on top of a database's operator-set buffer pool, preregistered

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE`.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

Written 2026-10-08, before any counted run. The rules below are set on the tuning workload (run on one machine, never counted)
and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings are the three-run
readings of `docs/OMNI_V1.md`. The runner is `tools/run_sysbench.py`, the workflow `.github/workflows/sysbench.yml`, the three-run
table `tools/sysbench_abc.py`. This is register row 24 (databases and caches at large), its second store after MongoDB; the row
named HammerDB's TPC-C for MySQL, and sysbench's published OLTP workloads are run first because Ubuntu ships sysbench as its own
package (one less thing fetched from outside), with TPC-C through HammerDB to follow.

## Why this benchmark

The InnoDB buffer pool is the one cache every MySQL operator sizes, once, at installation, for the machine they had and the
working set they expected; MySQL's own shipped default is 128 MB, and the setting is changed online, in whole chunks, by one
statement through the server's own console. The working set moves: a report widens it, a quiet hour narrows it. Too small a pool
reads pages from the file system on every touch; too large a pool holds memory the machine's other tenants could use. The fixed
pool is the native controller here, and Omni-Compass sits on top of it with sysbench's published OLTP workloads asking the
questions. It is the mirror of the MongoDB test with the most common database in the world: the same plug, the same rule, a
different engine's console.

## What is someone else's

- **MySQL 8.0 as Ubuntu ships it** (Oracle's MySQL Community Server from Ubuntu's own `mysql-server` package), one server on the
  machine, its configuration as shipped but for the settings an operator sets for InnoDB: the buffer pool, **512 MB**
  (`innodb_buffer_pool_size`; MySQL's own default is 128 MB, and 512 MB is set here so that the first notches of the working set fit
  the pool and the last do not, the same shape as the MongoDB test), the chunk the server resizes in, 128 MB (the shipped
  `innodb_buffer_pool_chunk_size`), one buffer pool instance, and the performance schema on (it is on by default; it is named so
  the reading's source is plain). The version the runner finds is recorded in every result.
- **sysbench** (Alexey Kopytov's sysbench, GPL, as Ubuntu's own `sysbench` package ships it, version 1.0 series) with its published
  OLTP scripts as shipped (`oltp_point_select`, `oltp_read_only`, `oltp_read_write`, `oltp_update_index`); only the table count, the
  table size, the thread count, the offered rate, the run time and the request distribution (uniform, for the reason the first
  smoke run gave below) are set from the command line.
- **The machine:** a GitHub Actions runner (4 cores, 16 GB): the server and sysbench share it. There is no watt-meter on it.

Nothing here models a database. Omni-Compass writes one setting through the server's own console (`SET GLOBAL
innodb_buffer_pool_size`) and reads what the server itself reports (`SHOW GLOBAL STATUS`: the pool's pages, the pages holding data,
the pages read from disk, the resize status; `performance_schema`: the statements' own timer) and what sysbench itself records.

## The load

For each workload six tables of 1,000,000 rows each are prepared once by sysbench (about 240 MB of data and index a table), and
both arms read the same rows. Before every arm the server is restarted at the operator's configured pool and the operating
system's page cache is dropped, so both arms start cold alike. The **working set** then steps one notch at a time, **1 2 3 2 3 4 5
6 5 4 3 2 1 2 1**, 20 s a notch (the burst workload steps **1 6 1 8 1 6**): notch n lets sysbench range over the first n tables,
**drawn uniformly** (`--rand-type=uniform`), about 240 MB at notch 1 and 1.4 GB at notch 6, so the working set is the tables in
use and fits the operator's pool at the low notches and outgrows it at the high ones. sysbench offers transactions at a **fixed rate** (its `--rate`, open-loop: the next transaction is due whatever the
last one took) **from 32 threads**, the same in both arms, and counts every transaction's latency into its own histogram (buckets
about 2% apart), from which the gauges are read.

| Workload | sysbench script, as shipped | Statements a transaction | Offered a second |
|---|---|---:|---:|
| **tuning** | `oltp_point_select` (one primary-key read) | 1 | 3,000 |
| read_only | `oltp_read_only` (10 point reads, 4 range reads) | 14 | 300 |
| read_write | `oltp_read_write` (the read-only mix, 2 updates, a delete, an insert) | 18 | 200 |
| update_index | `oltp_update_index` (one indexed update) | 1 | 1,000 |
| burst | `oltp_read_only` on the burst steps | 14 | 300 |

The offered rates are chosen under the runner's capacity for each script so that the pool, not the processor, is the thing being
asked about; they are declared here and are the same in both arms.

## Arms

- **native:** MySQL at the operator's pool, 512 MB, for the whole run.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the buffer pool size**, inside the cover
  **[128 MB, 2,048 MB]** (one chunk, the server's own floor; about an eighth of the machine), moved in whole chunks of 128 MB.
  Everything else, the dataset, the transactions and the server's settings, stays the same.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the server's own mean statement latency over the last second: the performance schema's statement
  summary (`events_statements_summary_global_by_event_name`, the select, update, insert and delete rows), the timer total and the
  statement count, differenced; a second with no statements reads as calm (0).
- **Band.** From 0 to the **statement line, 0.6 ms** (a statement served from the pool is well inside; one that reads pages from
  the file system is slower). The compass pulls the reading to 40% of the line (0.24 ms), the service profile of the Kubernetes
  adapter, with its usual gains (kp 1.0, response time 2 s, smoothing 0.5, one decision a second). *Written as 1 ms before the
  first smoke run, set at 0.5 ms on the tuning workload's second smoke run and at 0.6 ms on its third, on their figures, before
  any counted run, as the MongoDB preregistration did; the figures are under "What the smoke run shows" below.*
- **Direction, and the do-no-harm gate.** A positive force (slow statements) grows the pool by ceil(force / 0.10) chunks of
  **128 MB**, **only while the pool is full** (pages holding data at 90% of its pages or more): slow statements in a pool with room to
  spare are not the pool's to mend, and the knob is left alone. A negative force (calm) **while the pool's misses are under one
  percent of its read requests in the last second** (the pool holds the working set) gives back one chunk, after a ten-second
  dwell since the last change (a shrink evicts pages, and the server's resize itself takes seconds). *Written as "no page read
  from disk in the last second" and changed on the third smoke run: InnoDB keeps stale pages resident, so a pool once filled
  never reads empty and a few new-page reads a second never stop; the operator's question is whether the pool holds the working
  set, and the miss share answers it.*
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line with the pool full, four chunks (512 MB, about a quarter of the cover) are added at once, and
  again the next second if the service is still past the wall; never past the cover.
- **One writer, and the server's own pace.** The pool size is read once before the first write (the operator's 512 MB) and read
  back after every write; the server carries a resize out asynchronously and says so (`Innodb_buffer_pool_resize_status`), and the
  plug waits for it to complete before reading back; a size found at a value Omni did not write, with no resize in progress, stops
  Omni writing (the plug contract).
- **Reset.** At the end of every omni arm the pool is handed back to the operator's 512 MB and read back; the report says whether
  every arm was handed back.

Disclosed: on this machine the data files sit in the operating system's own page cache as well, so a buffer-pool miss is a read
from memory, not a disk read; the gain available to the knob is accordingly smaller than on a machine whose data does not fit in
memory, and the result will say what it is. The MongoDB test on the same kind of machine found exactly this (`docs/YCSB_PREREGISTRATION.md`).

## Gauges (from sysbench's own histogram and summary, the server's own status, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: transactions a second answered within the **transaction line**, the statement line times the statements a transaction as the script ships it (0.6 ms for the point select and the indexed update, 8.4 ms for read-only, 10.8 ms for read-write) | **higher is better** (the product number) |
| throughput (transactions a second); queries a second | higher is better |
| latency p95, p99, mean (from the histogram) | lower is better |
| errors (sysbench's ignored errors: deadlocks and retries) | **any increase is WORSE** |
| buffer pool held, mean (the knob, the resource); pages holding data, mean | lower is better (Omni will hold more under a wide working set, and that reads WORSE) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 transactions inside the line (the compass's own cost included) | lower is better |
| pages read from disk into the pool (misses), pool size changes written | shown, not judged |

Memory held is the resource this benchmark trades; no energy is claimed beyond the host's CPU seconds (evidence class L).

## Workloads

- **Tuning workload:** `oltp_point_select`, the standard steps. The band, the direction rule and its gate, the dwell, the chunk and
  the fail-up above were set on it; nothing else is tuned. It is run and shown, and not counted.
- **Untouched workloads:** **read_only**, **read_write**, **update_index**, **burst** (read-only on the burst steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, order alternating, sysbench's own output for every notch, the
audit and the server's error log archived with the code. Three separate runs on the frozen engine (A, B, C); the table
(`tools/sysbench_abc.py`) reads confirmed better or WORSE when all three runs move the same way with every 95% interval clear of
zero, no difference beyond the noise when a run's interval includes zero, and the runs disagree when clear runs point different
ways. `tests/test_run_sysbench.py` and `tests/test_sysbench_abc.py`, run by `verify.py`, prove the rules without a server.

## What the smoke run shows, said before the counted runs

A one-repetition run of the tuning workload on GitHub's machine exercises the harness end to end before any counted run; its
result is recorded here when it has run, and it is not counted.

- **First smoke run (37745096028, 2026-10-08 07:42 UTC): ran end to end on the first try, and showed the design did not
  reach the pool.** MySQL 8.0.46 from Ubuntu's package, sysbench 1.0.20; both arms answered about 2,930 transactions a second
  inside the line with a mean of 0.18 to 0.22 ms and a p95 of 0.24 to 0.39 ms at every notch; native's pages holding data
  reached 496 MB of its 512 MB only at the top notch and its pages read from disk were 34,524 over the whole arm, 3.8% of its
  900,194 reads; omni, seeing calm and nothing read from disk, gave one chunk back in the first notch (512 to 384 MB) and
  then held, its own misses 31,220, and handed the pool back. The cause is sysbench's shipped request distribution,
  `special`, which sends three quarters of the requests to one percent of the rows, so the hot set stayed in a few dozen
  megabytes whatever the tables in use; a benchmark in which the working set never reaches the operator's pool has nothing
  for the knob to do and would read as a free memory saving, which is not the question. The same fault the YCSB test met
  in its zipfian draw, met here in sysbench's. The one change, made here before any counted run: **rows are drawn
  uniformly over the tables in use** (`--rand-type=uniform`), so the working set is the tables in use; the scripts' operation
  mixes stay as shipped. A second smoke run follows; the statement line is confirmed or changed here on its figures before
  the counted runs. Nothing in the rules, the gauges or the workloads changed.
- **Second smoke run (37748144365, 08:10 UTC): the working set reached the pool, and the figures set the line.** With the
  uniform draw native's pages holding data reached 493 MB of 512 MB from the second notch on and stayed there, and its pages
  read from disk were 269,370 over the arm, 30% of its reads; omni gave one chunk back in the first notch (512 to 384 MB), held
  there with the pool full for the whole run but one chunk added and given back near the end, and read 349,742 pages from disk.
  The server's mean statement latency, by notch, in native: **0.14 to 0.17 ms** at the low notches once warm (the pool holding
  the working set), **0.20 to 0.22 ms** at the notches whose working set outgrew it (30% misses, each a read from the operating
  system's page cache); p95 0.20 to 0.23 ms when the pool held the working set and 0.47 to 0.50 ms when it did not. Against
  the 1 ms line every reading sat under 0.22 of the band, below the 0.4 center in every notch, so the compass could only ever
  read calm, the same mis-set band the MongoDB test found. **The statement line is set at 0.5 ms**, with the center unchanged
  at 0.4 (0.2 ms): the hit range (0.14 to 0.17 ms) is calm and a full pool missing a third of its reads (0.20 to 0.22 ms) is at
  or past the center and grows. The transaction lines scale with it (0.5 ms a point select or indexed update, 7 ms the
  read-only transaction, 9 ms read-write). The one repetition's whole-arm figures are recorded, not counted: work inside the
  line 2,901 a second in both arms; p95 0.40 ms in both; pool held 512 MB against 408 MB; disk reads 269,370 against 349,742;
  CPU-seconds 172.3 against 171.7; both arms handed back. A third smoke run follows to show the band at work.
- **Third smoke run (37751313605, 08:39 UTC): the band worked one way and not the other, and the figures set the gate.** With
  the 0.5 ms line omni grew the pool as the working set widened, 384 to 640, 768, 896 and 1,024 MB over the first ten notches,
  and read 116,437 pages from disk against native's 268,450 (−57%); work inside the line (2,887 against 2,885 a second), p95
  (0.41 ms in both) and the host's CPU (135.8 against 140.6 s) did not move, because a miss on this machine is a read from
  the page cache. But at the low notches on the way down, where the working set was one or two tables (240 to 480 MB), the
  pool went on growing, to 1,408 MB at a notch whose working set was 240 MB, and ended the run at 1,152 MB: the pool held
  877 MB on average against native's 512. Two causes, both in the rule as written, both fixed here on the tuning workload.
  First, the give-back gate, "no page read from disk in the last second", was never satisfied: InnoDB keeps stale pages
  resident, so a pool once filled reads full forever, and a few new-page reads a second never stop even when the working set
  fits; **the gate is now the pool's miss share, under one percent of its read requests in the last second**, which is the
  operator's own question (does the pool hold the working set?) asked of the server's own counters. Second, this runner's hit
  latency (0.20 to 0.22 ms) sat at the 0.5 ms line's center (0.20 ms), so calm reads drew a small upward force; the second
  smoke's runner read hits at 0.14 to 0.17 ms, and the difference between runners is as large as the difference a notch of
  misses makes (0.05 to 0.06 ms). **The statement line is set at 0.6 ms** (center 0.24 ms), above the hit range seen on both
  runners and under the miss-heavy range of this one (0.25 to 0.27 ms); on a runner like the second smoke's the compass will
  read calm throughout and the miss-share gate will hold the pool at the working set, which is the right answer there. The
  transaction lines scale with it (0.6 ms a point select or indexed update, 8.4 ms read-only, 10.8 ms read-write). The one
  repetition's whole-arm figures are recorded, not counted. A fourth smoke run follows; the counted runs begin on its figures
  if the pool follows the working set both ways. Nothing else in this document changed.
- **Fourth smoke run (37754681298, 09:09 UTC): the pool followed the working set both ways, and the rules stand.** On a
  faster runner than the first three (hits 0.06 to 0.08 ms, miss-heavy notches 0.11 to 0.13 ms, every reading well under the
  0.24 ms center), omni gave the pool back to 256 MB at the first notch, grew it to 896 MB on the cold start of the second
  (the first reads of each table come from the file system before the page cache has them, and those are slow: a fail-up on
  a real stall), gave back to 512 MB as the misses fell under one percent, grew again to 640 and then 1,024 MB as the tables
  in use widened to four, five and six, and gave back chunk by chunk to 256 MB as they narrowed to one, ending where the
  working set was. The one repetition's whole-arm figures, recorded and not counted: work inside the line 2,936 against
  2,945 a second (−0.3%); p95 0.24 against 0.23 ms; pool held 672 against 512 MB (+31%); pages read from disk 189,773 against
  268,721 (−29%); host CPU-seconds 86.3 against 92.1 (−6%); both arms handed back. One figure is the knob's own cost and the
  gauges will carry it: at one notch the mean latency read 0.57 ms against a p95 of 0.26 ms, a heavy tail from the server's
  own stall while it resized the pool; the mean-latency row is where that shows, and it will be judged like every other row.
  Two things are declared on these figures before the counted runs. The hit latency of GitHub's runners ranges from 0.06 to
  0.22 ms across the four smoke runs, so on a fast runner the compass reads calm throughout and the pool is governed by the
  miss-share gate and the fail-up alone; on a slow runner the center also bites; both are the same rule applied to what the
  server reports, and the counted runs will pool them as they come. And the memory the governor holds over a whole run may
  read above native's (it buys pool for the wide notches and gives it back for the narrow ones), which the resource row will
  show as WORSE if it does; the question the benchmark asks is whether the misses it saves bought any service, and the work,
  p95 and CPU rows answer it. **The counted runs A, B and C begin on these rules, unchanged from here.**

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
