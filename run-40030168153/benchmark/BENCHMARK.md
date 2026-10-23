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
| duration (min) | 20.18 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.4% |
| power (W), mean | 627 | 630 | +0.5% |
| power (W), peak | 656 | 674 | +2.7% |
| energy (Wh) | 211 | 211 | +0.1% |
| energy, parked workers still on at idle power (Wh) | 211 | 211 | +0.1% |
| CPU used (cores), mean | 0.843 | 0.922 | +9.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.038 | +9.4% |
| energy per core-hour (Wh) | 744 | 684 | -8.2% |
| node-hours per core-hour | 7.12 | 6.51 | -8.6% |
| pending pods, pod-minutes | 0.000 | 0.250 | new |
| pending pods, peak | 0.000 | 1.00 | new |
| HPA replicas, mean | 8.85 | 9.04 | +2.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.05 | 0.767 | -27.0% |
| requests timed | 1,070 | 1,150 | +7.5% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 123 | 47.78 | -61.1% |
| response time (ms), median | 112 | 42.40 | -62.1% |
| response time (ms), 95th percentile | 252 | 71.70 | -71.5% |
| response time (ms), 99th percentile | 333 | 93.57 | -71.9% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.8426 | 7.4440 | -5.1% | [-2.5462, +1.7122] | EVEN, no significant difference |
| kwh_per_core_hour | 0.8162 | 0.7768 | -4.8% | [-0.2419, +0.1650] | EVEN, no significant difference |
| utilisation | 0.0348 | 0.0380 | +9.3% | [-0.0072, +0.0145] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.0000 | 0.7200 | n/a | [+0.0000, +2.1600] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.0360 | 2.2439 | -26.1% | [-5.2918, +3.7198] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.444 0.466 0.485 0.501 0.516 0.531 0.542 0.551 0.557 0.563 0.567 0.572 0.577 0.581 0.584 0.585 0.587
- nodes decided per minute: 6 6 5 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 616 | 614 | 4.75 | 5.00 | 0.000 | 0.000 | 0.528 | 0.474 |
| 1 | 6.00 | 6.00 | 615 | 620 | 5.00 | 5.75 | 0.000 | 0.000 | 0.517 | 0.629 |
| 2 | 6.00 | 6.00 | 615 | 615 | 5.00 | 6.00 | 0.000 | 0.000 | 0.508 | 0.511 |
| 3 | 6.00 | 6.00 | 622 | 620 | 5.25 | 6.00 | 0.000 | 0.250 | 0.705 | 0.658 |
| 4 | 6.00 | 6.00 | 632 | 636 | 7.50 | 8.50 | 0.000 | 0.000 | 0.968 | 1.06 |
| 5 | 6.00 | 6.00 | 628 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.890 | 1.05 |
| 6 | 6.00 | 6.00 | 634 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.07 |
| 7 | 6.00 | 6.00 | 646 | 660 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 1.69 |
| 8 | 6.00 | 6.00 | 648 | 657 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.62 |
| 9 | 6.00 | 6.00 | 646 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.56 |
| 10 | 6.00 | 6.00 | 639 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.15 | 1.46 |
| 11 | 6.00 | 6.00 | 616 | 618 | 10.00 | 10.00 | 0.000 | 0.000 | 0.574 | 0.579 |
| 12 | 6.00 | 6.00 | 617 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.563 | 0.505 |
| 13 | 6.00 | 6.00 | 621 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.688 | 0.686 |
| 14 | 6.00 | 6.00 | 632 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.936 | 1.09 |
| 15 | 6.00 | 6.00 | 633 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.991 | 1.05 |
| 16 | 6.00 | 6.00 | 633 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.02 |
| 17 | 6.00 | 6.00 | 625 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.746 | 0.794 |
| 18 | 6.00 | 6.00 | 616 | 618 | 10.00 | 10.00 | 0.000 | 0.000 | 0.549 | 0.566 |
| 19 | 6.00 | 6.00 | 616 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.553 | 0.541 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
