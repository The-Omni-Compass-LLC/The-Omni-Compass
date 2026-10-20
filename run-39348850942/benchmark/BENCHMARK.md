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
| worker nodes in service, mean | 6.00 | 5.05 | -15.8% |
| worker nodes in service, min | 6.00 | 5.00 | -16.7% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 1.70 | -15.7% |
| power (W), mean | 629 | 566 | -10.0% |
| power (W), peak | 654 | 622 | -4.8% |
| energy (Wh) | 212 | 191 | -10.0% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.3% |
| CPU used (cores), mean | 0.906 | 1.09 | +20.4% |
| CPU allocatable (cores), mean | 24.00 | 20.21 | -15.8% |
| utilisation (used / allocatable) | 0.038 | 0.054 | +42.9% |
| energy per core-hour (Wh) | 694 | 519 | -25.3% |
| node-hours per core-hour | 6.62 | 4.63 | -30.0% |
| pending pods, pod-minutes | 0.000 | 0.250 | new |
| pending pods, peak | 0.000 | 1.00 | new |
| HPA replicas, mean | 8.92 | 9.22 | +3.3% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.33 | 0.783 | -41.2% |
| requests timed | 1,040 | 1,115 | +7.2% |
| time over the response line (% of samples) | 0.769 | 0.000 | -100.0% |
| response time (ms), mean | 155 | 76.87 | -50.4% |
| response time (ms), median | 128 | 69.50 | -45.7% |
| response time (ms), 95th percentile | 327 | 111 | -66.0% |
| response time (ms), 99th percentile | 475 | 139 | -70.7% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2350 | 5.3372 | -26.2% | [-3.6475, -0.1446] | GAIN |
| kwh_per_core_hour | 0.7555 | 0.5915 | -21.7% | [-0.3345, +0.0106] | EVEN, no significant difference |
| utilisation | 0.0373 | 0.0537 | +44.2% | [+0.0031, +0.0310] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 0.7680 | n/a | [+0.0000, +2.3040] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.8157 | 2.3164 | -39.3% | [-6.1013, +2.3535] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.416 0.437 0.457 0.473 0.488 0.501 0.513 0.523 0.532 0.536 0.54 0.544 0.549 0.553 0.556 0.559 0.56 0.56
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
| 0 | 6.00 | 6.00 | 617 | 617 | 4.25 | 5.00 | 0.000 | 0.000 | 0.579 | 0.572 |
| 1 | 6.00 | 5.00 | 620 | 545 | 5.75 | 6.00 | 0.000 | 0.000 | 0.630 | 0.638 |
| 2 | 6.00 | 5.00 | 618 | 547 | 6.00 | 7.00 | 0.000 | 0.000 | 0.610 | 0.692 |
| 3 | 6.00 | 5.00 | 624 | 551 | 6.25 | 7.00 | 0.000 | 0.250 | 0.775 | 0.792 |
| 4 | 6.00 | 5.00 | 634 | 569 | 9.00 | 9.75 | 0.000 | 0.000 | 1.04 | 1.27 |
| 5 | 6.00 | 5.00 | 632 | 565 | 9.00 | 10.00 | 0.000 | 0.000 | 0.964 | 1.15 |
| 6 | 6.00 | 5.00 | 636 | 570 | 9.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.29 |
| 7 | 6.00 | 5.00 | 647 | 592 | 9.75 | 10.00 | 0.000 | 0.000 | 1.39 | 1.85 |
| 8 | 6.00 | 5.00 | 645 | 590 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 1.85 |
| 9 | 6.00 | 5.00 | 645 | 588 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 1.79 |
| 10 | 6.00 | 5.00 | 651 | 576 | 10.00 | 10.00 | 0.000 | 0.000 | 1.52 | 1.46 |
| 11 | 6.00 | 5.00 | 618 | 547 | 10.00 | 10.00 | 0.000 | 0.000 | 0.617 | 0.670 |
| 12 | 6.00 | 5.00 | 619 | 546 | 10.00 | 10.00 | 0.000 | 0.000 | 0.625 | 0.648 |
| 13 | 6.00 | 5.00 | 626 | 552 | 10.00 | 10.00 | 0.000 | 0.000 | 0.808 | 0.830 |
| 14 | 6.00 | 5.00 | 633 | 570 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.30 |
| 15 | 6.00 | 5.00 | 638 | 572 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.33 |
| 16 | 6.00 | 5.00 | 632 | 571 | 10.00 | 10.00 | 0.000 | 0.000 | 0.973 | 1.32 |
| 17 | 6.00 | 5.00 | 626 | 556 | 10.00 | 10.00 | 0.000 | 0.000 | 0.811 | 0.913 |
| 18 | 6.00 | 5.00 | 620 | 547 | 10.00 | 10.00 | 0.000 | 0.000 | 0.634 | 0.686 |
| 19 | 6.00 | 5.00 | 616 | 546 | 10.00 | 10.00 | 0.000 | 0.000 | 0.551 | 0.651 |
| 20 |  | 5.00 |  | 549 |  | 10.00 |  | 0.000 |  | 0.722 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
