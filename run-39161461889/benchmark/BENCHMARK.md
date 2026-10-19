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
| duration (min) | 20.07 | 20.17 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.5% |
| power (W), mean | 624 | 640 | +2.6% |
| power (W), peak | 648 | 681 | +5.1% |
| energy (Wh) | 209 | 215 | +3.1% |
| energy, parked workers still on at idle power (Wh) | 209 | 215 | +3.1% |
| CPU used (cores), mean | 0.750 | 1.19 | +58.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.031 | 0.050 | +58.4% |
| energy per core-hour (Wh) | 832 | 539 | -35.2% |
| node-hours per core-hour | 8.00 | 5.05 | -36.9% |
| pending pods, pod-minutes | 0.517 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.28 | 9.44 | +14.0% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.28 | 0.517 | -59.7% |
| requests timed | 1,135 | 1,105 | -2.6% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 60.04 | 86.62 | +44.3% |
| response time (ms), median | 43.10 | 73.70 | +71.0% |
| response time (ms), 95th percentile | 130 | 142 | +9.3% |
| response time (ms), 99th percentile | 209 | 158 | -24.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.8736 | 5.7113 | -35.6% | [-5.1547, -1.1778] | GAIN |
| kwh_per_core_hour | 0.9187 | 0.6043 | -34.2% | [-0.5073, -0.1279] | GAIN |
| utilisation | 0.0310 | 0.0487 | +57.4% | [+0.0062, +0.0308] | GAIN |
| pending_pod_minutes_per_hour | 1.4754 | 0.0000 | -100.0% | [-4.4262, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.7133 | 1.4823 | -60.1% | [-5.9823, +1.4183] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.488 0.504 0.52 0.534 0.545 0.555 0.561 0.567 0.571 0.575 0.579 0.583 0.587 0.588 0.59
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
| 0 | 6.00 | 6.00 | 614 | 627 | 4.00 | 5.25 | 0.000 | 0.000 | 0.479 | 0.845 |
| 1 | 6.00 | 6.00 | 616 | 624 | 4.75 | 8.00 | 0.000 | 0.000 | 0.546 | 0.749 |
| 2 | 6.00 | 6.00 | 613 | 622 | 5.00 | 8.00 | 0.000 | 0.000 | 0.445 | 0.722 |
| 3 | 6.00 | 6.00 | 617 | 629 | 5.00 | 8.00 | 0.500 | 0.000 | 0.545 | 0.893 |
| 4 | 6.00 | 6.00 | 631 | 650 | 7.50 | 10.00 | 0.000 | 0.000 | 0.925 | 1.45 |
| 5 | 6.00 | 6.00 | 629 | 646 | 9.00 | 10.00 | 0.000 | 0.000 | 0.879 | 1.32 |
| 6 | 6.00 | 6.00 | 624 | 642 | 9.00 | 10.00 | 0.000 | 0.000 | 0.778 | 1.25 |
| 7 | 6.00 | 6.00 | 642 | 671 | 9.75 | 10.00 | 0.000 | 0.000 | 1.24 | 2.02 |
| 8 | 6.00 | 6.00 | 644 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 2.07 |
| 9 | 6.00 | 6.00 | 640 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 2.03 |
| 10 | 6.00 | 6.00 | 636 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 1.91 |
| 11 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.596 | 0.797 |
| 12 | 6.00 | 6.00 | 614 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.483 | 0.715 |
| 13 | 6.00 | 6.00 | 618 | 629 | 10.00 | 10.00 | 0.000 | 0.000 | 0.571 | 0.879 |
| 14 | 6.00 | 6.00 | 626 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.786 | 1.32 |
| 15 | 6.00 | 6.00 | 626 | 641 | 10.00 | 10.00 | 0.000 | 0.000 | 0.829 | 1.22 |
| 16 | 6.00 | 6.00 | 629 | 644 | 8.00 | 10.00 | 0.000 | 0.000 | 0.884 | 1.29 |
| 17 | 6.00 | 6.00 | 620 | 638 | 8.00 | 10.00 | 0.000 | 0.000 | 0.662 | 1.12 |
| 18 | 6.00 | 6.00 | 615 | 619 | 8.00 | 10.00 | 0.000 | 0.000 | 0.506 | 0.631 |
| 19 | 6.00 | 6.00 | 613 | 623 | 8.00 | 10.00 | 0.000 | 0.000 | 0.470 | 0.717 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
