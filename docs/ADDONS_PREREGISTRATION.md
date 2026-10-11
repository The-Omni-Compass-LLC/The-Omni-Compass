# The add-on test: Omni-Compass on top of Kubernetes with its add-ons (preregistration)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Declared on 10 October 2026, before any run of this test. Ordered by the founder the same day: native must be the
setup clusters actually run, with its add-ons, not bare Kubernetes, and Omni-Compass must show what it adds on top of
that. Every earlier Kubernetes set stays as it is; this is a new set beside them.

## The question

With KEDA, the event-driven autoscaler most clusters add to Kubernetes, and its HTTP add-on owning the service's
autoscaler, does Omni-Compass on top still make the service faster, use fewer machines or less energy, without making
anything worse?

## The arms (two, as always)

- **native**: Kubernetes with the add-ons below, nothing else. Omni-Compass is not started.
- **omni**: the same cluster and add-ons, with Omni-Compass on top: engine omni-v3 unchanged (`python3 tools/omni_version.py`),
  the compass law (`ARM=compass`), every live muscle as in the v3 Kubernetes sets. Its moves on the service's autoscaler
  reach KEDA's ScaledObject through the plug (`scripts/kubectl_keda.py`), because KEDA rebuilds the HPA from the
  ScaledObject and would undo a move written to the HPA itself (one writer per knob). The plug carries a move exactly or
  refuses it; a run in which any move did not reach KEDA whole is invalid.

## The add-ons, frozen

- metrics-server v0.9.0 (as every set), KEDA **2.21.0** and the KEDA HTTP add-on **0.16.0** from their release manifests,
  SHA-256 pinned (`scripts/kind_addons.sh`), every KEDA pod on the control plane.
- Two native setups, each its own set of paired runs:
  - **both**: KEDA scales php-apache on the HPA's own CPU target (50% of request, as `deploy/kind/demo.yaml`) and on the
    add-on's live requests in flight (target 1 per pod: one request fills a pod's 500m limit), whichever asks for more.
  - **http**: KEDA scales on the live requests in flight alone, as the add-on is set up for a web service.
- Replica range 1 to 10, the HPA's default behaviour, the interceptor at one replica (its own autoscaler, 200 requests
  waiting per replica, would hold one at this load).
- The load and the probe both enter through the add-on's interceptor (catch-all route to php-apache).

## The workload and the measure

As `benchmark-reps`: the six-worker kind cluster, a fresh cluster per arm, both arms back to back on the same runner in an
order rotated by repetition; the closed-loop load generator stepping 1 2 3 1 2 1; 120 s warm-up, 900 s measured; ten
paired repetitions per setup (run A). Every gauge of `tools/live_reps.py` is reported, losses included, with the paired
mean difference and its 95% interval.

## How it is read

- A gauge whose 95% interval of the paired difference is clear of zero is a difference in this run; one whose interval
  includes zero is no difference beyond the noise, and that is the result.
- One run (A) is a first reading. A confirmed reading needs runs B and C on the same commit (`tools/confirm_abc.py`):
  confirmed better or worse, no difference beyond the noise, or the runs disagree.
- Response times are class L (measured on live software). Machines in service are counted live; the watts are the
  declared model (class S), as in every kind set.

## Known limits, said before the result

- On kind there is no node autoscaler for native (no cloud to add or remove machines), so native keeps all six workers
  in service; Omni-Compass's machine and energy gauges are measured against that. A node autoscaler (Cluster Autoscaler
  or Karpenter, as on the Azure set) is the next add-on test.
- The interceptor adds one hop to every request in both arms.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
