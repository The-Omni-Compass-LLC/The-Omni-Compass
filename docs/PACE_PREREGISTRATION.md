# Preregistration: the decision pace of the Kubernetes governor (omni-v16)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Written and committed before the runs, on the founder's word of 22 October ("Go"). The runs' commit is the one that
carries this file; nothing in the engine, the harness or this rule changes after the first run starts.

## The question

How often should the Kubernetes governor take its full decision? Every engine through omni-v15 decided every 60 s: the
period was written into the first harness on 26 September, with no reason recorded, and never measured against another.
Native's pod autoscaler checks every 15 s (the controller manager's `--horizontal-pod-autoscaler-sync-period`), the
metrics it reads refresh every 15 s, the Cluster Autoscaler scans every 10 s and KEDA every 30 s. The founder asked for
15, 10 and 5 s on 14 October; until now the period was not a clean setting, because rules counted in decisions changed
their meaning with it.

omni-v16 (`docs/OMNI_V16.md`, on main since 22 October) counts every clock of the governor in seconds, so the period changes
only how often it looks: the brain's own minute (its blending of each reading, its inner time, its dwell and waits, its
machines added or removed a minute), the compass's damping and smoothing, the edge's window and rates, the coast per
raise, the additions past the scheduling floor (a step a minute), a command's minute to land, the host's busy share
over a minute, the heat law's minute, one batch job a minute, the conveyance every 15 s whichever check falls due, and
the loop that keeps its own schedule (`tests/test_pace_clocks.py`, `tests/test_loop_schedule.py`). At 60 s it makes
exactly omni-v15's decisions (the toy cluster, 4,578 records, none different); the conveyance's 15 s and the loop's
schedule are the only changes a run at 60 s can see.

## What was read first, in our own models (class S)

The toy gate, before any run (`results/toy_gate/V16_VS_V15.md`, `results/toy_gate/V16_PACE.md`): omni-v16 against omni-v15
on every toy, and omni-v16 alone at 60, 15, 10 and 5 s on a plant that moves every 5 s, in the cloud's
setting and in this benchmark's. A pace that reads a LOSS there is not run here.

## What is run

Workflow `benchmark-reps` on `main` (omni-v16), three runs (A, B and C) of 10 repetitions each, on GitHub's own
machines (no cost), released by the grid conductor as the campaign's entry `kubernetes decision pace`
(`scripts/reruns.txt`, in the first block, right after the steady test: its A with the first pass, its B and C with the
next two). Each repetition runs five arms back to back on the same runner, each on a fresh kind cluster, in an
order rotated by repetition (`scripts/kind_paired.sh`):

| Arm | What governs |
|---|---|
| native | Kubernetes alone (the HPA at its target, the scheduler); Omni-Compass not started |
| compass | Omni-Compass on top of native, the compass law at the max, at its default heartbeat: a full decision every 15 s (amendment 2) |
| compass60 | the same, a full decision every 60 s, every engine's period before omni-v16 |
| compass10 | the same, a full decision every 10 s |
| compass5 | the same, a full decision every 5 s |

The fast checks (the scheduling floor, the pod reflex, and the conveyance every 15 s) run every 5 s in every Omni arm.
The load is the reruns' steady scenario: 900 measured seconds an arm, a fixed rate (`loadgen=open`), the same work in
every arm; the line 500 ms at the 95th percentile. Each Omni arm ends with the reset, which must return every setting to
native with no record left (`scripts/kind_bench.sh`).

## How each pace is read

By the one key (`tools/readings.py`), from the three runs' receipts (`tools/live_reps.py`, `tools/confirm_abc.py`): each
pace against native, and each other pace against the compass arm at its default of 15 s, paired within the repetition. A row reads GAIN or LOSS
only when all three runs agree in sign with every 95% interval clear of zero; EVEN when an interval includes zero; and
"the runs disagree" when clear runs point different ways. A resource that rises (pods, machines, energy, the settings
commands, the governor's own processor) is power given, never a LOSS; it is shown and named.

## The rule that picks the default (frozen now)

The default becomes the fastest pace that meets all four:

1. In the toy gate, no LOSS at that pace.
2. Against native: no row reads LOSS.
3. Against the 60 s arm: no row of work done, time waited, missed or failed reads LOSS or "the runs disagree".
4. Omni-Compass's own processor at that pace (the receipt's "Omni's own CPU (cores)", from the overhead record every
   Omni arm writes) stays under 0.1 of one core, a fortieth of the runner's four.

If no faster pace meets all four, the default stays 60 s, as omni-v16 landed it. A faster default is the next version,
omni-v17, under the standing rule (tested in the toy first, told, not asked), and every benchmark runs again on it.

## What does not change

