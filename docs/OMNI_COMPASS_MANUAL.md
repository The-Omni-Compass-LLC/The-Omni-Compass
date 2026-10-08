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

**On this edition.** This edition is written for the referee and the underwriter as much as for the engineer. Every
result in it was run three separate times on a frozen, fingerprinted engine, under rules written before the first run, and
is reported with every loss beside every gain. Where a number is from a model it says so; where a test could not see an
effect it says so; where something has not been shown it says so, in its own section. The questions a careful reader will
ask are asked here first, in section 3.5 beside each result and in section 16.7 as a list, and answered where an answer
exists. Nothing in this manual asks to be believed on our word: every table names the runs it was made from, every run's
raw files are in the repository, and every table can be rebuilt from them by the tool it names.

**AJ Dubra**
Founder, The Omni-Compass LLC

## Preface: How to Use This Manual

| You are | Read |
|---|---|
| CEO, board member, investor | Foreword; Part I (sections 1-3); section 14 (evidence); section 15 (the frozen engines and the three-run rule); section 17 (license); the Executive Summary below |
| CTO, architect, head of platform | Parts I-III; section 9 (wiring levels) to plan the rollout; Part VI |
| The engineer wiring it | Everything, in order. Do not skip the wire check (section 8) or the watch level (section 9, level 1) |
| Auditor, diligence team | Part II (mechanism), Part VI (proof), Appendix C (equations), Appendix F (evidence map) |
| Referee, reviewer | The standards below; sections 13 to 15 (the method, the classes, the frozen engines and the three-run rule); section 16.7 (threats to validity, stated by us); Appendix F, "How to audit one result from this manual to its raw files"; then any table in `results/live/` and its preregistration |
| Underwriter, insurer | Sections 1.2 and 1.3 (do no harm, the pedals, the two switches); section 11 (the three ways a governor stops and what each leaves behind); section 12 (least privilege, supply chain); section 16.7 |
| Anyone who wants the whole list | `docs/REGISTER.md`: every muscle wired (945, by family), every benchmark run on every platform (Kubernetes, Azure AKS, GPU, CPU, UPS and batteries, buildings, power grids, robotics) with its result and file, and every open benchmark still to run, in order |

**Conventions.** `code` is a command, file or switch exactly as typed. "Native" means your system as it runs today,
without Omni-Compass. "Omni" (the second arm of every benchmark) means that same native system with Omni-Compass on top
of it; there is no third arm and no other name. "Muscle" means any machine, service or controller Omni-Compass can read
and set. "Knob" or "lever" means one setting on a muscle. "The band" is a knob's or a service reading's safe range; "the
cover" is a knob's hard range, which nothing Omni-Compass computes can leave. Every step that writes to a system is marked
**WRITES**. Every number carries its evidence class (section 14): **P** for a physical meter, **L** for live software with
no meter, **S** for a model of ours. A number from a model is never written as if it came from hardware.

**The standards every page of this manual keeps.** A referee or an underwriter reading this manual should expect, and
will find, the following discipline throughout, because it is the discipline the repository enforces on itself:

1. **Two arms, always.** Every benchmark compares native against omni, the same system with Omni-Compass on top, on the
   same machines, with the same work at the same moments. Omni-Compass is never run standalone and never compared as a
   competitor to the controller it sits on.
2. **Preregistered, then run.** The arms, the knob, its cover, the gauges, their directions and the readings are written
   down and committed before the first counted run (`docs/*_PREREGISTRATION.md`). Rules are frozen on one tuning case
   that is shown and never counted, then applied unchanged to untouched cases. Any amendment made after a result has been
   seen is written into the preregistration with its time and reason, and the table that carries the result says so.
3. **Three separate runs, one rule.** Every result is run three times as separate GitHub runs (A, B and C) on the same
   frozen engine, and every judged row reads exactly one of: confirmed better, confirmed worse, no difference beyond the
   noise (with the count of runs in which the interval crossed zero), or the runs disagree. The phrase "not confirmed"
   does not appear in this repository.
4. **Every row, losses included.** A row that went against Omni-Compass is in the table beside the rows that went for it.
   When Omni-Compass loses, the first suspect is our own wiring, native setup or scoring; when that is fixed, the test is
   run again and the loss stays in the record. A benchmark may be left unpublished; it is never published with rows cut.
5. **Nothing read across engines.** The engine is frozen and fingerprinted (`OMNI_V1.json`, `OMNI_V2.json`,
   `OMNI_V3.json`). Any change to a rule, gain, guard, preset or muscle makes the next version, and every result is run
   again on it. Every table made by rule checks the engine of each run it reads and refuses to mix them.
6. **The raw files live with the code.** Every finished run's files are copied into `results/live/raw/run-<id>/` with one
   SHA-256 manifest per repetition, and every table names the runs and the commit it was made from. Anyone with the
   repository can recompute every table from the files it names.
7. **Do no harm.** Omni-Compass moves a knob only where a paired trial on the muscle itself shows the muscle no worse for
   it (the verdict, `omnicompass/verdict.py`, with its 2% allowance). Where it cannot improve a knob, that knob stays
   native, and the result says "nothing for Omni to move".

**How this manual is organised.** Part I says what the governor is and where its value comes from, with the arithmetic
that turns "more work" into "a smaller bill". Part II is the mechanism: the engine's eight equations and its control
law, the closed-circle principle that keeps it inside its walls, the compass law that carries push and pull to every
muscle, and the two-way nervous system that decides how much authority each organ has. Part III is the harness: the
plug every muscle is wired through, the adapters, and the wire check that must pass before anything writes. Part IV
wires it onto a stack one level at a time and then stack by stack: Kubernetes on kind and on Azure, a database behind
its pooler, a message broker's consumer group, a cache's memory ceiling, the independent simulators, drone swarms and
the big organisms on a rented machine. Part V is operating it: the switches, the rules the governor keeps, the log, and
maintenance. Part VI is proof: paired runs and receipts, evidence classes, the frozen engines and the three-run rule,
the Omni index, and every result to date with its losses, followed by the threats to validity we state ourselves and the
open program. Part VII is the code, the C++ twins and the license. The back matter holds the glossary, every command,
the file map, the equations in full, the metrics, troubleshooting and the evidence map.

## Executive Summary

**What it is.** Omni-Compass is a supervisory governor. It sits on top of the controller a system already has, the
Kubernetes autoscaler, the GPU's firmware, the cooling loop, the battery inverter, the robot's servo, the grid's tap
changer, the database's connection pooler, the message broker's consumer group, the cache's memory ceiling, and it moves
only the settings those controllers already accept. It reads each muscle's own meter, computes one bounded force per
muscle from a single smooth law, and holds the service in the middle of its safe band rather than far below its limit.
The native controller keeps running exactly as shipped; Omni-Compass sets what it already exposes, and when Omni-Compass
stops, every setting goes back to the value it read once before its first write. It is never standalone and it never
competes with the controller underneath it.

**What it does for you.** Every running system keeps room "just in case": machines sized for the worst minute of the
day, a pool of connections held open for a load that comes once an hour, a consumer group sized for the quiet hours and
then overrun at the peak, a cache ceiling set once and left. Omni-Compass turns that room into one of two things, and the
operator chooses which: more work for the same resources, or the same work for fewer. The two are the same measurement
read from two sides (section 3.4): a third more work from what is already installed is a quarter off the bill.

**What has been shown, on the frozen engine Omni v3, three separate times each.** On real Kubernetes, six preregistered
tests of ten paired runs each (`results/live/V3_*.md`): work inside the response line **+35% to +49%** in every run of the
all-four test, the 95th-percentile response time **47% to 66% faster** across the steady, wandering, all-four and fault
tests, failed requests 9% to 14% fewer where load swings, machines 1.5% to 2.9% fewer at steady load and 19% to 23%
fewer on a queue of batch jobs, and beside a noisy neighbour no difference beyond the noise on any row. On a real
database behind its pooler (`results/live/V3_PGBENCH.md`): 61% to 72% fewer connections held open for the same work and
the same latency on two of three workloads, at a confirmed cost of 14% to 28% more CPU on the host, counted against
Omni-Compass. On a real message broker, Apache Kafka as shipped (`results/live/V3_KAFKA.md`): 16% to 21% more messages
inside the 500 ms line on all three untouched workloads, a 95th percentile of 9 to 14 ms against native's 1.6 s, no
message lost, at the confirmed cost of three to four times the consumers running. On a real cache, Redis as shipped
(`results/live/V3_REDIS.md`): 14% to 27% more requests inside the 2 ms line and a hit rate 14% to 27% higher on all three
untouched workloads, at the confirmed cost of a memory ceiling held at 200 to 270 MB against the operator's 64 MB, which
outweighs the gain in the index. On a real database's storage-engine cache, MongoDB as its publisher ships it under YCSB
(`results/live/V3_YCSB.md`): the cache given back by about half on two of four untouched workloads and by 13% to 37% on a
third, confirmed, with work inside the line, p95 and CPU inside the noise and no failed operation, at the confirmed cost
of 2% to 4% on the mean latency of the burst workload. In the modelled realms, 945 muscles
and six organisms (`results/realms/REALMS.md`): every organism superior within its guardrails, zero muscles worse, at
every size from 1 to 1,000 copies. On the independent simulators: a power grid's losses better in 7 of 11 grids and
worse in 4; robot arms' peak torque down 10% to 29% where Omni-Compass moved and left native where the paired trial said
not to; buildings' electricity bought and daily peak better in all 11 battery districts and the bill worse in 7; drone
swarms' energy a mission 7% to 20% lower with no late mission, near miss or collision. The one combined number, the Omni
index over the six real categories confirmed three times, stands at **+23.5%** (`results/OMNI_INDEX.md`): Kubernetes
+25.5%, the database +14.2%, messaging +166.9%, the cache −24.9%, the database's storage-engine cache +10.2% and the
database's buffer pool +12.2%, every category weighed the same and every row inside the noise counted as exactly nothing. The cache's category is negative because the memory it holds is the resource it
trades and reads worse by rule, even as its work and hit rate read better; the index does not hide that.

**What has not been shown, said plainly.** An energy or cloud-bill saving on real machines. Energy on kind is a
declared model, because the machines are containers on one runner. Azure's bill on a 4-worker fleet read no difference
beyond the noise on every gauge, which is the honest reading of a fleet too small to show one machine; the 40-worker
fleet that can show one is preregistered and has been refused by Azure's own cluster capacity in its region, each refusal
recorded. Every earlier GPU result ran on a controller since replaced and is obsolete; the card runs again on rented
hardware at one named commit. Each of these is an open item in section 16, not a footnote.

**How it stays safe.** It watches before it writes. It records every original setting before it acts and reads back
every write. It never writes past a knob's cover. It gives everything back the moment service crosses the wall or a
sense goes blind. It stops writing a knob the instant anyone else touches it. It moves a slow knob only after a paired
trial on the muscle itself shows no more than 2% cost. One OFF switch returns every setting to its original value; a
watchdog with a lease does the same if the governor is killed outright; and a separate kill switch, for security only,
turns the whole harness off in one human hand.

**How you know.** Every run produces receipts: native against omni on the same system, the same load and the same clock,
each gauge with its 95% interval, the raw files archived beside the code and fingerprinted. Results are labelled by a rule
written before the run, confirmed only when three separate runs agree, and reported with every loss in the table.

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
16. Results to Date (16.1 real Kubernetes; 16.2 the organisms with the cluster inside; 16.3 the bill on a real cloud;
    16.4 a real database, broker and cache; 16.5 the modelled realms and the simulators; 16.6 the one number and the
    table; 16.7 threats to validity, stated by us; 16.8 what is not yet shown, and the open program)

**Part VII - Code, Twins and Terms**
17. License and Commercial Terms
18. Python, C++ and the Seal

**Back Matter** - Glossary; Appendix A Command Reference; Appendix B File Map; Appendix C The Equations in Full;
Appendix D Metrics; Appendix E Troubleshooting; Appendix F Evidence Map; Appendix G Reproducing Everything; Contact

---

# PART I - THE GOVERNOR

## 1. What Omni-Compass Is

A governor on a steam engine does not build the engine and does not turn the shaft. It watches the speed and moves the
throttle so the speed stays in a band. Omni-Compass is that, for every machine you run.

It is a process on a host. It reads meters, steps a bounded mathematical law, and writes only the levers it has been
given. It is not the chip, not the GPU driver, not Kubernetes, not the building controller. Those keep running exactly
as they do today; Omni-Compass sets the values they already accept.

Three facts about that process fix what the rest of this manual can and cannot claim. First, it is **one process per
stack**, a controller (`omni_controller/controller.py` on a cluster; the harness's own controller on a database or a
cache) that wakes on a fixed period, reads the stack's own gauges through the stack's own interface, decides, writes
through the same interface, and reads back what the device took; it has no agent inside the pods, no kernel module, no
hook in the request path, so it can add latency to nothing it does not govern. Second, every lever it may touch is
**named before it starts**, read once into a snapshot, and handed back to that snapshot when it stops, is killed, or
loses a sense; a lever it was not given it cannot reach, because the plug for it does not exist. Third, it has a
**watching mode** in which it reads and decides and writes nothing, and every rollout begins there (section 9): the
first thing an operator learns about Omni-Compass on their own stack is what it would have done, in a log, with the
stack untouched.

What follows from those three is the shape of the evidence in Part VI. Because the native controller keeps running
underneath, every benchmark is the native stack against the same native stack with Omni-Compass on top, and never
Omni-Compass against anything else. Because the levers are the stack's own settings, every gain is one the operator
could have reached by hand, if they had been able to read every gauge every few seconds and move every knob without
ever being wrong; the claim is not a new mechanism but a steady hand on the mechanisms that exist. And because the
process is small and separate, its own cost (CPU on the host, reads of the API) is measured in every run and counted
against it where it shows.

### 1.1 Always on top of a native controller

The first design decision, and the one every other follows from, is that Omni-Compass is **supervisory**. It never
replaces the controller a system already has, never bypasses it, and never runs in its place. The Kubernetes
Horizontal Pod Autoscaler keeps scaling pods on its own CPU target; Omni-Compass moves that target inside a range the
operator allows. The cluster autoscaler keeps adding and deleting machines; Omni-Compass marks machines idle and lets the
autoscaler do the deleting. The card's firmware keeps boosting the clock and enforcing its power limit; Omni-Compass sets
the ceiling the boost may reach and the limit the firmware enforces. PgBouncer keeps handing connections to clients;
Omni-Compass sets its pool size through the pooler's own console. Kafka's consumer group keeps rebalancing partitions on
its own; Omni-Compass changes how many consumers are in the group, which is what an operator does. Redis keeps evicting by
its own rule; Omni-Compass sets the ceiling that rule works under.

This matters to a referee for a precise reason: every benchmark in this manual has exactly two arms, **native** (the
system with its own controller, as shipped and as the operator set it) and **omni** (the same system with Omni-Compass on
top). There is no third arm in which Omni-Compass replaces the controller, and no comparison in which Omni-Compass is a
rival to it. A gain is therefore always "what the governor added on top of what the native controller already did", and a
loss is always "what the governor cost on top of it". Nothing in the record is an argument against any native controller;
every native controller in this manual is a good controller that the governor sits on.

### 1.2 Do no harm: the verdict

The second design decision is that Omni-Compass must never make anything worse. This is not a slogan printed on a
report; it is a trigger inside the engine. Before Omni-Compass moves a slow knob (a machine given back, a card's clock
ceiling, a robot axis's speed, a drone's cruise override), it runs a **paired trial on the muscle itself**
(`omnicompass/verdict.py`): the muscle's own cost per piece of work is measured at native and at one step past the
deepest step already allowed, under the same traffic, with at least thirty pieces of work on each side; the step is
allowed only if the trial's median cost is no more than 2% above the reference and no more than 2% above the cost first
measured at native. A refused step is not tried again for a set number of decisions. Where no step passes, the verdict
reads **left native**, the knob is never moved, and the result for that muscle says "nothing for Omni to move". This is
why, in the robot-arm benchmark, two of four arms were left entirely native and are reported as such, and why in the
real Kubernetes tests machines were kept whenever one machine fewer made the requests slower in the trial. Gains are not
capped; the allowance caps only what may be spent to get them.

### 1.3 The pedals, the modes and the two switches

Omni-Compass drives a system the way a self-driving car drives itself: it feels, gauges and adjusts, with nobody in the
seat. The vocabulary is used the same way everywhere in this repository (`docs/MECHANISM_OF_ACTION.md`, "The pedals"):

- **Off (manual).** Omni-Compass is not driving; native runs alone. This is the native arm of every benchmark.
- **Watching.** Omni-Compass reads every gauge and logs the decision it would take, and writes nothing. Any difference
  between a watching arm and native is the cost of its being there (its CPU, its reads) plus noise, never a decision; a
  watching arm that writes anything fails its run. Watching is the first level of every rollout (section 9).
- **Autopilot.** The pedals: **idle** (no foot on the gas or the brake, calm traffic, the engine at its floor of two
  machines in service, ready for the next burst), **gas** (traffic climbs and capacity is added at once, never held back),
  **brake** (traffic falls and capacity is eased off a step at a time, never below idle), **reset** (the brake held to the
  floor: every setting the governor ever wrote is handed back to where native had it, read back, and the record removed;
  every benchmark arm ends with a reset and checks it).
- **Cruise.** For work that comes as a pile: when pods have waited for a place for two decisions in a row, every machine
  goes into service and stays there, without second-guessing, until the line has been empty for two decisions. In cruise
  the governor also stops its five-second floor reads, because every machine is already in service and the reads would
  only cost CPU on the machines the queue is using.
- **The emergency brake.** When the work is done and demand is at zero (the service at its autoscaler's own floor,
  wanting no more, at half its target or less), straight to idle in one move, with every safety check still holding.
- **The kill switch.** Separate from all of the above, and for **security only**: one switch in a human hand
  (`python3 tools/omni_switch.py off`, `omnicompass/master.py`) turns Omni-Compass's governing off across the whole
  machine at once, for anything rogue, or for anyone trying to drive a system through Omni-Compass's brain. Every
  governor hands back and exits; none starts while the switch is off. The reset is the end of a run; the kill switch is
  the end of trust.

The floor of two machines is an operator's number; the brake never takes a system below it, however hard it is pressed.
There is no ceiling: every machine the operator has is usable, and the protection is the band inside each machine.

### 1.4 Nothing is hardwired

Omni-Compass carries no table of per-stack special cases. One law (section 6) is written once and runs on every muscle
through one plug (section 8). The gains differ from muscle to muscle only through the muscle's declared physics: its
response time, its decision period and its cover. Where a rule was found not to work, it was removed, not switched off and
left in the code: the engine files are frozen and fingerprinted, and `verify.py` fails if any of them changes. A reader
who finds a behaviour in a result can find the exact lines that produced it, and will find no second path.

