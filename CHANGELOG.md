# Changelog

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE` at the root of this repository.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

## 2026-10-06
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
