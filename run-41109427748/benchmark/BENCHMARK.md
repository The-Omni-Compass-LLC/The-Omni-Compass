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
| duration (min) | 20.23 | 20.22 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | -0.1% |
| power (W), mean | 627 | 630 | +0.5% |
| power (W), peak | 652 | 669 | +2.5% |
| energy (Wh) | 211 | 212 | +0.4% |
| energy, parked workers still on at idle power (Wh) | 211 | 212 | +0.4% |
| CPU used (cores), mean | 0.829 | 0.918 | +10.7% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.038 | +10.7% |
| energy per core-hour (Wh) | 756 | 686 | -9.2% |
| node-hours per core-hour | 7.23 | 6.53 | -9.7% |
| pending pods, pod-minutes | 0.500 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.86 | 8.98 | +1.3% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.783 | +0.0% |
| requests timed | 1,065 | 1,145 | +7.5% |
| time over the response line (% of samples) | 0.094 | 0.000 | -100.0% |
| response time (ms), mean | 127 | 49.62 | -61.0% |
| response time (ms), median | 112 | 43.10 | -61.4% |
| response time (ms), 95th percentile | 275 | 72.40 | -73.7% |
| response time (ms), 99th percentile | 389 | 98.54 | -74.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.9647 | 7.5170 | -5.6% | [-2.6585, +1.7548] | EVEN, no significant difference |
| kwh_per_core_hour | 0.8284 | 0.7837 | -5.4% | [-0.2508, +0.1696] | EVEN, no significant difference |
| utilisation | 0.0342 | 0.0378 | +10.4% | [-0.0069, +0.0148] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 1.4400 | 0.0000 | -100.0% | [-4.3200, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2138 | 2.2680 | +2.4% | [-3.6001, +3.8103] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.467 0.486 0.502 0.517 0.53 0.541 0.551 0.557 0.562 0.567 0.572 0.576 0.579 0.583 0.585 0.586
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
| 0 | 6.00 | 6.00 | 615 | 615 | 4.25 | 4.00 | 0.000 | 0.000 | 0.514 | 0.510 |
| 1 | 6.00 | 6.00 | 616 | 616 | 5.00 | 5.50 | 0.000 | 0.000 | 0.542 | 0.573 |
| 2 | 6.00 | 6.00 | 615 | 617 | 5.00 | 6.00 | 0.000 | 0.000 | 0.505 | 0.563 |
| 3 | 6.00 | 6.00 | 624 | 618 | 5.00 | 6.00 | 0.000 | 0.000 | 0.665 | 0.612 |
| 4 | 6.00 | 6.00 | 632 | 636 | 8.50 | 8.50 | 0.500 | 0.000 | 0.973 | 1.07 |
| 5 | 6.00 | 6.00 | 632 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.958 | 0.986 |
| 6 | 6.00 | 6.00 | 628 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.903 | 1.06 |
| 7 | 6.00 | 6.00 | 642 | 655 | 10.00 | 10.00 | 0.000 | 0.000 | 1.23 | 1.59 |
| 8 | 6.00 | 6.00 | 647 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 1.43 |
| 9 | 6.00 | 6.00 | 645 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 1.62 |
| 10 | 6.00 | 6.00 | 637 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.56 |
| 11 | 6.00 | 6.00 | 618 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.586 | 0.514 |
| 12 | 6.00 | 6.00 | 617 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.558 | 0.526 |
| 13 | 6.00 | 6.00 | 621 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.688 | 0.731 |
| 14 | 6.00 | 6.00 | 631 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.955 | 0.992 |
| 15 | 6.00 | 6.00 | 630 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.919 | 1.04 |
| 16 | 6.00 | 6.00 | 630 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.950 | 0.986 |
| 17 | 6.00 | 6.00 | 623 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.740 | 0.834 |
| 18 | 6.00 | 6.00 | 616 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.515 | 0.653 |
| 19 | 6.00 | 6.00 | 617 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.571 | 0.485 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
