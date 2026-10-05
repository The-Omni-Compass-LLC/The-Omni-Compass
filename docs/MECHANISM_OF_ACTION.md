# Omni-Compass: mechanism of action, from the equations to the muscles

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Protected by copyright, patents and trademarks: Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Every statement here is tied to code in this repository, and the measured numbers are reproduced by
`python tools/mechanism.py`, which writes `results/MECHANISM_OF_ACTION.json`. The engine files are frozen. Their SHA-256
hashes are checked by `verify.py`.

## 1. The state: six numbers that describe the whole system

| Symbol | Name | What it stands for in a data centre |
|---|---|---|
| E | energy / excitation | how hard the system is being driven: queues, overload, power, heat |
| U | order parameter | how healthy and settled the system is: +1 healthy basin, -1 failed basin |
| I_U | integrated need | unmet need accumulated over time: memory of pressure that has not been relieved |
| S | stress | slow structural stress from heat, power, network, security, staleness |
| B, B_dot | bath and its rate | a damped oscillator driven by stress: the slow "tide" of physical load |

## 2. The equations (omnicompass/core.py, lines 5-12)

```
(1) dE/dt    = -alpha_E E + beta_int + beta_ext + v_eff
(2) dU/dt    = mu U (1 - U^2) - (dE/dt)/E_max - lambda_U U + u,          |u| <= 25
(3) dI_U/dt  = (1 - U) - sigma_1 E - delta S - lambda_I I_U
(4) v_eff    = cos(omega_B t / 2) * c * tanh(lambda_0 + lambda_1 (U - 0.5) + lambda_2 S)
(5) Phi(S)   = alpha_s S^2 / 2 + beta_s S^3 / 4 - delta S
(6) dS/dt    = -dPhi/dS = delta - alpha_s S - (3/4) beta_s S^2
(7) dB/dt    = B_dot ;   dB_dot/dt = gamma_c delta S - (omega_B / Q_B) B_dot - omega_B^2 B
(8) R_B[n]   = finite-difference audit of (7), never fed back
```

Each term does one job:

- **(1) Energy.** Energy decays at rate alpha_E = 3.487. It is driven by two forcings: internal pressure `beta_int` (queue and
  overload) and external pressure `beta_ext` (power, heat, network, staleness, security). The drive term `v_eff` (4) is
  bounded by `c` through the hyperbolic tangent, so no input can drive E without limit. This is the saturation (the tanh
  "speed limit"): however extreme the observation, the engine's response rate is capped at c = 1.
- **(2) Order.** `mu U (1 - U^2)` is a double-well (bistable) drift with two stable basins, U = +1 (healthy) and
  U = -1 (failed), and an unstable ridge at U = 0. A rise in energy (`dE/dt`) pushes U out of the healthy basin. `u` is
  the bounded control input.
- **(3) Integrated need.** I_U grows while U is below 1 (the system is not settled). It is reduced by energy and stress
  already being dealt with, and it leaks at lambda_I = 0.719. It is the engine's memory of unrelieved pressure.
- **(5)-(6) Stress.** A cubic potential (the "well in the basin"). S rolls downhill to its stable root. This is the
  slowest restoring force.
- **(7) Bath.** A damped harmonic oscillator (natural frequency omega_B = 1, quality Q_B = 2.5) driven by stress. It turns
  stress into a smooth, lagged "tide". It is the only second-order element.
- **(8) Audit.** The bath equation is re-checked numerically every step. The check is never fed back.

Integration: classical 4th-order Runge-Kutta, 10 micro-steps of 0.01 per macro step (`rk4_step`, `macro_step`). The C++
twin matches the Python to 3.6e-15 on 500 reference trajectories.

## 3. From telemetry to state (omnicompass/adapter.py, `observe_vector`, `assimilate`)

Each decision the telemetry is normalised to nine observations: q (queue), load, power, thermal, network, drift, stale,
security, conflict. An observed state is computed from them:

```
E_obs   = 0.25 q + 0.18 max(0, load - 0.85) + 0.16 power + 0.13 thermal + 0.10 network + 0.08 drift + 0.06 conflict + 0.04 stale
U_obs   = 1 - (0.27 q + 0.18 power + 0.16 thermal + 0.12 network + 0.12 drift + 0.10 conflict + 0.05 stale)
S_obs   = 0.36 thermal + 0.28 power + 0.18 network + 0.10 security + 0.08 stale - 0.20 q
B_obs   = 0.52 power + 0.26 thermal + 0.22 drift
I_obs   = q + drift + conflict
beta_int = 0.58 q + 0.42 max(0, load - 0.75)        beta_ext = 0.33 power + 0.27 thermal + 0.20 network + 0.12 stale + 0.08 security
```

