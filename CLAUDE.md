# CLAUDE.md: standing orders for any session working on this repository

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE`.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

These are the founder's orders, gathered from the full working record. They load every session. Follow them unless
the founder overrides one in the conversation.

## What Omni is

- Omni-Compass is a **supervisory governor**. It always sits **on top of a native controller**: the Kubernetes HPA,
  GPU firmware, cooling, batteries, a grid's tap changer, a robot's servo, and so on. It is never standalone and never a
  competitor to native.
- Every benchmark has exactly two arms, **native** and **omni** (omni means Omni on top of native). There is no other
  arm and no other name.
- **Do no harm.** Omni must never make anything worse. Where it can't improve a knob, that knob stays native. The 2%
  verdict (`omnicompass/verdict.py`) is the engine's trigger, not a stamp on a report. Gains are uncapped.
- Headline: more work, faster, on fewer machines, with less energy. One combined number: the Omni index.
- The word is **compass**, never "bowl". The law is `omnicompass/compass_law.py` (`CompassLaw`): a band with 5%
  cushions, pushed to the middle by two antagonist forces, smooth (tanh), not hammering.
- Wiring is a two-way plug, one wire in and one wire out. The brain does the math. The knob is restored to the snapshot
  taken once, at the start.
- Pedals and modes: idle (no gas, no brake), gas (ramp up), brake (ramp down to idle), reset (brake to the floor:
  everything back to native), cruise (a known queue waiting), autopilot / watching / off. The **kill switch** is
  separate, for security only (`omnicompass/master.py`, `tools/omni_switch.py`).
- Scaling: floor of 2 machines, no ceiling, every machine usable. Traffic tests step by one (1 2 3 2 3 4 …).
- Nothing is hardwired. Anything that doesn't work is removed, not just switched off.

## The engine is frozen: Omni v3 (v2 and v1 kept for their results)

- `OMNI_V3.json` and `docs/OMNI_V3.md` (v3 = v2 plus the slack gate on speed knobs and the marine preset); `OMNI_V2.json`
  (v2 = v1's law, controllers and runners byte for byte, plus the 945-muscle catalog and its thirteen new presets) and
  `OMNI_V1.json` stay for their results. Check with `python3 tools/omni_version.py [--commit <sha>]`: it prints omni-v3,
  omni-v2, omni-v1, or what differs.
- The version numbers are bookkeeping so no result is read across engines. When the founder says the engine is final, the
  engine that stands then is published as **Omni-Compass 1.0**; the older fingerprints go to `docs/history` as the road to
  1.0, never as a second product.
- Any change to a rule, gain, guard, preset or muscle makes **the next version**, and every result is run again on it. Never read a result across
  versions. Never change the engine without telling the founder first.
- Confirmation: each benchmark runs as A, B and C (`tools/confirm_abc.py`). Every judged row gets one of three
  readings: confirmed better or confirmed worse (the same sign in all three, every 95% interval clear of zero); no
  difference beyond the noise (an interval includes zero: that is the result, say so); the runs disagree (clear runs
  pointing different ways: the test is unstable there, look into it). Never write "not confirmed".
- Evidence classes: P (physical meter), L (live software), S (our own models). Never present S as proof.

## The six organisms and the grid

- Omni v2 (6 Oct): four realms (Compute/AI/Cloud 430, Physics/Robotics/Autonomous 376, Energy/Facility/Industrial 470,
  Distribution/Specialized 440), the whole tower (945 distinct muscles in 59 families), and the four stacked (1,716). They share
  a spine of 257 muscles. v1 was 345/262/282/337, 656 and 1,226 with a spine of 190; its results stay v1 results.
- The organisms are named `tower` and `stack` in code and workflows (never by a count); the old names `organism_656` and
  `stack_1226` are read as aliases.
- Each organism runs native and omni at 1, 10, 100 and 1,000 copies × 1, 10, 100 and 1,000 runs: 96 squares, with both
  values shown in every square. 1,000 is the maximum.
- Benchmark breadth: every domain that can be benchmarked defensibly (`docs/REGISTER.md`), with Omni on top of that
  domain's own native controller, one or two at a time.
- GPU: all old GPU results are obsolete. The founder reruns them on Lambda. Never spend GPU money before the CPU side
  is done, and give the founder one exact commit.

## Honesty

- Report every row, losses included. Never drop a row because it went against Omni. If Omni loses, first suspect our
  own wiring, native setup or scoring; fix that, then rerun. The founder may choose not to publish a benchmark; it is
  never published with rows cut out.
- Preregister before running, freeze the rules on one tuning case, and test on untouched cases.
- "Flake" is not a root cause.

## Legal, on every output

- At the top and end of every output: © 2026 The Omni-Compass LLC; evaluation and simulation use only; any
  commercialization or monetization requires a signed, paid Omni-Compass Enterprise License; patents, copyrights and
  trademarks filed in the USA (say "filed", never give numbers); nothing is set in stone.
- Keep the SPDX headers so Black Duck, FOSSA and Snyk detect the license.

## Repository

- Referee and underwriter level. Only finals up front; old material goes to `docs/history` / `archive/` or is removed.
  One version is always the main one; `main` and the working branch stay in sync.
- Verify before every push: `tools/release_manifest.py` under Python 3.12 (as GitHub runs it), 0 FAIL. Clear
  `/tmp/tmp*` first, because test leftovers fill the disk. Keep the Python 3.12 environment outside `/tmp` (for example
  `/root/v312`), because a container reset wipes `/tmp`. After a push, check the GitHub verify run itself, not only the
  local one.
- The manual (`docs/`, about 200+ pages, rebuilt as a PDF) explains the physics, philosophy, wiring and how to read every
  metric, and holds the muscle catalog and the register.
- Zips on request: split into parts under the upload limit, each part openable on its own, built from a pushed commit.
- Never put a model identifier in a commit, PR or file.

## Talking to the founder

- The founder is not an engineer. Use plain language: yes/no plus a number. When asked a question, answer it before
  doing any work.
- Say what each step costs and how long it takes. Give Lambda and Azure steps click by click (the founder types on a
  laptop and chats on a phone).
- Credentials go only into GitHub secrets. Never ask for them, never echo them back.
- Latest standing order (Oct 5): push everything on the newest engine, run it again and double-check it, keep the old
  runs going, don't ask questions, and work to the highest referee and underwriter level.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass Enterprise License. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone.
