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
| duration (min) | 20.08 | 20.23 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.7% |
| power (W), mean | 627 | 642 | +2.4% |
| power (W), peak | 651 | 686 | +5.3% |
| energy (Wh) | 210 | 216 | +3.1% |
| energy, parked workers still on at idle power (Wh) | 210 | 216 | +3.1% |
| CPU used (cores), mean | 0.833 | 1.23 | +47.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.051 | +47.9% |
| energy per core-hour (Wh) | 753 | 521 | -30.8% |
| node-hours per core-hour | 7.20 | 4.87 | -32.4% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 8.95 | 9.33 | +4.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 1.05 | +96.9% |
| requests timed | 1,080 | 1,100 | +1.9% |
| time over the response line (% of samples) | 0.093 | 0.000 | -100.0% |
| response time (ms), mean | 115 | 94.93 | -17.1% |
| response time (ms), median | 103 | 82.00 | -20.2% |
| response time (ms), 95th percentile | 218 | 152 | -30.1% |
| response time (ms), 99th percentile | 299 | 192 | -35.7% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.8700 | 5.5202 | -29.9% | [-4.0384, -0.6568] | GAIN |
| kwh_per_core_hour | 0.8187 | 0.5852 | -28.5% | [-0.3930, -0.0678] | GAIN |
| utilisation | 0.0342 | 0.0506 | +47.7% | [+0.0043, +0.0296] | GAIN |
| pending_pod_minutes_per_hour | 0.7680 | 0.7619 | -0.8% | [-2.3040, +2.2857] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5360 | 3.0416 | +98.0% | [-1.5603, +5.3212] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.393 0.421 0.446 0.469 0.489 0.505 0.52 0.535 0.547 0.557 0.563 0.568 0.572 0.577 0.582 0.585 0.588 0.589 0.591
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
| 0 | 6.00 | 6.00 | 615 | 616 | 5.00 | 5.00 | 0.000 | 0.250 | 0.507 | 0.570 |
| 1 | 6.00 | 6.00 | 624 | 630 | 5.75 | 7.00 | 0.250 | 0.000 | 0.727 | 0.956 |
| 2 | 6.00 | 6.00 | 615 | 623 | 6.00 | 7.25 | 0.000 | 0.000 | 0.521 | 0.694 |
| 3 | 6.00 | 6.00 | 621 | 633 | 6.00 | 8.00 | 0.000 | 0.000 | 0.675 | 1.03 |
| 4 | 6.00 | 6.00 | 632 | 651 | 9.00 | 9.75 | 0.000 | 0.000 | 0.976 | 1.47 |
| 5 | 6.00 | 6.00 | 632 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 0.939 | 1.34 |
| 6 | 6.00 | 6.00 | 628 | 647 | 9.00 | 10.00 | 0.000 | 0.000 | 0.903 | 1.40 |
| 7 | 6.00 | 6.00 | 643 | 672 | 9.75 | 10.00 | 0.000 | 0.000 | 1.27 | 2.03 |
| 8 | 6.00 | 6.00 | 645 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.08 |
| 9 | 6.00 | 6.00 | 644 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.12 |
| 10 | 6.00 | 6.00 | 635 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 2.12 |
| 11 | 6.00 | 6.00 | 616 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.537 | 0.809 |
| 12 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.547 | 0.726 |
| 13 | 6.00 | 6.00 | 619 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.620 | 1.06 |
| 14 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.939 | 1.31 |
| 15 | 6.00 | 6.00 | 631 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.980 | 1.40 |
| 16 | 6.00 | 6.00 | 633 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 0.994 | 1.26 |
| 17 | 6.00 | 6.00 | 623 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.734 | 1.05 |
| 18 | 6.00 | 6.00 | 614 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.471 | 0.761 |
| 19 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.560 | 0.737 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
