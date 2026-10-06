# Omni v1: the frozen engine, and every result checked against it

> © 2026 The Omni-Compass LLC. Evaluation and simulation use only. See LICENSE.

## What is frozen

Omni v1 is the engine as it stands at commit `a004a8f` and is unchanged through `f162ce8`. It covers:

- the compass law (`omnicompass/compass_law.py`);
- the live controllers (`omni_controller/`);
- the realms with their 656 muscles and six organisms (`realms/`);
- the runners of the independent simulators (`tools/run_kil.py`, `tools/run_citylearn.py`, `tools/run_pandapower.py`).

`OMNI_V1.json` holds one SHA-256 for each of these 38 files, plus one digest over all of them: `ccc7fbdf8b312ed7…`.

```
python3 tools/omni_version.py                    # this checkout: prints "omni-v1", or every file that differs
python3 tools/omni_version.py --commit <sha>     # the engine at the commit any result ran on
```

A result counts as a v1 result only if the commit it ran on carries exactly these bytes. Every GitHub Actions run
records its commit, so anyone can check any result in one command.

## What is the same in every muscle, and what is not

The law is one function. It reads the service as a position between calm (0) and its line (1). It pulls the position
toward the middle and pushes against whatever is driving it. Its force is smoothed by tanh, and past the wall it goes
to full force at once. The gains are the same on every muscle: pull 1.0, add 0.10, take back 0.02, release −0.2.

Results differ from domain to domain for three declared reasons, never because the gains were changed per domain:

1. **The machine underneath** (`realms/presets.py`): boot time, idle and peak power, heat capacity, battery size,
   motor torque. These are fixed engineering figures for the class of machine.
2. **The room native leaves.** Omni can only win back what the native controller wastes.
3. **The guard rules each live adapter carries**, all listed in the preregistrations:
   - Kubernetes: rules 1–8 and amendments 9 and 12;
   - the grid: one whole tap per move, and a week of evidence before stepping down.

   Some knobs are left native by a physics test computed from the machine's own figures (`MECHANISM_OF_ACTION.md`
   §9.6), such as a power cap where idle power dominates, or a UPS reserve.

## The change rule

v1 does not change. A new rule, a new gain or a new guard makes a new version (v2) with its own fingerprint, and every
result is run again on it. No result is ever read across versions.

## Every result, by version

**Status of each result**

| Result | Ran on | v1? | v1 run |
|---|---|---|---|
| Kubernetes: fairness (`results/live/FAIRNESS.md`) | `3539036` | no | **A, B, C done: [`V1_FAIRNESS.md`](../results/live/V1_FAIRNESS.md)** |
| Kubernetes: faults (`results/live/FAULTS.md`) | `3539036` | no | **A, B, C done: [`V1_FAULTS.md`](../results/live/V1_FAULTS.md)** |
| Kubernetes: steady (`results/live/STEADY.md`) | `3539036` | no | A and C done, B finishing its last pair; table to follow |
| Kubernetes: wandering, all four (`results/live/WANDERING.md`, `ALL_FOUR.md`) | `3539036` | no | A and B done, C running; tables to follow |
| Kubernetes: batch queue (`results/live/BATCH.md`) | `a0ebaff` | no | A and B done, C running; table to follow |
| Kubernetes: the six organisms with the real cluster inside (1 to 1,000 copies) | `a004a8f` | **yes** | running (run 37359815637) |
| Kubernetes: the big organisms | `a004a8f` | **yes** | running (run 37359820055) |
| Azure AKS steady (`AKS_BILL.md`) | `5b2832f` | no | dispatched after the running burst |
| Azure AKS burst | `8199e3a` | no | queued after v1 steady |
| The 656 muscles and six organisms, modelled (`results/realms/`) | `9c5d417` | **yes** | **A, B, C done**: runs 37359815637's realms check, 37385660330 and 37393204931 each reproduced the published table byte for byte (a deterministic model: reproduced in 3 of 3) |
| The organisms at 1 / 10 / 100 / 1,000 copies, modelled (`results/scale/GRID.md`) | `a8548b6` | no | to run after the six-kube queue clears |
| CityLearn, every district | `ac39b16` | no | A done (run 37384954241: 12 districts ran, 3 have no battery to move, 8 CityLearn cannot run), B running, C to follow; table by `tools/citylearn_abc.py` |
| Power grid, pandapower and SimBench | `8eab01c` | **yes** | running (run 37377029333) |
| GPU, one card and the card in the organisms | earlier card controller | no | new runs on real cards (founder) |
| Muscle studies, power budgets, PlanetLab fleet, tower off and on | September engines | no | marked old |

## How each result is confirmed

Every v1 benchmark runs three times, as separate GitHub Actions runs on the same frozen bytes:

- **A** is the result.
- **B** and **C** are the replications.

Every judged row gets one of three readings, and all three runs are shown beside it:

- **Confirmed better** or **confirmed worse**: the same sign in all three runs, each with its 95% interval clear of zero.
- **No difference beyond the noise**: in at least one run the interval includes zero, so native and omni could not be
  told apart on that measure. That is the result, stated as such, with the count of runs it holds in.
- **The runs disagree**: runs clear of the noise point different ways. The test itself is then unstable on that measure,
  and it is looked into before anything is claimed.

Every row is reported, losses included.

The table is made by rule, never by hand:

```
python3 tools/confirm_abc.py "Steady load" results/live/raw/run-<A> results/live/raw/run-<B> results/live/raw/run-<C> \
    --out results/live/V1_STEADY.md
```

It checks each run's commit against the v1 fingerprint, and heads the table with a warning if any run is not v1 or if the
three are not separate runs. CityLearn has its own table (`tools/citylearn_abc.py`): the simulator is deterministic, so
its three runs must reproduce each other, and a score reads confirmed better or worse by its sign when they do, same under
one part in a million, and "the runs differ" when they do not; a district with no electric battery is listed as nothing
for Omni to move, and a district CityLearn cannot run is listed with CityLearn's own error. `tests/test_confirm_abc.py`, run by `verify.py`, proves the rule: an interval over zero
reads no difference beyond the noise, a flipped sign clear of the noise reads disagreement, a rounding-level change reads
same, and a loss in all three reads WORSE.
