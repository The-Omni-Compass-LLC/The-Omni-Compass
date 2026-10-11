# Changelog

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## 2026-10-11
- **The notice as the founder ordered it (night of 10 October).** Two sentences are struck from the legal notice everywhere,
  and the notice now closes with the filing sentence and the website, nothing after it: "All patents, copyrights and
  trademarks filed in the USA. www.omni-compass.com". `tools/legal.py` holds the new wording (the page notice, the source
  header, the short line) and `--fix` wrote it into 663 files; the license papers (`LICENSE` and its SPDX copy, now revised
  11 October 2026, `NOTICE`, `DISCLOSURES.md`), the README's line under the headline, the assistants' rules files
  (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, Copilot's and Cursor's), `CITATION.cff`, `REUSE.toml`, `codemeta.json`, the SBOM,
  the manual's front matter, the old closing lines of seventeen pages and the book's page footers, back cover and copyright
  page were rewritten by hand, and the printed book was rebuilt (520 pages, neither sentence in its text). `--check`, which
  `verify.py` runs on every push, now fails any file of any kind that still carries either sentence (`RETIRED`; a new test
  in `tests/test_legal.py`). The frozen engine files never carried them: omni-v3 is unchanged and no result is read
  differently. Two frozen originals keep a different sentence, about the introductory 10% license benchmark (that the
  benchmark may change or be withdrawn): the reference engine (`reference/`, held by its recorded SHA-256 and program fingerprint) and its
  dated source snapshot (`docs/handoff/`); they change only on the founder's word. The founder's reservation of the right
  to change the software, its documentation, its results and its terms at any time, without notice, stands in plain words
  in `LICENSE` section 9 (and its SPDX copy and the SBOM), `NOTICE`, `DISCLOSURES.md` item 4, the manual and the book's
  copyright page: it was taken out with the struck sentences by mistake and put back the same night.

## 2026-10-10
- **The notice everywhere, a front page the repository writes itself, and the book for the people who wire it (evening).**
  (1) **One legal notice, written once** (`tools/legal.py`): all rights reserved; all patents, copyrights and trademarks filed
  in the USA; www.omni-compass.com; every copy, export, report and printout carries it with `LICENSE`, `NOTICE` and
  `DISCLOSURES.md`. It now stands at the top and end of every page and table,
  in the header of every script, source file and workflow, at the top and end of every workflow job's report, beside every
  file a workflow hands out (`legal-notice`), and in every zip (`tools/export_zip.py`); `verify.py` fails any push where a
  file lacks it. The 67 files locked by a fingerprint (the engine, its C++ twins, the reference engine, the pre-registered
  harness) keep their earlier header until the next engine version rewrites them. `LICENSE` revised: licensed, not sold; no
  rights by implication; feedback; lawful use and export control; severability; the filing sentence in the founder's words
  with no grant claimed; `NOTICE`, `REUSE.toml` (the third-party traces marked as theirs), the FOSSA custom-license rule, the
  SBOMs and `CITATION.cff` with it. Instruction files for every AI assistant that reads the repository (`AGENTS.md`,
  `GEMINI.md`, `.github/copilot-instructions.md`, `.cursorrules`): every answer opens and closes with the notice. Two pages
  that promised "research and non-commercial use" corrected to the license's evaluation-only terms. (2) **The front page
  writes itself**: within minutes of every finished benchmark run, and every hour, `front-page.yml` rebuilds the five live
  products' tables from their three newest runs and writes the engine on main, the index now, every table by when it last
  changed and the newest run of every benchmark; the runner's folder path is gone from its lines; its checkout keeps off the
  archive of raw runs; the old front page is kept whole in `docs/history/FRONT_PAGE_2026-10-10.md`. (3) **The package version
  follows the engine** (0.3.0 is omni-v3; `verify.py` checks it, so a changed engine cannot keep an old number). (4) **The
  manual**: the card for the glove box at the front; reading paths for the data-center operator, the engineer on call,
  security and counsel; 6.5 the reflex rule (one body, one brain); 10.11 the data center under the servers (cooling, power,
  batteries; built connectors, modelled evidence, no live facility yet, said so); the reflex rule's own chapter in the book's
  Part One; the page foot, the copyright page and the back cover in the founder's wording; the book rebuilt, 520 pages.
- **The founder's afternoon orders, held and pushed as one (15:45 UTC).** (1) **Omni v4 ordered**: the collective mechanism, one
  body, one brain, one tick a second; a trial runs to its full measurement and is never ended by the calm it causes; the brain never
  forces, it reacts to what the system shows; the body's cost is judged with a guard for every part; one trial at a time inside a body;
  nothing permanent; the wall belongs to the body; every wire forced through it (`docs/OMNI_V4_PLAN.md`, rewritten). Everything is
  wired; staying native is the brain's live decision every second, never a verdict from one run. (2) **Six organisms**, restated and
  never again counted beside the live products; realms re-cut by a written rule at v4. (3) **The final coverage sweep** against the
  internet: register rows 74 to 78 (game server fleets, ledger nodes, build farms, network security engines, device brokers), lines
  on rows 9, 13, 19, 32 and 42, any vendor's card in section 2.3, five families and the robotics widening for the catalog at v4, the
  mega-caps' closed systems mapped to the open analogs that carry the same muscles, a ledger node's consensus added to the
  exclusions (`docs/REGISTER.md`, `docs/COVERAGE_MAP.md`). (4) **The legal wording** on every page outside the frozen engine: "all"
  before patents, copyrights and trademarks; "All rights reserved"; www.omni-compass.com; every export carries the notice, the license, the NOTICE and the disclosures (190 files, `LICENSE` section 9,
  `NOTICE`, `DISCLOSURES.md` item 4, the SBOM's embedded license, `CLAUDE.md`). (5) **Two faults GitHub's own runs showed and no
  local check had**: the release manifest not refreshed after the morning's last document edits (GitHub's verify red on four commits;
  refreshed) and `.github/workflows/cpu-power.yml` refused by GitHub since its first push for an unquoted colon in a step name (ten
  failed runs with zero jobs; quoted); `verify.py` now parses every workflow file (PyYAML in the requirements). (6) **The second set
  of the five live products** complete (21 runs, every job green) and archived; its early reading from the logs in
  `docs/RERUN_2026-10-10.md` and the manual's 16.6c: the Kafka gain is real and cheap and the trial's measurement is the fault, four
  trial rules written for v4. (7) The README leads with the newest work and carries a "Find it" section of the terms people search
  for; the word "simulation" is kept only in the license's own phrase and for third-party simulators by name, our own models being
  "modelled". (8) **The repository keeps itself current**: `.github/workflows/front-page.yml` runs after every finished live run
  of the five products, archives it with the code and runs `tools/front_page.py`, which groups the archived runs by what they are
  (product, objective, engine, workloads), takes the three newest complete runs of a kind as A, B and C, rebuilds every table whose
  runs changed (the old one kept whole in `docs/history`), then the index, the wiring page, the benefit sheet and the dossier, and
  writes the newest lines into the README's latest block; `results/live/FRONT_PAGE_STATE.json` records what each table was built
  from (seeded with the first set of 10 October); tests in `tests/test_front_page.py`, run by `verify.py`.
- **Every table remade from the rerun of 10 October** (69 of the 71 runs landed by 12:30 UTC; `docs/RERUN_2026-10-10.md`,
  "what landed"): the seven Kubernetes tests, the two robustness scenarios, the five stacks under both objectives (two new
  tables for the service objective, `results/live/V3_REDIS_SERVICE.md` and `results/live/V3_KAFKA_SERVICE.md`), the four
  simulators and the six organisms with the cluster inside were read from the archived runs by their table tools; the grid's
  receipts at 1, 10 and 100 copies were replaced (the 1,000-copy run's one cut-off shard runs again); the index, the wiring page,
  the benefit sheet and the dossier were regenerated; 19 superseded tables and 3 receipts went whole to `docs/history`. The index
  reads **+4.8%** (service reading +10.7%): Kubernetes +28.9%, PostgreSQL +0.8%, Kafka +0.1%, Redis nothing, MongoDB +0.7%, MySQL
  +1.0%. The five stacks ran for the first time with the brain's own verdict on the knob: PostgreSQL, MySQL and MongoDB gave memory
  back where it paid and lost nothing; **Kafka and Redis read nothing because every spend trial on Kafka and most on Redis were
  abandoned before they were judged**: the rule of 9 October ended a spend trial when the service turned calm, and a spend that
  works calms the service within seconds. **Amendment 3** (Redis, Kafka, MongoDB) and **amendment 4** (PostgreSQL, MySQL):
  `tools/knob_verdict.py` lets a spend trial run to its samples, only the wall or the engine's own time limit ending it early; a
  give-back trial still ends when the service leaves calm; `tests/test_knob_verdict.py` holds both rules; the five stacks run again
  on it and that set becomes the result of record. The state of play, the README, the engine page, the register, the manual and
  the history index carry the new numbers; the earlier numbers stay in the history pages and in the dated paragraphs.
- **The Linux kernel benchmark, built and preregistered** (`docs/CPU_POWER_PREREGISTRATION.md`; `tools/run_cpu_power.py`,
  `tools/cpu_power_abc.py`, `scripts/cpu_power_run.sh`, `.github/workflows/cpu-power.yml`, `tests/test_run_cpu_power.py`, run by
  `verify.py`), at the founder's order that the kernel's own knobs be benchmarked: the kernel's frequency governor as shipped is
  native; Omni moves the frequency ceiling of every CPU through the kernel's own files inside [half the top clock, the top], the
  governor still running under it; the compass law holds the service's own latency at 40% of a 20 ms line; every notch down is
  tried on the machine itself first by the brain's verdict (the knob verdict around the engine's own, unchanged); the snapshot is
  taken once, the ceiling handed back and read back, one writer, the master switch and the lease honoured; energy from the
  processor's own meter (RAPL, class P with the caveat stated) and a wall plug where fitted; a CPU-bound service under an open
  stepped load, the same requests in count and spacing in both arms. GitHub's machines are virtual and expose neither the governor
  nor the meter, so the workflow runs the tests and the probe there and the benchmark on a machine on the metal (the founder's own,
  a rented bare-metal server, or a self-hosted runner), in one command. The knob verdict gains a third objective, **per-work**
  (the resource per unit of work inside the line, the card's reading), declared for this benchmark's second set; the five stacks'
  counted runs keep the resource objective and are untouched by it. The manual (10.10; PDF rebuilt), the integration manual, the
  harness page, the documents index, the register (row 18), the proof program (row 6), the state of play and the wiring page's
  knob table carry it. No run yet: it waits for a machine.
- **The coverage map, the founder's second check the same night** (`docs/COVERAGE_MAP.md`; register rows 58 to 73 and the
  exclusions paragraph of section 4; proof program rows 50 to 62): every domain in the world of controllers walked against the
  register and the 59 muscle families, each read as done or running, queued, model only (with the nearest candidate named and why
  nothing open exists yet) or excluded by rule; the abbreviations the founder asked about (AKS, CPU, UPS, GPU, AWS, EKS, GKE, HPA,
  KEDA, KWOK, RAPL, RAN, FHIR, FIX, ROS, AMoD, EV, HVAC, PLC, CDN, ATM) each given its place. Added: self-driving stacks (Autoware on
  CARLA, openpilot), the EV powertrain (FASTSim), mobility fleets (AMoDeus), stream processing (Flink's autoscaler), storage clusters
  (Ceph), AI batch admission (Kueue, Volcano), games (Godot, candidate), thermal plants (the open Modelica libraries, candidate; nuclear
  stands as the model only because no open plant benchmark ships a controller), fabs (candidate), surgical robot servos (candidate),
  the other Kubernetes scalers (Karpenter-class, the Cluster Autoscaler, KEDA, VPA, which the proof program had and the register did
  not), distributed SQL, the other brokers, CDN caches, air traffic management (BlueSky), observability pipelines. Written as rules:
  safety reserves, clinical dosing controllers, trading decisions, weapons, a person's command and solvers without a controller are
  never a knob.
- **The founder's sweep: nothing with value left out** (register rows 39 to 57; proof program section 3.5): operating systems (the
  Linux kernel's scheduler, network and memory knobs; Windows processor power management on the founder's own laptop), television
  and streaming (adaptive bitrate), telecom (a software 5G cell), web platforms and social media (the serving layer; the LDBC Social
  Network Benchmark on a graph database), financial trading infrastructure (a matching engine and a FIX gateway; Omni governs the
  machinery, never a trade), serverless (Knative), distributed compute (Ray, Dask), HPC power saving (Slurm) and scientific
  workflows, oil, gas and heat networks (pandapipes), a wind turbine (OpenFAST with ROSCO), agriculture and irrigation, healthcare
  systems, robotics navigation, humanoids and marine vehicles, mining (a candidate until an open source with a shipped controller
  is confirmed), video transcoding; aerospace and rockets were already rows 32 to 36. Each row names an open benchmark anyone can
  run, its shipped controller as native and one knob for Omni, and is preregistered before its first run.
