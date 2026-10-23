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
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.3% |
| power (W), mean | 630 | 642 | +1.9% |
| power (W), peak | 654 | 682 | +4.4% |
| energy (Wh) | 212 | 216 | +2.2% |
| energy, parked workers still on at idle power (Wh) | 212 | 216 | +2.2% |
| CPU used (cores), mean | 0.914 | 1.23 | +35.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.051 | +35.1% |
| energy per core-hour (Wh) | 689 | 520 | -24.6% |
| node-hours per core-hour | 6.57 | 4.86 | -26.0% |
| pending pods, pod-minutes | 0.800 | 0.533 | -33.3% |
| pending pods, peak | 2.00 | 2.00 | +0.0% |
| HPA replicas, mean | 9.12 | 9.29 | +1.9% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 1.07 | +100.0% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 0.865 | 0.000 | -100.0% |
| response time (ms), mean | 154 | 94.04 | -38.9% |
| response time (ms), median | 126 | 80.45 | -36.0% |
| response time (ms), 95th percentile | 307 | 154 | -49.8% |
| response time (ms), 99th percentile | 482 | 171 | -64.5% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2251 | 5.5889 | -22.6% | [-3.3993, +0.0880] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7549 | 0.5922 | -21.6% | [-0.3291, +0.0085] | EVEN, no significant difference |
| utilisation | 0.0376 | 0.0506 | +34.8% | [+0.0002, +0.0272] | GAIN |
| pending_pod_minutes_per_hour | 2.2798 | 1.5238 | -33.2% | [-4.5596, +3.0599] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5118 | 3.0000 | +98.4% | [-3.0236, +6.0120] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.468 0.488 0.505 0.519 0.533 0.545 0.555 0.562 0.567 0.571 0.576 0.581 0.585 0.588 0.589 0.59
- nodes decided per minute: 6 6 5 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 619 | 621 | 6.00 | 5.00 | 0.000 | 0.000 | 0.586 | 0.667 |
| 1 | 6.00 | 6.00 | 617 | 622 | 6.00 | 6.75 | 0.000 | 0.000 | 0.563 | 0.701 |
| 2 | 6.00 | 6.00 | 618 | 621 | 6.00 | 7.00 | 0.000 | 0.000 | 0.617 | 0.681 |
| 3 | 6.00 | 6.00 | 624 | 634 | 6.25 | 7.50 | 0.000 | 0.500 | 0.730 | 1.04 |
| 4 | 6.00 | 6.00 | 637 | 648 | 8.75 | 10.00 | 0.500 | 0.000 | 1.08 | 1.39 |
| 5 | 6.00 | 6.00 | 637 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.45 |
| 6 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.34 |
| 7 | 6.00 | 6.00 | 647 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.09 |
| 8 | 6.00 | 6.00 | 645 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.10 |
| 9 | 6.00 | 6.00 | 649 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.42 | 2.10 |
| 10 | 6.00 | 6.00 | 648 | 659 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 1.87 |
| 11 | 6.00 | 6.00 | 618 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.607 | 0.818 |
| 12 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.595 | 0.724 |
| 13 | 6.00 | 6.00 | 624 | 630 | 10.00 | 10.00 | 0.250 | 0.000 | 0.755 | 0.936 |
| 14 | 6.00 | 6.00 | 636 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.51 |
| 15 | 6.00 | 6.00 | 636 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.42 |
| 16 | 6.00 | 6.00 | 636 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 1.39 |
| 17 | 6.00 | 6.00 | 627 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.822 | 1.15 |
| 18 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.606 | 0.748 |
| 19 | 6.00 | 6.00 | 619 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.614 | 0.804 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
