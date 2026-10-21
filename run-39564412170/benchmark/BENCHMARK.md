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
| duration (min) | 20.08 | 20.20 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.6% |
| power (W), mean | 627 | 641 | +2.1% |
| power (W), peak | 651 | 682 | +4.8% |
| energy (Wh) | 210 | 216 | +2.7% |
| energy, parked workers still on at idle power (Wh) | 210 | 216 | +2.7% |
| CPU used (cores), mean | 0.857 | 1.21 | +41.8% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.051 | +41.8% |
| energy per core-hour (Wh) | 732 | 528 | -28.0% |
| node-hours per core-hour | 7.00 | 4.94 | -29.5% |
| pending pods, pod-minutes | 0.800 | 0.000 | -100.0% |
| pending pods, peak | 3.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.77 | 9.46 | +7.9% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.05 | 0.800 | -23.8% |
| requests timed | 1,095 | 1,100 | +0.5% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 97.13 | 94.49 | -2.7% |
| response time (ms), median | 85.80 | 82.30 | -4.1% |
| response time (ms), 95th percentile | 211 | 152 | -27.8% |
| response time (ms), 99th percentile | 319 | 192 | -39.9% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.6975 | 5.6893 | -26.1% | [-3.8335, -0.2017] | GAIN |
| kwh_per_core_hour | 0.8011 | 0.6018 | -24.9% | [-0.3746, -0.0241] | GAIN |
| utilisation | 0.0352 | 0.0497 | +41.0% | [+0.0020, +0.0281] | GAIN |
| pending_pod_minutes_per_hour | 2.3040 | 0.0000 | -100.0% | [-6.9120, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.0237 | 2.2857 | -24.4% | [-5.2372, +3.8095] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.488 0.505 0.521 0.534 0.547 0.557 0.562 0.567 0.571 0.577 0.581 0.585 0.588 0.59 0.591
- nodes decided per minute: 6 5 5 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 615 | 618 | 4.00 | 5.00 | 0.000 | 0.000 | 0.510 | 0.599 |
| 1 | 6.00 | 6.00 | 617 | 624 | 4.75 | 7.00 | 0.000 | 0.000 | 0.566 | 0.763 |
| 2 | 6.00 | 6.00 | 616 | 626 | 5.00 | 8.50 | 0.000 | 0.000 | 0.552 | 0.806 |
| 3 | 6.00 | 6.00 | 623 | 634 | 5.75 | 9.00 | 0.750 | 0.000 | 0.712 | 1.02 |
| 4 | 6.00 | 6.00 | 633 | 644 | 9.00 | 10.00 | 0.000 | 0.000 | 0.984 | 1.26 |
| 5 | 6.00 | 6.00 | 632 | 652 | 9.00 | 10.00 | 0.000 | 0.000 | 0.954 | 1.52 |
| 6 | 6.00 | 6.00 | 632 | 650 | 9.00 | 10.00 | 0.000 | 0.000 | 0.939 | 1.48 |
| 7 | 6.00 | 6.00 | 642 | 672 | 9.50 | 10.00 | 0.000 | 0.000 | 1.23 | 2.06 |
| 8 | 6.00 | 6.00 | 644 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 2.02 |
| 9 | 6.00 | 6.00 | 649 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 2.22 |
| 10 | 6.00 | 6.00 | 639 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 1.89 |
| 11 | 6.00 | 6.00 | 614 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.563 | 0.681 |
| 12 | 6.00 | 6.00 | 616 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.539 | 0.728 |
| 13 | 6.00 | 6.00 | 621 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.686 | 0.956 |
| 14 | 6.00 | 6.00 | 632 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.980 | 1.42 |
| 15 | 6.00 | 6.00 | 632 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.985 | 1.32 |
| 16 | 6.00 | 6.00 | 631 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.949 | 1.30 |
| 17 | 6.00 | 6.00 | 624 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.943 | 1.04 |
| 18 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.552 | 0.762 |
| 19 | 6.00 | 6.00 | 617 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.585 | 0.710 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