Native's own clocks, the harness, the scenario and every other rule. The cloud sets (Azure, Google, Amazon) are not part
of this choice, because they cost money; they run at whatever default lands.

## Threats to validity

- One scenario (steady, fixed-rate load) on kind: one runner whose nodes are containers on one host. A pace chosen here
  is the default everywhere until a scenario reads a LOSS at it, and then it is root-caused like any other.
- Below 15 s the processor numbers the governor reads repeat (metrics-server refreshes every 15 s): part of what is
  measured, not corrected for.
- The runs share GitHub's runners with the campaign; each repetition pairs its five arms on one runner at one time, so
  the queue changes no comparison.

## Amendment 1 (22 October, written before any run): how rule 1 reads the toy

Rule 1 reads each pace as every toy gate reads a candidate: against the engine that stands at its default, here omni-v16
deciding every 60 s, paired by seed (`results/toy_gate/`); the paired reading is what says whether a pace adds anything. The
toy's rows against native are printed beside them in full (`results/toy_gate/V16_PACE.md`), and a row there that reads LOSS
goes to the next version's list (`docs/CHANGE_CONTROL.md`) to be root-caused as the engine's: it is the engine's trade at
every pace, the default included. Written once the toy had read, before the first run, because "no LOSS at that pace" could
be read either way: in the cloud's setting the pods wait for a machine longer than native's at every pace, the default
included (pending pod minutes an hour: native 8.2, every 60 s 20.9, every 15, 10 and 5 s 18.4, 15.9 and 16.5), a reading of
EVEN at 60 and 10 s and of LOSS at 15 and 5 s only because the seeds' spread differs, while against the 60 s default each
faster pace reads EVEN. The reading kept is the toy gate's own, the one every version since 15 October was landed by.

## Amendment 2 (22 October, written before any run): the founder sets the heartbeat at 15 s

Once the toy had read (`results/toy_gate/V16_PACE.md`: against 60 s, no LOSS at any pace in either setting; at 15 s the alert
minutes 14.7% fewer in this benchmark's setting and energy per core 2.6% less in the cloud's), the founder's word was "15 sec
all over heart beat fix update code". The default is therefore 15 s from omni-v16 on, set by him and not by this rule, and the
rule above no longer picks it: omni-v16 lands with its full decision every 15 s, not at the 60 s the rule above first left it. The runs stay as written, with the arms around the default: native, the compass arm at 15 s,
and the same at 60, 10 and 5 s (the table above, written before the first run). They read the heartbeat he set: each pace
against native, and 60, 10 and 5 s against 15 s. A row that reads LOSS at 15 s, against native or (on work done, time waited,
missed or failed) against 60 s, is root-caused and fixed in the next version, and he hears it, as every other.

## Amendment 3 (22 October, afternoon, written before any omni-v17 run): the beat a dial, the main engine at 60 s

The founder's word the same afternoon, once he had read the reads a day in the pace study (about 86,000 at 5 s against 39,700
at 60 s): the heartbeat is a dial. Any beat can be set, and every setting is shown beside native with what it buys and what
it costs, because an operator may want a fast beat for its reads and accept what it costs, or a slow one, and each beat may
want its own combination of the other knobs. The main engine decides every 60 s (omni-v17, `docs/OMNI_V17.md`). No rule picks
a default from these runs: he set it. No omni-v16 run of this entry had started when this was written.

The runs on omni-v17 carry eight arms in every repetition, in an order rotated by repetition, on the same runner:

| Arm | What governs |
|---|---|
| native | Kubernetes alone (the HPA at its target, the scheduler); Omni-Compass not started |
| compass | Omni-Compass on top of native, the compass law at the max, at the main engine's beat: a full decision every 60 s |
| compass5, compass15, compass30 | the same, a full decision every 5, 15 and 30 s |
| compass75, compass90, compass120 | the same, a full decision every 75, 90 and 120 s |

Everything else stands as written above: the fast checks every 5 s in every Omni arm, the steady load, the line, the reset.
Each beat is read against native and against the compass arm at 60 s, paired within the repetition, by the one key, three
runs of 10 repetitions; a repetition's job may run four hours (`.github/workflows/benchmark-reps.yml`). A row that reads LOSS
at any beat against native is the engine's at that beat: it is named on the dial's page (the live engine page, "The heartbeat
dial") and root-caused like any other, in the toy first. The seven beats were read first in our own models
(`results/toy_gate/V17_LADDER.md`), and that reading found one fault before the version landed: at 90 and 120 s the cruise
wait (120 s) had rounded to one decision, so one reading with a pod waiting put every machine in service. omni-v17 carries the
fix (the cruise wait never fewer than two readings; `docs/OMNI_V17.md`, section 3), so the compass90 and compass120 arms run
the corrected rule; every other arm's counts are unchanged by it.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
