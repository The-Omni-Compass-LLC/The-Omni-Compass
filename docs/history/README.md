# Dated records

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Any commercial use requires a signed,
> paid Omni-Compass Enterprise License. See [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE).

Each page here is kept as written on its date. None is current: where one differs from
[`../STATE_OF_PLAY.md`](../STATE_OF_PLAY.md) or [`../../results/OMNI_INDEX.md`](../../results/OMNI_INDEX.md), those govern.

| Page | What it was |
|---|---|
| [`BENCHMARK_REPORT.md`](BENCHMARK_REPORT.md) | The September 2026 benchmark report |
| [`OMNICOMPASS_ABC_REPORT.md`](OMNICOMPASS_ABC_REPORT.md) | Omni-Compass against other cluster platforms, before the on-top design |
| [`OMNICOMPASS_BUYER_EDITION.md`](OMNICOMPASS_BUYER_EDITION.md) | The buyer edition of that report |
| [`CONSENSUS_AUDIT.md`](CONSENSUS_AUDIT.md) | The five-reviewer consensus audit |
| [`ENGINE_AUDIT.md`](ENGINE_AUDIT.md) | The engine read line by line against what runs |
| [`HANDOFF_CHAPTER.md`](HANDOFF_CHAPTER.md), [`HANDOFF_EARLIER.md`](HANDOFF_EARLIER.md) | Earlier handoff notes |
| [`PROBLEM_MAP_2026-09.md`](PROBLEM_MAP_2026-09.md) | The September 2026 problem map |
| [`AMENDMENT_RISING_STEP_CAP.md`](AMENDMENT_RISING_STEP_CAP.md) | A proposed amendment, declined |
| [`V3_SYSBENCH_set1.md`](V3_SYSBENCH_set1.md) | MySQL under sysbench, the first counted set (8 October 2026): every row inside the noise; the hand-back read NO on 15 of 45 omni arms through the plug's restore, fixed and rerun as the second set, which `results/live/V3_SYSBENCH.md` carries |
| [`V3_SYSBENCH_set2.md`](V3_SYSBENCH_set2.md) | MySQL under sysbench, the second counted set (8 October 2026): the pool −67% on burst and −50% to −56% on read_only, read_write's pages holding data +53% to +70% worse; superseded by the third set on amendment 2 (the pool grows only while missing) |
| [`V3_PGBENCH_set1.md`](V3_PGBENCH_set1.md) | PostgreSQL behind PgBouncer, the first counted set (6 October 2026): connections −61% to −72% with host CPU +14% to +28% worse; the CPU was later measured as the harness's own psql launches and the set was superseded by the second on amendment 2 (one console connection, the queue line) |
| [`V3_YCSB_set1.md`](V3_YCSB_set1.md) | MongoDB under YCSB, the first counted set (8 October 2026): the cache −41% to −49% on c and burst with the burst mean latency +2% to +4% worse; the give-back had emptied a cold cache before its first eviction, and the set was superseded by the second on amendment 1 (the miss-share gate) |
| [`OMNI_COMPASS_TECHNICAL_MANUAL.pdf`](OMNI_COMPASS_TECHNICAL_MANUAL.pdf) | The earlier technical manual |
| [`xpass/`](xpass) | The earlier XPASS package indexes |
