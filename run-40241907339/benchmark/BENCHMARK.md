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
| duration (min) | 20.17 | 20.22 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.2% |
| power (W), mean | 627 | 642 | +2.4% |
| power (W), peak | 651 | 686 | +5.3% |
| energy (Wh) | 211 | 216 | +2.6% |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.6% |
| CPU used (cores), mean | 0.849 | 1.23 | +44.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.051 | +44.4% |
| energy per core-hour (Wh) | 739 | 524 | -29.1% |
| node-hours per core-hour | 7.07 | 4.89 | -30.8% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.14 | 9.28 | +1.5% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.03 | 1.02 | -1.6% |
| requests timed | 1,065 | 1,100 | +3.3% |
| time over the response line (% of samples) | 0.094 | 0.000 | -100.0% |
| response time (ms), mean | 127 | 91.91 | -27.7% |
| response time (ms), median | 112 | 80.00 | -28.3% |
| response time (ms), 95th percentile | 266 | 149 | -44.0% |
| response time (ms), 99th percentile | 395 | 175 | -55.8% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.7212 | 5.6325 | -27.1% | [-3.8549, -0.2936] | GAIN |
| kwh_per_core_hour | 0.8035 | 0.5969 | -25.7% | [-0.3769, -0.0288] | GAIN |
| utilisation | 0.0350 | 0.0503 | +43.5% | [+0.0026, +0.0287] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.9756 | 2.8802 | -3.2% | [-5.9024, +4.3433] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.488 0.505 0.52 0.534 0.546 0.556 0.562 0.567 0.571 0.577 0.581 0.585 0.588 0.59 0.591
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
| 0 | 6.00 | 6.00 | 617 | 620 | 5.25 | 5.00 | 0.000 | 0.000 | 0.559 | 0.614 |
| 1 | 6.00 | 6.00 | 618 | 623 | 6.50 | 6.50 | 0.000 | 0.000 | 0.578 | 0.730 |
| 2 | 6.00 | 6.00 | 615 | 621 | 7.00 | 7.00 | 0.000 | 0.000 | 0.566 | 0.683 |
| 3 | 6.00 | 6.00 | 620 | 631 | 7.00 | 7.50 | 0.000 | 0.000 | 0.663 | 0.914 |
| 4 | 6.00 | 6.00 | 631 | 645 | 8.50 | 10.00 | 0.000 | 0.000 | 0.939 | 1.36 |
| 5 | 6.00 | 6.00 | 633 | 650 | 9.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.42 |
| 6 | 6.00 | 6.00 | 633 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.995 | 1.38 |
| 7 | 6.00 | 6.00 | 644 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 1.95 |
| 8 | 6.00 | 6.00 | 644 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.07 |
| 9 | 6.00 | 6.00 | 645 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.03 |
| 10 | 6.00 | 6.00 | 636 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.15 | 1.97 |
| 11 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.542 | 0.774 |
| 12 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.589 | 0.714 |
| 13 | 6.00 | 6.00 | 625 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.774 | 1.08 |
| 14 | 6.00 | 6.00 | 634 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.47 |
| 15 | 6.00 | 6.00 | 629 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 0.903 | 1.52 |
| 16 | 6.00 | 6.00 | 633 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.989 | 1.42 |
| 17 | 6.00 | 6.00 | 624 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.767 | 1.16 |
| 18 | 6.00 | 6.00 | 616 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.581 | 0.773 |
| 19 | 6.00 | 6.00 | 616 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.558 | 0.735 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
