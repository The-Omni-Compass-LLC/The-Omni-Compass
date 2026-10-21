# Omni v14: a knob for every muscle (the engine that stands since 20 October)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v14 has been the engine on main since 20 October, night. The founder's order behind it, of the same evening: knobs on
every monitor, "to turn off and on such a mechanism, a muscle, or tweak and turn any muscle". omni-v13 (`docs/OMNI_V13.md`)
took its mode and its dial for the whole governor; nothing in it could leave one muscle where native runs it while the others
ran. omni-v14 adds that and nothing else: every setting, gain, guard, preset and rule is omni-v13's.

Its fingerprint is `OMNI_V14.json` (digest DIGEST, 47 files). Forty-five files are omni-v13's bytes; two differ, the
Kubernetes governor (`omni_controller/controller.py`) and its muscles (`omni_controller/muscles.py`). With nothing left native
the governor is omni-v13's, write for write; the toy gate reads it so (`results/toy_gate/V14_VS_V13.md`). Every benchmark runs
again on omni-v14, A, B and C. Every earlier table stands as its own engine's result until its three runs on v14 land, and
results from two versions are never pooled. The readings from the toy gate are our own models (evidence class S), never a
benchmark result. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. The knob

`--native MUSCLE[,MUSCLE...]` (or `OMNI_NATIVE`) names the muscles the governor leaves native. A muscle named there is never
written: it stays where native runs it, and every other muscle runs as before. The governor still reads the whole body and
decides with all of it in view; only the write of a muscle left native is withheld, and the audit says so (`"held"`, and
`"native_muscles"` at the start). A name that is not a muscle is refused at the start, never ignored, so a misspelling can
never leave a muscle driven that the operator meant to leave native.

| Muscle | What is left native |
|---|---|
| `machines` | the node pool's size (the operator's node-scale command) |
| `replicas` | the pod autoscaler's target, the pod reflex's replica floor and the replica cap |
| `cpu` | the serving pods' CPU limits (the conveyance and the pod power cap) |
| `clock` | the processors' frequency ceiling |
| `gpu` | the GPU's power limit |
| `rollout` | the rollout guard (pause and undo) |
| `batch` | the batch admission and pacing |
| `rightsize`, `coldstart`, `contain`, `cooling` | the pods' rightsizing, the cold-start reserve, the namespaces' containment, the cooling setpoint |

## 2. The button

The control panel (`tools/omni_control.py`) carries it as one more button, `POST /v1/muscle {"muscle": NAME, "on": true|false}`,
role operator, every press audited with its holder and reason, and as a row of On and Native buttons on the console. Like a
dial press it passes through native: the governor's own kill file is set, its exit awaited (every setting it wrote restored
and read back), and it starts again with the new list. Nothing is changed under a running governor. The monitor wall
(`docs/MONITOR_WALL.md`) points every row at these buttons; the wall itself never presses one.

## 3. The toy gate against omni-v13

GATE

## 4. What stays omni-v13's

Every other engine file; every rule, gain and guard, the conveyance's hand-back of omni-v13 among them; the verdict byte for
byte. The next version's list (`docs/CHANGE_CONTROL.md`) carries what is still to fix. The GPU governors
(`omni_controller/gpu_governor.py`, `gpu_compass.py`) keep their own two levers, the power limit and the clock, and take the
per-muscle knob with the version that next changes them.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
