# Omni v5 — the engine fingerprint

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

**omni-v5** is a distinct engine, its own tree, no longer read as v3. It is fingerprinted file by file in `OMNI_V5.json`
(`tools/omni_version.py`); `python3 tools/omni_version.py` prints `omni-v5` on this checkout. v1, v2 and v3 stay frozen,
each kept for its own results; no result is ever read across versions.

## What v5 is

v5 is **a combination of everything**: it takes v3's proven engine (its live controllers, its realms and organisms, its
runners) and adds the **v5 compass law** (`realms/compass_arm_v5.py`) and its arm in the harness (`realms/harness.py`). The
goal is to be equal to or better than native and every prior version on every measure, and never worse on any — *do no
harm*.

The v5 muscle catalog (`realms/catalog_v5.csv`) is **1,097 muscles in 70 families** — v3's 945, then a first wave of six
new families of real control points: **Linux Kernel & OS Control** (cgroups, the CFS scheduler, DVFS/cpufreq, transparent
hugepages, the I/O scheduler, NUMA balancing, dirty-ratio writeback, swappiness, TCP buffers, …), **Serverless & Functions
(FaaS)**, **Virtualization & Hypervisor**, **Content Delivery & Edge Cache**, **Gut** (data-plane intake and waste), and
**Skin** (perimeter and admission); then a second wave (12 October) of 95 muscles: five new families, **Financial Markets
& Trading Systems** (matching engines, order gateways, pre-trade risk, market-data fan-out), **Media Streaming & CDN**
(transcoders, packagers, origin shields, player buffers), **Game Servers & Real-Time Interactive** (Agones fleets, tick
rates, matchmaking, relays), **Blockchain & Ledger Nodes** (a node's cache, mempool, peers and validation threads; never a
consensus rule) and **CI/CD & Build Farms** (runner scale sets, build concurrency, caches, test shards), plus additions to
seven families already there: security engines (an intrusion-detection system's capture threads and ring buffer, a web
firewall's inspection workers, a SIEM's ingest), MQTT brokers, DNS and mail caches, ROS 2 executors, humanoids and
manipulators, warehouse robot fleets, PX4 and ArduPilot drones and swarm spacing, and edge sites. The GPU family is named
for the hardware, not one vendor (**GPU Hardware**), and the eight audited families carry numbers (64 to 71) like every
other family. Each is a distinct real-world knob, modelled on the matching plant template, exactly as v3's 945 already
share five templates. The organisms on v5: Compute / AI / Cloud 530, Physics / Robotics / Autonomous 394, Energy /
Facility / Industrial 470, Distribution / Specialized 474, the four stacked 1,868, the whole tower 1,097; the spine all
four realms share is 257. (v3's own catalog `realms/catalog.csv` stays 945, frozen for v3's results.)

Two math-only guardrails, and otherwise free arms:

- **The edge** — a per-knob cushion that widens at once when service climbs and narrows slowly when it falls
  (`cushion = climb × reaction + z × wobble`), so nothing riding its own limit falls off.
- **The centre / the hole** — nothing is eased into a pit it cannot climb out of. A cooled zone is eased only by the
  degrees its cooling can still recover (the Lindley reach), and not at all while its cooling headroom is falling toward
  empty faster than the cooling can answer. A process loop's setpoint never sits closer to its band's edge than the
  loop's own largest swing toward that edge (the loop reach, read from the historian's low and high over each decision,
  carried ahead for a slow loop). A serving pool is never capped below the largest jump in demand it has shown (the drop
  floor) nor so far that a burst would push its responses over the line where native's would not (the latency floor).
  And nothing permanent: a machine handed back to a cloud is the cluster autoscaler's own decision, because the
  autoscaler shrinks from wherever it is left, so an early hand-back would leave the pool a machine short of native for
  good; and a motion axis is slowed only while the wake forecast over a whole deadline (the most that can arrive in one
  deadline at the recent peak rate) still finishes inside that deadline at the slowed speed, so a delay is always
  recovered before a later rush could make it permanent. When work comes, every muscle wakes straight to the level the
  work needs (the founder's rule: from idle straight to 99, never past 100).

Every other knob is free to move both ways inside its physical cover, generating units included (a unit's steam,
speed or gate loop eased inside its band serves the same load with less effort), and **a knob stays native only where its
own physics says moving it cannot help without harm**: an interactive pool's power cap (its response line is shorter
than one decision, so a cap's one decision of slower service cannot be seen and undone inside the line; the metered GPU,
class P, is where that cap is proven), a battery's peak-shave (round-trip energy bought for service), and a cloud pool's
machine hand-back. A batch queue's, a training job's or a terminal's power cap is free under the drop and latency floors.

**Amendment, 12 October.** The first v5 table (commit `c0e80a852`, the whole tower +0.0%) ran an engine that held every
generating unit's loop, every power cap and every inverter native by blanket gates. The gate on generating units alone
threw away almost all of what v5 saves: on the tower, 1.09% with it off against 0.04% with it on, on development seeds.
v5 was re-declared with the gates replaced by the physics floors above, developed on seeds 7100-7209 only, and the
preregistered seeds 3000-3009 were run again unchanged.

**Amendment 2, 12 October.** The catalog's second wave (95 muscles, five new families and additions to seven) took it to
1,097 muscles in 70 families; the engine's law is unchanged, its fingerprint re-declared because the catalog is part of
it. Developed on seeds 7100-7109 only (0 of 1,097 worse, all six organisms superior); the preregistered seeds 3000-3009
were run again unchanged on commit `04d9eb3b3`, with the same savings on the whole tower, the four stacked and Energy /
Facility (3.0 times v3's).

## The no-harm proof (modelled, class S)

On a fixed seed, for **every** muscle in the catalog, the v5 default uses no more energy than native, does no less work,
and is in violation no more often; it hands every knob back to native on the kill (the dead-man lease); and it acts where
it helps. The whole tower is no worse than native on energy and work. On the preregistered seeds the whole tower saves 0.99% of its energy against v3's 0.33% on the same seeds (3.0 times), the four stacked 0.99% against 0.33% (3.0 times), Energy / Facility 1.00% against 0.33% (3.0 times), all six
organisms superior within guardrails, 0 of 1,097 muscles worse than native. Inside the organisms v5 leaves 1 to 3 plants per organism (8 in the four stacked, which are the four realms together) one decision over their line in one of the ten seeds, all of them UPS or power-distribution plants it never touches (the body's power swing reaches them), against v3's 13 to 35 (83 in the four stacked). Seven of the eight come in the decisions right after the safety cutoff, when every knob is handed back to native at once and the body pays back what Omni saved (warmer rooms cool back down, eased loops return); one comes while Omni runs (a UPS line 40 W over its 211,436 W limit, where native sat 9 W under it, as a computer pool caught up on held work). A strict guard on the body's shared power lines removes them, but on development seeds it also removes almost all of the saving in a body whose UPS lines run at their limit (Compute / AI / Cloud 0.47% to 0.01%; native itself is over those lines in 4% to 15% of decisions); that trade is held for the founder's decision. This is checked in
`tests/test_compass_arm_v5.py` and run in full by `tools/run_realms_v5.py` (`results/realms_v5/`). Models are class S: a
model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test.

## In development

While v5 is in active development its fingerprint is **re-declared on each engine change** (`python3 tools/omni_version.py
--write v5`), and **no v5 result is published** until the v5 freeze. At the freeze, every benchmark is rerun on v5, A/B/C,
the founder hears each result before it goes up, and the fingerprint is final.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
