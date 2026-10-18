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
| duration (min) | 20.17 | 20.23 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.3% |
| power (W), mean | 629 | 643 | +2.2% |
| power (W), peak | 654 | 690 | +5.5% |
| energy (Wh) | 211 | 217 | +2.6% |
| energy, parked workers still on at idle power (Wh) | 211 | 217 | +2.6% |
| CPU used (cores), mean | 0.895 | 1.28 | +42.8% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.037 | 0.053 | +42.8% |
| energy per core-hour (Wh) | 703 | 503 | -28.4% |
| node-hours per core-hour | 6.71 | 4.70 | -30.0% |
| pending pods, pod-minutes | 0.267 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.07 | 9.41 | +3.7% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.767 | -2.1% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 0.769 | 0.000 | -100.0% |
| response time (ms), mean | 157 | 96.87 | -38.2% |
| response time (ms), median | 130 | 83.20 | -35.9% |
| response time (ms), 95th percentile | 327 | 158 | -51.6% |
| response time (ms), 99th percentile | 464 | 199 | -57.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.3132 | 5.3074 | -27.4% | [-3.6177, -0.4254] | GAIN |
| kwh_per_core_hour | 0.7634 | 0.5640 | -26.1% | [-0.3524, -0.0438] | GAIN |
| utilisation | 0.0369 | 0.0523 | +41.9% | [+0.0029, +0.0292] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 0.0000 | -100.0% | [-2.2857, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2381 | 2.2381 | +0.0% | [-4.4286, +3.7619] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.36 0.393 0.422 0.446 0.469 0.488 0.505 0.522 0.535 0.547 0.557 0.563 0.568 0.572 0.577 0.581 0.585 0.588 0.589 0.59
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
| 0 | 6.00 | 6.00 | 616 | 633 | 6.00 | 5.50 | 0.000 | 0.000 | 0.554 | 1.01 |
| 1 | 6.00 | 6.00 | 617 | 624 | 6.00 | 7.00 | 0.000 | 0.000 | 0.583 | 0.771 |
| 2 | 6.00 | 6.00 | 616 | 624 | 6.00 | 7.00 | 0.000 | 0.000 | 0.554 | 0.770 |
| 3 | 6.00 | 6.00 | 625 | 633 | 6.00 | 9.00 | 0.000 | 0.000 | 0.777 | 1.02 |
| 4 | 6.00 | 6.00 | 630 | 649 | 8.25 | 10.00 | 0.000 | 0.000 | 0.947 | 1.43 |
| 5 | 6.00 | 6.00 | 635 | 651 | 9.67 | 10.00 | 0.000 | 0.000 | 1.05 | 1.50 |
| 6 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.40 |
| 7 | 6.00 | 6.00 | 647 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 2.16 |
| 8 | 6.00 | 6.00 | 648 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 2.14 |
| 9 | 6.00 | 6.00 | 646 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 2.14 |
| 10 | 6.00 | 6.00 | 646 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.98 |
| 11 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.619 | 0.784 |
| 12 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.607 | 0.806 |
| 13 | 6.00 | 6.00 | 622 | 636 | 10.00 | 10.00 | 0.250 | 0.000 | 0.713 | 1.09 |
| 14 | 6.00 | 6.00 | 635 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.38 |
| 15 | 6.00 | 6.00 | 633 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.988 | 1.37 |
| 16 | 6.00 | 6.00 | 636 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.41 |
| 17 | 6.00 | 6.00 | 628 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.853 | 1.15 |
| 18 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.581 | 0.747 |
| 19 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.651 | 0.739 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
