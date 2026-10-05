# The Omni index: more for the same, or the same for less

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Every measure of every test is a ratio oriented so that above 1 is better for Omni-Compass on top of native: work (more is better), speed (a lower response time), machines (fewer), energy (less). A test's index is the geometric mean of its ratios; a category is the geometric mean of its tests; the headline is the geometric mean of the real categories, each weighted the same. Modelled muscles are shown beside it, never inside it. Every number is read from the test's own result file (`tools/omni_index.py`).

## Headline: Omni-Compass on top of native, real machines: **+15.4%** (more for the same, or the same for less, across work, speed, machines and energy)

| Category | Index | Work | Speed | Machines | Energy | Tests |
|---|---:|---:|---:|---:|---:|---:|
| Real Kubernetes (GitHub) | **+23.9%** | +5.9% | +87.6% | +16.8% | +0.3% | 16 |
| Real cloud (Azure AKS, billed) | **+7.5%** | +0.0% | +25.4% | -0.8% |  | 1 |
| Real card (NVIDIA, its own meter) | pending | | | | | the rerun on the current card controller (the 2026-10-02 run used the replaced one) |
| Modelled muscles (evidence S) | **+0.1%** | +0.0% |  |  | +0.1% | 6 |

Read: +10% in a column means 10% better for Omni-Compass in that measure (more work, a faster answer, fewer machines, less energy). The energy figure on GitHub's Kubernetes is a declared model, not a meter; Azure's machines are its own billed count.

## Every test

| Category | Test | Index | Work | Speed | Machines | Energy | Source |
|---|---|---:|---:|---:|---:|---:|---|
| Real Kubernetes (GitHub) | Set 22: same work, ten pairs | **+38.9%** | +0.0% | +156.9% | +44.9% | +0.1% | `results/live/LIVE_REPS_22.md` |
| Real Kubernetes (GitHub) | Set 23: same work, ten pairs | **+38.8%** | +0.0% | +164.4% | +40.2% | +0.2% | `results/live/LIVE_REPS_23.md` |
| Real Kubernetes (GitHub) | Set 24: same work, ten pairs | **+38.5%** | +0.0% | +150.6% | +46.3% | +0.3% | `results/live/LIVE_REPS_24.md` |
| Real Kubernetes (GitHub) | Set 25: same work, ten pairs | **+36.5%** | +0.0% | +134.2% | +47.8% | +0.4% | `results/live/LIVE_REPS_25.md` |
| Real Kubernetes (GitHub) | Set 26: same work, ten pairs | **+36.8%** | +0.0% | +124.3% | +55.8% | +0.1% | `results/live/LIVE_REPS_26.md` |
| Real Kubernetes (GitHub) | Set 27: same work, ten pairs | **+35.6%** | +0.0% | +113.1% | +57.8% | +0.5% | `results/live/LIVE_REPS_27.md` |
| Real Kubernetes (GitHub) | Capacity: load rising, ten pairs | **+31.9%** | +48.1% | +101.1% | +1.4% | +0.3% | `results/live/AMENDMENT_3_RUNS.md` |
| Real Kubernetes (GitHub) | Fairness: a noisy neighbour, ten pairs | **-0.3%** | not taken | -1.0% | +0.0% | +0.2% | `results/live/AMENDMENT_3_RUNS.md` |
| Real Kubernetes (GitHub) | Faults: machine down, spike, runaway pod, blind probe, ten pairs | **+39.1%** | not taken | +168.2% | +0.2% | +0.2% | `results/live/AMENDMENT_3_RUNS.md` |
| Real Kubernetes (GitHub) | All four in one run: load up and down one step at a time, ten pairs | **+37.5%** | +29.3% | +165.5% | +3.7% | +0.3% | `results/live/ALL_FOUR.md` |
| Real cloud (Azure AKS, billed) | Steady load, Azure's autoscaler underneath, five pairs | **+7.5%** | +0.0% | +25.4% | -0.8% | not taken | `results/live/AKS_BILL.md` |
| Real Kubernetes (GitHub) | Six organisms: Compute / AI / Cloud, the cluster inside, five pairs | **+11.1%** | +1.9% | +49.6% | +0.0% | +0.1% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Compute / AI / Cloud: the modelled stacks around the real cluster | **+0.0%** | +0.0% | not taken | not taken | +0.1% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: Physics / Robotics / Autonomous, the cluster inside, five pairs | **+9.3%** | +0.8% | +38.1% | +2.2% | +0.2% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Physics / Robotics / Autonomous: the modelled stacks around the real cluster | **+0.0%** | +0.0% | not taken | not taken | +0.1% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: Energy / Facility / Industrial, the cluster inside, five pairs | **+7.8%** | +0.5% | +31.6% | +1.9% | +0.3% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Energy / Facility / Industrial: the modelled stacks around the real cluster | **+0.1%** | +0.0% | not taken | not taken | +0.2% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: Distribution / Specialized, the cluster inside, five pairs | **+10.6%** | +2.0% | +45.6% | +0.1% | +0.6% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | Distribution / Specialized: the modelled stacks around the real cluster | **+0.0%** | +0.0% | not taken | not taken | +0.1% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: the whole tower (656), the cluster inside, five pairs | **+15.5%** | +4.2% | +67.2% | +1.7% | +0.3% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | the whole tower (656): the modelled stacks around the real cluster | **+0.1%** | +0.0% | not taken | not taken | +0.2% | `results/live/SIX_KUBE.json` |
| Real Kubernetes (GitHub) | Six organisms: the four stacked (1,226), the cluster inside, five pairs | **+8.9%** | +6.1% | +32.1% | +0.0% | +0.2% | `results/live/SIX_KUBE.json` |
| Modelled muscles (evidence S) | the four stacked (1,226): the modelled stacks around the real cluster | **+0.1%** | +0.0% | not taken | not taken | +0.2% | `results/live/SIX_KUBE.json` |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
