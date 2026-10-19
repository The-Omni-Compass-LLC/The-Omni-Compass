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
| duration (min) | 20.13 | 20.03 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.00 | -0.5% |
| power (W), mean | 630 | 638 | +1.3% |
| power (W), peak | 651 | 678 | +4.1% |
| energy (Wh) | 211 | 213 | +0.8% |
| energy, parked workers still on at idle power (Wh) | 211 | 213 | +0.8% |
| CPU used (cores), mean | 0.908 | 1.13 | +24.8% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.047 | +24.8% |
| energy per core-hour (Wh) | 694 | 564 | -18.8% |
| node-hours per core-hour | 6.61 | 5.30 | -19.8% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.06 | 9.29 | +2.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.800 | +50.0% |
| requests timed | 1,040 | 1,120 | +7.7% |
| time over the response line (% of samples) | 0.385 | 0.000 | -100.0% |
| response time (ms), mean | 158 | 75.20 | -52.3% |
| response time (ms), median | 131 | 68.70 | -47.5% |
| response time (ms), 95th percentile | 325 | 105 | -67.7% |
| response time (ms), 99th percentile | 451 | 131 | -71.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2053 | 6.0854 | -15.5% | [-2.8367, +0.6101] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7528 | 0.6416 | -14.8% | [-0.2709, +0.0581] | EVEN, no significant difference |
| utilisation | 0.0373 | 0.0463 | +24.2% | [-0.0029, +0.0220] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.7619 | 0.7805 | +2.4% | [-2.2857, +2.3415] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4877 | 2.2864 | +53.7% | [-2.2496, +4.5612] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.445 0.468 0.488 0.504 0.519 0.533 0.545 0.555 0.561 0.566 0.571 0.576 0.58 0.584 0.587 0.588 0.589
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
| 0 | 6.00 | 6.00 | 617 | 625 | 5.00 | 5.25 | 0.000 | 0.000 | 0.566 | 0.789 |
| 1 | 6.00 | 6.00 | 624 | 620 | 5.75 | 6.00 | 0.000 | 0.000 | 0.756 | 0.654 |
| 2 | 6.00 | 6.00 | 619 | 625 | 6.00 | 7.00 | 0.000 | 0.250 | 0.644 | 0.744 |
| 3 | 6.00 | 6.00 | 622 | 626 | 6.00 | 8.00 | 0.000 | 0.000 | 0.709 | 0.838 |
| 4 | 6.00 | 6.00 | 636 | 646 | 9.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.28 |
| 5 | 6.00 | 6.00 | 634 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.30 |
| 6 | 6.00 | 6.00 | 635 | 642 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.26 |
| 7 | 6.00 | 6.00 | 647 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 1.85 |
| 8 | 6.00 | 6.00 | 648 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 1.94 |
| 9 | 6.00 | 6.00 | 648 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 2.03 |
| 10 | 6.00 | 6.00 | 639 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.16 | 1.46 |
| 11 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.573 | 0.778 |
| 12 | 6.00 | 6.00 | 618 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.595 | 0.690 |
| 13 | 6.00 | 6.00 | 625 | 626 | 10.00 | 10.00 | 0.250 | 0.000 | 0.764 | 0.815 |
| 14 | 6.00 | 6.00 | 635 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.30 |
| 15 | 6.00 | 6.00 | 633 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.34 |
| 16 | 6.00 | 6.00 | 632 | 642 | 10.00 | 10.00 | 0.000 | 0.000 | 0.954 | 1.22 |
| 17 | 6.00 | 6.00 | 626 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.820 | 0.805 |
| 18 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.592 | 0.702 |
| 19 | 6.00 | 6.00 | 618 | 617 | 10.00 | 10.00 | 0.000 | 0.000 | 0.619 | 0.600 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
