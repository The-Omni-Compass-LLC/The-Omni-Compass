# GPU latency regression: evidence, mechanism and repair gate

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## Physical evidence (do not replace or rewrite)

- A10, 2026-10-02, 10 paired repetitions, frozen c908054: 50.79 to 52.62 served requests/kJ (+3.6%), 510.1 to 808.7 ms P95 (+58.5%, unfavorable), 3514 served both. Energy improvement fails the preregistered latency guardrail. The report records 2144 actuator writes (power and clock combined) and full restoration.
- A100, 2026-10-24, 10 paired repetitions, frozen e3b05dc: 40.48 to 40.56 requests/kJ (+0.2%, confidence interval includes zero), 252.9 to 253.4 ms P95, 6472 served both, zero power-limit writes. No causal benefit of power-limit authority demonstrated.
- These are distinct chips, controller commits and configurations. Neither establishes a 5% GPU service improvement.

## Causal hypothesis, not a proven diagnosis

The current two-wire controller in `omni_controller/gpu_compass.py` uses `service_costs()` to feed its `Verdict`: the per-request `service_ms` explicitly excludes queue wait. Its separate `position()` watches response-time P95 and failure signals, with a reactive fail-up path. A power/clock step may therefore pass a service-time comparison while increasing end-to-end queuing delay. In an open-loop arrival stream, even a modest reduction in service capacity near saturation can sharply increase tail latency. Distinguish this hypothesis from thermal throttling, scheduling, burst timing, and measurement artifacts using the raw `requests.csv`, `latency.csv`, `smi.csv` and `audit.jsonl` per repetition.

## Minimum acceptable code change before hardware confirmation

1. Preserve the engine, shield, bounded authority, frozen historical receipts and native/watch/omni design. Do not rewrite the mathematical core.
2. Add a **separate, fail-closed, end-to-end service admission gate** around GPU actuator authority. Compare observed response-time P95, served throughput and failed requests against a workload-matched native baseline; service-time-only approval is insufficient. Treat missing, stale, low-count or non-comparable telemetry as no permission to lower the native power or clock ceilings.
3. Reject a trial if P95 worsens beyond the preregistered +10% guardrail, completed requests fall beyond -1%, or unserved requests rise beyond +1% of native served. For operational safety, configure stricter margins if desired; do not silently relax the frozen historical protocol.
4. On any violation, **fail up** to the original GPU power limit and restore the original clock configuration. Verify requested and enforced limits by read-back. A refused write, failed restoration or competing writer invalidates the arm.
5. Apply a conservative hold/cooldown before any further down-step. The guard must distinguish a transient rollback from a statistically supported result. If no feasible step exists, remain native; zero writes is an acceptable outcome.
6. Unit tests must cover: stable service, queue-growth/P95 breach despite improved GPU service_ms, throughput loss, failures, stale and missing telemetry, native-baseline mismatch, competing writer, write refusal, and kill/restore. Test watch-mode no-write behavior. Keep every negative control and every failure visible.
7. Run **smoke** on the card with the new controller and collect independent raw meter and request traces. Freeze a new commit and preregistered configuration for a fresh 10-paired-repetition confirmation. Never relabel or alter the old counted runs. Report native, watch, and governing contrasts, paired intervals, latency guardrails, GPU energy, request count and actuator fidelity. No 5% claim unless supported by those new results.

## Reproduction and data location

- Historical receipts: `results/gpu/run-20261002T082232Z/GPU_REPS.md` and `results/gpu/run-20261024T091235Z/GPU_REPS.md`.
- Workload: `tools/gpu_workload.py`; controller: `omni_controller/gpu_compass.py`; one-wire alternative: `omni_controller/gpu_governor.py`; orchestrator: `scripts/gpu_paired.sh`; analysis: `tools/gpu_reps.py`; frozen rules: `docs/GPU_PREREGISTRATION.md`.
- Proposed command **only after guard implementation and tests**: `sudo PHASE=smoke REPS=1 DURATION=300 ENVELOPE=/path/to/approved-envelope.json bash scripts/gpu_paired.sh`. Run only on an authorized GPU with safe power limits and a verified restore path. A subsequent counted run requires a new clean freeze, the required 10 repetitions, and archived raw receipts.

**Status:** diagnostic engineering specification only. No new GPU controller code, hardware run, performance improvement or passing verification is claimed by this document.

---

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
