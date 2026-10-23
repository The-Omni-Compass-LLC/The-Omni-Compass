# Omni-Compass's own orchestrator: the organism run without Kubernetes

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 23 October 2026: "I want to build my own components ... the whole orchestration in Omni Compass would
only be to replace ... Kubernetes, and whatever orchestration ... Go ahead and build such a thing." This page is what was built
that day and what its first showing read. It is a first showing on one host, class L (live software, every piece a real
process), one run of each arm: it shows that the mechanism works end to end and how it behaved here, not yet a three-run
reading. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## 1. What it is

`omni_orchestrator/` is written from scratch on Python's standard library and Omni-Compass's own compass law
(`omnicompass/compass_law.py`). No code of Kubernetes, Docker Swarm, Nomad, Slurm or any other orchestrator is in it; the
only outside mechanism it uses is the Linux kernel's own, which stays native under it (its control groups wall the
processor and memory, its scheduler shares each core). What Kubernetes' published autoscaling rule says is written here, by
us, from its documentation, as the yardstick Omni is read against; that is a description of a rule, not Kubernetes' code.

| piece | file | what it does |
|---|---|---|
| the walls | `cgroup.py` | a machine's and a unit's CPU quota and memory limit through the kernel's control groups (`omni/<machine>/<unit>`); the processor each one used, read from the kernel's own counter |
| the machine's hand | `agent.py` | one process per machine, the only thing that starts or stops a unit on it: starts each unit inside its own walls on the machine's cores, probes a service on its health path twice a second (ready at its first answer; killed and started again after three missed answers), starts a crashed unit again after a wait that doubles from 1 to 30 s, marks a batch task done at exit 0 or failed after three tries; the units keep running whatever happens to the control plane |
| the front | `front.py` | one address for a service, its own process: every request joins one line, each ready unit has one hand that takes the next request and waits for its answer (one request at a time a unit, the waiting measured here), a unit that fails to answer sends the request back to the head of the line for another unit (three tries); the response time it measures is the brain's sense |
| the room rule | `scheduler.py` | a unit goes only where its request fits on a machine awake; **pack** (Omni): the machine left fullest, but a service of two or more units never on one machine alone; **spread** (the yardstick): the machine with the fewest units of the service, then the most room, as Kubernetes' scheduler scores by default |
| the brain | `brain.py` | **Omni:** the compass law on the service's 95th percentile response time in the band from 0 to its line; a force up adds units at once in proportion (past the wall, the most it may), a force down gives back one unit after it has held down for three beats with nothing waiting; it never holds fewer units than its native twin, the yardstick's rule computed on the same readings. **Yardstick:** every 15 s, units = ⌈units × busy ÷ 50%⌉, no move inside 10%, a rise to at most max(2 × units, units + 4), a fall only to the highest count of the last 300 s. **Machines:** the units' requests plus room for the next step, never fewer than two |
| the control plane | `control.py` | the ledger of what is wanted and what was placed, every change a line in a journal before it is acted on, replayed when the control plane starts again (the units it finds running are taken back as they are, none started again); every second: every hand polled (a machine silent three times is down and its units placed again), retiring units stopped once drained, the brain on its beat, the room rule for every unit the ledger lacks, batch tasks into the room the service leaves (a task yields its room the moment a service needs it), the routes for the front (only ready units), one timeline line; the kill switch is a file: the brain off, the declared state held; every decision one audit line with its reason |
| the workload | `workload.py` | a service whose every answer is checked (a chain of SHA-256 hashes from the request's seed; the digest is fixed by the seed, so the client knows whether the answer is right) and a batch task of the same kind |
| the clients | `load.py` | closed-loop clients stepping by one (1 2 3 2 3 4 …): each sends its next request when the last is answered and it has thought 0.1 s, so a slower answer brings fewer requests, as programs and people do; every answer checked against its known digest |

`tools/orchestrator_show.py` runs the whole showing on one host and writes `report.html` from its files;
`tests/test_orchestrator.py` holds the rules (the room rule, the yardstick's arithmetic, the twin floor, the ledger's replay).

## 2. The first showing, 23 October (quick form: six steps of 15 s)

The rig: six machines of half a processor each (the kernel's CPU quotas, two machines on each of three cores); the control
plane, the front, the six hands and the clients on the fourth core. Units of 250 millicores (request and limit); a request
about 40 ms of processor. Both arms took the same clients, 1 2 3 2 3 4, 15 s a step. Every number is from the showing's own
files (each request's record, the control plane's timeline and audit, the kernel's processor counters).

| gauge | yardstick | Omni | Omni against it |
|---|---:|---:|---:|
| requests answered (work) | 1,174 | 1,044 | −11.1% |
| requests failed | 0 | 0 | — |
| answers wrong | 0 | 0 | — |
| response time, 50th percentile (ms) | 89 | 110 | +23% |
| response time, 95th percentile (ms) | 165 | 213 | +29% |
| machine-minutes on (the bill) | 9.0 | 6.6 | −27% |
| processor-seconds used by the units | 52.8 | 50.2 | −5% |

Read by the one key, step by step (six pairs): requests answered −11.1% **LOSS**; the 95th percentile +23.8% **LOSS**;
machines on −26.5% **GAIN (a cut)**. The units Omni held were the yardstick's own at every beat (2 → 3 → 4 → 6 → 7, each
equal to the native twin, the compass force negative throughout because the 95th percentile sat far under the 800 ms line);
no unit ever waited for room. What differed is where they stood: Omni packed them, four units of 250 m on the two machines
of one core, and parked the two empty machines; the yardstick spread them, two units a core at most. Four units whose
quotas sum to the whole of a core, busy at once, share that core: each 40 ms answer waits for the others, and a slower answer
brings fewer requests from closed-loop clients. That is the trade of packing read on this rig: fewer machines on, each one
fuller, each answer slower.

The mechanism answer is already in the engine that stands and not yet in this orchestrator: on the kind rig no replica is
added to a host while it is 75% busy (`omni_controller/capacity.py`, omni-v7). The room rule here counts requests only; its
next form counts the machine's measured busy share as well, so a machine at its top takes no more units and the brain wakes
another instead. It is in the orchestrator as a declared option, `--room-rule busy` (`omni_orchestrator/scheduler.py`,
`BUSY_TOP`), off by default; the showing that runs it is read against this one, and nothing here was tuned after the reading.
The yardstick always places by requests alone, as Kubernetes' scheduler does.

**One body.** A job of 16 batch tasks (about 2 s of processor each, four at a time) ran in the room the service left while
the clients went 3 → 6 → 3: 16 of 16 tasks finished with their result files written, the service answered 603 requests, 0
failed, 0 wrong, its 95th percentile 233 ms.

**The drills**, with the clients running (four) through all of them: a unit killed (its hand started it again; 0 requests
failed), a machine lost with its units (declared down after three silent polls, its units placed again elsewhere; 0 failed)
and repaired (it joined empty), the control plane killed for 10 s and started again (the units kept serving; it replayed its
journal and took every unit back as it stood, none started again; 0 failed), the kill switch on (the brain off, the declared
two units and every machine held) and off. 1,507 requests through the drills, 1,507 answered, 0 failed, 0 wrong.

## 3. What it covers, and what it does not yet

Covered and shown: the desired state kept and survived (the journal), placement by room, a unit's whole life (start, probe,
restart, stop), processor and memory walls, one address with the load shared, units scaled with the load, machines woken
and parked, batch beside a service with the service first, a machine lost, a kill switch, an audit of every decision.

Not yet: many hosts over a network (the hands already answer over HTTP; the showing ran on one host), container images and a
registry (units are processes), network isolation, service names and encryption, storage that follows a unit, rolling updates
of a new version, secrets, users and permissions. The comparison that matters, this orchestrator against Kubernetes itself on
the same organism and load, runs on the kind rig on GitHub and has not run yet.

## 4. The claim, exactly

Omni-Compass can run the showing's organism (a checked service and a batch job) without Kubernetes, with its own scheduling,
scaling, lifecycle, recovery and coordination, on one host, with no request lost through a unit's death, a machine's loss,
the control plane's death or the kill switch. Against the yardstick on this rig it held the same units on fewer machines and
answered slower and less: the trade of packing, with its mechanism named above. Equivalent output and complete functional
coverage of a declared organism are targets to engineer toward, not results this showing establishes.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
