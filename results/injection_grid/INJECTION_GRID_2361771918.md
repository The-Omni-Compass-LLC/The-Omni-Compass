# The injection grid: the Python's 500 injections through every organism and every governor (modelled)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (our own models). The batch: base **2361771918**, 500 injections, injection k's seed seed_k = base + k·0x9E3779B9 mod 2^32; the Python's runs of it digest `8c00d97063b8cf61…` (`results/engine_runs/ENGINE_RUNS_500_2361771918.json`), the C++ engine's `8c00d97063b8cf61…` (the same, 500 runs agree). Engine **omni-v21**, commit `b8673f438d18`, run 2026-10-30 09:08 UTC, 0 s on 4 processes. Written by `python3 tools/injection_grid.py`; every cell's every gauge, and every run's change, in `injection_grid/INJECTION_GRID_2361771918.json`.

**How it is built.** run k of a cell stacks M copies, copy c on injection k + c (mod 500); the copies are separate clusters on one clock; every gauge per muscle (the work index, the share of muscles over the line, the power per muscle; a governor's way per muscle of the organism and the governor's body together) and the mean of the copies'; each run's change per decision against its reference over 24 blocks of ten decisions with its 95% interval (Student t); the cell's word by the founder's rule of 24 October over its N runs (tools/readings.py three_run_reading). The whole organism is a composition of real measured tables (tools/whole_system.py) and takes no injection; tools/scenarios_20.py reads it, native and with Omni-Compass on native.

## Omni-Compass on native against native, every organism, every cell

