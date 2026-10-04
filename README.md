# Omni-Compass

**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. Not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) and [`DISCLOSURES.md`](DISCLOSURES.md).

The Omni-Compass LLC · [www.omni-compass.com](https://www.omni-compass.com)

## The result

Omni-Compass on top of native Kubernetes, real clusters, paired runs, the same work sent to both sides:

| | Native | Native + Omni-Compass | Reading |
|---|---:|---:|---|
| **Work handled inside the response line** (capacity test, 10 pairs) | 16.2 req/s | **24.0 req/s** | **+48% more work** on the same machines |
| **Response time, 95th percentile** (sets 22-27, 10 pairs each) | 285-414 ms | 114-185 ms | **55-65% faster** |
| **Machines in service** (sets 22-27) | 6 | 3.8-4.3 | **29-36% fewer machines** |
| **Energy** (every test) | | | **equal or lower** in every test |
| **Failed requests** (sets 22-27) | 0 | 0 | none lost |

**The Omni index, every real test together: +15.0%** more for the same, or the same for less, across work, speed,
machines and energy (real Kubernetes +23.1%, Azure +7.5%). Every number is read from each test's own result file by
[`tools/omni_index.py`](tools/omni_index.py): [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md).

Six organisms with the real cluster inside (the four realms, the whole tower of 656 muscles, the four stacked, 1,226):
late 23-52% less often and 24-40% faster in every one ([`results/live/SIX_KUBE.md`](results/live/SIX_KUBE.md)).

## What is real and what is a model

| Evidence | What runs | Class |
|---|---|---|
| Real Kubernetes on GitHub | Kubernetes itself (API server, scheduler, its own autoscaler), a real web service, real requests, real response times and CPU. The machines are containers on one runner; energy there is a declared formula, not a meter | L |
| Real cloud, Azure AKS | All of the above on real Azure machines, Azure's own autoscaler, Azure's billed machine count | L |
| Real card, NVIDIA A10 on Lambda | The card's power limit and clocks, its own power meter, real GPU work. The first run (2026-10-02) used a card controller since replaced (it answered slower); the current controller's run is next | P |
| The 656 muscles | Software models of real control systems (AI serving, cooling, batteries, robot joints, grids), each from its maker's specification. They show the mechanism; they are labelled as models wherever they appear | S |

## Check it yourself

```
pip install -r requirements.txt && python verify.py      # must end: VERIFICATION: PASS
bash scripts/run_live_local.sh 3                          # native against native + Omni-Compass on your own kind cluster
sudo bash scripts/gpu_rented_run.sh                       # the card run, on any rented NVIDIA machine
```

`verify.py` reruns every held-out result byte for byte, the Python and C++ twins, the property tests, and checks that
the repository is lined up (`tools/layout_check.py`). Every live result carries its raw files and SHA-256 digests.

## How it works

Omni-Compass is a supervisory governor. It does not replace your autoscaler or your firmware: it sits on top, reads
the meters of each muscle (response time, utilisation, power, heat), holds each muscle's own setting in the middle of
its band with one bounded law, and hands every setting back the moment it stops. As demand rises, the warm machines
take it first; as it falls, the emptiest machine idles first, powered and ready, never switched off. The law, its
proof and its wiring: [`docs/MECHANISM_OF_ACTION.md`](docs/MECHANISM_OF_ACTION.md),
[`docs/TRACKING_THEOREM.md`](docs/TRACKING_THEOREM.md), [`docs/CONVEYANCE_LAW.md`](docs/CONVEYANCE_LAW.md).

## Read next

| For | Read |
|---|---|
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) |
| The method, written before each run | [`docs/K8S_BOWL_PREREGISTRATION.md`](docs/K8S_BOWL_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](docs/INTEGRATION_MANUAL.md) |
| The 656 muscles | [`docs/MUSCLE_CATALOG.md`](docs/MUSCLE_CATALOG.md) |
| Every command on one page | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the bowl law (`bowl.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_bowl.py`) |
| `cpp/` | The C++ twins, sealed equal to the Python laws |
| `realms/` | The 656-muscle catalogue and its models |
| `scripts/`, `deploy/`, `.github/workflows/` | The benchmarks: kind, AKS, the card, eight cards |
| `tools/` | Report builders, the Omni index, the layout check |
| `results/` | Every result with its raw files and digests |
| `docs/` | Results, method, manual, due diligence |
| `tests/` | The tests `verify.py` runs |

## License

**Proprietary. Evaluation and simulation use only.** You may download, run and modify the software only to evaluate
it and to reproduce the published results, including in shadow or test mode on systems you own or control. Everything
else requires a written **Omni-Compass Enterprise License** signed by The Omni-Compass LLC and paid for. No patent or
trademark license is granted for any other use.

| File | What it says |
|---|---|
| [`LICENSE`](LICENSE) | evaluation and simulation use only; everything else needs a signed, paid Omni-Compass Enterprise License |
| [`NOTICE`](NOTICE) | copyright, the US filings notice, third-party notices |
| [`PATENTS.md`](PATENTS.md) | patent applications filed in the United States; no patent license is granted |
| [`TRADEMARKS.md`](TRADEMARKS.md) | the Omni-Compass marks; trademark applications filed in the United States |
| [`DISCLOSURES.md`](DISCLOSURES.md) | every declaration, disclosure and disclaimer, made once |
| [`LICENSING_FAQ.md`](LICENSING_FAQ.md) | licensing in plain answers |
| [`.github/CLA.md`](.github/CLA.md) | contributions are assigned to The Omni-Compass LLC |
| [`REUSE.toml`](REUSE.toml), [`sbom/`](sbom), [`.fossa.yml`](.fossa.yml) | machine-readable license declarations for scanners |

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
