# Omni-Compass full benchmark harness

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Before you wire anything:** read [`DISCLOSURES.md`](../DISCLOSURES.md). Omni-Compass acts only through the wires it is given; it cannot be slapped on. If your paired receipts differ from the published benchmarks in direction, the first presumption is wiring: confirm the installation with section 8.5 of the manual (*Wired right or wired wrong*).

This tree is the GitHub-ready kit: frozen engine + C++ twin + two plants + live stub.

## What to run

```bash
pip install -r requirements.txt
python verify.py --quick          # engine, C++, soak, parity
python k8s_controlplane/test_controlplane.py
python -m k8s_controlplane.suite  # elastic / always_on / idle_power
python tests/test_hpa_three_way.py
python tests/test_omni_controller.py
```

The machine's own power (the Linux frequency governor as native, Omni on the frequency ceiling, energy from the processor's
meter; root on a machine on the metal, not a virtual one; `docs/CPU_POWER_PREREGISTRATION.md`):

```bash
sudo python3 tools/run_cpu_power.py --probe            # can this machine run it?
sudo bash scripts/cpu_power_run.sh                     # the three workloads, native and omni, three repetitions; one folder
python3 tools/cpu_power_abc.py A B C --out V3_CPU_POWER.md   # three runs into the table
```

Fleet plant (Omni as node authority vs HPA+CA / Karpenter-lite):

```bash
python -m fleet.planetlab --dir fleet/traces/planetlab --scenarios 8 --out /tmp/pl
```

C++:

```bash
cmake -S cpp -B cpp/build -DCMAKE_BUILD_TYPE=Release && cmake --build cpp/build -j2
./cpp/build/oc_smoke
```

## Two plants (do not mix the tables)

| Tree | What Omni is | What the energy number means |
|---|---|---|
| `k8s_controlplane/` | On top of HPA+CA (target / gate / park) | Pack and optional CA gate on a 20-node replica |
| `fleet/` | Node-pool authority; CA off | Consolidation vs CA and Karpenter-lite |

Observe must match the native arm on that plant. If it does not, the run is invalid.

## Engine species

Shipped `omnicompass/core.py` is the patent principal form: cubic \(U(1-U^2)\), FIG. 4 command, RK4 with held \(u\).
`omnicompass/pools.py` is actuation only (off / hold / park). It does not change the field.

## Not in this harness

Live kube-controller-manager, kind CI, GPU MIG scheduler, facility cooling plant.
`omni_controller/` is observe-first against kubectl; tests use `tests/fake_cluster/kubectl`.

See `LIMITS.md`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
