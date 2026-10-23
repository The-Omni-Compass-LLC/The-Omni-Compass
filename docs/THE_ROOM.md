# The room: every muscle's band, native's point in it, and what Omni-Compass may take

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's law of 23 October 2026, in his words: "if a muscle doesn't gain any benefit with OmniCompass in it and in
actuality has negative when everything else is a benefit, then that simply means that muscle is at its fullest limit";
native "just means not doing anything on there, and there can be no reason that anything native can be better than the
mathematics and physics of OmniCompass in it, unless it is because the muscle itself has its own limitations". This page
writes that law as the theory and the mathematics the engine is held to, names what the catalog already reads by it, and
sets the order of the work it calls for: the theory first, then the tuning, then the muscles Omni-Compass builds itself.
Words and mathematics only; no code changes here. Run and scored by The Omni-Compass LLC's own code. No outside party has
reviewed or approved these results.

## 1. The band, native's point, the room

A muscle is one setting on one machine that already has its own control (`docs/MUSCLE_CATALOG.md`). Its lever moves in a
band, the **cover**, from lo to hi: the device's or the buyer's lowest and highest setting, outside which nothing is written
(`omnicompass/compass_law.py`, `Plug`). Native holds the lever at one point in it, xₙ, by its own rule.

  the room upward    rᵤ = hi − xₙ
  the room downward  r_d = xₙ − lo
  the room           r = rᵤ + r_d, and r = 0 exactly when the band is one point

Omni-Compass acts on the lever only inside the cover, so every write x satisfies lo ≤ x ≤ hi, and every change it can make
is bounded by the room: |x − xₙ| ≤ max(rᵤ, r_d).

## 2. What the room is worth

Let g be the organism's gauge the muscle moves (work done, time waited, energy spent), read against native as the key
reads it (`tools/readings.py`): a rise in work is GAIN, a fall in waiting is GAIN, a fall in a resource spent is a cut and a
rise is power given. Let g(x) be the gauge at lever x with everything else the same. The **worth of the room** is the most
the gauge can move inside the cover:

  Wᵤ = sup { g(x) − g(xₙ) : xₙ ≤ x ≤ hi },  W_d = sup { g(x) − g(xₙ) : lo ≤ x ≤ xₙ }

in the gauge's own direction of aim. Two statements follow from the definitions alone:

1. **The gain on a muscle is bounded by the worth of its room.** Whatever law Omni-Compass runs, its reading on that gauge
   satisfies Δg ≤ max(Wᵤ, W_d). A muscle with r = 0 has W = 0 and can only read EVEN. The catalog's own word for it is
   **at its limit on native**: native already runs the knob at the top of its range, Omni-Compass reads it and leaves it.
2. **A LOSS on a muscle is never the muscle's.** With the lever inside the cover and the law pulling the reading toward
   the band's centre with a bounded force, the gauge can fall below native in only two ways: the lever was pushed **past**
   a limit the law was not wired to (a wall the sense never saw), or the wire reads or writes wrong (a sense that is blind
   or late, a write the device did not take, a read-back that lies). Both are the wiring's, and both are the brain's,
   nerves' and immune system's to catch, because they are wired to every muscle's limit. A LOSS is therefore always a
   fault to find in the wiring and fix in the next version (`docs/CHANGE_CONTROL.md`), never a number to live with.

## 3. The three readings a muscle can give, by this law

| reading | what it says about the room | what Omni-Compass does |
|---|---|---|
| **GAIN** | r > 0 and the law took some of its worth | holds it; the next version asks whether more of the worth is reachable |
| **EVEN, at its limit on native** | r = 0: native is at the wall of the band | reads the knob and leaves it native; nothing can be gained here by any law |
| **EVEN, the same as native** | r > 0 but the law took none of its worth | the room exists and is not taken: this is the room to reverse-engineer (section 5) |
| **LOSS** | a limit was crossed or a wire is wrong | root-caused and fixed, through the toy gate, as the next version; never carried |

## 4. What the catalog reads today, by this law

The realms result on the engine that stands (`results/realms_v5/REALMS_V5.md`, our own models, class S, every muscle
under its own load and the line), all 1,107 muscles:

| reading | muscles |
|---|---:|
| GAIN | 527 |
| EVEN, at its limit on native | 421 |
| EVEN, the same as native | 159 |
| LOSS | 0 |

So 421 muscles have no room by construction (admission knobs native already opens fully, power limits native already runs at
full, and the like: `docs/MUSCLE_CATALOG.md`, the aims), and 159 have room the engine does not yet take. The 159 are the
first work of section 5.

## 5. The order of the work this law calls for

1. **The room of every family, written.** For each of the 70 families: the band (lo, hi) and where it comes from (the
   device, the vendor's documents, the operator); native's point xₙ and the rule that puts it there; rᵤ and r_d; the gauge
   g the muscle moves; the worth Wᵤ and W_d read from the family's own model or its live receipts; and, for each wall,
   whether the wall is the **design** (a vendor's default, a published cap, a protocol's rule: movable by a muscle of our
   own) or the **physics** (a core does one thing at a time, a disk has one bandwidth, a chip has one power ceiling: not
   movable by any muscle). That table is built by a tool from the catalog and the receipts, one row a family, and it is
   what the next engine version tunes against.
2. **The 159 same-as-native muscles, one by one.** Each has room and no gain: either the law's gain on that knob is too
   small to move it inside the noise, the sense reads a gauge the knob does not move, or the trial's allowance never lets
   a step through. Each is a wiring question with an answer in the family's own files, and each answer is a change to the
   engine or to a muscle card, through the toy gate, as the next version.
3. **Omni-Compass's own muscles, where the wall is the design.** Where a family's wall is the vendor's design and not the
   physics, the muscle is rebuilt from its published mechanism with the wall as a dial and the compass law inside it
   (the orchestrator of 23 October, `docs/OMNI_ORCHESTRATOR.md`, is the first: Kubernetes' scheduler, autoscaler, node
   agent and service address rebuilt), benchmarked against the original two arms by the one key, and used in the organism
   only where it reads no LOSS and some GAIN against the original.
4. **The joined organism.** Omni-Compass's muscles, its brain over them, its governance over the collected clusters and its
   seat in the chip, run as one organism against native at every layer: the stacked run (`docs/WHOLE_SYSTEM_PREREGISTRATION.md`),
   every gauge, nothing paid for with another.

## 6. The orchestrator's LOSS of 23 October, read by this law

The showing of Omni-Compass's own orchestrator read work −11.1% and the 95th percentile +23.8% LOSS against the yardstick
while cutting machines 26.5% (`docs/OMNI_ORCHESTRATOR.md`). By section 2 that is a crossed limit or a wrong wire, and it was
a crossed limit: the muscle at its wall was the **processor core**; the room rule counted paper requests and saw room where
the core had none; two units busy at once on one core each took twice as long. The brain had no wire to that limit. With the
limit wired (a machine's room measured as the processor it can still give at full speed, the engine's own 75% rule), the
same showing read work EVEN, the 95th percentile EVEN and the machines cut 5.4%: the harm gone, the cut kept. The law held;
the wall had to be wired.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
