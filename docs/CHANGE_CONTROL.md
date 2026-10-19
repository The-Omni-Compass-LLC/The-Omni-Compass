# Change control: how the engine changes, and how a result stays tied to the engine it ran on

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The engine is the set of files whose bytes decide what Omni-Compass does: the brain, the compass law, the verdict, the live
governors, the harness the models run in, and the wires that fasten the brain to an outside simulator. Their SHA-256
digests together make the engine's fingerprint (`OMNI_V11.json`: 47 files, digest `745aa53ec8eeb67b`).
`python3 tools/omni_version.py` reads the tree and names the engine it holds, or says which file differs from every
declared engine.

## The rules

1. **Any change to a rule, a gain, a guard, a preset or a muscle makes the next version.** No engine file changes inside a
   version. A fix to a fault found in the engine is the next version, never a patch to the one that stands.
2. **Every change goes through the toy gate first** (`tools/toy_gate.py`, `results/toy_gate/`): the shipped controller on
   the toy cluster in the cloud setting, conveyance on one kind host set to a real run's own regime, the verdict on noisy
   work, the same seeds, paired against the engine that stands. A LOSS there is root-caused and fixed in the model; a
   change that reads no LOSS and shows promise goes to its GitHub trials; nothing is dispatched before.
3. **A version lands in one command**, `python3 tools/land_engine.py vN --since <UTC>`: the fingerprint, the version list,
   the conductor's campaign (`scripts/reruns.txt`), the grid's manifest and workflows, the package version (0.N.0), the
   root list and a release group. `tools/land_engine.py --check`, run by `verify.py`, refuses a push in which any of those
   places still names an older engine.
4. **Every benchmark runs again on the new version**, A, B and C, released by the conductor in a fixed order; a run is
   counted on the engine its own commit carries, read from GitHub at its head commit.
5. **No result is read across versions.** A three-run table is one engine's three runs (the table tools refuse to call
   runs on two engines one table); an older table stays its own engine's record, in `results/live/` until each
   benchmark's three runs on the new version land, then the newest table is the one shown.
6. **The founder hears every change first.** No engine change is pushed before he is told what it changes and why.

## The record

