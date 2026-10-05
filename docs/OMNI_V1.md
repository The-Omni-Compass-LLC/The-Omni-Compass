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
| Kubernetes: steady, wandering, all four, fairness, faults (`results/live/*.md`) | `3539036` | no | replication A, dispatched on `f162ce8` |
| Kubernetes: batch queue | `a0ebaff` | no | replication A, dispatched |
| Kubernetes: the six organisms with the real cluster inside (1 to 1,000 copies) | `a004a8f` | **yes** | running (run 37359815637) |
| Kubernetes: the big organisms | `a004a8f` | **yes** | running (run 37359820055) |
| Azure AKS steady (`AKS_BILL.md`) | `5b2832f` | no | dispatched after the running burst |
| Azure AKS burst | `8199e3a` | no | queued after v1 steady |
| The 656 muscles and six organisms, modelled (`results/realms/`) | `9c5d417` | **yes** | replication B to run |
| The organisms at 1 / 10 / 100 / 1,000 copies, modelled (`results/scale/GRID.md`) | `a8548b6` | no | to run after the six-kube queue clears |
| CityLearn, every district | `ac39b16` | no | replication A, dispatched |
| Power grid, pandapower and SimBench | `8eab01c` | **yes** | running (run 37377029333) |
| GPU, one card and the card in the organisms | earlier card controller | no | new runs on real cards (founder) |
| Muscle studies, power budgets, PlanetLab fleet, tower off and on | September engines | no | marked old |

## How each result is confirmed

Every v1 benchmark runs three times, as separate GitHub Actions runs on the same frozen bytes:

- **A** is the result.
- **B** and **C** are the replications.

A claim is confirmed only when it holds in all three: the same sign and the 95% interval clear of zero in each. If any
replication disagrees, the claim is reported as not confirmed, with all three tables shown. Every row is reported,
losses included.
