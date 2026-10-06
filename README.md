# Omni-Compass

**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. Not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) and [`DISCLOSURES.md`](DISCLOSURES.md).

The Omni-Compass LLC · [www.omni-compass.com](https://www.omni-compass.com)

**Two names only: native is the system as it runs on its own; omni is Omni-Compass on top of native.** Omni-Compass
never replaces native; every comparison below is native against omni.

## The result

Omni-Compass on top of native Kubernetes, real clusters, ten paired runs per test, on **Omni v1**, the frozen and
fingerprinted engine ([`docs/OMNI_V1.md`](docs/OMNI_V1.md)). Every test ran three times as separate GitHub runs (A the
result, B and C the replications); a reading below is **confirmed** only when it holds in all three runs with every 95%
interval clear of zero, and otherwise reads no difference beyond the noise. The six tables:
[`V1_ALL_FOUR`](results/live/V1_ALL_FOUR.md), [`V1_STEADY`](results/live/V1_STEADY.md),
[`V1_WANDERING`](results/live/V1_WANDERING.md), [`V1_FAULTS`](results/live/V1_FAULTS.md),
[`V1_BATCH`](results/live/V1_BATCH.md), [`V1_FAIRNESS`](results/live/V1_FAIRNESS.md).

| | native (run A) | omni (run A) | Reading over the three runs |
|---|---:|---:|---|
| **Work handled inside the response line** (all four in one run) | 18.6 req/s | **27.6 req/s** | **+42% to +48% more work on the same machines, confirmed better** |
| **Response time, 95th percentile** (steady, wandering, all four, faults) | 361-830 ms | 122-321 ms | **−57% to −69% in every run of all four tests, confirmed better** |
| **Failed requests** (wandering, all four) | 10.5-13.3% | 9.3-11.7% | **−12% to −13%, confirmed better**; zero in both arms at steady load; under faults no difference beyond the noise |
| **Machines in service** | 6 | 5.88 (steady), 4.6 (batch) | steady **−1.5% to −3.4%** and batch **−15% to −24%, confirmed better**; the other tests no difference beyond the noise |
| **Energy** (a declared model: on kind the machines are containers on one runner, so a machine out of service saves modelled watts, not a metered bill) | | | standby model confirmed lower in steady (−1.0 to −2.9%), batch (−11 to −17%) and wandering (−0.4 to −0.8%); elsewhere no difference beyond the noise |
| **A noisy neighbour on the same workers** (fairness) | | | no difference beyond the noise on every row: Omni neither helps nor hurts |
| **Pods left with no machine to take them** | 0 | 0 | same, in every test |

Omni gives a machine back only after a paired trial shows the service is no slower without it (the verdict). On these
clusters one machine fewer made each request 30-45% slower in most trials, so Omni kept the machines and spent them on
speed and work. Earlier engines without that check parked 29-36% of the machines (`docs/history/`); the frozen engine
puts work and speed first.

**What this does and does not show.** The product gain measured so far is more work inside the response line on the same
machines, 34-52% across the three capacity runs on earlier engines ([`CAPACITY`](results/live/CAPACITY.md) +34.1%,
[`CAPACITY_2`](results/live/CAPACITY_2.md) +51.9%, [`ALL_FOUR`](results/live/ALL_FOUR.md) +41.7%), with a faster tail; the
v1 runs give one engine's number three times. Not yet shown: an energy or cloud-bill saving on real machines (Azure's bill
did not move on the earlier engine, [`AKS_BILL`](results/live/AKS_BILL.md); the v1 Azure runs are in progress), and the
current card governor on a real GPU (the one real-card run, on the governor since replaced, saved 1.6-3.5% of the card's
energy and made its 95th percentile 43-84% slower:
[`HIL_RESCORED`](results/hil/run-20261002T082232Z/HIL_RESCORED.md)).

**The Omni index, every real test together: +12.9%** more for the same, or the same for less, across work, speed,
machines and energy (real Kubernetes +18.5%; Azure +7.5%). The index still reads the earlier engine's result files; it is
rebuilt from the v1 tables once the Azure v1 runs land. Every number is read from each test's own result file by
[`tools/omni_index.py`](tools/omni_index.py):
[`results/OMNI_INDEX.md`](results/OMNI_INDEX.md). Each test: [`STEADY`](results/live/STEADY.md),
[`WANDERING`](results/live/WANDERING.md), [`ALL_FOUR`](results/live/ALL_FOUR.md), [`FAULTS`](results/live/FAULTS.md),
[`FAIRNESS`](results/live/FAIRNESS.md).

Six organisms with the real cluster inside (the four realms, the whole tower of 656 muscles, the four stacked, 1,226),
on an earlier engine: late 23-52% less often and 24-40% faster in every one
([`results/live/SIX_KUBE.md`](results/live/SIX_KUBE.md)); the rerun at 1, 10, 100 and 1,000 copies on the frozen
engine is running.

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
bash scripts/run_live_local.sh 3                          # native against omni on your own kind cluster
sudo bash scripts/gpu_rented_run.sh                       # the card run, on any rented NVIDIA machine
```

`verify.py` reruns every held-out result byte for byte, the Python and C++ twins, the property tests, and checks that
the repository is lined up (`tools/layout_check.py`). Every live result carries its raw files and SHA-256 digests.

## How it works

Omni-Compass is a supervisory governor. It does not replace your autoscaler or your firmware: it sits on top, reads
the meters of each muscle (response time, utilisation, power, heat), holds each muscle's own setting in the middle of
its band with one bounded law, and hands every setting back the moment it stops. As demand rises, the warm machines
take it first; as it falls, the emptiest machine idles first, powered and ready, never switched off, and never below a floor of two (idle). The reset hands every setting back at
the end of a run; the kill switch, a separate security switch, turns Omni-Compass off everywhere at once. The law, its
proof and its wiring: [`docs/MECHANISM_OF_ACTION.md`](docs/MECHANISM_OF_ACTION.md),
[`docs/TRACKING_THEOREM.md`](docs/TRACKING_THEOREM.md), [`docs/CONVEYANCE_LAW.md`](docs/CONVEYANCE_LAW.md).

## Read next

| For | Read |
|---|---|
| **The register: every muscle wired, every benchmark run, every benchmark still to run** | [`docs/REGISTER.md`](docs/REGISTER.md) |
| **Omni v1: the frozen engine, fingerprinted; which version every result ran on; how each is confirmed three times** | [`docs/OMNI_V1.md`](docs/OMNI_V1.md), `python3 tools/omni_version.py` |
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) |
| The method, written before each run | [`docs/K8S_COMPASS_PREREGISTRATION.md`](docs/K8S_COMPASS_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](docs/INTEGRATION_MANUAL.md) |
| The 656 muscles | [`docs/MUSCLE_CATALOG.md`](docs/MUSCLE_CATALOG.md) |
| Every command on one page | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the compass law (`compass_law.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_compass.py`) |
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