- **Every benchmark run again on one commit** (`docs/RERUN_2026-10-10.md`): at the founder's order that every result be as of today,
  the seven Kubernetes tests, the five live stacks on the brain's own verdict (the resource objective; Redis and Kafka also under the
  service objective), the four simulators, the realms table and the kill and long robustness scenarios (three runs each), the six
  organisms with the real cluster inside, the modelled grid at 1, 10, 100 and 1,000 copies and the two big organisms at 1,000 copies
  on rented Azure machines were dispatched between 01:24 and 01:31 UTC on commit `3aac0ab7` (Omni v3 by `tools/omni_version.py`),
  native and omni, the wiring of each checked against its preregistration before the dispatch: 70 GitHub runs and two Azure
  machines. The five preregistrations' dispatch paragraphs, the state of play, the register (every row marked), the manual (9.4,
  16.6b), the wiring page and the v4 plan say so. Every published table stands until its new set lands; the new set then supersedes
  it and the old table goes whole to `docs/history`. Not restarted: the three 24-hour robustness machines (the same harness byte for
  byte, ending about 10:15 UTC) and the Azure fleet, which waits on the family allowance those machines hold.
- **The audit after the dispatch, at the founder's order that every term of 9 and 10 October be wired everywhere**: the wiring
  page gains a knob-by-knob table of where the brain's verdict stands today (the five stacks both ways through
  `tools/knob_verdict.py`; the cluster's machines, the card's clock ceiling, the robots' speed and the drones' cruise by the
  engine's own verdict; the grids, the districts and the 945 modelled muscles by the law alone, their trial being the next engine),
  pointed to from the state of play and the wiring guide, which now states how to wire for superiority (watch first, the
  observation run, the brain's verdict on the knob, the operator's setting always free). Three places that read "not confirmed"
  against the rule (the manual's PostgreSQL paragraph, the state of play's PostgreSQL row, the PostgreSQL preregistration) now read
  "inside the noise by the rule"; the manual's valley metaphor no longer uses the word the founder retired. The rerun record
  carries the measured length of every kind of run (from the earlier run of each kind, in runner-hours) and the two-day timeline.
