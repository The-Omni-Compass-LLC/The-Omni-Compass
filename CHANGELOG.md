# Changelog

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE` at the root of this repository.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

## 2026-10-06
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
