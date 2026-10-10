# Omni v4, designed and not built: the brain's verdict on every muscle, inside the engine

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.

Written 2026-10-09 at the founder's order of that evening, and left here for the founder's word. Nothing in this page is
built in the engine; the engine stays Omni v3 (`OMNI_V3.json`). The standing order is that any change to a rule, gain, guard,
preset or muscle makes the next version, every result is run again on it, and the engine is never changed without the founder
being told first. This page is the telling.

## The order

Omni-Compass need not be wired into every muscle. Where it cannot beat the native controller on the muscle's own gauges,
the muscle lives by itself and Omni only reads it: one wire out, no wire in. The brain must decide that itself, on the
muscle, in real time, by a measurement, knob by knob, not as one turn of a single dial for the whole system; and where a
muscle would read worse, the brain must either offset it within that muscle so the whole organism comes out ahead, or leave
the muscle native. "If it cannot, it shall not be."

## What already does this, and where it stops

- **The engine's verdict** (`omnicompass/verdict.py`): a paired trial on the muscle itself before a slow knob is moved, "left
  native" where no step passes. In v3 it guards the Kubernetes controller's machines, the robot arms' speed override and the
  drones' cruise. It does not guard every muscle.
- **The five live harnesses** (since 9 October, `tools/knob_verdict.py`): the same verdict around every live knob of the
  database, messaging and cache stacks, with the declared objective, outside the engine. Built, declared, and dispatched on
  10 October 2026 (`docs/RERUN_2026-10-10.md`).
- **The modelled realms** (`realms/harness.py`, in the engine): one governor reads the organism's aggregate and its one
  directive sets every muscle's knob (`docs/REALMS_PREREGISTRATION.md`, the arms). Each muscle obeys the shipped nervous
  system and its own cover, but no muscle is tried before it is moved. That is where the 13 trade muscles of the realms table
  come from: energy saved at a cost in service, or service bought with energy, on a muscle whose knob was moved on the
  organism's say-so, not its own.

## What v4 changes (engine files, so a new fingerprint)

1. **A verdict per muscle in the governor** (`omnicompass/adapter.py`, the muscle wiring in `omni_controller/muscles.py`):
   every knob the governor holds gets its own `Verdict`, in both directions from native, with the muscle's own cost per piece
   of work under the muscle's declared objective. The directive from the law still says which way and how hard; the
   allowance says how far, and a knob with no allowance is watch.
2. **The realms harness runs that verdict per muscle** (`realms/harness.py`): the omni arm starts every knob at native, trials
   each knob on its plant's own cost (energy per unit of work, the guardrails as the abandonment condition), and writes only
   inside the allowance. The organism result is then the sum of the knobs that earned their wire in. The watch arm, the kill
   at 90% and the hand-back stay as they are.
3. **The muscle's objective is declared in the catalog** (`realms/catalog.csv`, one column): resource by default; service
   where an operator would declare it. No gain or guard of the law changes.
4. **The fingerprint**: an `OMNI_V4.json` at the root, read by `tools/omni_version.py`, and a v4 record beside `docs/OMNI_V3.md` listing every result read on it (neither exists yet).

## What is expected

The 124 superior muscles keep their wire in; the 13 trades read as watch (the trial refuses them); the 807 noninferior
muscles stay watch, 746 of them never writing as now; no muscle reads WORSE, by construction. The organisms' work per energy
is expected unchanged or slightly lower (the trades no longer contribute their energy saving), with time in violation no
higher than native's everywhere. The six Kubernetes tests, the simulators and the live stacks are not expected to move, the
verdict being already on those knobs or outside the engine.

## What it costs, and how long

| Rerun on v4 | Runs | Where | Money | Time |
|---|---:|---|---|---|
| The 945 muscles and the organisms, A/B/C | 3 | GitHub | none | about a day |
| The seven Kubernetes tests, A/B/C | 21 | GitHub | none | one to two days, in parallel |
| The four simulators, A/B/C | 12 | GitHub | none | one day |
| The five live stacks, A/B/C | 15 | GitHub | none | one day |
| The six organisms with the cluster inside at 10 and 100 copies | 1 | GitHub | none | a day |
| The two big organisms at 1,000 copies | 2 | Azure, one rented machine each, about 25 hours | about two days of one machine each at the eastus `Standard_D8as_v4` rate | two days, in parallel |

About a week of runs in all, most of it waiting. Every v3 table stays a v3 result in `docs/history`; the index and the wiring
page are read again from the v4 tables.

## What the founder decides

One word, "v4", and it is built in the order above, fingerprinted, and every result run again on it. Until then the engine
stays Omni v3, the live harnesses carry the verdict outside it, and this page is the design.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
