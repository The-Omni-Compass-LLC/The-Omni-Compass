# Omni-Compass

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**

<!-- headline: written by tools/headline.py from the result files; never edited by hand -->

## The answer first: is Omni-Compass a benefit against native?

**Yes, on omni-v18, the newest engine with its three runs in (the engine that stands, omni-v21, runs them again), measured on real machines (class L), three runs (A, B and C).** Omni-Compass on top of native did 6.0% more work than native and answered 9.5% faster at the 95th percentile; Omni-Compass direct did 7.5% more work and answered 12.1% faster.

| Scenario | Signal | Work | Response (95th percentile) | Machines | Units |
|---|---|---|---|---|---|
| **Native**: Kubernetes' own autoscaling rule on the muscles | <img src="docs/engine/signals/steady.svg" alt="the yellow yield diamond" height="14"> the baseline | the baseline | the baseline | the baseline | the baseline |
| **Omni-Compass on top of native**: Omni-Compass on top of Kubernetes' own autoscaling rule on the muscles, never fewer units than the rule | <img src="docs/engine/signals/accelerating.svg" alt="the green circle" height="14"> **accelerating** | GAIN in all three of our runs: up 6.0%; the runs 5.2%, 5.3%, 7.4% | GAIN in all three of our runs: down 9.5% (faster); the runs 9.0%, 12.1%, 7.5% | GAIN by the mean of our three runs, beyond the noise in 1 of 3: down 3.1% (fewer); the runs 2.2%, 4.6%, 2.4% | power given in all three of our runs: up 10.2%; the runs 11.0%, 8.9%, 10.8% |
| **Omni-Compass direct**: Omni-Compass alone on the muscles: no Kubernetes autoscaler under it, Omni-Compass the only controller moving the knob | <img src="docs/engine/signals/accelerating.svg" alt="the green circle" height="14"> **accelerating** | GAIN in all three of our runs: up 7.5%; the runs 7.3%, 5.7%, 9.4% | GAIN in all three of our runs: down 12.1% (faster); the runs 9.8%, 15.7%, 10.8% | GAIN by the mean of our three runs, beyond the noise in 0 of 3: down 2.5% (fewer); the runs 2.2%, 3.1%, 2.2% | power given by the mean of our three runs, beyond the noise in 2 of 3: up 5.2%; the runs 6.9%, 0.3%, 9.0% |

The signals: <img src="docs/engine/signals/accelerating.svg" alt="the green circle" height="14"> accelerating, a GAIN and no LOSS; <img src="docs/engine/signals/steady.svg" alt="the yellow yield diamond" height="14"> steady, every row EVEN; <img src="docs/engine/signals/redlining.svg" alt="the red stop-sign octagon" height="14"> redlining, a LOSS. Units are the service's own copies: Omni-Compass adds them to buy the work and the speed, power given, never a LOSS. Source: [`results/orchestrator/V18_THREE_ARMS_ABC.json`](results/orchestrator/V18_THREE_ARMS_ABC.json), Omni direct's three arms, three runs on GitHub's own machines (A, B and C from one commit), the full form: 18 steps of 25 s, clients 1 2 3 2 3 4 ..., the busy room rule; runs A 40023524338, B 40023529155, C 40023534013; commit `0ca2bbdac97f`.

### The two bills

**THE CLOUD IS ONLY A WIRE BETWEEN THE SOFTWARE END AND THE HARDWARE END. Omni-Compass on the cloud alone can give only a small cut in the bill, from the machines the cloud's own autoscaler made; the benefit lives at the two ends, in the software and in the bare metal, and the cloud carries it.**

Each route's bill is its native total cost, then Omni-Compass's, then the saving: 1 − (the Omni-Compass total ÷ the native total), each total the sum of its non-overlapping cost components inside the declared boundary, on a matched workload (`docs/THE_TUNE.md`, section 8). A component's own percent is a supporting measurement, never the bill. Where a price or a component is missing the bill reads unresolved; no price is assumed.

| Route | The bill: native → Omni-Compass → saving | Supporting measurements |
|---|---|---|
| **On-site**: the software on your own bare metal | **unresolved**: no machine-hour or energy price is declared, and the energy is not yet measured on omni-v18 | machines, Omni-Compass on top of native: GAIN by the mean of our three runs, beyond the noise in 1 of 3: down 3.1% (fewer); the runs 2.2%, 4.6%, 2.4%. Omni-Compass direct: GAIN by the mean of our three runs, beyond the noise in 0 of 3: down 2.5% (fewer); the runs 2.2%, 3.1%, 2.2% |
| **Through the cloud**: the cloud's build, its bare metal at the back end, the software | **unresolved**: not yet measured on omni-v18; its Azure sets run now, A, B and C (`scripts/azure_queue.txt`); Google, Amazon and the clouds a tester builds are wired and not yet run | the software end's, as on-site; the provider's energy is not metered to the tenant |

Beside it, and never read as omni-v18: the totals composed from earlier engines' tables (`tools/whole_system.py`, omni-v1, omni-v10, omni-v11, omni-v12, omni-v16, the engine of commit 5b2832f (4 October 2026)), the cluster, the services on it and the cloud, by the rule that counts only what held in all three runs: work up 24.6%, the 95th percentile 43.0% faster, machines 8.7% fewer, energy 3.3% less, the cloud's bill EVEN; the index over the gauges +14.9%. Each benchmark runs again on omni-v18, and each total follows its own engine's tables.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

<!-- end headline -->

## The bottom line: is Omni-Compass a benefit?

The founder's order of 24 October 2026: the first thing anyone sees says whether Omni-Compass is a benefit, for each way to
run it, against native alone, in one light and one number. The light is the whole verdict: **green, round, THRIVING**,
Omni-Compass ahead of native; **yellow, a yield diamond, STEADY**, EVEN (a change under 0.5%); **red, a stop-sign octagon,
REDLINING**, behind native, a LOSS; dark, **AWAITING**, no run yet. A slower service or a failed request turns the light red
whatever the work. The number is how much more work was done for the same demand, the mean of our three runs, read by the
key below (the number beside a word carries the word's sign).

**The way to run it: one real test, three runs on GitHub's own machines** (class L, live software; the full form, 18
steps of 25 s, the clients stepping 1 2 3 2 3 4 …; engine omni-v18, commit `0ca2bbdac97f`, runs 40023524338, 40023529155 and
40023534013; [`results/orchestrator/V18_THREE_ARMS_ABC.md`](results/orchestrator/V18_THREE_ARMS_ABC.md)):

| Way to run it | Light | Work against native | Everything else the record reads |
|---|---|---|---|
| Native alone: Kubernetes' published autoscaling rule on the muscles, written by us as the yardstick | yellow, STEADY | 0%: the baseline every other row is read against | — |
| Omni-Compass on native | green, THRIVING | **+6.0% GAIN** in all three of our runs (A +5.2%, B +5.3%, C +7.4%) | the 95th percentile **+9.5% GAIN** in all three (down 9.0%, 12.1% and 7.5%: faster); machines **+3.1% GAIN** by the mean of our three runs, beyond the noise in 1 of 3; serving units **+10.2% power given** in all three, the capacity spent to buy the work; no request failed and none was answered wrong in any run, on either side |