| Version | Landed (UTC) | Digest | Files | What changed, and why |
|---|---|---|---:|---|
| omni-v5 | 11 Oct 22:40 | `6093b2b88aa911b9` | 44 | the max as the default brain on the 1,107-muscle catalog; re-declared while in development |
| omni-v6 | 15 Oct 06:18 | `df6147466ef18046` | 45 | shared-host capacity: on kind the host's processor counted once |
| omni-v7 | 15 Oct 15:25 | `d6d467b824c585f1` | 46 | conveyance bounded by the namespace's CPU quota; every rule in seconds |
| omni-v8 | 17 Oct 15:39 | `f93d233136a1f902` | 46 | CityLearn: a battery whose building has outages stays native (its charge is the building's reserve) |
| omni-v9 | 17 Oct 22:21 | `7379f3a79ff2c475` | 47 | CityLearn: the battery wire reads the coming hour; the exact Student t |
| omni-v10 | 18 Oct 04:23 | `4bf39b0d707784de` | 47 | CityLearn: the battery glide that cuts the bill most with no LOSS |
| omni-v11 | 18 Oct 16:03 | `745aa53ec8eeb67b` | 47 | Kubernetes: a reading with no machine in service is held, never read as an overload |

Each version was a fault found in a real run and fixed: the record is in `docs/OMNI_V6.md` to `docs/OMNI_V11.md`, and each
toy gate's reading in `results/toy_gate/`. Seven versions in seven days is the cost of fixing every fault the day it is
found (the founder's order of 18 October: every fault fixed, none set aside); the rules above are what keep that pace from
mixing results.

## What stability means here

A version is stable for a benchmark when its three runs on that version have landed with no change in between. omni-v11
has stood since 18 October 16:03 UTC; its campaign of 129 runs is under way, and its three-run tables are in
`results/live/V11_*.md` as they land (23 on 19 October). The engine's proofs (`docs/ENGINE_PROOFS.md`), its coverage
(`docs/ENGINE_COVERAGE.md`) and its reproducibility check (`tools/reproduce.py`) are run on every push, so a version that
stands is also a version that is re-proved, re-tested and re-built from its receipts each time anything else changes.

## Gaps this page names

- The fingerprint holds three of the outside-simulator wires (`tools/run_citylearn.py`, `tools/run_pandapower.py`,
  `tools/run_kil.py`). The other wires that hold a governor's rules (the data stores' `tools/run_redis.py`,
  `run_kafka.py`, `run_pgbench.py`, `run_sysbench.py`, `run_ycsb.py`, and `tools/run_swarm.py`, `run_mujoco.py`,
  `run_cpu_power.py`) are versioned by git and tested, but a change to them does not move the digest. The next version
  takes every wire into the fingerprint, so no rule can change without the version changing.
- A wire outside the fingerprint carried a fault: the swarm's proximity reflex (`tools/run_swarm.py`) slowed a drone over a
  second where its own comment says at once, and on a mission draw outside the preregistered seeds it let drones collide
  (`results/toy_gate/V12_SWARM_REFLEX.md`). Its fix is a change to a guard, so by rule 1 it is the next version, not a patch,
  even though the file's bytes do not move today's digest.

## The next version, waiting for the founder's word

Each change below was found in a real run or in our own reading of the code, and each has its evidence written down; none is
pushed before the founder is told (rule 6), and all go through the toy gate and land together with `tools/land_engine.py`.

| Change | Why | Evidence so far |
|---|---|---|
| The swarm's proximity reflex at once, its reach growing with the square of the speed | collisions on a draw outside the fixed seeds; the margin spent in the counted cells | every drone at or outside the keep-out on all ten cells and draws tried, 49% to 92% of the energy cut kept (`results/toy_gate/V12_SWARM_REFLEX.md`) |
| Every wire that holds a governor's rules in the fingerprint | a rule could change without the version changing | the gap above |
| A command with no pipe run without a shell | the static scan's three high findings (`docs/SECURITY_SCAN.md`) | each reviewed: every one runs only the operator's own configured command, never text read from the cluster or the network |
| The Redis harness's brain in its own process, as a deployment runs it | the brain thread shares the load generator's interpreter lock | `docs/TAIL_LATENCY.md`, section 4 |
| The verdict keeps a step only when the upper end of every 95% interval of its change in cost is inside the allowance (`omnicompass/verdict.py`), its reference measured long enough, from its own spread, to show a free step within the allowance; a trial that could not be read in its time is never started | today a step is kept when its estimated cost is within the 2% allowance even if the interval reaches past it: at the noise measured on the omni-v10 tables (the spread of the log response time 0.43 to 0.46), a give-back that truly costs 3% is kept about 31% of the time, 5% about 15% (found by the live-engine session, 19 October) | 89 kept steps on the omni-v10 data-store tables had an interval reaching past 2%, none read LOSS in a table; with the rule, modelled: a free step kept 98%, a 3% step 0%; the toy gate against omni-v11 reads no LOSS on any toy. The price, said before any run: where the work is too noisy to show a step in a trial's time, the muscle stays native, and some data-store GAIN rows may read EVEN |
| The power cap the brain asks for passed through a band, so it cannot switch back and forth at one threshold | on the omni-v11 long run the recommended cap moved 41 times in 116 decisions and turned back at 40 of them, between two values, at the gate on the engine's state (`omnicompass/adapter.py`); on Kubernetes the power wire is off and nothing was written, but the card's governor reads the same request | the long run's audit read by `tools/omni_exporter.py` (run 39173420146); to be read on the card's replay in the toy gate before any chip run |
| A raise the cluster's admission refuses is not written again until the quota or the pod changes, and the kind rig's governor role reads the namespace's quotas, as the Operator's Manual asks an operator to grant | in the omni-v11 capacity test the role could not read the quota, so the budget was "no budget known" and admission was the authority, as written; admission refused every CPU-limit raise (`exceeded quota: omni-cap`) and the governor wrote it again at every fast check: about 9 refused writes a minute, nothing changed on the service, the table EVEN | `results/STEERING.md` (capacity: about 970 to 1,000 writes an hour against 17 to 214 in every other test); the audits of runs 39171068872, 39175679247 and 39179020367 |
| The kill test's after-kill reading widened to 300 s | the one tail rise of the omni-v11 kill test came 140 to 190 s after the kill, past the 120 s window declared | `docs/ROBUSTNESS_PREREGISTRATION.md`, "On omni-v11"; declared before the next version's runs |
| The Kubernetes governor counting a worker an add-on marks while it serves, and keeping its clock under load | the CruiseKube runs of 18 and 19 October | the recorder's fix of 19 October (`CHANGELOG.md`) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
