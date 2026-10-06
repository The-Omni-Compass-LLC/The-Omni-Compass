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

## The tuning run (2026-10-06, run 37420052827; rules frozen above, nothing changed after it)

Three paired repetitions of `tpcb` on a GitHub runner (4 cores), 64 clients, the base rate from native's own unlimited
capacity (5,626 transactions a second, peak notch 90% of it). Not counted; the untouched workloads follow.

| Gauge | native | omni | reading |
|---|---:|---:|---|
| server connections alive, mean (the machines) | 20.0 | 9.3 | better (−53%, interval −57% to −50%) |
| work inside the 50 ms line (tps) | 2,137 | 2,152 | no difference beyond the noise |
| throughput (tps) | 2,437 | 2,474 | no difference beyond the noise |
| latency p95 (ms) | 1,361 | 433 | no difference beyond the noise (native's own p95 swung from 86 to 3,331 ms between repetitions) |
| latency p99 / median (ms) | 2,888 / 0.98 | 862 / 1.09 | no difference beyond the noise |
| failed transactions | 0 | 0 | same |
| host CPU-seconds | 433 | 480 | **worse** (+11%, interval +8% to +14%) |
| CPU-seconds per 1,000 transactions inside the line | 0.68 | 0.74 | no difference beyond the noise |
| pool size, mean (the knob) | 20 | 9.5 | shown |

The knob was handed back and read back at the end of every omni arm; Omni wrote 161 to 175 times an arm and failed up
9 times an arm. Read: on a shared 4-core runner the latencies are too noisy for three repetitions to tell the arms
apart, native's own p95 varying forty-fold between repetitions; what did separate is the machines, half as many database
connections held open for the same work, and the host's CPU, 11% more of it, which is the cost of PgBouncer queueing
clients behind a smaller pool. Both go into the untouched runs as they are; nothing in the rule changes.

## The first untouched run, and amendment 1 (2026-10-06, run 37425853293; declared before the counted runs)

The three untouched workloads ran once on the rule above (run 37425853293, three paired repetitions each). The result is
kept here as it came, and it is a loss:

| Workload | Work inside the line | Throughput | p95 (ms) | Servers alive | Host CPU-seconds |
|---|---|---|---|---|---|
| `select` (read-only) | 11,423 → 5,995 tps, **worse** | 11,428 → 10,373, **worse** | 4 → 3,886, **worse** | 19.2 → 2.5 | −1%, better |
| `simple_update` | no difference beyond the noise | no difference beyond the noise | 65 → 554, no difference beyond the noise | 20 → 8.1, better | +10%, **worse** |
| `tpcb_hot` (two branches) | no difference beyond the noise | no difference beyond the noise | 8 → 54, no difference beyond the noise | 19 → 5.3, better | +18%, **worse** |

**What happened on `select`.** The compass read the pooler's service time per transaction, 0.11 ms against a 50 ms
line, and gave back one idle connection a second until the pool stood at its floor of two (18 writes an arm, no fail-up).
Two connections serve about 15,500 read-only transactions a second; the peak notch offered 23,400. The backlog did not
show at the pooler: a client with a transaction in flight is served in 0.1 ms, and the time it spent behind its own
schedule waiting to send is not the pooler's to see. So the pooler's clock said calm while the users' p95 went from
4 ms to 3.9 s. The rule was blind to the one thing that mattered, and the preregistration had said so in one line
("the pooler cannot see time a client spends behind its own schedule") without drawing the consequence.

**Amendment 1 (`tools/run_pgbench.py`, `service_reading`, `decide`).** Two changes, declared here before any counted run:

1. **The reading** is the pooler's service time per transaction **or the share of its clients queued for a server**
   (`SHOW POOLS`, `cl_waiting / (cl_active + cl_waiting)`) scaled to the line, whichever is worse. A pool too small for
   the offered rate shows at the pooler as clients waiting; with every client waiting the position is past the wall and
   the knob is handed back to the pooler's own setting at once. The waiting share also decides the direction with the
   wait-time share: half or more waiting means the pool grows.
2. **The dwell holds only the brake.** Adding connections is never held, not even two seconds after a take-back (the
   gas is never held, as in every other Omni adapter); taking back waits five seconds after an add. The first rule held
   the needed add for five seconds once in the local check.

Nothing else changes: the band, the centre, the gains, the cushion, the cover [2, 90], one idle server a second on the
way down, the fail-up, the one-writer rule and the hand-back are as frozen above. Local check of the amended rule on
`select` (one short repetition, 16 clients): at the peak notch the pool held near 11 and the work inside the line and
the p95 matched native's; at the light notches the pool eased to 3. The counted runs are three new untouched runs (A, B,
C) on the amended rule; run 37425853293 stays in this file as the result the first rule produced and is not counted.

## The counted runs (2026-10-06, runs 37435740735, 37435751322, 37435761371, on amendment 1)

The three untouched workloads, three separate GitHub runs, three paired repetitions each; the table by rule is
`results/live/V3_PGBENCH.md` (`tools/pgbench_abc.py`).

| Workload | Connections held open (the machines) | Host CPU-seconds | Work inside the line, throughput, p50, p95, p99 |
|---|---|---|---|
| `select` | 19.3 → 7.5, **confirmed better** (−61% to −63% in the three runs) | **confirmed worse** (+14% to +27%) | no difference beyond the noise (3 of 3 runs) |
| `simple_update` | **the runs disagree** (+12% in one run, −34% and −35% in two) | **confirmed worse** (+18% to +28%) | no difference beyond the noise (2 or 3 of 3 runs) |
| `tpcb_hot` | 19.4 → 6.0, **confirmed better** (−69% to −72%) | **confirmed worse** (+15% to +25%) | no difference beyond the noise (2 or 3 of 3 runs) |

Failed transactions 0 and 0 in every run; the knob handed back and read back in every arm. Read: with the amended
reading the read-only collapse of the first run did not recur (work inside the line and throughput within the noise of
native's in all three runs), and Omni held a third of the connections open for the same work. The cost is real and
confirmed: the host spent 14% to 28% more CPU, which is PgBouncer queuing clients behind a smaller pool. The latencies
cannot be told apart on GitHub's shared runner, where native's own p95 moved from 3 ms to 3 s between repetitions; that
is the runner, and it is said so. Nothing in the rule changes after these runs.
