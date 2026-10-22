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
| duration (min) | 20.20 | 20.07 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.7% |
| power (W), mean | 629 | 642 | +2.1% |
| power (W), peak | 650 | 682 | +5.1% |
| energy (Wh) | 212 | 215 | +1.4% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.4% |
| CPU used (cores), mean | 0.876 | 1.24 | +41.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.052 | +41.1% |
| energy per core-hour (Wh) | 717 | 519 | -27.6% |
| node-hours per core-hour | 6.85 | 4.85 | -29.1% |
| pending pods, pod-minutes | 0.267 | 0.533 | +100.0% |
| pending pods, peak | 1.00 | 2.00 | +100.0% |
| HPA replicas, mean | 8.91 | 9.43 | +5.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.800 | 0.517 | -35.4% |
| requests timed | 1,035 | 1,100 | +6.3% |
| time over the response line (% of samples) | 1.16 | 0.091 | -92.2% |
| response time (ms), mean | 164 | 95.44 | -41.8% |
| response time (ms), median | 132 | 84.60 | -36.2% |
| response time (ms), 95th percentile | 336 | 153 | -54.7% |
| response time (ms), 99th percentile | 505 | 171 | -66.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.4769 | 5.3534 | -28.4% | [-3.8263, -0.3857] | GAIN |
| kwh_per_core_hour | 0.7798 | 0.5687 | -27.1% | [-0.3784, -0.0421] | GAIN |
| utilisation | 0.0360 | 0.0525 | +45.8% | [+0.0034, +0.0304] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 1.6931 | +122.2% | [-2.2857, +5.0794] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2918 | 1.6402 | -28.4% | [-3.6466, +2.4974] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 80 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.33 0.34 0.349 0.359 0.368 0.376 0.384 0.392 0.4 0.407 0.414 0.421 0.427 0.434 0.44 0.446 0.452 0.458 0.464 0.469 0.474 0.479 0.484 0.488 0.493 0.497 0.501 0.505 0.509 0.513 0.517 0.521 0.525 0.528 0.531 0.535 0.538 0.541 0.543 0.546 0.549 0.552 0.554 0.556 0.558 0.559 0.561 0.562 0.563 0.565 0.566 0.567 0.568 0.569 0.57 0.572 0.573 0.575 0.576 0.577 0.578 0.579 0.58 0.581 0.582 0.583 0.584 0.585 0.586 0.587 0.587 0.587 0.588 0.588 0.589 0.589 0.589 0.59 0.59 0.59
- nodes decided per minute: 6 6 6 6 6 6 6 6 6 5 5 5 5 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 615 | 620 | 5.00 | 6.00 | 0.000 | 0.000 | 0.538 | 0.650 |
| 1 | 6.00 | 6.00 | 619 | 621 | 5.25 | 7.00 | 0.000 | 0.000 | 0.611 | 0.694 |
| 2 | 6.00 | 6.00 | 620 | 625 | 6.00 | 8.00 | 0.000 | 0.000 | 0.603 | 0.778 |
| 3 | 6.00 | 6.00 | 621 | 632 | 6.00 | 8.00 | 0.250 | 0.500 | 0.691 | 0.988 |
| 4 | 6.00 | 6.00 | 632 | 653 | 9.00 | 10.00 | 0.000 | 0.000 | 0.976 | 1.51 |
| 5 | 6.00 | 6.00 | 632 | 647 | 9.00 | 10.00 | 0.000 | 0.000 | 0.964 | 1.36 |
| 6 | 6.00 | 6.00 | 632 | 650 | 9.00 | 10.00 | 0.000 | 0.000 | 0.965 | 1.44 |
| 7 | 6.00 | 6.00 | 646 | 673 | 9.50 | 10.00 | 0.000 | 0.000 | 1.34 | 2.06 |
| 8 | 6.00 | 6.00 | 644 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.04 |
| 9 | 6.00 | 6.00 | 645 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.05 |
| 10 | 6.00 | 6.00 | 648 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.94 |
| 11 | 6.00 | 6.00 | 621 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.667 | 0.745 |
| 12 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.580 | 0.768 |
| 13 | 6.00 | 6.00 | 623 | 630 | 10.00 | 10.00 | 0.000 | 0.000 | 0.724 | 0.913 |
| 14 | 6.00 | 6.00 | 635 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.46 |
| 15 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.41 |
| 16 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.941 | 1.33 |
| 17 | 6.00 | 6.00 | 626 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.819 | 1.08 |
| 18 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.599 | 0.791 |
| 19 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.560 | 0.751 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
