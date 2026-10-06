# Changelog

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE` at the root of this repository.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

## 2026-10-06
- **The stack at 1,000 copies, detached from the GitHub job** (`.github/workflows/big-organism-detached.yml`): every
  attempt at the four stacked with the real cluster inside was cut off by GitHub's six-hour job limit (v1 run
  37359820055: the tower 3 of 3 done, the stack 0 of 3). The new workflow rents one Azure machine, starts every repetition
  under nohup and leaves it running; a look every two hours collects the files when all are done (one artifact per cell,
  the same shape as `big-organism`'s) and deletes the machine; a machine older than 40 hours is collected as it stands.
  The commit to run is an input, so the v1 stack runs again on `f162ce8` (named `stack_1226` there) beside the v3 stack.
  Package install on the fresh machine is tried five times (one v1 attempt lost its machine to a stale package list).
  First starts (17:57 UTC, westus2 and centralus): every size refused, the CLI hiding Azure's reason behind its own
  "content already consumed" error; the workflow now reads the reason out of Azure's answer and lists the region's SKU
  restrictions. The subscription's regional quota is 10 vCPUs, so one 8-vCPU machine fills a region; eastus is the
  region the metered AKS runs use, and the default is now eastus2.
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
- The legal notice every generated report carries (`tools/legal.py`) now says "filed in the USA" and "nothing here is
  set in stone", as the standing orders have it; the committed reports were brought to the same wording (the archived
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

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
