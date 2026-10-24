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
| duration (min) | 20.17 | 20.23 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.3% |
| power (W), mean | 628 | 638 | +1.7% |
| power (W), peak | 651 | 672 | +3.2% |
| energy (Wh) | 211 | 215 | +2.0% |
| energy, parked workers still on at idle power (Wh) | 211 | 215 | +2.0% |
| CPU used (cores), mean | 0.860 | 1.13 | +31.5% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.047 | +31.5% |
| energy per core-hour (Wh) | 730 | 564 | -22.7% |
| node-hours per core-hour | 6.98 | 5.31 | -24.0% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.16 | 9.21 | +0.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.517 | +0.0% |
| requests timed | 1,070 | 1,120 | +4.7% |
| time over the response line (% of samples) | 0.280 | 0.000 | -100.0% |
| response time (ms), mean | 125 | 76.05 | -39.3% |
| response time (ms), median | 112 | 68.40 | -39.0% |
| response time (ms), 95th percentile | 253 | 105 | -58.4% |
| response time (ms), 99th percentile | 351 | 122 | -65.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.5973 | 6.0238 | -20.7% | [-3.4026, +0.2544] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7917 | 0.6356 | -19.7% | [-0.3278, +0.0210] | EVEN, no significant difference |
| utilisation | 0.0355 | 0.0466 | +31.3% | [-0.0004, +0.0235] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4634 | 1.4942 | +2.1% | [-2.2068, +2.9342] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.391 0.42 0.445 0.468 0.487 0.504 0.52 0.533 0.545 0.555 0.56 0.566 0.57 0.575 0.58 0.584 0.586 0.588 0.589
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
| 0 | 6.00 | 6.00 | 618 | 617 | 6.00 | 6.00 | 0.000 | 0.000 | 0.597 | 0.575 |
| 1 | 6.00 | 6.00 | 618 | 621 | 6.00 | 6.00 | 0.000 | 0.000 | 0.585 | 0.668 |
| 2 | 6.00 | 6.00 | 617 | 624 | 6.00 | 6.25 | 0.000 | 0.000 | 0.575 | 0.741 |
| 3 | 6.00 | 6.00 | 620 | 628 | 6.00 | 7.00 | 0.000 | 0.000 | 0.619 | 0.860 |
| 4 | 6.00 | 6.00 | 634 | 644 | 9.50 | 9.25 | 0.000 | 0.000 | 1.02 | 1.30 |
| 5 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.989 | 1.38 |
| 6 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.38 |
| 7 | 6.00 | 6.00 | 643 | 664 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 1.83 |
| 8 | 6.00 | 6.00 | 645 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 1.95 |
| 9 | 6.00 | 6.00 | 643 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 1.84 |
| 10 | 6.00 | 6.00 | 644 | 660 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 1.73 |
| 11 | 6.00 | 6.00 | 617 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.578 | 0.664 |
| 12 | 6.00 | 6.00 | 617 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.604 | 0.721 |
| 13 | 6.00 | 6.00 | 623 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.734 | 0.850 |
| 14 | 6.00 | 6.00 | 632 | 642 | 10.00 | 10.00 | 0.000 | 0.000 | 0.974 | 1.21 |
| 15 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.31 |
| 16 | 6.00 | 6.00 | 630 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.933 | 1.29 |
| 17 | 6.00 | 6.00 | 625 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.784 | 0.989 |
| 18 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.573 | 0.715 |
| 19 | 6.00 | 6.00 | 617 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.573 | 0.695 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
