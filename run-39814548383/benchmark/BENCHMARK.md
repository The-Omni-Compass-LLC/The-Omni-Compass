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
| duration (min) | 20.25 | 20.08 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.8% |
| power (W), mean | 628 | 643 | +2.4% |
| power (W), peak | 650 | 688 | +6.0% |
| energy (Wh) | 212 | 215 | +1.5% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.5% |
| CPU used (cores), mean | 0.872 | 1.27 | +45.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.053 | +45.9% |
| energy per core-hour (Wh) | 721 | 506 | -29.8% |
| node-hours per core-hour | 6.88 | 4.72 | -31.5% |
| pending pods, pod-minutes | 0.533 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.93 | 9.50 | +6.5% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.517 | +0.0% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 0.962 | 0.000 | -100.0% |
| response time (ms), mean | 156 | 100 | -35.9% |
| response time (ms), median | 130 | 90.90 | -29.9% |
| response time (ms), 95th percentile | 314 | 143 | -54.7% |
| response time (ms), 99th percentile | 488 | 178 | -63.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.5719 | 5.1734 | -31.7% | [-4.0150, -0.7241] | GAIN |
| kwh_per_core_hour | 0.7895 | 0.5511 | -30.2% | [-0.3980, -0.0733] | GAIN |
| utilisation | 0.0359 | 0.0538 | +50.0% | [+0.0047, +0.0327] | GAIN |
| pending_pod_minutes_per_hour | 1.5238 | 0.0000 | -100.0% | [-4.5714, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4706 | 1.6466 | +12.0% | [-2.2325, +2.6783] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 80 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.33 0.34 0.35 0.359 0.368 0.376 0.384 0.392 0.4 0.407 0.414 0.421 0.428 0.434 0.44 0.447 0.453 0.458 0.464 0.469 0.474 0.479 0.484 0.489 0.493 0.497 0.501 0.505 0.509 0.513 0.517 0.521 0.525 0.528 0.531 0.535 0.538 0.541 0.544 0.547 0.549 0.552 0.555 0.557 0.558 0.559 0.561 0.562 0.564 0.565 0.566 0.567 0.569 0.57 0.571 0.572 0.574 0.575 0.576 0.577 0.578 0.579 0.581 0.582 0.583 0.583 0.584 0.585 0.586 0.587 0.588 0.588 0.588 0.589 0.589 0.589 0.59 0.59 0.59 0.591
- nodes decided per minute: 6 6 6 6 6 6 6 5 5 5 5 4 4 4 4 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
- HPA target decided per minute (%): 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77

## Reset

```
restored target: 50
workers in service: 6 of 6
Omni records left after kill: none
```

## Minute by minute

| min | nodes native | nodes omni | power W native | power W omni | replicas native | replicas omni | pending native | pending omni | CPU native | CPU omni |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.00 | 6.00 | 616 | 622 | 5.00 | 6.00 | 0.000 | 0.000 | 0.542 | 0.710 |
| 1 | 6.00 | 6.00 | 620 | 625 | 5.00 | 8.00 | 0.000 | 0.000 | 0.623 | 0.789 |
| 2 | 6.00 | 6.00 | 616 | 624 | 5.00 | 8.00 | 0.000 | 0.000 | 0.542 | 0.754 |
| 3 | 6.00 | 6.00 | 622 | 636 | 5.25 | 8.50 | 0.500 | 0.000 | 0.692 | 1.07 |
| 4 | 6.00 | 6.00 | 636 | 648 | 9.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.40 |
| 5 | 6.00 | 6.00 | 634 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.34 |
| 6 | 6.00 | 6.00 | 634 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.39 |
| 7 | 6.00 | 6.00 | 647 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.99 |
| 8 | 6.00 | 6.00 | 644 | 679 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.23 |
| 9 | 6.00 | 6.00 | 649 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 2.22 |
| 10 | 6.00 | 6.00 | 639 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.15 | 1.97 |
| 11 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.588 | 0.735 |
| 12 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.577 | 0.808 |
| 13 | 6.00 | 6.00 | 624 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.739 | 1.04 |
| 14 | 6.00 | 6.00 | 634 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.42 |
| 15 | 6.00 | 6.00 | 630 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.940 | 1.44 |
| 16 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.963 | 1.42 |
| 17 | 6.00 | 6.00 | 625 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.771 | 1.16 |
| 18 | 6.00 | 6.00 | 620 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.637 | 0.705 |
| 19 | 6.00 | 6.00 | 619 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.605 | 0.851 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
