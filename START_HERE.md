# START HERE

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).

Omni-Compass is software that sits **on top of** the controllers a system already has (the GPU's firmware, the
Kubernetes autoscaler, a building's thermostats) and governs every layer under one law, so the machines and the power
already paid for do more work. Every result here is Omni-Compass on top of a native system against the same native
system alone, with the same work in both.

## Read in this order

| # | Read | What it gives you |
|---|---|---|
| 1 | [`README.md`](README.md) | what Omni-Compass is, the license, the repository at a glance |
| 2 | [`docs/OMNI_COMPASS_MANUAL.md`](docs/OMNI_COMPASS_MANUAL.md), section 3 | the problem we attack, the product, the benefit and its arithmetic, how to read a receipt, the two modes |
| 3 | [`docs/OMNI_COMPASS_MANUAL.md`](docs/OMNI_COMPASS_MANUAL.md), section 15 | every result to date, with its class and its source |
| 4 | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) | every table, column by column |
| 5 | [`DISCLOSURES.md`](DISCLOSURES.md) | the one rule (nothing more than 2% worse, only where energy or the bill is saved), the limits, what is modelled and what is metered |
| 6 | [`docs/K8S_BOWL_PREREGISTRATION.md`](docs/K8S_BOWL_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) | every test written down before it ran, every change and why |
| 7 | [`docs/book/THEORY.md`](docs/book/THEORY.md), [`docs/book/DECLARATION.md`](docs/book/DECLARATION.md) | the Unified Circle Principle, the four-piece engine, the physics |
| 8 | [`docs/specs/`](docs/specs/) | the contracts: causal authority, GPU physical evidence, RAPL, the universal muscle SDK, the proof map |

## The receipts

| What | Where |
|---|---|
| Real Kubernetes (sets 29 to 31, fault tests, cost to match, capacity) | [`results/live/`](results/live/) |
| The six organisms, 1x to 1,000x clusters | [`results/scale/GRID.md`](results/scale/GRID.md), [`results/scale/receipts/`](results/scale/receipts/) |
| GPU cards (modelled and real) | [`results/sim/gpu_two_wire/`](results/sim/gpu_two_wire/), [`results/gpu/`](results/gpu/) |
| Every check of the repository, in one file | [`results/VERIFY_RECEIPT.txt`](results/VERIFY_RECEIPT.txt) (`python3 verify.py --quick` reproduces it) |

## Run it yourself

| On | How |
|---|---|
| Any computer, no GPU | `python3 verify.py --quick` (every test and check, about 10 minutes) |
| One NVIDIA GPU | [`docs/GPU_RUN_GUIDE.md`](docs/GPU_RUN_GUIDE.md), section C: `sudo bash scripts/gpu_rented_run.sh` |
| An 8-GPU server | the same guide, section D: `sudo POOLED=1 bash scripts/gpu_8card.sh` (hard time budget built in) |
| Kubernetes | GitHub Actions, workflow `benchmark-reps` (kind), or `aks-metered` on your Azure account ([`docs/AZURE_SETUP.md`](docs/AZURE_SETUP.md)) |
| The six organisms at any size | `bash scripts/grid_one_machine.sh` on one machine, or the `six` workflow |

The master switch stops every Omni-Compass governor at once and hands every knob back: `python3 tools/omni_switch.py off`.

## History

Earlier sets, superseded runs and experiments from earlier packages are kept, unchanged, so anyone can check any old
number: earlier receipts in [`results/`](results/) and the packages in [`archive/`](archive/).

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See [`LICENSE`](LICENSE)
and [`NOTICE`](NOTICE).*
