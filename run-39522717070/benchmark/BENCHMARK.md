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
| duration (min) | 20.15 | 20.07 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.01 | -0.4% |
| power (W), mean | 629 | 642 | +2.1% |
| power (W), peak | 652 | 686 | +5.1% |
| energy (Wh) | 211 | 215 | +1.6% |
| energy, parked workers still on at idle power (Wh) | 211 | 215 | +1.6% |
| CPU used (cores), mean | 0.874 | 1.22 | +40.0% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.051 | +40.0% |
| energy per core-hour (Wh) | 719 | 524 | -27.1% |
| node-hours per core-hour | 6.87 | 4.90 | -28.6% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.00 | 9.29 | +3.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.800 | +2.1% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 0.865 | 0.091 | -89.4% |
| response time (ms), mean | 159 | 96.48 | -39.3% |
| response time (ms), median | 130 | 82.10 | -36.9% |
| response time (ms), 95th percentile | 329 | 153 | -53.5% |
| response time (ms), 99th percentile | 476 | 208 | -56.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.4538 | 5.4386 | -27.0% | [-3.6641, -0.3413] | GAIN |
| kwh_per_core_hour | 0.7776 | 0.5774 | -25.7% | [-0.3646, -0.0357] | GAIN |
| utilisation | 0.0360 | 0.0519 | +44.1% | [+0.0026, +0.0306] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 0.8466 | +11.1% | [-2.2032, +2.5397] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2618 | 2.5330 | +12.0% | [-4.4650, +5.0794] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.445 0.468 0.487 0.504 0.52 0.534 0.545 0.556 0.562 0.567 0.571 0.576 0.581 0.585 0.588 0.589 0.591
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
| 0 | 6.00 | 6.00 | 615 | 620 | 5.00 | 5.00 | 0.000 | 0.000 | 0.508 | 0.653 |
| 1 | 6.00 | 6.00 | 619 | 622 | 5.25 | 7.00 | 0.000 | 0.000 | 0.617 | 0.723 |
| 2 | 6.00 | 6.00 | 620 | 626 | 6.00 | 7.00 | 0.000 | 0.000 | 0.643 | 0.813 |
| 3 | 6.00 | 6.00 | 621 | 634 | 6.00 | 7.50 | 0.000 | 0.250 | 0.668 | 1.02 |
| 4 | 6.00 | 6.00 | 635 | 646 | 8.50 | 10.00 | 0.000 | 0.000 | 1.03 | 1.36 |
| 5 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.988 | 1.40 |
| 6 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.40 |
| 7 | 6.00 | 6.00 | 646 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.05 |
| 8 | 6.00 | 6.00 | 644 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.09 |
| 9 | 6.00 | 6.00 | 644 | 680 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.24 |
| 10 | 6.00 | 6.00 | 646 | 659 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.74 |
| 11 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.619 | 0.775 |
| 12 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.613 | 0.700 |
| 13 | 6.00 | 6.00 | 624 | 624 | 10.00 | 10.00 | 0.250 | 0.000 | 0.682 | 0.756 |
| 14 | 6.00 | 6.00 | 631 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.945 | 1.42 |
| 15 | 6.00 | 6.00 | 633 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 0.978 | 1.47 |
| 16 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.997 | 1.33 |
| 17 | 6.00 | 6.00 | 627 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.857 | 1.00 |
| 18 | 6.00 | 6.00 | 617 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.595 | 0.719 |
| 19 | 6.00 | 6.00 | 620 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.631 | 0.791 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
