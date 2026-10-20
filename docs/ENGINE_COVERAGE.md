# How much of the engine the tests run

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Line coverage of every Python file in the engine that stands (omni-v12), under the whole test suite: the unittest suite and every file `tools/function_tests.py` runs. Measured with coverage.py by `python3 tools/engine_coverage.py --measure` on commit `7ba7fc02048d`; `tools/engine_coverage.py --check`, run by `verify.py`, fails a push where this page is not what `results/ENGINE_COVERAGE.json` records.

**82% of the engine's 6,531 statements run under the tests** (5,324 run, 1,207 not). Coverage counts lines a test executes, not what it asserts: the properties the tests check are in `tests/test_engine_properties.py`, and the proofs of the core in `docs/ENGINE_PROOFS.md`.

| Engine file | Statements | Run by the tests | Coverage |
|---|---:|---:|---:|
| `tools/run_citylearn.py` | 166 | 41 | 25% |
| `omnicompass/stack_sim.py` | 210 | 55 | 26% |
| `omnicompass/closure.py` | 151 | 61 | 40% |
| `omnicompass/speed.py` | 60 | 25 | 42% |
| `omnicompass/mathdrive.py` | 50 | 22 | 44% |
| `omnicompass/shield.py` | 79 | 41 | 52% |
| `tools/run_kil.py` | 132 | 94 | 71% |
| `realms/plants.py` | 642 | 458 | 71% |
| `omnicompass/adapter.py` | 192 | 141 | 73% |
| `omnicompass/core.py` | 159 | 121 | 76% |
| `omni_controller/gpu_compass.py` | 295 | 227 | 77% |
| `omnicompass/master.py` | 77 | 63 | 82% |
| `realms/harness.py` | 413 | 354 | 86% |
| `omni_controller/quota.py` | 86 | 75 | 87% |
| `omni_controller/controller.py` | 850 | 760 | 89% |
| `omnicompass/compass.py` | 82 | 75 | 91% |
| `omnicompass/edge.py` | 49 | 45 | 92% |
| `realms/compass_arm_v5.py` | 838 | 770 | 92% |
| `omnicompass/conveyance.py` | 52 | 48 | 92% |
| `omnicompass/muscle_sdk.py` | 215 | 199 | 93% |
| `omni_controller/capacity.py` | 62 | 58 | 94% |
| `omnicompass/configurations.py` | 31 | 29 | 94% |
| `omnicompass/disruption_budget.py` | 16 | 15 | 94% |
| `omnicompass/storage.py` | 32 | 30 | 94% |
| `omni_controller/gpu_governor.py` | 354 | 332 | 94% |
| `omni_controller/muscles.py` | 564 | 531 | 94% |
| `omnicompass/student_t.py` | 52 | 49 | 94% |
| `omnicompass/compass_law.py` | 95 | 90 | 95% |
| `realms/compass_arm.py` | 107 | 102 | 95% |
| `omnicompass/authority_contract.py` | 26 | 25 | 96% |
| `realms/gpu_card.py` | 172 | 167 | 97% |
| `omnicompass/verdict.py` | 109 | 108 | 99% |
| `omnicompass/ce_score.py` | 7 | 7 | 100% |
| `omnicompass/nervous_system.py` | 65 | 65 | 100% |
| `realms/presets.py` | 41 | 41 | 100% |

## Where the tests reach least

Files under 60%: `tools/run_citylearn.py`, `omnicompass/stack_sim.py`, `omnicompass/closure.py`, `omnicompass/speed.py`, `omnicompass/mathdrive.py`, `omnicompass/shield.py`. The CityLearn runner is exercised by its own benchmark on GitHub (`citylearn.yml`, three runs on every engine) rather than by a unit test; the stack simulator, the shield and the speed and mathdrive modules hold paths the live governors do not call. Raising each to the level of the rest is the next tests' work: no engine file changes for a test.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
