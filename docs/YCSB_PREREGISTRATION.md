# YCSB on MongoDB: Omni-Compass on top of a database's operator-set cache size, preregistered

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE`.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

Written 2026-10-08, before any counted run. The rules below are set on the tuning workload (run on one machine, never counted)
and are then applied unchanged to the untouched workloads; every row is reported, losses included; the readings are the three-run
readings of `docs/OMNI_V1.md`. The runner is `tools/run_ycsb.py`, the workflow `.github/workflows/ycsb.yml`, the three-run table
`tools/ycsb_abc.py`. This is register row 24 (databases and caches at large), the first of its three stores.

## Why this benchmark

A database's storage engine keeps a cache of the pages it works on, and an operator sizes that cache once, at installation, for
the machine it had and the working set it expected. The working set moves: a report widens it, a quiet hour narrows it. Too small
a cache reads pages from the file system on every touch; too large a cache holds memory the machine's other tenants could use. The
fixed cache size is the native controller here, and Omni-Compass sits on top of it with YCSB, the published cloud-serving
benchmark, asking the questions.

## What is someone else's

- **MongoDB** (MongoDB, Inc.; the 8.0 series as its publisher distributes it for Ubuntu, installed from the publisher's own
  repository signed by the publisher's key), one server on the machine, its configuration as shipped but for the one setting an
  operator sets for the storage engine: the WiredTiger cache, **512 MB** (`storage.wiredTiger.engineConfig.cacheSizeGB`). The
  version the runner installs is recorded in every result.
- **YCSB 0.17.0, the MongoDB binding** (the Yahoo! Cloud Serving Benchmark, Apache License 2.0), fetched from the project's
  GitHub release and checked against the SHA-256 recorded here before any run:
  `6a054a706812269c80bfc6ed1e83457990c1c60b01f5083c873aaed05577e30d`. Its core workloads are run as the project ships them
  (record size, field counts, read and update mixes, the zipfian request distribution); only the key space, the rate, the thread
  count and the measurement type are set from the command line.
- **The machine:** a GitHub Actions runner (4 cores, 16 GB): the server and YCSB share it. There is no watt-meter on it.

Nothing here models a database. Omni-Compass writes one setting through the server's own console (`setParameter
wiredTigerEngineRuntimeConfig cache_size`) and reads what the server itself reports (`serverStatus`: the cache configured, the bytes
in it, the pages read into it, and its own operation latencies) and what YCSB itself records.

## The load

For each workload the dataset is loaded once (YCSB's own `load`, 1 KB records, as many as the highest notch needs), and both
arms read the same records. Before every arm the server is restarted at the operator's configured cache and the operating
system's page cache is dropped, so both arms start cold alike. The **key space** then steps one notch at a time, **1 2 3 2 3 4 5 6 5
4 3 2 1 2 1**, 20 s a notch (the burst workload steps **1 6 1 8 1 6**): notch n lets YCSB's distribution range over the first n ×
250,000 records, about 275 MB in the cache at notch 1 and 1.6 GB at notch 6, so the working set fits the operator's cache at the
low notches and outgrows it at the high ones. YCSB offers **3,000 operations a second from 32 threads** at every notch, the same in
both arms, and records every operation's latency (`measurementtype=raw`).

## Arms

- **native:** MongoDB at the operator's cache, 512 MB, for the whole run.
- **omni:** the same, with the compass law (`omnicompass/compass_law.py`) on **one knob, the cache size**, inside the cover
  **[256 MB, 2,048 MB]** (the server's own floor; a quarter of the machine). Everything else, the dataset, the operations and the
  server's settings, stays the same.

## The omni rule (frozen on the tuning workload)

- **Reading.** Once a second, the server's own mean read latency over the last second: `serverStatus().opLatencies.reads`, the
  latency total and the operation count, differenced; a second with no reads reads as calm (0).
- **Band.** From 0 to the response line, **2 ms** (a read served from the cache is well inside; a read that misses the cache
  and comes from the file system is slower). The compass pulls the reading to 40% of the line (0.8 ms), the service profile of
  the Kubernetes adapter, with its usual gains (kp 1.0, response time 2 s, smoothing 0.5, one decision a second).
- **Direction, and the do-no-harm gate.** A positive force (slow reads) grows the cache by ceil(force / 0.10) notches of
  **64 MB**, **only while the cache is full** (bytes in the cache at 90% of its size or more): slow reads in a cache with room to
  spare are not the cache's to mend, and the knob is left alone. A negative force (calm) with **no page evicted in the last second**
  gives back one notch of 64 MB a second, after a five-second dwell since the last growth.
- **Cushion.** A force inside ±0.05 moves nothing.
- **Fail up.** At 95% of the line with the cache full, a quarter of the cover (448 MB) is added at once, and again the next
  second if the service is still past the wall; never past the cover.
- **One writer.** The cache size is read once before the first write (the operator's 512 MB) and read back after every write; a
  size found at a value Omni did not write stops Omni writing (the plug contract).
- **Reset.** At the end of every omni arm the cache size is handed back to the operator's 512 MB and read back; the report says
  whether every arm was handed back.

Disclosed: on this machine the data files sit in the operating system's own page cache as well, so a WiredTiger cache miss is a
read from memory and a decompression, not a disk read; the gain available to the knob is accordingly smaller than on a machine
whose data does not fit in memory, and the result will say what it is.

## Gauges (from YCSB's own records, the server's own serverStatus, the host's `/proc/stat`)

| Gauge | Direction |
|---|---|
| work inside the response line: operations a second answered within 2 ms (YCSB's own client-side latency) | **higher is better** (the product number) |
| throughput (operations a second) | higher is better |
| latency p95, p99, mean | lower is better |
| failed operations (YCSB's own count) | **any increase is WORSE** |
| cache size held, mean (the knob, the resource); bytes in the cache, mean | lower is better (Omni will hold more under a wide working set, and that reads WORSE) |
| host CPU busy share, CPU-seconds, CPU-seconds per 1,000 operations inside the line (the compass's own cost included) | lower is better |
| pages read into the cache (misses), cache size changes written | shown, not judged |

Memory held is the resource this benchmark trades; no energy is claimed beyond the host's CPU seconds (evidence class L).

## Workloads

- **Tuning workload:** YCSB workload A (50% reads, 50% updates, zipfian), base 250,000 records, the standard steps. The band,
  the direction rule and its gate, the dwell, the notch and the fail-up above were set on it; nothing else is tuned. It is run
  and shown, and not counted.
- **Untouched workloads:** **b** (workload B, 95% reads), **c** (workload C, 100% reads), **f** (workload F, read-modify-write),
  **burst** (workload B on the burst steps 1 6 1 8 1 6).

## Runs

Each workload: three paired repetitions in one GitHub Actions job, order alternating, YCSB's per-operation records, the audit
and the server log archived with the code (raw files over 20 MB are left out of the artifact; their gauges are in the arm's
record). Three separate runs on the frozen engine (A, B, C); the table (`tools/ycsb_abc.py`) reads confirmed better or WORSE
when all three runs move the same way with every 95% interval clear of zero, no difference beyond the noise when a run's interval
includes zero, and the runs disagree when clear runs point different ways. `tests/test_run_ycsb.py` and `tests/test_ycsb_abc.py`,
run by `verify.py`, prove the rules without a server.

## What the smoke run shows, said before the counted runs

A one-repetition run of the tuning workload on GitHub's machine exercises the harness end to end before any counted run; its
result is recorded here when it has run, and it is not counted.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
