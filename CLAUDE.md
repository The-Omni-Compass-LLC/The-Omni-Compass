# CLAUDE.md: standing orders for any session working on this repository

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

These are the founder's orders, gathered from the full working record. They load every session. Follow them unless
the founder overrides one in the conversation.

## What Omni is

- Omni-Compass is a **supervisory governor**. It always sits **on top of a native controller**: the Kubernetes HPA,
  GPU firmware, cooling, batteries, a grid's tap changer, a robot's servo, and so on. It is never standalone and never a
  competitor to native.
- Every benchmark has exactly two arms, **native** and **omni** (omni means Omni on top of native). There is no other
  arm and no other name.
- **Do no harm.** Omni must never cause a LOSS against native. Where it can't bring a knob a GAIN,
  that knob stays native. The 2%
  verdict (`omnicompass/verdict.py`) is the engine's trigger, not a stamp on a report. Gains are uncapped.
- Headline: more work, faster, on fewer machines, with less energy. One combined number: the Omni index.
- **The max is the default brain** (12 October): every muscle runs at its own limit, never past it and never below
  native; it rides the edge, not the middle. "We're never looking to shave energy": the energy it takes is **power
  given**, shown beside the work, the speed and the wear it bought, never called a loss; the max never takes from one
  muscle to give to another. Results are judged on work, speed, misses and failures. Anyone can tune it down from the
  max (the dial: the tune-down, `V5SAVE`). A knob native already runs at the top of its range is "at its limit on native".
- The word is **compass**, never "bowl". The law is `omnicompass/compass_law.py` (`CompassLaw`): a band with 5%
  cushions, two antagonist forces, smooth (tanh), not hammering.
- Wiring is a two-way plug, one wire in and one wire out. The brain does the math. The knob is restored to the snapshot
  taken once, at the start.
- **One pedal, no brake** (12 October), like an electric car: push for more, lift off for less; lifting hands the
  setting back toward native; idle is the pedal lifted all the way; reset hands everything back to native; cruise (a
  known queue waiting), autopilot / watching / off. After a crash the plug walks every setting back to native gradually
  (the lease); the **kill switch** is separate, for security only, and instant (`omnicompass/master.py`,
  `tools/omni_switch.py`). The word "brake" is not used.
- Scaling: floor of 2 machines, no ceiling, every machine usable. Traffic tests step by one (1 2 3 2 3 4 …).
- Nothing is hardwired. Anything that doesn't work is removed, not just switched off.

## The engine: Omni v5 at the max (v3, v2 and v1 kept for their results)

- `OMNI_V5.json` and `docs/OMNI_V5.md`: the max (`realms/compass_arm_v5.py`, `V5CFG`) on the 1,107-muscle catalog, the
  bone inside every organism with the living body's immune system (V6-V13, `docs/FORMAL_V5.md` section 4: native twins
  of every room, the heat debt, batteries timed for their lines, nothing locked), every muscle its own card
  (`realms/muscle_cards_v5.csv`, 364 muscles, found by `tools/tune_cards.py` on development seeds only and kept only when
  it wins twice and never falls behind native on any seed; inside a body a battery wired by its power keeps the body's
  margins, V14; `docs/FORMAL_V5.md` section 5), the lease's walk back, the tune-down on the dial. v5 is re-declared on
  every engine change while in development. `OMNI_V3.json` (`docs/OMNI_V3.md`), `OMNI_V2.json` and `OMNI_V1.json` stay for their results,
  never up front. Check with `python3 tools/omni_version.py [--commit <sha>]`: it prints omni-v5, omni-v3, omni-v2,
  omni-v1, or what differs.
- The version numbers are bookkeeping so no result is read across engines. When the founder says the engine is final, the
  engine that stands then is published as **Omni-Compass 1.0**; the older fingerprints go to `docs/history` as the road to
  1.0, never as a second product.
- Any change to a rule, gain, guard, preset or muscle makes **the next version**, and every result is run again on it. Never read a result across
  versions. Never change the engine without telling the founder first.
