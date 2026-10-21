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
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.5% |
| power (W), mean | 630 | 631 | +0.2% |
| power (W), peak | 656 | 666 | +1.6% |
| energy (Wh) | 211 | 213 | +0.7% |
| energy, parked workers still on at idle power (Wh) | 211 | 213 | +0.7% |
| CPU used (cores), mean | 0.914 | 0.941 | +3.0% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.039 | +3.0% |
| energy per core-hour (Wh) | 689 | 671 | -2.7% |
| node-hours per core-hour | 6.57 | 6.38 | -2.9% |
| pending pods, pod-minutes | 0.800 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.12 | 9.18 | +0.7% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.800 | 0.000 | -100.0% |
| requests timed | 1,040 | 1,145 | +10.1% |
| time over the response line (% of samples) | 0.577 | 0.000 | -100.0% |
| response time (ms), mean | 155 | 50.42 | -67.5% |
| response time (ms), median | 130 | 43.70 | -66.3% |
| response time (ms), 95th percentile | 306 | 73.18 | -76.1% |
| response time (ms), 99th percentile | 449 | 96.22 | -78.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2207 | 7.2701 | +0.7% | [-1.9665, +2.0503] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7542 | 0.7593 | +0.7% | [-0.1838, +0.2021] | EVEN, no significant difference |
| utilisation | 0.0375 | 0.0388 | +3.4% | [-0.0093, +0.0127] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 2.2979 | 0.0000 | -100.0% | [-6.1318, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2979 | 0.0000 | -100.0% | [-4.5958, +0.0000] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.391 0.42 0.444 0.466 0.485 0.502 0.518 0.531 0.542 0.552 0.558 0.564 0.568 0.573 0.577 0.58 0.583 0.585 0.586
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
| 0 | 6.00 | 6.00 | 618 | 614 | 5.00 | 6.00 | 0.000 | 0.000 | 0.612 | 0.499 |
| 1 | 6.00 | 6.00 | 619 | 615 | 7.00 | 6.00 | 0.000 | 0.000 | 0.627 | 0.511 |
| 2 | 6.00 | 6.00 | 618 | 619 | 7.00 | 6.00 | 0.000 | 0.000 | 0.595 | 0.617 |
| 3 | 6.00 | 6.00 | 623 | 622 | 7.00 | 6.00 | 0.500 | 0.000 | 0.737 | 0.711 |
| 4 | 6.00 | 6.00 | 634 | 636 | 9.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.07 |
| 5 | 6.00 | 6.00 | 632 | 636 | 9.00 | 10.00 | 0.000 | 0.000 | 0.979 | 1.11 |
| 6 | 6.00 | 6.00 | 634 | 644 | 9.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.25 |
| 7 | 6.00 | 6.00 | 650 | 652 | 9.75 | 10.00 | 0.000 | 0.000 | 1.48 | 1.50 |
| 8 | 6.00 | 6.00 | 648 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 1.42 | 1.56 |
| 9 | 6.00 | 6.00 | 646 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 1.58 |
| 10 | 6.00 | 6.00 | 647 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 1.50 |
| 11 | 6.00 | 6.00 | 620 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.633 | 0.538 |
| 12 | 6.00 | 6.00 | 618 | 617 | 10.00 | 10.00 | 0.000 | 0.000 | 0.610 | 0.577 |
| 13 | 6.00 | 6.00 | 624 | 624 | 10.00 | 10.00 | 0.250 | 0.000 | 0.766 | 0.756 |
| 14 | 6.00 | 6.00 | 633 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.997 | 1.08 |
| 15 | 6.00 | 6.00 | 636 | 637 | 10.00 | 10.00 | 0.000 | 0.000 | 1.09 | 1.08 |
| 16 | 6.00 | 6.00 | 635 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.01 |
| 17 | 6.00 | 6.00 | 630 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.930 | 0.727 |
| 18 | 6.00 | 6.00 | 618 | 618 | 10.00 | 10.00 | 0.000 | 0.000 | 0.587 | 0.587 |
| 19 | 6.00 | 6.00 | 617 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.570 | 0.623 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
