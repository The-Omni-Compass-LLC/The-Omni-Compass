# Omni v19: the immune system, so native stays wherever Omni-Compass cannot beat it

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Omni v19 (`OMNI_V19.json`) stands on main from 25 October. The founder's orders of 24 and 25 October: "There's no reason that I
could have a loss if you were supposed to know that if OmniCompass can't beat the native, the native stays. Even in the cloud
... erase the negative or bring positive or at least bring steady stableness in the cloud"; and "let the math do what it's coded
to do and force and pull and push and physics inside the system". omni-v19 is omni-v18 with four rules added to the Kubernetes
governor (`omni_controller/controller.py`), each one part of the engine's immune system, and the words of two engine files
brought to the founder's order of 24 October (`omni_controller/muscles.py`, `omnicompass/nervous.py`: our models are models, a
test's stand-in is a stand-in) and one runner's help text to the ladder of 25 October (`tools/run_kil.py`: 1, 10, 100 and 500
copies). Every other file is omni-v18's bytes.

## The four rules, in plain words

| Term | What it is | Where it acts |
|---|---|---|
| **A pod waiting** | A pod the cluster cannot place: it has no machine with room for it. Time waited is harm, a LOSS by the one key. | read by the fast check every 5 s |
| **The immune hand-back** | The moment a pod waits while Omni-Compass holds a pod autoscaler's target below the operator's own (more pods than native would ask), that target goes back to native's at once, from the fast check, not the next decision, and is held there: 10 minutes the first time, doubled for each hand-back in a row up to two hours, halved again after a quiet hold. | the pod autoscaler's target |
| **The immune memory** | Omni-Compass remembers the largest rise it has seen inside two decisions (about the time a new machine takes to boot): in the requests on the machines, and in each service's demand. It keeps room for that rise. A machine is given back only when the machines left hold the requests plus a reserve of the larger of one machine and that rise; extra pods are asked for only as far as the machines can still place that rise times themselves. | the machines given back; the pods asked for |
| **Native's line** | A machine is given back only while the machines left stay at or under native's own autoscaler's line (the Cluster Autoscaler's scale-down utilization threshold, 0.5 by its documented default, `--native-release-util`), so Omni-Compass never leaves the machines thinner than native would; and every decision, while machines stand given back, a machine comes back the moment that line or the reserve is crossed. | the machines given back |
| **Immune maturity** | No give-back trial before the governor has watched its organism for one recheck period (two hours at the factory tune), so the immune memory has seen the organism's own rises before the first machine is given back. | the verdict's first trial |
| **The step back** | A pod that waited between two decisions counts as harm at the next decision: the service is not calm, and a give-back depth the verdict had allowed steps back by one, not tried again until the recheck has passed (Omni direct's own immune reaction, `omni_orchestrator/control.py`). | the verdict's allowed depth |

The mechanism is the engine's own: nothing is tuned to make a row read well. Each rule answers a fault found in the model's own
files: pods waiting for a place while Omni-Compass held more pods than the machines could place; a machine given back while the
rest were 84% booked, then a rise of 30% inside one reading; native's own autoscaler removing a machine while Omni-Compass
still held one back.

## What the model gate read (our own models, evidence class S)

The model gate against omni-v18 (`results/model_gate/V19_VS_V18.md`, eight seeds, every model): no LOSS against omni-v18 in
any model. In the cloud's models (the machines alone) pods waiting fall by 13% against omni-v18, a GAIN, and the candidate is
identical to native on every gauge; the conveyance and card models and the verdict read identical to omni-v18.

The pace models (`results/model_gate/V19_PACE.md`, the plant that moves every 5 s, a decision every 60 s), against native:

| Setting | Gauge | omni-v18 against native | omni-v19 against native |
|---|---|---|---|
| on-site (the kind setting) | pods waiting for a place | up 127.8%, more waiting, LOSS | down 5.2%, fewer waiting, GAIN |
| on-site | the 95th percentile | down 15.6%, faster, GAIN | down 6.9%, faster, GAIN |
| on-site | alert minutes | down 57.4%, GAIN | down 27.3%, GAIN |
| on-site | machine-hours | up 23.5%, power given | up 7.7%, power given |
| cloud (the machines alone) | pods waiting for a place | up 6.2%, LOSS | the same as native, EVEN |
| cloud | every other gauge | EVEN or GAIN | the same as native, EVEN |

The trade, said plainly: against omni-v18 the on-site 95th percentile and alert minutes give back part of their GAIN (omni-v18
bought them with pods that waited for a place); against native both still read GAIN, and the one LOSS against native in that
setting, the pods waiting, is gone. The founder's order of 24 October (native stays wherever Omni-Compass cannot beat it) rules
the trade.

Still on the next version's list, LOSS against native in the models and the same in omni-v18 (not caused by this version): the
pod start wait in the conveyance models (up 9%), the card's 95th and 99th percentiles (up 0.9% to 5.8%), the batch's requests
served (down 2.1%).

The self-pilot (`tests/test_selfpilot.py`: the shipped governor sizing the machines for a day against the HPA and the Cluster
Autoscaler on the same traffic) reads the same trade: pods waiting down 100% (none waited, GAIN), the HPA's shortfall EVEN,
machine-hours per core-hour up 18.3% and energy per core-hour up 11.4% (power given). Native's line here is read over the
machines left as a whole, where the Cluster Autoscaler reads each machine's own share against its 0.5, so the governor holds
more machines than native would: power given, never a LOSS by the one key. Reading the line machine by machine, as the
Cluster Autoscaler does, is on the next version's list, through the model gate.

The orchestrators on the same organisms (`results/orchestrators/ORCHESTRATORS.md`, our own models) read two more for that list,
the same on top of every orchestrator but Koordinator: where the batch stream runs beside the service on the kind rig's one host,
the service fails requests in every arm and the breach reflex lowers its autoscaler's target, so more serving pods take the
processor from the batch (requests failed down 6.5%, GAIN; a job's turnaround up 9.3% and the stream's makespan up 2.0%, LOSS); and
in the cloud, beside Volcano, a job's turnaround up 0.7% with a machine marked idle.

## Every benchmark runs again

Every benchmark runs again on omni-v19 from the moment it reached main; nothing is read across engines.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
