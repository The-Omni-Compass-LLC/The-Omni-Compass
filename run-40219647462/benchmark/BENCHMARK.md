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
| duration (min) | 20.15 | 20.25 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.5% |
| power (W), mean | 629 | 641 | +1.9% |
| power (W), peak | 657 | 687 | +4.6% |
| energy (Wh) | 211 | 216 | +2.4% |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.4% |
| CPU used (cores), mean | 0.897 | 1.22 | +35.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.051 | +35.9% |
| energy per core-hour (Wh) | 702 | 526 | -25.0% |
| node-hours per core-hour | 6.69 | 4.92 | -26.4% |
| pending pods, pod-minutes | 1.07 | 0.000 | -100.0% |
| pending pods, peak | 3.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.03 | 9.42 | +4.3% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.800 | 0.783 | -2.1% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 0.769 | 0.000 | -100.0% |
| response time (ms), mean | 158 | 94.81 | -40.1% |
| response time (ms), median | 130 | 82.90 | -36.0% |
| response time (ms), 95th percentile | 314 | 152 | -51.5% |
| response time (ms), 99th percentile | 476 | 176 | -63.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.3652 | 5.6192 | -23.7% | [-3.5170, -0.0069] | GAIN |
| kwh_per_core_hour | 0.7688 | 0.5955 | -22.5% | [-0.3419, -0.0021] | GAIN |
| utilisation | 0.0368 | 0.0499 | +35.5% | [+0.0007, +0.0264] | GAIN |
| pending_pod_minutes_per_hour | 3.0720 | 0.0000 | -100.0% | [-8.4480, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2979 | 2.2619 | -1.6% | [-3.8217, +3.7558] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.488 0.505 0.52 0.534 0.546 0.556 0.562 0.567 0.571 0.576 0.58 0.584 0.588 0.589 0.59
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
| 0 | 6.00 | 6.00 | 617 | 619 | 5.00 | 6.00 | 0.000 | 0.000 | 0.573 | 0.602 |
| 1 | 6.00 | 6.00 | 617 | 625 | 5.00 | 6.75 | 0.000 | 0.000 | 0.571 | 0.800 |
| 2 | 6.00 | 6.00 | 620 | 626 | 6.00 | 8.00 | 0.000 | 0.000 | 0.626 | 0.783 |
| 3 | 6.00 | 6.00 | 622 | 634 | 6.00 | 8.00 | 0.750 | 0.000 | 0.729 | 1.01 |
| 4 | 6.00 | 6.00 | 633 | 646 | 9.25 | 10.00 | 0.000 | 0.000 | 1.02 | 1.38 |
| 5 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.36 |
| 6 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.40 |
| 7 | 6.00 | 6.00 | 649 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 1.99 |
| 8 | 6.00 | 6.00 | 649 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 2.04 |
| 9 | 6.00 | 6.00 | 645 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 1.96 |
| 10 | 6.00 | 6.00 | 649 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.44 | 1.93 |
| 11 | 6.00 | 6.00 | 617 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.547 | 0.848 |
| 12 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.616 | 0.751 |
| 13 | 6.00 | 6.00 | 626 | 631 | 10.00 | 10.00 | 0.250 | 0.000 | 0.802 | 0.965 |
| 14 | 6.00 | 6.00 | 634 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.37 |
| 15 | 6.00 | 6.00 | 634 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.45 |
| 16 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.37 |
| 17 | 6.00 | 6.00 | 626 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.787 | 1.16 |
| 18 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.583 | 0.747 |
| 19 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.587 | 0.697 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
