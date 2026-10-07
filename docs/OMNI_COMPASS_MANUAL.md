# THE OMNI-COMPASS MANUAL

## The Governor, Its Mechanism, and How to Wire It onto Your Stack

**October 2026**
**The Omni-Compass LLC**

Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.

---

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. This manual and the software it describes are not
> open source. You may use them only to evaluate Omni-Compass and to reproduce its published results, including in
> shadow or test mode on systems you own or control. Any commercial use, commercialization, monetization, production
> use, operation of any system beyond evaluation, redistribution, hosted or managed service, or incorporation into any
> product or service requires a written **Omni-Compass Enterprise License**, signed by The Omni-Compass LLC and paid
> for. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC.
> "Omni-Compass" and its marks are trademarks of The Omni-Compass LLC. Full terms: `LICENSE` and `NOTICE`.

---

# FRONT MATTER

## Notice and Disclaimer

The software is provided "as is", without warranty of any kind. Every result in this manual carries its evidence
class (section 14). A simulated result is a statement about a model; a software benchmark is a statement about the
software it ran on; only a hardware meter speaks for hardware. Nothing in this manual is a promise of a particular
saving on a particular system. The only number that applies to your system is the one your own paired runs produce,
on your own receipt. Before Omni-Compass writes to any production system, it must run in watch mode, pass the wire
check, and be covered by a signed Omni-Compass Enterprise License.

**The wiring declaration.** Omni-Compass acts only through the wires it is given. A wrong reading, a wrong or shared
lever, a wrong range, or a service line set for another workload makes it do exactly what its law says with the wrong
information. It cannot be slapped on. If your paired receipts differ from the published benchmarks in direction, the
first presumption is wiring: confirm the installation with section 8.5 before drawing any conclusion. Every
declaration, disclosure and disclaimer is made once, in `DISCLOSURES.md`, and governs this manual.

## Foreword

I built Omni-Compass to sit on top of what already exists. Kubernetes, the GPU driver, the building controller, the
battery inverter, the robot's servo loop: those are muscles, and they are good muscles. What none of them has is one
brain that reads all of them at once, holds each of them in the middle of its safe range, and puts every setting back
exactly where it found it when it stops. That brain is Omni-Compass.

This manual is the whole of it: what the governor is, the mathematics it runs on, how its nervous system reads and
writes, how it is wired to each kind of machine, how to turn it on one level at a time, how to switch it off, and how
to prove on your own system what it does. Keep it with the code. When the code changes, this manual changes in the same
commit.

**AJ Dubra**
Founder, The Omni-Compass LLC

## Preface: How to Use This Manual

| You are | Read |
|---|---|
| CEO, board member, investor | Foreword; Part I (sections 1-3); section 14 (evidence); section 15 (the frozen engines and the three-run rule); section 17 (license); the Executive Summary below |
| CTO, architect, head of platform | Parts I-III; section 9 (wiring levels) to plan the rollout; Part VI |
| The engineer wiring it | Everything, in order. Do not skip the wire check (section 8) or the watch level (section 9, level 1) |
| Auditor, diligence team | Part II (mechanism), Part VI (proof), Appendix C (equations), Appendix F (evidence map) |
| Anyone who wants the whole list | `docs/REGISTER.md`: every muscle wired (945, by family), every benchmark run on every platform (Kubernetes, Azure AKS, GPU, CPU, UPS and batteries, buildings, power grids, robotics) with its result and file, and every open benchmark still to run, in order |

**Conventions.** `code` is a command, file or switch exactly as typed. "Native" means your system as it runs today,
without Omni-Compass. "Muscle" means any machine, service or controller Omni-Compass can read and set. "Knob" or
"lever" means one setting on a muscle. "The band" is a knob's or a service reading's safe range. Every step that
writes to a system is marked **WRITES**.

## Executive Summary

- **What it is.** A supervisory governor. It reads the meters of every muscle in your stack, computes one bounded
  force per muscle from a single closed mathematical law, and moves each muscle's own setting (a replica target, a
  clock ceiling, a power limit, a setpoint) to hold the service in the middle of its band. The muscles keep their own
  controls. Omni-Compass sets what they already accept.
- **What it does for you.** It turns the room your systems keep "just in case" into either more work for the same
  energy or the same work on fewer machines and fewer watts. On real Kubernetes, on the frozen engine Omni v1, run
  three separate times with ten paired runs each, it handled 42% to 48% more work inside the response line on the same
  machines, answered 57% to 69% faster at the 95th percentile, and gave back machines only where a paired trial showed
  no request slower (section 16). On a real database it held 61% to 72% fewer connections open for the same work and
  the same latency, at a confirmed cost in the host's CPU seconds (+14% to +28%), reported as such. The one combined
  number, the Omni index over the real categories confirmed three times, stands at +19.7% (`results/OMNI_INDEX.md`).
- **How it stays safe.** It watches before it writes, records every original setting before it acts, reads back
  every write, never writes past a knob's cover, gives everything back the moment service is at risk, stops writing
  if anyone else touches a knob, and returns every setting to its original value on one OFF switch.
- **How you know.** Every run produces receipts: native against Omni-Compass on the same system, the same load and
  the same clock, with 95% intervals. Results are labelled by a rule written before the run.

## Table of Contents

**Front Matter** - Notice and Disclaimer; Foreword; Preface; Executive Summary

**Part I - The Governor**
1. What Omni-Compass Is
2. The Muscles, the Realms and the Six Organisms
3. Where the Value Comes From

**Part II - The Mechanism of Action**
4. The Engine: Eight Equations and One Control Law
5. The Closed Circle: Why It Cannot Leave Its Compass
6. The Compass: Push, Pull and the Two Forces
7. The Two-Way Nervous System

**Part III - The Harness: Plugs, Wires and the Wire Check**
8. The Plug, the Adapters and the Wire Check

**Part IV - Wiring It onto Your Stack, Step by Step**
9. Before You Start, and the Eight Levels
10. Stack by Stack

**Part V - Operating It**
11. The OFF Switch, the Rules, and the Log
12. Maintenance, Upgrades and Security

**Part VI - Proving It**
13. Paired Runs and Receipts on Your Own System
14. Evidence Classes and How to Read a Result
15. The Frozen Engines and the Three-Run Rule
16. Results to Date

**Part VII - Code, Twins and Terms**
17. License and Commercial Terms
18. Python, C++ and the Seal

**Back Matter** - Glossary; Appendix A Command Reference; Appendix B File Map; Appendix C The Equations in Full;
Appendix D Metrics; Appendix E Troubleshooting; Appendix F Evidence Map; Contact

---

# PART I - THE GOVERNOR

## 1. What Omni-Compass Is

A governor on a steam engine does not build the engine and does not turn the shaft. It watches the speed and moves the
throttle so the speed stays in a band. Omni-Compass is that, for every machine you run.

It is a process on a host. It reads meters, steps a bounded mathematical law, and writes only the levers it has been
given. It is not the chip, not the GPU driver, not Kubernetes, not the building controller. Those keep running exactly
as they do today; Omni-Compass sets the values they already accept:

| Muscle | Its own control (kept) | What Omni-Compass sets |
|---|---|---|
| Kubernetes service | the HPA | the HPA's CPU target; replica floors |
| Kubernetes node pool | Cluster Autoscaler / Karpenter / MachineSet | how many machines stay in service (park and wake) |
| NVIDIA GPU | the card's firmware (boost, power and thermal limits) | the clock ceiling (up wire) and the power limit (down wire) |
| CPU | the kernel's frequency governor | the frequency ceiling |
| Data hall, building | the chiller and air handler loops | the supply-air setpoint; units in service |
| Battery site | the inverter | the reserve level; the peak ceiling |
| Robot joint, vehicle axis | the servo loop | speed and effort limits |
| Process loop, feeder | the PI controller | the setpoint inside its band |

When Omni-Compass stops, every one of those values goes back to what it was before Omni-Compass acted.

## 2. The Muscles, the Realms and the Six Organisms

The catalog (`realms/catalog.csv`) lists 945 distinct muscles in 59 families (Omni v2; v1 listed 656 in 46), each with its family, its plant model and its knob. The
register (`docs/REGISTER.md`) lists them by family next to every benchmark, run and still to run.
They fall into four realms. Every realm stands on the same spine (Kubernetes, machines, GPUs and CPUs, network,
storage, observability, security, cooling and electrical distribution, 257 muscles), plus its own domain muscles.

| Organism | Muscles | What it is |
|---|---:|---|
| 1. Compute / AI / Cloud | 430 | clusters, GPUs, AI training and inference, cloud capacity |
| 2. Physics / Robotics / Autonomous | 376 | joints, fleets, vehicles, flight and spacecraft axes |
| 3. Energy / Facility / Industrial | 470 | data halls, buildings, batteries, UPS, process loops, feeders, hospitals, farms, pipelines, mines, district heat, power plants, renewables, pharmaceutical and food plants |
| 4. Distribution / Specialized | 440 | networks, storage, databases, commerce, workflows, radio networks, clinical systems, ports |
| 5. The four stacked, every duplicate kept | 1,716 | all four realms on one clock, the shared spine counted in each |
| 6. The whole tower, every muscle once | 945 | every distinct muscle on one clock |

These six organisms are the benchmark set. Each is run native and with Omni-Compass on top, on the same seed, the
same load and the same clock, and each produces its own receipt.

## 3. Where the Value Comes From

### 3.1 The problem we are attacking

Computing has run into a wall that is not made of silicon. Data centers cannot get the power they need, cannot get it
fast enough, and are running out of room to put more machines. AI made it worse: every new model needs more chips, and
every chip needs more electricity and more cooling. The answers on the table are expensive and slow: new chips that do
more work per watt (a new generation, new hardware to buy), new power plants and power contracts (billions, and years),
and point fixes at a single layer (an AI serving trick, a scheduler, a power cap on one chip).

We attack it from the other side. Every system already running wastes room it paid for:

- GPUs boost to the top of their clock range and are knocked back by their own power limiter many times a second;
- Kubernetes keeps replicas and machines sized for the worst minute of the day;
- cooling runs colder than the heat requires; batteries hold more reserve than the hour needs.

