# The 1107 Muscles: What Each Is For, and How It Is Wired

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

A **muscle** is one setting on one machine that already has its own control: a replica target, a node pool's size, a GPU's clock ceiling, a chiller's setpoint, a battery's reserve, a joint's effort. Omni-Compass does not replace that control. It reads the machine's meters and, at its default, the max, moves the setting the machine already accepts toward the machine's own limit for the most work, never past it and never below native, through a plug that reads the setting once before the first write, reads back every write, steps aside if another controller moves it, and walks it back to native at the end. A knob native already runs at the top of its range is at its limit on native and is left there.

This chapter lists all 1107 muscles of the catalog (`realms/catalog_v5.csv`, engine omni-v5). For each one it says what kind of machine it is, which of the four kinds of knob it is, what Omni-Compass reads and does with it, how such a muscle is reached in a real stack, and which organisms it belongs to. The plants behind the benchmark numbers are models of these machines (evidence class **S**); a muscle in this list is wired on a real system only through the levels and the checks of the manual (chapters 8 and 9). See `DISCLOSURES.md`.

## How to read an entry

**The four kinds of knob.**

- **capacity**: how much of the machine is in service (replicas, instances, units, speed). At the max Omni-Compass pushes it to the machine's own limit for the most work, never past it and never below native.
- **admission**: what is let in (queues, rate limits, admission control). Native already lets everything in: the knob is at its limit on native, and Omni-Compass reads it and leaves it native.
- **power**: the power share or limit the machine may draw. Native already runs it at full: at its limit on native, read and left native.
- **setpoint**: the target the machine's own loop holds (a temperature, a reserve, a process value). At the max a room is cooled ahead of the heat and a battery's charge is held for its line, inside the safe band, never behind native on its line.

**The five kinds of plant.** Every muscle is modelled on one of five plants, each with its own service reading and lever:

