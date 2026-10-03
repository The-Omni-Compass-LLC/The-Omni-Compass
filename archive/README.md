# Archive

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Any commercial use requires a signed,
> paid Omni-Compass Enterprise License. See [`LICENSE`](../LICENSE) and [`NOTICE`](../NOTICE).

Work from earlier packages, kept unchanged so the whole path is open to inspection. Nothing here is part of the current
harness, and no current result depends on it. What replaced each piece:

| Here | What it was | Replaced by |
|---|---|---|
| `packages/xpass27/tournament/` | tournaments of Omni-Compass against other controllers (Karpenter-style replicas and public policies) | the on-top design: every comparison is native against native with Omni-Compass on top (`DISCLOSURES.md`); the cost to match (`results/live/COST_TO_MATCH.md`) |
| `packages/xpass27/organism/`, `collective/`, `plants/`, `muscles/` | earlier organism catalogue audits, scale ladders and the four-plant model | the realms, the 656-muscle catalogue and the six organisms (`realms/`, `tools/run_scale.py`, `results/scale/GRID.md`) |
| `packages/xpass27/qualification/` | earlier Kubernetes (E3) and NVIDIA (E4) qualification scripts | `scripts/kind_bench.sh`, `scripts/gpu_rented_run.sh`, `scripts/gpu_8card.sh` |
| `packages/xpass27/cpp/`, `omnicompass/`, `tools/run_*.cpp` | an earlier canonical C++ engine and muscle fabric | the sealed Python/C++ twins (`cpp/`, `results/SEAL.json`) |
| `packages/xpass27/workflows/`, `scripts/`, `tests/`, `tools/`, `docs/` | the workflows, scripts, tests and notes of those experiments | the current workflows and tests (`.github/workflows/`, `verify.py`) |
| `packages/kind_chaos_fairness/` | a chaos test and a two-application fairness test on kind | the fault test (`scripts/kind_faults.sh`, `results/live/FAULTS_31.md`); a fairness test under the current harness is planned |

Carried forward from those packages into the current tree, each with its test in `verify.py`: the disruption budget,
the universal muscle SDK, the causal authority contract and evidence gate, the independent GPU watchdog, the GPU
physical-evidence tools, and the specifications in `docs/specs/`.

---

*Evaluation and simulation use only. Commercial use, commercialization or monetization of any part of Omni-Compass
requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. See [`LICENSE`](../LICENSE).*
