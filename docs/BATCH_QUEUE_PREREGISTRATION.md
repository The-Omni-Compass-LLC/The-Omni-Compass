# Kueue and Volcano: Omni-Compass on top of a batch stream admitted by a queueing system of its own (preregistration)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on the night of 19 October 2026, before any run of this test, at the founder's order of that night: the governors
and orchestrators he named (Kueue, Volcano, Crane, Open Cluster Management, CruiseKube, Gödel, Armada, Karmada, the
Kubernetes scheduler as shipped, the KAI scheduler, Nephio, KubeEdge, KubeRay, and Koordinator) are each benchmarked with
the organism native under them, then Omni-Compass on top of them. This page is the first two, register row 63. Every
other Kubernetes set stays as it is; this is a new set beside them, on the engine that stands at the run's commit
(`python3 tools/omni_version.py`, recorded in every run).

## The question

When a stream of batch jobs is admitted by Kueue (Kubernetes SIG Scheduling; Apache-2.0) or placed by Volcano (the CNCF;
Apache-2.0), each as its project ships it, does Omni-Compass on top shorten the jobs' wait and turnaround, or hold fewer
machines or less energy, with no LOSS anywhere?

## What Kueue and Volcano are, and so what native is

- **Kueue** admits work a whole job at a time. A job carrying a queue's name is created suspended; Kueue admits it when its
  ClusterQueue has quota for every pod it asks for, and the Kubernetes scheduler then places the pods. Native is Kueue's
  release applied as published, with the operator's queue written as Kueue's own single-ClusterQueue example writes it:
  one ResourceFlavor, one ClusterQueue whose nominal quota is the workers' allocatable CPU and memory, read live from the
  cluster before the arms are told apart, and one LocalQueue in the namespace the jobs run in.
- **Volcano** is a batch scheduler of its own. Pods that name it (`schedulerName: volcano`) are grouped by its controllers
  and placed by its scheduler according to its queues, with its default queue and its default scheduling policy as
  shipped. Native is Volcano's release applied as published.
- In both arms the rest of the cluster is the batch test's (`docs/K8S_COMPASS_PREREGISTRATION.md`, amendment 8): six
  workers, the service and its autoscaler (HPA target 50) beside the jobs, the service's load generator at zero.

## The arms (two, as always)

