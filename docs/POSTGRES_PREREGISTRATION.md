# Databases: Omni-Compass on top of a database's own connection pooler, preregistered

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE`.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

Written 2026-10-06, before any counted run. The rules below were set on the tuning workload and are then applied
unchanged to the untouched workloads; every row is reported, losses included; the readings are the three-run readings of
`docs/OMNI_V1.md`. The runner is `tools/run_pgbench.py`, the workflow `.github/workflows/pgbench.yml`.

## Why this benchmark

PostgreSQL is the most used open-source database in the world, and PgBouncer is the connection pooler most of its
deployments put in front of it. The pooler has one setting that matters for capacity, the number of server connections
it keeps open to the database (its pool size), and it has no controller for it: the DBA sets a number once and the
pooler holds it through every quiet hour and every rush. That fixed number is the native controller here, and Omni sits
on top of it.

## What is someone else's

- **PostgreSQL 16** (the PostgreSQL Global Development Group, PostgreSQL License), as the distribution ships it, with
  its own settings untouched (`max_connections` 100, `shared_buffers` 128 MB, `synchronous_commit` on).
- **PgBouncer 1.22** (the PgBouncer project, ISC License), in transaction pooling, with the pool size it ships with,
  **20 server connections** (`default_pool_size`), and every other setting as shipped.
- **pgbench** (PostgreSQL's own benchmark, shipped with PostgreSQL): the TPC-B-like default script and its `-S` and
  `-N` variants, its per-transaction log (`-l`) for the latencies, its rate limiter (`-R`) for the offered load.
- **The machine:** a GitHub Actions runner (4 cores) in the counted runs. There is no watt-meter on it.

Nothing here models a database. Omni writes one setting through PgBouncer's own admin console (`SET default_pool_size`)
and reads what PgBouncer itself reports (`SHOW STATS`, `SHOW POOLS`, `SHOW CONFIG`).

## Arms

- **native:** PostgreSQL behind PgBouncer's shipped pool of 20, pgbench offering the load.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the pool size**, inside the
  cover [2, 90]: never under two server connections (the floor of two), never within ten of PostgreSQL's 100
  connections. Everything else is native's.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the service time per transaction as the pooler itself reports it: the change in
  `total_xact_time` plus the change in `total_wait_time` (clients waiting for a server) over the change in
  `total_xact_count` since the last second. No transaction in a second reads as calm (0).
- **Band.** From 0 to the response line, **50 ms** a transaction. The compass pulls the reading to 40% of the line
  (20 ms), the service profile of the Kubernetes adapter, with its usual gains (kp 1.0, response time 2 s, smoothing
  0.5, one decision a second).
- **Direction.** Where the time goes decides what a positive force (the service slow) does: if half or more of the
  time was spent **waiting for a server**, the pool grows by ceil(force / 0.10) slots this second (full force adds ten);
  if the time was spent **inside the server**, the pool shrinks by one (fewer backends fighting for the same cores and
  rows). A negative force (calm) gives back **one idle server a second**, and only when PgBouncer shows an idle server
  to give back (`sv_idle` ≥ 1): a server in use is never taken.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Dwell.** No reversal of direction within five seconds.
- **Fail up.** At 95% of the line the knob is handed back to the pooler's own setting (20) at once; the compass then
  resumes.
- **One writer.** If the knob is found at a value Omni did not write, Omni stops writing (the plug contract).
- **Reset.** At the end of every omni arm the knob is restored to the snapshot taken at the start and read back;
  the report says whether every arm was handed back.

Disclosed: the pooler cannot see time a client spends behind its own schedule before it sends a transaction. The compass
reads the pooler's view; the gauges below read the user's view from pgbench's own log, lag included.

## The load

pgbench with **64 client connections** to the pooler (more clients than native's 20 servers, as a pooled deployment
has), rate-limited, the offered rate stepping one notch at a time: **1 2 3 2 3 4 5 6 5 4 3 2 1 2 1**, 20 s a notch,
300 s an arm. The base rate is set **once per workload before the counted runs, in native mode**: one 20 s run with no
rate limit gives native's unlimited capacity, and the peak notch (6) offers nine tenths of it, so native is at its knee
and not past it (past the knee both arms fall behind the schedule, which says nothing about a controller). Each arm
starts from the pooler's own setting after a 5 s uncounted warm-up at the base rate. The two arms alternate order
between repetitions.

## Gauges (from pgbench's log, PgBouncer's `SHOW POOLS`, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: transactions a second whose latency (lag included) was within 50 ms | **higher is better** (the product number) |
| throughput (transactions a second) | higher is better |
| latency: median, 95th and 99th percentile, mean (ms, lag included) | lower is better |
| failed transactions | **any increase is WORSE** |
| server connections alive, mean and most at once (the machines) | lower is better |
| host CPU busy share, host CPU-seconds, CPU-seconds per 1,000 transactions inside the line | lower is better; measured, not modelled (evidence class L) |
| pool size, mean | shown, not judged |

**No energy is claimed.** A GitHub runner has no watt-meter; the host's CPU-seconds are a real measurement of the
machine's work and are reported as such, nothing more.

A change under one part in a million reads "same".

## Workloads

- **Tuning workload:** `tpcb`, pgbench's TPC-B-like default script at scale 20 (20 branches). The band, the direction
  rule, the cushion, the dwell and the floor and ceiling above were set on it; nothing else is tuned.
- **Untouched workloads:** `select` (select-only, `-S`, scale 20: read-heavy), `simple_update` (`-N`, scale 20: the
  default script without the branch and teller updates), `tpcb_hot` (the default script at scale 2: two branches,
  every transaction fighting for the same rows).

Each workload gets its own native calibration of the base rate, by the rule above.

## Runs

Each workload: **three paired repetitions** (native and omni, alternating order) in one GitHub Actions job; the
paired difference's 95% interval over the repetitions decides whether a change is beyond the noise within that run.
Three separate runs on the frozen engine (A, B, C); the three-run table reads confirmed better or confirmed worse when
the sign holds and every run's interval is clear of zero, no difference beyond the noise when a run's interval includes
zero, the runs disagree when clear runs point different ways. Two workloads run at a time, so the other benchmarks keep
their runners.

## What the first smoke already showed, said before the counted runs

One short repetition on a 4-core box, 64 clients, five notches of 4 s: omni did more work inside the line (1,400 against
1,312 transactions a second), its 95th-percentile latency over the whole profile was lower (24.5 against 77.2 ms) and
it kept 11 server connections alive against native's 20. At the peak notch the pool had been taken back to about 10,
and fewer backends on four cores answered faster than twenty. **At the lightest notch omni's p95 was higher (14.6
against 3.9 ms, inside the line)** because the pool had been given back to two or three: the expected cost of the
take-back at light load, stated here in advance. One repetition proves nothing; the counted runs will show whatever they
show, that row included.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone.