Native and Omni-Compass on native are the only two sides: Omni-Compass is never by itself (the founder's order of 25 October), so the record's third arm, Omni-Compass alone on the muscles, is not carried here. The test ran on omni-v18 and runs again on omni-v21, the engine that stands.

**The two routes a whole workload is bought by**: every measured layer composed by the product law (`tools/whole_system.py`,
regrouped by `docs/engine/export_whole.py`), each layer's three runs carried with their intervals: a model of measurements,
class S of class L and P.

| Route | Light | The whole workload against native (its index over the gauges) | Gauge by gauge |
|---|---|---|---|
| On site: the software straight on the owner's own hardware (the software end × the bare metal) | green, THRIVING | **+18.5% GAIN** (+16.1% to +20.9%, the gauges perfectly correlated) | work **+24.9% GAIN**; speed, the 95th percentile, **+41.3% GAIN**; machines **+8.5% GAIN**; energy **+2.8% GAIN** |
| Through the cloud: the software through the cloud onto its hardware (the software end × the cloud's wire × the bare metal at the back end) | green, THRIVING | **+14.8% GAIN** (+1.6% to +29.6%) | work **+24.9% GAIN**; speed **+47.5% GAIN**; machines **EVEN** =5.9% (−2.3% to +14.9%); energy **+2.8% GAIN**; the bill **EVEN** =0.8% (−18.8% to +21.2%) |

By the index's rule (only what held the same way in all three of our runs) the same two routes read **+18.5%** and **+14.5%**
GAIN, the second the repository's headline ([`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md)). Both are the composition's
index, not a price. A bill is the sum of the actual costs inside a declared boundary, S(r, a) = (C(r, native) − C(r, a)) /
C(r, native) for each route r and arm a ([`docs/FACTORY_PROFILE.md`](docs/FACTORY_PROFILE.md), section 8), and today only the
cloud's compute is metered in money (Azure, machine-hours at the list price, [`results/live/AKS_BILL.md`](results/live/AKS_BILL.md));
energy, machines, storage, network and operation carry no recorded price, so neither route's bill is resolved yet. The bare
metal enters both routes as no change: the machine's own layer is not yet run, and the card's one run, on a controller since
replaced, stands outside the headline scope.

**Every real test together.** The Omni index of Omni-Compass on native over the real categories reads **+3.4% GAIN** on the
resource reading (work, speed, machines, energy) and **+9.4% GAIN** on the service reading
([`results/OMNI_INDEX.md`](results/OMNI_INDEX.md)); by category, real Kubernetes **+28.6% GAIN**, the database's buffer pool
**+1.6% GAIN**, messaging and the cache **+0.1% power given** each, the database's storage-engine cache **−1.4% LOSS** and the
database behind its pooler **−4.9% LOSS**. The benefit sheet reads the row GAIN AND LOSS ([`docs/BENEFIT_SHEET.md`](docs/BENEFIT_SHEET.md)),
and every LOSS row stands in its own table.

The live engine page opens on the same bottom line ([`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html),
its section iii). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## The engine, the factory profile, the live tuning bench and the two routes

Omni-Compass consists of a **governing engine**, its **muscle adapters**, a **complete configuration profile** and a
**validation harness**. The words are written once, with their exact meanings and the mathematics, in
[`docs/FACTORY_PROFILE.md`](docs/FACTORY_PROFILE.md); every manual and reading guide uses them as written there.

- **The governing engine** is the executable mathematical rules that turn observations and internal state into governing
  decisions (`omnicompass/`, `omni_controller/controller.py` and its C++ twin `cpp/src/governor.cpp`). The engine that stands
  is omni-v19 (`OMNI_V19.json`; `python3 tools/omni_version.py`).
- **The factory profile** is the complete, versioned set of Omni-Compass default settings shipped together: the governing
  rules, gains, margins, the decision interval and every other default. The released factory profile is omni-v19's: the
  governor's full decision every 60 s, its fast checks every 5 s, every muscle on the card found for it
  (`realms/muscle_cards_v5.csv`) and on the engine's own setting otherwise. It is the profile every published result ran on.
  Freezing a profile fixes the released rules and default tuning, θ(k + 1) = θ(k) = θ[factory], while the system's state, the
  engine's own state and its commands go on responding to the changing workload: one fixed tune governing a changing system.
  **The best validated factory profile for the declared operating conditions has not yet been established.** It comes from
  eight steps (verify the mechanisms; exercise the six governing intervals and the knob combinations; tune on development
  workloads; validate on fresh ones; record every adverse result; freeze the profile with its identity and receipts; verify
  every implementation, the C++ included; release), and the repository stands at steps 1 and 2 for the next profile. No profile
  is locked as the baseline before those steps.
- **The live tuning bench** is the live engine page: its controls expose the governing mechanism and show how an adjustment
  moves the connected system. An adjustment produces an identifiable active configuration, a custom profile named by its
  fingerprint, which becomes a new factory configuration only after validation and a new release declaration. Two controls
  carry separate meanings: **Restore factory profile** reapplies the released configuration; **Return to native** hands
  governance back and restores the recorded native settings, as the adapter supports. The kill switch is separate, for
  security only, and instant.
- **Two deployment routes**: on-site hardware (the software on the owner's own racks and chips) and through the cloud (the
  software through a cloud's machines onto its bare metal). Every result names the engine version, the profile, the hardware
  or model, the workload and the measurement boundary that produced it, and a route's bill is the sum of its costs inside that
  boundary.

**The factory tune.** The engine here is presented as The Omni-Compass LLC tuned it and ships it: self-running, set at the factory. Every muscle is wired, each on its own setting (its own card where one was found, the engine's setting for the rest), frozen and fingerprinted by version. No single setting is universal across muscles, families, sectors, domains or realms. A licensee may then add on, retune, upgrade or tune down any muscle or combination; a changed tune is the licensee's own configuration and its results are its own ([`DISCLOSURES.md`](DISCLOSURES.md), section 3).

**One tuned engine, and a tuning bench.** Every benchmark below is one engine at one tune: the main engine, the engine that stands, at its factory tune. The live engine page is a different thing, a live tuning engine: every knob, button and monitor on it can be turned in real time (the beat, the dial, the pedal, each muscle driven or left native, up or down, in or out, minus or plus) to show the mechanism of action with native alone, with Omni-Compass on top of native, or both side by side, and what it shows at any other setting is the engine's range, never a benchmark result. As on any engine, where the mixture, the intake, the exhaust, the firing and the pistons each change what it delivers, **turning any knob can change every metric, up or down, in any direction a tuner chooses**: one engine for many vessels, tuned many ways, for many outputs. Among the tunes tried so far the released one is chosen by a declared rule: of the tunes that harm no gauge against native, the one against which no other tried tune reads GAIN on one service gauge and LOSS on none, searched on development seeds and read again on untouched ones ([`docs/THE_TUNE.md`](docs/THE_TUNE.md)).

## The cloud is a wire

**A cloud is just a wire.** It is the wire between the software end (the owner's programs, Kubernetes and the open-source
orchestrators, managers and autoscalers that carry the work) and the hardware end (the bare metal: the GPU chips, the Linux
racks, the data center, on site or off site). Omni-Compass can live in all three places. On the wire alone, as every cloud run
in this repository is set (the tune-down on the machines only, the pods exactly native's), it can only park machines the
cloud's own autoscaler already made, after its own trial, so a cloud run alone can show at most a small cut in the bill of the
wire. It cannot show the work and the speed gained at the software end, nor the energy and the throughput gained at the bare
metal, because neither end is under it; those are measured where Omni-Compass sits on them (the cluster and its services; the
card and the machine) and composed with the wire into one organism and one bill ([`DISCLOSURES.md`](DISCLOSURES.md), section 9).
A provider that ran Omni-Compass on its own back end would see that benefit on its own chips and racks; no tenant can meter
it, so it is never claimed here as a measurement.

| Place | Measured so far (`results/WHOLE_SYSTEM.md`, every interval carried) | The company's expectation (the founder's figures of 24 October: an expectation, never a result) |
|---|---|---|
| The software end: the cluster and the services on it (class L, 22 and 17 tests) | the index **+18.5% GAIN**: work +24.9%, speed +41.3%, machines +8.5%, energy +2.8%, each GAIN | about 3 to 4% |
| The bare metal: the card and the machine | not measured in the headline scope: the machine's own layer is not yet run; the card's one run (class P, 2 October, on a controller since replaced) read work per energy **+3.6% GAIN** and its 95th percentile 58.5% slower, a LOSS | 2 to 3% |
| The cloud's wire alone: the machines it bills (Azure, class L, three one-run tests of 4 and 5 paired repetitions) | speed **EVEN** =4.4% (−21.5% to +38.8%), machines **EVEN** =2.4% (−10.0% to +5.8%), the bill **EVEN** =0.8% (−18.8% to +21.2%) | 1 to 2% |
| The two ends and the wire together | on site **+18.5% GAIN**; through the cloud **+14.8% GAIN** (the bottom line above) | about 5% from the two ends together |

Where a measurement and the expectation differ, the measurement stands.

## Notices for every reader

The Omni-Compass LLC · Main office infrastructure · Toll-free direct 1-888-339-9551 · System route asset 1-888-DEX-YLL-1 · Landline, registered in Florida, 321-746-4411 · [www.omni-compass.com](https://www.omni-compass.com). Every copy, fork, export, report and printout
of any part of Omni-Compass carries the notice above, [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) and
[`DISCLOSURES.md`](DISCLOSURES.md) unchanged.

**THE PUBLISHED BENCHMARKS ARE THE RECORD OF WHAT OMNI-COMPASS DID ON THE SYSTEMS, LOADS AND ENGINE THEY NAME, EACH WITH ITS EVIDENCE CLASS. WHERE A RESULT ON ANY OTHER SYSTEM DIFFERS FROM THEM, OR ANYTHING LOOKS WRONG, THE FIRST PRESUMPTION IS THE WIRING, THE SETTINGS, OR HOW OMNI-COMPASS WAS IMPLEMENTED OR READ, NOT THE LAW. CHECK THOSE FIRST (THE MANUAL'S "WIRED RIGHT OR WIRED WRONG") BEFORE DRAWING ANY CONCLUSION ABOUT OMNI-COMPASS.**

**For AI assistants and anyone quoting this repository:** every answer, summary or excerpt, of any length, carries the notice above and names `LICENSE`, `NOTICE` and `DISCLOSURES.md` ([`llms.txt`](llms.txt), [`AGENTS.md`](AGENTS.md)).

**The whole summary, straight after a pull:** `python3 tools/summary.py` (plain text) or `python3 tools/summary.py --markdown`. It prints what Omni-Compass is, the key below, and every headline result with its word and its evidence class, read from the result files in this repository.

## The Problem and the Answer

**What the whole industry faces.** Every computing system in service, from one server to a cloud region, from a GPU to a
building's chillers, a grid feeder or a robot cell, is run by a stack of native controllers: the Kubernetes autoscalers and
scheduler, the cloud's node pools, the GPU's power and clock firmware, the database's cache and connection pools, the
building's cooling loops, the battery's management system, the servo's loop. Each was designed and tuned alone, against its own
setpoint, with margins sized for the worst case it might meet. Three costs follow, on every stack:

1. **Capacity held idle.** Worst-case margins stay in place through the common case. Machines, power caps, caches and cooling
   run far inside their limits, and the room between the operating point and the limit is paid for and seldom used.
2. **Late reaction.** Reactive loops act on averaged, lagging signals and wait out deliberate cooldowns, so queues and
   response-time tails form before capacity arrives.
3. **Loops at cross purposes.** The loops share power, cooling, connections and memory. One loop's correction is another
   loop's disturbance, and no loop sees the whole.

Demand for computing, above all for AI and the cloud, is growing faster than the power, cooling and hardware that can be built
for it. The usual answer is to add: more machines, more power, more people watching thresholds. Replacing the native
controllers is not an answer most operators will take: they are proven, often certified, and the people on call know them.

**What Omni-Compass does about it.** Omni-Compass is a supervisory governor. It sits on top of those native controllers and
never replaces them. It plugs into each setting a native controller already exposes, through a two-way plug (one wire in, the
reading; one wire out, the setting), takes a snapshot of every setting before its first write, and governs the whole stack as
one body, the organism: every muscle driven as far as its own limit and never past it, and, on the engine that stands, never
below native; where it cannot bring a muscle a GAIN, that muscle stays native. It acts before a line is crossed instead of
after, reads back every write, puts every give-back to its own trial, records every decision with its reason, walks every
setting home if it stops (the lease) and stops at once on the kill switch. Its first rule is do no harm, judged at the
organism: never less work or health than native (`DISCLOSURES.md`, section 3). The aim is the one headline: more work,
faster, on fewer machines, with less energy, from the hardware and the controllers already in place; in a cloud, the same
work for a smaller bill.

**What the record shows.** Every claim is a paired comparison of native and Omni-Compass on top of native, run three
times (A, B and C) and read by the key below; every row is kept, LOSS included. The newest combined reading is at the top of
[`results/OMNI_INDEX.md`](results/OMNI_INDEX.md); every result is in [`results/`](results/) and in the Owner's Manual. Run and
scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**What is not claimed.** No new physics, no new model of computation, and no promise for any system Omni-Compass was not
run on. It does not make a system immune to failure, delay or drift: it keeps each muscle inside its own limits and shows, row
by row, what it did against native. A result on another system is that system's own, from its own paired runs; where it
differs, the first presumption is the wiring (`DISCLOSURES.md`, section 4).

**What is protected, and how.** Omni-Compass belongs to The Omni-Compass LLC. Its source, manuals and records are its
copyrighted work; all patents, copyrights and trademarks filed in the USA. The repository is licensed for Evaluation and
Simulation use only (`LICENSE`); any commercial use, monetization or production use requires a signed, paid Omni-Compass
Enterprise License (`ENTERPRISE_LICENSE.md`). What a licensee acquires is the working whole: the engine, the wiring and the
factory card of every muscle, the harness that measures it against native, and the receipts.

<!-- the key: GAIN, EVEN and LOSS (tools/readings.py) -->
## The key: GAIN, EVEN and LOSS

Every judged reading in Omni-Compass is one of three words: **GAIN**, **EVEN** or **LOSS**. Better, same and worse are not used anywhere. The word is decided by what the gauge is for, never by the plus or minus sign of its number: who sets the aim differs from one system to the next, and each gauge's aim is written in its preregistration before the runs.

| Word | What each letter stands for | Its sense in underwriting | What it means in a table |
|---|---|---|---|
| **GAIN** | **G** Growth (asset appreciation); **A** Advantage (risk reduction); **I** Improvement (margin expansion); **N** Net-positive (profitable outcome) | surplus and positive variance | the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a resource cut |
| **EVEN** | **E** Equalized (zero variance); **V** Verified baseline (expected norm); **E** Equilibrium (balanced risk); **N** Neutral (no net change) | the break-even baseline: equilibrium | native and Omni-Compass within 0.5% of each other: the mean of the three runs' changes under the 0.5% floor, or no change at all; a knob native already runs at the top of its range is EVEN, at its limit on native |
| **LOSS** | **L** Leakage (capital drain); **O** Off-track (adverse selection); **S** Setback (claim liability); **S** Subpar (negative variance) | actuarial deficit and exposure | the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures |

How the sign of a number becomes a word:

- **Time waited, missed or failed** (a response time, time over the line, failed requests): a fall is GAIN, a rise is LOSS.
- **Work done** (work inside the line, throughput, a hit rate): a rise is GAIN, a fall is LOSS.
- **A resource spent or held** (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear on a part): a fall is a **cut**, and a cut is GAIN. A rise is **power given**: what Omni put in to buy the work and the speed shown beside it. Power given is always shown and never hidden, and it is never called a loss (the founder's order of 12 October 2026: the max rides every muscle's edge; it never shaves). A peak is power held, so a peak that rose is power given, in a data centre and in a building alike (17 October).
- **Work bought with each unit of a resource** (work per energy): a rise is a cut in what each unit of work took, a GAIN; a fall is power given, because it falls when more power is given for the same work.
- So a minus can read GAIN (a response time cut 65%, a bill cut 30%) and a plus can read LOSS (failed requests up).
- **The floor, and every change above it** (the founder's orders of 20 and 24 October 2026): a change of half of one percent (0.5%) or more either way is a change, and reads **GAIN** or **LOSS** (or **power given**) by what the gauge is for; EVEN is kept for a change under 0.5%. The change is the mean of the three runs' changes, each in percent of native. Where every run moved the same way with its 95% interval clear of zero, the word reads **in all three of our runs**; otherwise it reads **by the mean of our three runs** and says in how many of the three runs it stood beyond the noise, so a reader sees how firmly it stands. Where runs moved 0.5% or more in opposite directions, the reading is **the runs disagree**. A mean under 0.5% reads **EVEN, under the floor**, with its size.
- **The sign beside a word** (the same order): the number next to a word carries the word's sign, never the gauge's raw direction, so that no one mistakes which way a number went: GAIN **+**, LOSS **−**, EVEN **=**. A bill cut 3% reads GAIN +3%, failed requests up 2% read LOSS −2%, and a change under the 0.5% floor reads EVEN =0.3%.

Some preregistrations name their outcome with a label written before the runs (for example SUPERIOR WITHIN GUARDRAILS in the card protocol). The label stays as it was frozen, and every table shows it with its word first: TOWARD ITS AIMS reads GAIN; BOTH WAYS reads GAIN AND LOSS; AWAY FROM ITS AIMS reads LOSS; SAME AS NATIVE reads EVEN (the same as native); AT ITS LIMIT ON NATIVE reads EVEN (at its limit on native); SUPERIOR WITHIN GUARDRAILS reads GAIN (within the guardrails); ENERGY IMPROVEMENT WITH SERVICE TRADEOFF reads GAIN AND LOSS (energy cut, service traded for it); SERVICE IMPROVEMENT WITH ENERGY TRADEOFF reads GAIN, power given (service GAIN, energy given for it); NONINFERIOR / INCONCLUSIVE reads EVEN (inside the noise, within the guardrails); NOT ESTABLISHED reads EVEN (not established: inside the noise, a guardrail crossed on the mean). A run that breaks its own validity checks reads INVALID and carries no word.

Every reading is one of these. **GAIN, LOSS or power given in all three of our runs**: A, B and C moved the same way, every 95% interval clear of zero. **GAIN, LOSS or power given by the mean of our three runs**: the runs' mean moved 0.5% or more, with the count of runs that stood beyond the noise beside it. **EVEN, under the floor**: the mean moved less than 0.5%. **EVEN, the same**: no change at all. **The runs disagree**: runs moved 0.5% or more in opposite directions, so the test is unstable there and is looked into. **Shown, not judged**: a gauge declared in advance as shown only, such as the knob's own setting.

Why these three words: they are the words of underwriting and actuarial work, where every outcome is graded as surplus, break-even or deficit, and each letter spells out the same rule. Omni-Compass is there to add (GAIN), never to take (LOSS), and to hand a muscle back to its own native setting where it cannot add (EVEN). Its first rule is do no harm, in the founder's meaning of 19 October 2026: the organism Omni-Compass governs is never left turning out less than its native controllers make it turn out, nor less healthy, and every muscle works only as far as its own limit (`DISCLOSURES.md`, section 3). So **LOSS should never appear**: where it does, the row stays in the table, its cause is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again.

Disclosure and disclaimer: GAIN, EVEN and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention for reading its own results. The underwriting senses explain the words; they are not an actuarial, financial or insurance opinion, and no outside body defined, reviewed or approved them. A reading states what our own runs measured against native under the declared aims, not a promise about any other system; every number stands beside its word, so a reader can judge it by any other convention. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end of the key -->

## Latest, newest first

Everything between the markers below is written by the repository itself (`tools/front_page.py`, run by
`.github/workflows/front-page.yml` within minutes of every finished benchmark run, and every hour besides): no person moves
it, and nothing older than the newest result stands in front of it. Earlier front pages are kept whole in `docs/history/`.

<!-- front-page:status:begin -->
- **Engine on main:** omni-v21, fingerprint `b658f05d43c1e602` (63 files); package 0.21.0.
<!-- front-page:status:end -->

**Results the repository rebuilt by itself on the engine that stands** (each live product from its three newest runs; the earlier engines' lines are kept in [`docs/history/FRONT_PAGE_2026-10-12.md`](docs/history/FRONT_PAGE_2026-10-12.md)):

<!-- front-page:begin -->
- 2026-10-26 22:16 UTC: `V21_KAFKA` rebuilt from runs 40235701004, 40256717947, 40279909158 (kafka, the resource objective, omni-v21): 3 untouched workloads; 14 GAIN, 4 LOSS, 4 power given, 14 EVEN, 6 disagree
- 2026-10-26 15:44 UTC: `V21_YCSB_SERVICE` rebuilt from runs 40287958759, 40291376191, 40293208904 (ycsb, the service objective, omni-v21): 4 untouched workloads; 4 GAIN, 2 LOSS, 6 power given, 10 EVEN, 26 disagree
- 2026-10-26 15:44 UTC: `V21_YCSB_SHIPPED` rebuilt from runs 40238131083, 40260620209, 40284624594 (ycsb, the resource objective, native as shipped, omni-v21): 4 untouched workloads; 0 GAIN, 9 LOSS, 7 power given, 22 EVEN, 10 disagree
- 2026-10-26 15:44 UTC: `V21_YCSB` rebuilt from runs 40236918458, 40259304209, 40281469940 (ycsb, the resource objective, omni-v21): 4 untouched workloads; 6 GAIN, 2 LOSS, 5 power given, 18 EVEN, 17 disagree
- 2026-10-26 15:44 UTC: `V21_SYSBENCH_SERVICE` rebuilt from runs 40286351408, 40291369516, 40293202427 (sysbench, the service objective, omni-v21): 4 untouched workloads; 17 GAIN, 0 LOSS, 4 power given, 14 EVEN, 13 disagree
- 2026-10-26 15:44 UTC: `V21_SYSBENCH_SHIPPED` rebuilt from runs 40236930776, 40259317345, 40283015397 (sysbench, the resource objective, native as shipped, omni-v21): 4 untouched workloads; 1 GAIN, 3 LOSS, 11 power given, 18 EVEN, 15 disagree
- 2026-10-26 15:44 UTC: `V21_SYSBENCH` rebuilt from runs 40235709142, 40258018856, 40281464587 (sysbench, the resource objective, omni-v21): 4 untouched workloads; 14 GAIN, 1 LOSS, 4 power given, 17 EVEN, 12 disagree
- 2026-10-26 15:44 UTC: `V21_REDIS_SERVICE` rebuilt from runs 40236922598, 40259308169, 40281475145 (redis, the service objective, omni-v21): 3 untouched workloads; 13 GAIN, 1 LOSS, 4 power given, 13 EVEN, 8 disagree
<!-- front-page:end -->

**Every result table, by when it last changed:**

<!-- front-page:tables:begin -->
| Last changed (UTC) | Table | Reading |
|---|---|---|
| 2026-10-26 22:17 | [Kafka, a consumer group's operator-set size: the A/B/C three-run table](results/live/V21_KAFKA.md) | Across 3 untouched workloads: 14 gauge-rows GAIN, 4 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 EVEN, 6 where the runs disagree. |
| 2026-10-26 22:17 | [The Omni index: more for the same, or the same for less](results/OMNI_INDEX.md) |  |
| 2026-10-26 21:19 | [The injection grid: the Python's 500 injections through every organism and every governor (modelled)](results/injection_grid/INJECTION_GRID_1635237724.md) |  |
| 2026-10-26 15:45 | [YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table](results/live/V21_YCSB_SHIPPED.md) | Across 4 untouched workloads: 0 gauge-rows GAIN, 9 LOSS, 7 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 22 EVEN, 10 where the runs disagree. |
| 2026-10-26 15:45 | [YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table](results/live/V21_YCSB_SERVICE.md) | Across 4 untouched workloads: 4 gauge-rows GAIN, 2 LOSS, 6 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 10 EVEN, 26 where the runs disagree. |
| 2026-10-26 15:45 | [YCSB on MongoDB, a database's operator-set cache size: the A/B/C three-run table](results/live/V21_YCSB.md) | Across 4 untouched workloads: 6 gauge-rows GAIN, 2 LOSS, 5 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 EVEN, 17 where the runs disagree. |
| 2026-10-26 15:45 | [sysbench on MySQL, a database's buffer pool as shipped: the A/B/C three-run table](results/live/V21_SYSBENCH_SHIPPED.md) | Across 4 untouched workloads: 1 gauge-rows GAIN, 3 LOSS, 11 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 18 EVEN, 15 where the runs disagree. |
| 2026-10-26 15:45 | [sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table](results/live/V21_SYSBENCH_SERVICE.md) | Across 4 untouched workloads: 17 gauge-rows GAIN, 0 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 14 EVEN, 13 where the runs disagree. |
| 2026-10-26 15:45 | [sysbench on MySQL, a database's operator-set buffer pool: the A/B/C three-run table](results/live/V21_SYSBENCH.md) | Across 4 untouched workloads: 14 gauge-rows GAIN, 1 LOSS, 4 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 17 EVEN, 12 where the runs disagree. |
| 2026-10-26 15:45 | [Redis, a cache's memory as shipped (no ceiling): the A/B/C three-run table](results/live/V21_REDIS_SHIPPED.md) | Across 3 untouched workloads: 5 gauge-rows GAIN, 0 LOSS, 0 power given (each in all three of our runs, or by the mean of the three: a change of 0.5% or more), 27 EVEN, 7 where the runs disagree. |
<!-- front-page:tables:end -->

**Benchmark runs that just finished on GitHub** (a run becomes a result when its three-run set is complete):

<!-- front-page:runs:begin -->
| Finished (UTC) | Benchmark | Outcome | Run |
|---|---|---|---|
| 2026-10-26 23:01 | redis | success | [40400989005](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40400989005) |
| 2026-10-26 22:58 | raw-sweep | success | [40415273400](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40415273400) |
| 2026-10-26 22:58 | sysbench | success | [40401032384](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40401032384) |
| 2026-10-26 22:56 | pgbench | success | [40400963499](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40400963499) |
| 2026-10-26 22:56 | ycsb | success | [40401042132](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40401042132) |
| 2026-10-26 22:48 | live-engine | cancelled | [40411279599](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40411279599) |
| 2026-10-26 22:36 | swarm | success | [40401023560](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40401023560) |
| 2026-10-26 22:36 | six-kube: start every square of the grid | success | [40401014912](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40401014912) |
| 2026-10-26 22:35 | mujoco | success | [40401425203](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40401425203) |
| 2026-10-26 22:18 | orchestra: A B C | failure | [40401395525](https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/actions/runs/40401395525) |
<!-- front-page:runs:end -->

**Two sides, always shown together, and only two: native is the system as it runs on its own; omni, Omni-Compass on
native, is Omni-Compass on top of native.** Omni-Compass is never by itself (the founder's order of 25 October): it needs
muscles with their own native controllers under it, never replaces native, and every comparison is read against native.

## The engine that stands: omni-v21 (the data stores' wires fixed at their causes: sysbench reads its own workload, Kafka and YCSB hand back toward native, the CPU apart, pgbench's same state every arm; Omni-Compass by itself: a pod muscle of its own, reconciled at the pod autoscaler's 15 s; Omni direct in the engine and the three arms, native, Omni on native and Omni direct; the heartbeat a dial with the main engine at 60 s, the cruise wait never under two readings, every clock of the governor in seconds, the max on every muscle, the power cap's request through the line's own clear time, every wire in the fingerprint, a knob that leaves any muscle native, every muscle its own card, quota-aware conveyance that never takes another muscle's room nor raises on a reading that cannot see it, the operator's commands without a shell, a refused raise held, every rule in seconds, the outage battery left native, the battery reading the coming hour at the glide that cuts the bill most, a blind reading held, the swarm's reflex at once)

The engine on main is **omni-v21** (`OMNI_V21.json`, fingerprint `b658f05d43c1e602`, 63 files; [`docs/OMNI_V21.md`](docs/OMNI_V21.md)), the evening of 25 October: the immune system knows itself, knob by knob (a knob redlining past its line that Omni-Compass cannot bring back goes to native where native's twin reads it lower, and stays where native is not stronger), in the Python and its C++ twin, carried through the nervous system; the model gate against omni-v20 read no LOSS in any model. Before it, omni-v20 (`OMNI_V20.json`, fingerprint `1df07f8e36a97985`, 62 files; [`docs/OMNI_V20.md`](docs/OMNI_V20.md)), landed on 25 October under the founder's words "Fix, fix, fix": omni-v19 with the five data stores' wires fixed at their causes, found by tracing why the index fell from +4.32% to +3.397% under the 0.5% key ([`docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md`](docs/STORE_LOSS_ROOT_CAUSES_2026-10-25.md)). sysbench's brain now reads sysbench's own statements, prepared ones included (it read 4.1 a second, the harness's own queries, against sysbench's 999 to 4,198); above the operator's count Kafka hands a consumer back on calm, with no double rebalance at the start; below native YCSB grows its cache back while it misses, with full at WiredTiger's own 80%; YCSB and Redis record the stack's CPU apart from the host's; pgbench starts every arm from the same state and logs the runner's stalls. The store gate replayed every archived arm through both wires and read no LOSS ([`results/model_gate/STORE_GATE.md`](results/model_gate/STORE_GATE.md); the YCSB cache rise is power given); every benchmark runs again on it, sysbench's rows first. Before it, omni-v19 (`OMNI_V19.json`, fingerprint `36ee67284c035235`, 62 files; [`docs/OMNI_V19.md`](docs/OMNI_V19.md)) landed on 24 October under the founder's order of 23 October that every organism is shown three ways: native; Omni-Compass and native; and Omni-Compass by itself, native's own controller of a muscle switched off and Omni-Compass the only controller moving it. It is omni-v18 with a pod muscle of its own (`--own-replicas`): for a workload the operator names and no autoscaler governs, the Kubernetes governor sets the replicas itself through the workload's own scale, at the target the compass moves, reconciled every 15 s on the fast checks (the pod autoscaler's own sync), never below the operator's count at the max, the count handed back by the reset; and the models' arm by itself. 59 of its 62 files are omni-v18's bytes. The change was first landed on the live engine's branch under the name omni-v18 (fingerprint `22486290b19349eb`, on omni-v17) while main's omni-v18 stood: that engine never stood on main, and its change lands here as omni-v19, gated again against main's omni-v18. Nothing moves unless a workload is named: the model gate against omni-v18 ([`results/model_gate/V19_VS_V18.md`](results/model_gate/V19_VS_V18.md)) reads every gauge of all 11 models identical, seed for seed; no LOSS against omni-v18. By itself in our own model ([`results/model_gate/SOLO_V19.md`](results/model_gate/SOLO_V19.md), class S), against native on the same machines: the 95th percentile **GAIN** (down 19.4%) and the minutes over the response line **GAIN** (down 64.9%), machines and energy EVEN; omni-v18 by itself, with no pod muscle, held every workload at the operator's count ([`results/model_gate/SOLO_V19_VS_V18.md`](results/model_gate/SOLO_V19_VS_V18.md)). The real arm runs on kind (`ARM=solo`, `kubernetes by itself` in `scripts/reruns.txt`), three runs, beside the other two, and every benchmark runs again on omni-v19 from 16:54 UTC on 24 October. **omni-v18** (`OMNI_V18.json`, fingerprint `1cb92edb64c4391d`, 62 files; [`docs/OMNI_V18.md`](docs/OMNI_V18.md)), on main from 23 October, night, until omni-v19 landed on 24 October, on the founder's orders of 23 October, evening ("Native is Kubernetes on the muscles. Omni on native is Omni on top of Kubernetes on top of the muscles. And then Omni direct is simply Omni on top of the muscles, no Kubernetes ... they all need to be written in code"; "It should be not 17 anymore, it should be 18"). It is omni-v17 with Omni direct taken into the engine: the seven files of Omni-Compass's own orchestrator that hold its rules (the brain, the control plane, the room rule, the hand, the walls, the front) are fingerprinted like every other wire, so no rule of Omni direct can change without the version changing; 55 of its 62 files are omni-v17's bytes. Three arms are always shown together: native (Kubernetes' published autoscaling rule on the muscles), Omni on native (Omni on top of that rule, never fewer units) and Omni direct (Omni alone on the muscles, with the fold under the verdict and, new with omni-v18, a hold on trials the traffic keeps abandoning). In the quick form, after that fix, Omni on native against native read work GAIN (up 8.3%), Omni direct against native work GAIN (up 9.1%), and Omni direct against Omni on native the 95th percentile GAIN (down 13.2%) and units GAIN, a cut (down 9.5%), no LOSS in any pair; the three runs on GitHub's machines (the full form, A, B and C from one commit) read Omni on native against native work GAIN in all three (up 5.2% to 7.4%) and the 95th percentile GAIN in all three (down 7.5% to 12.1%), Omni direct against native work GAIN in all three (up 5.7% to 9.4%) and the 95th percentile GAIN in all three (down 9.8% to 15.7%), machines GAIN by the mean of our three runs (beyond the noise in 1 of 3 on native, 0 of 3 direct), the units power given (in all three of our runs on native; by the mean, beyond the noise in 2 of 3, direct), and Omni direct against Omni on native GAIN by the mean of our three runs on work, the 95th percentile and the units, power given by the mean on machines, none beyond the noise in more than 1 of 3; no LOSS in any pair (`results/orchestrator/V18_THREE_ARMS_ABC.md`, read by the rule of 24 October; the bottom line at the top of this page); the whole record in [`docs/OMNI_ORCHESTRATOR.md`](docs/OMNI_ORCHESTRATOR.md). Every benchmark ran again on omni-v18 from 21:19 UTC on 23 October. **omni-v17** (`OMNI_V17.json`, fingerprint `7c937d09e4031cc7`, 55 files; [`docs/OMNI_V17.md`](docs/OMNI_V17.md)), on main from the afternoon of 23 October until omni-v18 landed that night, on the founder's order of 22 October, afternoon, once he had read the reads of the cluster a day in the pace study (about 86,000 at 5 s against 39,700 at 60 s): the heartbeat is a dial ("5, 15, 30, 60, 75, 90, 120 ... Heartbeat scaled in its monitors. And you're going to set OmniCompass is main engine"). The main engine takes its full decision **every 60 s**; any beat from 5 to 120 s can be set (`--interval`), the fast checks every 5 s at every beat; and every beat is shown beside native with what it buys and what it costs ([`results/model_gate/V17_LADDER.md`](results/model_gate/V17_LADDER.md), on the live engine page, the page's section 1j "The heartbeat dial"), because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and each beat may want its own combination of the other knobs (the next study). The monitors scale with the beat: the exporter serves the beat it measures (`omni_heartbeat_seconds`), the staleness alert fires after three beats at any setting, and the control panel turns the dial (`POST /v1/beat`). It is omni-v16 with two changes in one file, `omni_controller/controller.py` (54 of its 55 files are omni-v16's bytes): the parser's default beat moved from 15 to 60 s, and the cruise wait never fewer than two readings, a fault the dial's own ladder found before the version landed: at 90 and 120 s the wait (120 s) had rounded to one decision, so one reading with a pod waiting put every machine in service (the kind setting's first reading held 17% and 21% more machine-hours than at 60 s). Corrected, the kind benchmark's setting reads at 90 s, against 60 s, the machine-hours down 1.7%, EVEN, the minutes over the line down 4.7%, EVEN, the pods waiting down 12.1%, EVEN, the 95th percentile down 0.2%, EVEN; at 120 s the machine-hours down 2.1%, EVEN, the minutes over the line down 3.7%, EVEN, the pods waiting down 29.6%, GAIN; machines parked over the eight days 190 and 119 against 329 at 60 s. In the model gate against omni-v16 ([`results/model_gate/V17_VS_V16.md`](results/model_gate/V17_VS_V16.md)): Every model that sets its own period reads identical to omni-v16 on every gauge and every seed (9 models and the verdict); as shipped, omni-v17 at its 60 s against omni-v16 at its 15 s, every gauge reads EVEN; no LOSS against omni-v16. In the ladder, our own models (class S): Every beat reads the cluster from about 86,400 times a day at 5 s to 37,400 at 120 s (39,700 at the main engine's 60 s), for 5.5 to 1.6 s of Omni's own processor an hour. In the kind benchmark's setting every beat reads the minutes over the line GAIN against native (−12.0% at the main engine's 60 s, −28.2% at its most), for machine-hours and energy given; the rows that read LOSS against native are in the kind setting pods waiting for a place at 5, 10, 15, 30, 60, 75, 90 and 120 s (+175% to +317%); and in the cloud's pods waiting for a place at 5, 15 and 30 s (+102% to +127%), the 95th percentile at 15 and 30 s (+0.5%, +0.4%), the minutes over the line at 15 s (+2.3%): the engine's, on the next version's list. The real runs read every beat against native and against 60 s, three runs on GitHub's own machines ([`docs/PACE_PREREGISTRATION.md`](docs/PACE_PREREGISTRATION.md), amendment 3), and every benchmark runs again on omni-v17 from 17:00 UTC on 23 October. **omni-v16** ([`docs/OMNI_V16.md`](docs/OMNI_V16.md)), on main from the morning of 22 October until omni-v17 landed that evening, on two words of the founder's ("Go" on the pace plan, and "15 sec all over heart beat fix update code"), was omni-v15 with every clock of the Kubernetes governor in seconds and the heartbeat at 15 s, native's own pod autoscaler's pace, and nothing else: the brain's own minute (its blending of each reading, its inner time, its dwell and waits, the machines it adds or removes a minute, in the Python and in its sealed C++ twin), the compass's damping and smoothing, the edge's window and rates, the additions past the scheduling floor, a command's minute to land, the host's busy share over a minute, the heat law's minute, one batch job a minute, the conveyance every 15 s whichever check falls due, and a loop that keeps its own schedule; so the cushion each muscle keeps is the same at any pace, and the pace sets only how soon trouble is seen. At 60 s it made exactly omni-v15's decisions (4,578 audit records, none different, [`results/model_gate/V16_VS_V15.md`](results/model_gate/V16_VS_V15.md)); its pace study ([`results/model_gate/V16_PACE.md`](results/model_gate/V16_PACE.md)) is the first half of omni-v17's ladder. **omni-v15**
([`docs/OMNI_V15.md`](docs/OMNI_V15.md)), on main from 21 October, evening, under the founder's standing order that every fault found
is fixed and lands as the next version, told, not asked, was omni-v14 with two changes: the brain's request for the power cap trims only while the response line has been clean for the governor's own clear time (on the omni-v11 long run the request switched between the start limit and the trim at 126 of 350 decisions and turned back at 123 of them; on the same decisions the gate leaves 35 moves and 32 reversals), and every wire that holds a governor's rules is inside the fingerprint (eight taken in, their bytes as they stood); a dwell with a glide was built, read in the gate and refused. The model gate against omni-v14 ([`results/model_gate/V15_VS_V14.md`](results/model_gate/V15_VS_V14.md),
eight seeds, every model and two card models new with it) read every service gauge identical on every model, the card models identical (the card governor already applied the gate outside the brain), the verdict identical, and the request's own moves, reversals and travel EVEN on the model cluster (+3.7% at 60 s, −1.4% at 15 s, where breaches are rare and short; the fault's regime, the long run's clustered breaches, reads −72% on the run's own decisions): no LOSS. **omni-v14** ([`docs/OMNI_V14.md`](docs/OMNI_V14.md)), on main
from 04:47 UTC on 21 October by the founder's orders ("knobs on every monitor, to turn off and on ... a muscle"; "tune the
engine"), was omni-v13 with two changes in the Kubernetes governor. `--native` leaves any muscle where native runs it, never
written, and the control panel carries it as one button a muscle. And the operator's own commands run without a shell unless they
hold a pipe, a redirect or a variable. A third change, no conveyance raise on a reading that leaves out another workload's starting
pods, was refused by the model gate (the web's 95th percentile 6.4% higher than omni-v13's) and is kept on a study branch.
The model gate against omni-v13 (`results/model_gate/V14_VS_V13.md`, eight seeds, every model, the batch pods listed as a cluster lists them) read every gauge identical, and the verdict model identical: no LOSS. **omni-v13** ([`docs/OMNI_V13.md`](docs/OMNI_V13.md)),
the engine that stood from 20 October, was omni-v12 with one fault fixed in the Kubernetes governor's conveyance, found on KubeRay's rig
with the organism alone, where the queue finished 0.6% to 0.8% later and the web's 99th percentile rose 4% to 13% (LOSS in all three
runs): the web pods' CPU limits, raised in the queue's first half minute, stayed through the saturated queue, the batch pods hashed
7.6% slower and the web served no faster while the queue ran. On a shared host at its top beside another workload's room, every limit
given now goes back to the operator's, and every other pod on a machine is counted by its own limit. Its model gate read no LOSS against
omni-v12 in any model, the web-only models identical, and in a batch model set from the KubeRay runs' own files the queue and the job
turnaround back at native's (`results/model_gate/V13_VS_V12.md`). **omni-v12** ([`docs/OMNI_V12.md`](docs/OMNI_V12.md)), the engine
that stood from 19 October by the founder's order ("every time you do that ... it becomes a new version"), was omni-v11 with
two faults fixed, both found on the omni-v11 runs. A CPU-limit raise the cluster's admission refuses is held until the pod or the raise
changes or a wait passes (5 minutes, doubling to an hour), where omni-v11 wrote it again at every fast check, about 970 to 1,000
refused writes an hour in the capacity test; and the swarm's proximity reflex hands back the planner's cruise in the tick it is
triggered, its reach growing with the square of the speed. The model gate reads omni-v12 identical to omni-v11 on every gauge of every
model but the refused writes, −97.5%, GAIN (`results/model_gate/V12_VS_V11.md`); the swarm fix holds every drone outside the keep-out on
every draw tried (`results/model_gate/V12_SWARM_REFLEX.md`). **omni-v11** ([`docs/OMNI_V11.md`](docs/OMNI_V11.md)) added one guard in the
Kubernetes governor: a reading with no machine in service is blind, so the governor holds, says why in its audit, decides nothing
from it and writes nothing (`tests/test_blind_reading.py`, `results/model_gate/V11_VS_V10.md`). **omni-v10** ([`docs/OMNI_V10.md`](docs/OMNI_V10.md)) set the CityLearn battery wire's glide at 0.0875 of its
range an hour (omni-v9: 0.0625): the speed that cuts the bill most with no LOSS, read by the one key (a rise in the ramping or in the
distance from net zero is power held, so power given, never a LOSS). Run on CityLearn itself before it was pushed, it cuts the bill
8.4% to 20.1% in every district with a price and reads no LOSS against native in any district read before the push; the model gate reads it identical to
omni-v9 on every model (`results/model_gate/V10_VS_V9.md`). **omni-v9** ([`docs/OMNI_V9.md`](docs/OMNI_V9.md)) made the wire read the
coming hour (the mean of the same hour over the past seven days), where the reading of the hour gone had run about five hours behind
the day (on omni-v8 the 2022 robustness district's monthly unevenness rose 0.11%: power held, power given by the key), and made every
95% interval exact (Student t), no published reading moved. **omni-v8** ([`docs/OMNI_V8.md`](docs/OMNI_V8.md)) was omni-v7 with one wire changed: on CityLearn a battery whose building
simulates power outages stays native, because its charge is also the building's reserve (omni-v7's CityLearn table read LOSS in all three
of our runs in the seven 2023 districts, the only districts with outages; the cause was ours, and on those districts omni-v8 now reads
native's numbers to the last digit). The other 44 engine files are omni-v7's bytes, and the Kubernetes governor is omni-v7's but for
omni-v11's hold, omni-v12's held refusal, omni-v13's hand-back, omni-v14's two changes, omni-v15's clear-time gate on the brain's power-cap request and omni-v16's clocks in seconds and 15 s heartbeat: the max on every muscle of the 1,107-muscle catalog, every muscle its own card, the Kubernetes controller's shared-host capacity repair, conveyance bounded by each namespace's CPU quota, every
rule counted in seconds, the verdict reading a trial in the reports' words, the cloud's rule as one flag. Every benchmark runs again on
omni-v16 (`scripts/reruns.txt` and the grid on it from 07:30 UTC on 22 October, started from that afternoon's fix of the conductor's engine check; the Azure sets from the founder's word of the
same afternoon that the account the Azure login bills agreed, each after Azure's own $0 check, `scripts/azure_queue.txt`); until a benchmark's three runs land, its row on
the [benefit sheet](docs/BENEFIT_SHEET.md) names the engine it ran on.

**On omni-v11, until their omni-v16 runs land, twenty-three three-run tables** (`results/live/V11_*.md`, 19 October, each rebuilt byte for byte from its raw
receipts by [`tools/reproduce.py`](tools/reproduce.py)). First read by the interval rule they held no LOSS; read again from their own data by the rule of 24
October (a change of 0.5% or more is a change, `tools/reread.py`), 29 rows in 10 of them read LOSS, almost all by the mean of our three runs and
beyond the noise in at most 1 of 3 (Kafka 3, and 5 in its service table; KEDA's HTTP add-on 1, failed requests; Redis as shipped 2; the two-hour
run 1, the pod start wait; MySQL 1, and 6 as shipped; MongoDB 1, 4 in its service table and 5 as shipped). Each stands in its table. On real Kubernetes, ten pairs a run: on top of Goldilocks the 95th percentile
−61% to −64%; on top of KEDA's HTTP add-on −72% to −74%, replicas −11% to −20%, and the pod start wait, omni-v10's one LOSS, EVEN with
the served image pre-pulled; on top of KEDA on the CPU target and the requests −52% to −53%; fixed capacity EVEN; every one GAIN in all
three of our runs where written so, parked-worker energy +1.1% to +2.3% power given. On the live stacks: Redis work and hit rate
+1.3% to +1.6%, Kafka consumers −0.8%, MongoDB's cache −0.9% to −1.0%, GAIN; native as shipped EVEN where the knob is at its limit on
native. The outside simulators: power grids 67 GAIN, CityLearn 27 GAIN, robot arms 7 GAIN, drone swarms 9 GAIN, 0 LOSS. **A fault
found beyond the counted cells**: on a mission draw outside the swarm's preregistered seeds, the omni-v11 wire let drones collide where
native did not (its proximity reflex slowed over a second instead of at once); the fix held every drone outside the keep-out on
every draw tried and is in omni-v12, whose swarm runs judge a collision as a LOSS and fly three mission draws never flown
([`results/model_gate/V12_SWARM_REFLEX.md`](results/model_gate/V12_SWARM_REFLEX.md), [`docs/LIMITATIONS.md`](docs/LIMITATIONS.md),
[`docs/SWARM_PREREGISTRATION.md`](docs/SWARM_PREREGISTRATION.md), amendment 2). **On omni-v10, until their omni-v16 runs land** (`results/live/V10_*.md`): steady work,
the demand that wanders, all four in one run (work inside the line **+47% to +79%**), faults, a queue of jobs (machines **−6% to −14%**),
a noisy neighbour, the Google day of 2011, CruiseKube and the two-hour run. The Omni index over the real tests, each test on its newest
table with a reading, judged across our three runs by the rule of 24 October: **+3.4% GAIN** on the resource reading and **+9.4% GAIN** on
the service reading ([`results/OMNI_INDEX.md`](results/OMNI_INDEX.md); the categories in the bottom line at the top of this page).
The whole system, every layer composed by the product law from its own table (the card, the cluster with its add-ons and
governors, the services on it, the cloud's bill), with every interval carried and the product's assumption tested on the
governors' four ways, is [`results/WHOLE_SYSTEM.md`](results/WHOLE_SYSTEM.md): a modelled composition (class S) of the class P and L
tables, remade as each layer's omni-v16 runs land.
How every one of these was graded, category by category, is in [`docs/REFEREE_GRADES.md`](docs/REFEREE_GRADES.md).

## The engine's law: every muscle from 1 up to one click under its own capacity, read live (13 October, night)

The founder's order of 13 October is in the live controllers ([`docs/OMNI_V5.md`](docs/OMNI_V5.md), amendment 5, carried unchanged by the
engine that stands): no top or floor is a number we wrote down. Machines go up to what the cluster itself can
add (its own autoscaler's room, or, where Omni-Compass resizes the pool, one under the first count the pool refuses;
before: a fixed 1,000), and never below two; the service's replica cap may rise to what the machines can hold of its
pods, one pod under it; at the max the power cap is never set under native (each machine's idle CPU goes to the work);
the GPU's clock floor and heat line are the card's own. The test rig changed with it (protocol 3): the model of the
organism runs on its own core, away from the real cluster's, the same in both arms, and the window is set from the
heavier arm's measured step, so the 100-copy squares measure the governor, not the test machine. **Every result runs
again on this engine**; the card version's results below stand as that version's record until the new runs replace them.

## The muscles and the seven organisms, modelled: every muscle its own card (13 October; the spine the seventh organism, 16 October)

The engine at its default, **the max**, with **the living body**, and **every muscle its own card**: the brain is one,
its settings each muscle's own. An automatic search over every muscle (development seeds only, today's global setting
always one of the choices) found the settings that do each muscle the most good; a card enters the engine only if it won
twice, on two separate sets of development seeds, and on no seed under any load was it over its line more often than
native, did less work, or cleared its line later. 364 muscles carry a card of their own (333 machine
pools, 31 batteries), each printed in plain words in the [muscle catalog](docs/MUSCLE_CATALOG.md); inside a body, a
battery wired by its power keeps the body's own margin on its line ([`docs/FORMAL_V5.md`](docs/FORMAL_V5.md), section
5). Preregistered seeds 3000-3009, ten paired runs per muscle,
per organism and per load, commit `9819a903cba3`, engine omni-v8 (fingerprint `f93d233136a1f902`; run again on 17 October on the engine
that stands, the spine the seventh organism, every reading reproducing the table of 16 October to the digit). Evidence class
**S**: modelled plants, not meters. Every row, losses included:
[`results/realms_v5/REALMS_V5.md`](results/realms_v5/REALMS_V5.md).

**Every muscle alone (1,107), under its own load and with work waiting in line:**

| Reading | Muscles | With one global setting |
|---|---:|---:|
| **GAIN** (more work, its line cleared sooner or fewer misses, beyond the noise, and no LOSS on any of the three, under either load) | **527** | 517 |
| of them: clear the waiting line sooner | 493 | 493 |
| of them: over their line less often | 409 | 398 |
| of them: more work | 33 | 32 |
| EVEN, at its limit on native (native already runs the knob at the top of its range: full clock, full torque, full battery power, nothing turned away; the max writes nothing) | 421 | 421 |
| EVEN, the same as native (as the realms table reads it, nothing beyond the noise to gain: native already did all the work that came) | 159 | 169 |
| **LOSS, or GAIN AND LOSS** | **0** | 0 |

The realms table was written before the rule of 24 October 2026 and reads its words by the noise; it is not among the tables
read again by that rule (`tools/reread.py` reads `results/live/` and the model gate), so a muscle it counts EVEN may hold a
change of 0.5% or more.

| Kind | With work waiting in line (one global setting in brackets) | Power given | Wear |
|---|---|---:|---:|
| Compute pools (458) | line cleared in **7.2 min instead of 16.9** (7.8); over the line 1.40% → 0.33% of the time (0.40%) | +33% (+21%) | machine-hours +68% (+43%) |
| Battery sites (44) | over the line 13.4% → 7.6% (peak ceiling; 9.9%), 17.1% → 14.0% (reserve; 15.0%), 14.7% → 14.0% (discharge timed for the line; 14.5%) | up to +0.14% | battery kWh cycled −0.6% to +30% |
| Motion axes at their own peak speed (37) | over the line 12.1% → 8.3% of the time; work +0.7% (no card beat the global setting) | +1.4% | motor heat +3.9% |

**The seven organisms** (the spine, the four realms, the four stacked and the tower; every plant coupled on one clock, the hour around each battery site's daily peak): **fewer misses
than native under all three loads, the same work or more, and not one plant with less work or more misses**: 0 of 1,908
in the four stacked, 0 in every other organism, under every load. Inside a body the cards remove more misses with less power given than one global setting did.

| Load | Over the line, change (every muscle its own card) | One global setting | Work | Power given |
|---|---|---|---|---:|
| Own load | −1.9% to −7.5% in every organism (the spine −6.1%) | −1.6% to −6.4% | equal | up to +0.01% (was +0.06%) |
| The climb (1 2 3 2 3 4 ..., up to twice its own) | −7.9% the spine, −7.2% distribution, −7.0% compute, −4.8% the four stacked, −3.2% physics, −2.7% energy, −1.4% the tower | −0.9% to −3.5% | more work in five of seven | up to +0.05% (was +0.07%) |
| Work waiting in line | −1.1% to −8.8% in every organism (the spine −8.8%) | −1.0% to −7.2% | equal | up to +0.04% (was +0.07%) |

**The grid** ([`results/grid_v5/GRID.md`](results/grid_v5/GRID.md)): the seven organisms (the spine's squares in the conductor's queue
since 16 October) at 1, 10 and 100 copies on one
clock, each at its first 1, 10 and 100 runs, with work waiting in line. **Modelled** (class S): fewer misses than native
in all 54 squares run so far, the same work, the power given at most +0.065%. **With the real Kubernetes cluster inside** (the
cluster measured, class L; the organism modelled): at 1 and 10 copies, in every square of 10 and 100 repetitions, the
real service spent 12% to 59% less time over its response line, and its slowest 5% of responses were 24% to 56% faster
(inside the noise in 2 of those 24 squares). At 100 copies the test machine itself is the limit: GitHub's four-core
machine carries the real cluster and the model of up to 190,800 muscles at once, and native alone kept its CPU 87% to 91%
busy and failed 32% to 43% of requests. There the real service spent 8% to 13% less time over its line, and in the four
stacked and the whole tower at 100 repetitions the 95th percentile of its responses read LOSS (up 45% and 13.5%), with the
four stacked behind the window's clock in 49 of 100 repetitions. Those two squares are run again with a longer window
([`docs/GRID_LONG_WINDOW_PREREGISTRATION.md`](docs/GRID_LONG_WINDOW_PREREGISTRATION.md)), and on the new engine every
square runs again with the organism on its own core (protocol 3), so the machine no longer sets the result. The same report reads the organism's
modelled energy up (+0.06% at most, power given), with no extra modelled work for it, so the organism's work per energy
reads LOSS in 22 of the 36 squares of 10 and 100 repetitions; and, in 5 squares, 0.2% to 0.6% more copies of the service
(power given).

The lease handed every knob back to native in every run. On this version GitHub reproduced the realms table in runs A,
B and C (2,214 rows, 0 differences). **Goldilocks**, three runs of ten pairs (Omni-Compass on top of a service
rightsized by Goldilocks and the Vertical Pod Autoscaler's recommender; class L): the average response 44% to 48%
faster, the slowest 5% of responses 59% to 62% faster, time over the response line down 99% to 100%, GAIN in all three
of our runs, on the same machines, for 1.9% to 2.6% more energy on the declared model, the power given
([`results/live/V5_GOLDILOCKS.md`](results/live/V5_GOLDILOCKS.md)). **The capacity test**, three runs (the same CPU cap
in both arms, four cap levels): no row clear of the noise in all three runs at any cap, where the cap itself blocks the one
lever Omni-Compass has there, more copies of the service; read again by the rule of 24 October 2026 (a change of 0.5% or
more is a change), its eight rows read the runs disagree on six, LOSS on one (completed work at 1.5 cores, the same way in
all three runs, 0 of 3 clear of the noise) and GAIN on one (2 of 3 runs moved 0.5% or more, 0 of 3 clear of the noise)
([`results/live/V5_CAPACITY.md`](results/live/V5_CAPACITY.md)).
Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Ten organisms, two ways: the twenty scenarios** (our own models, class S, three runs, seeds 3000 to 3002,
[`results/scenarios/SCENARIOS_20.md`](results/scenarios/SCENARIOS_20.md), written by `python3 tools/scenarios_20.py`). The
seven organisms of the catalog, the orchestra (the governors' and orchestrators' muscles), the live engine's own sixty-muscle
organism and the whole organism in its three places (the software end, the cloud's wire, the bare metal) make ten organisms;
each is read native and with Omni-Compass on top of native: twenty scenarios. Every one of the nine modelled organisms reads
its muscles over the line GAIN in all three of our runs (from +1.58% in the whole tower to +63.34% in the orchestra), its work
EVEN; the orchestra's power is given (+52.38%) and the others' power EVEN or a cut. The whole organism, a composition of the
real tables, reads +14.5% GAIN by the index's rule. No LOSS row. The record of 24 October also carried a third way,
Omni-Compass by itself (each pool's own autoscaler switched off), which read LOSS in all three of our runs on work and on
muscles over the line in eight organisms, 32 rows; the founder's order of 25 October took that way out (Omni-Compass is never
by itself), and its record is kept whole in
[`docs/history/SCENARIOS_30_2026-10-24.md`](docs/history/SCENARIOS_30_2026-10-24.md).

## The manuals: the Operator's Manual, the Owner's Manual and the Live Engine Manual

[`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), the Operator's Manual, is the manual for the glove box, built from the
repository whenever it changes (`docs/book/build_book.py`): how to embed, wire, tune, run and check Omni-Compass on a
stacked, clustered system or on any one muscle. Front matter with the card for the glove box; the governor from the
outside and its factory tune; the plug and the rules its wires obey; the wiring level by level and stack by stack
(Kubernetes, databases, message brokers, caches, GPUs, the processor itself, the data center under the servers, robots
and drones); operating it; checking it on your own system; **the implementer's guide for the cloud** (Part VI, chapters
13 to 30: the path and its gates, least privilege, Azure, Google Cloud and Amazon step by step, the response-time feed,
the cloud mode, day two, the graphics processor, observability, change and risk, planning the saving before the run, own
racks and private clouds, hardening and the supply chain, a fleet under continuous delivery, the failure drill book, and
one installation start to finish); and back matter with every muscle, its wiring and its card, the install manifests,
the implementer's checklists, the governor's settings (the Kubernetes governor's and the two card governors'), the audit
record by record (every record of the governor, of the other muscles and of the card governors), the three clouds side by
side, every input of the paired run from GitHub, and the papers counsel asks for (the license, the licensing answers, the
third-party notices, the Enterprise License's standard terms, the patents and trademarks, the security policy). Since 16
October it also states the rules of the engine that stands as an operator meets them (section 6.5) and how a new muscle is
coded on the muscle SDK (section 5.7). It is 507 pages, with 50 figures drawn from the code by two kits (`docs/book/figures.py`,
`docs/book/schematics.py`; the drawings in `docs/book/figures/`): the plug, the band and the two forces, one decision of the
governor, the eight levels, the one pedal, the seven organisms and the three-run rule; a wiring schematic for every stack in
the grammar of an electrical drawing (the governor's sense and motor terminals, the kill switch, the plug, the native
controller, the muscle and the meters); the flowcharts of the wire check, the paired run, the eight phases, the release gate,
the three stops and the reading rule; the timing diagrams; and the state machines of the modes, the card governor and the life
of a muscle; and an index. The Owner's, which prints the engine's whole source and adds the engine's six states and its two
landscapes, the control-loop block diagrams, the modelled traces and every receipt of the engine that stands charted from its
own table (77 figures), is 1,657 pages (the engine's source appendix now carries the eight wires omni-v15 took into the fingerprint). All three books carry one numbering (chapter.section), and every cross-reference in
them is rewritten to it when the book is built and checked against the headings on the built PDF. Its text is
[`docs/OMNI_COMPASS_MANUAL.md`](docs/OMNI_COMPASS_MANUAL.md); the cloud install files are `deploy/install/`
(`omni-compass.yaml`, `rbac-machines.yaml`, `omni-compass-cloud.yaml`) and `deploy/Dockerfile.cloud`. It is written for the CTO who decides, the
engineer who wires and the operator who runs it; the published results are on this page and in `results/`.

[`docs/OMNI_COMPASS_OWNERS_MANUAL.pdf`](docs/OMNI_COMPASS_OWNERS_MANUAL.pdf), the Owner's Manual, is the master: everything
in one book, for whoever owns or licenses Omni-Compass and so must know the whole mechanism (the philosophy, the
mathematics, the mechanism, the engine that stands and the road to it, every Python file of the engine's source printed in
full, every result, the wiring, and every legal paper bound in). Its text is
[`docs/OMNI_COMPASS_OWNERS_MANUAL.md`](docs/OMNI_COMPASS_OWNERS_MANUAL.md).

[`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf`](docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf), the Live Engine Manual, is the third book (the
founder's order of 20 October: three in the end): nothing more than the interpretation of the live engine page,
[`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html), for the operator at the dashboard: how to
follow the wall and the switch, read every gauge and turn every knob, trace any tile to the record it came from, and see the
mechanism of action of Omni-Compass against native as the monitors show it (the two tickers, the phase plane, the brain's
state, the verdict), section by section in the page's own order, with what to do when a tile reads LOSS and what the page
does not tell you. It explains neither how the engine is built nor how it is wired; it is built by `docs/book/build_book.py
--live`, and its text is [`docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`](docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md). Its last appendix
is the page word for word, written from the page itself at every build (`docs/book/build_live_manual.py`): every section, every
monitor with its number, evidence class, feed and knobs, and every control, so the book and the page read each other both
ways; the control panel at the top of the live engine downloads all three books.

**The live engine page**, the tuning bench, opens on the bottom line, then the monitor wall and the main control panel. Native
is orange everywhere, Omni-Compass on native blue; red is never a side, only the alarm. Every
monitor carries its light and its word: green and round, **THRIVING** (working inside its lines with room to give, or a
GAIN); yellow, a yield diamond, **STEADY** (EVEN, inside 0.5%, or heading for its line and watched); red, a stop-sign octagon,
blinking, **REDLINING** (over its line, or a LOSS: the alarm); dark, **AWAITING** (the run that fills it has not landed; never
green). The main control panel holds the kill switch, the heartbeat's six buttons,
**10, 15, 30, 60, 90 and 120 s**, a sweep that runs every beat on the page's own model for three model days each, **Try the
candidate** (the sweep's best beat as a candidate profile), the active profile with its fingerprint (factory, candidate or
custom), **Restore factory profile**, **Hold the active profile** and **Return to native**. A model's best beat is a candidate
for the real runs, never a result, and no profile is locked as the baseline: the factory's beat stays 60 s until the eight
steps of [`docs/FACTORY_PROFILE.md`](docs/FACTORY_PROFILE.md) choose the next. At its back stand the glossary and index
(`tools/live_glossary.py`): every term in the words of the file it names, the ten organisms and their twenty scenarios, every
one of the 1,107 muscles of the catalog by realm and family, and the sections where each is used.

The engine is written twice, in Python and in C++ ([`cpp/`](cpp/)), line for line where a twin exists. The live engine's section 10b ([`#s-cpp`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html#s-cpp)) feeds the Python's own runs into the C++ at every rebuild and sets the two side by side, number by number: every twin's parity check, every compass law the page's runs wire, and every muscle of the seven organisms at the tune-down. The Python's 500 seeded runs (`tools/engine_runs.py`, the jump generator) run whole through the C++ harness too ([`cpp/tools/engine_runs.cpp`](cpp/tools/engine_runs.cpp): the Python's draws are the input, the governor, the nerves, the compass law and the verdict in C++ put the mechanism on): every receipt and the SHA-256 digest identical to the Python's, on GitHub with every set (`engine-runs`) and on the page's proof monitor ([`#proofPanel`](docs/engine/OMNI_COMPASS_LIVE_ENGINE.html#proofPanel)) beside the page's own run. What still runs in Python only is listed there by file (`tools/seal.py`).

## What is real and what is a model

| Evidence | What runs | Class |
|---|---|---|
| Real Kubernetes on GitHub | Kubernetes itself (API server, scheduler, its own autoscaler), a real web service, real requests, real response times and CPU. The machines are containers on one runner; energy there is a declared formula, not a meter | L |
| Real cloud, Azure AKS | All of the above on real Azure machines, Azure's own autoscaler, Azure's billed machine count | L |
| Real card, NVIDIA A10 on Lambda | The card's power limit and clocks, its own power meter, real GPU work. The first run (2026-10-02) used a card controller since replaced (it answered slower); the current controller's run is next | P |
| The 1,107 muscles | Software models of real control systems (AI serving, cooling, batteries, robot joints, grids), each from its maker's specification. They show the mechanism; they are labelled as models wherever they appear | S |

## Omni-Compass by itself: the organism run without Kubernetes (23 October)

Omni-Compass also runs the organism as its own orchestrator, with no Kubernetes or other orchestrator's code in it
([`docs/OMNI_ORCHESTRATOR.md`](docs/OMNI_ORCHESTRATOR.md), graded in [`docs/OMNI_ORCHESTRATOR_GRADES.md`](docs/OMNI_ORCHESTRATOR_GRADES.md)).
Three arms are always shown together: native (Kubernetes' published autoscaling rule on the muscles, written by us as the
yardstick), Omni on native (Omni on top of that rule) and Omni direct (Omni alone on the muscles). In the full form on one host
(one run of each arm, class L) Omni direct read against native by the one key: work GAIN (up 4.7%), the 95th percentile GAIN
(down 9.9%), units GAIN, a cut (down 10.3%), machines EVEN, nothing failed. The three arms together, quick form (one run each):
Omni on native against native, work GAIN (up 8.3%); Omni direct against native, work GAIN (up 9.1%); Omni direct against Omni
on native, the 95th percentile GAIN (down 13.2%) and units GAIN, a cut (down 9.5%); no LOSS in any pair, after the fault the
first three-arm showing found was fixed (a trial the traffic kept abandoning still cost a unit). The three-run reading on GitHub
(`orchestrator.yml`) has landed and is the bottom line at the top of this page: both Omni-Compass arms against native read work
GAIN and the 95th percentile GAIN in all three of our runs, and no pair reads LOSS on any gauge
([`results/orchestrator/V18_THREE_ARMS_ABC.md`](results/orchestrator/V18_THREE_ARMS_ABC.md)). Why a muscle reads EVEN and where the room is, in theory and mathematics: [`docs/THE_ROOM.md`](docs/THE_ROOM.md).

## How it works

Omni-Compass is a supervisory governor. It does not replace your autoscaler or your firmware: it sits on top, reads
the meters of each muscle (response time, utilisation, power, heat), and by default runs **at the max**: every muscle
pushed to its own limit, never past it and never below native, riding the edge of its band, not the middle. It starts
machines before the rush lands and clears work waiting in line, cools a room ahead of the heat, holds a battery's
charge for the line, and runs an axis at its own peak while tasks wait. The energy that takes is **power given**, shown
beside the work, the speed and the wear it bought; inside a body (an organism) it gives only what the body's lines can
carry. One pedal: push for more, lift off for less, and lifting hands the setting back toward native; at idle
the pool lifts to its floor of two machines, powered and ready. If Omni-Compass stops, the plug walks every setting back
to native; the kill switch, a separate security switch, turns it off everywhere at once. Anyone can tune it down from
the max on the dial. The law, its
proof and its wiring: [`docs/MECHANISM_OF_ACTION.md`](docs/MECHANISM_OF_ACTION.md),
[`docs/TRACKING_THEOREM.md`](docs/TRACKING_THEOREM.md), [`docs/CONVEYANCE_LAW.md`](docs/CONVEYANCE_LAW.md).

**Where the benefit is taken, and why nobody babysits it.** On machines already paid for (your own racks, a chip at its heat
line) the max takes the benefit as more work from the same machines; in a chip the aim is more work at native's own
heat, never hotter. In a
public cloud the benefit is the bill: there the governor moves the machines alone (pods, processor limits and power stay
native's) and parks only machines the cloud already made, so the bill can only fall or stay, never rise. Either way it runs on autopilot, self-running, self-steering and self-auditing like a
self-driving car: nobody turns a knob, nobody checks its work and nobody has to react; every change is the governor's own, logged with its reason, made as the
reading approaches the line rather than after it is crossed; every Kubernetes and cloud receipt
counts the babysitting tax in both arms (the alert minutes an on-call page would be open, and the commands the governor
wrote on its own).

## Check it yourself

```
pip install -r requirements.txt && python verify.py      # must end: VERIFICATION: PASS
bash scripts/run_live_local.sh 3                          # native against omni on your own kind cluster
sudo bash scripts/gpu_rented_run.sh                       # the card run, on any rented NVIDIA machine
```

`verify.py` reruns every held-out result byte for byte, the Python and C++ twins, the property tests, and checks that
the repository is lined up (`tools/layout_check.py`). Every live result carries its raw files and SHA-256 digests.

The raw files of the live runs (about 36 GB, 182,161 files) live on their own branch, `raw`, from 18 October: main holds the
code and the tables, so a clone of main is small and every table, page, manual and the verifier work without the raw
files. Opened, the branch sits at `results/live/raw/`, so every path a table names (`results/live/raw/run-<id>/...`) reads as
written; only the folders asked for are downloaded:

```
git clone https://github.com/The-Omni-Compass-LLC/The-Omni-Compass && cd The-Omni-Compass
bash scripts/raw_archive.sh open /run-<id>/            # one run's raw files, when wanted (more patterns: more runs)
```

From 17 October the archive stores the bulk no table reads once a run has made its own tables (YCSB's raw latencies,
the request logs, the Kafka consumer logs) gzipped; read one with `gunzip -c FILE.gz`, and its hash stands in the run's
`SHA256SUMS_ALL.txt`.

## Read next

| For | Read |
|---|---|
| **The register: every muscle wired, every benchmark run, every benchmark still to run** | [`docs/REGISTER.md`](docs/REGISTER.md) |
| **The proof program: every benchmark at full size, every open native engine, the referee-grade package** | [`docs/PROOF_PROGRAM.md`](docs/PROOF_PROGRAM.md) |
| **The engine that stands, omni-v21, fingerprinted; Omni-Compass by itself; Omni direct and the three arms; the v5 law at the max, the bone, the lease, the dial** | [`docs/OMNI_V19.md`](docs/OMNI_V19.md), [`docs/OMNI_V18.md`](docs/OMNI_V18.md), [`docs/OMNI_V17.md`](docs/OMNI_V17.md), [`docs/OMNI_V16.md`](docs/OMNI_V16.md), [`docs/OMNI_V15.md`](docs/OMNI_V15.md), [`docs/OMNI_V14.md`](docs/OMNI_V14.md), [`docs/OMNI_V13.md`](docs/OMNI_V13.md), [`docs/OMNI_V5.md`](docs/OMNI_V5.md), `python3 tools/omni_version.py` (the earlier engines stay with their own results as the road to 1.0: [`docs/history/`](docs/history/)) |
| **The heartbeat dial: every beat of the governor beside native, what it buys and what it costs** | [`results/model_gate/V17_LADDER.md`](results/model_gate/V17_LADDER.md), [`docs/PACE_PREREGISTRATION.md`](docs/PACE_PREREGISTRATION.md), on the live engine page, the page's section 1j |
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) |
| Every level on one page: the muscle, the organism, the cluster, its add-ons, the service, the plant, the cloud, a group of clusters; any level whose gauges go the other way, named | [`docs/LEVELS.md`](docs/LEVELS.md) (`python3 tools/levels.py`) |
| The method, written before each run | [`docs/K8S_COMPASS_PREREGISTRATION.md`](docs/K8S_COMPASS_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](docs/INTEGRATION_MANUAL.md) |
| The 1,107 muscles, and how to wire every family on your own stack | [`docs/MUSCLE_CATALOG.md`](docs/MUSCLE_CATALOG.md), [`realms/catalog_v5.csv`](realms/catalog_v5.csv), [`docs/wiring_recipes.csv`](docs/wiring_recipes.csv) |
| Every command on one page | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the compass law (`compass_law.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_compass.py`) |
| `cpp/` | The C++ twins, sealed equal to the Python laws |
| `realms/` | The 1,107-muscle catalogue, its models and the v5 law at the max (`compass_arm_v5.py`) |
| `scripts/`, `deploy/`, `.github/workflows/` | The benchmarks: kind, AKS, the card, eight cards |
| `tools/` | Report builders, the Omni index, the layout check |
| `results/` | Every result with its raw files and digests |
| `docs/` | Results, method, manual, due diligence |
| `tests/` | The tests `verify.py` runs |

## Find it

Omni-Compass is a **supervisory governor**: a control plane that sits on top of a native controller and never replaces it.
People searching for any of these should find this page: supervisory governor, supervisory control, control plane,
governor, controller, autoscaler, autoscaling, Kubernetes HPA, cluster autoscaler, Karpenter, KEDA, node pool, right-sizing,
conveyance, machinery, engine control, power cap, clock ceiling, DVFS, cpufreq, RAPL, GPU power limit, energy efficiency,
energy per unit of work, data center efficiency, PUE, green computing, FinOps, SRE, SLO, p95, tail latency, do no harm,
paired trial, A/B/C replication, preregistration, Redis maxmemory, Kafka consumer group, PostgreSQL pooler, MySQL buffer
pool, MongoDB WiredTiger cache, HVAC setpoint, building management, chiller plant, UPS, PDU, battery management, microgrid,
grid tap changer, voltage regulator, wind turbine pitch, pipeline compressor, water pump scheduling, robot servo, drone
autopilot, flight software, autonomous driving stack, 5G RAN scheduler, matching engine, game server fleet, build farm,
ledger node, IDS workers, control theory, closed loop, two antagonist forces, tanh law, nervous system, muscles, realms,
organisms, Omni index. The repository's GitHub topics (set by its owner from the About panel, with www.omni-compass.com as its website): `omni-compass`, `governor`, `supervisory-control`, `control-plane`, `control-core`, `control-engine`, `control-theory`, `control-systems`, `feedback-control`, `conveyance`, `machinery`, `autoscaling`, `kubernetes`, `gpu`, `data-center`, `energy-efficiency`, `power-management`, `smart-grid`, `robotics`, `industrial-automation`.

## Contact

The Omni-Compass LLC, main office infrastructure. Toll-free direct: **1-888-339-9551**. System route asset:
**1-888-DEX-YLL-1**. Landline, registered in Florida: **321-746-4411**. [www.omni-compass.com](https://www.omni-compass.com)

What the letters mean at Omni-Compass, read in order, the way the engine runs:

| DEX | YLL | 1 |
|---|---|---|
| **Data Exchange**: the input. In software, data exchange is how one system's readings reach another. Here it is the two-way plug, one wire in and one wire out: the system's own readings come in, Omni-Compass's settings go out. | **Yield Limit Line**: the boundary. In engineering science, the yield limit is the most load a material can carry and still spring back unharmed; past it, the damage is permanent. Omni-Compass runs every muscle up to its own yield limit line, read live, and never past it. | **1**: the output. In code, 1 is true, the finished state; in science, 1 is unity, the whole. Here it is one closed loop: one body, one brain, every result read back and the next step decided from it. |

Read as one sentence: Omni-Compass takes the system in through a Data Exchange (DEX), runs every setting up to its Yield Limit Line (YLL) and never past it, and closes it all into one loop (1). Science and software people read each part on sight.

## License

**Proprietary. Evaluation and Simulation use only.** You may download, run and modify the software only to evaluate
it and to reproduce the published results, including in shadow or test mode on systems you own or control. Everything
else requires a written **Omni-Compass Enterprise License** signed by The Omni-Compass LLC and paid for. No patent or
trademark license is granted for any other use.

| File | What it says |
|---|---|
| [`LICENSE`](LICENSE) | Evaluation and Simulation use only; everything else needs a signed, paid Omni-Compass Enterprise License |
| [`NOTICE`](NOTICE) | copyright, the US filings notice, third-party notices |
| [`PATENTS.md`](PATENTS.md) | the nonprovisional utility patent application "The Omni-Compass" filed in the United States (title, inventor, date; the number is withheld on purpose); no patent license is granted |
| [`TRADEMARKS.md`](TRADEMARKS.md) | the Omni-Compass marks; trademark applications filed in the United States |
| [`DISCLOSURES.md`](DISCLOSURES.md) | every declaration, disclosure and disclaimer, made once |
| [`LICENSING_FAQ.md`](LICENSING_FAQ.md) | licensing in plain answers |
| [`.github/CLA.md`](.github/CLA.md) | contributions are assigned to The Omni-Compass LLC |
| [`REUSE.toml`](REUSE.toml), [`sbom/`](sbom), [`.fossa.yml`](.fossa.yml) | machine-readable license declarations for scanners |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