That room is paid for in energy, in machines and in floor space, and it produces nothing.

### 3.2 What Omni-Compass is, in one paragraph

Omni-Compass is software that sits **on top of** the controllers a system already has (the GPU's firmware, the
Kubernetes autoscaler, the building's thermostats) and governs every layer under one law: a bounded push and pull that
keeps each service in the middle of its band instead of far below its limit. It never replaces the native controller,
never asks for more than the native settings allow, hands every knob back the moment it is switched off or loses a
sense, and refuses any step that measures more than 2% worse on anything. No new hardware. It stacks on top of every
other fix a data center makes.

### 3.3 The benefit: more work from what is already paid for

The room that was spent on nothing becomes one of two things, and a company chooses which:

- **More work for the same cost:** the same machines and the same watts carry more work; or
- **The same work for less:** fewer machines in service, fewer watts, a smaller bill.

They are the same gain read from two sides (3.4). The health side comes with it: faster answers, faster recovery from
failures, nothing waiting, every knob returned, no human babysitting the stack.

### 3.4 How to read the benefit: the arithmetic

Every comparison is paired: the same system, the same work, the same moments, native alone against native with
Omni-Compass on top. Let

- *W* be the work served (requests answered, tokens generated), held equal in both arms;
- *C* be a resource it used: machine-hours, CPU core-hours, or joules.

**Productivity** is work per resource, *P = W / C*. With the work held equal, the gain from Omni-Compass on top is

  *G = P_omni / P_native − 1 = C_native / C_omni − 1.*

A gain *G* means the same resources can carry *G* more work. Read from the other side, the same work needs only

  *C_omni / C_native = 1 / (1 + G)*

of the resources, a saving of *S = G / (1 + G)*. So **a third more work (G = 33%) is a quarter off the bill
(S = 25%)**; 20% more work is 16.7% off; 50% more work is a third off. Both columns are the same measurement.

Three rules for reading any receipt:

1. **The work must be equal.** Every receipt states that the load was fixed-rate (open loop): the same requests at the
   same moments in every arm. Without that, a lower resource count could just mean less work was done.
2. **Nothing may be worse.** Beside every gain the receipt prints response times, failures, waiting and the controller's
   own CPU, each with its 95% interval. Our one rule (`DISCLOSURES.md`, section 3): no measure more than 2% worse, and
   only where energy or the bill is saved. A gain paid for with worse service is not a gain.
3. **Know the class and the comparator.** A machine-hour gain on kind (where idle machines stay powered and native has
   no node autoscaler) is not yet a bill; a modelled energy line is not a meter. Section 14 lists the classes; section 16
   says, for every result, what it is measured against.

### 3.5 Where the evidence stands today, read honestly

| What | Measured gain *G* (same work) | Class | What a referee will ask |
|---|---|---|---|
| Kubernetes machine-hours, the allocation law | +45% to +61% (sets 29 to 31, cost to match) | L | native here has no node autoscaler and the cluster is ~4% busy: the AKS bill run and the capacity test answer this |
| Kubernetes machine-hours, the compass law with the verdict | +5% to +12% | L | the same |
| Kubernetes CPU, Omni-Compass's own included | +5% to +8% | L | measured on real software |
| Kubernetes response time, 95th percentile | 57% to 66% faster; no native setting tried reached it (cost to match) | L | measured |
| Recovery from faults (machine lost, spike, runaway pod, blind probe) | faster than native from every fault, up to 49% | L | measured |
| Energy per work, kind standby model | +8% (compass) to +30% (allocation) | L, modelled | not a meter |
| Energy per work, six organisms, 1x to 1,000x | +0.08% to +0.19% | S | well-tuned native controllers in models leave little room |
| Energy per work on a real GPU | the corrected law is measuring now on a real NVIDIA A10 and next on 8 cards | P | the decisive measurement |

The upside the data points toward is large, on the order of a third more work from what is already installed on the
Kubernetes side. It becomes a claim, not a direction, when three tests land: the bill on a real cloud against Azure's
own autoscaler (`docs/AZURE_SETUP.md`), the capacity test on fixed machines under rising load, and the real-card runs
for watts. We publish each of them as it comes, whatever it says.

### 3.6 Two modes, both measured

On Kubernetes, Omni-Compass offers two laws, and a buyer chooses by what matters most:

- **Efficiency mode** (the allocation law): the most machines given back (about a third fewer in service in sets 29 to
  31) with answers still about 60% faster than native;
- **Service mode** (the compass law with the verdict): the fastest answers (95th percentile about two thirds faster) and
  fewer machines (about 10%).

Both pass the one rule in every set since the fixes; neither is tuned to a benchmark after the fact. The laws are frozen
for every test that follows, so each new result describes exactly the code that produced the old ones.

---

# PART II - THE MECHANISM OF ACTION

## 4. The Engine: Eight Equations and One Control Law

The engine (`omnicompass/core.py`, frozen and fingerprinted) carries a six-part state x = (E, U, I_U, S, B, B_dot):

| State | Meaning | Physical picture |
|---|---|---|
| E | deviation: how far the system is from where it should be | a tank that fills with stress and drains on its own |
| U | alignment, between the two poles -1 and +1 | a ball in a double well: two stable poles, a hill between them |
| I_U | memory of misalignment | an integrator that remembers and slowly forgets |
| S | basin structure | a ball rolling to the bottom of its landscape |
| B, B_dot | the bath | a spring with friction that absorbs and settles energy |

The eight equations (Appendix C gives them in full):

1. dE/dt = -alpha_E E + beta_int + beta_ext + v_eff
2. dU/dt = mu U (1 - U^2) - (dE/dt)/E_max - lambda_U U + u, with |u| <= 25
3. dI_U/dt = (1 - U) - sigma_1 E - delta S - lambda_I I_U
4. v_eff = cos(omega_B t / 2) c tanh(lambda_0 + lambda_1 (U - 0.5) + lambda_2 S)
5. Phi(S) = alpha_s S^2/2 + beta_s S^3/4 - delta S
6. dS/dt = -dPhi/dS
7. d2B/dt2 = gamma_c delta S - (omega_B/Q_B) dB/dt - omega_B^2 B
8. R_B: a finite-difference audit of (7), never fed back

**The control law.** u = clip(-f_U(x, t) + K_P (sigma - U), -25, +25), where f_U is the drift of U with the command
at zero, sigma is the target pole and K_P = 12. The first term cancels whatever is shoving U (the push); the second
pulls U to its pole, harder the farther it is (the pull). The command is held unchanged through every stage of the
fourth-order Runge-Kutta step and U is never rewritten afterwards. Inside the authority limit, U converges to its pole
at rate K_P; this is proved (`docs/TRACKING_THEOREM.md`).

## 5. The Closed Circle: Why It Cannot Leave Its Compass

The governing principle is the Unified Circle Principle:

    dX/dt = G(X),  X(0) in Omega
    G(X) . n(X) <= 0 on the boundary of Omega        (the flow points inward at the wall: nothing crosses)
    grad L(X) . G(X) <= 0                            (the compass's energy L only falls)
    => lim X(t) in M*                                (every path settles in the bottom of the compass)

In control engineering the second line is the Nagumo condition for an invariant set and the third is a Lyapunov
function. Together they mean: anything that starts inside the container stays inside it, for every disturbance up to a
known size, and comes to rest at the bottom. That is a certificate, not a test: it answers every case inside the walls
at once.

The engine's states are each closed in this sense: the deviation tank drains faster than it can fill; the alignment's
cubic walls push back from far out; the memory forgets; the bath's friction settles it. The rule behind all four is
the compass's east-west line: what flows out (drain, damping) must always be able to match what flows in (drive).

**The compass.** The Omni-Compass rose carries the whole Greek alphabet, Alpha to Omega: the complete set, in a ring
whose end runs back into its beginning. Its north-south axis is polarity: Alpha and plus at the top, Omega and minus at
the bottom, the two poles of the alignment's double well. Its east-west axis is flow: Beta and the push outward on one
side, Gamma and the pull inward on the other, the drive and the damping. The spiral at the center is the attractor
every path winds into. The ring closing on itself is the return: when Omni-Compass stops, every lever returns to where
it began.

## 6. The Compass: Push, Pull and the Two Forces

The compass (`omnicompass/compass_law.py`) is the law that carries the engine's push and pull to every muscle.

**Two bands.**
- **The cover**, a knob's hard range (the device's or the operator's lowest and highest setting). Every write is
  clipped to it. Nothing Omni-Compass computes can set a knob outside it.
- **The compass**, the service reading as a position from 0 (calm) to 1 (the service line). Omni-Compass pulls that
  position to the bottom of the compass, the middle (0.5 by default; an operator may set it lower for extra margin). The
  walls run from 0.05 to 0.95; the last 5% on each side, 10% in all, is cushion.

**The force.** F = A tanh((K_P (p - center) + K_D v) / A), where p is the position, v its rate of change, A the
authority.
- **Pull:** K_P (p - center), gentle near the bottom, stronger up the walls.
- **Push:** K_D v, the force that meets whatever is shoving the position, and the friction that stops it sloshing.
  With K_D at or above critical damping the position glides to the middle and stops, with no overshoot and no
  ringing. Overshoot is wasted energy: force spent going the wrong way and spent again coming back.
- **Smooth, never a hammer:** tanh bends the force over into its maximum instead of slamming into a wall.
- **Fail up:** past the 0.95 wall the up side goes to its full force at once and the down side may not act until the
  position is back inside the compass.

**Two forces: antagonist pairs.** Like the muscles of an arm, every plug has an up side (adds capacity, power,
cooling, speed) and a down side (takes it back), each with its own gain, because adding and taking back do not cost
the same: a new machine takes minutes to boot; giving one back is instant. Where a machine has two wires, each side
gets its own lever:

| Muscle | Up force | Down force |
|---|---|---|
| GPU card | clock ceiling raised | power limit lowered (the lid) |
| Kubernetes | scale out | scale in |
| Cooling | chiller on, colder setpoint | warmer setpoint, unit released |
| Battery | discharge | charge, reserve held |
| Vehicle, joint | motor effort | braking, regeneration |

**Why the GPU needs both wires.** A card's firmware boosts its clock as high as it may while there is work, and its
power limiter knocks the clock back each time the draw crosses the limit; on a busy card this happens many times a
second, at the top of the clock range where each extra step of speed costs the most watts. With one wire (the power
limit) a governor can only move the wall the boost pushes against. With two wires, the clock ceiling sets how high the
boost may climb and the power limit becomes a lid that rarely needs to act: the card runs at the bottom of its compass
instead of fighting itself at the top.

**What the card taught us.** Two rules make the difference between saving energy and spending the customer's time.
First, *race while work waits*: when the card is saturated, both wires go to full at once, so a burst is always served
at full speed; the compass paces only the slack between bursts. Second, *never slower than the card on its own*: the
governor learns, from the card's own meter, the clock and the draw the card reaches by itself while busy, and never
sets the clock ceiling or the lid under them. Without these rules the first real card saved 3.5% of its energy and
made the slowest answers 58.5% slower; with them, the modelled card saves energy with the slowest answers at native
speed or faster (section 16, and `docs/GPU_PREREGISTRATION.md`, amendments 6 and 7).

## 7. The Two-Way Nervous System

Every muscle is wired both ways: a sensory wire in (its meters) and a motor wire out (its knob), with the read-back
closing the loop. Between them sits the nervous system (`omnicompass/nervous_system.py`), which decides how much
authority each organ has at each moment:

- **Expand is always allowed** (except under a security hold): adding capacity, power, cooling or protection never
  waits.
- **Contract needs calm and a clean service record:** giving anything back is allowed only while the organ is calm
  enough and service has been inside its line for the last three decisions; continuous organs give back at most the
  calm share of their surplus per decision; discrete organs one unit at a time, through a release gate.
- **Fail up:** while service is breached, the knob returns to native at once.
- **Blind means hold:** if a sense goes stale or unreadable, nothing is given back until it returns.

One brain reads every organ at once. Because one law sets every knob, no two muscles fight: when the GPU's watts turn
to heat, the cooling knob already knows it is coming; when pods scale up, the power envelope is ready.

---

# PART III - THE HARNESS: PLUGS, WIRES AND THE WIRE CHECK

## 8. The Plug, the Adapters and the Wire Check

Think of a high-end car stereo: one head unit, one standard plug on its back, and an adapter harness for each make of
car that matches the car's factory plug. You never cut a factory wire, and when you pull the stereo, the car works as
it did. Omni-Compass is wired the same way.

**8.1 The plug (one design for every muscle).** Each plug has as many channels as its muscle has knobs. Every channel
declares its cover (range), its direction (which way is "more"), its units and how fast it may move. Every plug keeps
the same contract (`omnicompass/compass_law.py`, `Plug`):

1. **attach** - read the knob once, before any write: the snapshot. It never moves afterwards.
2. **read** - the service reading, into the compass.
3. **write** - one value, clipped to the cover, then read back from the device.
4. **one writer** - if the knob is found at a value Omni-Compass did not write, someone else owns it: Omni-Compass
   stops writing and leaves that value alone.
5. **restore** - on stop, the knob returns to the snapshot (where Omni-Compass found it, not the last value it wrote).
   For muscles whose native controller moves the knob itself, restore hands control back.

**8.2 Adapters (one per standard plug).** Omni-Compass speaks each industry's standard control interface through an
adapter. Status is stated plainly:

| Standard | Muscles | Adapter status |
|---|---|---|
| Kubernetes API | HPAs, deployments, pods, nodes | **built** (`omni_controller/controller.py`, `muscles.py`) |
| NVIDIA NVML / `nvidia-smi` | GPU clock ceiling, power limit | **built** (`omni_controller/gpu_compass.py`, two wires; `gpu_governor.py`, one wire) |
| Linux cpufreq, RAPL | CPU frequency ceiling, package watts | **built** (`--cpufreq-policy-root`, `--rapl-cmd`) |
| Site meter, building controller by command | site watts, supply-air setpoint | **built** (`--power-cmd`, `--cooling-cmd` command templates) |
| Cloud node groups (Karpenter, Cluster Autoscaler, MachineSet) | machines | **built** through `--node-scale-cmd` templates |
| BACnet, Modbus, SNMP | chillers, air handlers, PDUs, UPS | designed; today reached through the command templates above |
| OPC UA, EtherNet/IP, PROFINET, EtherCAT, ROS 2, CAN | PLCs, drives, robots, vehicles | designed; modelled in the realm harness |
| IEC 61850, DNP3, OpenADR, IEEE 2030.5, SunSpec, OCPP | substations, batteries, inverters, chargers | designed; modelled in the realm harness |

The engineer's job for one muscle is three things: which adapter, the address of the knob, and its safe range.

**8.3 Power-up order.** Read-only first; then take the knobs, the least consequential first; on stop, hand them back
in reverse order.

**8.4 The wire check (mandatory before any write).** For the GPU it is one command,
`sudo python3 tools/gpu_wire_check.py --gpu 0`, and `scripts/gpu_rented_run.sh` runs it first and stops if it fails:

| Step | It proves |
|---|---|
| 1 read | every meter answers: watts, temperature, utilization, limit, clock, top clock |
| 2 snapshot | the start limit is recorded once |
| 3 up wire | with the card busy, a ceiling below its own busy clock pulls the clock down under it; reset, the clock comes back above it |
| 4 down wire | a lower power limit is reported back exactly; the start limit is reported back exactly |
| 5 restore | clocks reset and the start limit read back |
| 6 stop | the governor, stopped by its signal, hands both wires back |
| 7 other writer | a limit set by someone else while the governor runs is left alone, and the governor exits 5 |

Any failure prints the wire, the step and what the device said, and nothing else runs. That turns a wiring fault from
guesswork into one named line to fix.

**8.5 Wired right or wired wrong.** The wire check proves the wires move. It does not prove the governor reads the
right thing. A correct installation leaves signatures in its own receipts; a wrong one leaves others. Check them on
your first paired runs, before you believe any number, good or bad.

| Check | Wired right | Wired wrong, and what to look at |
|---|---|---|
| Watch arm against native | equal on every gauge (watch writes nothing) | different: the probe, the load or the machine differs between arms, not Omni |
| Requests served, failed requests | equal to native | fewer served or more failed: a lever is cutting capacity; check its cover and its sign |
| p95 and p99 response time | at native or faster | slower: the reading or the floors are wrong (rows below) |
| GPU: the card's clock while busy | at or above the clock the card reaches on its own | below it: the speed floor is missing or the lid is under the card's own draw |
| GPU: the lid while busy | at or above the card's own busy draw | at the envelope floor while busy: the lid is sized from a curve, not from the card's own meter |
| GPU: credit per write (`GPU_REPS.md`) | compass decisions pace the slack, race decisions cover the bursts; fail-up is rare | fail-up in most decisions: being busy is being read as a breach, or the service line is set too low |
| Kubernetes: machines given back | through the release gate, one per decision, with no pod waiting | machines given back while pods wait, or none at all while the service is far inside its band: check the latency feed, `--slo-ms` and the release gate's reasons in the audit |
| Kubernetes: the reset | every HPA target, replica range, CPU limit and worker back to native, no record left | anything left: an earlier run or another controller wrote the same objects |
| Every lever after the run | at its snapshot | not at its snapshot: another writer, or a restore that failed (exit 3): restore by hand and investigate |
| The feed itself | fresh samples every few seconds | stale or empty: Omni reads it as blind and fails up; fix the feed, not the governor |

**The rule.** If any row reads "wired wrong", the result of that run says nothing about Omni-Compass: fix the wiring,
run the wire check and the watch arm again, and only then compare. The first real card run is the worked example: its
receipts showed the card's busy clock under its own (736-768 MHz against 861-889), the lid at the 105 W floor under its
own 135 W draw, and fail-up in 46% of decisions. Each of those is a row in this table.

---

# PART IV - WIRING IT ONTO YOUR STACK, STEP BY STEP

## 9. Before You Start, and the Eight Levels

### 9.1 What your system needs

| You run | You need |
|---|---|
| Kubernetes (vanilla, EKS, GKE, AKS, OpenShift/OKD, Rancher, kind) | Kubernetes 1.34 or newer (in-place pod resize); metrics-server (`kubectl top nodes` works); an HPA with a CPU target on each governed service; a readiness probe and a short preStop pause on each service |
| A response-time feed (strongly recommended at every level) | a CSV per service, `elapsed_seconds,latency_ms,ok`, written continuously; `scripts/latency_probe.py` writes one against any HTTP endpoint |
| NVIDIA GPUs | a driver with `nvidia-smi`; root (or the capability to run `nvidia-smi -pl` and `-lgc`); on a VM, full GPU passthrough |
| CPU power control | Linux cpufreq with the schedutil governor; RAPL for package watts; usually bare metal |
| Site power and cooling | a command that prints site watts, and a command that sets the supply-air setpoint through your building management system |

### 9.2 Get the software and check it

```
git clone https://github.com/The-Omni-Compass-LLC/The-Omni-Compass.git
cd The-Omni-Compass
pip install -r requirements.txt
python3 verify.py                       # every check; ends with VERIFICATION: PASS
```

Build the container image once:

```
docker build -f deploy/Dockerfile -t <your-registry>/omni-compass:<tag> .
docker push <your-registry>/omni-compass:<tag>
```

It runs as non-root, with a read-only root filesystem and no Linux capabilities.

### 9.3 The levels

Take them in order. Each has a pass condition; go to the next level only when it holds. The OFF switch works at every
level.

**Level 0 - Evaluate without touching anything.**

```
python3 verify.py
python3 tools/run_scale.py --runs 10 --scale 1 --out results/scale/eval     # the six organisms, simulated
python3 tools/run_gpu_card.py results/sim/gpu_two_wire/eval                  # the two-wire card, modelled
```

Pass: `VERIFICATION: PASS`. Nothing in your systems is touched.

**Level 1 - Watch (read-only).**

```
kubectl apply -f deploy/install/omni-compass.yaml     # set the image line; it runs --mode observe
kubectl -n omni-compass logs deploy/omni-compass -f
```

The install file grants a read-only identity; `scripts/pilot_shadow.sh` records `kubectl auth can-i` receipts that
show it cannot write. Every decision it would take is logged with its reason.
Pass: zero writes, and readings your operators agree with.

**Level 2 - The pods, on top of your autoscalers. WRITES.**
1. Grant `patch horizontalpodautoscalers` and `patch pods/resize` (`deploy/rbac-target.yaml`).
2. Run with `--mode target --latency-file <feed> --slo-ms <your p95 target>`.
3. Optional pod muscles, one at a time:

| Muscle | Switch | What it does |
|---|---|---|
| convey | `--latency-file` and `--cap-deployments ns/name` | gives each machine's idle CPU to the serving pods on it |
| rightsize | `--rightsize-deployments ns/name` | each pod's CPU request follows its measured use times (1 + headroom), in place |
| coldstart | `--coldstart-deployments ns/name --coldstart-signal ns/configmap` | scales a service to zero while no work waits, wakes it when work arrives |
| batch | `--batch` | admits held Jobs labelled `omnicompass.io/batch=true` when there is load and power headroom |
| batch pace | `--batch-pace` | pauses Jobs labelled `omnicompass.io/pausable=true` under power or heat stress, resumes them after |
| rollout guard | `--rollout-guard ns/name` | pauses a rollout while change is not permitted |
| contain | `--contain-namespaces ns --contain-cpu-m <m>` | holds an agent namespace to a CPU budget |
| security hold | `--security-configmap ns/name` | key `hold: "true"` blocks every expansion |

Your HPAs keep scaling as before; Omni-Compass sets their targets and raises floors ahead of bursts.
Pass: p95, p99 and failed requests no worse than native, over paired runs (section 13).

**Level 3 - The machines. WRITES.**
1. Grant `patch nodes` and `patch pods` (`deploy/kind/rbac-omni.yaml`).
2. Run with `--mode nodepool --active-nodes-only --closure /app/law/closure.json --node-scale-cmd "<command with {n}>"`
   and `--node-restore-cmd "<command>"` for the OFF switch. For the compass law on the same levers, use `--law compass`
   (reads the mean response time of the latency window between a tenth of `--slo-ms` and `--slo-ms`, held at
   `--compass-center 0.4`; p95 at the SLO, a blind feed or a waiting pod adds capacity at once; the HPA target never goes
   above the operator's; machines go back one at a time through the release gate).

| Your platform | The park/wake command |
|---|---|
| any cluster, bare metal, kind | `bash scripts/kind_nodepool.sh {n}` |
| Karpenter / EKS Auto Mode | the NodePool CPU limit at `{n}` times node CPU, parked nodes kept |
| Cluster Autoscaler node group | the group's desired size, scale-down through parking |
| OpenShift / OKD | the worker MachineSet replicas, parked |

A machine is given back only when every sense is live, the last order landed, pods are not scaling up, nothing waits
for a place, and the remaining machines stay inside the band.
Pass: fewer machines in service, with no service gauge worse.

**Level 4 - Omni-Compass decides; Kubernetes is the muscle. WRITES.** Add `--strict-replicas`: Omni-Compass decides
each service's replica floor and when to shrink; the HPA stays as the fast reflex upward.
Pass: as level 3.

**Level 5 - A GPU box, two wires. WRITES.**

```
sudo python3 tools/gpu_wire_check.py --gpu 0                    # must end: WIRED RIGHT
# watch: computes both wires and writes neither
sudo python3 -m omni_controller.gpu_compass --mode watch --gpus 0 --audit /var/log/omni/gpu.jsonl \
     --latency-file <feed> --slo-ms <p95 target> --floor-w <your lowest watts>
# govern: writes the clock ceiling and the power limit
sudo python3 -m omni_controller.gpu_compass --mode cap --gpus 0 --audit /var/log/omni/gpu.jsonl \
     --latency-file <feed> --slo-ms <p95 target> --floor-w <your lowest watts>
# OFF: clocks reset, power limit back to the start, read back
sudo touch /tmp/omni-gpu-kill
```

Every `--interval` seconds (default 2) it reads the card's own meters and the response times, and:
- **learns the card on its own** first: while the ceiling is at the top and the card is busy, its busy clock and busy
  draw; until 15 such readings are in, neither wire moves;
- **races while work waits**: at 95% utilization or more, the ceiling to the top and the lid to the start limit;
- **paces the slack**: the mean response time of the last 5 s, between a tenth of `--slo-ms` and `--slo-ms`, held at
  the compass's center (0.4); the ceiling moves in whole 15 MHz steps, never under the card's own busy clock, and the lid
  never under the card's own busy draw plus 10%, never over the start limit;
- **asks the card first (the verdict)**: before the ceiling may go one step lower, a paired trial measures the card's own
  time on each request (the workload's `service_ms`) at the top and at that step; the step is allowed only if it adds
  at most `--allow` (2%). Where no step passes, the ceiling stays at the top: the card runs as it does alone, and the
  audit says so (`verdict_state: left native`);
- **fails up** when p95 reaches `--slo-ms`, a request fails, the feed goes blind or the card reports a heat slowdown.

One law, no profiles: down gain 0.0125, center 0.4, floor at the card's own busy clock, allowance 2% (GPU
preregistration, amendment 8). The workload must write `service_ms` (the card's own time per request) in its latency
file, as `tools/gpu_workload.py` does; without it no step is ever allowed and the card stays native.
Pass: work per energy up or equal; requests served equal; no request more than 2% slower at the median, p95 and p99
at native or within 2%; every row of section 8.5 reads "wired right".

**Level 6 - CPU clock and power. WRITES.** On bare metal, add to the controller:
`--cpufreq-policy-root /sys/devices/system/cpu/cpufreq --cpufreq-require-schedutil --rapl-cmd "<prints CPU package watts>"`.
The OFF switch writes every policy's recorded maximum back exactly.
Pass: energy per unit of work down, no service gauge worse.

**Level 7 - Site power and cooling. WRITES.**
`--power-cmd "<prints site watts>" --site-limit-w <limit>` brings site power stress into the engine;
`--cooling-cmd "<sets {c}>" --cooling-min-c 18 --cooling-max-c 27 --cooling-restore-c 22` lets it hold the supply-air
setpoint in its band. CPU and GPU sharing one power budget (`hardware/node_exchange.py`) and GPU groups sharing a site
budget (`hardware/site_exchange.py`) run in simulation today. Batteries are designed as an organ, not yet wired.

## 10. Stack by Stack

Every wiring below is the same plug (section 8): one wire in (the stack's own meter), one wire out (one setting the
stack already accepts), a snapshot taken once before the first write, every write read back, everything restored on
OFF. Native is always the stack's own controller left as shipped; omni is that controller with Omni-Compass on top.

| Stack | Levels | Notes |
|---|---|---|
| Vanilla Kubernetes, kind, Rancher | 1-7 | as written |
| Amazon EKS | 1-5 | machines via Cluster Autoscaler node group or Karpenter; CPU power control is not exposed on EC2 VMs; GPUs on bare-metal or full-GPU instances |
| Google GKE, Azure AKS | 1-5 | the provider's node-pool size as the park/wake command; on AKS the managed cluster autoscaler stays native and deletes the machines Omni-Compass idles (10.1) |
| Red Hat OpenShift / OKD | 1-5 | the same permissions through a Role; machines via the worker MachineSet |
| NVIDIA GPU servers without Kubernetes | 5 | the two-wire GPU governor alone |
| Bare-metal CPU servers | 6 | cpufreq and RAPL through sysfs |
| Slurm / HPC | 5 on the GPU nodes | a job-level Slurm connector is not built |
| Building management | 7 | through your BMS's command line or API, in the command templates |
| PostgreSQL behind PgBouncer (any database behind a pooler with a console) | one knob | the pool size through the pooler's own admin console (10.2) |
| A power grid's substation tap changer (pandapower, SimBench) | one knob | the tap position, one whole tap per move (10.3) |
| Buildings with batteries (CityLearn) | one knob a building | the battery's charge and discharge inside the simulator's own limits (10.3) |
| Robot arms (MuJoCo Menagerie) | one knob an axis | the joint speed where the axis has slack; never on an axis at its takt (10.3) |
| A rented cloud machine running the big organisms | the whole harness | the detached run: rent, run, collect, delete (10.4) |

### 10.1 Managed Kubernetes on Azure: the bill as the gauge

On Azure Kubernetes Service the muscle is the same as on kind (section 9, levels 1 to 3) and one thing is new: the
bill is real. The workflow `aks-metered` builds a fresh cluster for every arm the same way: a system pool of one
machine, tainted so no workload lands on it (Azure's add-ons and the load generator live there; it is never measured
and never governed), and one or several **work pools** under Azure's own cluster autoscaler, every pool labelled
`omni-role=work`, every pool starting full. Native is that autoscaler alone. Omni on top is the same autoscaler with
Omni-Compass idling the machines it gives back, which the autoscaler then deletes on its own schedule. The bill counts
every work machine that exists, every 15 seconds, priced at Azure's list price for its family (`tools/live_reps.py`,
`POOL_PRICES`); each cluster is deleted when its arm ends, so nothing keeps billing.

**Sizing the fleet to the lever.** The smallest saving a fleet can show is one machine. On 4 workers one machine is
25% of the fleet, so only a saving of about 30% or more can clear the noise; on 15 workers about 10%; on 96 about 3%.
The expected machine saving under Omni-Compass is a few percent, so the 4-worker runs (`results/live/V1_AKS_STEADY.md`,
`V1_AKS_BURST.md`) read no difference beyond the noise on every gauge, which is the honest reading of a fleet too small
for the lever, not a result against it. A new subscription allows 200 vCPUs in a region but 10 per machine family, so
one family gives five 2-vCPU workers; the way past it is **several families at once**: eight pools of four to five
workers each make a fleet of 39 (`worker_pools` input, `size:max,size:max,...`; `pool_prices` names each family's
price). The app's replica ceiling is raised with the fleet (`hpa_max`: nine 200-millicore pods fit one 2-vCPU worker,
so 9 × workers lets the fleet fill), the same in both arms. The preregistered design is in
`docs/K8S_COMPASS_PREREGISTRATION.md`, "The fleet that can show one machine"; the account setup, click by click, in
`docs/AZURE_SETUP.md`.

### 10.2 A database behind its connection pooler

PostgreSQL is wired through PgBouncer, the pooler most of its deployments already run (`docs/POSTGRES_PREREGISTRATION.md`,
`tools/run_pgbench.py`). Nothing models the database. The wire in is the pooler's own report (`SHOW STATS`,
`SHOW POOLS`): once a second, the time a transaction spent in the server plus the time clients waited for one, over the
transactions completed. The wire out is one setting through the pooler's own admin console, `SET default_pool_size`,
inside the cover [2, 90]: never under two server connections, never within ten of PostgreSQL's connection limit. The
compass holds that reading at 40% of a 50 ms line. Where the time was spent decides the direction: waiting for a
server grows the pool; time inside the server shrinks it by one, so fewer backends fight for the same cores; calm gives
back one idle server a second, and only one the pooler itself shows idle. At 95% of the line the knob is handed back
to the pooler's own setting at once. If the knob is found at a value Omni-Compass did not write, it stops writing (one
writer). At the end of every omni arm the pool size is restored to the snapshot and read back. The same plug fits any
pooler or proxy with a console and a pool-size setting (PgBouncer, Pgpool-II, ProxySQL, the application's own pool).

### 10.3 Independent simulators, each with its own native controller

Three published simulators are wired the same way, and the simulator's own controller is always native:

- **CityLearn** (`tools/run_citylearn.py`): every district the simulator ships; the knob is each building's battery
  charge and discharge inside the simulator's own limits; the native arm is the simulator's own rule-based control.
- **pandapower on SimBench grids** (`tools/run_pandapower.py`): the knob is the substation tap changer, one whole tap
  per move and a week of evidence before stepping down; the native arm holds the tap at 1.00 per unit as the grid
  ships.
- **MuJoCo Menagerie robot arms** (`tools/run_mujoco.py`): the knob is the joint speed of an axis that has slack; the
  paired physics trial written before the run leaves an axis at its takt native, so UR5e and iiwa 14 have nothing for
  Omni-Compass to move and the Gen3 and Panda do.

Each is preregistered (`docs/CITYLEARN_PREREGISTRATION.md`, `docs/PANDAPOWER_PREREGISTRATION.md`,
`docs/ROBOTICS_PREREGISTRATION.md`), each runs A, B and C as separate GitHub runs, and each table is made by rule
(`tools/citylearn_abc.py`, `tools/pandapower_abc.py`, `tools/mujoco_abc.py`). These are evidence class S: statements
about the simulator's model, never about hardware.

### 10.4 The big organisms on a rented machine

The four stacked at 1,000 copies (1.7 million modelled muscles) with a real cluster inside takes more than GitHub's
six-hour job limit per repetition, so it runs **detached** (`.github/workflows/big-organism-detached.yml`): `start`
rents one Azure machine, installs the tools, starts every repetition of every organism under `nohup` and leaves the
machine running on its own; `collect` (every two hours on the clock, or by hand) copies the files back when every
repetition has finished, publishes one artifact per cell and deletes the machine; `survey` lists which machine sizes
and quotas a subscription may rent, region by region, and rents nothing. A machine older than `max_hours` is collected
as it is and deleted, so nothing runs forever on the bill. The commit to run is an input, so an older engine can be
run again on the same machine. **The clock rule** (section 13) decides the window for each size on each machine: the
first v3 machine stepped the stack in 31 s against a 12 s step and fell 4,628 s behind its window, so it was stopped,
recorded, and started again with a 10,800 s window and 45 s steps.

---

# PART V - OPERATING IT

## 11. The OFF Switch, the Rules, and the Log

**The rules Omni-Compass keeps on your system.**
1. **The master switch, for the whole harness, in a human hand:** `python3 tools/omni_switch.py off` turns every
   Omni-Compass governor on the machine off at once (the Kubernetes controller and the GPU governors). Each puts every
   setting it ever wrote back to the value it read before its first write, reads it back and exits; the command waits
   until all have, and says so. While the switch is OFF, no governor will start. `python3 tools/omni_switch.py on` allows
   them to be started again (nothing restarts by itself); `status` shows the switch and every governor running. Use it
   the moment anything looks wrong, including a suspected breach. Each governor also keeps its own switch for one
   muscle at a time: the kill file (or `OMNI_KILL=1`, or SIGTERM to the GPU governor).
   **If a governor dies without handing back** (killed outright, the machine crashed, it hung), nothing it wrote is
   left in place: every governor records, before its first write, the exact commands that put every setting back, and
   renews a lease every decision. Run `python3 tools/omni_switch.py watchdog` as its own service next to the governors:
   it hands back for any governor whose process is gone or whose lease has run out (a hung one is stopped first).
   `status` names any governor that died without handing back.
2. It records before it acts (annotations on Kubernetes objects; the `snapshot` line in the GPU audit).
3. It watches before it writes.
4. It never acts blind.
5. Service first: while response time is over its target, and for `--slo-clear` decisions after, nothing is given back.
6. Every change is read back; no new order goes on top of one that has not landed.
7. The living band and the cover: no organ is driven outside its range; machines are parked, never switched off by
   Omni-Compass; it never evicts or moves a pod.
8. One writer: if anyone else changes a knob, Omni-Compass stops writing it and leaves it alone.
9. Everything is logged: every read, decision, write and reason goes to the audit log.

**Reading the log.**

| Line | Meaning |
|---|---|
| `gate: a sense is blind` | a reading failed; nothing is given back until it returns |
| `gate: pods scaling up` | pods first, machines after |
| `decision failed (n in a row)` | the cluster could not be reached; nothing was written; turn it OFF for native |
| `decided_by: compass` | the compass set the wires this decision |
| `decided_by: fail_up` / `blind_fail_up` | the service crossed the 0.95 wall, or a sense went blind: full capacity at once |
| `decided_by: thermal_hold` | the card reported a heat slowdown; nothing was tightened |
| `foreign_writer` | someone else changed a knob; Omni-Compass now observes only |
| `restored ... ok: true` | the OFF switch put every setting back and read it back |

## 12. Maintenance, Upgrades and Security

- Run `python3 verify.py` after every upgrade; it must end `VERIFICATION: PASS`.
- Upgrade in watch mode first; take the levels again from level 1.
- The container runs non-root, read-only, with no capabilities; the Kubernetes identity has only the permissions of
  the level you run.
- The GPU governor needs root only for `nvidia-smi -pl` and `-lgc`.
- Report a security issue as `SECURITY.md` describes.

---

# PART VI - PROVING IT

## 13. Paired Runs and Receipts on Your Own System

1. **Paired runs.** Run your service the same way twice, once native and once with Omni-Compass on top, back to back
   on the same machines, the order rotated, at least 5 times (10 for a result you publish). `scripts/kind_paired.sh`
   and `tools/live_reps.py` do this on Kubernetes; `scripts/gpu_rented_run.sh` does it on a GPU box, in one command:
   wire check, smoke, the six organisms with the card inside, then the preregistered confirmation.
2. **The switch drill** after every run: turn Omni-Compass OFF; confirm every setting is back at its recorded
   original; turn it ON.
3. **The receipt.** Each gauge: native, Omni-Compass, the change, the 95% interval of the difference, and whether the
   interval excludes zero. A change is proven only when it does.
4. **The label, by rule written before the run:** SUPERIOR WITHIN GUARDRAILS / ENERGY IMPROVEMENT WITH SERVICE
   TRADEOFF / NONINFERIOR / NOT ESTABLISHED / WORSE / INVALID. Guardrails: work not lower by more than 1%; the share of
   time outside the service line not higher by more than 1 percentage point. The band-first rule is stricter: no win
   is claimed while the time outside the service line is above native's.

**At scale (simulated).** The six organisms run on GitHub's machines (Actions, workflow `six`) or on any machine
(`bash scripts/scale_ladder.sh`) at 1, 10, 100 and 1,000 paired runs and at 1, 10, 100 and 1,000 copies of each
organism on one clock. Real Kubernetes runs on GitHub's machines (workflow `benchmark-reps`); the six organisms with
a real cluster inside as one more muscle run in `six-kube` (1 to 100 copies on GitHub) and `big-organism` and
`big-organism-detached` (1,000 copies on a rented machine).

5. **Preregister, then run.** The arms, the knob, the cover, the gauges and the readings are written before the first
   counted run (`docs/*_PREREGISTRATION.md`); the rules are frozen on one tuning case and then applied unchanged to
   untouched cases. A rule changed after a result is a new version of the engine (section 15), never a footnote.
6. **The clock rule.** An organism must keep its window. `tools/run_kil.py` records how long after the window its last
   step ended; the report shows it as "organism behind its window (s)", shown and not judged, and marks a repetition
   **OFF THE CLOCK** when either arm ended more than 5% of the window late, because its last steps then saw a cluster
   whose load schedule had already ended. The pairing stands (both arms slip alike) and the mark stays on the cell. The
   remedy is a longer window for that size on that machine, never a faster reading of the same run.
7. **Every row, losses included.** A row that went against Omni-Compass is reported with the others. If Omni-Compass
   loses, the first suspect is our own wiring, native setup or scoring; that is fixed and the test run again, and the
   loss stays in the record. A benchmark may be left unpublished; it is never published with rows cut out.
8. **The raw files live with the code.** Every finished run's files (capture, response times, audit log, controller
   log, one SHA-256 manifest per repetition) are copied into `results/live/raw/run-<id>/` by the `archive-run`
   workflow (one run id per line in `.github/archive_request.txt`; a run still going is left for a later pass), and
   every table names the runs and the commit it was made from.

