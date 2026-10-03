# Canonical C++ Wiring Pass 3

This pass wires the existing 128-muscle interface harness to an explicit C++ execution of the canonical six-state, eight-line Omni-Compass mechanism.

## What is now executable

- State: `(E,U,I_U,S,B,B_dot)`.
- Controller: `raw=-f_U+KP*(sigma-U)`, `KP=12`, saturated to `+/-25`.
- `sigma` is locked from the initial nearest signed basin.
- One macro interval is `0.1` and contains ten `0.01` microsteps.
- Every microstep computes one controller command and holds it across classical RK4 k1/k2/k3/k4.
- No post-RK4 U overwrite is introduced.
- Twenty macro intervals therefore execute 200 controlled microsteps and 800 RK4 derivative evaluations per trajectory.
- `canonical_engine` emits per-stage traces for parity/referee work.
- `muscle_pathways` maps canonical state/control into family-level normalized authority requests and then through the existing independent authority/security gate.
- The full-tower harness performs 20 x 128 pathway decisions, readback checks, final restoration, and a 128-muscle security fail-closed reflex test.

## Evidence boundary

The 128 endpoints remain simulated adapters. This pass establishes executable wiring from the canonical C++ mathematical mechanism into all 128 standardized muscle pathways. It does not establish 128 production connectors or physical plant performance.

`canonical_reference_parameters()` uses midpoints of declared sampled ranges solely as a deterministic smoke vector. The declared ranges remain authoritative for Monte Carlo qualification and must not be silently replaced by those midpoint values.

## Next evidence gate

Generate frozen parameter/initial-condition vectors from the original Python engine, execute the exact vectors in Python and C++, and compare state, derivatives, command, and RK4 stages at every microstep. Only a passing parity receipt should upgrade the C++ port from structural correspondence to numerical equivalence.
