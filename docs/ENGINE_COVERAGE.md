# How much of the engine the tests run

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Line coverage of every Python file in the engine it was measured on (omni-v18; omni-v22, the engine that stands since, is measured at the next `--measure`), under the whole test suite: the unittest suite and every file `tools/function_tests.py` runs. Measured with coverage.py by `python3 tools/engine_coverage.py --measure` on commit `79e60a53bf27`; `tools/engine_coverage.py --check`, run by `verify.py`, fails a push where this page is not what `results/ENGINE_COVERAGE.json` records.

**70% of the engine's 10,318 statements run under the tests** (7,241 run, 3,077 not). Coverage counts lines a test executes, not what it asserts: the properties the tests check are in `tests/test_engine_properties.py`, and the proofs of the core in `docs/ENGINE_PROOFS.md`.

The 8 runners omni-v15 took into the fingerprint (the data stores', the swarm's, MuJoCo's and the CPU power runner, `tools/run_*.py`) hold 3,106 of these statements, 49% of them run under the tests: each is run whole by its own benchmark on GitHub, A, B and C, rather than by a unit test. The other 42 Python files, the engine as it stood before them, hold 7,212, 79% run. The whole figure fell when those runners came in; no test was lost.

| Engine file | Statements | Run by the tests | Coverage |
|---|---:|---:|---:|
| `tools/run_pgbench.py` | 581 | 96 | 17% |
| `tools/run_citylearn.py` | 166 | 41 | 25% |
| `omnicompass/stack_sim.py` | 210 | 55 | 26% |
| `tools/run_kafka.py` | 373 | 122 | 33% |
| `omni_orchestrator/control.py` | 476 | 176 | 37% |
| `omnicompass/closure.py` | 151 | 61 | 40% |
| `omnicompass/speed.py` | 60 | 25 | 42% |
| `tools/run_ycsb.py` | 394 | 173 | 44% |
| `omnicompass/mathdrive.py` | 50 | 22 | 44% |
| `tools/run_redis.py` | 356 | 165 | 46% |
| `tools/run_sysbench.py` | 386 | 187 | 48% |
| `omnicompass/shield.py` | 79 | 41 | 52% |
| `tools/run_swarm.py` | 257 | 134 | 52% |
| `tools/run_kil.py` | 132 | 94 | 71% |
| `realms/plants.py` | 642 | 458 | 71% |
| `omnicompass/adapter.py` | 207 | 157 | 76% |
| `omnicompass/core.py` | 159 | 121 | 76% |
| `omni_controller/gpu_compass.py` | 295 | 227 | 77% |
| `tools/run_mujoco.py` | 205 | 165 | 80% |
| `omnicompass/master.py` | 77 | 63 | 82% |
| `tools/run_cpu_power.py` | 554 | 474 | 86% |
| `realms/harness.py` | 413 | 354 | 86% |
| `omni_controller/quota.py` | 86 | 75 | 87% |
| `omnicompass/compass.py` | 82 | 75 | 91% |
| `realms/compass_arm_v5.py` | 838 | 770 | 92% |
| `omnicompass/conveyance.py` | 52 | 48 | 92% |
| `omnicompass/muscle_sdk.py` | 215 | 199 | 93% |
| `omni_controller/controller.py` | 909 | 842 | 93% |
| `omnicompass/edge.py` | 56 | 52 | 93% |
| `omnicompass/configurations.py` | 31 | 29 | 94% |
| `omni_controller/capacity.py` | 63 | 59 | 94% |
| `omnicompass/disruption_budget.py` | 16 | 15 | 94% |
| `omnicompass/storage.py` | 32 | 30 | 94% |
| `omni_controller/gpu_governor.py` | 354 | 332 | 94% |
| `omnicompass/student_t.py` | 52 | 49 | 94% |
| `omni_controller/muscles.py` | 608 | 573 | 94% |
| `omnicompass/compass_law.py` | 95 | 90 | 95% |
| `realms/compass_arm.py` | 107 | 102 | 95% |
| `omnicompass/authority_contract.py` | 26 | 25 | 96% |
| `omni_orchestrator/brain.py` | 58 | 56 | 97% |
| `realms/gpu_card.py` | 172 | 167 | 97% |
| `omnicompass/verdict.py` | 109 | 108 | 99% |
| `omni_orchestrator/scheduler.py` | 21 | 21 | 100% |
| `omnicompass/ce_score.py` | 7 | 7 | 100% |
| `omnicompass/nervous_system.py` | 65 | 65 | 100% |
| `realms/presets.py` | 41 | 41 | 100% |

## Where the tests reach least

Files under 60%: `tools/run_pgbench.py`, `tools/run_citylearn.py`, `omnicompass/stack_sim.py`, `tools/run_kafka.py`, `omni_orchestrator/control.py`, `omnicompass/closure.py`, `omnicompass/speed.py`, `tools/run_ycsb.py`, `omnicompass/mathdrive.py`, `tools/run_redis.py`, `tools/run_sysbench.py`, `omnicompass/shield.py`, `tools/run_swarm.py`. The CityLearn runner and the runners of the data stores and the swarm are exercised by their own benchmarks on GitHub (`citylearn.yml`, `redis.yml` and the rest, three runs on every engine) rather than by a unit test; the stack simulator, the shield and the speed and mathdrive modules hold paths the live governors do not call. Raising each to the level of the rest is the next tests' work: no engine file changes for a test.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
