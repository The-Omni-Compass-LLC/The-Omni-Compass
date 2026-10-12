# The max, formally: definitions, what the code guarantees, and what the runs measure

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page states the engine's default brain, the max (`realms/compass_arm_v5.py`, `V5CFG`, engine omni-v5 by
`tools/omni_version.py`), in definitions and properties. Each property carries its class: **V** a property of the code,
proved by reading the code path named beside it and checked by the runs; **S** measured on our own models; **L**
measured on real software; **P** measured by a physical meter. A V property is a statement about what the governor
writes; it is not a statement that a measured outcome follows. Measured outcomes are stated with their numbers and their
limits, and nothing on this page is claimed beyond them. The earlier formal results (`docs/TRACKING_THEOREM.md`,
`docs/FORMAL_STATUS.md`) belong to the earlier core engine's channels and are not restated here.

## 1. Setting

A **body** is a set of plants p_1, ..., p_n run on one clock of decisions k = 0, 1, 2, ... (15 s each in the
organisms). Each plant i has

- a template τ_i (compute_pool, thermal_zone, energy_storage, motion_axis, process_loop: `realms/plants.py`),
- one knob κ_i (capacity, setpoint, power or admission: the muscle's single wire),
- a **native controller** N_i, the plant's own law, unchanged by Omni-Compass: the pod autoscaler or the cluster
  autoscaler of a pool, the PI loop and staging of a cooled room, the dispatch of a battery site, the servo profile of
  an axis, the PI loop of a process,
- a state x_{i,k} and an exogenous input w_{i,k} (arrivals, heat from its own load, the site's own load, disturbance),
  drawn from the plant's seed, the same in every arm.

The plants are coupled through the body (`realms/harness.py`, `Body.couple`): with S_k the body's source power (every
plant that is neither a room nor a battery site) and Z_k the rooms' power, room z receives heat h_z · S_{k−1} and battery
site s receives load g_s · (S_{k−1} + Z_{k−1} − its nominal), where h_z and g_s are fixed by the body's calibration.

An **override** o_{i,k} is a set of key-value pairs that bounds what N_i may do at decision k: a floor and a cap on the
machines a pool's autoscaler may ask for, a setpoint for a room's loop, a reserve or a defended ceiling for a battery's
dispatch, a speed scale for an axis. The plant then steps by its own law under that bound:
x_{i,k+1} = f_i(x_{i,k}, N_i(x_{i,k}; o_{i,k}), w_{i,k}, coupling_k). The empty override leaves N_i exactly as shipped.

**Definition 1 (the two arms).** The native arm writes o_{i,k} = ∅ for every i and k. The Omni arm writes
o_k = G(y_0, ..., y_k) for k < K, where y_k is what the governor reads at decision k and K is the decision at which the
governor goes silent (in every run, K = 0.8 × the run's decisions), and the lease's walk back after K (Property V5).
Both arms run the same plants, the same seeds and the same inputs.

**Definition 2 (a governor, and a collection of tools).** A rule G is a **collection of separate tools** if there are
maps g_1, ..., g_n with o_{i,k} = g_i(y_{i,0}, ..., y_{i,k}) for every i and k: each muscle's bound depends on that
muscle's readings alone. G is **one governor over the body** if for some plant i the bound o_{i,k} depends on the
readings of another plant j ≠ i.

**Definition 3 (a twin).** The twin T_i of a plant i is the same plant model, built from the same row and seed, fed the
same exogenous input, run under N_i alone with no override. The pools' twins run inside the governor
(`Bone.__init__`, `Bone.advance_twin`); a twin is the governor's model of what native does with that plant.

**Definition 4 (room on a line).** The lines of a body are the battery sites' connections and the rooms' cooling. For a
line ℓ with distance to its limit gap_ℓ (the connection's limit plus what its battery can still clip, less its import;
or a room's cooling capacity less its command, and its degrees in hand), one-decision climb up_ℓ (the larger of line_z
times its step-to-step spread, the largest climb it has shown, and a prior of 5% of the line) and load per W of the
body's power a_ℓ, the room over r decisions is

  R(r) = min over ℓ of (gap_ℓ − √r · up_ℓ) / a_ℓ   (`Bone.room`, `Bone.room_for`),

the power the body may still add, read r decisions ahead.

## 2. What the code guarantees (class V)

**Proposition 1 (V). The max is one governor over the body.** In `max_body_step`, the floor written on a pool is
max(now + can, base), where can is the number of machines whose idle power fits in min(R(1), R(r) − used); R reads
every battery site and every room of the body, and `used` is what was granted to the pools decided before it in the
same decision. So the bound on one pool depends on the readings of the body's sites, rooms and other pools: by
Definition 2, the max is one governor, not a collection of tools. No set of separate tools has this property, however
many run at once. ∎

**Property V1 (one wire).** Every override the max writes uses only its muscle's own key: {floor, cap} on a pool wired
by capacity or setpoint; {setpoint} on a room wired by its setpoint; {setpoint} or {capacity} on a battery site wired by
that knob; {capacity} on an axis alone (inside a body an axis keeps its everyday speed); nothing on any other muscle.
Proof: every branch of `max_apply`, `max_hold` and `max_body_step` writes only these keys. ∎

**Property V2 (never fewer machines than native asks for).** For every pool i with a twin, at every decision k < K, the
count its autoscaler is asked for is never below the twin's: a floor written is ≥ m(T_{i,k}), and a cap written is
≥ max(m(T_{i,k}), n_min), where m counts machines in service and starting. Proof: `max_ask` sets base = m(T_{i,k}) and
want = max(forecast, base); `max_body_step` writes floor = max(now + can, base), and on a shortfall keep ≥ base. The
pool's own law is a function of its own arrivals and settings only, so its twin runs exactly as the native arm's pool
does: m(T_{i,k}) is the count native asks for at that decision. ∎

**Property V3 (native at its limit is left alone).** Under the max, the override of every muscle wired by power or
admission, of every process loop, and of every axis whose machine has no speed above its everyday setting is empty at
every decision: native already runs them at the top of their range. Proof: `max_ask` returns nothing for them and
`max_body_step` writes ∅. ∎

**Property V4 (grants come out of the room the lines have).** At a decision with R(1) ≥ 0, the idle power of the
machines the max adds, summed over the body, is at most R(1), and the machines of a pool that take r decisions to start
are granted only out of R(r) less what was already granted. With R(1) < 0, what the max added goes back, the pools
holding the most first, never below each pool's twin (V2), and no room is pulled below its operator's setpoint. Proof:
`_units`, the running decrements of r_src, r_all and used, and the shortfall branch of `max_body_step`. ∎
*Limit, stated with it:* R is a forecast. A line that climbs further within one decision than any climb it has shown,
while power granted earlier is still in service (power is handed back one decision after a line shows the need), can
still be carried over its limit. Section 4 gives how often that happened.

**Property V5 (the lease: everything handed back).** If the governor goes silent at decision K, every override moves
1/(K + W − k) of the way to its native value at each decision k ≥ K and is native from decision K + W − 1, W = 24
(`walk_back`; a floor that only held a pool at native's own count is let go at once). Every run checks every knob on
every seed (`restore_ok`); a muscle or organism that fails is labelled INVALID. In the official table every muscle and
every organism passed. ∎

**Definition 5 (the readings).** For each seed s, the paired difference is d_s = Omni_s / native_s − 1 for work and
energy, and Omni_s − native_s (percentage points) for the share of decisions over the line. Over n seeds, the 95%
interval is mean ± t_{0.975, n−1} · sd / √n. A gain or a loss is a row whose interval is clear of zero; otherwise the
row reads no difference beyond the noise. Across runs A, B and C: the same sign in all three with every interval clear
of zero reads "better (or worse) in all three of our runs"; an interval across zero reads "no difference beyond the
noise"; clear intervals of opposite signs read "the runs disagree" (`tools/readings.py`, `tools/confirm_abc.py`).

## 3. What the runs measure (classes S, L, P)

- **S, the muscles alone, 1,107 muscles, preregistered seeds 3000-3009, both loads** (`results/realms_v5/`, commit
  `44aceb48ea30`, digest `9be48445438943c2`): 517 better, 421 at their limit on native (V3: the max writes nothing),
  169 no difference beyond the noise, **0 worse, 0 mixed**.
- **S, inside the organisms, the same seeds, three loads**: every organism better as a whole under every load, and
  **0 plants worse** in every organism under every load (0 of the 1,908 in the four stacked). Misses (the share of
  plant decisions over their line) fall 1.6% to 6.4% under each organism's own load, 0.9% to 3.5% under the climb (the
  load stepping 1 2 3 2 3 4 ... to twice its own) and 1.0% to 7.2% with work waiting in line, against 0.1% to 0.7%,
  0.0% to 2.1% and 0.1% to 2.1% for the engine before (digest `8d4f91f0`), which left 3 plants worse under the climb.
  Every row is reported in `results/realms_v5/REALMS_V5.md`.
- **L, real software**: `docs/THE_RECEIPTS.md`, receipt by receipt.
- **P, a physical meter on a real chip**: not yet produced on the current governor (`docs/THE_SEAT.md`, section 5).

## 4. The living body: why plants did worse, and the version that cures them (the engine since 12 October, night)

Found on development seeds only (7100-7299), never on the preregistered ones. Under the climb, rooms and UPS lines
reach their limits in both arms; a plant did worse when the Omni arm reached a limit a moment sooner, or when a sense
the brain read was wrong. Each cause, and the property of the code that removes it:

1. **A room snapped back.** A room cooled ahead of the heat, then returned at once to its operator's setpoint when the
   lines ran short: its own PI loop overshot warm of native, and once its cooling ran flat out the difference was frozen
   in. *V9 (the pedal lifted, never snapped):* a pull-down is handed back toward the operator's setpoint over the
   cooling's own reaction time. *V10 (no pull-down that cannot be held):* a new pull-down is granted only out of the room
   the lines have for that reaction time.
2. **A battery's charge counted as room after it ran out.** *V6:* a site whose battery covers its draw, but whose charge
   above its floor runs out within r + 1 + T decisions (T = 2: the heat of machines handed back reaches the rooms a
   decision later and their cooling answers over its own averaging, one more), has as room on its line only its limit
   less its whole draw, read at the draw's own climb.
3. **Machines handed back while a queue needed them.** *V7:* on a shortfall, a pool is never held below
   ⌈(λ_{k−1} + Q_k / Δt) / μ⌉.
4. **A room left warmer than native.** *V8:* every room has a twin: the same room under its operator's settings, warmed
   by native's heat (the body's source power with each pool's power replaced by its twin's). A room wired by its
   setpoint that reads warmer than its twin by e > 0 has its setpoint written at most t_set − e, unless its cooling is
   already flat out.
5. **A room that cannot cure itself.** *V11 (the body cures what a muscle cannot):* a room wired by its cooling units,
   a power or an admission gate, or whose cooling is flat out, and that reads warmer than its twin by e > 0, puts a heat
   debt e · C / (Δt · h) on the body (C its heat capacity, h its share of the body's source heat); the room the bone
   grants is bounded by minus that debt, so the machines the max added go back until no such room is warmer than
   native's.
6. **A battery that never timed its discharge.** *V12:* a battery wired by its power holds its charge while its line has
   room after the largest climb it has shown, line_z of its wobbles and a twentieth of its limit, and gives native's full
   power once the line could need it; it holds nothing until it has read its line for a window of decisions (20).
7. **A lock in the senses.** *V13 (a forecast starts at the first reading):* a plant shows its initial values before its
   first step; the jump from them to the first reading was taken as the line's largest climb ("never forgotten") and
   kept every battery's timed discharge shut for the whole run. Every forecast of a line now starts at the plant's first
   real reading, and the bone reads nothing before the body's first step.
8. **A twin that started wrong.** The body reads its sources at their nominal power before the first step; the room twins
   read zero, so for the first ten or so decisions they ran up to 0.3 °C apart from native's rooms and the body cured
   differences that did not exist. The twins now start from the body's own reading (V8, the definition above), and with
   the max writing nothing every room twin equals its room to the last digit, every decision
   (`tests/test_compass_arm_v5.py`).

The battery's admission gate stays native: deferring a site's flexible load to keep its line clear left part of that
work not caught up by the end of a run (work first).

Measured on development seeds 7100-7199, the four realms under the climb, 400 organism runs each way:

| | Plants worse | Misses (pp), the four realms | Work, the four realms |
|---|---:|---|---|
| the engine before (omni-v5, 8d4f91f0) | 19 | −0.109, −0.125, −0.005, −0.144 | +0.0013%, +0.0016%, +0.0000%, +0.0022% |
| V6-V10 only | 7 | −0.104, −0.110, −0.005, −0.137 | kept |
| **this version (V6-V13)** | **0** | **−0.206, −0.187, −0.143, −0.212** | +0.0008%, +0.0010%, +0.0000%, +0.0016% |

The misses fall about twice as far as before (in the Energy / Facility / Industrial body, from almost nothing to 0.14
points), and no plant in any of the 400 runs did worse than native. The work gained is about two thirds of the version
before: the heat debt hands back machines while a room that cannot cure itself is warmer than native's.

One lock is left, said plainly: a line that once jumped (a battery that stopped covering its site) is read as able to
jump that far again for the rest of the run, which keeps the max from adding machines on that line. Removing it (every
line's climb read on the site's whole draw) roughly triples the misses removed on the same seeds (−0.34 points), but in
36 of the 400 runs a machine pool whose queue sat at its limit then did more work and took one decision longer to clear
it, which our decision count reads as worse. That is the next version's work, and it enters the engine only as a new
version, every result run again on it, the founder told first.

## 5. Limits, stated plainly

- V properties bound what the governor writes. They do not by themselves bound an outcome on a line the governor does
  not control (section 4).
- R is a forecast (V4). A climb no line has shown before can beat it within the one decision power takes to be handed
  back.
- S results are our models. They are never presented as proof of a physical saving; the physical receipt is a P run.
- The twin is exact for a pool (its law reads only its own inputs) and for a room (its heat is the body's own source
  reading with each pool's power replaced by its twin's, so with the max writing nothing it equals the room to the last
  digit); with the max writing, a room twin is native's room under native's heat as the brain reconstructs it, not a
  meter.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
