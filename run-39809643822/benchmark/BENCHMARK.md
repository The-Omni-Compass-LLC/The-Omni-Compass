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
| duration (min) | 20.15 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.01 | -0.2% |
| power (W), mean | 630 | 642 | +1.9% |
| power (W), peak | 651 | 681 | +4.6% |
| energy (Wh) | 212 | 215 | +1.7% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.7% |
| CPU used (cores), mean | 0.912 | 1.23 | +35.5% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.051 | +35.5% |
| energy per core-hour (Wh) | 691 | 520 | -24.8% |
| node-hours per core-hour | 6.58 | 4.86 | -26.2% |
| pending pods, pod-minutes | 0.250 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.83 | 9.45 | +7.0% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.767 | 0.533 | -30.4% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 0.769 | 0.000 | -100.0% |
| response time (ms), mean | 154 | 96.24 | -37.5% |
| response time (ms), median | 127 | 82.90 | -34.5% |
| response time (ms), 95th percentile | 319 | 157 | -50.8% |
| response time (ms), 99th percentile | 470 | 201 | -57.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2005 | 5.3272 | -26.0% | [-3.5157, -0.1843] | GAIN |
| kwh_per_core_hour | 0.7522 | 0.5663 | -24.7% | [-0.3454, -0.0230] | GAIN |
| utilisation | 0.0375 | 0.0525 | +40.0% | [+0.0019, +0.0292] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 0.0000 | -100.0% | [-2.2857, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2381 | 1.6466 | -26.4% | [-4.3905, +2.5778] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 80 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.33 0.34 0.349 0.359 0.368 0.376 0.384 0.392 0.4 0.407 0.414 0.421 0.428 0.434 0.44 0.446 0.452 0.458 0.463 0.469 0.474 0.479 0.483 0.488 0.493 0.497 0.501 0.505 0.509 0.513 0.517 0.521 0.524 0.528 0.531 0.534 0.537 0.54 0.543 0.546 0.549 0.552 0.554 0.556 0.558 0.559 0.561 0.562 0.563 0.564 0.566 0.567 0.568 0.569 0.57 0.572 0.573 0.575 0.576 0.577 0.578 0.579 0.58 0.581 0.582 0.583 0.584 0.585 0.586 0.587 0.587 0.588 0.588 0.588 0.589 0.589 0.589 0.59 0.59 0.59
- nodes decided per minute: 6 6 6 6 6 6 6 5 5 5 5 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
- HPA target decided per minute (%): 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77

## Reset

```
restored target: 50
workers in service: 6 of 6
Omni records left after kill: none
```

## Minute by minute

| min | nodes native | nodes omni | power W native | power W omni | replicas native | replicas omni | pending native | pending omni | CPU native | CPU omni |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.00 | 6.00 | 617 | 621 | 5.00 | 6.00 | 0.000 | 0.000 | 0.589 | 0.646 |
| 1 | 6.00 | 6.00 | 618 | 622 | 5.00 | 7.50 | 0.000 | 0.000 | 0.594 | 0.716 |
| 2 | 6.00 | 6.00 | 617 | 624 | 5.00 | 8.00 | 0.000 | 0.000 | 0.556 | 0.755 |
| 3 | 6.00 | 6.00 | 625 | 638 | 5.00 | 8.00 | 0.000 | 0.000 | 0.780 | 1.15 |
| 4 | 6.00 | 6.00 | 634 | 646 | 8.50 | 10.00 | 0.000 | 0.000 | 1.02 | 1.32 |
| 5 | 6.00 | 6.00 | 634 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.33 |
| 6 | 6.00 | 6.00 | 638 | 650 | 9.75 | 10.00 | 0.250 | 0.000 | 1.08 | 1.42 |
| 7 | 6.00 | 6.00 | 647 | 667 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 1.96 |
| 8 | 6.00 | 6.00 | 650 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.43 | 2.09 |
| 9 | 6.00 | 6.00 | 647 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 2.18 |
| 10 | 6.00 | 6.00 | 640 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.20 | 1.99 |
| 11 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.570 | 0.780 |
| 12 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.654 | 0.765 |
| 13 | 6.00 | 6.00 | 625 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.782 | 1.03 |
| 14 | 6.00 | 6.00 | 633 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.991 | 1.42 |
| 15 | 6.00 | 6.00 | 635 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.35 |
| 16 | 6.00 | 6.00 | 633 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.45 |
| 17 | 6.00 | 6.00 | 630 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.922 | 1.08 |
| 18 | 6.00 | 6.00 | 617 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.594 | 0.680 |
| 19 | 6.00 | 6.00 | 619 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.627 | 0.710 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
