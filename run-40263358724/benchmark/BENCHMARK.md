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
| duration (min) | 20.17 | 20.25 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.4% |
| power (W), mean | 627 | 641 | +2.3% |
| power (W), peak | 646 | 693 | +7.2% |
| energy (Wh) | 211 | 216 | +2.8% |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.8% |
| CPU used (cores), mean | 0.830 | 1.22 | +46.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.051 | +46.9% |
| energy per core-hour (Wh) | 755 | 526 | -30.3% |
| node-hours per core-hour | 7.23 | 4.92 | -31.9% |
| pending pods, pod-minutes | 0.250 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.95 | 9.36 | -6.0% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.250 | 0.783 | +213.3% |
| requests timed | 1,120 | 1,095 | -2.2% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 75.87 | 97.19 | +28.1% |
| response time (ms), median | 50.20 | 82.10 | +63.5% |
| response time (ms), 95th percentile | 179 | 159 | -11.2% |
| response time (ms), 99th percentile | 270 | 201 | -25.5% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.8251 | 5.6415 | -27.9% | [-3.9154, -0.4596] | GAIN |
| kwh_per_core_hour | 0.8144 | 0.5976 | -26.6% | [-0.3789, -0.0486] | GAIN |
| utilisation | 0.0343 | 0.0500 | +45.6% | [+0.0034, +0.0290] | GAIN |
| pending_pod_minutes_per_hour | 0.7200 | 0.0000 | -100.0% | [-2.1600, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 0.7317 | 2.2496 | +207.4% | [-1.4634, +5.2250] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.445 0.469 0.488 0.504 0.52 0.534 0.546 0.556 0.562 0.567 0.571 0.577 0.581 0.585 0.588 0.589 0.591
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
| 0 | 6.00 | 6.00 | 617 | 623 | 10.00 | 5.00 | 0.000 | 0.000 | 0.588 | 0.721 |
| 1 | 6.00 | 6.00 | 617 | 624 | 10.00 | 7.00 | 0.000 | 0.000 | 0.567 | 0.736 |
| 2 | 6.00 | 6.00 | 618 | 624 | 10.00 | 7.50 | 0.000 | 0.000 | 0.615 | 0.761 |
| 3 | 6.00 | 6.00 | 620 | 629 | 10.00 | 8.00 | 0.250 | 0.000 | 0.658 | 0.908 |
| 4 | 6.00 | 6.00 | 633 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 0.993 | 1.47 |
| 5 | 6.00 | 6.00 | 631 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 0.938 | 1.28 |
| 6 | 6.00 | 6.00 | 632 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.28 |
| 7 | 6.00 | 6.00 | 644 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.14 |
| 8 | 6.00 | 6.00 | 644 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 2.10 |
| 9 | 6.00 | 6.00 | 643 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 2.13 |
| 10 | 6.00 | 6.00 | 639 | 662 | 10.00 | 10.00 | 0.000 | 0.000 | 1.17 | 1.77 |
| 11 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.559 | 0.770 |
| 12 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.533 | 0.720 |
| 13 | 6.00 | 6.00 | 620 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.651 | 0.996 |
| 14 | 6.00 | 6.00 | 630 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.905 | 1.41 |
| 15 | 6.00 | 6.00 | 629 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 0.900 | 1.49 |
| 16 | 6.00 | 6.00 | 630 | 648 | 9.25 | 10.00 | 0.000 | 0.000 | 0.928 | 1.38 |
| 17 | 6.00 | 6.00 | 624 | 638 | 9.75 | 10.00 | 0.000 | 0.000 | 0.777 | 1.12 |
| 18 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.538 | 0.696 |
| 19 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.563 | 0.774 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
