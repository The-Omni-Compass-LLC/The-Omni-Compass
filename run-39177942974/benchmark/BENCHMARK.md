# Omni-Compass benchmark: Kubernetes native vs Kubernetes + Omni-Compass

Two identical kind clusters (1 control plane + 6 workers), same add-ons, workload (php-apache + HPA, target 50),
load schedule and capture. **Native**: Omni-Compass not running. **Omni**: Omni-Compass drives the HPA target, the
node pool (cordon/drain/uncordon), the power cap (in-place CPU limits on the app pods, enforced by the kernel), heat
(harness law on live power), security (hold signal) and the rollout guard. Response times are real HTTP requests timed
every 5 s. Power is a declared model (idle 100 W + 150 W x utilisation per worker in service; parked workers on
standby at idle power), not a meter.

## Gauges

| Gauge | Native | Omni-Compass | Change |
|---|---:|---:|---:|
| duration (min) | 20.15 | 20.27 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.03 | +0.6% |
| power (W), mean | 630 | 642 | +2.0% |
| power (W), peak | 652 | 692 | +6.0% |
| energy (Wh) | 211 | 217 | +2.6% |
| energy, parked workers still on at idle power (Wh) | 211 | 217 | +2.6% |
| CPU used (cores), mean | 0.910 | 1.24 | +36.2% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.052 | +36.2% |
| energy per core-hour (Wh) | 692 | 518 | -25.1% |
| node-hours per core-hour | 6.60 | 4.84 | -26.6% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.13 | 9.32 | +2.0% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.517 | -3.1% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 1.15 | 0.000 | -100.0% |
| response time (ms), mean | 156 | 98.04 | -37.1% |
| response time (ms), median | 128 | 84.90 | -33.4% |
| response time (ms), 95th percentile | 321 | 158 | -50.7% |
| response time (ms), 99th percentile | 524 | 192 | -63.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.1986 | 5.5525 | -22.9% | [-3.3118, -0.0204] | GAIN |
| kwh_per_core_hour | 0.7521 | 0.5887 | -21.7% | [-0.3205, -0.0012] | GAIN |
| utilisation | 0.0374 | 0.0508 | +35.7% | [+0.0008, +0.0272] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5299 | 1.4877 | -2.8% | [-2.3762, +2.2496] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.445 0.468 0.487 0.505 0.52 0.534 0.546 0.556 0.562 0.567 0.571 0.577 0.581 0.585 0.588 0.59 0.591
- nodes decided per minute: 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
- HPA target decided per minute (%): 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77

## Reset

```
restored target: 50
workers in service: 6 of 6
Omni records left after kill: none
```

## Minute by minute

| min | nodes native | nodes omni | power W native | power W omni | replicas native | replicas omni | pending native | pending omni | CPU native | CPU omni |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.00 | 6.00 | 617 | 621 | 6.00 | 5.25 | 0.000 | 0.000 | 0.575 | 0.683 |
| 1 | 6.00 | 6.00 | 620 | 622 | 6.00 | 6.00 | 0.000 | 0.000 | 0.657 | 0.705 |
| 2 | 6.00 | 6.00 | 620 | 628 | 6.00 | 7.00 | 0.000 | 0.000 | 0.652 | 0.872 |
| 3 | 6.00 | 6.00 | 623 | 636 | 6.00 | 8.50 | 0.000 | 0.000 | 0.716 | 1.07 |
| 4 | 6.00 | 6.00 | 635 | 650 | 9.25 | 10.00 | 0.000 | 0.000 | 1.05 | 1.43 |
| 5 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.35 |
| 6 | 6.00 | 6.00 | 634 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.47 |
| 7 | 6.00 | 6.00 | 647 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 2.00 |
| 8 | 6.00 | 6.00 | 646 | 680 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.24 |
| 9 | 6.00 | 6.00 | 650 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.45 | 1.97 |
| 10 | 6.00 | 6.00 | 646 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 1.96 |
| 11 | 6.00 | 6.00 | 616 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.565 | 0.739 |
| 12 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.659 | 0.746 |
| 13 | 6.00 | 6.00 | 625 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.777 | 0.879 |
| 14 | 6.00 | 6.00 | 635 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.46 |
| 15 | 6.00 | 6.00 | 632 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.974 | 1.37 |
| 16 | 6.00 | 6.00 | 634 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.55 |
| 17 | 6.00 | 6.00 | 630 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.912 | 0.992 |
| 18 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.589 | 0.789 |
| 19 | 6.00 | 6.00 | 619 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.622 | 0.734 |
| 20 |  | 6.00 |  | 626 |  | 10.00 |  | 0.000 |  | 0.805 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
