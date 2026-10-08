# Preregistration: the real Kubernetes cluster under a public demand trace (written before the runs, 2026-10-08)

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Any commercial use requires a signed,
> paid Omni-Compass Enterprise License. See [`LICENSE`](../LICENSE) and [`NOTICE`](../NOTICE). Patents, copyrights and
> trademarks filed in the USA.

## Why this test

Every Kubernetes test so far (`docs/K8S_COMPASS_PREREGISTRATION.md`: steady, wandering, all four, faults, batch,
fairness) drives the real cluster with a load schedule of our own: steps we wrote, one change at a time. A referee may
ask whether the shape of our own schedules suits the governor. This test keeps everything else of the wandering test and
replaces only the shape of the demand with one somebody else measured and published: a day of a real cluster's job
submissions, turned into a load schedule by a rule written here before any run. Register row 17, proof-program row 4.

## What is someone else's

- **The cluster and its native controller:** Kubernetes with its Horizontal Pod Autoscaler at the operator's target
  (50%), exactly as in the six tests; kind, six workers, fresh per arm; the floor of two machines, every machine usable.
- **The demand trace:** the **Google cluster-usage traces 2011** (`clusterdata-2011-2`, published by Google, public bucket
  `clusterdata-2011-2` on Google Cloud Storage), table `job_events`: the number of jobs **submitted** (event type 0) in each
  hour of the trace's first day. The trace starts at 600 s; events stamped 0 are jobs that existed before it and are not
  counted. 18 parts of the table (`part-00000` to `part-00017`) cover the day; each is named with its SHA-256 in the
  receipt. It is a batch cluster's job arrivals, not a web service's requests; what we take from it is the **shape** of a
  day's demand, measured by someone else, nothing more.
- **The rule that turns counts into load** (the organism runs' rule, `docs/K8S_COMPASS_PREREGISTRATION.md`, "the real
  cluster as one more muscle"): the 24 hourly counts are placed on the load generator's range by min and max,
  `r_raw(k) = 1 + round(7 (c_k - min c) / (max c - min c))`, 1 to 8 generators (the wandering test's range), rounding half
  up. Then the founder's rule for real traffic (the amendment to the wandering test, 2026-10-04): the schedule moves **one
  step a bin toward the trace's level, never skipping**, starting at the first bin's own level. Each bin is one step of
  **108 s** (the wandering test's step): 24 steps, **2,592 measured seconds**, a day in 43 minutes.

## The schedule, derived and committed before the runs

`tools/trace_schedule.py --out results/traces/google2011` (18 October 2011-trace parts, re-derivable by anyone; the tool and
its rule are tested without the network in `tests/test_trace_schedule.py`, run by `verify.py`). The receipt is
`results/traces/google2011/schedule.json`; the line the workflow takes is `results/traces/google2011/LOAD_STEPS.txt`:

| Hour | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| jobs submitted | 635 | 745 | 742 | 816 | 784 | 1232 | 898 | 764 | 529 | 643 | 683 | 617 | 681 | 795 | 598 | 853 | 882 | 917 | 834 | 1043 | 1039 | 1397 | 884 | 741 |
| level (min-max, 1 to 8) | 2 | 3 | 3 | 3 | 3 | 7 | 4 | 3 | 1 | 2 | 2 | 2 | 2 | 3 | 2 | 4 | 4 | 4 | 3 | 5 | 5 | 8 | 4 | 3 |
| **load generators (one step a bin)** | **2** | **3** | **3** | **3** | **3** | **4** | **4** | **3** | **2** | **2** | **2** | **2** | **2** | **3** | **2** | **3** | **4** | **4** | **3** | **4** | **5** | **6** | **5** | **4** |

`load_steps` = `2 3 3 3 3 4 4 3 2 2 2 2 2 3 2 3 4 4 3 4 5 6 5 4`. Said plainly: the one-step rule reaches the trace's two
sharp hours late (hour 5's level 7 becomes a step to 4, hour 21's level 8 a step to 6), so the replayed day is the trace's
shape with its two spikes blunted to the rate real traffic is allowed to move in this harness; the raw levels stand beside
the steps in the receipt. Nothing in this table was changed after the runs were dispatched.

## Arms, runs and gauges (the wandering test's, unchanged)

- **Workflow** `benchmark-reps`: ten paired repetitions, arms `native compass` in rotated order, a fresh six-worker kind
  cluster per arm, open-loop load (`loadgen=open`, the same work in every arm), `duration_s` 2592, `load_steps` as above,
  the HPA's replica cap as the operator set it (no `replica_ceiling`), floor two, every machine usable. Three separate
  dispatches on one commit are runs A, B and C.
- **Gauges**, native + Omni against native, paired with the 95% interval and read in words: time over the 500 ms line,
  failed requests, p95 and p99 response time, worker machines in service, energy (the declared model; on kind it is not a
  meter), CPU with Omni's own, pods started. No capacity is read (the load does not only rise).
- **Readings**: the three-run rule (`tools/confirm_abc.py`): confirmed better or confirmed WORSE when all three runs move
  the same way with every interval clear of zero; no difference beyond the noise when a run's interval includes zero (with
  the count of such runs); the runs disagree when clear runs point different ways. Every row shown, losses included.
- **Table**: written beside the six tests' tables in `results/live/`, named for the trace (V3_TRACE_GOOGLE2011). The test enters the Omni index's Kubernetes category beside the six
  (`tools/omni_index.py`, SOURCES), with the same measures as the wandering test, when its table lands.
- **No tuning case.** Nothing is fitted: the law, the gates, the HPA target, the floor, the line, the probe and the step
  length are the wandering test's; the only new thing is the shape of the demand, and it is someone else's.
- **Engine**: Omni v3, checked on every run by `tools/omni_version.py --commit`.
- **Cost**: free (GitHub's runners); about 1 h 40 min a run, the ten repetitions in parallel.

## What a referee should ask, and the answers given before the result

- *Is a batch cluster's job arrival a fair stand-in for a web service's demand?* It is a real day's demand shape measured
  by someone else, which is what this test is for; it is not the same service, and the result is read as "under a
  published day-shape", not as "under Google's load". The Azure Functions invocation trace, a request-driven shape, is
  the next trace in row 17 and follows the same rule.
- *Does blunting the spikes favour the governor?* It blunts them for both arms equally, and the one-step rule is the
  rule every real-traffic test here has run under since 4 October; a schedule with the raw levels would be a different,
  also legitimate, test, and the receipt holds the raw levels so a reader can run it.
- *Why a day in 43 minutes?* Because the wandering test's step is 108 s and its runs fit a GitHub job; the compression
  is the same for both arms, and the step length is the one every reading in this harness has been taken at.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. Patents, copyrights and trademarks filed in the USA.