| Plant | What it is | What Omni-Compass reads | What Omni-Compass moves |
|---|---|---|---|
| `compute_pool` | a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs | how far its queue and its load sit toward the service line (queue or lateness, and load above half) | the capacity it may use: its replica or instance count (through its autoscaler's target or floor), its power share, or one unit given back through the release gate |
| `thermal_zone` | a data hall or building zone cooled by chillers, air handlers or fans | its temperature against its limit | its supply setpoint (colder is more cooling), its power share, or one cooling unit given back when the room has margin |
| `energy_storage` | a battery, UPS or microgrid store with a load and a grid connection | its draw on the grid connection and its reserve | its reserve setpoint (how much charge it holds back); its power limit is left native |
| `motion_axis` | a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor | its tracking error and its load | its speed and effort share, or its power share |
| `process_loop` | a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint | how far the process sits from its band | its setpoint within its safe band, its actuator range, or its power share |

**Every muscle its own card.** The brain is one, its settings each muscle's own. A muscle's card holds the settings the max uses for that muscle (a machine pool: how full it runs on its forecast before it calls for more, and how many decisions of history it reads; a battery: how many wobbles of margin it keeps under its line, and, wired by its power, how long it reads its line before it holds and how much of it it keeps clear). The cards were found by an automatic search over every muscle on the development seeds, today's global setting always one of the choices, and kept only where the card beat the global setting beyond the noise on two separate sets of seeds and on no seed under any load fell behind native: never over its line more often, never less work, never its line cleared later (`tools/tune_cards.py`, `realms/muscle_cards_v5.csv`, `results/cards_v5/`). Inside a body, a battery wired by its power keeps the body's own margins on its line. 364 muscles carry a card of their own; every other muscle runs the global setting (machines started at 95% full, the last 20 decisions read, 3.09 wobbles of margin on a battery's line, 5% of it kept clear). Each muscle's card is in the last column of its family's table.


**The organisms.** The 1107 muscles build six organisms: each of the four realms (every muscle whose realm list includes it), the four stacked with every duplicate kept (1,908), and the whole tower with every muscle once (1107). A muscle of the shared spine sits in all four realms.

| Organism | Muscles |
|---|---:|
| Compute / AI / Cloud | 540 |
| Physics / Robotics / Autonomous | 404 |
| Energy / Facility / Industrial | 480 |
| Distribution / Specialized | 484 |
| The four stacked, every duplicate kept | 1,908 |
| The whole tower, every muscle once | 1107 |

**How a muscle is reached in a real stack.** The class of machine decides the wire:

| Class of machine | What it is | The wire in a real stack |
|---|---|---|
| `batch` | batch and queued jobs | the job queue (Kubernetes Jobs, Slurm, Spark) |
| `batch_reactor` | a GMP batch reactor, fermenter or food process | the batch control system (ISA-88, OPC UA) |
| `building` | a building zone | the building management system |
| `chamber` | a controlled chamber (clean room, kiln, reactor) | the PLC or DCS |
| `clinical` | clinical systems: imaging archives, records, interface engines, monitoring gateways | the application's own scaling and admission settings (Kubernetes, the vendor console) |
| `commerce` | a customer-facing service with bursts | the Kubernetes API |
| `cpu_host` | a CPU host whose clock and power can be set | Linux cpufreq and RAPL |
| `data_hall` | a data hall cooling plant | the building management system (BACnet, Modbus) or its command line |
| `database` | a database cluster | the database operator (replicas, connection pools) |
| `district_heat` | a district heating or cooling network | the network control system and substation controllers (Modbus, M-Bus) |
| `elevator_hoist` | an elevator or escalator drive and its group control | the lift controller and destination dispatch (modelled only) |
| `ev_traction` | an electric vehicle traction motor | the vehicle's motor controller (CAN; modelled only) |
| `fabric` | a high-speed fabric (RDMA, DPU, SmartNIC) | the fabric manager's API |
| `facility` | a facility battery behind the meter | the energy management system |
| `feeder_voltage` | a distribution feeder's voltage | the distribution management system (IEC 61850, DNP3; modelled only) |
| `flight_axis` | a flight-control axis | the flight controller (modelled only) |
| `gpu` | GPU serving with a response-time target | nvidia-smi (clock ceiling and power limit) or the serving autoscaler |
| `gpu_batch` | GPU training and batch work | nvidia-smi, the job scheduler's pause and resume |
| `hospital` | a hospital's critical rooms (operating rooms, isolation, pharmacy, imaging suites) | the hospital's building management system (BACnet) |
| `inverter` | a plant of grid-support inverters or wind turbines | the plant controller and inverter settings (SunSpec, IEC 61850, IEEE 1547) |
| `irrigation` | pumps, pressure and climate on a farm or in a greenhouse | the pump station controller, the pivot panel or the climate computer (Modbus, the vendor cloud) |
| `marine_propulsion` | a ship's propulsion shaft and power plant | the vessel automation and power management system (modelled only) |
| `microgrid` | a microgrid battery and loads | the inverter or energy management system (IEEE 2030.5, SunSpec, OpenADR) |
| `mill` | a grinding, flotation or materials-handling circuit | the plant DCS or PLC (OPC UA) |
| `network` | network routing and switching | the network controller (SDN, routing API) |
| `node` | a fleet of machines or VMs that boot in minutes | the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG) |
| `pipeline` | a pipeline segment with its compressors, pumps and valves | pipeline SCADA (DNP3, Modbus, OPC UA) |
| `port` | a container terminal's cranes and vehicles taking moves | the terminal operating system and fleet controllers |
| `process` | an industrial process loop | the PLC or DCS (OPC UA, EtherNet/IP, PROFINET) |
| `qpu` | a quantum or specialised accelerator queue | the accelerator's job queue |
| `rail_traction` | a train's traction and auxiliary systems | the train control and management system and ATO (modelled only) |
| `ran` | a radio access network cell or site | the RAN controller (O-RAN interfaces) |
| `reaction_wheel` | a spacecraft reaction wheel | the attitude controller (modelled only) |
| `robot_fleet` | a fleet of robots or vehicles taking tasks | the fleet manager's dispatch API |
| `robot_joint` | a robot joint servo | the robot controller (ROS 2, EtherCAT, the drive's fieldbus) |
| `server` | an application service on servers or pods | the Kubernetes API (HPA target and floor, pod resize) |
| `storage` | block, file or object storage | the storage system's QoS and tiering API |
| `turbine` | a generating unit's governor, boiler or excitation loop | the plant DCS and governor (OPC UA, IEC 61850; modelled only) |
| `ups` | an uninterruptible power supply | the UPS and PDU management interface (SNMP, Modbus) |
| `water` | a water or pumping process | the SCADA system (Modbus, DNP3) |
| `workflow` | a workflow or pipeline engine | the workflow engine's concurrency settings |

Wires marked *modelled only* exist as plants in the benchmark and are not built for live use.

## The shared spine: 267 muscles in all four realms

The machines every realm stands on: servers, machines, GPUs and CPUs, network, storage, observability, security, cooling and electrical distribution. Each spine muscle is part of every realm's organism, counted once in the tower and four times in the stack.

### Cloud VM & Capacity (21 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `node` (a fleet of machines or VMs that boot in minutes), reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 97 | vm count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 98 | vm size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 99 | vm start stop | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 100 | vm migrate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 101 | instance family | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 102 | asg min | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 103 | asg max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 104 | spot mix | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 105 | reservation mix | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 106 | zone selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 107 | region selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 108 | architecture selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 109 | accelerator selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 110 | boot disk class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 111 | placement group | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 112 | interruption response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1038 | target tracking policy | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1039 | scaling cooldown warmup | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1114 | vm cpu cap by priority | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1120 | predictive scaling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1121 | instance refresh | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |

### Container Resources (25 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 33 | cpu request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 34 | cpu limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 35 | memory request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 36 | memory limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 37 | ephemeral storage | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 38 | hugepages | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 39 | io weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 40 | pids limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 41 | memory high | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 42 | memory reclaim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 43 | swap limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 44 | cgroup io max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 45 | cpu weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 46 | cpu quota | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 47 | cpuset | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 48 | runtime class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1017 | in place resize | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1019 | namespace quota | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1020 | default limits | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1022 | memory hard limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1023 | memory protection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1024 | io latency target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1025 | freeze | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 2176 | cruisekube request rightsizing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 2177 | goldilocks vpa request recommendation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 10 decisions |

### Host CPU & Memory (26 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `cpu_host` (a CPU host whose clock and power can be set), reached through Linux cpufreq and RAPL. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 113 | cpufreq min | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 114 | cpufreq max | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 115 | rapl package power | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 116 | uncore frequency | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 117 | energy perf preference | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 118 | cpu idle policy | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 119 | memory bandwidth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 120 | numa balance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 121 | irq affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 122 | llc allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 123 | memory pressure gate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 124 | page reclaim rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 125 | transparent hugepages | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 126 | core online offline | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 127 | thermal throttle policy | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 128 | host power profile | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 1040 | frequency governor | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 1041 | turbo boost | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1042 | dram power limit | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 1043 | swappiness reclaim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1112 | core packing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1115 | per pod cpu frequency range and c state access | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 1116 | uncore frequency per node | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 2174 | ear cpu frequency policy | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 2175 | ear global energy budget | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 2178 | k8s power manager core profile | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |

### Kubernetes Placement & Scheduling (21 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 49 | node selector | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 85% full; reads the last 10 decisions |
| 50 | node affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 51 | pod anti affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 52 | topology spread | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 53 | numa placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 54 | gpu topology | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 55 | storage locality | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 56 | network locality | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 57 | taint toleration | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 58 | priority class | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 59 | preemption policy | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 60 | device claim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 61 | failure domain spread | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 62 | scheduler backoff | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 63 | gang admission | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 64 | deschedule | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1026 | scheduler scoring strategy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1027 | scheduler plugin weights | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 1028 | scheduling gates | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1029 | cpu manager | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 2179 | peaks power aware placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |

### Kubernetes Workload Scaling (32 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 17 | replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 18 | hpa cpu target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 19 | hpa memory target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 20 | hpa custom target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 21 | vpa apply | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 22 | scale to zero | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 80% full; reads the last 40 decisions |
| 23 | keda threshold | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 24 | rollout rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 25 | max surge | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 26 | max unavailable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 27 | deployment pause resume | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 28 | rollout abort | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 29 | pod eviction | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 30 | pdb policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 31 | scheduler queue priority | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 32 | api priority fairness | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1001 | hpa min replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1002 | hpa max replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 1003 | hpa scale down stabilisation window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1004 | hpa scale up stabilisation window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1005 | hpa scaling rate policies | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1006 | hpa policy selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1007 | hpa tolerance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1008 | hpa sync period | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1009 | vpa minmax allowed resources | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1010 | keda polling interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1011 | rollout progress deadline | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1012 | rollout readiness delay | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1014 | unhealthy pod eviction policy | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1015 | graceful termination | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1016 | probes | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 2172 | kepler energy target autoscaling | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |

### GPU Hardware (22 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `gpu` (GPU serving with a response-time target), reached through nvidia-smi (clock ceiling and power limit) or the serving autoscaler. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 129 | gpu allocate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 130 | gpu power limit | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 131 | gpu sm clock | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 132 | gpu memory clock | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 133 | gpu persistence mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 134 | gpu compute mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 135 | mig mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 136 | mig geometry | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 85% full; reads the last 10 decisions |
| 137 | gpu timeslice | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 138 | gpu mps | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 139 | gpu quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 140 | gpu reset | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 141 | gpu thermal limit | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 142 | gpu ecc response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 143 | gpu job power budget | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1044 | application clocks | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 1045 | gpu temperature target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1117 | sync boost | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 1118 | target clocks | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 2173 | climatik inference power cap | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 2180 | adaptive gpu power cap | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 2181 | nvidia platform power budget | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |

### Node Fleet & Karpenter-Class Control (24 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `node` (a fleet of machines or VMs that boot in minutes), reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 65 | node desired | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 66 | node pool min | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 67 | node pool max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 68 | node provision | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 60 decisions |
| 69 | node cordon | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 70 | node drain | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 71 | node consolidate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 72 | node replace | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 73 | node shutdown | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 74 | node power on | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 75 | nodepool weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 76 | disruption budget | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 77 | consolidation policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 78 | consolidate after | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 90% full; reads the last 20 decisions |
| 79 | expire after | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 80 | capacity class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1030 | scale down utilisation threshold | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1031 | scale down unneeded time | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1032 | scale down delay after add | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 1033 | expander | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 80% full; reads the last 10 decisions |
| 1034 | node pool limits | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1035 | kubelet eviction thresholds | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1036 | kubelet reserved resources | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1037 | max pods per node | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 40 decisions |

### Network Routing & Switching (19 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `network` (network routing and switching), reached through the network controller (SDN, routing API). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 225 | lb weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 226 | route weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 227 | rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 228 | bandwidth limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 229 | qos class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 230 | connection limit | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 231 | failover route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 232 | nic rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 233 | nic queue count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 234 | queue discipline | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 235 | congestion control | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 236 | egress budget | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 237 | ingress budget | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 238 | ecmp weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 239 | path selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 240 | network isolation | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1046 | nic interrupt coalescing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1047 | nic ring size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 80% full; reads the last 10 decisions |
| 1048 | port link power | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |

### Observability & Telemetry (9 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 373 | collector memory limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 374 | export concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 376 | cardinality budget | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 377 | retention window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 85% full; reads the last 40 decisions |
| 378 | remote write queue | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 379 | telemetry shed | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1053 | metric scrape interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1054 | batching | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 80% full; reads the last 10 decisions |
| 1119 | per pod energy attribution | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 60 decisions |

### Reliability, Security & Recovery (12 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 385 | restart | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 386 | rollback | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 388 | traffic divert recovery | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 389 | degraded mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 390 | actuator freeze | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 391 | workload isolate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 393 | credential rotation gate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 394 | policy enforcement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 395 | rate abuse gate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 396 | fault domain isolate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 397 | backup trigger | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 400 | kill switch | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |

### Storage Block/File/Object (20 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `storage` (block, file or object storage), reached through the storage system's QoS and tiering API. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 257 | volume size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 258 | iops limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 259 | throughput limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 260 | replica count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 261 | storage tier | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 262 | volume placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 263 | snapshot trigger | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 264 | rebalance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 265 | recovery rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 266 | backfill rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 267 | compaction pressure | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 268 | cache allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 269 | object replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 270 | erasure code profile | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 271 | storage admission | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 272 | degraded storage gate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1049 | scrub schedule | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1050 | io scheduler | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |
| 1051 | disk power spin down | power | at its limit on native (the full clock): read and left native | all four realms; stack; tower | global |
| 1052 | lifecycle tiering | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | all four realms; stack; tower | global |

### Cooling, Chillers & Thermodynamics (18 muscles)

Each is a data hall or building zone cooled by chillers, air handlers or fans; its class is `data_hall` (a data hall cooling plant), reached through the building management system (BACnet, Modbus) or its command line. Omni-Compass reads its temperature against its limit. It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 545 | supply air temperature | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | all four realms; stack; tower | global |
| 546 | return air target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | all four realms; stack; tower | global |
| 547 | coolant supply temperature | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | all four realms; stack; tower | global |
| 548 | coolant flow | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 549 | pump speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 550 | fan speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 551 | chiller setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | all four realms; stack; tower | global |
| 552 | compressor authority | power | at its limit on native (the site envelope at full): read and left native | all four realms; stack; tower | global |
| 553 | cooling tower fan | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 554 | cooling capacity | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 555 | rack thermal budget | power | at its limit on native (the site envelope at full): read and left native | all four realms; stack; tower | global |
| 556 | gpu thermal envelope | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | all four realms; stack; tower | global |
| 557 | cpu thermal envelope | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | all four realms; stack; tower | global |
| 558 | thermal workload migrate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 559 | thermal load shed | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1055 | server fan speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 1056 | economiser | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |
| 1122 | chiller plant supervisory control rl with safety layer | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | all four realms; stack; tower | global |

### PDU, UPS & Electrical Distribution (18 muscles)

Each is a battery, UPS or microgrid store with a load and a grid connection; its class is `ups` (an uninterruptible power supply), reached through the UPS and PDU management interface (SNMP, Modbus). Omni-Compass reads its draw on the grid connection and its reserve. It belongs to every organism.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 529 | server power cap | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 530 | rack power cap | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 531 | pdu branch power limit | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 532 | pdu outlet control | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0 wobbles of margin on its line |
| 534 | ups operating mode | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0 wobbles of margin on its line |
| 535 | ups charge rate | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 536 | ups discharge rate | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 537 | phase balance | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0 wobbles of margin on its line |
| 538 | load transfer | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 539 | reactive power target | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0 wobbles of margin on its line |
| 540 | voltage target | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0.25 wobbles of margin on its line |
| 541 | generator dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0 wobbles of margin on its line |
| 542 | electrical isolation | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 543 | breaker trip gate | admission | at its limit on native (nothing paced or turned away): read and left native | all four realms; stack; tower | global |
| 1057 | ups shutdown battery test | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | all four realms; stack; tower | 0 wobbles of margin on its line |
| 1110 | hierarchical power budget row pdu switchboard controllers | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 1111 | priority aware capping throttle low priority first | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |
| 1113 | power oversubscription with prediction | power | at its limit on native (full battery power): read and left native | all four realms; stack; tower | global |

## Realm: Compute / AI / Cloud (273 muscles of its own, 540 in its organism with the spine)

### AI Inference Serving (24 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `gpu` (GPU serving with a response-time target), reached through nvidia-smi (clock ceiling and power limit) or the serving autoscaler. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 161 | model replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 162 | model route weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 163 | model load | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 164 | model unload | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 165 | model instance count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 166 | continuous batching | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 167 | max batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 168 | batch queue delay | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 169 | inference concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 170 | inference max tokens | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 60 decisions |
| 171 | kv cache budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 172 | prefix cache budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 173 | speculative decode budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 174 | model precision | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| 175 | inference priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 176 | inference slo gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1058 | autoscaling target concurrency qps | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1059 | scale to zero panic window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 1060 | request priority levels | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1061 | kv cache swap space | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1062 | chunked prefill | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 20 decisions |
| 1063 | tensor parallel degree | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 40 decisions |
| 1064 | disaggregated prefill decode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1065 | lora adapter load | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |

### AI Training (18 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `gpu_batch` (GPU training and batch work), reached through nvidia-smi, the job scheduler's pause and resume. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 177 | training workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 178 | global batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 10 decisions |
| 179 | microbatch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 90% full; reads the last 10 decisions |
| 180 | gradient accumulation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 181 | data parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 182 | tensor parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 183 | pipeline parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 184 | expert parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 20 decisions |
| 185 | checkpoint interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 186 | checkpoint trigger | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 187 | training preempt | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 188 | training gang size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 10 decisions |
| 189 | elastic worker count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 90% full; reads the last 10 decisions |
| 190 | straggler mitigation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 191 | training precision | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| 192 | compute comm overlap | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 40 decisions |
| 1066 | activation checkpointing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 1067 | dataloader workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |

### Cross-Cluster, Multi-Region & Edge (18 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `node` (a fleet of machines or VMs that boot in minutes), reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 609 | multi cluster dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 610 | region dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 611 | zone dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 612 | edge dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 613 | cloud capacity class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 614 | workload migrate region | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 615 | data residency gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 616 | latency region gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 617 | cost region gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 618 | carbon region gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 619 | global failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 620 | federation quota | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 621 | cross cluster replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 622 | edge offload | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 623 | global admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5128 | edge site node pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| V5-5129 | edge inference gpu clocks | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| V5-5130 | edge sync interval | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |

### DPU SmartNIC & Programmable IO (12 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `fabric` (a high-speed fabric (RDMA, DPU, SmartNIC)), reached through the fabric manager's API. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| AUDIT-0021 | dpu pf tx rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0022 | dpu vf tx rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0023 | dpu sf tx rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0024 | dpu bandwidth share | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0025 | dpu qos group | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0026 | sriov vf count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0027 | smartnic flow steering | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 10 decisions |
| AUDIT-0028 | smartnic offload enable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0029 | dpu cpu budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| AUDIT-0030 | dpu memory budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| AUDIT-0031 | dpu service placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| AUDIT-0032 | dpu failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |

### Distributed Cluster Managers (15 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `batch` (batch and queued jobs), reached through the job queue (Kubernetes Jobs, Slurm, Spark). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 209 | task admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 210 | task priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 211 | resource reservation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 10 decisions |
| 212 | cluster quota | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 213 | task preemption | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 214 | binpack pressure | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 10 decisions |
| 215 | spread pressure | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 10 decisions |
| 216 | gang schedule | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 90% full; reads the last 60 decisions |
| 217 | worker allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 218 | maintenance evacuation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 90% full; reads the last 10 decisions |
| 219 | oversubscription | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 220 | resource reclaim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 20 decisions |
| 221 | queue fairness | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 222 | deadline pressure | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 223 | scheduler retry | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |

### GPU Fabric & RDMA (18 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `fabric` (a high-speed fabric (RDMA, DPU, SmartNIC)), reached through the fabric manager's API. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 145 | nvlink placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 146 | nvswitch route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 147 | gpu fabric quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 148 | rdma bandwidth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 149 | rdma route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 150 | nic affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 151 | collective concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 152 | collective algorithm | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 153 | collective chunk size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 154 | rank placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 155 | gpudirect policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 156 | congestion response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 157 | rail selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 158 | fabric failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 159 | communication priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 160 | fabric isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1068 | collective protocol | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 1069 | nic hca selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |

### HPC & Distributed Compute (19 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `batch` (batch and queued jobs), reached through the job queue (Kubernetes Jobs, Slurm, Spark). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 193 | job slots | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 194 | mpi ranks | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 195 | rank mapping | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 196 | node allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 197 | job walltime | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 198 | job priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 199 | job preemption | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 200 | checkpoint restart | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 20 decisions |
| 201 | parallel io budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 202 | collective budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 203 | accelerator share | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 204 | cpu gpu ratio | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 205 | memory per rank | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 206 | scratch budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 207 | scheduler fair share | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 208 | backfill policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 1070 | node power saving | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| 1071 | cpu frequency per job | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| 1072 | partition limits | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |

### Kubernetes Dynamic Device Allocation (8 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `gpu` (GPU serving with a response-time target), reached through nvidia-smi (clock ceiling and power limit) or the serving autoscaler. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| AUDIT-0001 | dra device class selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 40 decisions |
| AUDIT-0002 | dra claim capacity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| AUDIT-0003 | dra claim sharing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 20 decisions |
| AUDIT-0004 | dra device taint | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| AUDIT-0005 | dra device eviction | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| AUDIT-0006 | dra binding readiness | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 20 decisions |
| AUDIT-0007 | dra binding failure response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| AUDIT-0008 | dra device configuration | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |

### OpenShift & Machine API (9 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `node` (a fleet of machines or VMs that boot in minutes), reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 85 | machine remediation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 88 | machine health gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 89 | mcp pause | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 90 | mcp max unavailable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 91 | node config rollout | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 92 | operator reconcile budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 93 | cluster version pacing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 94 | infra machine admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 95 | machine failure domain | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |

### Quantum Computing Control Simulation (16 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `qpu` (a quantum or specialised accelerator queue), reached through the accelerator's job queue. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 593 | qubit mapping | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 594 | circuit admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 595 | shot allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 596 | circuit scheduling | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 597 | gate scheduling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 598 | pulse amplitude | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 599 | pulse duration | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 600 | pulse phase | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 601 | pulse frequency | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| 602 | coupling control | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 603 | reset scheduling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 604 | measurement scheduling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 605 | dynamical decoupling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 606 | noise aware routing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| 607 | error mitigation budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 608 | quantum queue priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |

### Work Admission & Demand Shaping (19 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 1 | api concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 2 | queue concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 3 | queue backpressure | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 4 | job admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 5 | batch admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 6 | inference admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 7 | load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 8 | priority gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 9 | tenant admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 10 | burst limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 11 | deadline admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 12 | work budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 13 | request queue limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 14 | retry admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 15 | background work gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 16 | maintenance work gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1074 | request concurrency limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1123 | adaptive concurrency limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| 1124 | priority request queue under limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |

### Linux Kernel & OS Control (20 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `cpu_host` (a CPU host whose clock and power can be set), reached through Linux cpufreq and RAPL. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5001 | cgroup cpu weight | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5002 | cgroup cpu quota | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5003 | cgroup memory high | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 10 decisions |
| V5-5004 | cfs scheduler latency | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5005 | cpufreq dvfs governor | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| V5-5006 | transparent hugepages | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5007 | io scheduler depth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5008 | numa auto balancing | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5009 | dirty ratio writeback | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5010 | vm swappiness | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5011 | tcp buffer autotune | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 60 decisions |
| V5-5012 | block nr requests | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5013 | ksm memory dedup | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |
| V5-5014 | net rx coalesce | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5015 | cpu cstate governor | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| V5-5016 | zswap pool fraction | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5017 | page cache reclaim | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5018 | irqbalance affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 60 decisions |
| V5-5019 | net qdisc codel target | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5020 | hugepage pool reserve | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 20 decisions |

### Serverless & Functions (FaaS) (9 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5021 | fn concurrency limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5022 | fn provisioned concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5023 | fn scale to zero idle | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5024 | fn memory size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5025 | fn prewarm pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5026 | fn reserved concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5027 | fn burst admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5028 | fn snapstart restore | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| V5-5029 | fn timeout budget | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |

### Virtualization & Hypervisor (9 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `cpu_host` (a CPU host whose clock and power can be set), reached through Linux cpufreq and RAPL. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5030 | vcpu allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5031 | memory ballooning | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5032 | vm overcommit density | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| V5-5033 | live migration pacing | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5034 | numa vcpu pinning | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5035 | sriov vf allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5036 | vgpu partition | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5037 | vm memory dedup ksm | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |
| V5-5038 | hypervisor cpu pinning | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |

### Gut: Data-plane Intake & Waste (8 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `process` (an industrial process loop), reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Omni-Compass reads how far the process sits from its band. Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5045 | ingress intake pacing | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |
| V5-5046 | dead letter retry cap | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5047 | gc compaction pacing | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |
| V5-5048 | ttl eviction waste | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5049 | backpressure threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5050 | queue drain rate | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |
| V5-5051 | retry budget window | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5052 | compaction debt drain | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |

### Skin: Perimeter & Admission (5 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5053 | rate limit token bucket | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5054 | connection admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5055 | waf inspection sampling | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower | global |
| V5-5056 | tls session cache | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5057 | ddos shield admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |

### Media Streaming & CDN (14 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `process` (an industrial process loop), reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Omni-Compass reads how far the process sits from its band. Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5072 | abr bitrate ladder cap | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5073 | player buffer target | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5074 | transcoder worker pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5075 | live transcode gpu clocks | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| V5-5076 | vod transcode batch power | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| V5-5077 | packager workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 60 decisions |
| V5-5078 | origin shield cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5079 | edge cache ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5080 | segment duration target | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5081 | cdn request coalescing | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5082 | drm license server pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 85% full; reads the last 40 decisions |
| V5-5083 | thumbnail sprite batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 80% full; reads the last 10 decisions |
| V5-5084 | media ingest admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5085 | encoder lookahead frames | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |

### Game Servers & Real-Time Interactive (12 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5086 | agones fleet buffer size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5087 | agones fleet min replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 60 decisions |
| V5-5088 | agones fleet max replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 40 decisions |
| V5-5089 | game server tick rate | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5090 | players per server cap | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5091 | matchmaking admission rate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5092 | matchmaking wait window | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5093 | relay server pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5094 | voice chat mixer pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5095 | game node pool autoscaler | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5096 | replay render batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5097 | cloud gaming gpu clocks | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |

### Blockchain & Ledger Nodes (10 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `storage` (block, file or object storage), reached through the storage system's QoS and tiering API. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5098 | node db cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5099 | mempool max size | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5100 | max peer connections | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5101 | script validation threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5102 | block relay admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5103 | rpc work queue depth | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5104 | utxo cache flush interval | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5105 | indexer batch workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5106 | archive node storage tier | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5107 | validator host power profile | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |

### CI/CD & Build Farms (10 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `batch` (batch and queued jobs), reached through the job queue (Kubernetes Jobs, Slurm, Spark). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Compute / AI / Cloud.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5108 | runner scale set min runners | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5109 | runner scale set max runners | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 60 decisions |
| V5-5110 | build concurrency limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5111 | build cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | global |
| V5-5112 | test shard parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5113 | job queue admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower | global |
| V5-5114 | artifact retention ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower | global |
| V5-5115 | build node cpu frequency | power | at its limit on native (the full clock): read and left native | Compute; stack; tower | global |
| V5-5116 | remote execution workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5117 | warm runner pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower | machines started at 75% full; reads the last 40 decisions |

## Realm: Physics / Robotics / Autonomous (137 muscles of its own, 404 in its organism with the spine)

### Automotive EV & Mobile Powertrain (14 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `ev_traction` (an electric vehicle traction motor), reached through the vehicle's motor controller (CAN; modelled only). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 1083 | state of charge limits | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 1084 | smart charging schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| AUDIT-0045 | traction torque limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0046 | regen braking level | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0047 | battery charge limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0048 | battery discharge limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0049 | battery thermal target | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0050 | motor thermal limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0051 | vehicle speed envelope | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| AUDIT-0052 | energy recovery target | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0053 | auxiliary power budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0054 | fast charge current | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0055 | fast charge voltage | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| AUDIT-0056 | vehicle safe state | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |

### Aviation & Autonomous Flight (28 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `flight_axis` (a flight-control axis), reached through the flight controller (modelled only). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 481 | throttle envelope | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 482 | attitude target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 483 | attitude rate target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 484 | velocity target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 485 | altitude target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 486 | waypoint authority | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 487 | flight hold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 488 | return to home | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 489 | land action | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 490 | mission admission | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 491 | geofence response | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 492 | failsafe selection | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 493 | battery reserve threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 494 | actuator saturation envelope | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 495 | flight mode transition | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 496 | flight termination safe state | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 1079 | attitude rate gains | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 1080 | horizontal speed limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 1081 | vertical speed limits | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 1082 | acceleration jerk limits | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| V5-5143 | px4 mpc xy vel max | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5144 | px4 mpc z vel max up | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5145 | px4 mpc acc hor | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5146 | px4 mc rollrate max | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5147 | ardupilot wpnav speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5148 | ardupilot atc accel r max | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| V5-5149 | drone battery failsafe reserve | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Physics; stack; tower | 1.5 wobbles of margin on its line |
| V5-5150 | swarm formation spacing | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |

### Robotics Fleet & Warehouse Automation (17 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `robot_fleet` (a fleet of robots or vehicles taking tasks), reached through the fleet manager's dispatch API. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 449 | robot dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 450 | task assignment | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 451 | traffic reservation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 452 | robot route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 453 | charging dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 454 | battery reserve | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 455 | elevator request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 456 | door request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 457 | conveyor speed | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 458 | agv speed | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 459 | warehouse zone admission | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 460 | robot quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 461 | fleet failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 462 | human safe stop | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |
| 463 | fleet concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| V5-5151 | amr fleet charge threshold | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Physics; stack; tower | 1.5 wobbles of margin on its line |
| V5-5152 | amr fleet active robots | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | global |

### Robotics Motion Control (26 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `robot_joint` (a robot joint servo), reached through the robot controller (ROS 2, EtherCAT, the drive's fieldbus). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 433 | joint position | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 434 | joint velocity | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 435 | joint acceleration | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 436 | joint effort | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 437 | cartesian velocity | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 438 | trajectory speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 439 | trajectory acceleration | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 440 | jerk limit | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 441 | collision margin | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 442 | force limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 443 | gripper force | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 444 | locomotion speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 445 | steering angle | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 446 | braking force | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 447 | balance correction | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 1076 | trajectory tolerances | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 1077 | velocity acceleration scaling | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 1078 | controller update rate | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5135 | ros2 executor threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower | machines started at 70% full; reads the last 40 decisions |
| V5-5136 | ros2 qos history depth | setpoint | left native: native already holds it inside its band (nothing to win) | Physics; stack; tower | global |
| V5-5137 | ros2 control loop rate | setpoint | left native: native already holds it inside its band (nothing to win) | Physics; stack; tower | global |
| V5-5138 | humanoid balance margin | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5139 | humanoid gait speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5140 | humanoid joint torque limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| V5-5141 | humanoid step height | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| V5-5142 | manipulator payload speed scaling | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |

### Spacecraft & Flight Software (14 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `reaction_wheel` (a spacecraft reaction wheel), reached through the attitude controller (modelled only). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 497 | space command admission | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 499 | flight task schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 500 | space mode transition | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 501 | payload duty cycle | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 502 | communication allocation | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 503 | space power budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 504 | space thermal command | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 505 | attitude command envelope | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 506 | reaction wheel allocation | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 507 | rcs authority | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 508 | safe mode transition | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 509 | watchdog recovery | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 510 | instrument activation | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 511 | fault isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |

### Rail Traction & Train Control (14 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `rail_traction` (a train's traction and auxiliary systems), reached through the train control and management system and ATO (modelled only). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2054 | traction effort limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2055 | regenerative braking share | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2056 | coasting speed target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2057 | dwell time schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2058 | hvac duty cycle | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2059 | train auxiliary power budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2060 | platform approach speed | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2061 | acceleration rate setpoint | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2062 | wheel slip protection mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2063 | traction motor thermal derate | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2064 | catenary voltage limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2065 | timetable recovery margin | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2066 | headway target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2067 | door release hold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |

### Marine Propulsion & Vessel Automation (12 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `marine_propulsion` (a ship's propulsion shaft and power plant), reached through the vessel automation and power management system (modelled only). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2068 | shaft speed target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 2069 | propeller pitch limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2070 | shaft power limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2071 | bow thruster duty | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2072 | ballast pump mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2073 | engine load sharing setpoint | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 2074 | slow steaming speed target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 2075 | auxiliary engine staging | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 2076 | shore power mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2077 | hotel load budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2078 | trim target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower | global |
| 2079 | rudder rate limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |

### Elevators & Vertical Transport (12 muscles)

Each is a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; its class is `elevator_hoist` (an elevator or escalator drive and its group control), reached through the lift controller and destination dispatch (modelled only). Omni-Compass reads its tracking error and its load. Its home realm is Physics / Robotics / Autonomous.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2146 | hoist speed target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2147 | acceleration limit | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2148 | regen drive mode | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2149 | standby power mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2150 | destination dispatch schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2151 | car parking mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2152 | door dwell hold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2153 | escalator speed target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower | global |
| 2154 | group capacity mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2155 | motor thermal derate | power | at its limit on native (full torque): read and left native | Physics; stack; tower | global |
| 2156 | brake test schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |
| 2157 | fire recall mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower | global |

## Realm: Energy / Facility / Industrial (213 muscles of its own, 480 in its organism with the spine)

### Building & Critical Environment HVAC (15 muscles)

Each is a data hall or building zone cooled by chillers, air handlers or fans; its class is `building` (a building zone), reached through the building management system. Omni-Compass reads its temperature against its limit. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 1094 | setpoint reset trim and respond | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 1095 | duct static pressure setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 1096 | optimal start stop | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| AUDIT-0081 | zone temperature target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| AUDIT-0082 | zone airflow | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| AUDIT-0083 | ahu fan speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| AUDIT-0084 | damper position | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| AUDIT-0085 | economizer position | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| AUDIT-0086 | boiler setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| AUDIT-0087 | heat pump mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0088 | humidity target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| AUDIT-0089 | occupancy ventilation | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0090 | building demand limit | power | at its limit on native (the site envelope at full): read and left native | Energy; stack; tower | global |
| AUDIT-0091 | thermal storage dispatch | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| AUDIT-0092 | hvac emergency mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Energy Storage & Microgrid (19 muscles)

Each is a battery, UPS or microgrid store with a load and a grid connection; its class is `microgrid` (a microgrid battery and loads), reached through the inverter or energy management system (IEEE 2030.5, SunSpec, OpenADR). Omni-Compass reads its draw on the grid connection and its reserve. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 513 | battery charge power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 10 decisions before it holds; keeps 0% of its line clear |
| 514 | battery discharge power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 515 | battery soc reserve | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0.75 wobbles of margin on its line |
| 516 | grid import limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | global |
| 517 | grid export limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 5% of its line clear |
| 518 | pv curtailment | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 519 | ev charge power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | global |
| 520 | heat pump power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 521 | electrolyzer power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 5 decisions before it holds; keeps 0% of its line clear |
| 522 | microgrid demand limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | global |
| 523 | peak shaving | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 524 | time of use schedule | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 1 wobbles of margin on its line |
| 525 | energy load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 526 | flex load admission | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 527 | storage dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 528 | microgrid emergency reserve | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 1 wobbles of margin on its line |
| 1085 | volt var | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 1086 | volt watt | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 1087 | constant power factor reactive power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | global |

### Facility & Grid Optimization (15 muscles)

Each is a battery, UPS or microgrid store with a load and a grid connection; its class is `facility` (a facility battery behind the meter), reached through the energy management system. Omni-Compass reads its draw on the grid connection and its reserve. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 561 | facility power budget | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 562 | utility demand limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 563 | demand response | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 564 | electricity price gate | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 565 | carbon intensity gate | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 566 | renewable dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 567 | generator start stop | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 568 | site battery dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 569 | pue target | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 1 wobbles of margin on its line |
| 570 | cooling power budget | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 571 | it power budget | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | 0 wobbles of margin on its line; reads its line 3 decisions before it holds; keeps 0% of its line clear |
| 572 | rack power allocation | power | at its limit on native (full battery power): read and left native | Energy; stack; tower | global |
| 573 | facility peak guard | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower | 0 wobbles of margin on its line |
| 574 | grid frequency response | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 575 | facility islanding | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Grid Transmission & Distribution (12 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `feeder_voltage` (a distribution feeder's voltage), reached through the distribution management system (IEC 61850, DNP3; modelled only). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| AUDIT-0033 | capacitor bank switch | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0034 | voltage regulator tap | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0035 | transformer tap | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0036 | inverter real power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0037 | inverter reactive power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0038 | feeder voltage target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0039 | feeder load transfer | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0040 | distribution storage dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0041 | demand response dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0042 | frequency droop setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0043 | grid protection mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0044 | grid restoration sequence | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Industrial PLC & Process Automation (18 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `process` (an industrial process loop), reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 465 | plc cycle authority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 466 | machine cell admission | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 467 | valve position | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 468 | pump flow | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 469 | compressor speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 470 | heater power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 471 | furnace setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 472 | pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 473 | temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 474 | mass flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 475 | tank level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 476 | conveyor rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 477 | feed rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 478 | purge vent action | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 1088 | controller mode | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 1089 | alarm limits | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 1090 | safety interlock trip | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 1091 | opc ua writes | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |

### Semiconductor Fab & Precision Manufacturing (13 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `chamber` (a controlled chamber (clean room, kiln, reactor)), reached through the PLC or DCS. Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 1092 | run to run control | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 1093 | idle sleep mode | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0057 | tool job dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0058 | wafer route | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0059 | chamber recipe selection | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0060 | chamber temperature | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0061 | chamber pressure | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0062 | gas flow | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0063 | rf power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0064 | vacuum pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0065 | robot transfer rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0066 | lot priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0068 | tool quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Water Wastewater & Pumping (12 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `water` (a water or pumping process), reached through the SCADA system (Modbus, DNP3). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| AUDIT-0069 | pump speed water | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0070 | valve position water | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0071 | reservoir level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0072 | line pressure target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0073 | flow target water | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| AUDIT-0074 | aeration rate | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0075 | chemical dose rate | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| AUDIT-0076 | filtration backwash | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0077 | lift station dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0078 | leak isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0079 | water demand shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| AUDIT-0080 | water emergency shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Healthcare Critical Environments (13 muscles)

Each is a data hall or building zone cooled by chillers, air handlers or fans; its class is `hospital` (a hospital's critical rooms (operating rooms, isolation, pharmacy, imaging suites)), reached through the hospital's building management system (BACnet). Omni-Compass reads its temperature against its limit. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2001 | operating room air change setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2002 | isolation room pressure target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2003 | patient room temperature setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2004 | surgical suite humidity target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2005 | ahu supply air temperature | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2006 | pharmacy cold room setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2007 | sterile storage humidity setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower | global |
| 2008 | imaging suite cooling capacity | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| 2009 | chiller plant staging | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| 2010 | exhaust fan capacity | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower | global |
| 2011 | ward night setback mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2012 | medical gas plant demand limit | power | at its limit on native (the site envelope at full): read and left native | Energy; stack; tower | global |
| 2013 | emergency power load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Agriculture & Irrigation (14 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `irrigation` (pumps, pressure and climate on a farm or in a greenhouse), reached through the pump station controller, the pivot panel or the climate computer (Modbus, the vendor cloud). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2026 | irrigation pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2027 | mainline pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2028 | soil moisture target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2029 | pivot speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2030 | fertigation dose | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2031 | greenhouse temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2032 | greenhouse co2 target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2033 | vent position setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2034 | grain dryer temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2035 | cold storage temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2036 | barn ventilation rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2037 | milking vacuum level setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2038 | well drawdown level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2039 | drip zone dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Oil & Gas Pipelines (14 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `pipeline` (a pipeline segment with its compressors, pumps and valves), reached through pipeline SCADA (DNP3, Modbus, OPC UA). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2040 | compressor discharge pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2041 | pump station suction pressure target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2042 | line pack target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2043 | pipeline flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2044 | compressor unit staging | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2045 | vfd pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2046 | terminal tank level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2047 | leak detection shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2048 | batch interface dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2049 | heater outlet temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2050 | drag reducing agent dose | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2051 | valve position target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2052 | cathodic protection voltage | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2053 | pressure protection priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Mining & Mineral Processing (14 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `mill` (a grinding, flotation or materials-handling circuit), reached through the plant DCS or PLC (OPC UA). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2092 | sag mill load setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2093 | mill speed target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2094 | crusher gap setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2095 | flotation aeration rate | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2096 | cyclone feed pressure target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2097 | thickener underflow density target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2098 | reagent dose | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2099 | conveyor speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2100 | dewatering pump level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2101 | ventilation on demand airflow | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2102 | stockpile level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2103 | slurry pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2104 | tailings discharge shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2105 | ore blend dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### District Heating & Cooling (13 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `district_heat` (a district heating or cooling network), reached through the network control system and substation controllers (Modbus, M-Bus). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2106 | supply temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2107 | return temperature target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2108 | differential pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2109 | network pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2110 | heat pump staging | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2111 | chp dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2112 | thermal storage level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2113 | peak boiler heater output | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2114 | substation flow limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2115 | peak demand shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2116 | outdoor reset setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2117 | cooling network supply temperature | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2118 | cooling storage level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |

### Power Generation & Turbine Control (14 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `turbine` (a generating unit's governor, boiler or excitation loop), reached through the plant DCS and governor (OPC UA, IEC 61850; modelled only). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2119 | turbine speed droop setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2120 | unit load setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2121 | boiler steam pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2122 | feedwater level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2123 | agc participation limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2124 | excitation voltage setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2125 | hydro gate position target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2126 | combustion air ratio setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2127 | cooling water flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2128 | inlet guide vane position | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2129 | reserve dispatch priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2130 | turbine ramp rate limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2131 | emissions shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2132 | nuclear rod position target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |

### Renewable Generation & Inverter Control (13 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `inverter` (a plant of grid-support inverters or wind turbines), reached through the plant controller and inverter settings (SunSpec, IEC 61850, IEEE 1547). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2133 | inverter volt var setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2134 | inverter volt watt setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2135 | active power curtailment | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2136 | plant reactive power target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2137 | wind turbine yaw offset | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2138 | pitch angle limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2139 | rotor speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2140 | inverter frequency droop setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2141 | ramp rate limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower | global |
| 2142 | tracker stow mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2143 | string mppt voltage setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2144 | noise mode schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2145 | ice detection shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

### Pharmaceutical & Food Manufacturing (14 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `batch_reactor` (a GMP batch reactor, fermenter or food process), reached through the batch control system (ISA-88, OPC UA). Omni-Compass reads how far the process sits from its band. Its home realm is Energy / Facility / Industrial.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2158 | reactor temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2159 | agitator speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2160 | fermenter dissolved oxygen target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2161 | ph setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2162 | pasteurizer holding temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2163 | freezer tunnel temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2164 | cip cycle dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2165 | cleanroom pressure cascade setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2166 | lyophilizer shelf temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2167 | chromatography flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2168 | steam sterilizer cycle priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2169 | oven zone temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower | global |
| 2170 | refrigerant compressor authority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |
| 2171 | batch hold quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower | global |

## Realm: Distribution / Specialized (217 muscles of its own, 484 in its organism with the spine)

### Cache & Memory Services (16 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 305 | cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 306 | cache ttl | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 307 | cache eviction policy | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 308 | cache replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 309 | cache sharding | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 310 | cache prefetch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 311 | cache writeback rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 312 | cache admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 313 | hot key isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 314 | cache connection limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 315 | cache memory limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 316 | cache compression | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 317 | cache warmup | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 318 | cache failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 319 | cache flush rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1106 | memory size threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |

### Commerce & Payment Systems (15 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `commerce` (a customer-facing service with bursts), reached through the Kubernetes API. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 401 | payment admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 402 | payment concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 403 | payment retry | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 404 | payment timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 405 | fraud review gate | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 406 | authorization route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 407 | processor route weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 408 | transaction queue limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 409 | idempotency window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 410 | order reservation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 411 | inventory hold | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 412 | checkout load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 413 | refund queue rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 414 | settlement batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 415 | payment failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |

### Data Analytics & ETL (15 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `batch` (batch and queued jobs), reached through the job queue (Kubernetes Jobs, Slurm, Spark). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 338 | executor size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 339 | dynamic allocation min | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 340 | dynamic allocation max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 341 | shuffle partitions | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 342 | shuffle bandwidth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 343 | etl concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 344 | stage parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 345 | query slots | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 85% full; reads the last 10 decisions |
| 346 | spill threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 347 | cache fraction | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 80% full; reads the last 20 decisions |
| 348 | batch interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 80% full; reads the last 20 decisions |
| 349 | stream backpressure | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 350 | data locality wait | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 80% full; reads the last 20 decisions |
| 351 | speculation policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 352 | analytics admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

### Database & Transactions (19 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `database` (a database cluster), reached through the database operator (replicas, connection pools). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 273 | db replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 275 | db memory | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 276 | db cache | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 90% full; reads the last 40 decisions |
| 277 | query concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 278 | read route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 279 | shard placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 280 | db failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 281 | replication lag gate | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 282 | db write throttle | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 283 | db pool resize | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 284 | transaction concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 285 | lock timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 286 | checkpoint rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 287 | vacuum compaction rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 1099 | parallel workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 1100 | background writer | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1101 | synchronous replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1102 | buffer pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 40 decisions |
| 1103 | io capacity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |

### Messaging & Streaming (22 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 289 | partition count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 290 | partition placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 291 | producer quota | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 292 | consumer quota | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 293 | broker io quota | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 294 | message retention | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 295 | queue depth limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 296 | consumer concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 297 | producer batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 298 | fetch batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 299 | rebalance rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 300 | replication factor | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 301 | retry backoff | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 302 | dead letter divert | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 303 | stream priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 304 | broker failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 1104 | prefetch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 1105 | memory disk alarm | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5124 | mqtt broker max connections | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5125 | mqtt max inflight messages | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5126 | mqtt session expiry | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5127 | broker cluster nodes | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |

### Runtime & Application (21 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 353 | worker count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 10 decisions |
| 354 | thread pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 355 | jvm heap | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 356 | gc budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 357 | connection pool runtime | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 358 | application cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 359 | runtime memory | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 360 | async concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 361 | event loop workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 80% full; reads the last 20 decisions |
| 362 | process count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 363 | request timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 364 | background workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 365 | runtime cpu budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 366 | runtime io budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 367 | runtime restart | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 1108 | go runtime | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 1109 | keepalive connection reuse | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| V5-5131 | dns resolver cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| V5-5132 | dns negative cache ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5133 | mail queue concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5134 | mail retry interval | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |

### Search, Indexing & Vector DB (16 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 321 | index workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 75% full; reads the last 20 decisions |
| 322 | index refresh rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 323 | segment merge rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 324 | search concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 325 | search timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 326 | shard count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 327 | shard replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 328 | shard rebalance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 329 | vector search k | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 330 | vector batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 331 | embedding workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 332 | index memory budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 333 | query route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 60 decisions |
| 334 | hot shard isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 335 | search admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 1107 | circuit breakers | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

### Service Mesh & API Reliability (16 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 241 | circuit breaker | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 242 | retry budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 243 | service timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 244 | service concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 245 | connection pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 246 | traffic divert | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 247 | traffic mirror | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 248 | canary weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 249 | outlier ejection | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 250 | health threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 251 | dns traffic weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 252 | session affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |
| 253 | request hedging | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 254 | fault injection gate | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 255 | service failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 1097 | load balancing policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |

### Telecom RAN & Edge Radio (12 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `ran` (a radio access network cell or site), reached through the RAN controller (O-RAN interfaces). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| AUDIT-0009 | ran connection admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| AUDIT-0010 | ran ue handover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0011 | ran cell traffic steering | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0012 | ran slice resource budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| AUDIT-0013 | ran prb allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0014 | ran scheduler weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0015 | ran tx power | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower | global |
| AUDIT-0016 | ran antenna tilt | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0017 | ran carrier enable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0018 | ran cell sleep | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0019 | ran du cu placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| AUDIT-0020 | ran fronthaul budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

### Workflow, Logistics & Fulfillment (15 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `workflow` (a workflow or pipeline engine), reached through the workflow engine's concurrency settings. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 417 | workflow admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 418 | workflow worker rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 419 | task queue rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 420 | workflow retry | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 421 | workflow backoff | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 422 | workflow timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 423 | inventory allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 424 | fulfillment route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 425 | warehouse queue | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 426 | carrier selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 427 | dispatch priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 428 | shipment batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 429 | route replan | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 430 | sla escalation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 431 | compensation action | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 40 decisions |

### Medical Imaging & Clinical Systems (12 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `clinical` (clinical systems: imaging archives, records, interface engines, monitoring gateways), reached through the application's own scaling and admission settings (Kubernetes, the vendor console). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2014 | pacs archive tier target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| 2015 | dicom router concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2016 | ehr application replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 2017 | hl7 interface queue limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2018 | fhir api rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2019 | reconstruction gpu workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| 2020 | modality worklist timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2021 | patient monitoring gateway capacity | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2022 | lab analyzer batch window | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2023 | telehealth session admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2024 | clinical backup window | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2025 | imaging prefetch priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

### Ports & Maritime Logistics (12 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `port` (a container terminal's cranes and vehicles taking moves), reached through the terminal operating system and fleet controllers. Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| 2080 | quay crane allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 2081 | yard crane fleet size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 2082 | berth window admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2083 | truck gate rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2084 | horizontal transport fleet size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 2085 | reefer plug power budget | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower | global |
| 2086 | shore power connection capacity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 2087 | rail mounted gantry dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 2088 | container dwell priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2089 | vessel arrival pacing | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| 2090 | stacking height target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| 2091 | equipment charging window | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

### Content Delivery & Edge Cache (6 muscles)

Each is a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; its class is `process` (an industrial process loop), reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Omni-Compass reads how far the process sits from its band. Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5039 | cdn cache ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5040 | edge cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| V5-5041 | origin shield concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| V5-5042 | prefetch aggressiveness | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5043 | tiered cache promotion | capacity | at its limit on native (the full actuator): read and left native | Distribution; stack; tower | global |
| V5-5044 | edge pop admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

### Financial Markets & Trading Systems (14 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `server` (an application service on servers or pods), reached through the Kubernetes API (HPA target and floor, pod resize). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5058 | matching engine threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5059 | order gateway sessions | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5060 | order admission rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| V5-5061 | pre trade risk check workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| V5-5062 | market data fanout threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 10 decisions |
| V5-5063 | market data conflation interval | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5064 | fix session heartbeat interval | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5065 | kernel bypass poll cores | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower | global |
| V5-5066 | tick store write batch | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5067 | post trade settlement workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 80% full; reads the last 20 decisions |
| V5-5068 | end of day risk batch power | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower | global |
| V5-5069 | colocation rack cooling setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Distribution; stack; tower | global |
| V5-5070 | backtest grid nodes | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5071 | surveillance alert queue workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |

### Reliability, Security & Recovery (6 muscles)

Each is a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; its class is `network` (network routing and switching), reached through the network controller (SDN, routing API). Omni-Compass reads how far its queue and its load sit toward the service line (queue or lateness, and load above half). Its home realm is Distribution / Specialized.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms | Its own card |
|---:|---|---|---|---|---|
| V5-5118 | ids capture threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | global |
| V5-5119 | ids ring buffer size | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower | global |
| V5-5120 | ids rule group admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |
| V5-5121 | waf inspection workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 70% full; reads the last 20 decisions |
| V5-5122 | siem ingest pipeline workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower | machines started at 80% full; reads the last 10 decisions |
| V5-5123 | endpoint scan scheduling | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower | global |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