The rule has a practical consequence for anyone comparing Omni-Compass with a tuned controller. A tuned controller
carries, somewhere, a number that someone chose for one stack: a cool-down of five minutes, a target of 70%, a step of
two replicas. Each of those numbers is a bet that the stack will behave tomorrow as it did when the number was chosen, and
each is one more place where a reader has to ask whether the result was the law or the tuning. Omni-Compass has a handful
of such numbers, the centre of the band, the 5% cushions and the 2% do-no-harm line, and they are the same on every
muscle, written once in the law and declared in every preregistration. Everything
else the law needs (how fast the muscle answers, how often it may be moved, how far it may go) is read from the muscle's
own declaration in the catalog (`omnicompass/muscles.py`) or from the native controller's own settings at the start of the
run, never typed in by hand for a benchmark. When a benchmark needs a line, a cover or a chunk size (the MySQL pool moves
in the server's own 128 MB chunks, the Redis ceiling in notches), the number comes from the stack being governed and is
written in the preregistration before the first counted run, where a referee can see that it was not chosen after seeing
the result.

The second consequence is how the repository changes. A guard or a gain that turned out not to help is not left in the
code under a flag, because a flag is a second path that a later reader has to reason about and a later test has to cover.
It is removed, the removal is written in the changelog, and the fingerprint moves to the next engine version (section 15),
so that no result taken on the old path is ever read against the new one. The three fingerprints that exist, v1, v2 and
v3, are the whole history of such changes.

### 1.5 The word

The law is a **compass**: a band with a cushion at each wall, pushed to its middle by two antagonist forces, smooth,
never hammering. The repository uses that word and no other for it. Earlier dated records that used another word are kept
word for word, as records are; the current law is `omnicompass/compass_law.py`, `CompassLaw`.

The word was chosen for what the law does, not for decoration. A compass has a needle, a centre it is drawn back to, and
a card marked at the edges; it does not slam to a wall and stay there, and it does not chatter when the hand holding it is
steady. The law has the same three parts. The **band** is the range the gauge is allowed to travel, from 0 to 1 once the
reading is placed on it, with the operator's line at the top. The **cushions** are the last 5% at each wall, 10% of the
band in all: a reading inside a cushion is already too close to a wall, and the law treats it as such before the line is
touched rather than after. The **centre**, 0.5 by default, is where the needle comes to rest, and two forces bring it
there: a **pull** proportional to the distance from the centre, gentle near it and harder up the walls, like a spring;
and a **push** proportional to the speed at which the reading is moving, meeting whatever is shoving it (a load rising, heat
building) with an equal and opposite force and doubling as the friction that stops the needle sloshing past the centre
(the gain is chosen for critical damping: it glides to the centre and stops, with no overshoot and no ringing). Past the
upper wall the pull goes to its full force at once, and the down side may not act until the reading is back inside the
band: the law fails up, never down. The force itself is `A × tanh(raw / A)`: near the centre it behaves as a spring, in
proportion to the distance, and far from the centre it bends over and flattens into its maximum `A`, the law's authority,
so that no reading, however far out, can make the law ask for more than one full step. That flattening is what "never
hammering" means in code: there is no reading that produces a jump, and two readings a decision apart produce two forces
a small amount apart. Section 6 gives the rules in full and Appendix C the equations; the reader who only needs the
picture can keep the needle, the centre and the two cushions in mind and will not be misled by anything later.

### 1.6 What it sets, muscle by muscle

Every muscle keeps its own control, and Omni-Compass sets what that control already accepts:

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
| Database behind a pooler | PgBouncer's pool, the DBA's fixed setting | the pool size through the pooler's own console |
| Database's storage engine | MongoDB's WiredTiger cache, the operator's fixed setting | the cache size through the server's own console |
| Message broker | the consumer group at the operator's count | how many consumers are in the group |
| Cache | the operator's memory ceiling and eviction rule | the memory ceiling through the cache's own console |
| Substation | the tap changer's own controller | the tap position, one whole tap per move |
| Drone | the shipped autopilot | the cruise override inside the autopilot's limits |

When Omni-Compass stops, every one of those values goes back to what it was before Omni-Compass acted: not to the last
value it wrote, but to the value it read once, before its first write.

## 2. The Muscles, the Realms and the Six Organisms

### 2.1 The catalog

The catalog (`realms/catalog.csv`) lists **945 distinct muscles in 59 families** (Omni v2 and v3; v1 listed 656 in 46),
each with its family, its plant model and its knob. A muscle is anything with a meter and a setting: a compute pool and
its machine count, a GPU and its clock ceiling, a chiller and its setpoint, a battery and its reserve, a feeder and its
tap, a robot joint and its speed limit, a pump and its flow. Each muscle carries a declared plant model, the simplest
physics that reproduces how its meter follows its knob, and a native controller of its own, which is what the muscle does
when Omni-Compass is not there. The catalog was built in four waves (`docs/realm_study/`): the spine from primary
specifications, each realm's extras from its own specifications, a cross-check against industry and open-source
controllers, and a verification, de-duplication and mapping pass. The register (`docs/REGISTER.md`, section 1) lists
every family with its muscle count and the kinds of knob it carries, so a reader can see at a glance what the modelled
realms contain and what they do not.

The fifty-nine families, by realm, are these. **Compute, AI and cloud** (eighteen): AI inference serving, AI training,
cloud virtual machines and capacity, container resources, cross-cluster and edge placement, DPU and programmable IO,
distributed cluster managers, GPU fabric and RDMA, HPC and distributed compute, host CPU and memory, Kubernetes dynamic
device allocation, Kubernetes placement and scheduling, Kubernetes workload scaling (the largest family, 31 muscles),
NVIDIA GPU hardware, node fleets and Karpenter-class control, OpenShift and the Machine API, quantum computing control
(simulated), and work admission and demand shaping. **Physics, robotics and autonomous** (eight): automotive EV and mobile
powertrains, aviation and autonomous flight, elevators and vertical transport, marine propulsion and vessel automation,
rail traction and train control, robotics fleets and warehouse automation, robotics motion control, and spacecraft and
flight software. **Energy, facility and industrial** (seventeen): agriculture and irrigation, building and
critical-environment HVAC, cooling and chillers, district heating and cooling, energy storage and microgrids, facility
and grid optimisation, grid transmission and distribution, healthcare critical environments, industrial PLCs and process
automation, mining and mineral processing, oil and gas pipelines, PDUs, UPS and electrical distribution, pharmaceutical
and food manufacturing, power generation and turbine control, renewable generation and inverter control, semiconductor
fabs and precision manufacturing, and water and wastewater pumping. **Distribution and specialized** (sixteen): cache and
memory services, commerce and payments, data analytics and ETL, databases and transactions, medical imaging and clinical
systems, messaging and streaming, network routing and switching, observability and telemetry, ports and maritime
logistics, reliability, security and recovery, runtimes and applications, search, indexing and vector databases, service
meshes and API reliability, block, file and object storage, telecom radio access and edge radio, and workflow, logistics
and fulfilment. Thirteen of these, marked "v2" in the register (the elevators, marine, rail, agriculture, district
heating, healthcare, mining, pipelines, pharmaceutical and food, power generation, renewable generation, medical imaging
and ports families), came with the second engine version; they, with the muscles added to the families that already
existed, are the difference between the 656 muscles in 46 families of v1 and the 945 in 59 of v2 and v3.

Every live benchmark in Part VI sits inside one of these families: the Kubernetes tests inside workload scaling and node
fleets, PostgreSQL and MySQL inside databases and transactions, Redis and MongoDB's cache inside cache and memory
services, Kafka inside messaging and streaming, the robot arms inside robotics motion control, the drones inside aviation
and autonomous flight, the power grids inside transmission and distribution, the buildings inside HVAC. A live result is
therefore also a check on one family's model: where the real stack and the modelled muscle move the same way under the
same law, the model has earned some trust; where they do not, the model is the thing to doubt, and the catalog's plant
model for that family is the place to look.

### 2.2 The four realms and the spine

The muscles fall into four realms. Every realm stands on the same **spine** of 257 muscles (Kubernetes, machines, GPUs
and CPUs, network, storage, observability, security, cooling and electrical distribution), because every realm's work
runs on computers that must be cooled and powered, plus its own domain muscles.

| Organism | Muscles | What it is |
|---|---:|---|
| 1. Compute / AI / Cloud | 430 | clusters, GPUs, AI training and inference, cloud capacity |
| 2. Physics / Robotics / Autonomous | 376 | joints, fleets, vehicles, flight and spacecraft axes |
| 3. Energy / Facility / Industrial | 470 | data halls, buildings, batteries, UPS, process loops, feeders, hospitals, farms, pipelines, mines, district heat, power plants, renewables, pharmaceutical and food plants |
| 4. Distribution / Specialized | 440 | networks, storage, databases, commerce, workflows, radio networks, clinical systems, ports |
| 5. The four stacked, every duplicate kept | 1,716 | all four realms on one clock, the shared spine counted in each |
| 6. The whole tower, every muscle once | 945 | every distinct muscle on one clock |

The realms differ in what their domain muscles are and in how much slack their native controllers leave. Compute, AI and
Cloud is clusters, cards, training and inference pools and cloud capacity, where the knobs are replica targets, machine
counts, clock ceilings and power limits, and where native controllers are already good, so the modelled gains are small
and the real gains come from the queue and the tail. Physics, Robotics and Autonomous is joints, fleets, vehicles, flight
and spacecraft axes, where the knob is a speed or effort limit and the physics decides, axis by axis, whether spending
slack as speed saves energy at all; this is the realm the v3 slack gate was written for. Energy, Facility and Industrial
is data halls, buildings, batteries, UPS, process loops, feeders and plants, where the knobs are setpoints, units in
service, reserves and taps, and where the muscles with the most room are also the ones whose reserves exist for a reason
the model does not contain (a UPS held for an outage is never a lever). Distribution and Specialized is networks, storage,
databases, commerce, workflows, radio networks, clinical systems and ports, where the knob is usually an admission, a
pool or a replica count, and where the real stacks of this manual (the pooler, the broker, the cache) live. Every realm's
list, by family and knob, is `docs/REALM_MUSCLES.md` and `docs/REGISTER.md` section 1.

### 2.3 What an organism run is

These six organisms are the benchmark set of the modelled realms. An organism is every one of its muscles stepped on one
clock, each from its own plant model, each with its own native controller, and the whole fed one demand trace from one
seed. Native runs the organism with every native controller alone. Omni runs the same organism, the same seed, the same
demand and the same clock, with the compass law on every knob the verdict allows. Each run produces its own receipt: the
organism's work, its energy, its time over its service line, and every knob's hand-back. In code and in the workflows the
two large organisms are named `tower` and `stack`, never by a count, because the counts changed between v1 and v2 and a
name that carried a count would read as a different organism; the old names are read as aliases.

The receipt is read in a fixed order. **Work** first: the organism's output over the window, which must not fall, and
which reads worse by rule if it does, however little, as the four stacked at 1,000 copies showed on a difference of one
part in a million (section 2.5). **Energy** second, and **work per energy** with it, which is the gain the modelled realms
are built to show. **Time over the service line** third, the share of steps on which any muscle's service reading was past
its line, which is the do-no-harm gauge for the body as a whole. Then **every knob's hand-back**, which must be complete
in every run or the run fails. The reading given to an organism (the realms tables under `results/realms/`, one per engine) uses the words
"superior within guardrails" when work and energy both improve with the service line respected, "service tradeoff" when a
gain in energy came with time over the line, and names the loss when there is one: the v2 reading on the Physics realm
and the tower was a service tradeoff, traced to the speed knobs on busy motion axes, and the slack gate that answers it is
the one rule that makes v3 (section 6.3). What an organism run cannot show is also fixed: it is evidence class S, the
plant models are our own, and nothing in it is presented as proof of a real stack. Its use is to show that one law holds
across every realm at once, at a size no live benchmark can reach, and to find the rules that then have to earn their
place on real software.

### 2.4 The grid of copies and runs

Every organism runs at **1, 10, 100 and 1,000 copies** (that many instances of the organism on one clock, so the four
stacked at 1,000 copies is 1.7 million modelled muscles) and at **1, 10, 100 and 1,000 paired runs** (that many
native-and-omni pairs, each from its own seed): 96 cells in all, both arms shown in every cell. One thousand is the
maximum in both directions. The grid as it stands (`results/scale/GRID.md`) is 84 of 90 judged cells on Omni v3; the six
cells left, 100 and 1,000 runs at 1,000 copies, are beyond the machines available and are declared as such, not hidden.
The reading at every size is the same to the digit, which is itself a finding about the law: it does not drift with scale.

The two axes answer two different questions, and a reader should keep them apart. **Copies** is the size of the body
the one brain governs: at 1,000 copies of the four stacked, the law computes a force for 1.7 million muscles from one
reading of one clock, and the question is whether it stays coherent, whether the decision time stays inside the decision
period, and whether the cluster inside it (section 2.5) is still served on time. **Runs** is the number of independent
paired trials, each from its own seed, and the question is statistical: how wide the interval of the paired difference is
and whether it moves as the trials multiply. A cell at 1 copy and 1,000 runs tells a reader about the noise of the method;
a cell at 1,000 copies and 1 run tells a reader about the scale of the brain; the cells on the diagonal tell both at once.
Every cell shows the native value and the omni value side by side, never a change alone, because a change without its
two ends cannot be checked against the organism's own records. The grid is rebuilt whole on every engine version, never
patched cell by cell, so that no square carries a result from a different engine than its neighbours (section 15).

### 2.5 The organisms with a real cluster inside

The modelled organisms are also run with a **real Kubernetes cluster inside** as one more muscle (`tools/run_kil.py`,
workflows `six-kube`, `big-organism`, `big-organism-detached`): the organism's own compute demand drives a real load
generator against a real service on a real cluster, and the cluster's watts come back into the organism as heat and load.
At 1 to 100 copies this runs on GitHub's machines; at 1,000 copies it needs a rented machine and runs there, detached from
the GitHub job that started it, for about seven hours a repetition. These runs are evidence class L for the cluster and S
for the organism around it, and are labelled "L + S".

Two rules keep these runs honest, and both are written in the preregistration before the machine is rented. The first is
the **clock rule**. The organism must step on the measured window's clock: the row "organism behind its window" says how
many seconds after the window its last step ended, and a repetition in which either arm ended more than 5% of the window
late is marked **off the clock** in the organism's line, because its last steps saw a cluster whose load schedule had
already ended. The row is shown and never judged; at 1,000 copies of the four stacked, both arms ended about 22 s behind
a 10,800 s window, a fifth of one percent, and no repetition was off the clock. The second is the **hand-back at 90%**.
Omni-Compass releases the cluster's knob at nine tenths of the window and the last tenth is run by native alone in both
arms, so that every repetition ends with the proof that the knob was given back and that native resumed where it would
have been.

The first such run on Omni v3 is in `results/live/V3_BIG_ORGANISM.md`: the four stacked at 1,000 copies, three paired
repetitions on one rented eight-core machine over 29 hours, the cluster's slowest 5% of requests at 2,882 ms under native
and 150 ms under omni, the time over the response line from 51% of samples to none, no failed request under omni, the
same six machines in service in both arms and the energy inside the noise. The organism's own rows, which are models, show
the work the same to one part in a million and read worse by the rule that any confirmed decrease is worse, however small;
the row is in the table with that word on it. The whole tower at 1,000 copies runs on the same machine type as this is
written, and the full organism-by-organism table is rebuilt when it lands.

### 2.6 The register

The register (`docs/REGISTER.md`) is the one list a referee can audit: every muscle by family (section 1), every
benchmark by platform with its native controller, Omni-Compass's knob, its gauges, its result and its file (section 2),
what is not measured yet, said plainly (section 3), and every open benchmark still to run, in order, one or two at a time
(section 4). The program that takes each benchmark to its full size, with what each step costs, is `docs/PROOF_PROGRAM.md`.
Every benchmark in this manual appears in the register under the same name.

A row in the register is read left to right as a sentence: the platform, the open benchmark used for it and who publishes
that benchmark, the native controller Omni-Compass sits on top of, the knob it moves, the gauges it is judged on, and its
state. The state is written in a small, repeated vocabulary so that a reader can scan the column: **queued** (in the audited queue,
not yet preregistered), **preregistered and built** (the rules are frozen and the harness runs, no counted result yet),
the smoke runs with what each one taught and what was changed before the counted runs, and **A, B, C done** with the
three run numbers, the engine version and the readings, losses first where there are any. A row never loses its history:
when a benchmark moves from smoke to counted, the smoke record stays in its preregistration, and when a result is
superseded by a run on a later engine, the earlier table moves to `docs/history` with its engine named. The register is
the only list that must be complete; the manual's section 16 and the dossier (`docs/DOSSIER.md`) are readings of it, and
anything in them that is not in the register is an error to be fixed in the register's favour.

The audited queue (section 4 of the register) is the program's promise about what comes next, and it is deliberately
short at the front: one or two benchmarks are run at a time, each preregistered, built, smoked and counted before the
next is opened, so that no result is ever waiting on a harness that was half built when the runs began. The queue is
ordered by what each benchmark adds to the index that the ones before it did not: a new resource traded (memory after
machines, a buffer pool after a cache), a new native controller, a new class of evidence.

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

Why the room is there is worth a paragraph, because it decides what can be done about it. Each layer of a stack is sized
by someone who cannot see the others. The autoscaler's author does not know what the power cap will do; the cooling
engineer sizes for the hottest hour of the year; the database operator sets a buffer pool for the largest table and leaves
it there; each of them, sensibly, leaves a margin against the layer next door, and the margins add up. None of these
people is wrong. The waste is not a mistake anyone made; it is the price of layers that cannot talk to each other, and it
is why a fix at one layer, however good, moves the margin rather than removing it. The benchmarks in this manual are
each a measurement of one such margin on real software: the connections a pooler holds open that no client is using, the
memory a cache keeps for data it will not be asked for, the machines a cluster keeps in service for a minute that has
passed. Each is small on its own and each is paid for every hour of the year.

The attack, then, is not a better autoscaler or a better cache. It is a governor that reads every layer's own gauge, keeps
each layer in the middle of its own band, and gives the margin back where the layer's own controller shows it is not
needed, with the layer's own controller still underneath and the layer's own setting restored when the governor is gone.
That is a different kind of thing from a point fix, and it is why it stacks on top of every point fix a data center has
already made rather than competing with any of them.

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

The results to date (section 16) show both readings on real software, and show that which one a stack gets is decided by
the stack, not by Omni-Compass. On the real Kubernetes cluster and on Apache Kafka the gain was taken as **more work,
faster**: the cluster carried more requests inside its response line on the same machines, and Kafka's slowest 5% of
messages waited 9 to 14 ms instead of about 1.6 s, at the cost of more consumers running while messages waited. On
PostgreSQL behind its pooler and on MongoDB the gain was taken as **the same work for less**: the same transactions
answered inside the same line with fewer connections open, or a smaller storage-engine cache, with the resource handed
back at the end of every run. On Redis neither reading came out ahead: the compass held more memory for a wide working
set and the rule says that the resource held reads worse. The combined index (section 16.6) is +23.5% over the six real
categories so far; the Redis category inside it is a loss (−24.9%), counted in full, and the MySQL category (+12.2%)
carries one confirmed loss of its own, the memory bought for a written working set. An operator
should expect the same honesty from their own paired run: the receipts will say which side of the gain their stack took,
and whether the compass's own cost (its CPU, its reads) ate into it.

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

**Three worked examples, from the tables.** In the all-four Kubernetes test on v3, the same ten machines carried 35% to
49% more requests inside the response line: *G* is 0.35 to 0.49, so the same work would need 1/1.35 to 1/1.49 of the
machines, a saving *S* of 26% to 33%, had the fleet been free to shrink; on kind it was not, which is why the table
reports the work column and not a bill. In the database test, the pooler held 61% to 72% fewer connections open for the
same work: the resource there is connections, *C_omni / C_native* is 0.28 to 0.39, and the gain read as "more work for
the same connections" would be *G* = 1.6 to 2.6, which the table reports as the machines-equivalent column, "fewer
connections by". In the Kafka test the work inside the line rose 16% to 21% while the consumers running rose by a factor
of 2.6 to 4: there the gain in work was bought with resources, and the table reports both, the one as confirmed better
and the other as confirmed worse, because that is what happened.

### 3.5 Where the evidence stands today, read honestly

Every number below is from a three-run table on the frozen engine Omni v3, with its evidence class and the question a
referee is entitled to ask about it. The answers to those questions are given, where they exist, in the row; where they
do not yet exist, the row says what will supply them.

| What | Measured, same work, three runs | Class | What a referee will ask, and the answer |
|---|---|---|---|
| Kubernetes: work inside the response line, all four in one run | **+35% to +49%** confirmed better | L | "Is the cluster real?" Kubernetes is real (API server, scheduler, HPA); the seven nodes are containers on one 4-core GitHub runner, so the host's own busy share is recorded beside every run and the machines column is machine-hours in service, not a bill. The bill is Azure's test (below) |
| Kubernetes: 95th-percentile response time, steady, wandering, all four, faults | **47% to 66% faster** confirmed better | L | "Did native have a fair chance?" Native is Kubernetes with its HPA at the operator's target of 50%; the cost-to-match runs on the earlier engine showed no native target tried (40, 30, 20) reached Omni's p95 (`docs/history/`). The runs are paired on one runner with the order rotated |
| Kubernetes: machines in service | −1.5% to −2.9% at steady load, **−19% to −23%** on the batch queue, confirmed better; inside the noise on the other tests | L | "Why so little?" Because the verdict kept every machine whose removal made requests slower in the paired trial. Earlier engines without that check parked 29% to 36% of the machines and paid for it in response time; the frozen engine puts service first. kind has no node autoscaler, so parked machines stay powered: the saving is machine-hours, not watts |
| Kubernetes: energy | the standby model, −13% to −16% on the batch queue, inside the noise elsewhere | L, modelled | "Is it a meter?" No. The machines are containers; energy is a declared formula (a parked worker at 25 W standby), stated as a model on every line |
| Kubernetes: fairness beside a noisy neighbour | no difference beyond the noise on every row, the neighbour's included | L | "Does it hurt the other tenant?" Not measurably, in three runs of ten pairs |
| Database behind its pooler: connections held open | **−61% to −72%** confirmed better on two workloads; the runs disagree on the third | L | "What did it cost?" Host CPU-seconds +14% to +28%, confirmed worse on all three workloads, the compass's own cost included, counted against Omni in the index; work and latency inside the noise |
| Message broker: work inside the 500 ms line; the 95th percentile | **+16% to +21%**; 1.6 s → 9 to 14 ms, confirmed better on all three workloads; no message lost | L | "Why is the latency figure so large?" By design native sat at nine tenths of its measured capacity, so its queue grew at the high steps and Omni's did not; the gain is the queue kept short. "What did it cost?" Consumers running 2 → 5.8 to 7.9, confirmed worse; host CPU worse on one workload, inside the noise on two |
| Database's storage-engine cache (MongoDB under YCSB): the cache size held | **−49% on c, −41% to −49% on burst, −13% to −37% on f**, confirmed better; b inside the noise in one run | L | "What did it cost?" Work inside the 1 ms line, p95, p99 and host CPU inside the noise on all four workloads, no failed operation; the burst mean latency **+2% to +4%, confirmed worse**, in the table. "Why is this the mirror of the Redis result?" Because here the operator's setting was larger than the working set needed on this machine, so the governor gave memory back; there it was smaller, so the governor bought service with memory. "Would this hold on a disk-bound store?" Not shown: on this machine a miss is a memory read, as disclosed before the run |
| Database's buffer pool (MySQL under sysbench): the pool held | **−67% on burst, −50% to −56% on read_only**, confirmed better; +59% to +79% on read_write as point estimates, with the pages holding data there **confirmed worse** | L | "What did it cost?" Work inside the line, p95, p99 and CPU inside the noise on every workload; on the read-and-write workload the compass bought pool for the written working set and the memory held reads worse by rule. "And the hand-back?" On all 45 omni arms in the counted set; the first set, where the restore met the server's unfinished shrink on 15 arms, is kept whole in the history (sections 10.9, 16.4) |
| Cache: work inside the 2 ms line; the hit rate | **+14% to +27%** and +14% to +27%, confirmed better on all three workloads; no failed request | L | "What did it cost?" The memory ceiling held, 64 → 200 to 270 MB, confirmed worse, and the memory used with it; host CPU inside the noise. "Why is p95 unchanged?" A miss costs the declared 5 ms trip in both arms and 5% of requests still miss at the high notches; the gain is in the mean and in the work inside the line. "Why is the cache's index negative?" Because its resource column is the memory held, a ratio of about 0.25, and the geometric mean of a 1.2 gain and a 0.25 cost is below one |
| The modelled realms: work per energy, 945 muscles, six organisms, 1 to 1,000 copies | **+0.07% to +0.37%**, every organism superior within guardrails, 0 muscles worse | S | "Why so small?" The native controllers in the models are well tuned and leave little room; the number is small and real within the model, the same at every size, and it is never counted in the headline |
| Power grid, 11 SimBench grids in pandapower | energy drawn and net import better in all 11; losses better in 7, **worse in 4**; tap operations fewer in 10, 4 → 8 a year in one, worse | S | "Where does it lose?" In the rural and semi-urban grids with their own generation, where a lower voltage raises losses; the table shows it |
| Robot arms, MuJoCo Menagerie | peak torque −29% and −10%, tracking error −21% where Omni moved; the Panda's copper loss **+14% worse**; two arms left native | S | "What about the arms that gained nothing?" The paired physics trial left them native and the table says "nothing for Omni to move" |
| Buildings with batteries, CityLearn, 11 districts | electricity bought, daily peak and unevenness better in all 11; the bill **worse in 7**; ramping worse in 7 | S | "Is the bill a loss?" Yes, in the 2023 districts, and it is in the table as such |
| Drone swarms, gym-pybullet-drones, three 20-drone cells | energy a mission −7% to −20%, missions a charge +8% to +25%; no late mission, reserve breach, near miss or collision | S | "Is the energy a meter?" No, a declared model from the simulator's own motor constants; the tracking error rose from 0.07 to 0.13 m inside its 0.25 m band and is shown |
| The governor's own cost, 1 to 1,000 copies with the real cluster inside | **0.006 to 0.013 of one core** at every size, 0.1% to 0.3% of the host's cores | L | "Does the brain's cost grow with the body?" No: it governs the real cluster, and that cost does not grow with the organism around it; shown, not judged, each run under its own engine (`results/live/V3_OWN_COST.md`) |
| The governor killed outright mid-run, 10 pairs × 3 runs | every setting back at the operator's **7 to 11 s** after the kill in 30 of 30 repetitions (mean 9 s; allowance 60 s); a second governor to the end in every one; the 120 s after the kill inside the noise against native | L | "What if Omni-Compass dies?" The watchdog hands back from the lease the governor left, within seconds, and the service does not measurably notice; the whole window with a kill and a restart in it still read faster and with fewer failures than native (`results/live/V3_ROBUST_KILL.md`) |
| Azure's bill on a 4-worker fleet (v1) | no difference beyond the noise on any gauge | L, a real bill | "Then where is the saving?" A fleet of 4 cannot show one machine; the 40-worker fleet that can is preregistered and waits on Azure's own cluster capacity in its region |
| The real card (GPU) | **obsolete**: every earlier card result ran on a controller since replaced | P pending | "When?" The founder's runs on rented cards at one named commit, after the CPU and cloud work |

The upside the real-software data points toward is a third to a half more work from what is already installed on the
Kubernetes side, with faster answers, and a smaller, resource-priced gain on the stacks where the knob is a pool, a
consumer group or a ceiling. It becomes a claim about the bill, not a direction, when two tests land: the bill on a real
cloud with a fleet big enough to show one machine, and the real card's own meter. We publish each of them as it comes,
whatever it says.

### 3.6 One law, frozen; and what came before it

The engine in every result of this manual is **the compass law with the verdict** (sections 6 and 1.2), frozen as Omni
v1 on 5 October 2026, grown to the 945-muscle catalog as v2 and given the slack gate on speed knobs as v3, with the law,
the controllers and the runners the same bytes in all three (`docs/OMNI_V1.md`, `OMNI_V2.md`, `OMNI_V3.md`). Earlier
engines, among them an allocation law that gave back about a third of the machines at the cost of response time and a
compass law without the verdict, produced the numbered sets kept in `docs/history/`; their results are history, labelled
as the engine that produced them, and are never read beside v1's or v3's. A buyer does not choose between modes: there is
one law, and it is the one every table in Part VI was made on. Each new result therefore describes exactly the code that
produced the old ones, and when the founder declares the engine final, the engine that stands then is published as
Omni-Compass 1.0, with the older fingerprints kept as the road to it, never as a second product.

"Frozen" has a precise meaning here. The engine is a fixed set of 40 files, and `OMNI_V3.json` holds one SHA-256 for
each of them and one digest over all of them; `OMNI_V2.json` and `OMNI_V1.json` do the same for the two earlier sets.
`python3 tools/omni_version.py` hashes the files in a checkout and prints which fingerprint they match (for this edition,
`omni-v3 (digest b53d05449ee04c4b, 40 files)`), or, when they match none, which files differ from the nearest; with
`--commit <sha>` it asks the same of any pushed commit, which is how every three-run table checks that its runs A, B and
C were on the same engine before it combines them, and refuses if they were not. The three versions differ in exactly
the ways their records name: v2 added the 945-muscle catalog and thirteen presets to v1 without touching the law, the
controllers or the runners, which are the same bytes in all three; v3 added the slack gate on speed knobs and the marine
propulsion preset to v2 (`docs/OMNI_V3.md`). Nothing else changed, and a reader can confirm that from the fingerprints
rather than from this sentence.

The rule that any change makes the next version is also the rule that keeps the results honest. A gain or a guard
changed after a result is in would make that result unrepeatable on the engine that now stands, so the change moves the
version, every result is run again on the new version, and the old tables keep their version in their name and move to
history. The founder's standing order is that the engine is never changed without being told first; this manual records
no change made otherwise.

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

### 4.1 What each equation does, in words

The six numbers describe the whole system the way a physician's six vital signs describe a patient, and each equation
says how one of them moves.

- **Equation 1, the deviation tank.** *E* is how hard the system is being driven: queues, overload, power, heat. It
  drains on its own at a fixed rate (alpha_E = 3.487) and is filled by two pressures, internal (queue and overload,
  beta_int) and external (power, heat, network, staleness, security, beta_ext), plus a drive term v_eff that is bounded
  by a hyperbolic tangent. However extreme the observation, the engine's response rate is capped at c = 1. This is the
  saturation, the "speed limit" that no input can exceed.
- **Equation 2, the alignment.** *U* is how healthy and settled the system is, and it lives in a double well: two stable
  poles at +1 (healthy) and −1 (failed) with an unstable ridge at 0. A rising deviation pushes *U* out of the healthy
  well; the bounded command *u* pulls it back. The cubic term mu U (1 − U²) is what makes the walls of the well push back
  harder the farther *U* strays.
- **Equation 3, the memory.** *I_U* grows while *U* is below its pole, is reduced by deviation and stress already being
  dealt with, and leaks at lambda_I = 0.719. It is the engine's memory of unrelieved pressure: a system that has been
  stressed for an hour is not the same as one stressed for a second, and this integrator is what knows the difference.
- **Equation 4, the drive.** The bounded drive v_eff mixes the alignment and the stress through a tanh, with a slow
  cosine of the bath's frequency on top, so the drive breathes rather than pushes constantly.
- **Equations 5 and 6, the stress.** *S* rolls downhill in a cubic potential to its stable root. It is the slowest
  restoring force: structural stress from heat, power, network, security and staleness that builds and relaxes over
  minutes rather than seconds.
- **Equation 7, the bath.** A damped harmonic oscillator (natural frequency omega_B = 1, quality Q_B = 2.5) driven by
  stress. It turns stress into a smooth, lagged tide, and it is the only second-order element in the engine; its friction
  is what settles the whole.
- **Equation 8, the audit.** The bath equation is re-checked numerically every step with a finite difference, and the
  check is recorded and never fed back: an instrument on the engine, not a part of it.

Integration is classical fourth-order Runge-Kutta, ten micro-steps of 0.01 per macro step, and the C++ twin matches the
Python to 3.6 × 10⁻¹⁵ on 500 reference trajectories (section 18).

### 4.2 From telemetry to state, and from state to action

Each decision, the telemetry is normalised to nine observations: queue, load, power, thermal, network, drift, staleness,
security and conflict. An observed state is computed from them by fixed weights (`omnicompass/adapter.py`,
`observe_vector`), the engine's state is blended toward it with weight 0.339, and the state is then evolved by one macro
step of the equations. From the state, the governor evaluates the control's push, u(x)/25, which is a number between −1
and +1 that says how hard the engine is pulling toward health; a target utilisation that falls as the memory and the
deviation rise; whether a release (giving something back) is permitted at all, which is only while the push reports
convergence and the band and dwell allow; and whether change is permitted, which requires *U* above its gate and no
security block. All of this is written to the audit every decision (`docs/MECHANISM_OF_ACTION.md`, sections 3 to 6, and
`python tools/mechanism.py`, which reproduces the measured numbers in `results/MECHANISM_OF_ACTION.json`).

The nine observations are worth naming in plain words, because every later number is a weighted sum of them
(`omnicompass/adapter.py`, `observe_vector` and `assimilate`). **Queue** is the work waiting as a share of the work being
served; **load** is utilisation against the stack's own target; **power** and **thermal** are the electrical and heat
stress against their limits; **network** is the same for the wire; **drift** is how far the levers stand from where native
had them, so that a governor that has pushed far from the operator's settings reads as more stressed than one that has
not; **staleness** is the age of the readings, which rises when a sense goes quiet; **security** is the hold flag; and
**conflict** counts other hands seen on the levers. Each is clipped to a declared range before it is used, so no single
runaway reading can swamp the others. The stress the engine assimilates leans most on the queue (a weight of 0.25) and on
load above 85% of target (0.18), then power, heat, network and drift in that order, with conflict and staleness last; the
utilisation it blends toward falls with the queue first (0.27) and with power and heat next. The weights are fixed numbers
in the frozen engine, the same on every stack, and a reader who wants to know why a decision read the body as stressed can
recompute the sum from the audit line, which records all nine observations. What the weights encode is a judgement made
once: that work waiting is the first sign of a body in trouble, that a lever far from native is itself a mild stress, and
that a reading one cannot trust is a reason for caution rather than for action.

### 4.3 Where the engine sits, and where the compass law sits

A reader meeting the engine and then the compass law (section 6) may ask which of the two moves the knob. The answer, in
the live controllers, is this: the **compass law** sets each knob, the **verdict** narrows where the law may go, and the
**engine** grants the authority, feeds the release gate and the nervous system, and is audited every decision
(`omni_controller/controller.py`, its docstring). The engine is the organism's physiology: how stressed it is, how long
it has been, whether it is settling. The compass law is the hand on each lever. The engine's own control law *u* is
evaluated, not applied to a knob directly: it is the push the nervous system reads to decide whether giving anything
back is permitted now. This separation is why the engine could be frozen with its proofs untouched while the compass law
was written as its own, separately tested law, and why `verify.py` seals both.

One decision, followed through, shows the order. The controller wakes on its period and reads its senses: the service
gauge (a response time, a statement latency, a consumer lag), the resource gauge (machines, connections, memory) and the
knob's current value read back from the device. The **engine** takes the normalised observations, blends its state toward
them and evolves one macro step; from the state it reports whether the body is converging, what authority the organ has
earned and whether a release is permitted at all (section 4.2). The **compass law** then reads the service gauge as a
position in its band and computes the force (section 6): positive, and the direction rule asks for capacity in proportion;
negative, and it asks for one notch back, but only if the engine's release gate is open, the resource is demonstrably idle
and the dwell has passed. The **verdict** stands over the slow knobs: a knob the paired trial has not cleared at the 2%
line is not moved at all and stays native. What survives all three is one write to the **plug**, read back from the device,
and one line in the **audit** that records the senses read, the engine's state and push, the force, the gate's reasons and
the value sent and taken. In the kill test's first repetition (section 7.1) this produced 114 such lines and 42 writes:
every decision that wrote nothing is in the record with the reason the gate held, which is the point of writing all of it down.

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

**In plain words.** Picture a bowl-shaped valley with a fence around its rim. The first line says the valley has a
shape: given where the system is, the equations say which way it rolls. The second line says that at the fence the
ground always slopes inward, so nothing that starts inside can ever roll out, however it is pushed within the strength
the fence was built for. The third line says there is a height, *L*, that only ever decreases along any path, so the
system cannot circle forever at one level; it must keep descending. The conclusion follows: every path ends at the
bottom, the set *M\**. The engineering value of such a certificate is that it is not a sample of behaviours; it is a
statement about all of them at once, inside the fence.

**What is certified, and what is not.** The certificate is about the engine's own state: the six numbers of section 4
stay inside their walls and settle. It is not a certificate about the plant the engine governs, whose physics the engine
does not contain; that is why every plant is tested paired against native (Part VI), why the compass law clips every
write to the knob's cover (section 6), and why the shield between the engine and the levers is tested separately on two
million adversarial cases with zero violations (`tests/test_shield_properties.py`) and the C++ engine soaked on one
hundred million decisions with no failure (`results/SOAK.json`). The mathematics closes the brain; the harness, the cover,
the verdict and the paired receipts close the hand.

The engine's states are each closed in this sense: the deviation tank drains faster than it can fill; the alignment's
cubic walls push back from far out; the memory forgets; the bath's friction settles it. The rule behind all four is
the compass's east-west line: what flows out (drain, damping) must always be able to match what flows in (drive). The
formal status of each statement, what is proved, what is tested and what is conjecture, is written out in
`docs/FORMAL_STATUS.md` and `docs/TRACKING_THEOREM.md`, and the theory chapters of this book (The Unified Circle
Principle, Closing the Circle in the Engine) give the derivations.

**What the certificate buys an operator, in practice.** Three things. The engine cannot run away: there is no input, no
sequence of readings and no fault in a sense that drives its internal state to infinity or into oscillation that grows,
because the walls are part of the equations and not a check bolted on afterwards. The engine cannot hold a grudge: the
memory state forgets at a fixed rate, so a bad hour does not bias the next day, and a governor restarted after a kill
starts from the same rest state the certificate names. And the engine's behaviour under any disturbance smaller than the
fence is the same kind of behaviour, a descent to the bottom, so a test on one plant's readings says something about the
engine on another's; what it does not say, and what no mathematics of the engine alone could say, is how the plant
answers, which is why the paired runs exist. An underwriter reading this section should take from it exactly this much:
the part of the system that makes decisions is bounded by proof; the part of the system that carries them out is bounded
by the cover, the gates and the hand-back, each tested; and the part that is the customer's own plant is measured, never
assumed.

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

### 6.1 The same law on every stack, and what differs

The law is written once (`CompassLaw`), and three declared numbers fit it to a muscle: the **decision period** *dt*
(how often the governor decides), the muscle's **response time** tau (how long the service reading takes to follow the
lever), and the **cover**. From tau and *dt* the law derives its own damping gain, K_D = (2 sqrt(K_P tau / dt) − 1) dt,
which is critical damping for a first-order muscle under a proportional-derivative pull: the position glides to the
center and stops. Nothing else is tuned per stack. The table below is the complete list of the compass's settings on every
stack in this manual, so a referee can see that the "gains" differ only through the declared physics:

