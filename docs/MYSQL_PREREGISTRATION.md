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
  table size, the thread count, the offered rate and the run time are set from the command line.
- **The machine:** a GitHub Actions runner (4 cores, 16 GB): the server and sysbench share it. There is no watt-meter on it.

Nothing here models a database. Omni-Compass writes one setting through the server's own console (`SET GLOBAL
innodb_buffer_pool_size`) and reads what the server itself reports (`SHOW GLOBAL STATUS`: the pool's pages, the pages holding data,
the pages read from disk, the resize status; `performance_schema`: the statements' own timer) and what sysbench itself records.

## The load

For each workload six tables of 1,000,000 rows each are prepared once by sysbench (about 240 MB of data and index a table), and
both arms read the same rows. Before every arm the server is restarted at the operator's configured pool and the operating
system's page cache is dropped, so both arms start cold alike. The **working set** then steps one notch at a time, **1 2 3 2 3 4 5
6 5 4 3 2 1 2 1**, 20 s a notch (the burst workload steps **1 6 1 8 1 6**): notch n lets sysbench range over the first n tables,
about 240 MB at notch 1 and 1.4 GB at notch 6, so the working set fits the operator's pool at the low notches and outgrows it at
the high ones. sysbench offers transactions at a **fixed rate** (its `--rate`, open-loop: the next transaction is due whatever the
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
- **Band.** From 0 to the **statement line, 1 ms** (a statement served from the pool is well inside; one that reads pages from the
  file system is slower). The compass pulls the reading to 40% of the line (0.4 ms), the service profile of the Kubernetes adapter,
  with its usual gains (kp 1.0, response time 2 s, smoothing 0.5, one decision a second). *The statement line is to be confirmed or
  changed on the tuning workload's smoke run, on its figures, before any counted run, as the MongoDB preregistration did; the change,
  if any, will be written here with the figures.*
- **Direction, and the do-no-harm gate.** A positive force (slow statements) grows the pool by ceil(force / 0.10) chunks of
  **128 MB**, **only while the pool is full** (pages holding data at 90% of its pages or more): slow statements in a pool with room to
  spare are not the pool's to mend, and the knob is left alone. A negative force (calm) with **no page read from disk in the last
  second** gives back one chunk, after a ten-second dwell since the last change (a shrink evicts pages, and the server's resize
  itself takes seconds).
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
| work inside the response line: transactions a second answered within the **transaction line**, the statement line times the statements a transaction as the script ships it (1 ms for the point select and the indexed update, 14 ms for read-only, 18 ms for read-write) | **higher is better** (the product number) |
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

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
