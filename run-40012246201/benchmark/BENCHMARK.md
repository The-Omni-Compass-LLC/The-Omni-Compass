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
| duration (min) | 20.15 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.2% |
| power (W), mean | 630 | 636 | +1.0% |
| power (W), peak | 656 | 676 | +3.2% |
| energy (Wh) | 212 | 213 | +0.7% |
| energy, parked workers still on at idle power (Wh) | 212 | 213 | +0.7% |
| CPU used (cores), mean | 0.909 | 1.07 | +17.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.038 | 0.045 | +17.9% |
| energy per core-hour (Wh) | 693 | 593 | -14.4% |
| node-hours per core-hour | 6.60 | 5.60 | -15.2% |
| pending pods, pod-minutes | 0.250 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.33 | 9.20 | -1.4% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.250 | 0.767 | +206.7% |
| requests timed | 1,040 | 1,130 | +8.7% |
| time over the response line (% of samples) | 0.769 | 0.000 | -100.0% |
| response time (ms), mean | 156 | 64.13 | -59.0% |
| response time (ms), median | 129 | 57.00 | -55.7% |
| response time (ms), 95th percentile | 327 | 92.95 | -71.6% |
| response time (ms), 99th percentile | 480 | 111 | -76.8% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2821 | 6.3638 | -12.6% | [-2.8069, +0.9663] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7604 | 0.6692 | -12.0% | [-0.2667, +0.0923] | EVEN, no significant difference |
| utilisation | 0.0374 | 0.0440 | +17.6% | [-0.0047, +0.0184] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.7258 | 0.0000 | -100.0% | [-2.1774, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 0.7143 | 2.2381 | +213.3% | [-1.4286, +5.1905] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.467 0.486 0.503 0.517 0.53 0.542 0.552 0.558 0.563 0.568 0.573 0.578 0.582 0.585 0.586 0.587
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
| 0 | 6.00 | 6.00 | 616 | 617 | 7.00 | 4.50 | 0.000 | 0.000 | 0.541 | 0.558 |
| 1 | 6.00 | 6.00 | 617 | 620 | 7.00 | 6.00 | 0.000 | 0.000 | 0.583 | 0.645 |
| 2 | 6.00 | 6.00 | 616 | 622 | 7.00 | 6.00 | 0.000 | 0.000 | 0.544 | 0.705 |
| 3 | 6.00 | 6.00 | 622 | 624 | 7.00 | 8.00 | 0.000 | 0.000 | 0.723 | 0.775 |
| 4 | 6.00 | 6.00 | 638 | 644 | 9.00 | 10.00 | 0.000 | 0.000 | 1.09 | 1.29 |
| 5 | 6.00 | 6.00 | 631 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.961 | 1.18 |
| 6 | 6.00 | 6.00 | 634 | 637 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.13 |
| 7 | 6.00 | 6.00 | 647 | 663 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 1.79 |
| 8 | 6.00 | 6.00 | 650 | 660 | 10.00 | 10.00 | 0.000 | 0.000 | 1.42 | 1.72 |
| 9 | 6.00 | 6.00 | 649 | 662 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 1.75 |
| 10 | 6.00 | 6.00 | 648 | 655 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.57 |
| 11 | 6.00 | 6.00 | 620 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.636 | 0.682 |
| 12 | 6.00 | 6.00 | 620 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.633 | 0.605 |
| 13 | 6.00 | 6.00 | 624 | 626 | 10.00 | 10.00 | 0.250 | 0.000 | 0.753 | 0.821 |
| 14 | 6.00 | 6.00 | 632 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.979 | 1.12 |
| 15 | 6.00 | 6.00 | 637 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.34 |
| 16 | 6.00 | 6.00 | 636 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.23 |
| 17 | 6.00 | 6.00 | 627 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.880 | 1.14 |
| 18 | 6.00 | 6.00 | 618 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.602 | 0.644 |
| 19 | 6.00 | 6.00 | 620 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.643 | 0.676 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
