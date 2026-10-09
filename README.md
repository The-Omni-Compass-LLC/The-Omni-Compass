# Omni-Compass

**More work, faster, on fewer machines, with less energy, on top of the stack you already run.**

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. Not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) and [`DISCLOSURES.md`](DISCLOSURES.md).

The Omni-Compass LLC · [www.omni-compass.com](https://www.omni-compass.com)

**Two names only: native is the system as it runs on its own; omni is Omni-Compass on top of native.** Omni-Compass
never replaces native; every comparison below is native against omni.

## The result

Omni-Compass on top of native Kubernetes, real clusters, ten paired runs per test, on **Omni v3**, the frozen and
fingerprinted engine ([`docs/OMNI_V3.md`](docs/OMNI_V3.md): v1's law and controllers byte for byte, the muscle catalog grown to 945 and a do-no-harm gate on speed knobs; the v1 tables, [`docs/OMNI_V1.md`](docs/OMNI_V1.md), read the same and stay as the first engine's record). Every test ran three times as separate GitHub runs (A the
result, B and C the replications); a reading below is **confirmed** only when it holds in all three runs with every 95%
interval clear of zero, and otherwise reads no difference beyond the noise. The six tables:
[`V3_ALL_FOUR`](results/live/V3_ALL_FOUR.md), [`V3_STEADY`](results/live/V3_STEADY.md),
[`V3_WANDERING`](results/live/V3_WANDERING.md), [`V3_FAULTS`](results/live/V3_FAULTS.md),
[`V3_BATCH`](results/live/V3_BATCH.md), [`V3_FAIRNESS`](results/live/V3_FAIRNESS.md).

| | native (run A) | omni (run A) | Reading over the three runs |
|---|---:|---:|---|
| **Work handled inside the response line** (all four in one run) | 21.0 req/s | **31.2 req/s** | **+35% to +49% more work on the same machines, confirmed better** |
| **Response time, 95th percentile** (steady, wandering, all four, faults) | 321-820 ms | 111-306 ms | **−47% to −66% in every run of all four tests, confirmed better** |
| **Failed requests** (wandering, all four) | 8.9-12.3% | 7.7-10.9% | **−9% to −14%, confirmed better**; zero in both arms at steady load; under faults lower in all three, clear of the noise in one |
| **Machines in service** | 6 | 5.90 (steady), 4.89 (batch) | steady **−1.5% to −2.9%** and batch **−19% to −23%, confirmed better**; the other tests no difference beyond the noise |
| **Energy** (a declared model: on kind the machines are containers on one runner, so a machine out of service saves modelled watts, not a metered bill) | | | standby model confirmed lower in steady (−1.3% to −2.1%) and batch (−13% to −16%); elsewhere no difference beyond the noise |
| **A noisy neighbour on the same workers** (fairness) | | | no difference beyond the noise on every row, the neighbour's own service included: Omni neither helps nor hurts |
| **Pods left with no machine to take them** | 0 | 0 | same, in every test |

Omni gives a machine back only after a paired trial shows the service is no slower without it (the verdict). On these
clusters one machine fewer made each request 30-45% slower in most trials, so Omni kept the machines and spent them on
speed and work. Earlier engines without that check parked 29-36% of the machines (`docs/history/`); the frozen engine
puts work and speed first.

**What this does and does not show.** The product gain measured so far is more work inside the response line on the same
machines, 34-52% across the three capacity runs on earlier engines ([`CAPACITY`](results/live/CAPACITY.md) +34.1%,
[`CAPACITY_2`](results/live/CAPACITY_2.md) +51.9%, [`ALL_FOUR`](results/live/ALL_FOUR.md) +41.7%), with a faster tail; the
v1 runs give one engine's number three times. Not yet shown: an energy or cloud-bill saving on real machines (Azure's bill
did not move on the earlier engine, [`AKS_BILL`](results/live/AKS_BILL.md), nor on v1's steady run, [`V1_AKS_STEADY`](results/live/V1_AKS_STEADY.md): every gauge inside the noise; the v1 burst is running), and the
current card governor on a real GPU (the one real-card run, on the governor since replaced, saved 1.6-3.5% of the card's
energy and made its 95th percentile 43-84% slower:
[`HIL_RESCORED`](results/hil/run-20261002T082232Z/HIL_RESCORED.md)).

**The Omni index, every real test together: +20.5%** more for the same, or the same for less, across work, speed,
machines and energy, six real categories each weighed the same: real Kubernetes on v3 +28.8% over seven tests (work +19%, speed +107%,
machines +5%, energy +2%); the real database on v3 +4.0% (on the second counted set: connections held open −36% to −38% on
the read-only workload with CPU and latency inside the noise; the first set's CPU cost was our own harness, measured and
removed, and its table is kept in the history; on the slow write workload the add rule buys connections above the operator's
setting, confirmed worse and counted against it); real messaging on v3, Apache Kafka, +166.9% (work inside the line +17%; a 95th
percentile of 1.6 s against 9 to 14 ms, because native's queue grew at nine tenths of its capacity and Omni's did not;
consumers held 2 → 6 to 8, confirmed worse and counted against it); and the real cache on v3, Redis, **−24.9%** (work inside
the line +14% to +27% and the hit rate +14% to +27%, confirmed better; the memory ceiling held 64 → 200 to 270 MB,
confirmed worse, the resource the gain costs, which outweighs the gain in the geometric mean; CPU inside the noise); and
the real database's storage-engine cache on v3, MongoDB under YCSB, **+8.5%** (the second counted set: the cache given back
by a quarter to a third on all four untouched workloads, confirmed better, with work, p95, mean latency and CPU inside the
noise; the first set's larger saving came from a cold cache emptied before its first eviction and cost latency, and it is
kept in the history); and the real database's buffer pool on v3, MySQL under sysbench, **+5.2%** (the third counted set:
the pool held −49% to −56% on burst, confirmed better; on read_write the pages the pool holds +44% to +52%, confirmed worse,
with the host's CPU −4% to −6%, confirmed better, a trade; read_only inside the noise and update_index disagreeing; the pool
handed back on all 45 omni arms; the two earlier sets kept whole in the history). Only a
row confirmed in all three runs enters; a row inside the noise counts as exactly zero. Azure's billed runs and the card
join the index when their three-run tables land (the earlier engine's +12.9% is kept in
`docs/history/OMNI_INDEX_pre_v1.md`). Every number is read from each test's own table by
[`tools/omni_index.py`](tools/omni_index.py): [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md).
Each test: [`V3_STEADY`](results/live/V3_STEADY.md), [`V3_WANDERING`](results/live/V3_WANDERING.md),
[`V3_ALL_FOUR`](results/live/V3_ALL_FOUR.md), [`V3_FAULTS`](results/live/V3_FAULTS.md), [`V3_FAIRNESS`](results/live/V3_FAIRNESS.md),
[`V3_BATCH`](results/live/V3_BATCH.md), [`V3_PGBENCH`](results/live/V3_PGBENCH.md), [`V3_KAFKA`](results/live/V3_KAFKA.md),
[`V3_REDIS`](results/live/V3_REDIS.md), [`V3_YCSB`](results/live/V3_YCSB.md).

