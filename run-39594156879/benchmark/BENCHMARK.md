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
| duration (min) | 20.02 | 20.13 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.01 | +0.6% |
| power (W), mean | 627 | 639 | +1.8% |
| power (W), peak | 657 | 676 | +3.0% |
| energy (Wh) | 209 | 214 | +2.4% |
| energy, parked workers still on at idle power (Wh) | 209 | 214 | +2.4% |
| CPU used (cores), mean | 0.841 | 1.14 | +35.5% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.047 | +35.5% |
| energy per core-hour (Wh) | 746 | 561 | -24.8% |
| node-hours per core-hour | 7.14 | 5.27 | -26.2% |
| pending pods, pod-minutes | 0.000 | 0.267 | new |
| pending pods, peak | 0.000 | 1.00 | new |
| HPA replicas, mean | 9.04 | 9.30 | +2.9% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.517 | -34.0% |
| requests timed | 1,055 | 1,115 | +5.7% |
| time over the response line (% of samples) | 1.04 | 0.090 | -91.4% |
| response time (ms), mean | 139 | 80.62 | -41.8% |
| response time (ms), median | 115 | 73.10 | -36.5% |
| response time (ms), 95th percentile | 277 | 111 | -60.0% |
| response time (ms), 99th percentile | 499 | 149 | -70.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.8457 | 6.0251 | -23.2% | [-3.6855, +0.0484] | EVEN, no significant difference |
| kwh_per_core_hour | 0.8164 | 0.6358 | -22.1% | [-0.3549, +0.0014] | EVEN, no significant difference |
| utilisation | 0.0346 | 0.0467 | +35.1% | [+0.0005, +0.0247] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 0.7619 | n/a | [+0.0000, +2.2857] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.3041 | 1.4401 | -37.5% | [-3.8403, +2.0876] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.469 0.488 0.505 0.521 0.534 0.546 0.556 0.561 0.566 0.571 0.576 0.58 0.584 0.587 0.589 0.59
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
| 0 | 6.00 | 6.00 | 616 | 619 | 5.50 | 6.00 | 0.000 | 0.000 | 0.546 | 0.582 |
| 1 | 6.00 | 6.00 | 617 | 622 | 6.00 | 6.50 | 0.000 | 0.000 | 0.549 | 0.695 |
| 2 | 6.00 | 6.00 | 616 | 623 | 6.00 | 7.00 | 0.000 | 0.000 | 0.538 | 0.725 |
| 3 | 6.00 | 6.00 | 620 | 628 | 6.00 | 7.00 | 0.000 | 0.000 | 0.648 | 0.876 |
| 4 | 6.00 | 6.00 | 632 | 650 | 8.00 | 10.00 | 0.000 | 0.000 | 0.953 | 1.36 |
| 5 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.32 |
| 6 | 6.00 | 6.00 | 630 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 0.919 | 1.27 |
| 7 | 6.00 | 6.00 | 644 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 1.99 |
| 8 | 6.00 | 6.00 | 647 | 664 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.80 |
| 9 | 6.00 | 6.00 | 642 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 1.93 |
| 10 | 6.00 | 6.00 | 635 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.84 |
| 11 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.570 | 0.753 |
| 12 | 6.00 | 6.00 | 616 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.598 | 0.670 |
| 13 | 6.00 | 6.00 | 621 | 631 | 10.00 | 10.00 | 0.000 | 0.250 | 0.679 | 0.930 |
| 14 | 6.00 | 6.00 | 633 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.974 | 1.14 |
| 15 | 6.00 | 6.00 | 630 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.949 | 1.32 |
| 16 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.963 | 1.29 |
| 17 | 6.00 | 6.00 | 621 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.708 | 1.06 |
| 18 | 6.00 | 6.00 | 616 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.543 | 0.772 |
| 19 | 6.00 | 6.00 | 618 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.577 | 0.678 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