Each cell: work · muscles over the line · power, the mean change of its runs and its word (the number carries the word's sign).

| Organism | Muscles | 1 run × 1 org. | 10 runs × 1 org. | 100 runs × 1 org. | 500 runs × 1 org. | 1 run × 10 org. | 10 runs × 10 org. | 100 runs × 10 org. | 500 runs × 10 org. | 1 run × 100 org. | 10 runs × 100 org. | 100 runs × 100 org. | 500 runs × 100 org. | 1 run × 500 org. | 10 runs × 500 org. | 100 runs × 500 org. | 500 runs × 500 org. |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| The spine | 267 | EVEN =0.00% · GAIN +7.42% · EVEN =0.44% | EVEN =0.00% · GAIN +7.60% · EVEN =0.40% | EVEN =0.00% · GAIN +7.57% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% | EVEN =0.00% · GAIN +7.60% · EVEN =0.40% | EVEN =0.00% · GAIN +7.57% · EVEN =0.41% | EVEN =0.00% · GAIN +7.56% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% | EVEN =0.00% · GAIN +7.57% · EVEN =0.42% | EVEN =0.00% · GAIN +7.56% · EVEN =0.42% | EVEN =0.00% · GAIN +7.67% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% | EVEN =0.00% · GAIN +7.71% · EVEN =0.42% |
| Compute / AI / Cloud | 540 | EVEN =0.00% · GAIN +6.43% · EVEN =0.49% | EVEN =0.00% · GAIN +6.77% · EVEN =0.48% | EVEN =0.00% · GAIN +6.72% · EVEN =0.49% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% | EVEN =0.00% · GAIN +6.77% · EVEN =0.48% | EVEN =0.00% · GAIN +6.72% · GAIN +0.51% | EVEN =0.00% · GAIN +6.71% · EVEN =0.49% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% | EVEN =0.00% · GAIN +6.71% · EVEN =0.49% | EVEN =0.00% · GAIN +6.71% · EVEN =0.49% | EVEN =0.00% · GAIN +6.77% · GAIN +0.50% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% | EVEN =0.00% · GAIN +6.83% · GAIN +0.51% |
| Physics / Robotics / Autonomous | 404 | EVEN =0.00% · GAIN +3.19% · EVEN =0.23% | EVEN =0.00% · GAIN +3.14% · EVEN =0.23% | EVEN =0.00% · GAIN +3.13% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.14% · EVEN =0.23% | EVEN =0.00% · GAIN +2.98% · EVEN =0.24% | EVEN =0.00% · GAIN +3.13% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.13% · EVEN =0.24% | EVEN =0.00% · GAIN +3.13% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% | EVEN =0.00% · GAIN +3.19% · EVEN =0.24% |
| Energy / Facility / Industrial | 480 | EVEN =0.00% · GAIN +2.56% · EVEN =0.00% | EVEN =0.00% · GAIN +2.45% · EVEN =0.00% | EVEN =0.00% · GAIN +2.53% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% | EVEN =0.00% · GAIN +2.46% · EVEN =0.00% | EVEN =0.00% · GAIN +2.49% · EVEN =0.00% | EVEN =0.00% · GAIN +2.54% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% | EVEN =0.00% · GAIN +2.53% · EVEN =0.00% | EVEN =0.00% · GAIN +2.54% · EVEN =0.00% | EVEN =0.00% · GAIN +2.61% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% | EVEN =0.00% · GAIN +2.60% · EVEN =0.00% |
| Distribution / Specialized | 484 | EVEN =0.00% · GAIN +7.20% · EVEN =0.18% | EVEN =0.00% · GAIN +7.01% · EVEN =0.16% | EVEN =0.00% · GAIN +6.97% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% | EVEN =0.00% · GAIN +7.03% · EVEN =0.16% | EVEN =0.00% · GAIN +6.93% · EVEN =0.17% | EVEN =0.00% · GAIN +6.96% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% | EVEN =0.00% · GAIN +6.97% · EVEN =0.16% | EVEN =0.00% · GAIN +6.96% · EVEN =0.16% | EVEN =0.00% · GAIN +7.00% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% | EVEN =0.00% · GAIN +7.04% · EVEN =0.16% |
| The four stacked | 1,908 | EVEN =0.00% · GAIN +4.62% · EVEN =0.00% | EVEN =0.00% · GAIN +4.62% · EVEN =0.00% | EVEN =0.00% · GAIN +4.60% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% | EVEN =0.00% · GAIN +4.63% · EVEN =0.00% | EVEN =0.00% · GAIN +4.55% · EVEN =0.00% | EVEN =0.00% · GAIN +4.61% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% | EVEN =0.00% · GAIN +4.61% · EVEN =0.00% | EVEN =0.00% · GAIN +4.61% · EVEN =0.00% | EVEN =0.00% · GAIN +4.66% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% | EVEN =0.00% · GAIN +4.68% · EVEN =0.00% |
| The whole tower | 1,107 | EVEN =0.00% · GAIN +1.27% · EVEN =0.00% | EVEN =0.00% · GAIN +1.21% · EVEN =0.00% | EVEN =0.00% · GAIN +1.26% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% | EVEN =0.00% · GAIN +1.21% · EVEN =0.00% | EVEN =0.00% · GAIN +1.23% · EVEN =0.00% | EVEN =0.00% · GAIN +1.27% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% | EVEN =0.00% · GAIN +1.26% · EVEN =0.00% | EVEN =0.00% · GAIN +1.27% · EVEN =0.00% | EVEN =0.00% · GAIN +1.31% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% | EVEN =0.00% · GAIN +1.30% · EVEN =0.00% |
| The orchestra | 55 | EVEN =0.04% · GAIN +61.27% · power given +48.99% | EVEN =0.11% · GAIN +61.56% · power given +53.09% | EVEN =0.13% · GAIN +63.23% · power given +54.30% | EVEN =0.14% · GAIN +62.68% · power given +53.86% | EVEN =0.11% · GAIN +61.15% · power given +53.22% | EVEN =0.16% · GAIN +61.63% · power given +52.27% | EVEN =0.14% · GAIN +62.89% · power given +54.07% | EVEN =0.14% · GAIN +62.41% · power given +53.81% | EVEN =0.13% · GAIN +62.83% · power given +54.26% | EVEN =0.14% · GAIN +62.85% · power given +54.06% | EVEN =0.13% · GAIN +62.82% · power given +53.73% | EVEN =0.14% · GAIN +62.38% · power given +53.80% | EVEN =0.14% · GAIN +62.38% · power given +53.80% | EVEN =0.14% · GAIN +62.38% · power given +53.80% | EVEN =0.14% · GAIN +62.38% · power given +53.80% | EVEN =0.14% · GAIN +62.38% · power given +53.80% |
| The live engine's organism | 60 | EVEN =0.00% · GAIN +4.87% · EVEN =0.00% | EVEN =0.00% · GAIN +4.78% · EVEN =0.00% | EVEN =0.00% · GAIN +4.29% · EVEN =0.00% | EVEN =0.00% · GAIN +4.34% · EVEN =0.00% | EVEN =0.00% · GAIN +4.72% · EVEN =0.00% | EVEN =0.00% · GAIN +3.73% · EVEN =0.00% | EVEN =0.00% · GAIN +4.26% · EVEN =0.00% | EVEN =0.00% · GAIN +4.31% · EVEN =0.00% | EVEN =0.00% · GAIN +4.27% · EVEN =0.00% | EVEN =0.00% · GAIN +4.25% · EVEN =0.00% | EVEN =0.00% · GAIN +4.28% · EVEN =0.00% | EVEN =0.00% · GAIN +4.30% · EVEN =0.00% | EVEN =0.00% · GAIN +4.30% · EVEN =0.00% | EVEN =0.00% · GAIN +4.30% · EVEN =0.00% | EVEN =0.00% · GAIN +4.30% · EVEN =0.00% | EVEN =0.00% · GAIN +4.30% · EVEN =0.00% |

## Every way on each organism at 500 runs × 1 organism, ranked by work, then by muscles over the line

The governor's way is the organism with the governor's body on its clock, on the same injections; Omni-Compass on top of the governor is both with Omni-Compass on top. Read against native, the organism alone.

**The spine**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power GAIN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power GAIN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power GAIN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power GAIN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power GAIN); 23 more in the record