Six organisms with the real cluster inside (the four realms, the whole tower of 945 muscles, the four stacked, 1,716),
on an earlier engine: late 23-52% less often and 24-40% faster in every one
([`results/live/V1_SIX_KUBE.md`](results/live/V1_SIX_KUBE.md), v1; the earlier engine's in [`results/live/SIX_KUBE.md`](results/live/SIX_KUBE.md)); on v3 at 10 and 100 copies every
cell is better on 4 to 6 gauges and worse on none beyond the noise but a rounding-level work loss in 4 of 12
([`results/live/V3_SIX_KUBE.md`](results/live/V3_SIX_KUBE.md)); the 1,000-copy cells run on Azure: the tower
on v1 ([`results/live/V1_BIG_ORGANISM.md`](results/live/V1_BIG_ORGANISM.md)) answered its slowest 5% in 0.2 s against native's
4.1 s and was over its line 0.2% of the time against 64%; the four stacked on v3
([`results/live/V3_BIG_ORGANISM.md`](results/live/V3_BIG_ORGANISM.md), 1.7 million muscles on one clock with the cluster
inside, three repetitions on a rented machine with a 10,800 s window) answered their slowest 5% in 150 ms against native's
2.9 s, were over the line 0% of the time against 51%, failed no request against 0.14%, on the same six machines and the
same energy inside the noise, both arms on the clock. A cell whose machine could not step the organism inside its window
is marked off the clock in the report and run again with a longer window.

## What is real and what is a model

| Evidence | What runs | Class |
|---|---|---|
| Real Kubernetes on GitHub | Kubernetes itself (API server, scheduler, its own autoscaler), a real web service, real requests, real response times and CPU. The machines are containers on one runner; energy there is a declared formula, not a meter | L |
| Real cloud, Azure AKS | All of the above on real Azure machines, Azure's own autoscaler, Azure's billed machine count | L |
| Real card, NVIDIA A10 on Lambda | The card's power limit and clocks, its own power meter, real GPU work. The first run (2026-10-02) used a card controller since replaced (it answered slower); the current controller's run is next | P |
| The 945 muscles | Software models of real control systems (AI serving, cooling, batteries, robot joints, grids), each from its maker's specification. They show the mechanism; they are labelled as models wherever they appear | S |

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
| **The proof program: every benchmark at full size, every open native engine, the referee-grade package** | [`docs/PROOF_PROGRAM.md`](docs/PROOF_PROGRAM.md) |
| **Omni v3, v2 and v1: the frozen engines, fingerprinted; which version every result ran on; how each is confirmed three times** | [`docs/OMNI_V3.md`](docs/OMNI_V3.md), [`docs/OMNI_V2.md`](docs/OMNI_V2.md), [`docs/OMNI_V1.md`](docs/OMNI_V1.md), `python3 tools/omni_version.py` |
| Every result, every platform, where each stands | [`docs/STATE_OF_PLAY.md`](docs/STATE_OF_PLAY.md), [`results/OMNI_INDEX.md`](results/OMNI_INDEX.md) |
| How to read a result table | [`docs/HOW_TO_READ_THE_RESULTS.md`](docs/HOW_TO_READ_THE_RESULTS.md) |
| The method, written before each run | [`docs/K8S_COMPASS_PREREGISTRATION.md`](docs/K8S_COMPASS_PREREGISTRATION.md), [`docs/GPU_PREREGISTRATION.md`](docs/GPU_PREREGISTRATION.md), [`docs/REALMS_PREREGISTRATION.md`](docs/REALMS_PREREGISTRATION.md) |
| A referee's checklist | [`docs/REFEREE_CHECKLIST.md`](docs/REFEREE_CHECKLIST.md) |
| Every claim with its evidence class, losses kept | [`docs/EVIDENCE_LEDGER.md`](docs/EVIDENCE_LEDGER.md), [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) |
| Due diligence | [`docs/DUE_DILIGENCE.md`](docs/DUE_DILIGENCE.md) |
| The manual (wiring, operating, every result) | [`docs/OMNI_COMPASS_MANUAL.pdf`](docs/OMNI_COMPASS_MANUAL.pdf), [`docs/INTEGRATION_MANUAL.md`](docs/INTEGRATION_MANUAL.md) |
| The 945 muscles | [`docs/MUSCLE_CATALOG.md`](docs/MUSCLE_CATALOG.md) |
| Every command on one page | [`docs/HANDOFF.md`](docs/HANDOFF.md) |

## Repository

| Path | What it is |
|---|---|
| `omnicompass/` | The engine (`core.py`), the compass law (`compass_law.py`), the verdict, the shield, the master switch |
| `omni_controller/` | The live controllers: Kubernetes (`controller.py`) and the card (`gpu_compass.py`) |
| `cpp/` | The C++ twins, sealed equal to the Python laws |
| `realms/` | The 945-muscle catalogue and its models (Omni v2) |
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
| [`PATENTS.md`](PATENTS.md) | the nonprovisional utility patent application "The Omni-Compass" filed in the United States (title, inventor, date; the number is withheld on purpose); no patent license is granted |
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