The state is blended toward the observed state with weight a = 0.339: `x <- (1 - a) x + a x_obs`. It is then evolved
by one macro step (0.1 engine time units) of equations (1)-(7).

## 4. From state to action (the allocation law, `Governor.step`)

```
push     = u(x) / 25,  u(x) = clip(-f_U(x) + 12 (1 - U), -25, 25)        equation (2)'s controller, evaluated, not applied
rho*     = clamp(rho0 - kI I_U - kE E, rho_min, rho0)                      target utilisation (the HPA target)
n_req    = ceil(n load / rho*) + ceil(kq q n)                               machines wanted
release  only while push <= push_release (the engine reports convergence), after band and dwell
cap      = clamp(cap_now load (1 + margin), cap_min, 1) when calm and U >= U_gate; 1 under backlog;
           always <= 1 - cap_gain max(0, B - B_cap)                         the bath limits the power cap
change   permitted only while U >= U_gate and no security block
rollback authorised if S >= S_rollback, U is falling, or a security block is seen
```

## 5. Which equation drives which muscle

| Muscle | Engine quantity used | Where |
|---|---|---|
| HPA target (pods) | rho* from I_U and E, equations (1) and (3) | adapter `Governor.step`; live `omni_controller/controller.py` |
| Node pool (machines) | n_req from load, queue and rho*; release gated by push from equation (2) | same |
| Power cap (pod CPU limits, CPU frequency, GPU limit) | cap from U gate and bath B, equation (7) | same; `omni_controller/muscles.py` |
| Rollout guard | change_permitted (U), rollback (S, dU) | `muscles.py` |
| Security hold | security observation raises S and blocks expansion | adapter, shield |
| Speed-first law | rho* for pods; push gates machine release | `omnicompass/speed.py` |
| Right-sizing | rho* sizes CPU; E widens the memory margin; push gates scale-in | `omnilab/rightsize.py` |
| Cold start | rho* sizes instances; I_U sets how long to keep warm | `omnilab/coldstart.py` |
| GPU packing | I_U pre-warms nodes; push gates power-off | `omnilab/gpupack.py` |
| Training power | E tightens the applied ramp limit under sustained grid stress | `omnilab/powersmooth.py` |
| GPU health | S and E shorten the checkpoint interval | `omnilab/health.py` |
| Cooling | E widens the inlet-temperature margin | `omnilab/cooling.py` |
| Inference | the full allocation law (node_delta) sizes replicas | `omnilab/inference.py` |
| Agent containment | I_U throttles; the security observation contains | `omnilab/containment.py` |
| VM energy | I_U and E raise the learning rate when attribution goes stale | `omnilab/vmenergy.py` |

## 6. Measured: what the equations actually do inside the governor

Measured on a real observation stream (fleet plant, web services, fleet mode, 360 decisions):

| Mode (eigenvalue of the Jacobian at the operating point) | Time constant | In decisions |
|---|---|---|
| -7.90 | 0.13 | 1.3 |
| -3.10 | 0.32 | 3.2 |
| -0.72 | 1.39 | 13.9 |
| -0.20 +/- 0.98i (the bath) | 5.0, period 6.4 | 50, rings every 64 decisions |
| -0.17 | 6.0 | 60 |

- **Every mode is stable** (all real parts negative). The operating point is a stable equilibrium inside the healthy basin:
  E = 0.095, U = 0.976, S = 0.315, B = 0.10. This is the basin keeping everything in, stated as mathematics.
- **Per decision, the equations and the observation move the state about equally.** Across all six variables the
  equations contribute 45-50% of each step's movement and the observation blend the rest.
- **Equation (2)'s control input u is not applied during governance.** The engine evolves open-loop (u = 0). The control
  law is evaluated only to produce `push`, which decides when capacity may be released.
- **Compute:** about 95 microseconds per decision in Python, and about 2.9 microseconds in the C++ twin.

## 7. What this explains, and what it points to

