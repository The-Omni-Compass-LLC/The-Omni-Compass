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
| duration (min) | 20.05 | 20.00 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.00 | -0.2% |
| power (W), mean | 628 | 643 | +2.4% |
| power (W), peak | 652 | 686 | +5.1% |
| energy (Wh) | 210 | 214 | +2.2% |
| energy, parked workers still on at idle power (Wh) | 210 | 214 | +2.2% |
| CPU used (cores), mean | 0.858 | 1.27 | +48.2% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.036 | 0.053 | +48.2% |
| energy per core-hour (Wh) | 732 | 506 | -30.9% |
| node-hours per core-hour | 6.99 | 4.72 | -32.5% |
| pending pods, pod-minutes | 0.000 | 0.533 | new |
| pending pods, peak | 0.000 | 2.00 | new |
| HPA replicas, mean | 8.85 | 9.27 | +4.7% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.517 | -34.0% |
| requests timed | 1,055 | 1,095 | +3.8% |
| time over the response line (% of samples) | 0.948 | 0.000 | -100.0% |
| response time (ms), mean | 139 | 96.13 | -30.9% |
| response time (ms), median | 115 | 82.60 | -28.2% |
| response time (ms), 95th percentile | 301 | 157 | -47.8% |
| response time (ms), 99th percentile | 473 | 191 | -59.7% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.5791 | 5.1127 | -32.5% | [-3.9476, -0.9403] | GAIN |
| kwh_per_core_hour | 0.7901 | 0.5450 | -31.0% | [-0.3910, -0.0978] | GAIN |
| utilisation | 0.0353 | 0.0539 | +52.7% | [+0.0060, +0.0326] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 1.7067 | n/a | [+0.0000, +5.1200] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2557 | 1.6999 | -24.6% | [-3.6649, +2.6318] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.393 0.422 0.446 0.469 0.489 0.506 0.521 0.534 0.546 0.556 0.562 0.567 0.571 0.576 0.581 0.585 0.588 0.589 0.59
- nodes decided per minute: 6 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 620 | 622 | 4.50 | 5.00 | 0.000 | 0.500 | 0.619 | 0.702 |
| 1 | 6.00 | 6.00 | 619 | 631 | 5.25 | 7.00 | 0.000 | 0.000 | 0.610 | 0.936 |
| 2 | 6.00 | 6.00 | 622 | 624 | 6.00 | 7.00 | 0.000 | 0.000 | 0.711 | 0.776 |
| 3 | 6.00 | 6.00 | 621 | 633 | 6.00 | 7.00 | 0.000 | 0.000 | 0.676 | 1.00 |
| 4 | 6.00 | 6.00 | 630 | 649 | 8.00 | 10.00 | 0.000 | 0.000 | 0.914 | 1.41 |
| 5 | 6.00 | 6.00 | 632 | 652 | 8.00 | 10.00 | 0.000 | 0.000 | 0.974 | 1.49 |
| 6 | 6.00 | 6.00 | 631 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 0.945 | 1.49 |
| 7 | 6.00 | 6.00 | 645 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.03 |
| 8 | 6.00 | 6.00 | 644 | 677 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.17 |
| 9 | 6.00 | 6.00 | 650 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 2.14 |
| 10 | 6.00 | 6.00 | 636 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 2.11 |
| 11 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.592 | 0.734 |
| 12 | 6.00 | 6.00 | 614 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.492 | 0.704 |
| 13 | 6.00 | 6.00 | 622 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.689 | 1.04 |
| 14 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.973 | 1.39 |
| 15 | 6.00 | 6.00 | 630 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.928 | 1.38 |
| 16 | 6.00 | 6.00 | 633 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.979 | 1.42 |
| 17 | 6.00 | 6.00 | 621 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.666 | 1.08 |
| 18 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.560 | 0.739 |
| 19 | 6.00 | 6.00 | 618 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.595 | 0.859 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