- **The gaps the tree shows, written into the register** (the founder's reading of 10 October): the index's six real categories are
  Kubernetes, PostgreSQL, Kafka, Redis, MongoDB and MySQL; Azure waits on its three-run close and the card on its run on the current
  controller; the power grids and the districts are in as simulations, never in the index by rule. What is not yet a category: a
  second and a third cloud (AWS and Google Cloud under Azure's method, new row 38 of the register's queue: each needs its own
  account credential in a GitHub secret and its own allowance, nothing spent until then), CPU power through Linux's own governor
  with RAPL (row 18, now saying what it needs: a machine where the governor and the meter are writable, the founder's own tower or a
  rented bare-metal server, since GitHub's runners and cloud machines allow neither), and the card's energy meter, which the card
  harness already has (the integral of the device's power draw, the CPU package by RAPL, the wall plug where fitted) and which reads
  on the founder's run. The state of play lists the three as open item 8. (`tools/benefit_sheet.py`, `tools/wiring_verdicts.py`, both pages regenerated):
  the founder found the sheet read backwards against the tables (plus is good on the sheet; a cut reads minus in a table). Now the
  sheet's number carries its word (gain, loss, nothing) and every confirmed change is written out beside it: a gauge that fell when
  falling is good reads **cut** (less waiting, fewer machines, less energy, less memory), one that rose when rising is good reads
  **up**, each with **good** or **cost**; the wiring page's columns, causes and loss list use the same words. The tables keep their
  raw signs with the Reading column beside them, and how to read the results and the manual (14) say so.

## 2026-10-09
- **The benefit sheet: one number per benchmark, plus always good for Omni** (`tools/benefit_sheet.py`, `docs/BENEFIT_SHEET.md`,
  `results/BENEFIT_SHEET.json`, checked by `verify.py`): at the founder's order that a reader must never have to work out
  whether a minus is good, every benchmark gets one figure whose sign always means the same thing (less energy, fewer machines,
  less memory, a shorter wait all read plus), with yes, no, none or trade beside it. The number is the Omni index's own reading
  where the test is in the index, and the same arithmetic over every judged gauge for the simulators and the organisms. README,
  the documents index, how to read the results, the state of play and the manual (14, the appendices) point to it.
- **The brain's own verdict on every live knob, in real time** (`tools/knob_verdict.py`, `tests/test_knob_verdict.py`; the five
  harnesses `tools/run_redis.py`, `run_kafka.py`, `run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py` and their three-run table
  tools; the five workflows take an `objective` input; `verify.py` runs the tests): at the founder's order that the brain must
  decide, on the muscle and in real time, whether a knob pays before it writes it, every live knob now starts in watch and is
  written only inside the allowance a paired trial on the stack itself has earned, one notch a trial, under the declared
  objective (resource: the index's reading, the default; service: work and speed alone). A refused step is not taken, a trial
  holds the knob, a fail-up never spends beyond the allowance, the operator's setting is always free. The trial, the judge and
  the allowance are the frozen engine's own `omnicompass/verdict.py`, unchanged: Omni v3 stays v3. The audit lines carry the cost
  sample and the verdict's state every second; the arm records and the three-run tables carry the verdict per workload. Declared
  as amendments (Redis 2, Kafka 2, PostgreSQL 3, MySQL 3, YCSB 2) with the expectation written before the runs; no run dispatched
  yet, at the founder's word. The manual (9.4, 16.6b, appendix B), the integration manual, the state of play, the register and the
  wiring page carry it; `docs/OMNI_V4_PLAN.md` designs the same verdict per muscle inside the engine as the next engine, not built.
- **Wire in, or watch: the verdict per knob, from every result** (`tools/wiring_verdicts.py`, `docs/WIRING_VERDICTS.md`,
  `results/WIRING_VERDICTS.csv`, checked by `verify.py`): at the founder's order that Omni need not be wired into every
  muscle (where it cannot beat native, the muscle stays native and Omni only reads it: one wire out, no wire in), every
  three-run table, the four simulator tables, the 945 modelled muscles and the organism tables are read by one rule into
  three words: **write** (a gauge confirmed better, none confirmed worse), **watch** (nothing confirmed better; a loss is
  named with its cause) and **operator's choice** (a trade, shown with both readings of the index). Real stacks 12 write, 7
  operator's choice, 5 watch of 24; simulators 21, 15, 3 of 39; modelled muscles 124, 13, 808 of 945 (746 never wrote); the
  14 organism cells with the cluster inside all write on the cluster's gauges. Every confirmed loss on a real stack is listed
  with its cause: Kafka's consumers and the CPU they poll with, Redis's memory, MySQL's pages on a written working set, and
  PostgreSQL's connections above the operator's setting on `simple_update`, where nothing was bought and the verdict is
  watch. The engine is unchanged (Omni v3); the page decides what an operator connects. README, the register, the state of
  play, how to read the results, the Kubernetes preregistration (the declaration), the wiring guide, the integration manual
  and the manual (1.2, 16.6b, the appendices; PDF rebuilt) carry it.
- **A second reading of the Omni index, declared beside the first** (`tools/omni_index.py`, `results/OMNI_INDEX.md`,
  `docs/K8S_COMPASS_PREREGISTRATION.md`): at the founder's question about what a cache is for (Redis is bought for speed and
  spends memory to deliver it; the resource reading counts that memory as a cost and reads Redis at −24.9% while its work and
  hit rate read confirmed better), the same tests and the same three-run rule are also scored on **service alone, work and
  speed**, with machines, energy, memory, connections and consumers shown and not scored, for every test alike. The service
  reading stands at **+71.8%** (Kubernetes +83.2%, Kafka +1,192.8%, Redis +8.8%, the three database stacks exactly nothing,
  their gains being resources given back); the resource reading, +20.5%, stays the headline the program preregistered. Both
  are printed in the same tables as two columns; a confirmed loss in work or speed counts against Omni in both. README, the
  state of play and the manual (summary, 16.6) carry the second number beside the first.
- **The whole tower at 1,000 copies with the real cluster inside, on v3, 3 of 3 on the clock** (`results/live/V3_BIG_ORGANISM.md`,
  now both big organisms side by side; started by run 37756284680, collected by run 37945866426 after 25 hours on one rented
  Azure machine, eastus `Standard_D8as_v4`, a 10,800 s window of 240 steps of 45 s, commit `6f0f93e5`, Omni v3): 945,000
  modelled muscles on one clock; the cluster's **p95 6,690 → 160 ms (−98%)**, p99 9,068 → 187 ms, **time over the line 76% →
  0, failed requests 4.8% → 0**, all clear of zero; replicas, pods started and machines (6 in both arms) the same or inside
  the noise; energy inside the noise; both arms 14 s behind the window; the organism's model energy −0.4% and work
  rounding-level worse, shown. The machine was deleted by the collect. The v3 record, register row 8, state of play, the
  manual (2.5, 16.2, the evidence map) and the Kubernetes preregistration carry it.
- **The second counted sets of PostgreSQL and MongoDB and the third of MySQL, on the amended harnesses: the costs are gone,
  the gains are smaller and real; the index moves from +24.1% to +20.5%** (runs 37858494179, 37858496620, 37858499033;
  37858501997, 37858505059, 37858509109; 37858512907, 37858515717, 37858519010; commit `310cf318`, Omni v3; the earlier
  tables kept whole in `docs/history`). **PostgreSQL** (`results/live/V3_PGBENCH.md`): host CPU and median latency inside the
  noise on all three workloads (the first set's +14% to +28% and +15% to +17% worse, gone); connections held open **−36% to
  −38% on `select`, confirmed better**; `simple_update` connections most at once **+72% to +80%, confirmed WORSE** (amendment
  1's add rule buying servers above the operator's 20 on a slow write workload, as in the first set, nothing bought); the runs
  disagree on `tpcb_hot`; category +4.0% (was +14.2%). **MongoDB** (`results/live/V3_YCSB.md`): the cache held **−21% to −36% on
  all four untouched workloads, confirmed better**, settling at 330 to 405 MB where the gate finds the working set; the burst
  mean latency inside the noise (the +2% to +4% worse, gone); 8 rows better, 0 worse; category +8.5% (was +10.2%). **MySQL**
  (`results/live/V3_SYSBENCH.md`): burst pool **−49% to −56%, confirmed better**; read_write pages holding data **+44% to +52%,
  confirmed WORSE** (was +53% to +70%) with host CPU **−4% to −6%, confirmed better**, a trade; read_only inside the noise (the
  second set's −50% to −56% was in part the cold-start give-back now refused); update_index the runs disagree; category +5.2%
  (was +12.2%). Every knob handed back in every arm; no controller fault. The index, the dossier, the register, the v3 record,
  the state of play, README and the manual carry the new tables.

## 2026-10-08
- **The costs in the three database tables traced to their mechanisms, and the three that were ours amended, with the engine
  locked** (Omni v3 before and after; the harnesses are outside the fingerprint). **PostgreSQL** (`docs/POSTGRES_PREREGISTRATION.md`,
  amendment 2): the +14% to +28% host CPU was not "PgBouncer queuing", as the record had said without a measurement; it was
  our harness launching a `psql` process for every reading (7,956 console logins in one workload's pooler log; 52 ms of CPU
  a launch; a per-process meter on a paired `select` repetition put +55.9 CPU-seconds on the launches against a +52.8 s host
  difference, PgBouncer +1.2 s, PostgreSQL −4.7 s). The harness now holds one console connection an arm (`Console`, the
  server's own wire protocol), takes a server back only while clients waited for one under 1% of the pooler's time and a
  transaction was served, adds servers back one per percent of waiting, up to the operator's 20 (the +15% to +17% median was
  the pool shrunk into a queue), and records its own CPU. **MySQL**
  (`docs/MYSQL_PREREGISTRATION.md`, amendment 2): 36 of read_write's 82 grows came with the pool missing under 1% of its
  reads (slow writes the pool cannot mend); the pool now grows only while missing (1% or more, the give-back's own line), and
  no chunk is given back in a second with no read request. **MongoDB** (`docs/YCSB_PREREGISTRATION.md`, amendment 1): every
  burst and c arm gave four notches back in its first five seconds, before its first eviction, because a cold cache evicts
  nothing; the give-back gate is now the miss share under 1% of requests (the MySQL gate), growth is gated on missing the same
  way, and a second with no request moves nothing. Said before the runs: the MongoDB memory rows may fall to the noise, because
  the saving was the artefact. Tests cover every new case; the second (PostgreSQL, MongoDB) and third (MySQL) counted sets
  follow on these rules, the earlier tables kept whole in `docs/history`. Dispatched 23:16 UTC on commit `310cf318`:
  PostgreSQL A2/B2/C2 37858494179, 37858496620, 37858499033; MySQL A3/B3/C3 37858501997, 37858505059, 37858509109; MongoDB
  A2/B2/C2 37858512907, 37858515717, 37858519010.
- **The public-trace test done, A/B/C on v3: a day of demand nobody here wrote reads the same way as our own schedules**
  (`results/live/V3_TRACE_GOOGLE2011.md`, runs 37826513664, 37826518868, 37826522419, commit `13ee69e8`, 30 of 30 pairs
  valid): p95 **−65% to −71%**, p99 −49% to −61%, mean −51% to −55%, time over the line −81% to −84%, failed requests −8% to
  −17%, **machines in service −6% to −10%**, HPA replicas −5% to −6%, standby-model energy −4% to −7%, all confirmed better;
  pods started +23% to +35% as point estimates, inside the noise in one run; no pod ever without a machine; 9 rows better, 0
  worse. The Kubernetes category of the index moves to **+28.8%** over seven tests and the headline to **+24.1%**. The
  preregistration carries the result and the comparison with the wandering test; register row 17, proof-program row 4, the
  v3 record, state of play, README, the manual (3.5, 16.1, 16.6, 16.7, 16.8, the executive summary) and the dossier carry it.
- **A public demand trace on the real Kubernetes cluster, preregistered and built** (`docs/TRACES_PREREGISTRATION.md`,
  `tools/trace_schedule.py`, `tests/test_trace_schedule.py`, `results/traces/google2011/`; register row 17, proof-program row 4):
  the first day of the Google cluster-usage trace 2011 (jobs submitted an hour, 18 public parts named with their SHA-256)
  turned into the wandering test's load schedule by a rule written before the runs (min-max onto 1 to 8 generators, one
  step a bin, 24 steps of 108 s), the receipt committed; everything else is the wandering test's. Runs A, B and C on v3
  dispatched at 18:43 UTC on commit `13ee69e8`: 37826513664, 37826518868, 37826522419. The register's queue rows for robot
  arms and drones now read done (they were).
- **MySQL under sysbench, the second counted set A2/B2/C2 on the amended plug: the pool given back on read-mostly working sets,
  bought on a written one, handed back on every arm** (`results/live/V3_SYSBENCH.md`, runs 37770617236, 37770620582,
  37770624805, commit `a033fd09`, Omni v3): the pool held **−67% on burst and −50% to −56% on read_only, confirmed better**; on
  read_write the pages holding data **+53% to +70%, confirmed WORSE**; work inside the line, p95, p99 and host CPU inside the
  noise on every workload; no error; **the pool handed back and read back on all 45 omni arms**. 4 rows better, 1 worse, 0
  disagree; the category enters the index at +12.2% and the headline moves to **+23.5%** over six real categories. The first
  set's table (every row inside the noise, 15 arms not handed back) is kept whole in `docs/history/V3_SYSBENCH_set1.md`; the
  preregistration carries both sets. Register row 24, proof-program row 11, the v3 record, state of play, README, the manual
  (3.3, 3.5, 10.9, 16.4, 16.6, the executive summary, the evidence map) and the dossier carry the result.
- **The fleet's seventh dispatch ran no arm; an inventory workflow for the subscription** (`docs/K8S_COMPASS_PREREGISTRATION.md`
  amendment 8; `.github/workflows/azure-inventory.yml`): repetitions 1 to 3 refused by Azure's cluster capacity in eastus as
  before (32 refusals across seven dispatches); repetitions 4 and 5 stopped at the pre-flight, which found only 2 of 10 vCPUs
  free in two machine families. The new workflow lists, read-only, every resource group, AKS cluster, machine and scale set
  and one region's per-family vCPU usage, and deletes only groups named in full that begin with our own runs' prefixes. Its
  first run (37773586107) found exactly our four machines and nothing left behind: the holders are two of the 24-hour
  robustness machines, rented as eight-core sizes in those families; the eighth dispatch follows their collect.
- **MySQL under sysbench, the first counted set A/B/C on v3, every row inside the noise, and a hand-back finding**
  (`results/live/V3_SYSBENCH.md`, runs 37757840760, 37757850988, 37757861572, commit `23f6ca4c`; `docs/MYSQL_PREREGISTRATION.md`,
  register row 24, proof-program row 11, the v3 record): on the four untouched workloads no gauge-row is confirmed better or
  worse and none disagrees; no error; the pool moved 3 to 26 times an arm. **15 of 45 omni arms did not read the operator's
  512 MB back at the end**: the audits show the server still withdrawing the blocks of a shrink the law had asked for when the
  restore was issued (InnoDB finishes a shrink only when the load releases the pinned pages), and MySQL ignores a new size
  while a resize is in progress. The plug's restore, not the law: `BufferPool.restore` now waits for the resize in flight,
  writes the snapshot and writes once more if the server ignored it, with a receipt in every omni arm's record; the table
  (`tools/sysbench_abc.py`) counts the arms not handed back and those mid-resize; `tests/test_run_sysbench.py` proves the three
  cases. Declared as an amendment; the first set's rows stand; the second counted set runs on the amended plug. The index now
  spans six real categories at **+21.2%** (MySQL at +0.0%); README, the state of play, the manual (3.3, 3.5, 10.9, 16.4, 16.6,
  the executive summary, the evidence map) and the dossier carry it. The update_index "inside the line" row is disclosed as
  counting almost nothing in either arm (a single update's client round trip exceeds the server-side 0.6 ms line). The second
  counted set dispatched on the amended plug at 11:31 UTC, commit `a033fd09`: runs 37770617236, 37770620582, 37770624805.
- **The 24-hour robustness run dispatched on three rented machines** (`docs/ROBUSTNESS_PREREGISTRATION.md` scenario 2b, the
  dispatch record): runs 37761059781, 37761072412 and 37761084779 of `big-organism-detached` with `test=robust`, 86,400 s an
  arm, one pair a machine, commit `4d5633dd` (v3), eastus, all three rented at the first attempt and running by 10:20 UTC;
  collected and deleted at 60 hours at the latest. Corrected from the subscription's inventory the same day: the start job
  rented eight-core machines of three families (`Standard_D8as_v7`, `Standard_D8s_v7`, `Standard_D8s_v4`), not the four-core
  size the scenario named; about $55 to $70 for the three, the rules unchanged, the correction in the scenario's record. The index tool carries the MySQL table's entry
  ahead of the result (silent until the sysbench table exists in `results/live/`).
- **The manual, twelve thin sections expanded** (1.4 nothing hardwired, 1.5 the word, 2.3 the organism receipt, 2.4 the two
  axes of the grid, 2.5 the clock rule and the 1,000-copies result, 2.6 reading a register row, 3.1 why the room is there,
  3.3 both readings on real software, 4.3 one decision followed through, 6.3 the memory gates on MongoDB and MySQL, 7.2 the
  snapshot and the read-back, 7.3 the API errors held in the long run, 7.4 memory and decision time over time, 9.2 what the
  verifier checks, 10.4 the robust mode of the detached workflow, 16.3 the fleet's refusals); PDF rebuilt, 472 pages.
- **The four stacked at 1,000 copies with the real cluster inside, on v3, 3 of 3 on the clock** (`results/live/V3_BIG_ORGANISM.md`;
  started by run 37564821425, collected by run 37754612102; one rented Azure machine, eastus `Standard_D8as_v4`, a 10,800 s
  window of 240 steps of 45 s, three paired repetitions over 29 hours, commit `126b8941`, Omni v3): the cluster's p95 2,882
  → 150 ms, p99 5,405 → 165 ms, time over the line 51% → 0, failed requests 0.14% → 0, all clear of zero; replicas, pods and
  machines the same; energy inside the noise; the organism's model energy −0.4% and work rounding-level worse, shown; both
  arms 22 s behind the window (0.2%). The machine was deleted by the collect. The whole tower at 1,000 copies started the same
  way (run 37756284680). The v3 record, register row 8, state of play, README and the manual's section 16.2 carry it.
- **MySQL under sysbench, preregistered, built and smoke-tested four times** (`docs/MYSQL_PREREGISTRATION.md`,
  `tools/run_sysbench.py`, `tools/sysbench_abc.py`, workflow `sysbench`, tests in `tests/test_run_sysbench.py` and
  `tests/test_sysbench_abc.py`; register row 24, proof-program row 11): MySQL 8.0 and sysbench from Ubuntu's own packages,
  the operator's 512 MB InnoDB buffer pool as native, Omni on the pool size in the server's own 128 MB chunks through its
  console, reading the server's own statement latency from the performance schema. The four smoke runs on the tuning
  workload, all recorded: sysbench's shipped request draw never reached the pool (made uniform), the 1 ms line kept every
  reading under the center (set at 0.5 ms, then 0.6 ms), and the "no page read from disk" give-back gate was never satisfied
  because InnoDB keeps stale pages resident (now the pool's miss share under one percent); on the fourth smoke the pool
  followed the working set both ways. The counted runs A, B and C follow. The manual carries section 10.9 and the stack's
  settings row; the integration manual its row.
- **Robustness, the long run, three runs** (`results/live/V3_ROBUST_LONG.md`, runs 37716886448, 37716900258, 37716913526,
  3 pairs × 7,200 s an arm each, Omni v3; `docs/ROBUSTNESS_PREREGISTRATION.md` scenario 2): the governor's memory at most
  1.07 of its first ten minutes after two hours (no leak), 97.5% or more of the expected decisions in every repetition
  (valid), 2 to 3 failed decisions a run where the cluster's API answered 500 on the HPA read (held and resumed; shown with
  the reason, as preregistered), the decision time's last hour at most 1.20 of its first (no slowing), every setting handed
  back at the end; machines and energy inside the noise, service confirmed better in one run and inside the noise in two.
  The reader (`tools/live_reps.py` `robust_decisions`, `tools/confirm_abc.py`) gained the long run's preregistered rows,
  with fixed cases in `tests/test_robust.py`; each run's live report in the archive was rebuilt from the untouched raw
  files and its checksum list updated for those two derived files.
- **MongoDB under YCSB on v3, confirmed three times** (`results/live/V3_YCSB.md`, runs 37727968670, 37727976107,
  37727983746, all at `7ee471b4` on Omni v3; `docs/YCSB_PREREGISTRATION.md`, register row 24, proof-program row 11):
  the operator's 512 MB WiredTiger cache as native, the compass on the cache size inside [256, 2,048] MB through the
  server's own console as omni. On the four untouched workloads the cache held fell about half on c and burst and 13% to
  37% on f, confirmed better (b inside the noise in one run); work inside the 1 ms line, p95, p99 and host CPU inside the
  noise on all four; no failed operation; the burst mean latency +2% to +4%, confirmed worse, the one loss; every cache
  handed back. 6 rows better, 1 worse, 0 disagree. Four smoke runs preceded the counted runs and are all in the
  preregistration: two harness faults, YCSB's zipfian draw that never reached the cache, hashed run keys over an ordered
  load, and the line set at 1 ms from 2 ms on the tuning workload's own figures. **The Omni index now spans five real
  categories: +25.9%** (`results/OMNI_INDEX.md`; the MongoDB category +10.2%); `tools/omni_index.py` and `tools/dossier.py`
  carry the table (dossier section 3d).
- **The fleet's sixth dispatch** (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendments 5 and 6): eastus refused the fifth
  dispatch's first repetition (the 23rd refusal), the run was cancelled to weigh a second region, the 6 October survey shows
  no other region can take a 40-worker fleet on this subscription, and the fleet was dispatched a sixth time in eastus
  unchanged; its first repetition was refused too (the 24th); the run continues.
- **The manual, expanded to referee and underwriter level** (`docs/OMNI_COMPASS_MANUAL.md`, the PDF rebuilt): the
  standards every page keeps, the executive summary as prose with what is and is not shown, the governor's on-top
  principle, the verdict, the pedals, the modes and the two switches, the catalog, the realms, the organisms and the
  grid, the arithmetic with worked examples, every result with the question a referee will ask beside it, the engine's
  equations in words and where the engine sits against the compass law, the closed circle in plain words and what it does
  and does not certify, the compass's settings on every stack in one table, the direction rules, the do-no-harm gates,
  the profiles and the pedals, the nervous system's authority and release gate, the plug contract line by line, the
  levels, the wiring of a message broker, a cache and a drone swarm (sections 10.5 to 10.7), the three ways a governor
  stops and what each leaves behind, least privilege and the supply chain, the method of paired runs, the evidence
  classes with examples and how to read a row, why three runs and why geometric means, a narrative of every result family
  with its losses (16.1 to 16.6), threats to validity stated by us (16.7), what is not yet shown and the open program
  (16.8), a fuller glossary, file map, troubleshooting and the audit trail from any row to its raw files. The
  integration manual and the wiring guide carry the three new stacks.
- **Robustness, preregistered and built** (`docs/ROBUSTNESS_PREREGISTRATION.md`, register row 31): the governor killed
  outright at 40% of a governed window (SIGKILL) with the watchdog beside it, the seconds until every setting is back at
  the operator's polled by the harness (`scripts/kind_robust.sh`, `ROBUST=kill` in `scripts/kind_bench.sh`), a second
  governor to the end, the 120 s after the kill compared in both arms; the long run (eight windows) with the governor's
  memory sampled from the process table; the governor's own CPU at 1 to 1,000 copies from the audits already archived
  (`tools/own_cost.py`, `results/live/V3_OWN_COST.md`: 0.006 to 0.013 of one core at every size). `tools/live_reps.py`
  gains the robustness rows and `tools/confirm_abc.py` the three-run rows for them; `tests/test_robust.py` in
  `verify.py`. No engine file changes: `omni_controller/`, `omnicompass/` and `realms/` are the v3 bytes.
- **Robustness, the kill scenario, confirmed three times** (`results/live/V3_ROBUST_KILL.md`, runs 37716845219,
  37716859133, 37716872788, all omni-v3 at `bd389c409ad9`, 10 pairs each): the governor killed with SIGKILL at 40% of the
  window in every repetition; the watchdog's hand-back put every setting back at the operator's 7 to 11 s later in 30 of
  30 (mean 9 s; allowance 60 s); a second governor started and governed to the end in every one; the 120 s after the kill
  read no difference beyond the noise against native in all three runs; the whole window, a kill and a restart inside it,
  read mean response −32% to −39%, p95 −42% to −45%, time over the line −28% to −34% and failed requests −9% to −15%,
  confirmed better; machines and energy inside the noise. The register, the proof program, the engine page, the state of
  play and the manual (3.5, 16.4b, 16.8, the results table) carry it; the long run (3 pairs × 3 runs) is running.
- **YCSB on MongoDB, preregistered and built** (`docs/YCSB_PREREGISTRATION.md`, `tools/run_ycsb.py`, `tools/ycsb_abc.py`,
  workflow `ycsb`, tests in `verify.py`; register row 24): MongoDB 8.0 from its publisher's signed repository with the
  operator's 512 MB WiredTiger cache as native; Omni on the cache size inside [256, 2,048] MB through the server's own
  console, reading the server's own mean read latency, growing only while the cache is full, giving a notch back when calm
  and nothing is evicted; YCSB 0.17.0 (pinned by SHA-256) running its published core workloads with the key space stepping
  through the cache and past it; the disclosed limit that the data also sits in the OS page cache on this machine. The
  smoke run first, then A, B and C.
- **Robustness smoke run passed** (run 37713124793, one repetition, 600 s, not counted): the governor killed at 240 s,
  every setting back at the operator's 7 s later by the watchdog's hand-back, a second governor to the end, the reset
  check passed. One harness fault fixed before the counted runs: the memory sampler's process-id join (every sample read
  zero); the memory ratio now needs a window over twenty minutes. The kill (10 pairs × 3 runs) and long (3 pairs × 3
  runs) scenarios dispatched on v3.
- **The manual, further expanded**: the governor's audit read end to end, what an upgrade is and is not, why each
  requirement of a stack is there, the four realms in prose, what the Azure, database and simulator runs taught us, the
  twins and the three fingerprints, Appendix D as a table of every gauge with its source and class, Appendix G
  (reproducing everything from a clean machine); the theory chapters carry what the grid has shown, the receipt's
  arithmetic and the one number, and what closing the loop has shown since; the results reader carries the workload,
  swarm, own-cost and robustness tables.
- **Redis on v3, confirmed three times** (`results/live/V3_REDIS.md`, runs 37704450300, 37704464642, 37704479534, all
  omni-v3 at `467f73eba7a6`): on all three untouched workloads (small, large, burst) work inside the 2 ms line +14% to
  +27%, the hit rate +14% to +27% and the mean latency −30% to −61%, confirmed better; no failed request; the memory
  ceiling held 64 → 200 to 270 MB and the memory used confirmed worse (the resource the gain costs); host CPU-seconds
  inside the noise on all three; keys evicted −76% to −92% (shown); every ceiling handed back; 12 gauge-rows better, 6
  worse, 0 where the runs disagree. **The Omni index with the cache in: +30.2%** (Kubernetes +25.5%, the database +14.2%,
  Kafka +166.9%, Redis −24.9%): the cache's category reads negative because the memory it holds for a wide working set is
  the resource it trades, and reads worse by rule, while its work and hit rate read better; every category weighs the same.
- **Kafka on v3, confirmed three times** (`results/live/V3_KAFKA.md`, runs 37697222651, 37697239400, 37697255445, all
  omni-v3 at `a0b5d2381e9e`): on all three untouched workloads (light, heavy, burst) work inside the 500 ms line +16% to
  +21%, end-to-end p95 1.6 s → 9 to 14 ms, mean lag −92% to −97%, confirmed better; no message lost in any arm;
  consumers held 2 → 5.8 to 7.9 confirmed worse (the resource the gain costs); host CPU-seconds confirmed worse on light
  (+10% to +20%), inside the noise on heavy and burst; CPU per 1,000 messages inside the line better on burst; every count
  handed back; 21 gauge-rows better, 8 worse, 0 where the runs disagree. The tuning workload is shown and not counted.
- **The Omni index reads every workload table the same way** (`tools/omni_index.py`): the database, messaging and cache
  tables (`V3_PGBENCH.json`, `V3_KAFKA.json`, `V3_REDIS.json` when it lands) enter through one list, each a real category
  weighed the same, tuning workloads excluded. With Kafka in, the headline is **+56.4%** (Kubernetes +25.5%, the database
  +14.2%, Kafka +166.9%). The index page says why the messaging speed ratio is large: native sat at nine tenths of its
  measured capacity by design, so its queue grew and Omni's did not. README, the state of play, the manual, the engine
  page, the register and the proof program carry the result.

## 2026-10-07
- **Redis, preregistered and built** (`docs/REDIS_PREREGISTRATION.md`, `tools/run_redis.py`, `tools/redis_abc.py`, workflow
  `redis`, tests in `verify.py`): Redis as shipped with the operator's 64 MB ceiling and allkeys-lru as native; an
  application with a declared 5 ms store trip on a miss and a working set that steps 1 2 3 2 3 4 5 6 …; Omni on the
  ceiling inside [16, 512] MB through Redis's own console, growing only while the cache is full (a cold miss is not the
  ceiling's), giving back a notch a second when calm and nothing is evicted. The tuning workload on one machine (not
  counted): hit rate 66% → 81%, work inside the line +22%, the ceiling held 64 → 304 MB (the cost). Three untouched
  workloads run as A, B and C on v3. The two smoke runs that shaped the rule are described in the preregistration.
- **Azure**: the standard-tier fleet run was refused on all five repetitions too (seventeen refusals in seven hours, all
  Azure's eastus capacity for new clusters); dispatched again.
- **Kafka, preregistered and built** (`docs/KAFKA_PREREGISTRATION.md`, `tools/run_kafka.py`, `tools/kafka_abc.py`, workflow
  `kafka`, tests in `verify.py`): Apache Kafka 3.9.1 as shipped on the runner, a producer at a stepped rate, the consumer
  group at the operator's count as native; Omni on the consumer count inside [1, 8], holding the group's own end-to-end
  latency at 40% of a 500 ms line; the host's CPU seconds as the cost. The tuning workload on one machine (not counted):
  p95 429 → 12 ms, lag 329 → 45, consumers held 2 → 5.8. Three untouched workloads run as A, B and C on v3.
- **Drone swarms on v3, confirmed three times** (`results/live/V3_SWARM.md`, runs 37677964512, 37677984739, 37678005151): in
  all three untouched 20-drone cells energy a mission −7% (short), −18% (mixed), −20% (long) and missions a charge +8%,
  +22%, +25%, confirmed better; no late mission, reserve breach, near miss or collision in any arm of any run; 9 gauge-rows
  better, 0 worse. PyBullet reproduced to a part in a thousand across GitHub's machines, not to the bit, so the table's
  reproduction tolerance is one part in a thousand (preregistration amendment 1, made after the runs were seen and said so).
- **Azure fleet on the standard control-plane tier** (amendment 4; `tier` input of `aks-metered`, `AKS_TIER` in
  `scripts/aks_paired.sh`): the free tier was refused by Azure's capacity in eastus on ten repetitions over four hours; the
  control plane's tier is not in the bill. The drone swarm runs A, B and C finished (37677964512, 37677984739, 37678005151)
  and are requested for archive.
- **Drone swarms, the first item of the queue, built and preregistered** (`docs/SWARM_PREREGISTRATION.md`, `tools/run_swarm.py`,
  `tools/swarm_abc.py`, workflow `swarm`, tests in `verify.py`): gym-pybullet-drones (University of Toronto, MIT) flies
  Crazyflie 2.x quadrotors with its shipped position controller as native; Omni sits on top on one knob, the cruise
  override inside the autopilot's limits, spending tracking slack as speed; a declared energy model, the autopilot's
  battery reserve, collisions void the cell. The tuning swarm (5 drones, not counted): energy a mission −16%, missions a
  charge 5.8 → 6.9, no late mission, no collision. Three untouched 20-drone cells run as A, B and C on v3.
- **Azure fleet run refused five times by Azure's own cluster capacity in eastus** (run 37651333302, "creating a new cluster is
  unavailable at this time"); dispatched again.
- **The referee dossier rebuilt from the v3 tables** (`tools/dossier.py`, `docs/DOSSIER.md`): real Kubernetes three times
  (one chart, every run's interval), the real database, the bill on a real cloud, the grid at 84 of 90 cells, the 945
  muscles and the three simulators, the harnesses, and what is not yet shown; the obsolete card charts removed.
- **The state of play rewritten for v3** (`docs/STATE_OF_PLAY.md`): current facts only, the six Kubernetes tests, the
  database, Azure, the simulated results, the card and the open items; the 2026-10-06 page moved whole to `docs/HISTORY.md`.
- **The v3 grid at 100 copies** (`results/scale/receipts/v3-100x.md`, run 37501765605, 170 shards pooled from the archive with
  the run's own command): every organism superior within guardrails at 10, 100 and 1,000 runs, work per energy +0.07%
  to +0.36%. **The grid is complete at 84 of 90 cells** (`results/scale/GRID.md`); the six left are beyond the machines
  available, as declared. The same figure at every size from 1 to 1,000 copies.
- **The v3 grid at 1,000 copies** (`results/scale/receipts/v3-1000x.md`, run 37578946088, 60 shards, 10 paired runs per
  organism; `results/scale/GRID.md` now 60 of 90 cells): every organism superior within guardrails at 10 runs, work per
  energy +0.07% (Physics) to +0.37% (Energy, the four stacked, the tower), work unchanged, every knob handed back. The
  100-copy run's shards are all done; its pooling job did not start, so the receipt is pooled from the archived shards.
- **Azure fleet at 40 workers** (amendment 3): the pre-flight found `Standard_D2s_v3` not offered in eastus and stopped the
  45-worker run before anything was built or billed; the pool is dropped and v3 steady runs on the nine remaining
  families (run 37651333302). **The v3 grid at 1,000 copies finished** (run 37578946088, 61 shards) and is requested for
  archive; the receipt and the grid table follow.
- **Azure fleet rebuilt from the families the subscription allows** (preregistration amendment 2): the DAv4, ESv4 and
  EAv4 families have no allowance at all (the "remaining 0" refusals), so three of the eight pools could never be built.
  Ten allowed families give 45 workers; list prices from Azure's own price API; `scripts/aks_paired.sh` pre-flights
  every pool's size and family allowance before anything is built or billed.
- **All six Kubernetes tests confirmed on v3** (`results/live/V3_WANDERING.md`, `V3_ALL_FOUR.md` join the four already in):
  wandering p95 −57% to −63% and failed requests −9% to −12%; all four work inside the line +35% to +49%, p95 −61% to
  −66%, failed requests −11% to −14%; all confirmed better; machines and energy inside the noise in both. The same
  readings as v1. **The Omni index now reads from the v3 tables** (`tools/omni_index.py`, `results/OMNI_INDEX.md`): +19.7%,
  real Kubernetes +25.5% (work +19%, speed +93%, machines +4%, energy +3%), the database +14.2%; the README's result
  table is the v3 run A. The v1 tables stay as the first engine's record in `docs/OMNI_V1.md`.
- **Power grid on v3, confirmed three times** (`results/live/V3_PANDAPOWER.md`, runs 37568375564, 37568393269, 37568411160):
  the same table as v1 to the digit, as a deterministic simulator under the same runner bytes must give: 67 gauge-rows
  better, 14 worse (losses in the four grids with their own generation; tap operations 4 → 8 a year in one rural grid),
  0 where the runs differ. Run C of the wandering and all-four tests finished and requested for archive.
- **Kubernetes batch queue on v3, confirmed three times** (`results/live/V3_BATCH.md`): machines −19% to −23%, machines
  after the queue −29% to −35%, standby-model energy −13% to −16%, mean response −10% to −14%, all confirmed better; the
  queue finished no difference beyond the noise in all three runs. Four of the six v3 Kubernetes tests are now in.
- **Azure fleet runs refused twice**: the 39-worker run (DASv4 held by the detached machine) and the 35-worker run (DAv4
  "remaining 0" on three repetitions over 45 minutes, something in the subscription holding that family); both cancelled
  before any arm ran; the survey mode now lists the families in use and every resource group and cluster still standing,
  so the holder can be found before the next dispatch.
- **Azure burst v1, five pairs** (`results/live/V1_AKS_BURST.md`, run 37534538088 attempt 2): the bill +5.0% with its
  interval across zero; machines, p95 and failed requests inside the noise; p99 −34% (6.0 s → 4.0 s) clear of the noise
  in this one run. Replaces the four-pair table. Power-grid v3 runs 1 and 2 archived; run C of the batch test on v3
  finished (37581021752) and requested for archive.
- **Azure fleet, 35 workers while the detached machine runs**: the 39-worker steady run was refused on every repetition
  (the DASv4 family had 2 vCPUs left: the rented Standard_D8as_v4 running the v3 stack holds 8 of its 10), cancelled
  before any arm ran, and dispatched again at 35 workers with the steps scaled as preregistered (amendment in
  `docs/K8S_COMPASS_PREREGISTRATION.md`, the fleet that can show one machine).
- **Kubernetes on v3, three of six tests confirmed three times** (`results/live/V3_STEADY.md`, `V3_FAIRNESS.md`,
  `V3_FAULTS.md`; every run omni-v3): steady p95 −65% to −66%, machines −1.5% to −2.9%, standby-model energy −1.3% to
  −2.1%, all confirmed better; fairness no difference beyond the noise on every row; faults p95 −47% to −62% and time
  over the line −22% to −42% confirmed better, machines and energy inside the noise. The same readings as v1. Register
  rows 1, 4 and 5; the other three tests land as their B and C runs finish.
- **Azure burst v1, the four-pair copy withdrawn**: repetition 4's rerun finished (run 37534538088, attempt 2, 5 of 5),
  so the raw copy of the first attempt is removed and the whole run is archived in its place; the table is remade with
  five pairs when the copy lands.
- **The manual brought up to everything built since v1** (`docs/OMNI_COMPASS_MANUAL.md`, PDF rebuilt): section 10 now
  wires Azure's managed Kubernetes with the bill as the gauge and the fleet sized to the lever, a database behind its
  pooler, the three independent simulators and the big organisms on a rented machine; section 13 adds preregistration,
  the clock rule, every-row reporting and the raw-file archive; a new section 15 explains the frozen engines v1, v2 and
  v3, the version tool, the three-run rule and the Omni index; section 16 (results) is rewritten from the v1 and v3
  tables, losses beside gains, the earlier card results marked obsolete and the queue named; the glossary, command
  reference, file map and evidence map follow. `docs/INTEGRATION_MANUAL.md`, `docs/WIRING_GUIDE.md` and
  `docs/HOW_TO_READ_THE_RESULTS.md` carry the same additions; the register's heading reads 945 muscles in 59 families.
- **The archive bot copies finished runs only** (`.github/workflows/archive-run.yml`): it had copied the first 108 jobs of
  the v3 grid at 100 copies (run 37501765605) while the run was still going, and would never have looked again. That
  part-copy is removed; the run is re-requested when it ends. The grid at 1,000 copies is queued behind it (run
  37578946088). Run C of the Kubernetes batch test on v3 dispatched (37581021752); run B (37573759437) archived.
- **A fleet of several machine families on Azure** (`scripts/aks_paired.sh` `AKS_WORKER_POOLS`, `scripts/kind_bench.sh`
  worker selector `omni-role=work` and per-pool machine counts in the bill file, `tools/live_reps.py` the bill at each
  pool's own list price, `aks-metered` inputs `worker_pools` and `pool_prices`): the subscription allows 200 vCPUs in
  eastus but 10 a family, so one family gives 5 machines; eight families give 39 workers. Preregistered in
  `docs/K8S_COMPASS_PREREGISTRATION.md` (the fleet that can show one machine), replacing the one-family 11- and 15-worker
  plan the allowance refused. Register rows 12c and 12d.
- **The v1 stack at 1,000 copies, 3 of 3** (`results/live/V1_BIG_ORGANISM.md`, collection run 37575930111 from the detached
  machine): p95 −74%, p99 −83%, clear of the noise; machines 6 in both arms; organism energy −0.2%; organism work
  rounding-level worse; the compass arm ended up to 615 s after the 2,880 s window in all three repetitions (marked OFF
  THE CLOCK; native kept the clock). The tower and the stack now make one report from both archived runs.
- **"Nothing here is set in stone" removed** from the notice (`tools/legal.py`), the standing orders and every tracked
  file outside the archived raw records (which stay byte-exact under their checksums), on the founder's order. The manual
  PDF carries the old notice until its rebuild.
- **Aerospace and propulsion in the queue** (`docs/REGISTER.md` rows 32 to 37, `docs/PROOF_PROGRAM.md`): Basilisk attitude,
  momentum and thrusters; Orekit and GMAT station-keeping; Basilisk constellations; RocketPy and OpenRocket; Cantera
  combustion. Pure physics solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) are named as not benchmarkable: no controller,
  no knob; their value is the HPC cluster that runs them.
- **CityLearn on v3, A/B/C** (`results/live/V3_CITYLEARN.md`, runs 37568381751, 37568399439, 37568416917): the same pattern
  as v1: electricity bought, daily peak and daily unevenness better in all 11 battery districts, carbon in 8; the bill
  worse in 7 and ramping worse in 7 (the 2023 districts), reported as such; 71 score-rows better, 33 worse, 1 where the runs
  differ. `tools/six_kube_report.py` now reads several archived runs and writes to a named file, so the big organisms'
  tower (job-bound run) and stack (collected from the detached machine) make one report.
- **The proof program** (`docs/PROOF_PROGRAM.md`): the program of record on the founder's order: every benchmark at the
  largest size each platform allows, on open native engines, with the rules, sizes, order, costs, the defensibility
  package and the disclosures.
- **Azure burst on v1** (`results/live/V1_AKS_BURST.md`, run 37534538088, 4 pairs; repetition 4 lost its native cluster to
  an Azure API error and is run again): no difference beyond the noise on any gauge on the 4-worker fleet; Omni's own CPU
  0.009 cores. The 11-worker start was refused by the machine family's 10-vCPU allowance; the regional total was raised to
  200 but every family's request was refused through the API (QuotaNotAvailableForResource, ContactSupport): the
  subscription's terms. Next: a fleet of several machine families (4 to 5 workers each under the one allowance), or the
  owner's request in the portal.
- **Robot arms on v3, A/B/C** (`results/live/V3_MUJOCO.md`, runs 37568387334, 37568405026, 37568422829): the same
  readings as v1, as the runner is the same bytes: Gen3 7 gauges confirmed better, 0 worse; UR5e and iiwa 14 nothing to
  move. The four A/B/C table tools (`confirm_abc`, `mujoco_abc`, `pandapower_abc`, `citylearn_abc`) now name in their
  title the engine the three runs carry instead of a fixed "Omni v1".
- **The v3 repeats dispatched** (03:48 UTC): power grid ×3, CityLearn ×3, robots ×3, the six Kubernetes tests (run A;
  B and C follow each A). They should have been queued when v3 was declared; they were not.
- **The register's queue, audited against every family and what a referee or buyer expects** (`docs/REGISTER.md` §4, rows
  23 to 31): drone swarms, aircraft and defense edge (PX4, ArduPilot, Crazyswarm, JSBSim, K3s), databases and caches at
  large (YCSB, HammerDB), big data (Spark TPC-DS), messaging (Kafka), caches (Redis), search (OpenSearch), storage (fio),
  warehouse robots (Open-RMF), and a robustness row (a 24-hour run, Omni killed mid-run, Omni's own cost at every size).
  None changes a result that stands; each gets its own preregistration, A, B and C, every row shown.
- **Azure with a fleet that can show one machine** (`docs/K8S_COMPASS_PREREGISTRATION.md`, written before the run;
  `.github/workflows/aks-metered.yml` inputs `max_workers` and `hpa_max`; `scripts/kind_bench.sh` raises the app's
  replica ceiling with the fleet and expects it back untouched): the 4-worker runs could not show anything under a
  quarter of the fleet, and the 10-pod ceiling kept the autoscaler at about 1.9 workers in both arms. Now 11 workers
  (15 once the stack machine frees its 8 vCPUs), ceiling 9 pods a worker, load steps scaled with the fleet, 5 pairs,
  v3 first. Register rows 12c and 12d.
- **The organism must keep the window's clock** (`tools/six_kube_report.py`, `docs/K8S_COMPASS_PREREGISTRATION.md`): the
  report now shows "organism behind its window (s)" (shown, not judged) and marks a repetition OFF THE CLOCK when either
  arm ended more than 5% of the window late, its last steps having seen a cluster whose load schedule had ended. Found
  while watching the v3 stack at 1,000 copies on Azure: 1.7 million muscles step in 31 s against a 12 s step, 4,628 s
  behind after the native arm. Marked in the published reports: v1 six-kube at 1,000 copies, the Physics realm (2 of 3,
  up to 290 s) and the tower (2 of 3, up to 3,820 s) on GitHub's 4-core runners; v3 six-kube, the stack at 100 copies
  (4 of 5, up to 277 s); v1 big organism, the tower's repetition 3 (2,392 s). The pairing stands in every case. The
  remedy is a longer window for that size on that machine, never a change to the organism or the law: the v3 stack
  machine was collected as it stood and started again with a 10,800 s window (45 s steps).
- **The v1 big organisms** (`results/live/V1_BIG_ORGANISM.md`, run 37359820055): the tower at 1,000 copies on a rented
  Azure machine, 3 of 3: p95 −95% (4.1 s → 0.2 s), time over the line −99.7%, both clear of the noise; machines 6 in both
  arms; organism energy −0.2%; organism work rounding-level worse. The stack's native arms ran 5,184 s and 5,984 s past
  the window and never finished a pair inside the six-hour job.

## 2026-10-06
- **Six organisms with the real cluster, Omni v3, 10 and 100 copies** (`results/live/V3_SIX_KUBE.md`, run 37501769448 on
  `33b15eb`, 12 cells, 5 pairs each, 62 of 62 jobs): every cell better on 4 to 6 gauges, worse on none beyond the noise
  except a rounding-level organism-work loss (6 to 11 parts in a million; the rule reads anything past one part in a
  million) in 4 cells. The v1 and v3 copies now carry a Source line naming run, commit and engine.
- **Azure steady on Omni v1, 5 paired repetitions** (`results/live/V1_AKS_STEADY.md`, run 37385657374 on `f162ce8`;
  repetitions 3 to 5 re-run after the regional quota refused them while the big-organism machine was up): no difference
  beyond the noise on any gauge; the bill −4.7% with its interval across zero; Omni's own CPU 0.014 cores. The burst on v1
  follows (branch `omni-v1` at `f162ce8`, since the workflow needs a branch to run an older commit; a tag push was refused).
- **The stack at 1,000 copies, detached from the GitHub job** (`.github/workflows/big-organism-detached.yml`): every
  attempt at the four stacked with the real cluster inside was cut off by GitHub's six-hour job limit (v1 run
  37359820055: the tower 3 of 3 done, the stack 0 of 3). The new workflow rents one Azure machine, starts every repetition
  under nohup and leaves it running; a look every two hours collects the files when all are done (one artifact per cell,
  the same shape as `big-organism`'s) and deletes the machine; a machine older than 40 hours is collected as it stands.
  The commit to run is an input, so the v1 stack runs again on `f162ce8` (named `stack_1226` there) beside the v3 stack.
  Package install on the fresh machine is tried five times (one v1 attempt lost its machine to a stale package list).
  First starts (17:57 UTC, westus2 and centralus): every size refused, the CLI hiding Azure's reason behind its own
  "content already consumed" error; the workflow now reads the reason out of Azure's answer and lists the region's SKU
  restrictions. eastus2 refused every size too. The workflow's survey mode (rents nothing) then asked Azure, region by
  region, which 8-vCPU sizes this subscription may rent: eastus allows 32 vCPUs and the v4 sizes (D8as_v4 is the one
  granted on 2026-10-05); every other region surveyed allows 10 vCPUs and only the v5 to v7 sizes. So the start job
  asks Azure for each refused size's restriction, tries D8as_v4 and D8s_v4 first and falls back to the v7 sizes, and the
  default region is eastus. Both machines were then granted (eastus, D8as_v4, the v3 stack; westus3, D8as_v7, the v1
  stack) and the tests started, but the start step's ssh session hung until the job's hour ran out: the test had been
  put in the background as part of an "a && b &" list, so a shell holding the session waited for it. Fixed; the collect
  look, dispatched by hand, found both machines running.
- **The version tool reads a commit from before a runner was written** (`tools/omni_version.py`, `tests/test_omni_version.py`):
  the power-grid runner was added at `8eab01c` inside v1 without touching any other engine file, so the Kubernetes and
  organism runs at `a004a8f` (six-kube 37359815637, big-organism 37359820055) hold 37 of the 38 v1 files, all v1 bytes.
  The tool used to print only what differed from the newest version there; it now prints "omni-v1 (37 of 38 files, all v1
  bytes; not yet in this commit: tools/run_pandapower.py)", and `docs/OMNI_V1.md` says the same. A changed byte or an
  extra engine file is still no version. `tools/code_book.py` reads the version through the same functions.
- **The real database joins the Omni index** (`tools/omni_index.py`, `results/OMNI_INDEX.md`): per workload, work inside
  the line, p95, the connections held open (machines) and the host's CPU seconds (energy: the compass's own cost, confirmed
  worse, counted against Omni). Headline +20.1% over the two real categories in (Kubernetes +26.2%, the database +14.2%).
- **Omni v2** (`OMNI_V2.json`, `docs/OMNI_V2.md`; the founder's order: make v2, add every missing muscle family, don't be
  cheap). The law, the controllers and the runners are v1's byte for byte. The catalog (`realms/catalog.csv`, built by
  `tools/realms_catalog_v2.py` from `realms/catalog_v1.csv`, `docs/realm_study/TRUE_MUSCLES.csv` and the new
  `realms/wave4_families.csv` by the v1 rules) grows from 656 muscles in 46 families to 945 in 59: the 656 of v1 byte for
  byte, 118 real controls the realm study had found and the tower lacked, and 171 muscles in thirteen new families with
  one new preset each (`realms/presets.py`): hospitals' critical rooms, clinical systems, farms and irrigation, oil and
  gas pipelines, rail traction, marine propulsion, ports, mining, district heating and cooling, power generation,
  renewables and inverters, elevators, pharmaceutical and food plants. Every added muscle names its real system, its
  setting and its source. The organisms: Compute 430, Physics 376, Energy 470, Distribution 440, the stack 1,716, the
  tower 945, the spine 257. The two whole-tower organisms are named `tower` and `stack` in code and workflows (nothing is
  named by a count); `organism_656` and `stack_1226` are read as aliases, so every v1 record still reads. Every added
  muscle was run through the harness before the freeze (deterministic, watch equals native, every knob handed back, Omni
  never more often outside its band than native); two presets were adjusted on that check and the adjustment is written
  into `docs/REALMS_PREREGISTRATION.md`. `tools/omni_version.py` now prints omni-v2, omni-v1, or what differs; the
  three-run tables accept either fingerprint and refuse to mix them. Every modelled result is to be run again on v2;
  v1's tables stay v1's.
- **PostgreSQL, the counted runs on amendment 1** (`results/live/V3_PGBENCH.md`; runs 37435740735, 37435751322, 37435761371,
  three paired repetitions each, the three untouched workloads): the connections held open to the database (the machines)
  confirmed better on `select` (−61% to −63%) and `tpcb_hot` (−69% to −72%); on `simple_update` the runs disagree (one
  run +12%, two runs −34% and −35%). Host CPU-seconds **confirmed worse** on all three workloads (+14% to +28%): a smaller
  pool makes PgBouncer queue clients, and queuing costs the host CPU. Work inside the line, throughput and every latency
  gauge read no difference beyond the noise: native's own p95 swings a hundredfold between repetitions on GitHub's shared
  runner. Failed transactions 0 in both arms; the knob handed back in every arm. The honest reading for a database behind
  a pooler: Omni holds a third of the connections for the same work, at a CPU cost, and the shared runner is too noisy
  to tell the latencies apart. Register row 30; the Omni index reads the table.
- The six organisms with the real cluster inside, v1 (`results/live/V1_SIX_KUBE.md`, run 37359815637): 98 of 100 cells
  (1, 10, 100 copies of all six; 1,000 copies of the four realms and the tower; the two 1,000-copy stack cells cut off by
  GitHub's six-hour job limit). p95 and time over the line better in every cell of every organism; 0 gauges worse
  beyond the noise except a rounding-level work loss (−0.0003%) in the larger cells and HPA replicas +0.7% in one cell;
  the machines stay at 6 in both arms (kind has no node autoscaler). The big organisms on Azure (37359820055): the tower
  at 1,000 copies 3 of 3 done; the stack at 1,000 copies never finished inside a six-hour job and needs a run detached
  from GitHub's job, to build.
- The six-organism grid on v3, 10 copies (`results/scale/receipts/v3-10x.md` from run 37433972731): every organism
  superior within guardrails at 10, 100 and 1,000 runs; 100 copies dispatched.
- The six-organism grid on v3, 1 copy (`results/scale/GRID.md`, receipt `results/scale/receipts/v3-1x.md` from run
  37430723080: 60 shards, 1,000 paired runs per organism): every organism superior within guardrails at 10, 100 and
  1,000 runs, work per energy +0.08% to +0.3%, every knob handed back. The v1 grid and its receipts move to
  `results/scale/v1/`; `tools/grid.py` builds the grid from the current engine's receipts (`v3-<size>x.md`) and marks
  the sizes not yet run as "to run". 10 copies is running; 100 and 1,000 follow one at a time.
- **PostgreSQL: the first untouched run was a loss, and it is kept** (run 37425853293, `docs/POSTGRES_PREREGISTRATION.md`):
  on the read-only workload Omni gave the pool back to its floor of two and the users' p95 went from 4 ms to 3.9 s,
  work inside the line −47%, because the compass read the pooler's own service time (0.1 ms per transaction) and the
  pooler cannot see clients backed up behind their own schedule. On the two write workloads no difference beyond the
  noise on work and latency, half to three quarters fewer connections, 10% to 18% more host CPU. **Amendment 1**,
  declared before the counted runs: the reading is the pooler's service time or the share of its clients queued for a
  server, whichever is worse (every client waiting is past the wall); and the dwell holds only the brake, adding is never
  held. The three untouched workloads run again three times on the amended rule (A, B, C); the first run is recorded, not
  counted. `tools/pgbench_abc.py` (with `tests/test_pgbench_abc.py` in `verify.py`) builds the three-run table by the
  readings rule.
- The power grid's v1 A/B/C table (`results/live/V1_PANDAPOWER.md`; runs 37377029333, 37397142210, 37412578757 on the
  v1 fingerprint; 11 untouched SimBench grids, a full year each, both load models, every gauge reproduced in 3 of 3):
  with ZIP loads the energy the loads drew is confirmed better in all 11 grids (−1.3% to −1.5%) and the net import in
  all 11 (−1% to −15%); losses confirmed better in 7 and confirmed worse in 4 (the rural and semi-urban grids that carry
  their own generation, +0.6% to +1.5%: a lower voltage draws more current for the same power through those feeders);
  tap operations fewer in 10 grids (−27% to −36%) and 4 → 8 a year in one rural grid, the cost declared before the run;
  no grid is ever more often outside its 0.95-1.05 band, two are less often. With constant-power loads the energy
  drawn is the same by construction, the import better in 7 grids and worse by 0.01% to 0.03% in 4. Register row 28.
- **The v3 realms table** (`results/realms/`; runs 37429141430, 37429151263 and 37429161515 on the v3 fingerprint, A, B
  and C reproduced to the last digit; v2's table moved to `results/realms/v2/`): 945 muscles, 0 worse; 124 superior
  within guardrails, 807 no difference beyond the noise, 9 energy improvement with a service tradeoff (all of them
  v1's), 4 service improvement with an energy tradeoff, 1 not established (hoist_speed_target (elevator_hoist, capacity)). **Every organism superior within
  guardrails**: work per energy Compute +0.1%, Physics +0.1%, Energy +0.3%, Distribution +0.2%, the whole tower +0.3%;
  work unchanged; time over the line not above native's in any organism. Fourteen rows changed label against v2: the
  rail, marine, elevator, EV and robot-joint speed muscles the slack gate now leaves native read no difference beyond
  the noise (two of them had read superior under v2, two of them now read native: that is the price of the gate and it
  is shown).
- **Omni v3** (`OMNI_V3.json`, `docs/OMNI_V3.md`; declared in `docs/REALMS_PREREGISTRATION.md` before any v3 run, the
  founder told first). Two changes against v2, both in the modelled realms: the slack gate on speed knobs
  (`realms/compass_arm.py`, `speed_slack`): a motion axis is offered its speed knob only where it is busy at most half
  the time at full speed (task rate × (move time + dwell) ≤ 0.5, from the plant's own figures), as the robot benchmark's
  paired physics trial leaves a loaded arm native; and the marine propulsion preset, twelve 200 rad speed changes an
  hour instead of four of 600, so a one-hour run holds enough moves to count. On the shipped presets the knob is offered
  on a flight axis (duty 0.34) and a reaction wheel (0.35) and left native on rail traction (0.80), EV traction (0.76),
  robot joints (0.54 at the middle size; a muscle's own size moves it either side), marine propulsion (0.52) and
  elevator hoists (0.52). The law, the controllers, the catalog and the runners are v2's byte for byte.
  `tests/test_compass_arm.py` proves the gate; the realms workflow compares a run with the published table only when
  both carry the same frozen tree. Every modelled result is to be run again on v3; the v2 table stays a v2 result.
- **The v2 realms table** (`results/realms/REALMS.md`, `MUSCLES.csv`, `REALMS.json`; runs 37422832244, 37422840154 and
  37422847697 on the v2 fingerprint, A, B and C reproduced to the last digit; v1's table moved to `results/realms/v1/`):
  945 muscles, 0 worse; 126 superior within guardrails, 793 no difference beyond the noise, 15 energy improvement with a
  service tradeoff (9 were v1's), 7 not established, 4 service improvement with an energy tradeoff. The not-established
  rows are new: three rail traction speed muscles where Omni's slowing adds 1.6 to 2.7 points of lateness on a train
  that runs near its timetable's capacity, two marine propulsion and two elevator speed muscles where the slower cycle
  finishes fewer moves in the hour. The organisms: Compute, Energy and Distribution superior within guardrails;
  Physics and the whole tower energy improvement with a service tradeoff (+0.1% and +0.3% work per energy, time over
  the line up by under 0.01 point), where v1 had every organism superior. By the honesty rule the first suspect is our
  own wiring: the speed knob on a motion axis has no do-no-harm gate in the realm harness (the robot benchmark has one,
  its paired physics trial), so a train or a ship with no slack is slowed anyway. The fix is an engine change and makes
  v3; it is declared in `docs/REALMS_PREREGISTRATION.md` before any v3 run.
- The PostgreSQL tuning run (37420052827, `tpcb`, 3 paired repetitions, not counted): server connections alive 20 to
  9.3 (−53%, better); work inside the line, throughput and every latency gauge no difference beyond the noise (native's
  own p95 swung from 86 ms to 3.3 s between repetitions on GitHub's shared runner); host CPU-seconds +11% worse, CPU
  per 1,000 transactions inside the line no difference; 0 failed transactions in both arms; the knob handed back every
  time. Recorded in `docs/POSTGRES_PREREGISTRATION.md`; the three untouched workloads run next.
- `OMNI_V2.json` rewritten from the checkout's tracked files (40 files, digest `4fc223939c4fab03`): its first write had
  listed the last commit's tree and missed `realms/catalog_v1.csv` and `realms/wave4_families.csv`, so no commit read as
  v2 although the engine's bytes were v2's throughout; `tools/omni_version.py` now lists every tracked or staged file
  for the checkout, and `verify.py` requires the checkout's engine to carry a declared fingerprint.
- The realms runner's report (`tools/run_realms.py`) names the muscle count from the results it writes (the first three v2
  realms runs, 37420034190, 37420040519 and 37420047009, stopped at the report with an undefined name and are run again);
  the realms workflow compares a run's table with the published one only when both are on the same engine (the same
  muscle count), otherwise it says so and lets the run stand as the first on that engine.
- Databases, preregistered and built (`docs/POSTGRES_PREREGISTRATION.md`, `tools/run_pgbench.py`,
  `.github/workflows/pgbench.yml`, `tests/test_run_pgbench.py` run by `verify.py`): PostgreSQL 16 as the distribution
  ships it behind PgBouncer 1.22 with the pool of 20 server connections it ships with (the DBA's one fixed setting) is
  native; omni is the same with the compass law on the pool size, written through PgBouncer's own console inside [2, 90]
  and handed back at the end. The reading is the service time the pooler itself reports each second (transaction time
  plus the wait for a server), on a band to a 50 ms line; where the time goes decides the direction (waiting for a
  server: more slots, by the force; inside the server: one fewer); calm gives back one idle server a second and never
  one in use; past the wall the knob is handed back to the pooler's own setting at once. pgbench offers the load, 64
  clients, the rate stepping one notch at a time with the peak notch at nine tenths of native's own unlimited capacity,
  found once in native mode before the counted runs. Gauges from pgbench's own log (work inside the line, p95, failed),
  PgBouncer's pools (server connections alive, the machines) and the host's CPU-seconds, measured, no energy claimed.
  The first smoke on a 4-core box (one repetition, not counted): omni 1,400 against 1,312 transactions a second inside
  the line, p95 24.5 against 77.2 ms over the profile, 11 server connections alive against 20; at the lightest notch
  omni's p95 was higher (14.6 against 3.9 ms, inside the line), the declared cost of the take-back at light load.
- The robot runner's test (`tests/test_run_mujoco.py`) compares the result, not the wall-clock bookkeeping: the run's
  elapsed seconds flipped between 0.0 and 0.1 under load and had failed the determinism check once.
- The Omni index's columns now say what the sign means (`tools/omni_index.py`, `results/OMNI_INDEX.md`): "more work
  by", "faster by", "fewer machines by", "less energy by", every column pointing the same way, plus good for
  Omni-Compass; the reading line spells out each one ("fewer machines by +4%" is the same work on 4% fewer
  machine-hours).
- The legal notice every generated report carries (`tools/legal.py`) now says "filed in the USA" and "filed in the USA" with a closing sentence since removed (2026-10-07), as the standing orders had it; the committed reports were brought to the same wording (the archived
  raw run folders were left as the bot wrote them, their checksums intact).
- The robot arms' v1 A/B/C tables (`results/live/V1_MUJOCO.md`: UR5e, iiwa 14, Gen3, runs 37409191253, 37409852642,
  37410015922; `results/live/V1_MUJOCO_PANDA.md`: the tuning robot, runs 37409198316, 37409860065, 37410022940; all on
  the v1 fingerprint, every gauge reproduced to the last digit in all three). A robot on a line is judged on hitting its
  points and lasting, and that is where Omni moved it: where the paired physics trial let Omni move, the arm hit its
  points more accurately with less force on its motors, doing the same job inside the same takt. Peak motor torque
  confirmed better (Gen3 −29%, Panda −10%), tracking error confirmed better (−21% on both), the cycle 27% longer and
  inside the takt; the energy per takt also confirmed better, by a little (Gen3 −0.8%, Panda −0.5%); the Panda's copper
  loss confirmed worse (+14%, the gravity-holding torque paid for longer). The UR5e and the iiwa 14 are left native by
  the trial (slowing would cost on their own figures), so Omni moves nothing there and nothing gets worse.
- The robot arms, preregistered and built (`docs/ROBOTICS_PREREGISTRATION.md`, `tools/run_mujoco.py`,
  `.github/workflows/mujoco.yml`, `tools/mujoco_abc.py`; tests in `verify.py`): MuJoCo integrates each arm, MuJoCo
  Menagerie supplies the robot with the position servos it ships with as native, and Omni sits on top on one knob, the
  speed override, inside the task's takt. The planned speed is set per robot as the fastest its own servo tracks; a
  paired physics trial in native mode, before any counted cycle, leaves the override native where a slower cycle is not
  cheaper (the gravity-holding torque is paid for longer), the do-no-harm gate on the arm's own figures. Energy is a
  declared model from MuJoCo's torques and velocities, with the standing draw charged for the whole takt in both arms.
  The first smoke: the tuning robot and the Kinova move (tracking error and peak torque lower, cycles 25% longer inside
  the takt, motion energy −1.7% and −7%, energy per takt −0.5% and −0.8%); the UR5e and the iiwa are left native by the
  trial. Disclosed: the waypoint offset was capped at 0.6 rad after the first smoke showed the UR5e model's full-turn
  joint ranges turned "25% of the range" into 90-degree swings into the floor. MuJoCo and the Menagerie commit are pinned.
- CityLearn's v1 A/B/C table (`results/live/V1_CITYLEARN.md`, runs 37384954241, 37393198549, 37399402398, all on the v1
  fingerprint): 11 districts with electric batteries, every score reproduced to the last digit in all three runs except
  the comfort score, which CityLearn itself varies between runs (it reads "the runs differ" and is not claimed).
  Electricity bought, daily peak and daily load unevenness confirmed better in all 11 districts; carbon better in 8, same
  in 3; the bill confirmed better in 1 district and confirmed worse in 7 (the 2023 challenge districts, +0.2% to
  +0.35%); ramping confirmed better in 4 and worse in 7 (the 2023 districts, +4.5% to +6.2%); the highest peak worse in
  the three 2023 phase-3 districts; energy not served worse in the 2023 districts. Three districts have no battery, so
  Omni moves nothing there; eight CityLearn's own controller cannot run, listed with its error.
- The Omni index rebuilt on v1 (`tools/omni_index.py`, `results/OMNI_INDEX.md`): it now reads each test's v1 table
  (`results/live/V1_*.json`, which `tools/confirm_abc.py` writes beside every `.md`) and lets a measure in only as its
  three-run reading allows: confirmed better or confirmed worse counts as the geometric mean of the three runs' ratios,
  and anything inside the noise counts as exactly 1. Real Kubernetes, six tests: **+26.2%** (work +20.4%, speed +95.1%,
  machines +4.4%, energy +2.7%). Azure's billed runs and the card join when their v1 runs land; the earlier engine's
  index (+12.9%) is kept at `docs/history/OMNI_INDEX_pre_v1.md`. The register's Kubernetes rows point at the v1 tables.
- `PATENTS.md` states what has been filed, from the application data sheet the founder supplied: a nonprovisional
  utility patent application under 35 U.S.C. 111(a), "The Omni-Compass", inventor Alan John Dubra, 15 drawing sheets,
  signed 20 September 2026, eighteen-month publication; the application number is withheld on purpose, and the sheet
  itself (which carries personal details) is not in the repository.
- The fifth and sixth v1 A/B/C tables: all four in one run (`results/live/V1_ALL_FOUR.md`, runs 37384945573, 37385646550,
  37394444337) and wandering demand (`results/live/V1_WANDERING.md`, runs 37384942870, 37385643291, 37394436586). All
  four: work inside the response line +48.4%, +44.7%, +42.1% (18.6 → 27.6 requests a second in A), p95 −57 to −63%,
  time over the line −39 to −43%, failed requests −12 to −13%, every one confirmed better in all three runs; machines and
  energy no difference beyond the noise. Wandering: p95 −56 to −60%, time over the line −37 to −44%, failed requests −12
  to −13%, confirmed better; machines no difference; the declared energy models −0.3 to −0.8%, confirmed lower. All six
  Kubernetes tests now have their three v1 runs; the README's result table is the v1 readings.
- The fourth v1 A/B/C table, the batch queue (`results/live/V1_BATCH.md`, runs 37385637932, 37385654462, 37394452486):
  machines in service −15 to −24%, machines after the queue is done −26 to −36%, standby-model energy −11 to −17% and
  mean response −11 to −13%, every one confirmed better in all three runs; the queue finished 0.7-0.9% later, clear of
  the noise in two runs and inside it in one, so that row reads no difference beyond the noise in 1 of 3 runs; p95 and
  the idle-power energy model no difference beyond the noise. The confirmation tool now reads the batch queue's finish
  time and machines-after, and a real cloud's bill, as lower-is-better (one row had read "confirmed lower").
- The power grid's A/B/C table by rule (`tools/pandapower_abc.py`; `tests/test_pandapower_abc.py`, run by `verify.py`):
  pandapower is deterministic, so the three runs must reproduce each other; a gauge reads confirmed better or worse by its
  sign when they do, same under one part in a million, "the runs differ" when they do not; any added voltage violation and
  every extra tap operation read WORSE. The first v1 grid run (37377029333, 11 untouched SimBench grids, a full year,
  both load models): with ZIP loads the energy the loads drew is 1.3-1.5% lower in all 11 grids and the net import lower
  in all 11; losses are lower in 7 and higher in 4 (the rural and two semiurban grids, +0.6 to +1.5%); voltage violations
  never increase; tap operations fall in 10 grids (the city, suburb and commercial grids tap hundreds to thousands of
  times a year natively, Omni cuts that 20-35%) and double from 4 to 8 in one rural grid; with constant-power loads the
  load energy cannot change and the loss and import rows split the same way.
- GitHub's verify check caught a bug in the A/B/C tools that the local check missed: when a run's commit could not be
  read (GitHub's `gh` prints nothing for an unknown run), `tools/omni_version.py --commit ""` quietly checked the working
  tree instead, so an unresolvable run would have read as v1. Now a commit that cannot be read is "unknown" in both tables
  (`tools/confirm_abc.py`, `tools/citylearn_abc.py`), `omni_version.py` refuses an empty commit, and the test asserts it.
- The third v1 A/B/C table, steady load (`results/live/V1_STEADY.md`, runs 37384939815, 37385640601, 37391296025, all
  on the v1 fingerprint): mean response −47 to −51%, p95 −65 to −69%, time over the line −98 to −99%, machines in service
  −1.5 to −3.4%, standby-model energy −1.0 to −2.9%, every one confirmed better in all three runs; the idle-power energy
  model reads no difference beyond the noise in 2 of 3; failed requests zero in both arms. Three of the six Kubernetes
  tests now have their three runs: steady and faults confirmed better, fairness no difference beyond the noise.
- CityLearn's A/B/C table by rule (`tools/citylearn_abc.py`; `tests/test_citylearn_abc.py`, run by `verify.py`). CityLearn is a
  deterministic simulator, so the three runs must reproduce each other: a score reads confirmed better or confirmed worse
  by its sign when they do, same under one part in a million, and "the runs differ" when they do not, which is a finding
  about the simulator or the harness. Two things the first v1 run showed, now stated in the table rather than hidden in a
  per-district reading: a district with no electric battery gets nothing from Omni (the runner moves only
  `electrical_storage` commands; the Quebec districts' comfort score still differs between the arms, which is CityLearn's
  own run-to-run variation, not an Omni result), and the 2023 challenge districts come out worse on the bill (+0.2 to
  +0.35%), ramping (+4.5 to +6.2%) and energy not served (+2 to +10%) while better on daily peak and electricity bought.
  Eight districts CityLearn's own controller cannot run are listed with CityLearn's error.
- The confirmation table carries the capacity test's own gauge as a judged row: work inside the response line (requests a
  second, higher is better), read from the run file's capacity block with its interval. The first v1 all-four run reads
  18.6 → 27.6 requests a second, +48.4% (+6.0 to +12.0 requests a second), p95 −63.2%, time over the line −40.0%.
- The A/B/C confirmation table is made by rule (`tools/confirm_abc.py`; `tests/test_confirm_abc.py`, run by `verify.py`):
  three separate GitHub runs on the same frozen engine, each checked against the v1 fingerprint. Every judged row gets
  one of three readings: confirmed better or confirmed worse (the same sign in all three, every 95% interval clear of
  zero); no difference beyond the noise (an interval includes zero: native and omni could not be told apart on that
  measure, with the count of such runs); the runs disagree (runs clear of the noise point different ways). Nothing reads
  "not confirmed": a measurement the test cannot tell from zero is a result, and is stated as one.
- The archive keeps every raw file within GitHub's limit: GitHub refuses a file over 100 MB, and the 1,226-muscle
  organism at 1,000 copies writes a 99.6 MB record, so a slightly larger v1 record would have stopped the archive.
  `archive-run.yml` now stores any raw file over 50 MB gzipped (`gzip -n`, the same bytes every time; its repetition's
  `SHA256SUMS.txt` keeps the original's hash: `gunzip -c FILE.gz | sha256sum`). `tools/six_kube_report.py` reads the
  record plain or gzipped, and `tests/test_six_kube.py`, now run by `verify.py`, checks that both read the same.

## 2026-10-05
- Omni v1: the engine frozen and fingerprinted (`OMNI_V1.json`, `docs/OMNI_V1.md`, `tools/omni_version.py`): one SHA-256
  per engine file (38) and one digest over all of them. Every result states the version it ran on; any change makes v2
  and everything runs again. Every v1 benchmark runs three times (A, B, C); a claim is confirmed only when all three
  agree, with the 95% interval clear of zero in each. The register states the old GPU card result as the trade-off it
  was (card energy -3.5%, p95 +58.5%).
- The verify check on GitHub failed on the register commit (`f162ce8`) in the several-card GPU bench, which was ruled
  INVALID. The cause was in the test's stand-in `nvidia-smi` (`tests/fake_gpu/nvidia-smi`), not in Omni: every write
  opened the shared state file with "w", which empties it before the atomic replace. A process reading in that moment
  failed (22 of 400 reads with another process writing; 0 of 400 after the fix), which happens more often on GitHub's
  slower runners. Writes now go only through a temporary file and an atomic replace. A new test
  (`state_never_empty` in `tests/test_gpu_bench.py`) fails on the old stand-in (13 of 150 reads) and passes on the fixed
  one. Engine bytes unchanged: still omni-v1.
- `CLAUDE.md`: the founder's standing orders, kept in the repository so every working session starts from them.
- The batch test with cruise stepping back (`results/live/BATCH.md`): machines -20.7%, -32.4% once the queue is done,
  energy -14.3% (standby model), mean response -11.7%; queue time +1.1%, inside the noise. Added to the Omni index.
- Tweak A finished, muscle by muscle (`docs/MECHANISM_OF_ACTION.md` 9.6, `docs/REALMS_PREREGISTRATION.md`): the 656 muscles
  on the compass law read 0 WORSE and 0 NOT ESTABLISHED (108 worse this morning), every organism SUPERIOR WITHIN
  GUARDRAILS. Each lever moves only where its physics says it can pay: cooling power native; a UPS reserve native; a
  battery reserve spent only at the connection's wall when it can cover the overrun (the four batteries that buy fewer
  overruns read SERVICE IMPROVEMENT WITH ENERGY TRADEOFF); a power cap only where the machine's own curve saves (9.8);
  an effort cap only where copper loss exceeds the standing draw; node-pool machines released at margin 0.3, where no
  pool is later than native. Nine muscles read ENERGY IMPROVEMENT WITH SERVICE TRADEOFF: they run a little slower for
  less energy, which the label states.
- Tweaks A-E before any GPU run (`docs/MECHANISM_OF_ACTION.md` section 9; amendments 11 and 12; the realms amendment):
  - A. The 656-muscle realms table now runs the compass law (it still compared native against the retired allocation
    law). On the compass law all five organisms are SUPERIOR WITHIN GUARDRAILS: energy 0.1-0.2% lower, work the same,
    lateness no higher. Per muscle: 64 superior, 9 worse (from 108). The allocation-law table moves to
    `docs/history/realms_allocation_law/`. Also fixed: each modelled muscle's compass was made fresh at every decision
    (from the rename); the organism runs go again on the fixed code.
  - B. The Azure burst test at `1 3 1 4 1 3`: at `1 6 1 8 1 6` the service's capped autoscaler could not serve the load in
    either arm (41% failed in both).
  - C. While cruising, the floor step reads and writes nothing (it read every pod every five seconds while a queue
    drained).
  - D. A change under one part in a million of the value reads "same", the number still shown.
  - E. The organism's start file is written whole and read only when whole (one six-kube repetition read it empty); the
    CityLearn omni arm's undefined name, left by the rename, is fixed.
- The Kubernetes results on the frozen engine: steady, wandering, all four, faults, fairness (`results/live/`). Capacity
  +41.7%, p95 59-64% faster, machines up to 2% fewer (the verdict keeps a machine when giving it back slows the
  service), energy equal or lower, no pod ever without a machine. The Omni index is now read from these only: +12.9%.
  The README and STATE_OF_PLAY say so; the earlier engines' sets go to history.
- Amendment 10 (Kubernetes reporting): pods the scheduler could not place are counted and judged; the snapshot count of
  pending pods and energy per core-hour are shown, not judged. Disclosed as made after the results were seen.
- GPU amendment 12: the steady hold applies only under an operator's cap (bisected: it slowed the card on its own
  firmware). The card model regenerated on this code.
- CityLearn round 2: four districts better on electricity, peak and ramping (`results/citylearn/round2/`).
- Amendment 9: the emergency brake also reads idle from the autoscaler's floor (least pods, wanting no more, half
  its target or less), so it fires when a queue empties, not only at a zero reading a served service never shows. No
  result already measured could change (0 of 5,102 readings at the floor). The recording script no longer stops on an
  unanswered reading of machine CPU; end-of-window reads are retried. The batch test runs again.
- The law is named for what it is: the compass law (the word "bowl" is gone). In code: `omnicompass/compass_law.py`
  (class `CompassLaw`), `realms/compass_arm.py`, `omni_controller/gpu_compass.py`; the arm is `compass`. Runs recorded
  before the rename keep their folder names (`bench-bowl-N`), which the report tools read as the compass arm.
  The preregistration is `docs/K8S_COMPASS_PREREGISTRATION.md`. Raw recorded files and sealed records are untouched.
- The verifier's final line now reflects every check. It had read a local name left from the preregistration loop, so it
  printed PASS even when a check above it failed (`verify.py`). With that fixed, two hidden failures surfaced and were
  fixed. (1) The sealed GPU governor had three comment and log strings changed by the "reset" rename; its sealed bytes
  are restored, and behaviour is unchanged. (2) The mechanism identity was re-recorded: only M_act (the GPU actuator)
  changed, from the recorded GPU amendments; F, Theta, C, h, G, dt and A and every fixture result are identical.
  160 checks pass, none fail.
- On the frozen engine: the fault test and the fairness test, ten pairs each (`results/live/FAULTS.md`,
  `results/live/FAIRNESS.md`). Nothing came out worse beyond the noise; the Omni index is now +15.6%.
- The archive takes a list of runs; failed Azure and CityLearn runs post their own output on the run's page.
- One engine, frozen: the live Kubernetes controller with rules 1-8. New today: rule 5 (a pinned gauge is not a steady
  demand), rule 6 (coasting: ease off a step a window), rule 7 (cruise: every machine in service while work waits),
  rule 8 (the emergency brake: straight to the floor at zero demand). The floor of two machines; every machine usable.
- The names: native (the system on its own) and omni (Omni-Compass on top of native); the pedals (idle, gas, brake,
  reset) and the kill switch (security only, `omnicompass/master.py`).
- CityLearn, an independent simulator of real buildings and batteries: round 1 recorded (battery districts better,
  water-tank districts worse on peaks), the fix (only the electric batteries steered), round 2 on untouched districts.
- The harness keeps recording through an unanswered reading or load step (the Azure burst test lost two native arms to
  it before the fix).
- The batch test (a queue of jobs) for cruise and the emergency brake.
- The repository lined up: the front door, one index of documents, dated reports in `docs/history/`, the layout check
  in every verification.

## 2026-10-04
- The Omni index; all four in one run (+29% work, p95 -62%, machines -3.6%, energy -0.3%, each proven); the six
  organisms with the real cluster inside; the staging law written as equations.

## 2026-10-02
- The compass law (`omnicompass/compass_law.py`) and the plug contract: one smooth law for every muscle, one restore point,
  read-back, the one-writer rule.
- Two-wire GPU governor (`omni_controller/gpu_compass.py`): clock ceiling and power limit; the wire check
  (`tools/gpu_wire_check.py`) runs before anything else.
- The six organisms (four realms, the four stacked with duplicates, the whole tower) as one benchmark set, with the
  real card inside on a GPU machine (`tools/run_hil.py`) and the 1 / 10 / 100 / 1,000 runs-and-size grid
  (`tools/run_scale.py`, workflow `six`).
- Robot-joint simulation compiled (identical results, about 30 times faster).
- Real Kubernetes set 24 reproduces set 23.
- License: evaluation and simulation use only; Omni-Compass Enterprise License for everything else; US filings notice.
- The Omni-Compass Manual, edition 1.0.

## Earlier
See `docs/HISTORY.md` and `docs/STATE_OF_PLAY.md`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