- **Why "engine off" scores close to "engine on" in the muscle benchmarks.** With the equations frozen, the observation
  blend still moves the state. Both versions are then low-pass filters of the same telemetry. The engine's fast modes
  (1-3 decisions) behave almost like the blend itself. Its distinct contribution is its slow memory: I_U (14 decisions),
  S (60) and the bath (period 64 decisions). The muscle mappings mostly read E and rho*, which live on the fast modes.
- **The engine clock is not matched to the workload's rhythm.** One decision advances engine time by 0.1. At 60-second
  decisions the bath rings every 64 minutes, but web demand has a 24-hour rhythm and training power a 2-second one. This
  is a wiring choice in the adapter (engine time per decision), not a property of the equations.
- **The controller in equation (2) is unused as an actuator.** Wiring its output u (or U's trajectory under u) directly
  to the actuators is the unexplored way to "let the math do the work".

Three wiring experiments follow directly. None changes a single equation:

1. **Clock matching.** Set engine time per decision so that the bath's natural period equals the workload's rhythm.
   The oscillator in (7) then carries the cycle and can anticipate it.
2. **Slow-mode actuation.** Drive machines from I_U, S and B (the memory modes) rather than E (a fast mode).
3. **Closed-loop actuation.** Apply equation (2)'s u and use its magnitude, not only its sign, as the actuator command.

Each is testable in the existing harness against every platform in the league (tuning/league.py), and will be tested
there.


## The pedals: idle, gas, brake, reset, and the kill switch

Omni-Compass drives a system the way a self-driving car drives itself: it feels, gauges and adjusts, with nobody in
the seat. The words below are used the same way everywhere in this repository.

**Two names only.** **native** is the system as it runs on its own (Kubernetes and its autoscalers, the card's
firmware, CityLearn's controller). **omni** is Omni-Compass on top of native: the same native system, with Omni-Compass
governing it. Omni-Compass never runs instead of native, only on top of it, so every comparison is native against omni.

**The modes.** Off (manual): Omni-Compass not driving, native runs alone. Watching: Omni-Compass reads every gauge and
logs what it would do, and writes nothing. Autopilot: the pedals below. Cruise and the emergency brake: for work that
comes as a pile.

| Term | Meaning | In the code |
|---|---|---|
| **Idle** | No foot on the gas or the brake: calm traffic, the engine running at its floor (two machines in service, ready) | `MIN_NODES`, the floor of the staging law (8.8) |
| **Gas** | Ramping up: traffic climbs and capacity is added at once, never held back; the whole cluster can take work the instant it is needed | (8.3); a lower HPA target is never limited |
| **Brake** | Ramping down: traffic falls and capacity is eased off a step at a time, never below idle | (8.4)-(8.5); coasting, rule 6 |
| **Reset** | The brake held to the floor: every setting the governor ever wrote is handed back to where native had it, read back, and the record removed; the next run starts fresh. Every benchmark arm ends with one and checks it | the reset file (`--kill-file`, a name kept for compatibility), `Controller.restore` |
| **Cruise** | A pile of work waiting for a place: every machine in service, held there without second-guessing, until the line has been empty for two decisions | rule 7, `--cruise-after` |
| **Emergency brake** | The work is done and demand is at zero: straight to idle (the floor) in one move, every safety check still holding | rule 8, `--brake-demand` |
| **Kill switch** | Security only: one switch in a human hand that turns Omni-Compass's governing off across the whole system at once, for anything rogue or anyone trying to drive a system through Omni-Compass's brain | `omnicompass/master.py`, `tools/omni_switch.py off` |

The fuel cut-off point (the floor) is a number the operator sets; the brake never takes the system below it, however
hard it is pressed. Earlier dated records, and the sealed original engine files, call the reset a "kill switch"; they
are kept word for word.

## 8. The staging law: machines on and off in order, with demand that moves

Demand climbs, spikes, eases part way, climbs again and settles to idle. The staging law decides how many machines are
in service at every decision, and which ones, so that capacity follows demand up at once and comes back down only as
far as it safely can. It is the compass law (`omnicompass/compass_law.py`) applied to the machine pool
(`omni_controller/controller.py`), the release gate (`omnicompass/nervous_system.py node_release_gate`), the verdict
(`omnicompass/verdict.py`) and the actuator (`scripts/kind_nodepool.sh`). Every symbol below is a line of that code.

**Position and force.** The service reading r (the 95th-percentile response time, or the pressure that stands for it)
is placed in its band [lo, hi], where hi is the response line:

    p = (r - lo) / (hi - lo),      v = s v + (1 - s) (p - p_prev) / dt                       (8.1)
    F = A                                       if p >= 1 - c        (fail up, past the wall)
    F = A tanh( (kp (p - p0) + kd v) / A )      otherwise; F = 0 if F < 0 while v > 0 and p > p0   (8.2)

with the band's center p0 = 0.5, cushion c = 0.05, authority A = 1, kp = 1 and kd = max(0, 2 sqrt(kp tau / dt) - 1) dt
(critical damping for a muscle that answers in tau seconds). F > 0 asks for capacity, F < 0 offers it back.

**How many machines.** With n machines in service now, n_nat the count native ran, m the floor (two by default, `MIN_NODES`) and M the
machines that exist (every machine usable; an operator may hold whole machines back with `NODE_CUSHION`, off by
default), every count stays in m <= n' <= M. The protection is not a machine sitting out: it is the band inside every
machine. Capacity is added at 95% of the response line, before the line is reached (8.2-8.3), and a machine goes back
only if the ones left still run at or under the engine's utilisation target rho (8.5): a margin spread over all of
them.

    up      n' = min(M, max(m, n + 1))                              if p >= 1 - c                     (8.3)
    down    n' = max(m, n - 1)                                      if F < R and p < p0 and the verdict
                                                                    allows n_nat - (n - 1) and the gate G holds  (8.4)
    hold    n' = n                                                  otherwise

with the release threshold R = -0.2. Up is immediate and is never gated. Down is one machine per decision, never below the floor, and only
when every term of the release gate holds:

    G = [n > 1] and [nothing pending] and [pods not scaling up] and [no breach now] and
        [ used / ((n - 1) x per_node) <= rho ] and [contraction authority] and [every sense live] and
        [the last machine command landed]                                                          (8.5)

rho is the engine's utilisation target: after a machine goes back, what remains runs at or under rho. The verdict
(section 7 of the GPU preregistration, `omnicompass/verdict.py`) allows a machine count below native only after a
paired trial showed the service at that count at most 2% worse than at the count before; that 2% is where the trigger
sits, inside the engine.

**This is hysteresis by construction.** The up condition (p >= 0.95) and the down condition (p < 0.5 with F < -0.2)
are far apart, so a demand that hovers never makes machines flap; a spike crosses the wall and adds a machine at once;
a dip has to be deep, calm and sustained before one goes back, and then only one per decision. Between the two, the
count holds.

**Which machines.** The actuator orders the pool:

    idle   the open machine with the fewest serving pods, then the fewest pods, goes first;
           it is marked prefer-not (PreferNoSchedule) and its pods first to go (pod-deletion-cost), so the
           autoscaler's own scale-down empties whole machines; no pod is moved, evicted or restarted   (8.6)
    wake   the idle machine still carrying the most work goes first (it is warm); the mark comes off and it is in
           service at once, with no boot                                                          (8.7)
    floor  two machines always in service (MIN_NODES, the operator may set more), ready for a spike  (8.8)
    margin  every machine usable; the cushion is the band inside each one (the 5% before the line, and rho), not a
            whole machine held out                                                                 (8.9)

An idled machine stays powered and Ready at its floor (park_frac x idle power), never off: a pod that finds the open
machines full lands on it at once, so no request ever waits on a machine Omni-Compass idled. Where a node autoscaler
underneath really removes an empty machine (Azure's cluster autoscaler, Karpenter), that same order hands it the
emptiest machine first, and the bill falls with the machine.

**The same law on every discrete unit.** Machines are one case. In the muscle models (`realms/compass_arm.py
release_safe`), a cooling plant's chillers and a compute pool's machines follow the same law: one unit back only when
the units left cover the recent peak with headroom (RELEASE_MARGIN 0.6 for machines, 0.8 of a unit's capacity for
chillers), one at a time, and back at once when the wall is reached.

**What is proved, measured and open.** The order (8.6)-(8.8) is checked through the real actuator by
`tests/test_staging_order.py` (the emptiest idles first, the warmest wakes first, two always in service, every machine usable, no pod moved).
The gate (8.5) is checked by `tests/test_node_release_gate.py`. On real Kubernetes the law gave the same work 55-65%
faster on 29-36% fewer machines (sets 22-27) and 48% more work on the same machines (the capacity test); its run under
demand that wanders (up, spike, part way down, back up, idle) is in progress. Open: an order across different kinds of
unit (a battery before a generator, a CPU before a GPU) is not wired; each pool is ordered within itself.

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