**Compute / AI / Cloud**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power GAIN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power GAIN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power GAIN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power GAIN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power GAIN); 23 more in the record

**Physics / Robotics / Autonomous**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power GAIN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power GAIN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power GAIN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power GAIN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power GAIN); 23 more in the record

**Energy / Facility / Industrial**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power GAIN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power GAIN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power GAIN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power GAIN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power GAIN); 23 more in the record

**Distribution / Specialized**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power GAIN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power GAIN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power GAIN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power GAIN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power GAIN); 23 more in the record

**The four stacked**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power EVEN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power EVEN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power EVEN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power EVEN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power EVEN); 23 more in the record

**The whole tower**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power EVEN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power EVEN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power EVEN); 4. Omni-Compass on top of Armada (work EVEN, over GAIN, power EVEN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power EVEN); 23 more in the record

**The orchestra**: 1. Omni-Compass on native (work EVEN, over GAIN, power power given)

**The live engine's organism**: 1. Omni-Compass on top of Karmada (work EVEN, over GAIN, power GAIN); 2. Omni-Compass on top of KubeEdge (work EVEN, over GAIN, power GAIN); 3. Omni-Compass on top of Open Cluster Management (work EVEN, over GAIN, power GAIN); 4. Omni-Compass on top of Armada (work EVEN, over the runs disagree, power GAIN); 5. Omni-Compass on top of The Kubernetes scheduler (vanilla, and its bin-packing profile) (work EVEN, over GAIN, power GAIN); 6. Omni-Compass on top of Crane (work EVEN, over GAIN, power GAIN); 23 more in the record

## Every LOSS cell of Omni-Compass (0)

A LOSS counts against Omni-Compass only where the way read is Omni-Compass's: on native against native, on top of a governor against that governor, or on top of a governor against native.

- none

## The governors' own LOSS cells against native (49)

Each governor on the organism, read against native: the governor's own reading, shown as the governor's, never counted as Omni-Compass's.

- The spine, Armada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The spine, Karmada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The spine, Open Cluster Management against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- Compute / AI / Cloud, Armada against native, 1 runs × 1 organisms: over, LOSS in our one run
- Compute / AI / Cloud, Karmada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- Compute / AI / Cloud, Open Cluster Management against native, 1 runs × 1 organisms: over, LOSS in our one run
- Energy / Facility / Industrial, Armada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- Energy / Facility / Industrial, Open Cluster Management against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- Distribution / Specialized, Armada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- Distribution / Specialized, Karmada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- Distribution / Specialized, Open Cluster Management against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Armada against native, 1 runs × 1 organisms: over, LOSS in our one run
- The live engine's organism, Armada against native, 1 runs × 10 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Armada against native, 10 runs × 10 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Armada against native, 100 runs × 10 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Armada against native, 1 runs × 100 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Armada against native, 10 runs × 100 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Armada against native, 100 runs × 100 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Armada against native, 500 runs × 100 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Armada against native, 1 runs × 500 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Armada against native, 10 runs × 500 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Armada against native, 100 runs × 500 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Armada against native, 500 runs × 500 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Karmada against native, 1 runs × 1 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Karmada against native, 1 runs × 10 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Karmada against native, 10 runs × 10 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Karmada against native, 100 runs × 10 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Karmada against native, 1 runs × 100 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Karmada against native, 10 runs × 100 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Karmada against native, 100 runs × 100 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Karmada against native, 500 runs × 100 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Karmada against native, 1 runs × 500 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Karmada against native, 10 runs × 500 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Karmada against native, 100 runs × 500 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Karmada against native, 500 runs × 500 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Open Cluster Management against native, 1 runs × 1 organisms: over, LOSS in our one run
- The live engine's organism, Open Cluster Management against native, 1 runs × 10 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Open Cluster Management against native, 10 runs × 10 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Open Cluster Management against native, 100 runs × 10 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Open Cluster Management against native, 500 runs × 10 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Open Cluster Management against native, 1 runs × 100 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Open Cluster Management against native, 10 runs × 100 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Open Cluster Management against native, 100 runs × 100 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Open Cluster Management against native, 500 runs × 100 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Open Cluster Management against native, 1 runs × 500 organisms: over, LOSS by our one run, beyond the noise in 0 of 1
- The live engine's organism, Open Cluster Management against native, 10 runs × 500 organisms: over, LOSS by the mean of our 10 runs, beyond the noise in 0 of 10
- The live engine's organism, Open Cluster Management against native, 100 runs × 500 organisms: over, LOSS by the mean of our 100 runs, beyond the noise in 0 of 100
- The live engine's organism, Open Cluster Management against native, 500 runs × 500 organisms: over, LOSS by the mean of our 500 runs, beyond the noise in 0 of 500
- The live engine's organism, Nephio against native, 1 runs × 10 organisms: over, LOSS by our one run, beyond the noise in 0 of 1

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
