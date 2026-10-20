# The group of clusters: Omni-Compass on top of the clusters a group orchestrator governs, four ways (preregistration)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 20 October 2026, before any run of this test. It holds the governors on the founder's list of 19 October, night,
whose organism is not one cluster but several: Karmada (register row 95) first; Open Cluster Management (row 96) and Armada
(row 94) join it, each by an amendment written before its first run. Each runs the four ways of the founder's order of 20
October. This is the level "a group of clusters" of `docs/LEVELS.md`, measured live for the first time.

## The question

When a group orchestrator places a stream of batch jobs across a group of clusters, what does it do to the group on its own,
what does Omni-Compass do to the group without it, and does Omni-Compass on top of each member, under the orchestrator, make
the group's work faster or use fewer machines or less energy, with no LOSS anywhere?

## The organism: a group of two clusters

Two of the batch rig's clusters (each `deploy/kind/cluster-full.yaml`: one control plane and six workers, Kubernetes 1.35 on
kind v0.31.0), `omni-m1` and `omni-m2`, on one GitHub runner. Each member runs the batch rig's bench unchanged
(`scripts/kind_bench.sh`, `BATCH_QUEUE=group`): its service and probe, its metrics-server, its own default scheduler, its
capture, and, in the Omni-Compass arms, its own governor on the runner's last core (`docs/BATCH_QUEUE_PREREGISTRATION.md`,
amendment 5). The members open their measured windows together (`GROUP_BARRIER`), and the stream starts once both are open.

## The stream, the same work

The batch rig's stream unchanged: 24 jobs of 10 pods, 5 at a time, one job every 30 s, each pod hashing 3,000 MB
(`deploy/kind/batch-stream-job.yaml`), sent to the group (`scripts/kind_group_orch.sh`): to the orchestrator, which places
each job, or, on the group alone, by the harness to the members in turn (job 1 to `omni-m1`, job 2 to `omni-m2`, and so on),
the simplest placement a group without an orchestrator has.

## The arms: the four ways, all four in every repetition

- **nativebare**, the group alone: no orchestrator; the jobs go to the members in turn; Omni-Compass is not started.
- **native**, the orchestrator as its project ships it, on a one-node cluster of its own beside the members
  (`deploy/kind/cluster-host.yaml`), every job sent to it; Omni-Compass is not started.
- **compassbare**, Omni-Compass on top of each member of the group alone (one governor per member, each wired to its own
  cluster only, as on one cluster).
- **compass**, Omni-Compass on top of each member, the orchestrator on top of the group.

Each comparison is the first arm against the second, paired within the repetition, read by the one key for the first arm:
compass against native (Omni-Compass on top of the orchestrated group), native against nativebare (what the orchestrator does
on its own), compassbare against nativebare (what Omni-Compass does without it), compassbare against native, and compass
against nativebare. Omni-Compass never writes the orchestrator's objects and never sends, holds or places a job; in each member
it works the same levers as on one cluster, on top of what the orchestrator sends there.

## Karmada, frozen

- **Karmada v1.19.0** (`karmada-io/karmada`, the CNCF, Apache-2.0), installed as its own CLI installs it (`karmadactl init` on
  the orchestrator's cluster; its images `docker.io/karmada/*:v1.19.0` and the Kubernetes images it names, each recorded with
  its digest in `orch.txt`), from its release: `karmadactl-linux-amd64.tgz` (SHA-256
  `cf690eacc25ed13b6a27366c1b0b33e0e6edd2833e379922d420a5355550ef3d`) and `crds.tar.gz` (SHA-256
  `e8d225a910924432f90d0e0397890d7d94b5a444b32e4586343570feeeafe100`); a file that does not match its pin fails the arm.
- Both members joined in push mode (`karmadactl join`), by the address its pods reach them at; the arm waits until Karmada
  reports both Ready.
- **The operator's one setting**, a propagation policy for the stream (`deploy/kind/karmada-propagation.yaml`): every job may go
  to either member, divided among them by Karmada's Aggregated preference, which its documentation gives for work that should
  run on as few clusters as its available resources allow. Which member each job goes to, and how, is Karmada's.
- Its own record of every job (`orch_jobs.json`), where it placed each (`orch_end.json`) and its scheduler's and controller
  manager's last words are kept in every arm. Its certificates and the members' credentials stay outside the run's files.

## The measure, merged from the members

Every member's record is merged into the arm's own files (`tools/merge_group.py`), read by `tools/live_reps.py` as any arm:
the window opens when the stream starts and closes with the first member's window; every job once, submitted when it was sent
(to Karmada, or to its member) and done when every member's part of it is done (a part not done leaves its job unfinished at
the window's end); the members' machines in service, processors and modelled watts summed at each moment; every member's
probe, governor record and pod record. The gauges are the batch rig's: job wait (mean, 95th percentile), turnaround, jobs
unfinished, machines in service, energy, and every other gauge of the table, losses included, each with its paired 95%
interval. Ten repetitions a run, three runs (A, B and C) started together (`kind-group.yml`), each comparison's three-run table
by `tools/confirm_abc.py --pair`.

## Tried first

One repetition (`kind-group.yml`, label `trial`), never counted in any table, to see the group stand: both members' windows
open together, Karmada places the jobs, the records merge. A trial that shows a fault in the rig is fixed in the rig, and the
fix is written here as an amendment before the counted runs.

## Known limits, said before the result

- Two members of six workers each, fifteen kind nodes on one runner's four processors (three for the clusters, one for the
  governors): the group shares one machine, as every kind cluster here does; the work is the same in every arm.
- On the group alone the harness places the jobs in turn, without regard to how busy each member is; that is the group
  without an orchestrator, not a scheduler of the harness's own.
- Karmada's own cluster runs on the cluster cores in its two arms only; what it costs the group is part of "the orchestrator on
  its own".

## What it is not

A contest between Omni-Compass and the orchestrator for the same job: Omni-Compass places no job and writes nothing of the
orchestrator's; on the group alone it sits on top of each member's own scheduler, under the orchestrator on top of the same.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
