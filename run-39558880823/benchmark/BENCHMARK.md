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
| duration (min) | 20.00 | 20.03 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.00 | +0.2% |
| power (W), mean | 629 | 629 | -0.1% |
| power (W), peak | 652 | 664 | +1.8% |
| energy (Wh) | 210 | 210 | +0.1% |
| energy, parked workers still on at idle power (Wh) | 210 | 210 | +0.1% |
| CPU used (cores), mean | 0.893 | 0.880 | -1.5% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.037 | -1.5% |
| energy per core-hour (Wh) | 705 | 715 | +1.4% |
| node-hours per core-hour | 6.72 | 6.82 | +1.5% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.02 | 9.01 | -0.0% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.783 | +0.0% |
| requests timed | 1,035 | 1,150 | +11.1% |
| time over the response line (% of samples) | 0.290 | 0.000 | -100.0% |
| response time (ms), mean | 163 | 44.65 | -72.7% |
| response time (ms), median | 135 | 38.90 | -71.1% |
| response time (ms), 95th percentile | 321 | 66.66 | -79.2% |
| response time (ms), 99th percentile | 428 | 85.51 | -80.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 9, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.1153 | 7.7231 | +8.5% | [-1.3944, +2.6454] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7441 | 0.8045 | +8.1% | [-0.1351, +0.2587] | EVEN, no significant difference |
| utilisation | 0.0379 | 0.0363 | -4.2% | [-0.0118, +0.0090] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.8466 | 0.7805 | -7.8% | [-2.5397, +2.3415] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.4935 | 2.2685 | -9.0% | [-4.4318, +4.3848] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.391 0.42 0.444 0.467 0.486 0.502 0.518 0.531 0.541 0.55 0.556 0.562 0.567 0.572 0.577 0.58 0.583 0.585 0.586
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
| 0 | 6.00 | 6.00 | 618 | 616 | 4.75 | 4.00 | 0.000 | 0.000 | 0.545 | 0.512 |
| 1 | 6.00 | 6.00 | 620 | 615 | 5.00 | 6.00 | 0.000 | 0.000 | 0.625 | 0.499 |
| 2 | 6.00 | 6.00 | 620 | 616 | 5.50 | 6.00 | 0.000 | 0.000 | 0.646 | 0.527 |
| 3 | 6.00 | 6.00 | 622 | 620 | 6.00 | 6.00 | 0.250 | 0.250 | 0.706 | 0.666 |
| 4 | 6.00 | 6.00 | 632 | 636 | 10.00 | 8.75 | 0.000 | 0.000 | 0.970 | 1.08 |
| 5 | 6.00 | 6.00 | 632 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.974 | 0.977 |
| 6 | 6.00 | 6.00 | 633 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.984 | 1.02 |
| 7 | 6.00 | 6.00 | 646 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.58 |
| 8 | 6.00 | 6.00 | 649 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.35 |
| 9 | 6.00 | 6.00 | 648 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.42 | 1.47 |
| 10 | 6.00 | 6.00 | 641 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.19 | 1.39 |
| 11 | 6.00 | 6.00 | 616 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.562 | 0.504 |
| 12 | 6.00 | 6.00 | 619 | 617 | 10.00 | 10.00 | 0.000 | 0.000 | 0.623 | 0.527 |
| 13 | 6.00 | 6.00 | 625 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.789 | 0.691 |
| 14 | 6.00 | 6.00 | 634 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.08 |
| 15 | 6.00 | 6.00 | 637 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 0.963 |
| 16 | 6.00 | 6.00 | 632 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.973 | 0.979 |
| 17 | 6.00 | 6.00 | 627 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.844 | 0.810 |
| 18 | 6.00 | 6.00 | 620 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.643 | 0.521 |
| 19 | 6.00 | 6.00 | 619 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.591 | 0.536 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
