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
| duration (min) | 20.15 | 20.22 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.3% |
| power (W), mean | 629 | 641 | +1.9% |
| power (W), peak | 650 | 684 | +5.3% |
| energy (Wh) | 211 | 216 | +2.2% |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.2% |
| CPU used (cores), mean | 0.898 | 1.20 | +33.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.050 | +33.9% |
| energy per core-hour (Wh) | 701 | 533 | -23.9% |
| node-hours per core-hour | 6.68 | 4.99 | -25.3% |
| pending pods, pod-minutes | 0.517 | 0.267 | -48.4% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.17 | 9.34 | +1.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.800 | +54.8% |
| requests timed | 1,045 | 1,100 | +5.3% |
| time over the response line (% of samples) | 0.287 | 0.000 | -100.0% |
| response time (ms), mean | 153 | 94.50 | -38.3% |
| response time (ms), median | 129 | 80.80 | -37.5% |
| response time (ms), 95th percentile | 302 | 153 | -49.3% |
| response time (ms), 99th percentile | 444 | 201 | -54.7% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2137 | 5.7584 | -20.2% | [-3.1192, +0.1965] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7536 | 0.6093 | -19.1% | [-0.3037, +0.0184] | EVEN, no significant difference |
| utilisation | 0.0370 | 0.0492 | +33.2% | [+0.0001, +0.0257] | GAIN |
| pending_pod_minutes_per_hour | 1.4877 | 0.7619 | -48.8% | [-2.9754, +1.5238] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4762 | 2.2857 | +54.8% | [-2.2381, +4.5714] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.488 0.505 0.519 0.533 0.546 0.557 0.562 0.568 0.572 0.577 0.581 0.586 0.589 0.59 0.591
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
| 0 | 6.00 | 6.00 | 617 | 621 | 5.00 | 6.00 | 0.000 | 0.000 | 0.559 | 0.640 |
| 1 | 6.00 | 6.00 | 620 | 623 | 6.00 | 6.75 | 0.000 | 0.000 | 0.651 | 0.742 |
| 2 | 6.00 | 6.00 | 618 | 620 | 7.00 | 7.00 | 0.000 | 0.000 | 0.610 | 0.662 |
| 3 | 6.00 | 6.00 | 626 | 635 | 7.00 | 7.50 | 0.000 | 0.250 | 0.798 | 1.06 |
| 4 | 6.00 | 6.00 | 633 | 646 | 9.00 | 10.00 | 0.250 | 0.000 | 1.01 | 1.34 |
| 5 | 6.00 | 6.00 | 636 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.39 |
| 6 | 6.00 | 6.00 | 633 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 0.984 | 1.35 |
| 7 | 6.00 | 6.00 | 645 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.10 |
| 8 | 6.00 | 6.00 | 647 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 2.13 |
| 9 | 6.00 | 6.00 | 646 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 2.02 |
| 10 | 6.00 | 6.00 | 646 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.61 |
| 11 | 6.00 | 6.00 | 616 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.538 | 0.784 |
| 12 | 6.00 | 6.00 | 618 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.598 | 0.680 |
| 13 | 6.00 | 6.00 | 623 | 632 | 10.00 | 10.00 | 0.250 | 0.000 | 0.747 | 0.965 |
| 14 | 6.00 | 6.00 | 633 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.46 |
| 15 | 6.00 | 6.00 | 635 | 653 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.44 |
| 16 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.995 | 1.37 |
| 17 | 6.00 | 6.00 | 629 | 637 | 10.00 | 10.00 | 0.000 | 0.000 | 0.891 | 1.11 |
| 18 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.608 | 0.715 |
| 19 | 6.00 | 6.00 | 620 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.648 | 0.727 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
