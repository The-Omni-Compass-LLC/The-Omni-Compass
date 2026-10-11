# Omni v5 — the engine fingerprint

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**omni-v5** is a distinct engine, its own tree, no longer read as v3. It is fingerprinted file by file in `OMNI_V5.json`
(`tools/omni_version.py`); `python3 tools/omni_version.py` prints `omni-v5` on this checkout. v1, v2 and v3 stay frozen,
each kept for its own results; no result is ever read across versions.

## What v5 is

v5 is **a combination of everything**: it takes v3's proven engine (its live controllers, its realms and organisms, its
runners) and adds the **v5 compass law** (`realms/compass_arm_v5.py`) and its arm in the harness (`realms/harness.py`). The
goal is to be equal to or better than native and every prior version on every measure, and never worse on any — *do no
harm*.

The v5 muscle catalog (`realms/catalog_v5.csv`) is **1,002 muscles in 65 families** — v3's 945 plus six new families of
real control points: **Linux Kernel & OS Control** (cgroups, the CFS scheduler, DVFS/cpufreq, transparent hugepages, the
I/O scheduler, NUMA balancing, dirty-ratio writeback, swappiness, TCP buffers, …), **Serverless & Functions (FaaS)**,
**Virtualization & Hypervisor**, **Content Delivery & Edge Cache**, **Gut** (data-plane intake and waste), and **Skin**
(perimeter and admission). Each is a distinct real-world knob, modelled on the matching plant template, exactly as v3's
945 already share five templates. (v3's own catalog `realms/catalog.csv` stays 945, frozen for v3's results.)

Two math-only guardrails, and otherwise free arms:

- **The edge** — a per-knob cushion that widens at once when service climbs and narrows slowly when it falls
  (`cushion = climb × reaction + z × wobble`), so nothing riding its own limit falls off.
- **The centre / the hole** — a machine is handed back only when what is left covers the recent peak, and a cooled zone is
  eased only by the degrees its cooling can still recover, so nothing drops into a pit it cannot climb out of.

Every other knob is free to move both ways inside its physical cover, and **a knob stays native wherever the law cannot
improve it without harm.** In the no-harm default (`V5CFG`) the power cap, the battery peak-shave and a generation
setpoint stay native — each trades service or output for energy, so each belongs to a **Max / service dial**, not the
"nothing worse" default. The energy saving of a power cap is proven on the **metered GPU** (class P), never on the model.

## The no-harm proof (modelled, class S)

On a fixed seed, for **every** muscle in the catalog, the v5 default uses no more energy than native, does no less work,
and is in violation no more often; it hands every knob back to native on the kill (the dead-man lease); and it acts where
it helps. The whole tower is no worse than native on energy and work. This is checked in
`tests/test_compass_arm_v5.py` and run in full by `tools/run_realms_v5.py` (`results/realms_v5/`). Models are class S: a
model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test.

## In development

While v5 is in active development its fingerprint is **re-declared on each engine change** (`python3 tools/omni_version.py
--write v5`), and **no v5 result is published** until the v5 freeze. At the freeze, every benchmark is rerun on v5, A/B/C,
the founder hears each result before it goes up, and the fingerprint is final.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
