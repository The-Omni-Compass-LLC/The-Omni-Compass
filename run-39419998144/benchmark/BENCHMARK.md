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
| duration (min) | 20.23 | 20.25 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.1% |
| power (W), mean | 628 | 642 | +2.2% |
| power (W), peak | 651 | 684 | +5.1% |
| energy (Wh) | 212 | 217 | +2.3% |
| energy, parked workers still on at idle power (Wh) | 212 | 217 | +2.3% |
| CPU used (cores), mean | 0.862 | 1.23 | +42.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.051 | +42.1% |
| energy per core-hour (Wh) | 728 | 524 | -28.1% |
| node-hours per core-hour | 6.96 | 4.90 | -29.6% |
| pending pods, pod-minutes | 0.250 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.86 | 9.30 | +5.0% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.783 | +46.9% |
| requests timed | 1,070 | 1,100 | +2.8% |
| time over the response line (% of samples) | 0.187 | 0.000 | -100.0% |
| response time (ms), mean | 123 | 95.50 | -22.6% |
| response time (ms), median | 112 | 82.35 | -26.6% |
| response time (ms), 95th percentile | 251 | 158 | -37.1% |
| response time (ms), 99th percentile | 350 | 181 | -48.4% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.6475 | 5.5666 | -27.2% | [-3.8595, -0.3116] | GAIN |
| kwh_per_core_hour | 0.7966 | 0.5903 | -25.9% | [-0.3753, -0.0318] | GAIN |
| utilisation | 0.0356 | 0.0503 | +41.3% | [+0.0024, +0.0278] | GAIN |
| pending_pod_minutes_per_hour | 0.7200 | 0.0000 | -100.0% | [-2.1600, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5484 | 2.2438 | +44.9% | [-3.2052, +4.5714] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.468 0.487 0.504 0.52 0.534 0.546 0.556 0.562 0.567 0.572 0.577 0.581 0.586 0.589 0.59 0.592
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
| 0 | 6.00 | 6.00 | 616 | 621 | 5.00 | 6.00 | 0.000 | 0.000 | 0.550 | 0.645 |
| 1 | 6.00 | 6.00 | 618 | 623 | 5.00 | 6.00 | 0.000 | 0.000 | 0.588 | 0.718 |
| 2 | 6.00 | 6.00 | 616 | 621 | 5.00 | 7.00 | 0.000 | 0.000 | 0.531 | 0.690 |
| 3 | 6.00 | 6.00 | 621 | 635 | 5.00 | 7.50 | 0.250 | 0.000 | 0.697 | 1.02 |
| 4 | 6.00 | 6.00 | 632 | 648 | 7.75 | 10.00 | 0.000 | 0.000 | 0.961 | 1.38 |
| 5 | 6.00 | 6.00 | 634 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.44 |
| 6 | 6.00 | 6.00 | 632 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 0.980 | 1.37 |
| 7 | 6.00 | 6.00 | 644 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.13 |
| 8 | 6.00 | 6.00 | 649 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 1.91 |
| 9 | 6.00 | 6.00 | 648 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 2.09 |
| 10 | 6.00 | 6.00 | 636 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.87 |
| 11 | 6.00 | 6.00 | 616 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.579 | 0.766 |
| 12 | 6.00 | 6.00 | 616 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.533 | 0.705 |
| 13 | 6.00 | 6.00 | 620 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.647 | 0.980 |
| 14 | 6.00 | 6.00 | 635 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.35 |
| 15 | 6.00 | 6.00 | 635 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 1.42 |
| 16 | 6.00 | 6.00 | 633 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 0.965 | 1.55 |
| 17 | 6.00 | 6.00 | 622 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.715 | 1.14 |
| 18 | 6.00 | 6.00 | 619 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.641 | 0.753 |
| 19 | 6.00 | 6.00 | 616 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.548 | 0.825 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
