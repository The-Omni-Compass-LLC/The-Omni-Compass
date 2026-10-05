# Changelog

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE` at the root of this repository.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

## 2026-10-05
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
- The bowl law (`omnicompass/bowl.py`) and the plug contract: one smooth law for every muscle, one restore point,
  read-back, the one-writer rule.
- Two-wire GPU governor (`omni_controller/gpu_bowl.py`): clock ceiling and power limit; the wire check
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
