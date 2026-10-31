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
| duration (min) | 20.17 | 20.08 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.4% |
| power (W), mean | 626 | 641 | +2.5% |
| power (W), peak | 646 | 682 | +5.6% |
| energy (Wh) | 210 | 215 | +2.1% |
| energy, parked workers still on at idle power (Wh) | 210 | 215 | +2.1% |
| CPU used (cores), mean | 0.794 | 1.22 | +53.8% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.033 | 0.051 | +53.8% |
| energy per core-hour (Wh) | 788 | 525 | -33.4% |
| node-hours per core-hour | 7.56 | 4.91 | -35.0% |
| pending pods, pod-minutes | 0.250 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.70 | 9.45 | +8.7% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.517 | +0.0% |
| requests timed | 1,130 | 1,095 | -3.1% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 64.36 | 95.98 | +49.1% |
| response time (ms), median | 44.00 | 81.50 | +85.2% |
| response time (ms), 95th percentile | 149 | 154 | +2.9% |
| response time (ms), 99th percentile | 221 | 179 | -19.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.4516 | 5.3717 | -36.4% | [-5.1128, -1.0855] | GAIN |
| kwh_per_core_hour | 0.8767 | 0.5705 | -34.9% | [-0.5071, -0.1110] | GAIN |
| utilisation | 0.0328 | 0.0518 | +58.3% | [+0.0064, +0.0332] | GAIN |
| pending_pod_minutes_per_hour | 0.7258 | 0.0000 | -100.0% | [-2.1774, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4942 | 1.6340 | +9.4% | [-2.8078, +2.6746] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.469 0.489 0.505 0.52 0.534 0.547 0.557 0.562 0.567 0.572 0.577 0.581 0.585 0.589 0.59 0.591
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
| 0 | 6.00 | 6.00 | 612 | 618 | 6.00 | 6.00 | 0.000 | 0.000 | 0.442 | 0.629 |
| 1 | 6.00 | 6.00 | 614 | 626 | 6.00 | 7.50 | 0.000 | 0.000 | 0.474 | 0.784 |
| 2 | 6.00 | 6.00 | 614 | 624 | 6.00 | 8.00 | 0.000 | 0.000 | 0.496 | 0.759 |
| 3 | 6.00 | 6.00 | 618 | 633 | 6.00 | 8.00 | 0.250 | 0.000 | 0.582 | 0.954 |
| 4 | 6.00 | 6.00 | 631 | 646 | 7.00 | 10.00 | 0.000 | 0.000 | 0.922 | 1.37 |
| 5 | 6.00 | 6.00 | 633 | 648 | 9.00 | 10.00 | 0.000 | 0.000 | 0.942 | 1.40 |
| 6 | 6.00 | 6.00 | 634 | 643 | 9.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.25 |
| 7 | 6.00 | 6.00 | 638 | 667 | 9.33 | 10.00 | 0.000 | 0.000 | 1.14 | 1.91 |
| 8 | 6.00 | 6.00 | 645 | 679 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 2.23 |
| 9 | 6.00 | 6.00 | 643 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.25 | 2.11 |
| 10 | 6.00 | 6.00 | 638 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.11 | 1.99 |
| 11 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.554 | 0.735 |
| 12 | 6.00 | 6.00 | 615 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.597 | 0.727 |
| 13 | 6.00 | 6.00 | 625 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.765 | 0.967 |
| 14 | 6.00 | 6.00 | 629 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.896 | 1.36 |
| 15 | 6.00 | 6.00 | 631 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.891 | 1.39 |
| 16 | 6.00 | 6.00 | 629 | 646 | 9.00 | 10.00 | 0.000 | 0.000 | 0.901 | 1.36 |
| 17 | 6.00 | 6.00 | 622 | 631 | 9.00 | 10.00 | 0.000 | 0.000 | 0.709 | 1.09 |
| 18 | 6.00 | 6.00 | 615 | 623 | 9.00 | 10.00 | 0.000 | 0.000 | 0.521 | 0.713 |
| 19 | 6.00 | 6.00 | 614 | 624 | 9.00 | 10.00 | 0.000 | 0.000 | 0.484 | 0.738 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