- Three runs: each benchmark runs as A, B and C (`tools/confirm_abc.py`). Every judged row gets one of three
  readings: GAIN or LOSS in all three of our runs (the same sign in all three, every 95% interval clear of zero, the word
  set by the gauge's aim; a resource spent that rose is power given); EVEN, no difference beyond the noise (an interval includes zero: that is the result, say so); the runs disagree (clear runs
  pointing different ways: the test is unstable there, look into it). Never write "confirmed" or "not confirmed"
  (the founder's order of 11 October: nobody outside approved these results); every three-run table says "Run and
  scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."
  (`tools/readings.py`).
- Evidence classes: P (physical meter), L (live software), S (our own models). Never present S as proof.

## The six organisms and the grid

- Omni v5 (12 Oct, night): four realms (Compute/AI/Cloud 540, Physics/Robotics/Autonomous 404, Energy/Facility/Industrial
  480, Distribution/Specialized 484), the whole tower (1,107 distinct muscles in 70 families, the founder's nine open-source
  pieces among them: Kepler, Climatik, EAR, CruiseKube, Goldilocks, the Kubernetes Power Manager, PEAKS, Adaptive GPU
  Power Capping, NVIDIA's platform power manager), and the four stacked (1,908). They share a spine of 267 muscles; the
  1,097-muscle catalog of earlier the same day keeps its results. v2/v3 were 430/376/470/440, 945 and 1,716; v1 was 345/262/282/337, 656 and 1,226
  with a spine of 190; their results stay theirs.
- The organisms are named `tower` and `stack` in code and workflows (never by a count); the old names `organism_656` and
  `stack_1226` are read as aliases.
- The grid: each organism runs native and omni at 1, 10 and 100 clustered copies (one organism, ten of the same
  organism, a hundred) × 1, 10 and 100 runs: 54 squares, modelled and with the real cluster inside, with both values shown
  in every square. **1, 10 and 100 only** (the founder's order of 12 October, to cut the time and the bill): no 1,000
  copies and no 1,000 runs anywhere; the whole grid runs on GitHub's own machines and nothing is rented for it. Every grid
  button starts all three sizes × all three run counts and uses every runner GitHub gives. The conductor
  (`scripts/dispatch_grid.py`, `grid.yml` every 15 minutes; the six and six-kube buttons with their defaults) starts every
  run not yet started, reads started runs back from their names, never starts one twice, and keeps the queue at what
  GitHub runs plus a margin; it starts nothing while an Azure run, a grid report or a verify waits for a runner (Azure
  first). It also releases the reruns of every benchmark on the engine that stands (`scripts/reruns.txt`; A of
  every benchmark, then B, then C; a few a tick; read back by count, never started twice). Shards are cut from measured run times; each stops at its deadline and hands in every run it finished. With
  the cluster inside only runs of protocol 3 count (12 Oct: the governor never below the organism's CPU priority, its
  decisions counted inside the window; 13 Oct: the model of the organism on the runner's last core and the kind nodes on
  the others, the same in both arms); a repetition whose job fails runs again, up to three times, paired within one run,
  and one that fails three times is listed. With the cluster inside, the window is set from the heavier arm's step,
  timed before either arm, so the max keeps the organism's clock.
- Three loads: each organism's own load, the climb (the load stepping by one, 1 2 3 2 3 4 …) and work waiting in line
  (`LINE`, `realms/harness.py`); every muscle alone runs its own load and the line.
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

- At the top and end of every output: © 2026 The Omni-Compass LLC; all rights reserved; evaluation and simulation use
  only; any commercialization or monetization requires a signed, paid Omni-Compass Enterprise License; then **all**
  patents, copyrights and trademarks filed in the USA (say "filed", never give numbers), followed by www.omni-compass.com
  and nothing after it (the founder's wording of 10 October: the word "all" before patents and "all rights reserved"
  everywhere; that night he struck two earlier sentences from the notice, and they stand nowhere: no page, header, report,
  license paper or program output carries them, and `tools/legal.py --check` fails any file that does).
- Every export of any part of Omni-Compass (a zip, a report, a table, a PDF, a chat answer) carries the README's notice,
  the LICENSE, the NOTICE and DISCLOSURES.md the same way, written as a multi-billion-dollar company would protect a
  released asset.
- Keep the SPDX headers so Black Duck, FOSSA and Snyk detect the license.
- The notice is written once, in `tools/legal.py`; `python3 tools/legal.py --fix` puts it on every page, header, workflow
  report and export, and `--check` (run by `verify.py`) fails any push where a file lacks it. Engine files locked by a
  fingerprint take the new header only with the next engine version.

## Orders of 14 October

- **The manual carries no illustrations and no blank pages.** None of the founder's plates (his illustration images) go
  in the manual: no cover art, no title-page rose, no plates, no List of Plates; no charts either. Every chapter starts on
  the next page; a part's heading sits at the top of a page with its first chapter under it. The contents and page numbers
  are rebuilt from the book itself (`docs/book/build_book.py`). The plates stay in `docs/book/plates/` as his property.
- **Every fix realigns everything, on every push.** When code changes or a bug is fixed, everything that describes it is
  brought up to it in the same push: the manual and its PDF, the README, the index, the tables, the plans and the
  standing pages. Then the newest-engine material is scanned top to bottom for the retired words and the old ways
  (better/worse, brake, bowl, "confirmed", "simulation" for our own models, standalone or competitor arms, 1,000 copies,
  power given called a loss) and anything found is fixed before the push. Old material stays where it is.
- **The factory tune** is declared and disclosed (`DISCLOSURES.md`, section 3; the README; the manual's notice): the engine
  is presented as the owner tuned it and ships it, self-running, set at the factory; every muscle wired on its own setting
  (its card, or the engine's setting); no setting universal; any licensee may then add on, retune, upgrade or tune down
  any muscle, and a changed tune's results are its own.
- **The wiring disclaimer in bold capitals** (`DISCLOSURES.md`, section 4; the README; the manual's notice; `llms.txt`):
  the published benchmarks are the record of what Omni-Compass did on the systems, loads and engine they name; where a
  result elsewhere differs, the first presumption is the wiring, the settings, or how Omni-Compass was implemented or read.
- **The notice travels with every output.** No code can force an outside AI to print it, so it is placed in everything
  they read: the top and end of every file, every program output, `llms.txt` (for AI crawlers), `AGENTS.md`, `GEMINI.md`,
  `.github/copilot-instructions.md` and `.cursorrules`, each ordering the notice on every answer of any length; the
  license makes a copy without it a breach. Those instructions point to the notice at the top and end of their own file
  (a second copy near the top is stripped by `tools/legal.py`).
- **The founder hears where things stand** in every report: what is running, what landed, what reads GAIN, EVEN or LOSS,
  and what is still on an older engine, in plain words.
- **The founder's prompt rules** (his document "A.I. prompt rules"), as they apply here:
  - Type: all text (body, tables, lists, code) at **11 pt or larger** on a line height of at least **1.5**; only running
    heads, footers and page labels may be smaller, at 8 pt; headings scale up from the body.
  - Language (the founder's correction of 14 October): not a 10th-grade level. The manual is written at referee level, for
    CTOs, principal engineers, physicists and mathematicians who will wire Omni-Compass onto a whole company's stack: the
    exact terms of control engineering, software engineering, physics and mathematics, used precisely and defined where
    they first appear, so that no reader can mistake what is stated, what is measured or how to wire it. Formulas are
    written in LaTeX (`$...$`, `$$...$$`) in the markdown.
  - Before a document is finished, audit it like a referee: equation and theorem numbers, cross-references, undefined
    symbols, repeated claims, and every claim backed by the text. No padding: every addition must earn its place.
  - In chat: no greetings, no echoing the request, no sign-offs; no follow-up questions (decide and do it); do what can be
    done without listing what can't. This never hides a result: every row, LOSS included, is still reported (Honesty).

## Orders of 13 October

- **GAIN, EVEN, LOSS** (the founder's order of 13 October, evening: "better, same and worse are going to be gain, even and
  loss, wherever and ever, all over where it lives, where it used to live"). Every judged reading, in every table, page,
  report, program output and the manual, is GAIN, EVEN or LOSS, decided by what the gauge is for and never by the sign of
  its number: time waited, missed or failed, a fall is GAIN; work done, a rise is GAIN; a resource spent or held, a fall
  is a cut, a GAIN, and a rise is **power given**, never a loss. Better/worse, lower/higher-as-a-verdict and toward/away
  are not used. The key (G.A.I.N. Growth, Advantage, Improvement, Net-positive; E.V.E.N. Equalized, Verified baseline,
  Equilibrium, Neutral; L.O.S.S. Leakage, Off-track, Setback, Subpar), disclosed and disclaimed, is written once in
  `tools/readings.py` and stands at the top of the README, `docs/HOW_TO_READ_THE_RESULTS.md` and the manual's front matter
  (`python3 tools/readings.py --fix`; `--check` fails a page whose key differs). "Theoretically I should never see the word
  loss": a LOSS row is never cut; its cause is found and fixed and the test rerun. `python3 tools/summary.py` prints the whole
  summary straight after a pull. Raw machine records (JSON receipts, raw run folders) keep their recorded field values;
  every page that shows them uses the words. Next: the words become the code that tells Omni how to move (the next engine).
- Every muscle runs from 1 up to one click under its own capacity, read live from the system, never a number written in
  code: never below 1 (a pool's machines never below 2), no ceiling where the system can keep adding, and back down again;
  guardrailed so no muscle overworks and hurts the organism, and the organism never hurts a muscle. Where the brain's own
  math shares the machine, it counts in the body's load. Encoded in the live controllers as Omni v5 amendment 5 (digest
  `6093b2b8`, `docs/OMNI_V5.md`): machines, replicas, the power cap, the GPU's clock floor and heat line, batch.
- Omni's brain works for the organism, never for Omni: it decides what to push and pull so the whole system is the best it
  can be, collectively, one body.
- Never decide a benchmark's settings ourselves: the written ones stand (the Azure burst steps are `1 3 1 4 1 3`, 5
  October). When a result comes in negative, find the cause and fix it at once, unasked; a test machine's limit is never
  reported as Omni's result.

- **Everything on the newest engine** (13 October, night): every benchmark runs again on the engine that stands, and its
  result carries that engine's name. Nothing is shown or compared as "v3" once v5 stands: a v3 table is the road, in
  `docs/history`, never a setting to go back to by name. More versions will follow (perhaps to v10); each one reruns
  everything. Where a change made a result worse, the fix is made inside the newest engine and rerun.
- **One cloud first** (13 October, night): Kubernetes on Azure is finished first; Google (GKE), Amazon (EKS) and the GPU
  chips (Lambda) are not run until the founder says the Azure Kubernetes results are where he needs them.
- **The company's telephone** (13 October, night; wording of 14 October): "main office infrastructure, toll-free direct
  1-888-339-9551, system route asset 1-888-DEX-YLL-1", on every contact line where the company is named for reaching it
  (README, LICENSE and its copy, NOTICE, Enterprise License, Trademarks, Licensing FAQ, Security, Support, the manual's
  "Who to call", codemeta), always before the website, never inside the legal notice, which ends with
  www.omni-compass.com. The letters, read in order, are the company's own reading of how the engine runs (README "Contact",
  the manual's "Who to call"): DEX, Data Exchange (the input, the two-way plug); YLL, Yield Limit Line (the boundary, every
  muscle to its own limit and never past it, as a material is loaded to its yield limit and springs back unharmed); 1, one
  closed loop (the output; in code 1 is true, in science 1 is unity; one body, one brain). The founder's order of 14
  October: write it as the meaning, the way science and software people read it, wherever it fits in the manual; "years
  of life lost" is written nowhere. The founder's
  personal number is never written anywhere.
- **A copy he can keep**: the manual's PDF and the whole repository as a downloadable zip, in parts, from a pushed commit,
  sent to the founder after each landed change.

## Orders of 10 October (afternoon)

- The reflex rule is the whole mechanism: a trial runs to its full measurement and is never ended by the calm it causes;
  the brain never forces, it reacts to what the system shows; one body, one brain, the body's cost judged, nothing anywhere
  pushed to a LOSS to move one thing to a GAIN; one trial at a time inside a body; nothing permanent; the wall
  belongs to the body.
  Written into the engine as **Omni v4** (`docs/OMNI_V4_PLAN.md`), every wire forced through it, every result rerun.
- Everything is wired. Staying native is the brain's live decision every second, never a verdict from one run.
- **Six organisms**, never five: the four realms, all realms stacked (1,716), the whole catalog once (945). The live
  software products are never counted beside them. Realms are re-cut by a written rule at v4; new muscles raise the count.
- The word "simulation" is not used for our own models in reports: they are "modelled" (class S); live software is "the
  real thing" (class L); a meter is class P. The license's own phrase stays as written.
- The newest result is always at the front; the repository keeps itself current (the archive bot and the front page);
  old material goes to `docs/history`.
- The manual is a printed book: front matter, body, back matter, the wiring instructions for the people who implement it,
  the theory of the mechanism; rebuilt as a PDF whenever it changes.
- The founder hears what a result says before it goes up.

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

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
