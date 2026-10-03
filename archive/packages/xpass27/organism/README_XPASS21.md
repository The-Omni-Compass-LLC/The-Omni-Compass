# XPASS21 — One Organism, Simultaneous Muscle Breadth

## Scientific object
A **trial is one coupled organism**, not one muscle. At breadth 640, all 640 canonical muscle channels exist and act on every shared simulation clock step. They interact through organism-level queue, resource/power, network and thermal pressures.

The primary paired arms are:
1. `NATIVE`: the declared native specialist muscle feedback.
2. `OMNI_OVER_NATIVE`: the exact same native muscles, with one frozen CLAIM1 supervisory state per organism modulating their authority/targets.

There is deliberately no `OMNI_ALONE` primary arm. Omni is a supervisory governor, not an actuator replacement.

## Matrix
Breadth: `1, 10, 100, 500, 640` simultaneous muscles.
Monte Carlo trials: `1,000, 10,000, 100,000, 1,000,000` independent organisms.
Default shared-clock steps: `24`.

Every paired cell uses the same initial conditions and exogenous innovations for Native and Omni-over-Native.

## Memory/scaling design
The runner streams independent trials in chunks. A million-trial request therefore does not allocate a `[1,000,000,640]` tensor at once. Each chunk still contains the complete simultaneous muscle dimension. Accumulators preserve totals and worst-channel health. This is a computational batching strategy, not a change in the simulated organism.

## Evidence semantics
This is E2 simulation. `resource_index` is a declared model quantity, not kWh. `trials` are Monte Carlo organisms, not physical servers. Physical and live-software claims require E3/E4 receipts from the existing Kind/NVIDIA harnesses.

## Current local receipts
- 1,000 trials × 640 muscles × 24 steps: completed for both paired arms.
- 10,000 trials × 640 muscles × 24 steps: completed for both paired arms.
- 100,000 and 1,000,000 full-width cells: not completed in this constrained session; GitHub matrix is provided to execute them.

The current synthetic plant does **not** show an Omni superiority result. That adverse/null result is preserved. The benchmark is an evidence instrument, not a scoring machine.
