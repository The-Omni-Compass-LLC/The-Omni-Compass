# Referee audit: evidence and convergence gates (2026-10-27)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This is an **audit worklist**, not a certification. No independent reviewer has approved the results. Never promote a model, simulation, or finite fixture test into a physical measurement or global theorem.

## Release identity
- Every published verification receipt must identify the exact source commit, engine fingerprint, benchmark version, test inputs, and generated artifacts.
- A quick verification receipt from an older commit does **not** certify the current head. Mark it historical until rerun.
- The live-engine appraisal introduction currently describes omni-v17 while its generated counts describe omni-v21. Resolve by regenerating from the actual engine identity; do not manually relabel a stale derivation.

## Formal convergence obligations
- State the exact implemented discrete-time map and its operating domain before claiming convergence.
- Distinguish the continuous-time U-channel Lyapunov result from the sampled-data RK4 bound and from the full forced six-state dynamics.
- Prove discrete forward invariance over the declared parameter box with a rigorous bound (for example validated interval arithmetic), or retain status OPEN.
- Quantify measurement delay, stale observations, saturation, external-controller interaction, and actuator failure assumptions.
- Keep numerical counterexamples and negative controls; a finite sample is not a universal proof.

## Three-arm comparisons
A = native alone; B = Omni on native; C = Omni direct. Evaluate B/A and C/A **separately**. Preserve the native and Omni raw values, direction of benefit for each gauge, signed difference, units, uncertainty, repetitions, and actual engine commit. Never count an orchestrator-overhead comparison as an Omni-on-native loss.

Report *exact equality* separately from a small effect below a practical tolerance, and separately from an inconclusive interval. The current 0.5% EVEN floor is a practical tolerance, **not mathematical equality**. Do not change published historical verdicts without regenerating the reports from frozen raw data and documenting the policy change.

## Defensive acceptance
- A forbidden or unverified write must remain watch-only; a rejected actuation must not be counted as a realized performance gain.
- Verify rollback and restoration under abrupt termination, stale readings, competing controller writes, and failed actuator commands.
- A hardware probe returning unavailable is a skip **only for its documented exit status**. Unexpected probe failures and unittest failures must propagate to CI.
- Physical energy, power, and thermal claims require independent eligible meters and identified hardware, not virtual-host estimates.

## Evidence classes
Use docs/EVIDENCE_LEDGER.md: T theorem under assumptions; V finite verification; S model/simulation; L external software observation; P independent physical measurement; O open. A claim cannot inherit a stronger class from another test.

## Current known gaps at time of writing
- Current-engine benchmark coverage reported as 5 of 26 families (omni-v21).
- The LOSS ledger reports 327 historical adverse gauge rows, including 156 Omni-on-native, 27 controller-replacement, and 144 other. Revalidate each against its own engine and arm before closing it.
- The current appraisal reports 165,143 raw files matched against stored checksums. This is an **internal report**, not a fresh independent hash traversal by this audit.
- No full verification run on the latest commit, physical CPU measurement, or independent penetration test is asserted here.

## Graduation gates
1. Source/claim traceability and a clean exact-head verify receipt.
2. Cross-language parity plus mutation and negative controls.
3. Formal claims reconciled with the exact sampled implementation.
4. All 26 benchmark families rerun on the current engine, or explicitly labeled historical.
5. Separate A/B/C results with adverse metrics retained.
6. Physical claims supported by measured eligible hardware.
7. Outside replication before describing the whole system as independently validated.

---

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
