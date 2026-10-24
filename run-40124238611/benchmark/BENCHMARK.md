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
| duration (min) | 20.13 | 20.20 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.3% |
| power (W), mean | 626 | 641 | +2.5% |
| power (W), peak | 646 | 682 | +5.6% |
| energy (Wh) | 210 | 216 | +2.8% |
| energy, parked workers still on at idle power (Wh) | 210 | 216 | +2.8% |
| CPU used (cores), mean | 0.803 | 1.21 | +51.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.033 | 0.051 | +51.1% |
| energy per core-hour (Wh) | 779 | 528 | -32.2% |
| node-hours per core-hour | 7.47 | 4.94 | -33.8% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 8.71 | 9.42 | +8.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.500 | 0.783 | +56.7% |
| requests timed | 1,125 | 1,100 | -2.2% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 68.91 | 95.24 | +38.2% |
| response time (ms), median | 46.30 | 81.50 | +76.0% |
| response time (ms), 95th percentile | 166 | 153 | -8.2% |
| response time (ms), 99th percentile | 249 | 185 | -25.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.2639 | 5.7187 | -30.8% | [-4.5097, -0.5828] | GAIN |
| kwh_per_core_hour | 0.8579 | 0.6054 | -29.4% | [-0.4386, -0.0587] | GAIN |
| utilisation | 0.0332 | 0.0496 | +49.5% | [+0.0039, +0.0297] | GAIN |
| pending_pod_minutes_per_hour | 0.7805 | 0.7619 | -2.4% | [-2.3415, +2.2857] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4634 | 2.2619 | +54.6% | [-2.1951, +4.5302] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.488 0.505 0.519 0.533 0.546 0.555 0.561 0.567 0.571 0.576 0.581 0.584 0.588 0.589 0.59
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
| 0 | 6.00 | 6.00 | 615 | 621 | 5.00 | 5.00 | 0.000 | 0.000 | 0.491 | 0.624 |
| 1 | 6.00 | 6.00 | 616 | 624 | 5.00 | 7.75 | 0.000 | 0.000 | 0.536 | 0.750 |
| 2 | 6.00 | 6.00 | 615 | 623 | 5.00 | 8.00 | 0.000 | 0.000 | 0.507 | 0.723 |
| 3 | 6.00 | 6.00 | 620 | 633 | 5.00 | 8.00 | 0.250 | 0.250 | 0.642 | 1.02 |
| 4 | 6.00 | 6.00 | 628 | 648 | 7.25 | 10.00 | 0.000 | 0.000 | 0.864 | 1.40 |
| 5 | 6.00 | 6.00 | 631 | 647 | 8.00 | 10.00 | 0.000 | 0.000 | 0.942 | 1.38 |
| 6 | 6.00 | 6.00 | 634 | 648 | 9.50 | 10.00 | 0.000 | 0.000 | 1.04 | 1.39 |
| 7 | 6.00 | 6.00 | 644 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.08 |
| 8 | 6.00 | 6.00 | 644 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 2.06 |
| 9 | 6.00 | 6.00 | 645 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 1.99 |
| 10 | 6.00 | 6.00 | 638 | 660 | 10.00 | 10.00 | 0.000 | 0.000 | 1.13 | 1.69 |
| 11 | 6.00 | 6.00 | 617 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.566 | 0.793 |
| 12 | 6.00 | 6.00 | 616 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.561 | 0.811 |
| 13 | 6.00 | 6.00 | 621 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.683 | 0.966 |
| 14 | 6.00 | 6.00 | 630 | 655 | 10.00 | 10.00 | 0.000 | 0.000 | 0.916 | 1.59 |
| 15 | 6.00 | 6.00 | 629 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.907 | 1.39 |
| 16 | 6.00 | 6.00 | 630 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.948 | 1.45 |
| 17 | 6.00 | 6.00 | 620 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.634 | 0.997 |
| 18 | 6.00 | 6.00 | 613 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.473 | 0.703 |
| 19 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.542 | 0.697 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