| Stack | Reading (the wire in) | Line | Center | Decision period | Response time | Cover of the knob |
|---|---|---|---|---|---|---|
| Kubernetes, the HPA target | the mean response time of the latency window | the operator's SLO (500 ms) | 0.4 | 60 s | the pods' start time | [0.6 × the operator's target, the operator's target] |
| Kubernetes, the machines | the same, through the release gate and the verdict | the same | 0.4 | 60 s | a machine's wake | [the floor of 2, every machine] |
| PgBouncer, the pool size | time in the server plus time waiting for one, per transaction | 50 ms | 0.4 | 1 s | 2 s | [2, PostgreSQL's limit minus 10] |
| Kafka, the consumer count | the group's own end-to-end latency, mean of the last second | 500 ms | 0.4 | 1 s | 3 s (a rebalance) | [1, the topic's partitions] |
| Redis, the memory ceiling | the application's request latency, mean of the last second | 2 ms | 0.4 | 1 s | 2 s | [16 MB, 512 MB] |
| MongoDB, the storage-engine cache | the server's own mean read latency, last second | 1 ms (set on the tuning workload's smoke run, from 2 ms) | 0.4 | 1 s | 2 s | [256 MB, 2,048 MB] |
| MySQL, the InnoDB buffer pool | the server's own mean statement latency, last second | 0.6 ms a statement (set on the tuning workload's smoke runs, from 1 ms) | 0.4 | 1 s | 2 s | [128 MB, 2,048 MB], in 128 MB chunks |
| A drone's cruise override | the drone's tracking error | 0.25 m, the declared safe error | 0.5 | one control tick (48 Hz) | 1 s | [1.0, 2.0] × the planner's cruise |
| A substation's tap | the bus voltage in its band | the band's edge | 0.5 | one solve | a week of evidence before a step down | the tap's own range, one tap per move |
| A robot axis's speed | the axis's tracking error against its takt | the declared error | 0.5 | one control step | the axis's response | the axis's own limits |
| A GPU's clock ceiling and lid | the mean response time of the last 5 s | the SLO | 0.4 | 2 s | the card's response | [the card's own busy clock, its top clock]; [the busy draw + 10%, the start limit] |

The center is 0.4 wherever the reading is a service time (the "service profile" of the Kubernetes adapter, so that the
service sits a little below the middle of its band with margin for a burst) and 0.5 where the reading is a physical
error. A **cushion** of ±0.05 in force moves nothing, so a reading that sits at the center with the usual jitter does not
make the knob chatter. These are the same numbers in every preregistration and every table; none was changed after a
result was seen.

### 6.2 Direction rules: how a force becomes a move

The force is a number between −1 and +1. Each stack turns it into a move on its knob by a direction rule declared in its
preregistration, always of the same shape: a positive force adds capacity in proportion to the force (ceil(force / 0.10)
notches, so full force adds ten notches at once, capped by the cover), a negative force takes one notch back per
decision, and only when the resource it would take is demonstrably idle (an idle consumer that read nothing in the last
second, an idle server the pooler itself shows idle, a cache with nothing evicted in the last second) and only after a
**dwell** of a few seconds since the last change, so a knob that was just moved is not moved back by its own transient.
At 95% of the line the knob **fails up**: every consumer the topic can use, the pooler's own setting handed back, a
quarter of the cache's cover added at once, the planner's own cruise, the card's own clocks. The up side is fast and the
down side is slow and gated because adding and taking back do not cost the same, and because a gain bought by taking
something back must be able to prove itself before it is kept.

Written out stack by stack, from the preregistrations, the rule reads as follows; the unit, the cover and the fail-up move
are each the stack's own, and the shape is the same in every row.

| Stack | The knob and its unit | The cover | One notch back, when idle | Fail up at 95% of the line |
|---|---|---|---|---|
| Kubernetes (the cluster) | worker machines in service | the floor of two to every machine the operator has | one machine a decision, when the remaining machines would carry the load far under the wall | one machine up at once |
| PostgreSQL behind PgBouncer | the pooler's pool size, server connections | [2, 90]: the floor of two, never within ten of PostgreSQL's 100 | one connection a decision, when the pooler itself shows a server idle | the pooler's own setting (20) handed back at once |
| Apache Kafka | consumers in the group | one to the topic's partitions (8) | one consumer a decision, when a consumer read nothing in the last second | every consumer the topic can use |
| Redis | the memory ceiling, MB | [16, 512] MB | one notch a decision, when calm and nothing was evicted in the last second | a quarter of the cover added at once |
| MongoDB (WiredTiger) | the cache size, 64 MB notches | [256, 2,048] MB | one notch a decision, when calm and nothing was evicted in the last second | a quarter of the cover (448 MB) added at once while full |
| MySQL (InnoDB) | the buffer pool, 128 MB chunks | [128, 2,048] MB | one chunk a decision, when the miss share is under 1% | four chunks at once while the pool is full |

Two things in the table deserve a reader's attention. The "when idle" column is never a guess from the knob's own
value: it is a reading from the stack's own counters (the pooler's idle servers, the consumer's last fetch, the cache's
eviction count, the pool's disk reads against its requests), so the law gives back only what the stack itself reports it
is not using. And the fail-up column is the stack's own fastest safe move, not a multiple of the notch; where the stack
has a controller of its own (the pooler, the planner, the card's firmware), fail up means handing the knob back to it,
which is the one move that can never be worse than native by construction.

### 6.3 The do-no-harm gates inside the law

Three gates sit inside the law itself, each a consequence of a loss seen on a tuning case and each disclosed in the
preregistration that carries it:

- **The verdict** (section 1.2): a slow knob moves only where a paired trial on the muscle shows no more than 2% cost.
- **The slack gate on speed knobs** (Omni v3): a motion axis that is busy more than half the time at full speed keeps its
  speed native, because spending its slack as speed when it has none would only cost energy. This gate is what turned
  the v2 "service tradeoff" on the Physics realm and the tower into "superior within guardrails" on v3, and it is the
  one rule that distinguishes v3 from v2.
- **The full-cache gate** (Redis): a miss in a cache with room to spare is a cold miss that no ceiling can mend, so the
  ceiling grows only while the cache is at 90% of it or more. On the tuning workload without that gate the law raised the
  ceiling to 500 MB while 21 MB were in use; with it, the ceiling follows the working set.

The same gate recurs, in the form each store's own gauges allow, on every memory knob that followed, and each form was
fixed on the tuning workload and disclosed before the counted runs:

- **MongoDB's storage-engine cache** grows by a notch only while the cache is full and the server's own read latency is
  above the centre of its band, and gives a notch back only while calm and nothing has been evicted in the last second
  (`docs/YCSB_PREREGISTRATION.md`). The smoke runs showed the line itself had to be set from the server's own readings
  (0.15 to 0.46 ms under a 2 ms line left the law nothing to do), and it was set to 1 ms before the counted runs.
- **MySQL's buffer pool** grows by a chunk only while the pool is at least 90% full of data pages and the server's own
  statement latency is above the centre, and gives a chunk back only while the **miss share**, pages read from disk as a
  share of the pool's requests in the last second, is under 1% (`docs/MYSQL_PREREGISTRATION.md`). The earlier rule, "no
  disk reads in the last second", was never satisfied on the tuning workload: InnoDB keeps stale pages resident, so a pool
  once filled reads full for ever, and a few new-page reads a second never stop even when the working set fits, so the
  pool the law had grown was never given back (877 MB held on average against native's 512 on that smoke run); the smoke
  record says so, and the miss-share rule replaced it before run A.

What the three forms share is the reason: a memory knob has no slack to spend unless the memory is both full and being
missed, and memory given back while it is being missed is not a saving but a cost moved to the disk. The gate is written
in each harness in the store's own units and checked by that harness's own tests against a fake server, so that a reader
can see in the preregistration exactly which reading opens the gate and which closes it.

### 6.4 The profiles and the pedals

The compass has two **profiles**, service (the default) and batch, which differ only in what the pedals do with a pile of
work: in the service profile the law paces the slack; in the batch profile cruise puts every machine in service while
work waits for a place and the emergency brake takes them straight to the floor when the queue is done (section 1.3).
Both are written out in the Kubernetes preregistration (`docs/K8S_COMPASS_PREREGISTRATION.md`, rules 7 and 8, amendment
9), both ran in the batch test, and the result (section 16) is machines 19% to 23% fewer over the whole window and 29% to
35% fewer after the queue finished, with the queue itself finishing no later beyond the noise.

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

"Two-way" is a statement about wiring, and it is checked, not assumed. Each muscle's plug (section 8) carries exactly one
sensory wire and one motor wire, and the wire check that must pass before any write (section 8.4) proves that the wires
move: a value written through the motor wire is taken by the device and read back as the value sent, and the snapshot is
restored and read back at the end. No governor writes a knob whose wire check has not passed, because a knob that can be
written but not read back cannot be handed back with proof. What the wire check does not prove, section 8.5 says plainly:
that the governor is reading the right gauge for the knob; that is what the watching arm is for. The receipts of every run
therefore carry, for every write, the value sent and the value the device reported, side by side, and a reader who wants
to know whether the governor's hand was really on the stack can check the two columns rather than take the summary's word.

The four rules above are the whole of the nervous system's authority model, and they are asymmetric on purpose. Adding
is cheap to undo and expensive to delay, so it is never gated beyond the security hold. Taking back is cheap to delay and
expensive to get wrong, so it is gated three ways: by calm (the engine's own state must report that the body is
settling), by the service record (the gauge must have been inside its line for the last three decisions, not merely
this one), and by the release gate's reasons, which are written into the audit every time the gate holds (section 7.1).
Sections 7.2 to 7.4 take the three ideas that make this safe at scale, the governor's sense of its own hand, the rule that
a missing reading is a hold and not a guess, and the case for one brain over many, and give the evidence for each from
the live runs.

### 7.1 Authority, and the release gate

Authority is how far the nervous system lets an organ move in one decision. It is granted from the engine's state
(section 4.3): an organ in a calm body with a clean service record may give back; an organ in a stressed body may only
add. On Kubernetes the **release gate** (`omnicompass/nervous_system.py`, `node_release_gate`) lets one machine be
given back only when every one of the following holds, and writes the first reason that fails into the audit so a reader
can see why a machine was kept: the remaining machines would stay under 95% full; no pod is waiting for a place; the
pods are not scaling up; the service is not breached; the organ's own pressure is under the release threshold; every
sense is live; and the last command has landed (no new order goes on top of one the cluster has not yet carried out).
One machine per decision is the rule in the slow, reversible direction; past the wall, one machine up at once.

**What the gate writes, in a real run.** The first repetition of the first kill-scenario run (`results/live/raw/run-37716845219/paired-1/`,
the omni arm's `audit.jsonl`) holds 114 decisions and 42 writes. Its gate records read, in the governor's own words,
"release permitted" eleven times, each with the utilisation the remaining machines would carry after the release (0.034
to 0.153, all far under the 95% wall); "node organ has no contraction authority" once, a calm cluster whose engine state
had not yet earned the right to give back; and "latency breached now; node organ has no contraction authority; a sense is
blind" once, three reasons at once in a decision whose latency sense read stale, every one of them a reason to hold. A reader can
therefore see, decision by decision, not only what the governor did but why it declined to do the rest, and the first
reason that failed is the one written, so that a machine kept in service always has a stated cause.

### 7.2 Proprioception and the one-writer rule

The nervous system knows where its own levers are. Every write is read back from the device (the plug contract, section
8), and the audit records both the value sent and the value the device took. If a lever is found at a value Omni-Compass
did not write, someone else owns it: the governor stops writing that lever and leaves it alone, because restoring over it
would fight the new owner. This is **proprioception**: the governor's sense of its own hand. It is the reason a wrong
installation leaves a signature in the receipts (section 8.5) rather than a silent error, and it is what the wire check
proves before anything runs.

The rule begins with the **snapshot**. The governor reads every knob it may move once, at the start, before its first
decision, and that reading is the operator's setting for the whole run: every reset, every hand-back and every kill
returns the knob to the snapshot, never to a value computed later, and the receipts record the snapshot beside the final
read-back so that a reader can check the two are equal. The rule continues with the **read-back** after every write: the
plug sends a value, waits for the device to take it, and reads the device's own report of what it holds. Where the device
takes time to apply a setting, the plug knows that and does not mistake the transition for a foreign hand. The clearest
case is MySQL's buffer pool, which the server resizes in chunks over several seconds and reports as it goes: the plug
reads the server's own resize status and treats a pool caught mid-resize as its own write in progress, not as another
owner's value, and waits for the server to report completion before it judges the write (`tools/run_sysbench.py`,
`BufferPool`). The same shape holds on the Kubernetes autoscaler's bounds, Redis's memory ceiling and MongoDB's cache
size: the value is read from the device's own console, and only a value that the governor neither wrote nor is waiting
on is read as someone else's.

What follows from a foreign value is deliberately conservative. The governor does not restore over it, because an
operator who changed a knob by hand meant to, and a second controller that changed it is a conflict to be reported, not
won. The lever is left where it was found, the audit records the value and the time, and the governor goes on governing
the other levers. A reader of the receipts who finds such a record knows at once that two hands were on the stack, and
the paired run that contains it is read with that in mind.

### 7.3 Blind means hold, and fail up

A sense that goes stale or unreadable is not read as calm. It is read as **blind**, and while any sense is blind nothing
is given back; the knob holds, or, if the service was breached when the sense went blind, returns to native at once. In
the fault test on real Kubernetes the response-time probe is deliberately paused for a minute in every arm; the audit
shows the governor holding through the blind minute and resuming when the sense returns, and the table shows no row
worse for it. The rule is simple to state and strict in effect: Omni-Compass never acts on a reading it does not have.

The rule was also tested without being arranged. In the two-hour robustness run on real Kubernetes
(`results/live/V3_ROBUST_LONG.md`), the cluster's own API answered a handful of the governor's reads of the autoscaler
with a server error, two or three times a run out of the 120 decisions a two-hour window expects. Each of those decisions is in the controller's
log with the reason the API gave, each was held (no write, no hand-back, no guess), and the governor took its next
decision on schedule when the API answered again. The preregistration had said in advance that such decisions would be
shown with their reason and not judged, and that is how they appear in the table: 97.5% of the expected decisions valid,
the failed ones counted and named, the knob handed back at the end of every run. A referee who wants to see the rule in
the same rule written by the gate itself can find it in the kill test's receipts (section 7.1), where a decision whose
latency sense read stale is held with "a sense is blind" among its reasons, and in the fault test's blind-probe window,
where it was arranged on purpose. The point in every case is the same:
a stale or missing reading produces a hold, never a move, and the hold is in the record.

### 7.4 Why one brain

The alternative to one brain is a controller per layer, each tuned alone: an autoscaler that adds pods while a power cap
is trying to hold the machines down, a cooling loop that chases heat the clock governor is about to remove. These
controllers fight because none of them knows the others' intent. One law that sets every knob from one state cannot
fight itself: the force on each lever is computed from the same reading of the same body at the same moment. This is also
why the modelled organisms are run whole, at up to 1.7 million muscles on one clock (section 2.4): the question they
answer is whether one brain stays coherent at that size, and the reading at every size is the same to the digit.

One brain also has to stay the same brain over time, and that is a measurable claim. The two-hour robustness run
(section 16.8) measures the governor's own memory at the start and the end of each run and the time it takes to reach a
decision in the last hour against the first. Over three runs the memory ratio was 1.05 to 1.07 and the decision-time
ratio 1.07 to 1.20, both inside the limits set before the run (a leak would show as steady growth; a brain that slows as
its records accumulate would show a ratio climbing toward the 1.5 limit), and the cluster's service under the governed arm
was inside the noise of native in two of three runs. The 24-hour runs on three rented machines, started as this is
written, ask the same two questions over twelve times the window. A single controller that keeps its memory and its
speed over a day is the least a referee should ask of a brain that proposes to hold every knob at once; the figures are
in the table, not asserted here.

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

**The plug contract, line by line, and why each line is there.** *Attach* reads the knob once before any write and keeps
that value as the snapshot. It is read once and never again, because a snapshot that moved with the knob would restore to
wherever the governor last left it, and the whole point of the restore is to return to where the operator had it. *Read*
takes the service reading (a response time, a temperature, a queue, an error) into the compass as a position in its band;
the plug declares the band, the law does not guess it. *Write* takes one value, clips it to the cover before it leaves the
plug, sends it through the muscle's own interface, and then reads the lever back from the device and records both the
sent and the taken value; a device that took something other than what was sent (a clock that rounds to 15 MHz steps, a
pool size the pooler capped) is recorded as it is, not as it was asked. *One writer* compares the lever as found at every
read with the value last written; a lever found elsewhere has another owner, and the plug raises `ForeignWriter`, after
which the governor leaves that lever alone for the rest of the run and says so in its audit and its exit code. *Restore*
writes the snapshot back on stop and reads it back; a restore that does not read back is an error (exit 3), never a
silent success. The same five lines are implemented for Kubernetes objects (annotations hold the snapshot on the object
itself, so a watchdog can restore from the object without the governor's memory), for `nvidia-smi`, for PgBouncer's
console, for Redis's `CONFIG SET`, for the consumer group and for the simulators' knobs, and `tests/test_*` prove each
against a fake device.

**8.3 Power-up order.** Read-only first; then take the knobs, the least consequential first; on stop, hand them back
in reverse order. In the Kubernetes controller the order is: the latency feed and the cluster's own metrics (read); the
HPA target (a setting the HPA accepts and corrects within a minute); the pods' CPU limits (conveyance, in place); the
machines (the slowest and most consequential, through the release gate and the verdict). On stop the machines are woken
first, then the limits, then the target, so the cluster is never left with fewer machines than its pods need while a
setting above them is still being handed back.

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

**8.6 The wire check on the other stacks.** The GPU has a one-command wire check because its wires are the hardest to
get right. The other stacks carry the same proof in a different place: every Kubernetes arm records `kubectl auth can-i`
receipts for what the governor's identity can and cannot do (and fails if it can do anything it must not), checks that
the cluster holds nothing but the harness, and ends with the reset check that every HPA target, replica range, CPU limit
and worker is back at native with no record left; every database, broker and cache arm reads the knob back after every
write and hands it back at the end, and the report says "handed back: yes" or the run is invalid; every simulator arm
checks that every override was handed back. The watching arm, where it is run, is the wire check of the reading: a
watching governor that disagrees with native on any gauge has found a difference in the probe, the load or the machine,
not in Omni-Compass.

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

**Why each requirement is there.** Kubernetes 1.34 or newer is required because the conveyance muscle resizes a pod's CPU
limit in place, which older versions do only by restarting the pod, and a restart is a disruption Omni-Compass never
causes. metrics-server is the HPA's own eyes and the governor's: without it neither knows what the pods use. An HPA with a
CPU target on each governed service is the native controller Omni-Compass sits on; a service without one has nothing for
level 2 to move. A readiness probe and a short preStop pause are what make a drain invisible to clients: the Service
stops sending requests to a pod before it stops, and kube-proxy sends them to another ready endpoint. The response-time
feed is the one wire a cluster does not already have: Kubernetes knows what its pods use, not what its users wait; the
compass needs the second, and `scripts/latency_probe.py` writes it against any HTTP endpoint every five seconds. On the
GPU, root is needed only for the two `nvidia-smi` writes, and a VM must pass the whole card through or the driver refuses
to lock clocks (the wire check's step 3 is where that shows).

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

What `verify.py` checks is worth knowing before it is run, because its last line, `VERIFICATION: PASS` or `FAIL`, is the
only thing a reader has to read. It runs every test in `tests/` (the law, the plugs, the readings rule, every benchmark's
own harness against a fake server), checks the engine's fingerprints against the preregistered registry so that a changed
engine file fails before anything is measured, compares the release's files with its manifest
(`tools/release_manifest.py --check`: the engine, the C++ twins, the live evidence's digests, one object that names the
commit it was written at) and runs the layout check (`tools/layout_check.py`: the declared root, every link and every
named path present). It takes a few minutes on a laptop and needs no network beyond the clone. GitHub runs the same
script on every push under Python 3.12, and each run is listed under the repository's Actions tab with the commit it
checked; a result in this manual is only ever cited from a commit whose run passed.

To know which engine a checkout carries, ask it:

```
python3 tools/omni_version.py                  # omni-v3, omni-v2, omni-v1, or what differs
python3 tools/omni_version.py --commit <sha>   # the same question of any pushed commit
```

Every result table in `results/live/` cites the commit it ran on, and the three-run tools refuse to combine runs from
different engines (section 15). The founder's standing order is that no result is ever read across engines, and the
command above is how a reader checks that for themselves.

### 9.3 The levels

Take them in order. Each has a pass condition; go to the next level only when it holds. The OFF switch works at every
level.

The levels exist because a governor earns authority the way a new operator does: by watching first, then by touching
the setting that is cheapest to undo, then the next. Level 0 touches nothing and proves the software is the software
(`verify.py` checks every sealed file's fingerprint and runs every test). Level 1 watches a live cluster for as long as
the operator likes and logs every decision it would have taken, so the operators can read those decisions against what
they would have done; nothing passes level 1 until they agree with its readings. Level 2 moves the HPA target, which the
HPA itself corrects within a minute if the governor is wrong, and raises replica floors ahead of bursts; it is the first
level that can show a gain and the first that can show a loss, and the paired receipts of section 13 are its pass
condition. Level 3 moves machines, the slowest lever, through the release gate and the verdict; it is where the bill moves
and where the most care is spent. Level 4 hands Omni-Compass the replica decision itself, with the HPA kept as the fast
reflex upward; it is an option, not a step on the way, and the benchmarks in this manual do not use it. Levels 5 to 7 are
the GPU, the CPU and the site, each with its own wire check and its own pass. An installation may stop at any level and
run there indefinitely; most will stop at level 3.

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
| A message broker's consumer group (Apache Kafka) | one knob | the consumer count inside [1, partitions], read from the consumers' own records; the rebalance paid on every move (10.5) |
| A cache's memory ceiling (Redis) | one knob | `maxmemory` through the cache's own console, grown only while the cache is full (10.6) |
| Drone swarms (gym-pybullet-drones; PX4 and ArduPilot next) | one knob a drone | the cruise override inside the autopilot's limits; a separation wall; collisions void the cell (10.7) |
| A database's storage-engine cache (MongoDB under YCSB) | one knob | the WiredTiger cache size through the server's own console, grown only while the cache is full (10.8) |

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

**What the Azure runs taught us.** Three lessons, each recorded as an amendment to the preregistration before the fleet was
dispatched again. First, a fleet is sized by the lever, not by the budget: a 4-worker fleet cannot show the few-percent
machine saving the law makes, so its honest reading is "inside the noise", and running it again would not change that.
Second, a new subscription's allowance is per machine family, so the fleet that can show one machine is built from nine
families at once, each pool at its own list price, and the bill prices each pool separately. Third, a cloud region can
refuse a new cluster for hours at a time (Azure's capacity for new control planes in its region, on both control-plane
tiers); the harness therefore checks the subscription's allowances before it builds anything, so a refusal costs cents and
not a cluster, and every refusal is recorded with its time.

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

**What the database taught us.** The first untouched run on this stack was a loss, and it stays in the preregistration as
it came (`docs/POSTGRES_PREREGISTRATION.md`, "The first untouched run, and amendment 1"): on the read-only workload the
pooler's own clock read 0.11 ms a transaction against a 50 ms line, so the law gave back one idle connection a second until
the pool stood at its floor of two, while the users' 95th percentile went from 4 ms to 3.9 s. The pooler could not see the
time a client spent behind its own schedule waiting to send, so its clock said calm while the users waited; the
preregistration had said so in one line without drawing the consequence. Amendment 1, declared before any counted run,
made the reading the worse of two: the pooler's service time, or the share of its clients queued for a server, so a pool
too small for the offered rate shows at the pooler as clients waiting and the knob fails up to the operator's setting at
once; and it held the dwell on the brake only, never on the gas. The counted runs are three new untouched runs on the
amended rule; the first run is not counted and is not hidden. The confirmed result is a resource held, not speed, and its
confirmed cost is the host's CPU: the compass's own reads of the pooler's console every second are CPU the native pooler
never spends, and they are counted against it.

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

**What the simulators taught us.** Three things a referee should weigh. First, a deterministic simulator makes the
three-run rule stricter, not looser: MuJoCo and pandapower reproduce to the digit on any machine, so their A, B and C must
agree to the digit and any difference is a finding about the harness, while PyBullet reproduces only to a part in a
thousand across machines, which the swarm table discloses as an amendment and tolerates by that much and no more.
Second, a knob that cannot pay is left alone by the physics, not by a rule of thumb: the robot arms' paired trial showed
that two of four arms gain nothing from a speed override and left them native, the cooling model showed that a cap on
cooling power can never remove less heat and so is never a lever, and a battery's reserve is spent only at the wall
because every round trip through the cells costs the efficiency loss (`docs/MECHANISM_OF_ACTION.md`, 9.6). Third, a gain
in one gauge is often a loss in another, and the simulators show both: the grid's losses rise in the four grids with their
own generation while the energy drawn falls everywhere; the buildings' bills rise in the 2023 districts while their peaks
fall; the Panda's copper loss rises while its torque falls. The tables carry every one of those rows, and the index
carries none of them, because they are models.

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
recorded, and started again with a 10,800 s window and 45 s steps. That second machine is the one that produced the
result in section 2.5: three repetitions over 29 hours on one eight-core machine, both arms about 22 s behind a 10,800 s
window, no repetition off the clock.

The same workflow carries a second test. With the input `test=robust` the machine runs the robustness harness's long
scenario instead of an organism (`scripts/kind_paired.sh` with `ROBUST=long`, exactly as the GitHub job runs it), with
the window stretched to whatever `duration_s` asks and the wandering load schedule repeated to fill it; the 24-hour run of
section 16.8 uses it, one paired repetition on each of three rented eight-core machines of three families (the start job
tries the size it is given and falls back through the eight-core sizes the subscription may rent when the allowance refuses
it; the four-core size asked for was refused because the tower's machine held its family's allowance, and the
preregistration records what was rented), collected and deleted at 60 hours at the
latest. The cells it writes are named `robust-long-x<window>-<repetition>` beside the organisms' `six-<organism>-x<copies>-
<repetition>`, and the collect job gathers both. The `max_hours` input is the machine's own limit, written into the
machine at start, so a collect that finds a machine past its limit takes what is there and deletes it, whichever job
started it.

Three things a reader should know about any detached result. The machine is one Azure virtual machine rented for this
run alone, not a GitHub runner shared with a queue of other jobs, so its size is known (the table names it) and it is not
cut off at six hours; that, and not only the job limit, is why the big organisms are run there. The files come back
exactly as the machine wrote them, copied cell by cell with the machine's own log beside them, and the archive bot stores
them under the collect run's number with a SHA-256 list of every file, so the start run and the collect run are both
cited in the table. And the machine is deleted after the collect, so a result cannot be re-read from the machine, only
from the archived files; the preregistration says this before the first start.

### 10.5 A message broker's consumer group

Apache Kafka is wired as an operator runs it (`docs/KAFKA_PREREGISTRATION.md`, `tools/run_kafka.py`): one broker as
shipped, a topic of eight partitions, a consumer group at the operator's count of two. Nothing models the broker. The
wire in is the group's own end-to-end latency: each message carries its production time, each consumer records when its
handling ended, and the reading is the mean over the messages consumed in the last second; a second with nothing consumed
while messages wait reads as the line (someone is waiting and no one is taking), and nothing consumed with nothing
waiting reads as calm. The wire out is the count of consumers in the group, which is what an operator changes, inside the
cover [1, 8]: never fewer than one, never more than the topic has partitions. The compass holds the reading at 40% of a
500 ms line with a response time of 3 s, because a consumer added or removed shows only after the group rebalances. Slow
service with messages waiting adds consumers in proportion to the force; calm with nothing waiting gives back one idle
consumer a second after a five-second dwell; at 95% of the line every consumer the topic can use starts at once. The
rebalance that every move costs is paid by Omni-Compass and counted in the gauges. At the end of every omni arm the count
is handed back to the operator's and read back. The result (section 16) is the shape this wiring predicts: the queue kept
short, no message lost, at the cost of consumers running, which reads worse by rule and stands beside the gain.

### 10.6 A cache's memory ceiling

Redis is wired as Ubuntu ships it, with the two settings an operator sets for a cache, a memory ceiling of 64 MB and the
allkeys-lru eviction rule (`docs/REDIS_PREREGISTRATION.md`, `tools/run_redis.py`). The application in front of it is ours
and declared: 1,500 requests a second from 32 threads on a Zipf working set that widens and narrows one notch at a time;
a miss costs a declared 5 ms trip to the store behind the cache and a write-back. The wire in is the application's own
request latency, the mean over the last second (a hit about 0.3 ms, a miss about 5.5 ms). The wire out is one setting
through Redis's own console, `CONFIG SET maxmemory`, inside the cover [16, 512] MB. The compass holds the reading at 40%
of a 2 ms line. Its direction rule carries the do-no-harm gate in the form this stack needs: misses grow the ceiling by
notches of 8 MB **only while the cache is full** (memory used at 90% of the ceiling or more), because a miss in a cache
with room to spare is a cold miss that no ceiling can mend; calm with nothing evicted in the last second gives back one
notch a second, after a five-second dwell since the last growth; at 95% of the line with the cache full a quarter of the
cover is added at once. One writer: a ceiling found at a value Omni-Compass did not write stops it. At the end of every
omni arm the ceiling is handed back to the operator's 64 MB and read back. The memory the compass holds for a wide
working set is the resource this benchmark trades and reads worse by rule; the gain is the hit rate and the work inside
the line. The result (section 16.4) is exactly that shape: on all three untouched workloads the work inside the line and
the hit rate rose 14% to 27% and the ceiling held rose from 64 MB to 200 to 270 MB, with the host's CPU inside the noise
and every ceiling handed back.

### 10.7 Drone swarms: the autopilot's cruise

In gym-pybullet-drones (University of Toronto, MIT License; `docs/SWARM_PREREGISTRATION.md`, `tools/run_swarm.py`) every
Crazyflie 2.x flies its shipped position controller along the planner's path at the planner's cruise: that is native. The
wire in is each drone's tracking error, the distance between the drone and the point its autopilot was told to be at, on
a band from 0 to a declared safe error of 0.25 m. The wire out is one knob a drone, the cruise override: the fraction of
the planner's cruise the carrot moves at, never under 1.0 (the planner's own) and never over 2.0 (a quarter of the
autopilot's own speed limit), moving by at most 0.01 a control tick. With slack the compass spends it as speed; as the
error grows it eases; at 95% of the safe error the cruise is the planner's at once. Two guards belong to this stack: a
**separation wall** (a drone with another within 0.5 m flies the planner's cruise, whatever the error reads) and the
**paired physics trial** before the counted missions, which asks the simulator's own figures whether a faster mission
costs less energy at all and keeps the error under the safe error; where it does not, the override is left native for
that cell and the cell reads "nothing for Omni to move". Energy is a declared model from the simulator's own motor
constants, said to be a model wherever it is printed; a collision voids the cell. At every landing and at the end of the
run the override is handed back and read back.

### 10.8 A database's storage-engine cache

MongoDB is wired as an operator runs it (`docs/YCSB_PREREGISTRATION.md`, `tools/run_ycsb.py`): the 8.0 series from its
publisher's own signed repository, its configuration as shipped but for the one setting an operator sets for the storage
engine, the WiredTiger cache, at 512 MB. The questions are asked by YCSB, the published cloud-serving benchmark, running its
own core workloads as the project ships them, with the key space stepping one notch at a time through the cache and past
it, so the working set fits the operator's cache at the low notches and outgrows it at the high ones. The wire in is the
server's own mean read latency over the last second, from its `serverStatus` operation latencies, differenced. The wire out
is one setting through the server's own console, `setParameter wiredTigerEngineRuntimeConfig cache_size`, inside the cover
[256 MB, 2,048 MB]: the server's own floor at one end, a quarter of the machine at the other. The compass holds the reading
at 40% of a 1 ms line (written as 2 ms before the first smoke run and set at 1 ms on the tuning workload's figures, as the
preregistration reserved; see below). The direction rule is the cache's: slow reads grow the cache by notches of 64 MB only while the
cache is full (bytes in it at 90% of its size or more), because slow reads in a cache with room to spare are not the
cache's to mend; calm with no page evicted in the last second gives back one notch a second after a five-second dwell; at
95% of the line with the cache full a quarter of the cover is added at once. One writer, read-back and the hand-back at the
end are the plug's, as everywhere. Disclosed before the run: on a machine where the data files fit in the operating
system's own page cache, a storage-engine cache miss is a read from memory and a decompression, not a disk read, so the
gain available to this knob is smaller than it would be on a machine whose data does not fit in memory; the result will
say what it is. The same plug fits any store whose engine exposes a cache size at run time (InnoDB's buffer pool, RocksDB's
block cache) and any store that does not can only be sized at restart, which is not a knob Omni-Compass moves.

**What the smoke runs taught, and why they are in the record.** A benchmark of a cache is only a benchmark if the
working set reaches the cache. Three smoke runs of the tuning workload, one repetition each and none counted, were needed
before the harness asked the question it was built to ask, and each is written in the preregistration with its run number
and its figures. The first failed before an arm ran, on two harness faults (a relative file path handed to a program that
runs from its own directory; a server log copied as a file the upload step could not read). The second ran end to end and
showed the design did not touch the cache at all: YCSB's shipped request distribution is zipfian, which concentrates
almost every request on a few thousand hot records whatever the key space, so at the top notch of 1.5 million records the
cache held 36 MB of its 512 MB, both arms answered inside the line with a p95 of 0.20 ms, and omni, seeing calm and nothing
evicted, gave memory back to the floor of the cover. That would have read as a free memory saving for Omni-Compass, and it
would have been worthless: a knob with nothing to do had moved to its floor. The requests were changed to a uniform draw
over the notch's key space so the working set is the key space, the one departure from YCSB as shipped, and said so. The
third smoke still held 38 MB, and the per-notch figures the runner now prints showed why: the dataset was loaded with
ordered keys but the run phase used YCSB's default hashed keys, so every read asked for a record that did not exist and
was answered from the index alone, which fits in a few megabytes. The run phase now names ordered keys too. Nothing in the
rules, the gauges or the workloads changed across the three. The fourth smoke reached the cache: native held 336 to 481 MB
of its 512 MB across the notches and read 453,000 pages into it, and its per-notch figures set the line. The server's mean
read latency ran 0.15 to 0.24 ms while the cache held the working set and 0.23 to 0.33 ms while it did not, with a p95
never above 0.42 ms; against a 2 ms line every one of those readings sat in the bottom quarter of the band, under the 0.4
center, so the compass could only ever read calm, the same fault as a Kubernetes line set at ten times the service's normal
response. The line was set at 1 ms, the one change the preregistration had reserved for the tuning workload, with the
center unchanged, so that a hit is calm and a full cache reading past 0.4 ms is slow; the one repetition's whole-arm figures
(work inside the line −1.9%, cache held −31%, pages read +32%, host CPU +8%, p95 equal) are recorded and not counted. The
point for a referee is the method: a result that flatters the governor is the first thing to suspect, the suspicion is
pursued to a harness cause, the cause is written down with the run that showed it, a band is set on the tuning case's own
figures and never on an untouched one, and the counted runs begin only when the harness provably asks the question.

### 10.9 A database's buffer pool, resized online in the server's own chunks

MySQL is wired as an operator runs it (`docs/MYSQL_PREREGISTRATION.md`, `tools/run_sysbench.py`): the 8.0 series from
Ubuntu's own package, its configuration as shipped but for the settings an operator sets for InnoDB, the buffer pool at
512 MB (MySQL's own default is 128 MB, and the preregistration says why 512 MB is the operator's setting here), the chunk the
server resizes in at its shipped 128 MB, one pool instance, and the performance schema on. The questions are asked by
sysbench, the standard OLTP benchmark Ubuntu ships as its own package, running its published scripts as shipped at a fixed
offered rate, with the number of tables in use stepping one notch at a time through the pool and past it. The wire in is
the server's own mean statement latency over the last second, from the performance schema's statement summary,
differenced. The wire out is one statement through the server's own console, `SET GLOBAL innodb_buffer_pool_size`, inside
the cover [128 MB, 2,048 MB] and always in whole chunks, because that is how the server itself moves the pool. Two things
about this knob differ from the MongoDB cache and the plug carries both. The server resizes asynchronously and reports its
progress in its own status variable, so the plug waits for the resize to complete before reading back, and a pool found
mid-resize is the server still carrying out Omni-Compass's own write, not a foreign hand. And a shrink evicts pages while
the resize runs, so the dwell after any move is ten seconds rather than five. The compass holds the reading at 40% of a
0.6 ms statement line (written as 1 ms, set on the tuning workload's smoke runs, as the MongoDB line was: a hit reads 0.14
to 0.22 ms across GitHub's runners and a full pool missing a third of its reads 0.05 to 0.06 ms more, so the center sits at
0.24 ms, above the hits and under the misses); the direction rule is the cache's with one difference the smoke runs forced:
slow statements grow the pool by chunks only while the pool is full, at 95% of the line with the pool full four chunks are
added at once, and calm gives one chunk back after the dwell only while the pool's misses are under one percent of its read
requests, because InnoDB keeps stale pages resident, so neither "pages free" nor "no page read from disk" ever says that a
pool holds its working set, and the miss share does. The work-inside-the-line
gauge uses a transaction line, the statement line times the statements a transaction as sysbench's script ships it (one for
a point select, fourteen for the read-only mix), and says so. One writer, read-back and the hand-back at the end are the
plug's, as everywhere. The same disclosure as MongoDB's holds and is made before the run: on a 16 GB machine with a 1.4 GB
dataset a pool miss is a read from the operating system's page cache, not from disk.

**What the first counted set taught about this knob.** Three runs of five workloads (`results/live/V3_SYSBENCH.md`, 8 October)
read every gauge inside the noise, and 15 of the 45 omni arms did not read the operator's pool back at the end. The audits
show the server still "withdrawing blocks" of a shrink the law had asked for when the arm ended: InnoDB withdraws the last
blocks of a shrink only when the pages the load has pinned are released, so under load the withdrawal does not finish, and
the server ignores a new `innodb_buffer_pool_size` while a resize is in progress, so the restore the plug issued at that
moment was dropped. Every following arm began from a fresh server at the operator's setting, so no other arm was affected,
and the decision loop never wrote during a resize (its writes are gated on the status); only the restore was. The plug now
waits for the resize the server is carrying out (the load has stopped by then, so a stalled withdrawal finishes), writes the
snapshot, and writes once more if the server ignored the first write; the receipt of that restore (what was in flight, the
seconds waited, the writes, the final read-back) is in every omni arm's record and the table counts the arms. The rows of the
first set stand as they are, hand-back NO included, in `docs/history/V3_SYSBENCH_set1.md`; the preregistration carries the
finding and the amendment; and the second counted set, run on the amended plug the same afternoon with nothing else changed,
handed the pool back on all 45 omni arms and is the result in section 16.4. The lesson is general and is the reason section 7.2 exists: a
knob the device applies on its own time has to be handed back on the device's time, and the proof of the hand-back is the
read-back, not the write.

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

**The three ways a governor stops, and what each leaves behind.** A referee or an underwriter should know exactly what
happens to a governed system in each of the three ways Omni-Compass can stop, because the answer is the same in all
three: every setting at native, read back, with no record left.

- **The reset** (the brake held to the floor) is the planned end of a run. The governor sees its reset file, hands every
  setting back in reverse order of power-up, reads each back, writes its last audit line and exits 0. Every benchmark arm
  ends with one and then checks the cluster from outside the governor: the HPA target at the operator's, the replica range
  as set, every pod's CPU limit at its shipped value, every worker back in service, no `omnicompass.io/` annotation left on
  any object. An arm whose reset check fails is invalid and is left out of the table, never counted.
- **The kill switch** (security) is the unplanned end of trust. `tools/omni_switch.py off` writes the switch file and
  sends every registered governor SIGTERM; each performs the same hand-back as a reset and exits; the command waits until
  all have and reports any that have not. No governor starts while the switch is off. It is one switch for the whole
  machine, not one per muscle, because the case it exists for, something driving a system through Omni-Compass's brain, is
  not a case for picking which muscle to stop.
- **A death without a hand-back** (killed outright, a crash, a hang) is the case the lease covers. Before its first write
  every governor registers itself with the exact command that puts every setting back
  (`omni_controller.controller --restore-only`, which restores from the snapshot annotations on the objects themselves,
  so it needs no memory of the dead process), and renews a lease every decision. The watchdog
  (`tools/omni_switch.py watchdog`), run as its own service beside the governors, finds any governor whose process is gone
  or whose lease is older than its limit (five decision periods, at least two minutes), stops a hung one, runs its
  recorded restore command, and records what it did. The robustness benchmark (section 16, in preparation) kills the
  governor outright in the middle of a governed run and measures how many seconds pass before every setting is back and
  what the service saw in that gap.

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
| `"watchdog": "handed back"` (in the watchdog's own log) | a governor died or hung without handing back; the watchdog ran its recorded restore command; `ok` says whether every command exited 0 |
| `cruise: on` / `cruise: off` | work waited for a place for two decisions: every machine in service; the line has been empty for two: cruise ends |
| `emergency_brake` | the work is done and demand is at zero: straight to the floor in one move |
| `verdict_state: left native` | no step of the slow knob passed the paired trial: the knob is never moved on this muscle |
| `shield_interventions` | the shield clipped a write to its bounds or its step limit; the count says how often |
| `overhead` (the last line of the audit) | the governor's own CPU over the window: its process and every command it ran |

**How to read an audit from end to end.** The audit (`audit.jsonl`, one JSON record a line, every line timestamped) is the
governor's complete account of itself, and a reader can follow a run through it without the manual: the first lines are
the snapshot (every setting as found, written to the objects as annotations so a watchdog can restore from them); then,
every decision, the readings (the response time and its age, the pods waiting, the machines seen, whether any sense is
blind), the compass's position and force (`compass`), the authority the nervous system granted and the release gate's
reason (`authority`, `node_gate`), the decision itself (the machines recommended against the machines seen, the HPA
target set), every write with the command that made it and the value read back, and the decision's wall time
(`decision_ms`); in cruise, the floor step's silence; at the end, the reset's writes and read-backs and the `overhead`
record. The benchmark harness prints a decision trail from the audit at the end of every omni arm (`scripts/kind_bench.sh`),
one line a decision, so a reviewer reading a run's log sees what the governor saw and did at each minute.

## 12. Maintenance, Upgrades and Security

- Run `python3 verify.py` after every upgrade; it must end `VERIFICATION: PASS`.
- Upgrade in watch mode first; take the levels again from level 1.

**What an upgrade is, and what it is not.** The engine is frozen and fingerprinted (section 15). An upgrade that changes
any engine file, a rule, a gain, a guard, a preset or a muscle, is by definition the next engine version, and every
published result is run again on it before it is quoted beside the old ones; `tools/omni_version.py` says which version a
checkout carries, and a checkout that matches none says which files differ. An upgrade that changes only the harness,
the tools, the tables or this manual leaves the engine's fingerprint as it was and every result standing; the robustness
harness of section 16.8 is an example, built without touching an engine file. An operator can therefore tell, from one
command, whether a new checkout is the engine the results were made on or something that must prove itself again.
- The container runs non-root, read-only, with no capabilities; the Kubernetes identity has only the permissions of
  the level you run.
- The GPU governor needs root only for `nvidia-smi -pl` and `-lgc`.
- Report a security issue as `SECURITY.md` describes.

**Least privilege, proven on every run.** The Kubernetes governor runs as its own service account
(`deploy/kind/rbac-omni.yaml`) with exactly the verbs the level needs: patch on the governed HPA, nodes, pods and the
governed deployment, get on its security ConfigMap, create on pod evictions. It cannot delete nodes, create or delete pods
or deployments, touch the load generator or anything in `kube-system`, read any secret, create a namespace, or write its
own security hold. Every benchmark arm records `kubectl auth can-i` for each of these and fails if a "cannot" reads yes
or a "can" reads no (`bench-*/rbac_omni.txt` in every archived run). The security hold itself is a ConfigMap another
identity owns: when its key reads `hold: "true"` every expansion is blocked, and the governor cannot clear it.

**What never leaves the repository.** Cloud credentials live only in the repository's encrypted secrets and are used
only by the workflows that need them; no credential, key or token appears in any file, log, table or commit, and the
founder is never asked for one in conversation. The repository carries SPDX license identifiers on every source file so
that license scanners (Black Duck, FOSSA, Snyk) read the evaluation license correctly, and every generated report carries
the legal notice at its head and foot (`tools/legal.py`). Patent, copyright and trademark filings are referred to as
filed; no filing number appears anywhere.

**Supply chain.** Everything the benchmarks download is pinned and checked: metrics-server by version and SHA-256
(`scripts/kind_bench.sh`), Apache Kafka against the Apache Software Foundation's own SHA-512 file for that release,
Redis as the Ubuntu runner's own package, MongoDB from its publisher's own repository signed by the publisher's key and
YCSB against the SHA-256 written in its preregistration, gym-pybullet-drones at one named commit, Python packages by
`requirements.txt`. A download whose checksum does not match stops the run before anything else happens.

**The upgrade drill, step by step.** An operator who receives a new checkout does five things, in order, and stops at the
first that fails. First, `python3 tools/omni_version.py`: if it prints the version the operator's results were made on, the
engine is unchanged and the rest of the drill is about the harness; if it prints a list of differing files, the checkout
is a new engine and nothing the operator measured before applies to it until measured again. Second, `python3 verify.py`,
which must end with its pass line; the verifier runs every unit test, the shield's adversarial cases, the Python-against-C++
agreement and the release manifest, and a checkout that fails it is not installed anywhere. Third, the wire check on the
operator's own stack, which proves that every wire the new checkout would use still follows, reads back and returns.
Fourth, watch mode for at least one full cycle of the operator's load, reading the log the governor would have written
and comparing its would-be decisions against what the operator would have done. Fifth, the levels again from level one,
each with its paired receipt. An upgrade that skips a step has not been upgraded; it has been installed.

**The security hold, and who holds it.** The hold is the one control that outranks the governor's own judgment, and it
is deliberately not the governor's to hold. It lives in a ConfigMap owned by another identity (the operator's security
team, in practice); while its key reads true, every expansion the governor would make is blocked and every contraction is
still allowed, so a governor under a hold can only give capacity back, never take more. The governor reads the hold on
every decision and records in its audit that it read it; it has no verb that could write it. The kill switch (section 11)
is the blunter instrument beside it: the hold constrains a running governor, the switch stops every governor on the machine
and hands everything back. An operator who suspects anything untoward uses the switch first, reads the audit second, and
rotates the governor's identity third; the hold is for the slower case of a change window or an incident elsewhere during
which no one wants capacity added.

**What has been reviewed, and what has not.** Reviewed and tested on every run: the governor's permissions against the
list above, read from the cluster itself; the shield's refusal of every write past a cover, of every give-back while
blind, and of every move under a hold, on two million generated cases; the lease and the watchdog's hand-back on a real
cluster, thirty times (section 16.4b); the checksums of every download. Not yet done, and said so: an independent
security review of the code by a party outside the company, which is in the open program (section 16.8), and a
penetration test of the deployed governor on a customer-like cluster. Until those are done, the operator's own review
stands in for them, and this section tells the operator exactly what to look at.

---

# PART VI - PROVING IT

## 13. Paired Runs and Receipts on Your Own System

The method of every benchmark in this manual is the method a reader can use on their own system, and it is deliberately
simple: the same system, the same work, native and then omni back to back on the same machines, repeated with the order
rotated, each gauge reported with the 95% interval of its paired difference. Pairing is what makes a difference of a few
percent visible on a shared machine whose own noise is larger than that: two arms run minutes apart on one runner see the
same neighbours and the same hour, so their difference is a difference between arms, while two arms on separate machines
differ by about 15% in p95 on their own. The order rotates so that no arm always runs first, warm or cold. The work is held
equal by an open-loop load, a fixed rate of requests at fixed moments, so that a lower resource count can never mean that
less work was done. The steps below are the whole method.

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

**How many repetitions, and why.** The width of a paired interval shrinks with the square root of the number of pairs,
so going from five pairs to ten narrows it by about a third, and from ten to forty by half again. On GitHub's runners,
ten pairs of a 900 s window put the interval on work inside the line at about ±10 points of native and on p95 at ±13
to ±29 points (the all-four table: +48.6% with an interval of +38.7 to +58.4; p95 −61.6% with −74.8 to −48.4), wide
intervals that still confirm because the gains are tens of percent; the energy intervals on the same runs are ±0.2 to
±3%, narrow because the gauge is a declared formula over counts of machines, and that is why energy there reads "no
difference beyond the noise" honestly rather than as a small claimed gain. A gain of a few percent on a cluster would
need forty pairs or more to confirm at these widths, and the manual does not claim one anywhere a table shows it
inside the noise. Three pairs of a 7,200 s window, the long run's shape, give a wider interval on each run
but three such runs, each read on its own, still have to agree in sign for a confirmed reading. On a stack with a finer
knob (connections, consumers, megabytes) the intervals are narrower at three pairs than the cluster's at ten, because
the knob moves in hundreds of small steps rather than in whole machines. An operator planning their own receipt should
run five pairs first, look at the interval widths on the gauges they care about, and set the count for the published
run from those widths, never from the result.

**Why the load is open-loop.** A closed-loop load generator waits for each answer before sending the next request, so
a slower system is offered less work and its throughput "improves" its own latency; two arms under closed-loop load are
not doing the same work. An open-loop generator sends requests at fixed moments whatever the system does, so both arms
are offered the same work to the request, a queue forms when the system falls behind, and the time over the line and
the failed requests record the cost. Every real-stack test in this program (the cluster's load generator, pgbench's rate
limit, Kafka's producer at a fixed rate, Redis and YCSB at a fixed target rate) offers its work open-loop, and a lower
resource count in the omni arm can therefore never mean less work was asked.

**What a receipt looks like.** One row per gauge: the gauge's name and direction; native's value and omni's; the paired
change as a percentage of native with its 95% interval; the reading. A head naming the system, the knob, the cover, the
window, the number of pairs, the order rotation, the engine's fingerprint and the commit; a foot saying whether every
arm was handed back and whether any repetition was off the clock. `tools/live_reps.py` prints exactly this for a
Kubernetes run and the three-run tools print it for three runs side by side; a receipt from any other tool should be
laid out the same way so that a reader of this manual can read it without learning a new shape.

## 14. Evidence Classes and How to Read a Result

| Class | Rung | What it is | What it can show |
|---|---|---|---|
| T / V | E1 | deterministic tests, proofs, Python against the C++ twin | the law is what it says, and both languages agree |
| S | E2 | simulation on a modelled plant | whether the law helps the model, and where it breaks |
| L | E3 | real software (Kubernetes on kind), no hardware meter | real decisions on real software; energy there is a declared model |
| P | E4 | a physical meter (the GPU's own power reading) | the hardware's own answer |

Read every number with its class beside it. A simulation number is never quoted as a hardware result. When a
receipt's energy line is modelled, the receipt says so.

**What each class can and cannot carry, with the examples in this manual.** A class **T / V** result (the C++ twin
agreeing with the Python to 3.6 × 10⁻¹⁵ on 500 trajectories; two million adversarial cases through the shield with zero
violations) says that the law is what the text says it is and that both implementations compute it; it says nothing
about whether the law helps any machine. A class **S** result (the 945 muscles, the organisms at 1,000 copies, the power
grid in pandapower, the robot arms in MuJoCo, the buildings in CityLearn, the drones in PyBullet) says what the law does to
a published model of a plant under that model's own native controller; it carries exactly the model's fidelity and no
more, which is why S results are shown beside the Omni index and never inside it, and why the manual says "the energy is
a declared model" on every S line that reports energy. A class **L** result (real Kubernetes on kind, PostgreSQL behind
PgBouncer, Apache Kafka, Redis, the organisms with the real cluster inside) says what the law did to real software making
real decisions on real requests; the machines, where they are containers on one runner, are counted in machine-hours in
service and their energy, where it is reported, is a declared formula, which the table says; the CPU seconds of the host
are measured. A class **P** result would say what a physical meter read, and the one P instrument in this program, the
GPU's own power reading, has no current result: every earlier card result ran on a controller since replaced and is
obsolete. Azure's bill is an L result with a real bill: the machines billed are Azure's own count, the price is Azure's
list price, and the energy is still not a meter.

**How to read a row.** Every row in every three-run table has the same shape: the gauge and its direction; native's
value in run A and omni's value in run A, so the size of the numbers is visible; the paired change in each of the three
runs as a percentage of native with its 95% interval; and the reading. Read the reading first, then the intervals, then
the sizes. A reading of "confirmed better" with intervals of −0.5% to −0.1% is a small, real effect; a reading of "no
difference beyond the noise (3 of 3 runs)" with intervals of −30% to +25% is a test that could not see an effect of that
size either way, which is a statement about the test's power, and the manual says so where it applies (the 4-worker Azure
fleet). A "confirmed WORSE" row is a loss, stands in the table, and enters the index as a loss.

**A worked reading, from the cache table.** Take the Redis table's `large` workload (`results/live/V3_REDIS.md`). The
product row, work inside the 2 ms line, reads confirmed better, with the three runs' paired changes each clear of zero and
of the same sign; that is the gain. The resource row, the memory ceiling held, reads confirmed WORSE: Omni held a ceiling
of about 256 MB on average where the operator had set 64 MB, in every run, clear of zero. The two rows together are the result: the
cache answered more requests inside the line because it was given more memory, and the table says both. A reader who
quotes the first row without the second has misread the table, and the index is built so that this cannot happen there:
the cache's category enters the one number as a loss (about 0.75 on its own), because the resource it spent is counted at
full weight against the work it gained. The CPU row, inside the noise, says the host did not pay in processor time; the
failed-request row, zero in both arms, says nothing was refused to get there. Four rows, three directions, one honest
sentence: more work inside the line, bought with memory, at no cost in CPU or refusals. That is how every table in
section 16 should be read, row by row, before any sentence about it is written.

**Three questions to ask of any class L result.** First, what was native, exactly: which controller, at which published
version, with which settings, and were those settings an operator's or ours? (Every preregistration names them; the
broker's native was set at its knee by design and says so.) Second, what did the governor spend: machines, memory,
connections, CPU, its own cost? (Every table has the resource rows; a result with a gain and no resource row is not in this
program.) Third, who else could have produced the gain: the order of the arms, the warm-up, the runner's neighbour, the
clock? (Rotation of the arm order, the warm-up before every window, the paired design on one machine and the clock rule
are the answers, and section 16.7 names the residue they do not remove.)

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
Kubernetes and Azure tests, `pgbench_abc.py`, `kafka_abc.py`, `redis_abc.py`, `swarm_abc.py`, `mujoco_abc.py`,
`pandapower_abc.py`, `citylearn_abc.py`; a deterministic simulator's three runs must reproduce each other to the digit,
or to the declared tolerance where the simulator is not bit-reproducible across machines, and a score reads "the runs
differ" when they do not), and `tests/test_confirm_abc.py`, run by `verify.py`, proves the rule on fixed cases.

**Why three separate runs, and why the readings are what they are.** One run of ten paired repetitions gives one
interval, and an interval from one run can be narrow by luck: the runner was quiet that hour, the order of arms happened
to favour one side. A second run on another day and another machine is a replication; a third makes a coincidence
expensive. The three runs are separate GitHub runs, which means separate machines, separate hours and separate
installations of every dependency, so what agrees across them is not an artefact of one machine. The readings are
designed so that there is no reading a reader could mistake for a weaker form of "yes": a row is confirmed only when all
three runs move the same way with every interval clear of zero; a single run whose interval crosses zero makes the row
"no difference beyond the noise", and the count says how many of the three; and two clear runs that disagree in sign are
reported as a disagreement, which is an instability in the test to be found and fixed, not averaged away. The tables are
made by tools, not by hand, and the tools check each run's engine and refuse to mix engines.

**The Omni index** (`tools/omni_index.py`, `results/OMNI_INDEX.md`) is the one combined number. Every measure of every
test is a ratio oriented so that above 1 is better for Omni-Compass on top of native: work (more), speed (a lower
response time), machines (fewer), energy (less). A test's index is the geometric mean of its ratios, a category's the
geometric mean of its tests, the headline the geometric mean of the real categories, each weighted the same. A measure
enters only as its three-run reading allows: confirmed better or worse counts as the geometric mean of the runs'
ratios; no difference beyond the noise counts as exactly 1. Modelled muscles are shown beside the index, never inside it.

**Why geometric means, and three rules a referee should check.** A ratio of 2 and a ratio of 0.5 are the same size of
effect in opposite directions; their arithmetic mean is 1.25, which would read as a gain, while their geometric mean is 1,
which is the truth. Geometric means also make the index indifferent to which side a gauge is written from (work per
machine or machines per unit of work), and they let a category of three tests and a category of six weigh the same.
Three rules follow from the design and can be checked in the tool: first, the tuning workload or tuning cell of every
benchmark is excluded, because the rules were fitted on it; second, no row inside the noise contributes anything, in
either direction, so the index can never be moved by a run that happened to be quiet; third, the categories are the real
ones only (Kubernetes, the database, messaging, the cache as it lands, Azure and the card as their tables land), each
weighed the same whatever the number of tests inside it. The index therefore answers one question only: across every real
category confirmed three times, what did Omni-Compass on top of native deliver in more work, faster answers, fewer
machines and less energy, counting the resources it spent against it. The index page says, where a ratio is large, why
it is: in messaging, native sat at nine tenths of its measured capacity by design, so its queue grew at the high steps and
Omni's did not, and a queue kept short against a queue that grows is a large ratio in response time.

## 16. Results to Date

Every result below is Omni-Compass **on top of** a native system against the same native system alone, with the same
work in both arms, read by the three-run rule of section 15, on the engine named. Losses are in the tables beside the
gains. The whole list, benchmark by benchmark with its native engine, its knob, its gauges and its file, is
`docs/REGISTER.md`; the program that takes every benchmark to full size is `docs/PROOF_PROGRAM.md`.

How to read the chapter. Each section names the stack, the native controller Omni-Compass sat on, the one knob it moved,
the result file in `results/live/` or `results/`, the three GitHub run numbers (or the rented machine's start and
collect runs) and the engine version those runs were on; a reader can open the file, find the runs under the repository's
Actions tab, and check the commit with `tools/omni_version.py --commit`. The figures quoted in prose are the table's
figures and no others; where a range is given ("−13% to −37%") it is the span of the three runs' point estimates, not an
interval. Every row of every table has one of the readings of the three-run rule (section 15): confirmed better, confirmed WORSE, no
difference beyond the noise with the count of runs, or the runs disagree; rows that are shown and not judged say so and
why. A loss is written in the same sentence as the gain it came with, never in a footnote, and the index (section 16.6)
counts every confirmed loss against Omni at full weight.

Two cautions a referee should hold while reading. The real-software results (evidence class L) were taken on GitHub's
shared runners or on single rented machines, with the host's CPU-seconds as the only measure of energy and no meter on
the wall; sections 13 and 14 say what that does and does not allow. And the modelled results (evidence class S) are
reported as what they are, our own plant models run whole, and are never summed with the live ones; the index is built
from the real categories alone, and the modelled realms sit beside it as a separate finding about the law's coherence
at scale.

### 16.1 Real Kubernetes: six tests, ten pairs each, three runs each

The six Kubernetes tests were designed to ask six different questions of the same cluster, and they are read together.
The cluster is kind: a real Kubernetes control plane and six worker nodes as containers on one 4-core GitHub runner, with
a real metrics-server, a real HPA at the operator's target of 50% CPU, a real PHP service behind a NodePort, and a real
load generator whose replica count steps through a schedule identical in both arms. A real probe times HTTP requests
every five seconds from outside the service. Native is that cluster with its HPA alone; omni is the same cluster with the
compass law on the HPA target inside [30%, 50%] and on the machines through the release gate and the verdict. Both arms
start from the same fresh cluster, run for 900 s after a 120 s warm-up, and end with the reset check.

- **Steady work in steps** (`V3_STEADY.md`) asks: at a fixed, stepped load, does the governor hold the same work with
  fewer machines or faster answers? Work is equal by design. The 95th percentile fell 65% to 66% and the 99th 68% to
  72% in all three runs; machines in service fell 1.5% to 2.9% and the standby-model energy 1.3% to 2.1%; time over the
  line fell 97% to 99%; failed requests were zero in both arms. The machine saving is small because the verdict kept every
  machine whose removal made requests slower in the paired trial.
- **Demand that wanders** (`V3_WANDERING.md`) asks: when load goes up and down one step at a time, does the governor
  follow it without harm? p95 fell 57% to 63%, p99 40% to 51%, the mean 46% to 49%, time over the line 39% to 40%, and
  failed requests 9% to 12%, all confirmed better; machines and energy read inside the noise.
- **All four in one run** (`V3_ALL_FOUR.md`) asks the product question: more work, faster, on fewer machines, with less
  energy, in one run. Work inside the response line rose **35% to 49%** (21.0 to 31.2 requests a second in run A), p95
  fell 61% to 66%, failed requests 11% to 14%, all confirmed better; machines and energy inside the noise.
- **Faults** (`V3_FAULTS.md`) asks: when a machine dies, traffic triples, a pod runs away and the probe goes blind, at
  the same moments in both arms, does the governor make recovery worse? p95 fell 47% to 62% and p99 39% to 63%, time over
  the line 22% to 42%, confirmed better; failed requests were lower in all three runs and clear of the noise in one;
  machines and energy inside the noise.
- **A queue of batch jobs** (`V3_BATCH.md`) asks: when the work is a pile, does cruise and the emergency brake finish it
  no later and hand the machines back? Machines fell 19% to 23% over the window and 29% to 35% after the queue finished,
  the standby-model energy 13% to 16%, the mean response 10% to 14%, all confirmed better; the queue finished no
  differently beyond the noise in all three runs (on v1 it had read 0.7% to 0.9% later, a loss that stayed in the record).
- **Fairness** (`V3_FAIRNESS.md`) asks: does the governor help or hurt a noisy neighbour on the same workers? No difference
  beyond the noise on every row, the neighbour's own p95, p99, failures and time over the line included.

The same six tests were run on Omni v1 with the same readings (`V1_*.md`), the controllers being the same bytes, and the
v1 tables stay as the first engine's record. The earlier engines' sets, before the verdict, parked 29% to 36% of the
machines and paid for it in response time (`docs/history/`); the frozen engine puts service first, and that choice is
visible in every machines row above.

### 16.2 The organisms with the real cluster inside, and the big organisms

The six modelled organisms were run with the kind cluster inside as one more muscle at 1, 10 and 100 copies on GitHub
(`V1_SIX_KUBE.md`, `V3_SIX_KUBE.md`) and at 1,000 copies on a rented Azure machine (`V1_BIG_ORGANISM.md`). At 10 and 100
copies on v3, every one of the twelve cells read better on four to six gauges (response time, time over the line, the
organism's energy and its time over its own line) and worse on none beyond the noise, except a rounding-level work loss
of six to eleven parts in a million in four cells, which the table shows. The four stacked at 100 copies ran off the clock
in four of five repetitions (up to 277 s past a 1,440 s window): the machine could not step 170,000 muscles inside the
window, both arms slipped alike, the pairing stands and the mark stays on the cell. At 1,000 copies on v1 the tower
answered its slowest 5% in 0.2 s against native's 4.1 s and was over its line 0.2% of the time against 64%; the four
stacked read p95 −74% and p99 −83% with the compass arm 300 to 615 s past its 2,880 s window in all three repetitions,
marked off the clock, which is why the v3 stack was run with a 10,800 s window. **On v3 the four stacked at 1,000 copies**
(`V3_BIG_ORGANISM.md`: 1.7 million muscles on one clock with the real cluster inside, three paired repetitions on one
rented machine over 29 hours, 240 steps of 45 s an arm) **kept the clock in both arms**, 22 s behind a 10,800 s window
(0.2%), and read: the cluster's slowest 5% answered in 150 ms against native's 2,882 ms (−95%), its slowest 1% in 165 ms
against 5,405 ms (−97%), time over the response line 51% of samples to none, failed requests 0.14% to none, all clear of
zero with three pairs; replicas, pods started and machines (six in both arms) the same; the standby-model energy −0.6%
inside the noise; the host's CPU −1%, shown. The organism's own model (class S, shown beside the cluster and never inside
the index) read energy −0.4% and work per energy +0.4% better, time over its own line −0.7% better, and work −0.0006%, a
rounding-level model difference that the rule reads as worse and the table shows as such. The v1 stack's loss, the compass
arm falling off the clock, is gone with the longer window; the gain, the cluster's tail, is the same shape at 1,000 copies
as at 10 and 100. The whole tower at 1,000 copies runs the same way on a second rented machine as this edition is written.

### 16.3 The bill on a real cloud

Azure Kubernetes Service with Azure's own cluster autoscaler as native (`V1_AKS_STEADY.md`, `V1_AKS_BURST.md`): five
paired repetitions each on a 4-worker fleet, every machine billed every 15 s at list price, a fresh cluster per arm. Every
gauge read no difference beyond the noise; the bill read −4.7% on steady load and +5.0% on the burst, both with intervals
across zero; the burst's p99 read −34% clear of the noise in that one run. This is the honest reading of a fleet in which
one machine is a quarter of the fleet, so that only a saving of about 30% could clear the noise against an expected saving
of a few percent (section 10.1). The fleet of 40 workers in nine machine families that can show one machine is
preregistered (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendments 1 to 4) and has been refused by Azure's own cluster
capacity in its region on every dispatch so far, each refusal recorded; it runs the moment the region admits a cluster.

The refusals are themselves part of the record, and the preregistration's amendments 5 to 7 keep the count: six dispatches
and 29 refused repetitions in eastus, each with Azure's own reason (its managed-Kubernetes capacity in the region, not
the subscription's quota), a survey of every other region showing none with the vCPU quota the fleet needs, one dispatch
cancelled by hand and recorded as such, and the seventh dispatch left to try. That seventh dispatch was refused on all
five of its repetitions over the morning of 8 October, 34 refusals in all (amendment 8); whatever the region admits on a
later dispatch is read by the same table as the four-worker runs, with the refused repetitions counted in the amendment,
not in the table. A reader should take
from this what it says and no more: the small fleet's bill reading is inside the noise by the arithmetic of its size, the
large fleet's reading does not exist yet, and nothing about the bill on a real cloud is claimed in the index until it does.

### 16.4 A real database, a real message broker, a real cache

Three stacks whose knob is a resource an operator sizes once and leaves, run as the same shape of test: three paired
repetitions a run, three runs, the operator's fixed setting as native, the compass on that setting through the stack's own
console as omni, a tuning workload shown and not counted, and untouched workloads judged.

- **PostgreSQL 16 behind PgBouncer** (`V3_PGBENCH.md`): connections held open fell 61% to 72% on `select` and `tpcb_hot`,
  confirmed better; the runs disagreed on `simple_update`; the host's CPU-seconds rose 14% to 28% on all three, confirmed
  worse, the compass's own cost included and counted against Omni-Compass in the index; work and latency read inside the
  noise. The gain is a resource held, not speed; the cost is CPU, and both are in the table.
- **Apache Kafka 3.9.1** (`V3_KAFKA.md`): on light, heavy and burst, work inside the 500 ms line rose 16% to 21%, the
  end-to-end 95th percentile fell from about 1.6 s to 9 to 14 ms, the mean lag fell 92% to 97%, all confirmed better; no
  message was lost in any arm; consumers running rose from 2 to 5.8 to 7.9, confirmed worse; host CPU-seconds rose 10% to
  20% on light, confirmed worse, and read inside the noise on heavy and burst; CPU per thousand messages inside the line
  fell 10% to 12% on burst. Native sat at nine tenths of its measured capacity by design, so its queue grew at the high
  steps and Omni's did not; the gain is the queue kept short and the cost is the consumers that kept it so. 21 gauge-rows
  better, 8 worse, 0 where the runs disagree.
- **Redis 7.0.15** (`V3_REDIS.md`): on small, large and burst, work inside the 2 ms line rose 14% to 27%, the hit rate
  14% to 27% and the mean latency fell 30% to 61%, all confirmed better; no request failed; the 95th percentile stayed
  within a hair of native's, because a miss costs the declared 5 ms trip in both arms and 5% of requests still miss; the
  memory ceiling held rose from 64 MB to 200 to 270 MB and the memory used with it, both confirmed worse, the resource the
  gain costs; the host's CPU-seconds read inside the noise on all three; keys evicted fell 76% to 92% (shown); every
  ceiling was handed back. 12 gauge-rows better, 6 worse, 0 where the runs disagree. The tuning workload, shown and not
  counted, read the same way (hit rate 75% to 87%, the ceiling 64 to 299 MB).
- **MongoDB 8.0.32 under YCSB 0.17.0** (`V3_YCSB.md`, `docs/YCSB_PREREGISTRATION.md`): the knob is the storage engine's
  cache size, the operator's 512 MB as native, and the question is the opposite of the Redis one: not whether the governor
  will buy service with memory, but whether it will give memory back without losing service. On workloads c and burst the
  cache held fell by about half (512 to about 260 MB) and on f by 13% to 37%, confirmed better; on b it fell 27% to 50% but
  one run's interval included zero, so that row reads no difference beyond the noise; work inside the 1 ms line, p95 and
  p99 read inside the noise on all four workloads (work between −2.7% and +1.1%, every interval over zero); no operation
  failed in any arm; the host's CPU-seconds read inside the noise on all four, +12% to +15% on c with intervals over zero;
  pages read into the cache rose 14% to 58% (shown, not judged: the misses the smaller cache costs); and one row is a
  confirmed loss, the mean latency on burst, +2.2% to +3.7% in all three runs, clear of zero, which stands. Every cache
  size was handed back in every arm. 6 gauge-rows better, 1 worse, 0 where the runs disagree. The tuning workload, shown
  and not counted, read the same way (the cache 12% to 15% smaller, everything else inside the noise). The disclosure made
  before the run held: on this machine the data sits in the operating system's page cache too, so a storage-engine miss
  costs a memory read and a decompression, not a disk read, which is why half the cache could be given back at no
  measurable cost in work or p95 and a few percent of mean latency; on a machine whose data does not fit in memory the
  same knob would be asked a harder question, and this table does not answer it.

- **MySQL 8.0.46 under sysbench 1.0.20** (`V3_SYSBENCH.md`, `docs/MYSQL_PREREGISTRATION.md`): the knob is the InnoDB buffer
  pool, 512 MB at the operator's setting, moved in the server's own 128 MB chunks inside [128, 2,048] MB through the server's
  own console. Two counted sets were run on the same engine. The first (runs 37757840760, 37757850988, 37757861572) read every
  gauge inside the noise and its hand-back row read NO on 15 of 45 omni arms, because the plug's restore was issued while the
  server was still carrying out a shrink the law had asked for, which MySQL ignores; the plug, not the law, was fixed (the
  restore waits for the server's resize and writes again), the fix was declared as an amendment, and the first set's table is
  kept whole in `docs/history/V3_SYSBENCH_set1.md`. The second set on the amended plug (runs 37770617236, 37770620582,
  37770624805, commit `a033fd09`) is the result: on the four untouched workloads **the pool held fell −67% on burst and −50% to
  −56% on read_only, confirmed better**, with the pages holding data falling the same; work inside the line, throughput, p95,
  p99 and host CPU inside the noise on every workload; on read_write, where the working set is written as well as read, the
  compass bought pool for the wide notches and **the pages holding data rose +53% to +70%, confirmed WORSE**, the pool held
  +59% to +79% as point estimates (one run clear of zero), while p95 read −11% to −18% and CPU −4% to −5% inside the noise;
  update_index inside the noise on every row; no error in any arm; **the pool handed back and read back on all 45 omni arms**.
  4 gauge-rows better, 1 worse, 0 disagree; the category enters the index at +12.2%. The update_index "work inside the line"
  row counts almost nothing in either arm (a single update's client round trip exceeds the server-side 0.6 ms line) and is
  disclosed as such.

### 16.4b Robustness: the governor killed outright, and its own cost

The robustness benchmark (`docs/ROBUSTNESS_PREREGISTRATION.md`) is a test of Omni-Compass itself, not of a gain. In the
kill scenario (`V3_ROBUST_KILL.md`, ten pairs in each of three runs), the governor received SIGKILL at 40% of a 900 s
window on the wandering load, with the watchdog running beside it from the start as it would in service. In all thirty
repetitions the watchdog found the dead lease on its next pass, ran the governor's recorded restore command, and every
setting (the HPA target, the replica range, every pod's CPU limit, every worker, the records on the objects) was back at
the operator's **7 to 11 s after the kill**, mean 9 s against a preregistered allowance of 60 s; a second governor started
at 50% and governed to the end in every repetition; and the 120 s after the kill read no difference beyond the noise
against native's same window in all three runs, so the service did not measurably notice the governor's death. The whole
window, with a kill and a restart inside it, still read mean response 32% to 39% faster, p95 42% to 45% faster, time over
the line 28% to 34% lower and failed requests 9% to 15% fewer, confirmed better, with machines and energy inside the noise.
The governor's own CPU over every archived run with the real cluster inside (`V3_OWN_COST.md`) is 0.006 to 0.013 of one
core at every size from 1 to 1,000 copies, 0.1% to 0.3% of the host's cores, each run under its own engine; the cost of
governing a real cluster does not grow with the modelled organism around it.

**The long run** (`V3_ROBUST_LONG.md`, three pairs of 7,200 s an arm in each of three runs) asks whether the governor
drifts, leaks or slows over hours. Its resident memory after two hours was at most 1.048, 1.067 and 1.052 times its first
ten minutes in the three runs, against a preregistered limit of a quarter: no leak. It made 117 to 119 of the 120
decisions its 60-second interval predicts in every repetition, 97.5% at the fewest against a threshold of 95%: valid. Its
decision time, read as the gap between consecutive decisions less the interval it sleeps, was at most 1.20 times in the
last hour what it was in the first: no slowing. Every setting was handed back at the end of every repetition and read
back at the operator's with no record left. Two things are shown rather than judged, as the preregistration said they
would be. First, failed decisions: 2, 3 and 3 in the three runs, all in one repetition's omni arm, all the same cause, the
cluster's own API answering 500 to the governor's read of the HPA for two or three decisions in a row; the governor held,
wrote nothing, and resumed on the next good read, which is the blind-means-hold rule doing what section 7.3 says it does.
Second, the whole window's service: with three pairs a run the intervals are wide, and mean response, p95, p99 and time
over the line read confirmed better in run A and inside the noise in B and C, so the reading is no difference beyond the
noise in two of three runs; machines, energy and failed requests read inside the noise in all three. The long run is a
test of the governor's constancy, and on that question every row answered as the preregistration required.

### 16.5 The modelled realms and the independent simulators

Every result here is evidence class S: a statement about a published model under its own native controller, never about
hardware, and never counted in the Omni index.

- **The 945 muscles and six organisms** (`results/realms/REALMS.md`, A/B/C on v3): reproduced to the last digit in three
  of three runs; zero muscles worse; every organism superior within guardrails, with work per energy +0.1% to +0.3%, work
  unchanged and time over the line not above native's. On v2 the Physics realm and the tower had read a service tradeoff;
  the slack gate on speed knobs corrected it and made v3.
- **The grid of copies and runs** (`results/scale/GRID.md`, 84 of 90 cells on v3): every organism superior within
  guardrails in every cell of ten runs or more; work per energy +0.07% (Physics) to +0.37% (Energy, the four stacked, the
  tower), the same figure at every size; every knob handed back; the six cells left are beyond the machines available.
- **The power grid** (`V1_PANDAPOWER.md`, `V3_PANDAPOWER.md`, the same table to the digit): eleven SimBench grids solved
  by pandapower, the tap changer's own controller as native, one whole tap per move as the knob. With ZIP loads the energy
  the loads drew fell 1.3% to 1.5% and the net import fell in all eleven grids; losses fell in seven and **rose in four**
  (the rural and semi-urban grids with their own generation, +0.6% to +1.5%); tap operations fell in ten grids and rose
  from 4 to 8 a year in one, the declared cost, confirmed worse; no grid was more often outside its voltage band. 67
  gauge-rows better, 14 worse.
- **Robot arms** (`V1_MUJOCO.md`, `V1_MUJOCO_PANDA.md`, `V3_MUJOCO.md`): four arms from the MuJoCo Menagerie with their
  shipped controllers as native and the joint speed of an axis with slack as the knob, after a paired physics trial. The
  trial left the UR5e and the iiwa 14 native ("nothing for Omni to move"); on the Gen3 and the Panda, peak torque fell 29%
  and 10%, tracking error 21%, energy per takt 0.8% and 0.5%, confirmed better; the Panda's copper loss **rose 14%**,
  confirmed worse.
- **Buildings with batteries** (`V1_CITYLEARN.md`, `V3_CITYLEARN.md`): every district CityLearn ships, its own rule-based
  control as native, each building's battery charge and discharge inside the simulator's limits as the knob. In the
  eleven battery districts electricity bought, the daily peak and the daily unevenness fell in all eleven and carbon in
  eight, confirmed better; the bill **rose in seven** (the 2023 districts) and ramping rose in seven, confirmed worse; 71
  score-rows better, 33 worse, 1 where the runs differ by the simulator's own variation; three districts had nothing to
  move and eight the simulator cannot run.
- **Drone swarms** (`V3_SWARM.md`): twenty Crazyflie 2.x quadrotors in gym-pybullet-drones with the shipped position
  controller as native and the cruise override inside the autopilot's limits as the knob, three untouched cells. Energy a
  mission fell 7% (short), 18% (mixed) and 20% (long) and missions a charge rose 8%, 22% and 25%, confirmed better; no late
  mission, reserve breach, near miss or collision in any arm; the tracking error rose from 0.07 to 0.13 m inside its
  0.25 m band, shown; every override handed back. PyBullet reproduced to a part in a thousand across GitHub's machines and
  not to the bit, so the table's reproduction tolerance was set to one part in a thousand after the runs were seen, and
  the preregistration's amendment 1 says so with its time.

### 16.6 The one number, and the table

**The one number.** The Omni index over the real categories confirmed three times: **+23.5%** (real Kubernetes on v3 +25.5%,
the real database on v3 +14.2%, real messaging on v3 +166.9%, the real cache on v3 −24.9%, the real database's
storage-engine cache on v3 +10.2%, the real database's buffer pool on v3 +12.2%, each category weighed the same; Azure and
the card join as their three-run tables land). The fifth category lowered the headline from +30.2% to +25.9% when it joined
on 8 October; the sixth, MySQL's buffer pool, entered the same day at exactly nothing on its first counted set (every row
inside the noise, the headline at +21.2%) and at +12.2% on the second set run the same afternoon on the amended plug, the
headline at +23.5%: a category enters at whatever its table confirms, nothing included, which is the reader's guarantee
that the number is not built from the categories that happened to work. That is how the number is meant to move: every real category enters at equal weight as its table lands, whatever it does to the mean.
The storage-engine cache's figure is positive for the reason the Redis figure is negative, read the other way: there the
governor gave memory back (the cache held halved on two workloads) while work, p95 and CPU stayed inside the noise, so
its resource column is a gain and its other columns are exactly one; its one confirmed loss, the burst mean latency, is
not an index column and stands in its table. The messaging figure is large because its speed ratio is:
native sat at nine tenths of its measured capacity by design, so its queue grew at the high steps and its slowest 5%
waited 1.6 s, while Omni's waited 9 to 14 ms; the resource that bought it, three to four times the consumers, stands
beside it as a confirmed loss. The cache's figure is negative because the memory held is its resource column: the ceiling
rose from 64 MB to 200 to 270 MB (a ratio of about 0.25 in the index's "fewer machines" sense) while work and the hit rate
rose 14% to 27%, and a geometric mean of those four columns is below one. That is the arithmetic of a resource bought,
reported as such; a reader who weighs memory as cheaper than a consumer or a machine will read the cache's rows for
themselves, which is why every row is in its table.

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
| **MySQL under sysbench, the four untouched workloads**, 3 pairs × 3 runs (the second counted set, on the amended plug) | v3 | L | buffer pool held **−67% on burst and −50% to −56% on read_only, confirmed better**; pages holding data on read_write **+53% to +70% confirmed WORSE** (the pool bought for a written working set); work inside the line, p95, p99 and CPU inside the noise everywhere; no error; the pool handed back on 45 of 45 omni arms (the first set, every row inside the noise and 15 arms not handed back through the plug's restore, is kept in `docs/history/V3_SYSBENCH_set1.md`) | `results/live/V3_SYSBENCH.md` |
| **The 945 muscles and six organisms, modelled**, A/B/C | v3 | S | reproduced to the last digit in 3 of 3; 0 muscles worse; **every organism superior within guardrails** (work per energy +0.1% to +0.3%, work unchanged, time over the line not above native's); on v2 Physics and the tower read a service tradeoff, which the slack gate corrected | `results/realms/REALMS.md` |
| **The organisms at 1, 10, 100 and 1,000 copies**, 1 to 1,000 paired runs a cell, 84 of 90 cells | v3 | S | every organism superior within guardrails in every cell of 10 runs or more; work per energy +0.07% to +0.37%, the same figure at every size; the six cells left (100 and 1,000 runs at 1,000 copies) are beyond the machines available | `results/scale/GRID.md`, `results/scale/receipts/` |
| **Power grid: 11 SimBench grids solved by pandapower**, both load models, A/B/C | v1 and v3 (the same table to the digit) | S | with ZIP loads the energy the loads drew confirmed better in all 11 (−1.3% to −1.5%) and the net import in all 11; losses confirmed better in 7 and **worse in 4** (the rural and semi-urban grids with their own generation, +0.6% to +1.5%); tap operations fewer in 10 grids, 4 → 8 a year in one (confirmed worse, the declared cost); no grid more often outside its band | `results/live/V1_PANDAPOWER.md`, `V3_PANDAPOWER.md` |
| **Robot arms, MuJoCo Menagerie**, A/B/C | v1 and v3 | S | where Omni-Compass moved (Gen3, Panda): peak torque −29% and −10%, tracking error −21%, energy per takt −0.8% and −0.5%, confirmed better; the Panda's copper loss +14% **confirmed worse**; UR5e and iiwa 14 left native by the paired physics trial | `results/live/V1_MUJOCO.md`, `V1_MUJOCO_PANDA.md`, `V3_MUJOCO.md` |
| **CityLearn, every district it ships**, A/B/C | v1 and v3 | S | 11 battery districts: electricity bought, daily peak and daily unevenness confirmed better in all 11, carbon in 8; the bill **worse in 7** (the 2023 districts) and ramping worse in 7; 71 score-rows better, 33 worse, 1 where the runs differ (the simulator's own variation); 3 districts with nothing to move; 8 the simulator cannot run | `results/live/V1_CITYLEARN.md`, `V3_CITYLEARN.md` |
| **Drone swarms, gym-pybullet-drones** (Crazyflie 2.x, the shipped autopilot as native; Omni on the cruise override inside the autopilot's limits), 20 drones × 4 missions, three cells, A/B/C | v3 | S | energy a mission −7% (short), −18% (mixed), −20% (long) and missions a charge +8% to +25%, confirmed better; no late mission, reserve breach, near miss or collision in any arm; tracking error 0.07 → 0.13 m inside its 0.25 m band | `results/live/V3_SWARM.md` |
| **Apache Kafka as shipped, a consumer group's operator-set size** (one broker, 8 partitions; the group at the operator's 2 consumers as native; Omni on the count inside [1, 8]), three untouched workloads, 3 pairs × 3 runs | v3 | L | work inside the 500 ms line **+16% to +21% confirmed better** on all three; end-to-end p95 1.6 s → 9 to 14 ms and mean lag −92% to −97% confirmed better; no message lost in any arm; consumers held 2 → 5.8 to 7.9 **confirmed worse** (the resource the gain costs); host CPU-seconds confirmed worse on light (+10% to +20%), inside the noise on heavy and burst; every count handed back; 21 gauge-rows better, 8 worse | `results/live/V3_KAFKA.md` |
| **Redis as shipped, a cache's operator-set memory ceiling** (64 MB, allkeys-lru as native; Omni on the ceiling inside [16, 512] MB through Redis's own console, grown only while the cache is full), three untouched workloads, 3 pairs × 3 runs | v3 | L | work inside the 2 ms line **+14% to +27% confirmed better** on all three; hit rate +14% to +27% and mean latency −30% to −61% confirmed better; no failed request; the memory ceiling held 64 → 200 to 270 MB and the memory used **confirmed worse** (the resource the gain costs); p95 within a hair of native's; host CPU inside the noise; every ceiling handed back; 12 gauge-rows better, 6 worse | `results/live/V3_REDIS.md` |
| **MongoDB as its publisher ships it, a database's operator-set storage-engine cache size** (512 MB as native; Omni on the cache size inside [256, 2,048] MB through the server's own console, grown only while the cache is full and reads are slow), YCSB's workloads b, c, f and burst untouched, 3 pairs × 3 runs | v3 | L | the cache size held **−49% on c, −41% to −49% on burst, −13% to −37% on f, confirmed better**; on b −27% to −50% with one run's interval over zero, no difference beyond the noise; work inside the 1 ms line, p95, p99 and host CPU inside the noise on all four; no failed operation; the mean latency on burst **+2% to +4%, confirmed worse**; pages read into the cache +14% to +58% (shown); every cache handed back; 6 gauge-rows better, 1 worse. "Why is the gain memory and not speed?" Because on this machine the data sits in the operating system's page cache too, so a storage-engine miss costs a memory read, not a disk read, as disclosed before the run; the question the knob would face on a disk-bound store is not answered here. "Is the mean-latency loss hidden?" No: it is a confirmed-worse row in the table and in this manual; it is not an index column, which the index's rules name | `results/live/V3_YCSB.md` |
| **Robustness: the governor killed outright mid-run** (SIGKILL at 40% of the window, the watchdog beside it), 10 pairs × 3 runs | v3 | L | every setting back at the operator's **7 to 11 s after the kill in 30 of 30 repetitions** (allowance 60 s), a second governor to the end in every one, the 120 s after the kill inside the noise against native; the whole window still confirmed better on mean response, p95, time over the line and failed requests | `results/live/V3_ROBUST_KILL.md` |
| **The governor's own cost** at 1, 10, 100 and 1,000 copies with the real cluster inside | v3 and v1, each under its own engine | L | 0.006 to 0.013 of one core at every size, 0.1% to 0.3% of the host's cores; shown, not judged | `results/live/V3_OWN_COST.md` |
| **Scale**: the controller governing 50, 500 and 1,000 simulated nodes (KWOK), decision time and correctness | every push | L | runs on every push | `results/scale/` |
| GPU, one card and the card inside the organisms | earlier card controller | P | **obsolete**: every earlier card result ran on a controller since replaced; the one-card, card-inside-1,000-copies and eight-card runs are run again by the founder on rented cards after the CPU and cloud work, at one named commit | `docs/GPU_PREREGISTRATION.md`, `docs/GPU_RUN_GUIDE.md` |

**Running now** (8 October): the whole tower at 1,000 copies on a rented machine (the four stacked at 1,000 copies done,
section 16.2); MySQL's buffer pool under sysbench done, two counted sets (`V3_SYSBENCH.md`, section 16.4; the first set and the plug's amendment in section 10.9); the robustness test
(`docs/ROBUSTNESS_PREREGISTRATION.md`), the kill scenario and the two-hour long run both done (section 16.4b), the
24-hour run on three rented machines under way (one pair a machine, two arms of a day each, collected on 10 October);
the real cluster under a public demand trace (the Google cluster trace of 2011, `docs/TRACES_PREREGISTRATION.md`), A, B
and C dispatched on the day's derived schedule;
YCSB on MongoDB done (`V3_YCSB.md`, section 16.4), MySQL's buffer pool under sysbench done (`V3_SYSBENCH.md`, section 16.4),
the other stores of register row 24 after; and Azure steady and burst on the fleet of several machine families (seven
dispatches refused by Azure's own cluster capacity in eastus or held by our own machines' quota, 34 refusals, amendments 5
to 8; the eighth dispatch follows the 24-hour machines' collect). **Queued, in order, in `docs/REGISTER.md` section 4**: drone swarms and
defense edge (PX4 and ArduPilot multi-vehicle, Crazyswarm), databases and caches at large (YCSB, HammerDB), Spark,
OpenSearch, fio, Open-RMF, the 24-hour robustness run, spacecraft attitude and thrusters (Basilisk),
station-keeping (Orekit, GMAT), constellations, rockets (RocketPy, OpenRocket) and combustion (Cantera). Pure physics
solvers (OpenFOAM, SU2, REBOUND, GADGET, MESA) are not benchmarked: they have no controller and no knob, so Omni-Compass
has no place on them; their value is the HPC cluster that runs them.

### 16.7 Threats to validity, stated by us

A referee will look for the ways these results could mislead. We list the ones we know, what each would do to the
numbers, and what the record does about it.

1. **The machines are shared.** Every Kubernetes, database, broker and cache run is on one GitHub runner with four cores,
   and the governor, the load generator, the probe and the system under test share it. A governor that costs CPU can slow
   the service it governs, and a noisy neighbour on the host can move a run. The pairing on one runner with rotated order
   removes the between-machine noise; the host's own busy share is recorded beside every run; the governor's own CPU is a
   gauge in every table and a confirmed loss where it is one (the database, Kafka's light workload); and three separate
   runs on separate machines must agree before anything is confirmed.
2. **kind is not a cloud.** Idle machines stay powered and native has no node autoscaler, so a machine given back on kind
   is a machine-hour in service, not a watt and not a dollar. The energy rows on kind are a declared model and say so on
   every line. The bill is Azure's test, and its only result so far is inside the noise on a fleet too small to show one
   machine.
3. **Native is at its knee by design in the broker test.** The Kafka producer's peak offers nine tenths of the capacity
   measured for the operator's two consumers, so native's queue grows at the high steps and omni's does not. This is the
   situation the benchmark is of (a group sized for the quiet hours and overrun at the peak), it is preregistered, and it
   is why the latency ratios are large; the index page and the table say so. A native group sized for the peak would show
   a smaller latency gain and a smaller consumer cost, and would be a different, also legitimate, benchmark.
4. **Declared penalties.** The cache's 5 ms store trip on a miss and the broker's 1, 2 or 5 ms of CPU per message are
   declared parameters of our own application, not measurements of anyone's store. The gauges that depend on them (work
   inside the line, the request latency) scale with them; the hit rate, the lag, the consumers and the memory held do not.
5. **Simulators are models.** Every S result is a statement about a published model under its own controller. A model may
   flatter or punish the governor in ways the real plant would not. S results are therefore shown beside the index and
   never inside it, and the muscles' models are the simplest physics that reproduces the meter's response to the knob,
   with the native controllers tuned as their authors ship them.
6. **The tuning case was seen.** Every benchmark's rules were set on one tuning case, and that case is shown and not
   counted. Where a rule changed after a counted result was seen (the swarm table's reproduction tolerance), the amendment
   is written in the preregistration with its time and reason, the table says so, and the runs were not rerun.
7. **The engine changed twice.** v1 to v2 added muscles without touching the law; v2 to v3 added one gate. Every result is
   labelled with its engine, the tools refuse to mix engines, and the v1 results stay as v1 results. A reader comparing a v1
   number with a v3 number is comparing two engines, and the manual never does so except to say that the controllers were
   the same bytes and the readings the same.
8. **Three runs are three, not thirty.** The three-run rule is a replication standard, not a large sample. A row confirmed
   in three runs of ten pairs is a row whose paired difference cleared zero in each of three independent samples of ten;
   the intervals are shown so a reader can judge their width. Where the intervals are wide, the manual says the test lacked
   power rather than calling the result a null.
9. **The founder's own harness.** The application in front of the cache, the producer in front of the broker, the load
   generator and the probe are ours. They are declared, versioned, archived with every run and reproducible from the
   repository; they are not independent of us. The independent pieces are the systems under test, their native
   controllers, the simulators and their shipped controllers, and the benchmark tools (pgbench, kind, Kubernetes,
   PyBullet, MuJoCo, pandapower, CityLearn) that others wrote. The load schedules of the Kubernetes tests were ours too,
   written one step at a time; the public-trace test (`docs/TRACES_PREREGISTRATION.md`) answers that by replaying a day
   of demand somebody else measured (the Google cluster trace of 2011, then the Azure Functions trace) under the wandering
   test's own rules, the derivation receipted and committed before the runs.

### 16.8 What is not yet shown, and the open program

Three things this manual does not show, and the program that will show them or show their absence:

- **An energy or bill saving on real machines.** The fleet of 40 workers in nine Azure machine families that can show one
  machine is preregistered and dispatched on v3; it runs when Azure's region admits a cluster. If the saving is a few
  percent, a 40-worker fleet can see it; if the saving is not there, the table will say "no difference beyond the noise"
  on a fleet that could have seen it, and that will be the result.
- **The real card.** Every earlier GPU result ran on a controller since replaced. The two-wire governor with the verdict
  runs on rented cards at one named commit, with the wire check first (`docs/GPU_RUN_GUIDE.md`,
  `docs/GPU_PREREGISTRATION.md`); until then the card has no result and the manual says so.
- **Robustness over a day.** The governor killed outright is a measured result (section 16.4b: every setting back in 7 to
  11 s, thirty times out of thirty), its own cost is tabulated, and the two-hour run is measured three times (no leak,
  no slowing, every decision expected but a few the cluster's API refused, every setting handed back); the 24-hour run,
  one pair on each of three rented eight-core machines of three families, is under way (`docs/ROBUSTNESS_PREREGISTRATION.md`,
  scenario 2b) and is read when its machines are collected; the same test on the other stacks remains open.
- **A demand shape that is not ours.** Every Kubernetes result so far was driven by a load schedule we wrote. The
  public-trace test (`docs/TRACES_PREREGISTRATION.md`) replays a day of the Google cluster trace of 2011 under the
  wandering test's own rules, three runs of ten pairs, dispatched on 8 October; the Azure Functions trace follows by the
  same rule. Until its table lands, the "our own schedules" threat of section 16.7 stands unanswered, and the manual says so.

The queue beyond these, in order, is `docs/REGISTER.md` section 4, one or two at a time, each preregistered before it
runs: PX4 and ArduPilot swarms, YCSB and HammerDB, Spark, OpenSearch, fio, Open-RMF, Basilisk, Orekit and GMAT, RocketPy
and OpenRocket, Cantera. When the founder declares the engine final, the engine that stands then is
published as Omni-Compass 1.0, and the older fingerprints go to `docs/history` as the road to it.

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

**Why two languages.** A law that exists in one implementation can hide a bug that is also its behaviour: the tests pass
because the tests were written against the same code. Two implementations written separately, in languages with
different numerics and different defaults, that agree to fifteen decimal places on five hundred trajectories and on every
fixture of the governor, the shield, the HPA law, the closure, the conveyance and the nervous system, are evidence that the
text of the law is what both compute. The C++ twin is also the one a buyer would embed where Python does not run (a
controller, a firmware, a PLC), and the soak (`results/SOAK.json`, one hundred million decisions, no failure) is run on
it. The seal makes the twins' agreement a property of the repository rather than a claim: change a sealed byte and
`verify.py` fails, naming the file.

**The three fingerprints.** The seal fingerprints the twinned laws; `OMNI_V1.json`, `OMNI_V2.json` and `OMNI_V3.json`
fingerprint the engine as a whole (law, controllers, muscles, runners: 38 to 40 files); `RELEASE_MANIFEST.json`
fingerprints the release (the commit, the engine, the twins, the GPU protocol, the live evidence and the verification
receipt) and is rewritten by `tools/release_manifest.py` before every push, under the Python GitHub runs. A reader holding
any one of the three can tell whether the files in front of them are the files the results were made on.

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
| Work inside the line | the requests, transactions or messages a second answered within the response line; the product number on every real stack |
| Pedals | idle, gas, brake and reset: the governor's four ways of moving capacity under autopilot |
| Cruise | every machine in service while work waits for a place, held without second-guessing until the line has been empty for two decisions |
| Emergency brake | the work done and demand at zero: straight to the floor in one move, every safety check still holding |
| Kill switch | security only: one switch in a human hand that turns every governor on the machine off at once; never the reset |
| Lease | the record every governor renews each decision; a lease older than its limit, or a dead process, makes the watchdog hand back for it |
| Watchdog | the service beside the governors that hands back for any governor that died or hung without doing it itself |
| Verdict | the paired trial on the muscle itself that allows a slow knob to move only where the cost is within 2%; "left native" where no step passes |
| Slack gate | v3's rule: a motion axis busy more than half the time at full speed keeps its speed native |
| Tuning case | the one workload, cell or swarm the rules were fitted on; shown in every table and never counted |
| Untouched case | a workload, cell or swarm the rules were applied to unchanged; the judged rows |
| Knee | nine tenths of a system's measured capacity, where its queue begins to grow; the broker's native was set there by design |
| Amendment | a change to a preregistration after it was written, with its time and reason; one made after a result was seen says so |
| Dwell | the seconds after a knob moves during which the law will not move it back |
| Notch | the smallest step a knob moves in one decision (one consumer, 8 MB of cache, one tap) |
| Evidence class P, L, S | a physical meter; live software with no meter; a model of ours |
| Handed back | the knob read back at the operator's value at the end of an arm; every table says whether every arm was |
| Off the clock | see above; a repetition whose arm ended more than 5% of its window late |
| Own cost | the governor's CPU (its process and every command it ran) as a share of one core over the window, from its audit; a few thousandths of a core at every size |
| Smoke run | one repetition that exercises a harness end to end before any counted run; never counted, always recorded |
| L + S | an organism run with a real cluster inside: the cluster is L, the organism around it S |
| Working set | the records a workload actually touches over a window; a cache benchmark measures nothing unless the working set reaches the cache |
| Key space | the records a benchmark may ask for at one notch; in the MongoDB test the knob's load, stepped one notch at a time |
| Uniform draw | every record in the key space equally likely, so the working set is the key space; YCSB's shipped zipfian draw concentrates on a few thousand hot records whatever the key space |
| Ordered keys | records named in load order, so a run that asks for record n finds record n; a run with hashed keys against an ordered load asks for records that do not exist |
| Full-cache gate | the MongoDB and Redis rule: slow reads grow the cache only while the cache is full (nine tenths used), because a miss in a cache with room to spare is not the cache's to mend |
| Buffer pool | InnoDB's cache of table and index pages, the one memory setting every MySQL operator sizes; resized online by the server in whole chunks |
| Chunk | the unit in which MySQL resizes its buffer pool (128 MB as shipped); the knob's notch on that stack |
| Page cache | the operating system's own cache of file contents; where the data fits in it, a storage-engine miss is a read from memory and a decompression, not a disk read, and the gain available to the cache knob is smaller |

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
| The three-run table (database, messaging, cache, swarms, robots, grid, buildings) | `tools/pgbench_abc.py`, `tools/kafka_abc.py`, `tools/redis_abc.py`, `tools/swarm_abc.py`, `tools/mujoco_abc.py`, `tools/pandapower_abc.py`, `tools/citylearn_abc.py`, the same arguments |
| The six organisms with the cluster inside | `python3 tools/six_kube_report.py <raw dirs> --out results/live/V3_SIX_KUBE.md` |
| The grid of copies and runs | `python3 tools/grid.py` (reads `results/scale/receipts/`) |
| The Omni index | `python3 tools/omni_index.py` |
| The database benchmark, one run | `python3 tools/run_pgbench.py --out <dir>` (workflow `pgbench`) |
| The message broker, one run | `python3 tools/run_kafka.py --setup`, then `--workloads light,heavy,burst --out <dir>` (workflow `kafka`) |
| The cache, one run | `python3 tools/run_redis.py --setup`, then `--workloads small,large,burst --out <dir>` (workflow `redis`) |
| The database's storage-engine cache under YCSB, one run | `python3 tools/run_ycsb.py --setup`, then `--workloads b,c,f,burst --out <dir>` (workflow `ycsb`) |
| The database's buffer pool under sysbench, one run | `python3 tools/run_sysbench.py --setup`, then `--workloads read_only,read_write,update_index,burst --out <dir>` (workflow `sysbench`) |
| The robustness test | workflow `robustness`: `scenario` kill or long, `reps`, `duration_s`; the own-cost table `python3 tools/own_cost.py <raw run dirs> --out results/live/V3_OWN_COST.md` |
| The drone swarms, one cell | `python3 tools/run_swarm.py --cell short|mixed|long|all --out <dir>` (workflow `swarm`) |
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
| `.github/workflows/` | every benchmark as GitHub runs it: `benchmark-reps`, `six`, `six-kube`, `big-organism`, `big-organism-detached`, `aks-metered`, `pgbench`, `kafka`, `redis`, `ycsb`, `sysbench`, `robustness`, `swarm`, `citylearn`, `pandapower`, `mujoco`, `archive-run`, `verify` |
| `tests/`, `verify.py` | every unit and property test, the shield's adversarial cases, the Python-against-C++ agreement; `verify.py` runs them all and must end with its pass line |
| `tools/omni_version.py`, `tools/release_manifest.py`, `tools/layout_check.py` | which engine a checkout or commit carries; the release manifest and verification as GitHub runs it; the check that every path the documents name exists |
| `tools/confirm_abc.py` and its siblings (`pgbench_abc.py`, `kafka_abc.py`, `redis_abc.py`, `ycsb_abc.py`, `sysbench_abc.py`, `swarm_abc.py`, `mujoco_abc.py`, `pandapower_abc.py`, `citylearn_abc.py`) | the three-run tables, one tool per kind of raw record, each checking the engine of every run it reads |
| `tools/omni_index.py`, `tools/dossier.py`, `tools/own_cost.py` | the one number from the tables; the dossier from the tables; the governor's own cost from the archived audits |
| `tools/legal.py` | the legal notice every generated report carries at its head and foot |
| `docs/book/` | the builder of this manual's PDF (`build_book.py`) and the theory chapters bound into it |
| `release/` | the copyright deposit and the release notes, printed at named commits |
| `CHANGELOG.md`, `docs/STATE_OF_PLAY.md` | what changed, by date; where everything stands today |
| `docs/*_PREREGISTRATION.md` | the rules of every benchmark, written before it ran, with every amendment and its time |
| `docs/DOSSIER.md`, `docs/dossier/` | every result in one place, with its charts, built by `tools/dossier.py` from the tables |
| `docs/HISTORY.md`, `docs/history/` | earlier states of play, earlier engines' sets and the pre-v1 index, kept whole |
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

Every gauge, where it comes from, and whether it is measured or modelled: `docs/METRICS_CATALOG.md`. The gauges that
appear in the three-run tables of this manual, with their source and their direction, are these:

| Gauge | Source | Measured or modelled | Direction |
|---|---|---|---|
| work inside the response line (requests, transactions or messages a second answered within the line) | the probe's own records, pgbench's log, the consumers' records, the application's records | measured | higher is better; the product number |
| response time, mean, median, 95th and 99th percentile | the same | measured | lower is better |
| time over the response line (share of samples) | the same, against the preregistered line | measured | lower is better |
| failed requests, lost messages | the same | measured | any increase is WORSE |
| worker machines in service, mean; node-hours | the cluster's own node records every 15 s | measured (machine-hours on kind; Azure's own count on AKS) | lower is better |
| compute bill at list price | Azure's own machine count × list price per family | measured (a real bill) | lower is better |
| energy (Wh), the standby model | a declared formula over the machines in service (kind) | **modelled**, said so on every line | lower is better |
| host CPU busy; host CPU-seconds; CPU-seconds per 1,000 units inside the line | `/proc/stat` of the real machine under the test | measured | lower is better |
| Omni's own CPU (cores), mean | the governor's audit (its process and every command it ran) | measured | shown, not judged in the Kubernetes tables; a confirmed loss where it is one |
| connections held open, consumers running, memory ceiling held | the pooler's, the group's, the cache's own reports | measured | lower is better (the resource held) |
| cache hit rate; consumer lag | Redis's INFO; the consumers' records | measured | higher is better; lower is better |
| HPA replicas, pods started, pod start wait | the API server's own records | measured | shown, not judged except pod start wait |
| organism work, energy, time over its line | the organism's plant models | **modelled** | by direction; S class |
| energy a mission, missions a charge (drones) | the simulator's motor constants through a declared model | **modelled** | lower; higher |
| cache size held, mean; bytes in the cache, mean; pages read into the cache (MongoDB) | the server's own `serverStatus` (WiredTiger cache) | measured | lower is better (the resource held); shown, not judged (pages read) |
| seconds from the kill to every setting back at the operator's (robustness) | the harness polling the cluster once a second from the kill | measured | lower is better; past 60 s WORSE; never, INVALID |
| the governor's resident memory, last ten minutes over the first ten (robustness, long run) | the process table, sampled every 15 s by the harness | measured | a growth over a quarter is WORSE |
| decisions made of expected; failed decisions (robustness, long run) | the governor's audit | measured | under 95% INVALID; any failed decision shown with its reason |
| mission time, position error, collisions (drones) | the simulator's own state at every step | measured in the simulator (S class) | lower; under the safe error; any collision voids the cell |
| handed back (every arm) | the knob read back at the end of the arm | measured | yes in every arm, or the run is invalid |
| off the clock | the organism's own clock against its window | measured | shown; marks the cell |

**Three rules for reading any gauge in this appendix.** A measured gauge is one the system under test, or the host's own
kernel, reported about itself; a modelled gauge is one computed from a declared formula over measured inputs, and every
table says which it is on the line itself, never only here. A resource gauge (machines, connections, consumers, memory,
cache) is always judged lower-is-better, even where the governor's purpose was to add the resource to buy service, so that
a gain bought with a resource is paid for in the same table and in the index. And a gauge marked "shown, not judged"
never enters a reading or the index; it is there so that a reader can see what the governor did (how often it moved, how
many pages it read, how many pods it started), not to be counted for or against it.

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
| Kubernetes: a repetition marked OFF THE CLOCK | the machine could not step the organism inside its window | a longer window for that size on that machine; never a faster reading of the same run |
| Broker: consumers climb to the cover and stay | messages wait at every step (the producer is past the group's capacity) | the benchmark's capacity step sets the peak at nine tenths of the operator's group; check the measured capacity in the run's log |
| Cache: the ceiling grows while little memory is used | cold misses read as pressure | the full-cache gate is the rule (used ≥ 90% of the ceiling); check `used_mb` beside `maxmemory_mb` in the run's log |
| Cache: the ceiling never grows | the working set fits the operator's ceiling | expected: a cache that fits has nothing for the ceiling to mend, and the row reads inside the noise |
| Storage-engine cache: the cache never fills, whatever the key space, and omni reads as a free memory saving | the benchmark's requests concentrate on a few hot records (YCSB's shipped zipfian draw), or the run asks for records the load did not write (hashed keys over an ordered load), so the reads are served from the index | a result that flatters the governor is the first thing to suspect: check "in cache" against the cache size in the per-notch lines; draw requests uniformly over the key space and name the same key order in load and run; a knob with nothing to do is not a saving |
| Storage-engine cache: the compass only ever reads calm | the line is set far above the stack's own latencies (a 2 ms line over 0.15 to 0.45 ms reads) | set the line on the tuning workload's own figures so that a hit is calm and a full-cache miss is slow, and write the figures in the preregistration before any counted run |
| Swarm: a cell reads "void" | two drones came within two collision radii in either arm | a task or simulator setting (keep-out, altitude stagger, depot spacing); fixed before any counted run and said in the preregistration |
| Three-run table heads itself with a warning | a run's commit is not the engine it claims, or the three are not separate runs | run `tools/omni_version.py --commit <sha>` on each; make the table only from runs on one frozen engine |
| Archive bot skips a run | the run was not finished when the bot passed | leave the id in `.github/archive_request.txt`; the next pass copies it |

## Appendix F - Evidence Map

`docs/EVIDENCE_LEDGER.md` (every claim and its class), `docs/CLAIMS_REGISTER.md` (what is claimed and what is not),
`docs/GPU_PREREGISTRATION.md`, `docs/REALMS_PREREGISTRATION.md`, `docs/K8S_COMPASS_PREREGISTRATION.md`,
`docs/POSTGRES_PREREGISTRATION.md`, `docs/KAFKA_PREREGISTRATION.md`, `docs/REDIS_PREREGISTRATION.md`,
`docs/SWARM_PREREGISTRATION.md`, `docs/CITYLEARN_PREREGISTRATION.md`, `docs/PANDAPOWER_PREREGISTRATION.md`,
`docs/ROBOTICS_PREREGISTRATION.md`, `docs/ROBUSTNESS_PREREGISTRATION.md`, `docs/YCSB_PREREGISTRATION.md` and
`docs/MYSQL_PREREGISTRATION.md` (the rules written before each run), `docs/OMNI_V1.md` to `OMNI_V3.md` (every result by engine), `docs/REGISTER.md` (every benchmark
and its file), `docs/PROOF_PROGRAM.md` (the program to full size with its costs), `docs/DOSSIER.md` (every result in one
place), `results/OMNI_INDEX.md` (the one number), `docs/STATE_OF_PLAY.md` (where everything stands), `docs/HANDOFF.md`
(every command in one page).

**The map, claim by claim.** Each claim this manual makes is listed here with the class of evidence behind it and the
document that carries it, so that a reader can go from any sentence of the executive summary to the file that would have
to be wrong for the sentence to be wrong.

| Claim | Class | Where the evidence is | What would falsify it |
|---|---|---|---|
| The engine's six states stay inside their walls and settle | T / V (proof and test) | `docs/FORMAL_STATUS.md`, `docs/TRACKING_THEOREM.md`, `tests/`, `results/SOAK.json` | a trajectory leaving its wall, or the C++ twin disagreeing with the Python |
| No write ever leaves a knob's cover; a blind sense holds; fail-up is immediate | T / V | `tests/test_shield_properties.py` (two million cases), the plug tests per stack | one case of a write past the cover or a give-back while blind |
| On a real cluster the governor does more work inside the line, faster, on no more machines, at no more energy | L | the six Kubernetes tables in `results/live/`, A/B/C each, `docs/K8S_COMPASS_PREREGISTRATION.md` | a confirmed-worse row on work, speed, machines or energy in any of the six, which would stand in the table |
| Killed outright, the governor's settings are back at the operator's within seconds | L | `results/live/V3_ROBUST_KILL.md`, `docs/ROBUSTNESS_PREREGISTRATION.md` | a repetition handed back after 60 s, or not at all |
| Over two hours the governor neither leaks, slows nor drifts, and hands everything back at the end | L | `results/live/V3_ROBUST_LONG.md`, `docs/ROBUSTNESS_PREREGISTRATION.md` | memory growing past a quarter, the decision time growing past a half, fewer than 95% of expected decisions, or a setting not handed back |
| Governing costs a few thousandths of a core at every size | L | `results/live/V3_OWN_COST.md` | an own-cost figure growing with the organism |
| The pooler, the broker and the cache each gain on their untouched workloads | L | `V3_PGBENCH.md`, `V3_KAFKA.md`, `V3_REDIS.md`, each preregistration | a confirmed-worse product row on an untouched workload; the memory row of the cache is such a loss and stands |
| The one number is +23.5% across the real categories, losses included | L, by rule | `results/OMNI_INDEX.md`, `tools/omni_index.py` | a category omitted, a loss not entered, a tuning row counted |
| The modelled realms, grids, arms, buildings and swarms gain under their own native controllers | S | `results/realms/`, `V3_PANDAPOWER.md`, `V3_MUJOCO.md`, `V3_CITYLEARN.md`, `V3_SWARM.md` | a run of the same simulator at the same version and seed giving other digits |
| A physical meter shows less energy for the same work | P | **no current result**; `docs/GPU_PREREGISTRATION.md` names the run | the rerun on the current card controller reading no difference or worse |
| Omni-Compass never changes the engine between a rule and its result | by construction | `OMNI_V3.json`, `tools/omni_version.py --commit <sha>` on every table's commits | a table whose runs' commits carry different fingerprints |

**What a referee asks of each document.** Of a preregistration: is it dated before the first counted run, does it name the
tuning case and the untouched cases, is every amendment dated and does any amendment made after a result was seen say so?
Of a three-run table: are the three run ids separate runs, does the head name the engine at each commit, is every gauge
of the preregistration present including the ones that went against the governor, and is the reading one of the three the
rule allows? Of the index: is every real category in it, is every tuning row out of it, and does a confirmed loss enter
as a loss? Of the raw folder: does the SHA-256 manifest in it match the files, does the governor's audit show every
decision with its reading and its write, and does the hand-back record read the operator's value? Every one of those
questions has a yes in this program or a disclosure naming the exception; the disclosures are in section 16.7.

**How to audit one result from this manual to its raw files.** Take any row of section 16. Its source column names a
three-run table in `results/live/`; the table's head names the three GitHub run ids, the commit each ran on and the engine
`tools/omni_version.py` reads at that commit. Each run id names a folder `results/live/raw/run-<id>/` holding every
repetition's files (the capture, the response times, the governor's audit and log, the per-request records, one SHA-256
manifest per repetition). The table tool named in the table's text (`tools/confirm_abc.py` or its siblings) rebuilds the
table from those folders; `tools/omni_index.py` rebuilds the index from the tables; `tools/dossier.py` rebuilds the
dossier. The preregistration named in the table's text holds the rules, written before the first counted run, with every
amendment dated. Nothing in that chain is by hand.

**What one repetition leaves behind.** Take the first repetition of the first kill-scenario run, archived at
`results/live/raw/run-37716845219/paired-1/`. It holds two folders, one per arm, and the omni arm's folder holds
twenty-nine files, every one of which a reader can open: `preflight.txt` (the UTC time, the arm, the git commit the arm
ran at, the versions of Docker, kind, kubectl, the API server and Python, the metrics-server version with its SHA-256,
the worker count and the probe's address); `rbac_omni.txt` (twenty lines of `kubectl auth can-i`, each verb the governor
needs reading yes and each it must not have reading no); `window_start.txt` and `window_end.txt` (the window's clock);
`load_schedule.log` (every load step and when it was applied); `latency.csv` (the probe's response times, one row a
second); `capture.csv` (the cluster's state every fifteen seconds: replicas, workers, pods pending, the HPA's target);
`host_cpu.csv` (the runner's own `/proc/stat`); `pod_watch.json` and `pods_end.json`, `nodes_end.txt`, `hpa_end.json`
(the API server's own records at the end); `audit.jsonl` (one line per decision: the compass's position, heading and
letter, the engine's state, every write with its value sent and its value read back); `controller.log` and
`controller2.log` (the first governor's log, and the second one's after the kill); `audit_kill.jsonl` (the watchdog's
restore writes, each with its command and its reason, such as "reset: remove record"); `watchdog.log` (one record: which
governor, its process id, whether it was hung or dead, every command run and each exit code); `robust.log` (the kill at
the 360th second with the settings as they stood, "target=50 range=1,10 limits=1850m 3700m workers=5/6", and the
hand-back "every setting at the operator's after 8 s, target=50 limits=500m workers=6/6 left=none"); `rss.csv` (the
governor's resident memory every fifteen seconds); `omni_writes.txt` (how many writes the governor made in the window:
42); `kill_switch.txt` (the reset check: target restored, workers in service, no record left); `omni2.pid` (the second
governor's process id) and `kill` (the marker the harness wrote at the kill); `robust.out` (the same robustness log as the
job printed it); `end_reads.err`, `pod_watch.err` and `capture.csv.errors` (empty, as they should be);
`metrics-server-components.yaml` (the pinned manifest as applied); and `SHA256SUMS.txt`, one line per file. A reader who doubts a number in the kill table can find the second it was taken.

## Appendix G - Reproducing Everything, From a Clean Machine

A referee with a laptop and a GitHub account can rebuild every table in this manual and rerun every benchmark. The steps,
in order, with what each costs:

1. **Get the code and prove it is the code.** `git clone` the repository, `pip install -r requirements.txt` under Python
   3.12 (the version GitHub runs), then `python3 verify.py`: it checks every sealed file's fingerprint, runs every test in
   `tests/`, including the rules of every three-run table on fixed cases, and ends `VERIFICATION: PASS`. About ten
   minutes on a laptop. `python3 tools/omni_version.py` then says which frozen engine the checkout carries.
2. **Rebuild any table from its raw files.** Every three-run table names its three run ids; their files are in
   `results/live/raw/run-<id>/`. `python3 tools/confirm_abc.py "<title>" results/live/raw/run-<A> results/live/raw/run-<B>
   results/live/raw/run-<C> --out /tmp/check.md` rebuilds a Kubernetes or Azure table; `tools/pgbench_abc.py`,
   `kafka_abc.py`, `redis_abc.py`, `ycsb_abc.py`, `swarm_abc.py`, `mujoco_abc.py`, `pandapower_abc.py` and `citylearn_abc.py`
   the others, with the same arguments. Compare the result with the committed table: they are the same bytes below the legal notice. A
   few seconds each.
3. **Rebuild the index and the dossier.** `python3 tools/omni_index.py` reads every `V1_*.json` and `V3_*.json` table and
   writes `results/OMNI_INDEX.md`; `python3 tools/dossier.py` writes `docs/DOSSIER.md` and its charts. Seconds.
4. **Rerun a benchmark.** Every benchmark is a GitHub Actions workflow with its inputs documented at its head
   (`.github/workflows/`): `benchmark-reps` for the Kubernetes tests (`duration_s`, `arms`, `loadgen`, `load_steps`,
   `faults`, `workload`), `pgbench`, `kafka`, `redis`, `ycsb`, `swarm`, `robustness`, `citylearn`, `pandapower`, `mujoco`,
   `six`, `six-kube`. Dispatch it three times for A, B and C; each run archives its files when its id is added to
   `.github/archive_request.txt`. The Kubernetes tests run on GitHub's free runners in about an hour each; the database,
   broker, cache and swarm runs in about half an hour; the organisms at 1,000 copies need a rented machine (`aks-metered`
   and `big-organism-detached` need an Azure subscription and its credentials in the repository's secrets).
5. **Run it on your own system.** Section 13 is the method; `scripts/kind_paired.sh` and `tools/live_reps.py` are the
   tools; the preregistrations are the templates for writing your own rules down before you run.
6. **Check a result against its preregistration.** Each `docs/*_PREREGISTRATION.md` was committed before its first
   counted run; `git log` on the file shows when, and every amendment carries its own date and reason in the text.

Nothing in this chain requires a credential, a licence key or a word from us; the evaluation licence covers all of it.

## Contact

Licensing, pilots and the Omni-Compass Enterprise License: **The Omni-Compass LLC.**

*Copyright (c) 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only.*

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
