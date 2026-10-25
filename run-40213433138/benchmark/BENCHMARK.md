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
| duration (min) | 20.07 | 20.27 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.03 | +1.0% |
| power (W), mean | 625 | 642 | +2.7% |
| power (W), peak | 648 | 682 | +5.3% |
| energy (Wh) | 209 | 217 | +3.7% |
| energy, parked workers still on at idle power (Wh) | 209 | 217 | +3.7% |
| CPU used (cores), mean | 0.780 | 1.23 | +58.0% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.032 | 0.051 | +58.0% |
| energy per core-hour (Wh) | 802 | 521 | -35.0% |
| node-hours per core-hour | 7.70 | 4.87 | -36.7% |
| pending pods, pod-minutes | 0.500 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.59 | 9.41 | +9.5% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.517 | -34.0% |
| requests timed | 1,130 | 1,100 | -2.7% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 65.51 | 95.69 | +46.1% |
| response time (ms), median | 45.10 | 81.35 | +80.4% |
| response time (ms), 95th percentile | 156 | 156 | -0.3% |
| response time (ms), 99th percentile | 243 | 177 | -27.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.6082 | 5.5950 | -35.0% | [-5.1760, -0.9632] | GAIN |
| kwh_per_core_hour | 0.8926 | 0.5929 | -33.6% | [-0.5070, -0.0990] | GAIN |
| utilisation | 0.0322 | 0.0505 | +57.0% | [+0.0058, +0.0321] | GAIN |
| pending_pod_minutes_per_hour | 1.4575 | 0.0000 | -100.0% | [-3.6408, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.3352 | 1.5238 | -34.7% | [-4.6952, +2.2857] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.468 0.488 0.504 0.52 0.534 0.546 0.556 0.561 0.566 0.571 0.576 0.581 0.585 0.588 0.589 0.591
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
| 0 | 6.00 | 6.00 | 613 | 619 | 4.00 | 6.00 | 0.000 | 0.000 | 0.450 | 0.632 |
| 1 | 6.00 | 6.00 | 613 | 624 | 4.00 | 6.50 | 0.000 | 0.000 | 0.429 | 0.774 |
| 2 | 6.00 | 6.00 | 615 | 624 | 4.00 | 8.00 | 0.000 | 0.000 | 0.467 | 0.756 |
| 3 | 6.00 | 6.00 | 616 | 631 | 4.00 | 8.00 | 0.250 | 0.000 | 0.557 | 0.953 |
| 4 | 6.00 | 6.00 | 629 | 644 | 7.50 | 10.00 | 0.000 | 0.000 | 0.875 | 1.32 |
| 5 | 6.00 | 6.00 | 628 | 650 | 9.00 | 10.00 | 0.000 | 0.000 | 0.876 | 1.45 |
| 6 | 6.00 | 6.00 | 630 | 652 | 10.00 | 10.00 | 0.250 | 0.000 | 0.918 | 1.50 |
| 7 | 6.00 | 6.00 | 640 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.19 | 2.04 |
| 8 | 6.00 | 6.00 | 642 | 677 | 10.00 | 10.00 | 0.000 | 0.000 | 1.23 | 2.15 |
| 9 | 6.00 | 6.00 | 643 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 2.07 |
| 10 | 6.00 | 6.00 | 641 | 666 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 1.86 |
| 11 | 6.00 | 6.00 | 616 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.545 | 0.727 |
| 12 | 6.00 | 6.00 | 616 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.509 | 0.776 |
| 13 | 6.00 | 6.00 | 622 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.685 | 0.886 |
| 14 | 6.00 | 6.00 | 632 | 653 | 10.00 | 10.00 | 0.000 | 0.000 | 0.985 | 1.52 |
| 15 | 6.00 | 6.00 | 628 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 0.859 | 1.55 |
| 16 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.952 | 1.32 |
| 17 | 6.00 | 6.00 | 622 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.669 | 1.17 |
| 18 | 6.00 | 6.00 | 614 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.498 | 0.720 |
| 19 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.522 | 0.772 |
| 20 |  | 6.00 |  | 627 |  | 10.00 |  | 0.000 |  | 0.806 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