- **native**: Kubernetes with the queueing system; Omni-Compass is not started.
- **omni**: the same cluster and the same queueing system with Omni-Compass on top (`ARM=compass`), with the live muscles
  of the batch test: the node pool (a worker idled with the prefer-not mark, a pod that finds the open workers full lands
  on it at once, and nothing is evicted or moved), the service's autoscaler target and CPU limit, the rollout guard and
  the security hold, cruise (rule 7) and idle (rule 8). Omni-Compass writes nothing to Kueue's or Volcano's objects or to
  the jobs: its identity can read jobs and cannot write them, and has no rule at all for either project's resources
  (`deploy/kind/rbac-omni.yaml`; the `kubectl auth can-i` receipts in every run's `rbac_omni.txt`).

## The queueing systems, frozen

- Kueue **v0.20.2** (`manifests.yaml` from the release, SHA-256 `1ab14ecd590575ac57f50fa4cbcf529766bc2c32ba974bda1614381281ec52b4`)
  and Volcano **v1.16.0** (`installer/volcano-development.yaml` at the tag, SHA-256
  `9aa62e15541f5e955d73353da9321ab233a2cbe0f8fbac4b4a4d38ba497303ee`), fetched in every arm and refused unless the hash
  matches; kind v0.31.0 with Kubernetes v1.35.0, as every set.
- The release file is applied as published but for one thing, the same in both arms: every Deployment and Job of the
  queueing system is placed on the control plane, beside metrics-server and CoreDNS, before the file is applied, so the
  six measured workers carry only the work (Volcano's certificate Job ships with no placement). The run checks every pod
  of the queueing system is on the control plane (`scripts/kind_batch_queue.sh`).
- The stream's image (busybox 1.36) is pulled onto every worker before the arm begins and the puller removed before the
  window opens, as the served image is (`deploy/kind/prepull.yaml`), so a job's wait is the queueing system's and the
  scheduler's, never a download on the one machine all kind nodes share.
- `batch_queue.txt` records the release, the hash, the quota and every image the queueing system runs.

## The workload and the measure

- The stream (`deploy/kind/batch-stream-job.yaml`): 24 Jobs, one every 30 s from the window's opening, the same schedule
  in every arm; each Job runs 10 pods, 5 at a time, each pod hashing 3,000 MB (requests 500m CPU and 64 Mi, limit one
  CPU). The total is the batch test's: 240 pods of 3,000 MB.
- The six-worker kind cluster, a fresh cluster per arm, both arms back to back on the same runner in an order rotated by
  repetition; 120 s warm-up, 1,500 s measured; ten paired repetitions a run (`benchmark-reps.yml`, `workload=batch`,
  `batch_queue=kueue` or `volcano`).
- The four queue gauges (`tools/live_reps.py`, `job_stream`), each judged by its aim, a fall a GAIN:
  - a job's wait, from its submission to its first pod running, mean and 95th percentile (the queueing system's
    admission and the scheduler's placement together: the same measure for Kueue, which holds the job, and Volcano, which
    holds its pods);
  - a job's turnaround, from its submission to its last pod done, mean;
  - the jobs unfinished at the window's end.
  A job not started or not done by the window's end counts the window's end, never less.
- Beside them, every gauge of `tools/live_reps.py`, losses included: when the last job finished, the worker machines in
  service after it, machines in service and energy over the window, CPU with Omni-Compass's own, pods started, the
  service's response times.

## How it is read

- Each gauge's paired mean difference with its 95% interval: one whose interval is clear of zero is a difference in this
  run; one whose interval includes zero is no difference beyond the noise, and that is the result.
- One run (A) is a first reading. Runs B and C on the same commit make the three-run reading (`tools/confirm_abc.py`):
  GAIN or LOSS in all three of our runs, judged by what the gauge is for (a resource spent that rose reads power given), no
  difference beyond the noise, or the runs disagree.
- Wait, turnaround and response times are class L (measured on live software); machines are counted live; the watts are
  the declared model (class S), as in every kind set.
- A run is invalid, kept in the raw files and not counted, when a release file does not match its hash, a pod of the
  queueing system is off the control plane, Kueue refuses the operator's queue, Volcano's default queue never appears, the
  image is not on every worker, or a reset does not hand back the operator's settings.

## Known limits, said before the result

- No accelerators: GitHub's machines have none. The first plan for row 63 named KWOK-simulated accelerators, but a KWOK
  node runs no pod, so a job's wait there would measure no real work. This test runs real CPU work; the accelerators wait
  for a machine with cards (the GPU kit on Lambda, after the CPU side).
- Kueue holds a job whole and suspended until it is admitted, so its waiting work is invisible to anything that reads
  pods; Omni-Compass reads pods and never Kueue's own objects. Volcano holds pods, which wait Pending where the governor
  sees them. The difference is the systems', and the receipts show what each arm did with it.
- Kueue's quota is the workers' allocatable resources as kind reports them (each kind node reports the runner's
  processors), the same in both arms; on kind there is no node autoscaler for native, so native keeps all six workers.
- The other orchestrators of the founder's list take this rig one at a time, each with its own page before its runs
  (register rows 88 to 98).

## Amendment 1: the KAI scheduler (written before its first run, 20 October 2026)

The KAI scheduler (`NVIDIA/KAI-Scheduler`, NVIDIA, from Run:ai; Apache-2.0; register row 91) joins the rig as a third
queueing system (`batch_queue=kai`). It places pods by its own queues: a pod that names it (`schedulerName:
kai-scheduler`) and carries a queue's label (`kai.scheduler/queue`) is grouped with its job's other pods and placed by
KAI's scheduler under the queue's quota, limit and over-quota weight.

- **Native** is KAI's chart as published, installed by Helm, with the two default queues its chart makes on install
  (`default-parent-queue` and `default-queue`: quota 0, no limit, over-quota weight 1). The jobs go to `default-queue`.
- **Frozen**: the chart `oci://ghcr.io/kai-scheduler/kai-scheduler/kai-scheduler` at v0.18.6 (released 15 October 2026),
  its archive's SHA-256 `dff53248c4a044249a1f62ca8d35bd8dfc02719b99e302b35c69f946f4c5b7ff` pinned and refused otherwise.
- **Placement**: the chart's own setting places KAI's components (its operator applies it to the scheduler, the binder,
  the pod grouper, the queue and pod-group controllers and the admission webhook): every one on the control plane
  (`deploy/kind/kai-values.yaml`); any deployment the setting does not reach is placed there after install; the run checks
  every serving pod of KAI is on the control plane.
- **What it is not**: KAI's GPU sharing and topology placement need cards; this test is its queues and gang placement on
  CPU work. The cards wait for the GPU kit on Lambda.

- **Its runs**: in a workflow of its own (`kind-orchestrators.yml`, the same rig), whose A, B and C are started together,
  so they never take the place of a campaign run of `benchmark-reps.yml` (`scripts/reruns.txt` reads runs back by their
  count in a workflow).

Everything else is as written above: the stream, the window, the gauges and how they are read.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
