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
| duration (min) | 20.13 | 20.23 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.5% |
| power (W), mean | 629 | 641 | +2.0% |
| power (W), peak | 650 | 687 | +5.8% |
| energy (Wh) | 211 | 216 | +2.5% |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.5% |
| CPU used (cores), mean | 0.887 | 1.24 | +39.6% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.037 | 0.052 | +39.6% |
| energy per core-hour (Wh) | 709 | 518 | -27.0% |
| node-hours per core-hour | 6.76 | 4.84 | -28.4% |
| pending pods, pod-minutes | 0.533 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.04 | 9.37 | +3.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.500 | -36.2% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 0.481 | 0.000 | -100.0% |
| response time (ms), mean | 155 | 94.55 | -39.0% |
| response time (ms), median | 129 | 81.40 | -36.7% |
| response time (ms), 95th percentile | 308 | 154 | -50.1% |
| response time (ms), 99th percentile | 475 | 195 | -59.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.3314 | 5.5627 | -24.1% | [-3.4518, -0.0967] | GAIN |
| kwh_per_core_hour | 0.7654 | 0.5892 | -23.0% | [-0.3376, -0.0128] | GAIN |
| utilisation | 0.0365 | 0.0508 | +39.2% | [+0.0018, +0.0282] | GAIN |
| pending_pod_minutes_per_hour | 1.5238 | 0.0000 | -100.0% | [-4.5714, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2381 | 1.4343 | -35.9% | [-4.4762, +2.1543] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.469 0.488 0.505 0.521 0.534 0.547 0.557 0.563 0.568 0.572 0.577 0.581 0.584 0.588 0.589 0.59
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
| 0 | 6.00 | 6.00 | 618 | 618 | 5.00 | 6.00 | 0.000 | 0.000 | 0.590 | 0.633 |
| 1 | 6.00 | 6.00 | 618 | 623 | 5.00 | 7.00 | 0.000 | 0.000 | 0.581 | 0.709 |
| 2 | 6.00 | 6.00 | 619 | 625 | 5.50 | 7.00 | 0.000 | 0.000 | 0.613 | 0.761 |
| 3 | 6.00 | 6.00 | 625 | 638 | 6.50 | 7.75 | 0.000 | 0.000 | 0.792 | 1.12 |
| 4 | 6.00 | 6.00 | 633 | 650 | 9.50 | 10.00 | 0.500 | 0.000 | 0.982 | 1.42 |
| 5 | 6.00 | 6.00 | 633 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.984 | 1.30 |
| 6 | 6.00 | 6.00 | 635 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.49 |
| 7 | 6.00 | 6.00 | 644 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.10 |
| 8 | 6.00 | 6.00 | 646 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.06 |
| 9 | 6.00 | 6.00 | 644 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.17 |
| 10 | 6.00 | 6.00 | 640 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 2.11 |
| 11 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.661 | 0.732 |
| 12 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.585 | 0.707 |
| 13 | 6.00 | 6.00 | 624 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.756 | 0.995 |
| 14 | 6.00 | 6.00 | 633 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 0.990 | 1.39 |
| 15 | 6.00 | 6.00 | 632 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.976 | 1.46 |
| 16 | 6.00 | 6.00 | 632 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.971 | 1.35 |
| 17 | 6.00 | 6.00 | 628 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.889 | 1.03 |
| 18 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.589 | 0.766 |
| 19 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.593 | 0.722 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