## 14. Evidence Classes and How to Read a Result

| Class | Rung | What it is | What it can show |
|---|---|---|---|
| T / V | E1 | deterministic tests, proofs, Python against the C++ twin | the law is what it says, and both languages agree |
| S | E2 | simulation on a modelled plant | whether the law helps the model, and where it breaks |
| L | E3 | real software (Kubernetes on kind), no hardware meter | real decisions on real software; energy there is a declared model |
| P | E4 | a physical meter (the GPU's own power reading) | the hardware's own answer |

Read every number with its class beside it. A simulation number is never quoted as a hardware result. When a
receipt's energy line is modelled, the receipt says so.

## 15. The Frozen Engines and the Three-Run Rule

**The engine is frozen, and every freeze has a fingerprint.** The engine is the compass law
(`omnicompass/compass_law.py`), the live controllers (`omni_controller/`), the realms with their muscles and six
organisms (`realms/`), and the runners of the independent simulators (`tools/run_kil.py`, `run_citylearn.py`,
`run_pandapower.py`). `OMNI_V1.json`, `OMNI_V2.json` and `OMNI_V3.json` hold one SHA-256 per file and one digest over
all of them. Any change to a rule, a gain, a guard, a preset or a muscle makes **the next version**, and every result is
run again on it; no result is ever read across versions. When the engine is declared final, the engine that stands then
is published as Omni-Compass 1.0 and the older fingerprints go to `docs/history` as the road to it, never as a second
product.

| Engine | What changed | Fingerprint | Results read on it |
|---|---|---|---|
| **v1** (`docs/OMNI_V1.md`) | the compass law, the controllers, 656 muscles in 46 families, six organisms; the power-grid runner added inside the version without touching any other engine file | `ccc7fbdf8b312ed7…`, 38 files | the six Kubernetes tests A/B/C, the six organisms with the cluster inside, the big organisms, Azure steady and burst, CityLearn, the power grid, the robot arms, the modelled realms |
| **v2** (`docs/OMNI_V2.md`) | v1's law, controllers and runners byte for byte; the catalog grown to 945 muscles in 59 families with thirteen new presets | `OMNI_V2.json` | the modelled realms (Physics and the tower read a service tradeoff: the cause was found and made v3) |
| **v3** (`docs/OMNI_V3.md`) | v2 plus the slack gate on speed knobs (a motion axis busy more than half the time at full speed keeps its speed native) and the marine preset | `b53d05449ee04c4b`, 40 files | the modelled realms A/B/C (every organism superior within guardrails, 0 worse), the grid at 1 and 10 copies, the cluster inside the organisms at 10 and 100 copies, the database A/B/C, the robot arms A/B/C, CityLearn A/B/C; the Kubernetes six tests, the power grid, Azure and the 1,000-copy organisms running |

```
python3 tools/omni_version.py                   # this checkout: omni-v3, omni-v2, omni-v1, or every file that differs
python3 tools/omni_version.py --commit <sha>    # the engine at the commit any result ran on
```

A commit that holds every engine file but one not yet written reads as that version with the file named ("omni-v1, 37
of 38 files, all v1 bytes; not yet in this commit: tools/run_pandapower.py"): a v1 result for every test but the one
that runner serves, which could not have run there. Every table made by rule checks each run's commit against the
fingerprint and heads itself with a warning if any run is not the engine it claims or if the three are not separate runs.

**The three-run rule.** Every benchmark runs as **A, B and C**, three separate GitHub runs on the same frozen bytes.
Every judged row gets one of three readings, and all three runs are shown beside it:

- **Confirmed better** or **confirmed worse**: the same sign in all three runs, each with its 95% interval clear of
  zero.
- **No difference beyond the noise**: in at least one run the interval includes zero, so native and omni could not be
  told apart on that measure. That is the result, stated as such, with the count of runs it holds in.
- **The runs disagree**: runs clear of the noise point different ways. The test itself is then unstable on that
  measure, and it is looked into before anything is claimed.

Nothing reads "not confirmed". The tables are made by rule, never by hand (`tools/confirm_abc.py` for the paired
Kubernetes and Azure tests, `pgbench_abc.py`, `mujoco_abc.py`, `pandapower_abc.py`, `citylearn_abc.py`; a
deterministic simulator's three runs must reproduce each other to the digit, and a score reads "the runs differ" when
they do not), and `tests/test_confirm_abc.py`, run by `verify.py`, proves the rule on fixed cases.

**The Omni index** (`tools/omni_index.py`, `results/OMNI_INDEX.md`) is the one combined number. Every measure of every
test is a ratio oriented so that above 1 is better for Omni-Compass on top of native: work (more), speed (a lower
response time), machines (fewer), energy (less). A test's index is the geometric mean of its ratios, a category's the
geometric mean of its tests, the headline the geometric mean of the real categories, each weighted the same. A measure
enters only as its three-run reading allows: confirmed better or worse counts as the geometric mean of the runs'
ratios; no difference beyond the noise counts as exactly 1. Modelled muscles are shown beside the index, never inside it.

## 16. Results to Date

Every result below is Omni-Compass **on top of** a native system against the same native system alone, with the same
work in both arms, read by the three-run rule of section 15, on the engine named. Losses are in the tables beside the
gains. The whole list, benchmark by benchmark with its native engine, its knob, its gauges and its file, is
`docs/REGISTER.md`; the program that takes every benchmark to full size is `docs/PROOF_PROGRAM.md`.

**The one number.** The Omni index over the real categories confirmed three times: **+19.7%** (real Kubernetes on v3 +25.5%,
the real database on v3 +14.2%; Azure and the card join as their three-run tables land).

| Result | Engine | Class | Reading | Source |
|---|---|---|---|---|
| **Real Kubernetes, all four in one run** (load up and down one step at a time, 10 pairs × 3 runs) | v1 | L | work inside the response line **+42% to +48% in all three runs, confirmed better**; p95 −57% to −63% confirmed better; failed requests −12% to −13% confirmed better; machines no difference beyond the noise | `results/live/V1_ALL_FOUR.md` |
| **Real Kubernetes, steady work in steps** (10 pairs × 3 runs) | v1 | L | p95 **−65% to −69%** and time over the line confirmed better; machines −1.5% to −3.4% confirmed better; failed requests zero in both arms | `results/live/V1_STEADY.md` |
| **Real Kubernetes, demand that wanders** (10 pairs × 3 runs) | v1 | L | p95 **−56% to −60%** confirmed better; failed requests confirmed better; modelled standby energy −0.4% to −0.8% confirmed lower | `results/live/V1_WANDERING.md` |
| **Real Kubernetes, faults** (a machine down, a spike, a runaway pod, a blind probe, 10 pairs × 3 runs) | v1 | L | p95 **−61% to −64%** confirmed better; failed requests, machines and energy no difference beyond the noise | `results/live/V1_FAULTS.md` |
| **Real Kubernetes, a queue of batch jobs** (cruise, then the emergency brake, 10 pairs × 3 runs) | v1 | L | machines **−15% to −24%** and modelled energy −11% to −17% confirmed better; p95 no difference beyond the noise | `results/live/V1_BATCH.md` |
| **Real Kubernetes, fairness** (a noisy neighbour on the same workers, 10 pairs × 3 runs) | v1 | L | no difference beyond the noise on every row: Omni-Compass neither helps nor hurts the neighbour | `results/live/V1_FAIRNESS.md` |
| **The same six Kubernetes tests on v3** (10 pairs × 3 runs each) | v3 | L | the same readings as v1, the controllers being v1's bytes: all four work inside the line +35% to +49%, p95 −47% to −66% across steady, wandering, all four and faults, failed requests −9% to −14% where they occur, steady machines −1.5% to −2.9%, batch machines −19% to −23% and standby-model energy −13% to −16%, all confirmed better; fairness no difference beyond the noise on every row | `results/live/V3_STEADY.md`, `V3_WANDERING.md`, `V3_ALL_FOUR.md`, `V3_FAIRNESS.md`, `V3_FAULTS.md`, `V3_BATCH.md` |
| **The six organisms with the real cluster inside**, 1 to 1,000 copies, 5 paired repetitions a cell (3 at 1,000) | v1 | L + S | 98 of 100 cells: p95 and time over the line better in every cell; 0 gauges worse beyond the noise except a rounding-level work loss (−0.0003%) and HPA replicas +0.7% in one cell; machines stay at 6 in both arms (no autoscaler under kind); the Physics realm and the tower at 1,000 copies off the clock in 2 of 3 repetitions (marked) | `results/live/V1_SIX_KUBE.md` |
| The same at 10 and 100 copies | v3 | L + S | 12 cells, 5 pairs each: every cell better on 4 to 6 gauges, worse on none beyond the noise except a rounding-level work loss in 4 cells; the stack at 100 copies off the clock in 4 of 5 repetitions (marked) | `results/live/V3_SIX_KUBE.md` |
| **The big organisms at 1,000 copies on a rented machine**: the tower (3 of 3) and the four stacked (3 of 3, detached) | v1 | L + S | tower: p95 **−95%** (4.1 s → 0.2 s) and time over the line −99.7% clear of the noise, machines 6 in both arms, energy −0.2%, work rounding-level worse, repetition 3 off the clock; stack: p95 **−74%** and p99 −83% clear of the noise, the compass arm 300 to 615 s past the 2,880 s window in all three (marked OFF THE CLOCK; native kept the clock), which is why the v3 stack runs with a 10,800 s window | `results/live/V1_BIG_ORGANISM.md` |
| **Azure AKS, the bill, steady load**, 4 workers, 5 pairs | v1 | L (a real bill) | no difference beyond the noise on any gauge; the bill −4.7% with its interval across zero; a fleet of 4 cannot show the lever (10.1) | `results/live/V1_AKS_STEADY.md` |
| **Azure AKS, the bill, a burst sized to the cluster**, 4 workers, 5 pairs (repetition 4 lost its native cluster to an Azure API error in the first attempt and was run again by itself) | v1 | L (a real bill) | the bill +5.0% with its interval across zero; machines, p95 and failed requests inside the noise; p99 −34% clear of the noise in this one run; B and C to follow | `results/live/V1_AKS_BURST.md` |
| **PostgreSQL behind PgBouncer, the three untouched workloads**, 3 pairs × 3 runs | v3 | L | connections held open **−61% to −72% confirmed better** on `select` and `tpcb_hot`, the runs disagree on `simple_update`; host CPU-seconds **confirmed worse** on all three (+14% to +28%, the compass's own cost, counted against Omni-Compass); work and latency no difference beyond the noise | `results/live/V3_PGBENCH.md` |
| **The 945 muscles and six organisms, modelled**, A/B/C | v3 | S | reproduced to the last digit in 3 of 3; 0 muscles worse; **every organism superior within guardrails** (work per energy +0.1% to +0.3%, work unchanged, time over the line not above native's); on v2 Physics and the tower read a service tradeoff, which the slack gate corrected | `results/realms/REALMS.md` |
| **The organisms at 1, 10, 100 and 1,000 copies**, 1 to 1,000 paired runs a cell, 84 of 90 cells | v3 | S | every organism superior within guardrails in every cell of 10 runs or more; work per energy +0.07% to +0.37%, the same figure at every size; the six cells left (100 and 1,000 runs at 1,000 copies) are beyond the machines available | `results/scale/GRID.md`, `results/scale/receipts/` |
| **Power grid: 11 SimBench grids solved by pandapower**, both load models, A/B/C | v1 and v3 (the same table to the digit) | S | with ZIP loads the energy the loads drew confirmed better in all 11 (−1.3% to −1.5%) and the net import in all 11; losses confirmed better in 7 and **worse in 4** (the rural and semi-urban grids with their own generation, +0.6% to +1.5%); tap operations fewer in 10 grids, 4 → 8 a year in one (confirmed worse, the declared cost); no grid more often outside its band | `results/live/V1_PANDAPOWER.md`, `V3_PANDAPOWER.md` |
| **Robot arms, MuJoCo Menagerie**, A/B/C | v1 and v3 | S | where Omni-Compass moved (Gen3, Panda): peak torque −29% and −10%, tracking error −21%, energy per takt −0.8% and −0.5%, confirmed better; the Panda's copper loss +14% **confirmed worse**; UR5e and iiwa 14 left native by the paired physics trial | `results/live/V1_MUJOCO.md`, `V1_MUJOCO_PANDA.md`, `V3_MUJOCO.md` |
| **CityLearn, every district it ships**, A/B/C | v1 and v3 | S | 11 battery districts: electricity bought, daily peak and daily unevenness confirmed better in all 11, carbon in 8; the bill **worse in 7** (the 2023 districts) and ramping worse in 7; 71 score-rows better, 33 worse, 1 where the runs differ (the simulator's own variation); 3 districts with nothing to move; 8 the simulator cannot run | `results/live/V1_CITYLEARN.md`, `V3_CITYLEARN.md` |
| **Scale**: the controller governing 50, 500 and 1,000 simulated nodes (KWOK), decision time and correctness | every push | L | runs on every push | `results/scale/` |
| GPU, one card and the card inside the organisms | earlier card controller | P | **obsolete**: every earlier card result ran on a controller since replaced; the one-card, card-inside-1,000-copies and eight-card runs are run again by the founder on rented cards after the CPU and cloud work, at one named commit | `docs/GPU_PREREGISTRATION.md`, `docs/GPU_RUN_GUIDE.md` |

**Running now** (7 October): the four stacked at 1,000 copies on the detached machine,
and Azure steady and burst on the fleet of several machine families (the first two dispatches were refused by the
subscription's family allowances before any arm ran; the fleet is rebuilt from the families the survey shows allowed). **Queued, in order, in `docs/REGISTER.md` section 4**: drone swarms and
defense edge (PX4 and ArduPilot multi-vehicle, Crazyswarm), databases and caches at large (YCSB, HammerDB), Spark,
Kafka, Redis, OpenSearch, fio, Open-RMF, the 24-hour robustness run, spacecraft attitude and thrusters (Basilisk),
station-keeping (Orekit, GMAT), constellations, rockets (RocketPy, OpenRocket) and combustion (Cantera). Pure physics
solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) are not benchmarked: they have no controller and no knob, so Omni-Compass
has no place on them; their value is the HPC cluster that runs them.

---

# PART VII - CODE, TWINS AND TERMS

## 17. License and Commercial Terms

The software and this manual are licensed under the Omni-Compass Evaluation License (`LICENSE`): evaluation and
simulation use only. Everything else - commercial use, production use, operating any system beyond evaluation,
redistribution, a hosted or managed service, incorporation into a product or service, or using the software or its
results to build a competing product - requires a written Omni-Compass Enterprise License signed by The Omni-Compass
LLC and paid for. Patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. No patent or trademark license is granted for any other use. Contributions are accepted only on the
terms in `.github/CONTRIBUTING.md`, which assign their rights to The Omni-Compass LLC.

## 18. Python, C++ and the Seal

The laws are twinned: each has a Python version and a C++20 version that give the same answers, proven by a parity
test on every build (`cmake -S cpp -B cpp/build && cmake --build cpp/build`).

| Law | Python | C++ | Proven by |
|---|---|---|---|
| core engine | `omnicompass/core.py` | `cpp/src/core.cpp` | 500 frozen fixtures |
| governor | `omnicompass/adapter.py` | `cpp/src/governor.cpp` | `tests/test_cpp_governor_parity.py` |
| safety shield | `omnicompass/shield.py` | `cpp/src/shield.cpp` | `tests/test_cpp_shield_parity.py` |
| HPA replica law | `fleet/harness.py` | `cpp/src/hpa.cpp` | `tests/test_cpp_hpa_parity.py` |
| closure law | `omnicompass/closure.py` | `cpp/src/closure.cpp` | `tests/test_cpp_closure_parity.py` |
| conveyance law | `omnicompass/conveyance.py` | `cpp/src/conveyance.cpp` | `tests/test_cpp_conveyance_parity.py` |
| nervous system | `omnicompass/nervous_system.py` | `cpp/src/nervous_system.cpp` | `tests/test_cpp_twins_parity.py` |
| compass and ledger | `omnicompass/compass.py`, `storage.py` | `cpp/src/compass.cpp` | `tests/test_cpp_twins_parity.py` |
| GPU governor rules | `omni_controller/gpu_governor.py` | `cpp/src/gpu_rules.cpp` | `tests/test_cpp_twins_parity.py` |

The seal (`results/SEAL.json`) holds the SHA-256 fingerprint of every twinned file, written only after every parity
test passes. `verify.py` fails, naming the file, if any sealed file changes afterwards. The compass law
(`omnicompass/compass_law.py`) and the two-wire GPU governor are in Python today; their C++ twins are next.

---

# BACK MATTER

## Glossary

| Term | Meaning |
|---|---|
| Antagonist pair | the up side and the down side of a muscle's control, each with its own gain |
| Authority | how far the nervous system lets an organ move this decision |
| Band | a reading's or a knob's safe range |
| Compass | the band seen as a position from 0 (calm) to 1 (the line), with its bottom in the middle |
| Confirmed better / confirmed worse | the same sign in all three runs (A, B, C), every 95% interval clear of zero |
| Cover | a knob's hard range; every write is clipped to it |
| Cushion | the 5% at each edge of the compass, 10% in all |
| Fail up | the return to full capacity the moment service crosses the wall or a sense goes blind |
| Governor | the process that reads, decides and writes; Omni-Compass |
| Muscle | any machine, service or controller Omni-Compass reads and sets |
| Native | the system as it runs without Omni-Compass |
| No difference beyond the noise | an interval over zero in at least one run: native and omni could not be told apart; the result, stated as such |
| Off the clock | a repetition in which either arm ended more than 5% of its window late; marked, the pairing stands |
| Organism | a set of muscles run together on one clock |
| Omni index | the one combined number: the geometric mean of every real category's work, speed, machines and energy ratios, each read by the three-run rule |
| Omni v1, v2, v3 | the frozen engines, fingerprinted file by file; a result belongs to the engine its commit carries |
| Plug | the two-way connection to one muscle: read, write, read back, restore |
| Pool (Azure) | one machine family under Azure's autoscaler with its own ceiling; several pools make the fleet |
| Profile | a named set of the compass's settings for one kind of work: service (the default) or batch |
| Race | full speed at once while work waits, so a burst is never served slowly |
| Speed floor | the clock a card reaches on its own while busy, learned from its own meter; the governor never sets the ceiling under it |
| Receipt | the paired record of native against Omni-Compass for one run |
| Snapshot | a knob's value read once before the first write; the restore point |
| The runs disagree | runs clear of the noise point different ways; the test is unstable on that measure and is looked into |
| Wire check | the test that proves every wire follows, reads back and returns before anything runs |
| Work per energy | work done divided by energy used; the primary outcome |

## Appendix A - Command Reference

| Task | Command |
|---|---|
| Verify everything | `python3 verify.py` |
| Six organisms, simulated | `python3 tools/run_scale.py --runs N --scale K --out <dir>` |
| The full ladder | `bash scripts/scale_ladder.sh` |
| Two-wire card, modelled | `python3 tools/run_gpu_card.py <dir> [fresh]` |
| GPU wire check | `sudo python3 tools/gpu_wire_check.py --gpu 0` |
| GPU, whole benchmark in one command | `sudo nohup bash scripts/gpu_rented_run.sh > run.log 2>&1 &` |
| The six organisms with the real card inside | `python3 tools/run_hil.py --out <dir>` |
| GPU governor, two wires | `sudo python3 -m omni_controller.gpu_compass --mode watch|cap ...` |
| Kubernetes, watch | `kubectl apply -f deploy/install/omni-compass.yaml` |
| Kubernetes paired runs | `scripts/kind_paired.sh`, then `tools/live_reps.py` |
| OFF (Kubernetes) | `touch /tmp/omni.kill` |
| OFF (GPU) | `sudo touch /tmp/omni-gpu-kill` |
| The whole harness OFF, ON, status, watchdog | `python3 tools/omni_switch.py off|on|status|watchdog` |
| Seal check | `python3 tools/seal.py --check` |
| Which engine a checkout or a commit carries | `python3 tools/omni_version.py [--commit <sha>]` |
| The three-run table (Kubernetes, Azure) | `python3 tools/confirm_abc.py "<title>" raw/run-<A> raw/run-<B> raw/run-<C> --out results/live/V3_<TEST>.md` |
| The three-run table (database, robots, grid, buildings) | `tools/pgbench_abc.py`, `tools/mujoco_abc.py`, `tools/pandapower_abc.py`, `tools/citylearn_abc.py`, the same arguments |
| The six organisms with the cluster inside | `python3 tools/six_kube_report.py <raw dirs> --out results/live/V3_SIX_KUBE.md` |
| The grid of copies and runs | `python3 tools/grid.py` (reads `results/scale/receipts/`) |
| The Omni index | `python3 tools/omni_index.py` |
| The database benchmark, one run | `python3 tools/run_pgbench.py --out <dir>` (workflow `pgbench`) |
| The independent simulators | `python3 tools/run_citylearn.py`, `run_pandapower.py`, `run_mujoco.py` (workflows `citylearn`, `pandapower`, `mujoco`) |
| Azure, the bill | workflow `aks-metered`: `reps`, `arms`, `duration_s`, `load_steps`, `worker_pools`, `pool_prices`, `hpa_max` |
| The big organisms, detached | workflow `big-organism-detached`: `mode` start / collect / survey, `organisms`, `size`, `duration_s`, `commit`, `max_hours` |
| Archive a finished run with the code | add its id to `.github/archive_request.txt` and push (workflow `archive-run`) |
| Verify before a push, as GitHub runs it | `python3 tools/release_manifest.py` under Python 3.12: 0 FAIL |

## Appendix B - File Map

| Path | Contents |
|---|---|
| `omnicompass/` | the engine, governor, nervous system, shield, compass, conveyance law, the compass |
| `omni_controller/` | the Kubernetes controller and muscles; the GPU governors (one and two wires) |
| `realms/` | the 945-muscle catalog, the plant models, the realm harness, the compass on every muscle, the modelled card |
| `tools/` | benchmarks, receipts, the wire check, the scale ladder, manifests, seals |
| `scripts/` | one-command runs (GPU, Kubernetes, ladder) |
| `deploy/` | container image, install and permission files |
| `cpp/` | the C++20 twins |
| `results/` | every published result, with its raw files and checksums |
| `results/live/V1_*.md`, `V3_*.md` (+ `.json`) | the three-run tables, one per test, named by the engine they ran on |
| `results/live/raw/run-<id>/` | every archived run's files, one SHA-256 manifest per repetition |
| `results/scale/GRID.md`, `results/realms/REALMS.md`, `results/OMNI_INDEX.md` | the grid of copies and runs, the modelled realms, the one combined number |
| `OMNI_V1.json`, `OMNI_V2.json`, `OMNI_V3.json` | the frozen engines' fingerprints |
| `docs/` | this manual, the preregistrations, the evidence ledger, the theorem, the realm study |
| `docs/OMNI_V1.md`, `OMNI_V2.md`, `OMNI_V3.md` | what each engine is and every result read on it |
| `docs/REGISTER.md`, `docs/PROOF_PROGRAM.md` | every muscle, every benchmark run and every benchmark still to run; the program to full size |
| `.github/workflows/` | every benchmark as GitHub runs it: `benchmark-reps`, `six`, `six-kube`, `big-organism`, `big-organism-detached`, `aks-metered`, `pgbench`, `citylearn`, `pandapower`, `mujoco`, `archive-run`, `verify` |
| `LICENSE`, `NOTICE`, `LICENSES/` | the license and notices |

## Appendix C - The Equations in Full

    (1) dE/dt    = -alpha_E E + beta_int + beta_ext + v_eff
    (2) dU/dt    = mu U (1 - U^2) - (dE/dt)/E_max - lambda_U U + u,   |u| <= U_AUTHORITY = 25
    (3) dI_U/dt  = (1 - U) - sigma_1 E - delta S - lambda_I I_U
    (4) v_eff    = cos(omega_B t / 2) * c * tanh(lambda_0 + lambda_1 (U - 0.5) + lambda_2 S)
    (5) Phi(S)   = alpha_s S^2 / 2 + beta_s S^3 / 4 - delta S
    (6) dS/dt    = -dPhi/dS = delta - alpha_s S - (3/4) beta_s S^2
    (7) dB/dt    = B_dot ;  dB_dot/dt = gamma_c delta S - (omega_B / Q_B) B_dot - omega_B^2 B
    (8) R_B[n]   = finite-difference audit of (7); never fed back into the state

    Control (one micro step, zero-order hold across all four RK4 stages):
        u = clip(-f_U(x, t) + K_P (sigma - U), -U_AUTHORITY, +U_AUTHORITY),  K_P = 12,  sigma in {-1, +1}

    The compass (every muscle):
        p = position of the service reading in its band (0 calm, 1 the line)
        F = A tanh((K_P (p - center) + K_D v) / A),   K_D >= critical damping
        p >= 0.95  =>  full up force; down side held
        knob <- clip(knob + g_side F span, cover)

    The GPU governor (two wires, omni_controller/gpu_compass.py; one law, amendments 8 to 10):
        p = (mean response of the last 5 s - S) / (SLO - S),  S = SLO / 10;  p95 >= SLO, a failure, blind  =>  fail up
        fail up / race (utilization >= 0.95)  =>  ceiling = top clock, lid = start limit (the card's own settings)
        steady under the limit (saturated and drawing >= 0.97 of the limit)  =>  ceiling = the card's own busy clock,
            lid = start limit (the same watts, no knock-backs)
        otherwise:
            ceiling <- clip(ceiling + round(g_side F f_top / 15 MHz) 15 MHz, c_floor, f_top)
            c_floor = max(f_busy_own x floor, f_top - k* 15 MHz)       (never under the card's own busy clock,
                                                                         never past the verdict's deepest step k*)
            lid = clip(ceil(1.10 P_busy_own), envelope floor, start limit)
        g_up 0.10, g_down 0.0125, center 0.4, floor 1.00

    The verdict (omnicompass/verdict.py; every slow knob, the GPU ceiling and the Kubernetes machine count):
        reference r = the median cost per request at the deepest allowed step, measured fresh, n >= 30 requests
        trial t     = the median cost at one step past it, n >= 30 requests, under the same traffic
        allow the step  iff  t <= r (1 + a)  and  t <= c_native (1 + a),   a = 0.02
        a refused step is not tried again for R decisions (GPU R = 900; Kubernetes 120); the knob never goes past the
        deepest allowed step, so steps cannot add up beyond the allowance

    Kubernetes, the compass on the HPA target (omni_controller/controller.py; sets 30 and 31):
        target x in [0.6 x_op, x_op] (times the conveyed gain); the up force lowers x (more pods)
        p >= 0.95 from load (line breached, every sense live, nothing pending)  =>  x = 0.6 x_op at once
        p >= 0.95 from a blind sense or pods waiting for a lost machine           =>  x = x_op (native's own)
        fault over (p < center, line clean, nothing pending)                      =>  x = x_op at once, never held
        machines: one more at once past the wall; one back only when the verdict and the release gate agree
        g_up 0.10, g_down 0.02, release force < -0.2

    The productivity arithmetic (every receipt; manual section 3.4):
        work W equal in both arms;  G = C_native / C_omni - 1;  the same work needs 1/(1 + G) of the resources;
        saving S = G / (1 + G):  G = 1/3  <=>  S = 1/4

Parameter ranges, defaults and the proof of convergence: `omnicompass/core.py`, `docs/TRACKING_THEOREM.md`,
`docs/CANONICAL_ENGINE.md`.

## Appendix D - Metrics

Every gauge, where it comes from, and whether it is measured or modelled: `docs/METRICS_CATALOG.md`.

## Appendix E - Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Wire check `FAIL 3 up wire (lock)` | the driver or VM refuses clock locking | use bare metal or full passthrough; or run the one-wire governor |
| Wire check `FAIL 3 up wire (follows down)` | the card ignores the ceiling | update the driver; check for another management agent holding clocks |
| Wire check `FAIL 4 down wire` | the power limit is refused or capped by the board | check `nvidia-smi -q -d POWER`; run as root |
| `another copy of this test is already running` | a second copy was started | wait for the first or reboot; start once |
| `something else is using the GPU` | another process holds the card | stop it; the benchmark must run alone |
| Governor exit 5 | another writer changed a knob | find the other controller; Omni-Compass left its value alone |
| Governor exit 3 | a restore did not read back | restore by hand (`nvidia-smi -rgc`, `-pl <start>`); investigate before rerunning |
| `decision failed (n in a row)` | the cluster API is unreachable | turn it OFF; native runs on |
| Energy saved but p95 slower than native | the card served bursts below its own clock, or the lid sat under its own draw | read section 8.5; in the audit compare `telemetry.clock_mhz` while busy with `native_busy_clock_mhz`, and `want_w` with `native_busy_draw_w` |
| Fail-up in most decisions | `--slo-ms` set too low for the workload, or a stale feed read as blind | set `--slo-ms` from the workload's own target; check the feed's age |
| No saving at all, service unchanged | the card is saturated almost all the time (it races), or the service sits above the compass's center | expected on a card with no slack; the saving comes from the quiet stretches |
| Kubernetes: no machine ever given back | the release gate refuses (its reason is in the audit), or the service is above the compass's center | read `node_gate.reason` in the audit; check `--slo-ms` and the latency feed |

## Appendix F - Evidence Map

`docs/EVIDENCE_LEDGER.md` (every claim and its class), `docs/CLAIMS_REGISTER.md` (what is claimed and what is not),
`docs/GPU_PREREGISTRATION.md`, `docs/REALMS_PREREGISTRATION.md`, `docs/K8S_COMPASS_PREREGISTRATION.md`,
`docs/POSTGRES_PREREGISTRATION.md`, `docs/CITYLEARN_PREREGISTRATION.md`, `docs/PANDAPOWER_PREREGISTRATION.md` and
`docs/ROBOTICS_PREREGISTRATION.md` (the rules written before each run), `docs/OMNI_V1.md` to `OMNI_V3.md` (every
result by engine), `docs/REGISTER.md` (every benchmark and its file), `docs/STATE_OF_PLAY.md` (where everything
stands), `docs/HANDOFF.md` (every command in one page).

## Contact

Licensing, pilots and the Omni-Compass Enterprise License: **The Omni-Compass LLC.**

*Copyright (c) 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only.*

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
