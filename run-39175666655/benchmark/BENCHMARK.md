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
| duration (min) | 20.15 | 20.12 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.01 | -0.2% |
| power (W), mean | 630 | 629 | -0.1% |
| power (W), peak | 652 | 662 | +1.4% |
| energy (Wh) | 212 | 211 | -0.3% |
| energy, parked workers still on at idle power (Wh) | 212 | 211 | -0.3% |
| CPU used (cores), mean | 0.914 | 0.886 | -3.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.037 | -3.1% |
| energy per core-hour (Wh) | 689 | 710 | +3.1% |
| node-hours per core-hour | 6.56 | 6.77 | +3.2% |
| pending pods, pod-minutes | 0.533 | 0.267 | -50.0% |
| pending pods, peak | 2.00 | 1.00 | -50.0% |
| HPA replicas, mean | 8.92 | 9.06 | +1.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.30 | 0.533 | -59.0% |
| requests timed | 1,035 | 1,145 | +10.6% |
| time over the response line (% of samples) | 0.870 | 0.000 | -100.0% |
| response time (ms), mean | 161 | 49.04 | -69.5% |
| response time (ms), median | 130 | 43.00 | -67.0% |
| response time (ms), 95th percentile | 324 | 70.30 | -78.3% |
| response time (ms), 99th percentile | 451 | 103 | -77.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.1993 | 7.6345 | +6.0% | [-1.5577, +2.3847] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7524 | 0.7957 | +5.8% | [-0.1446, +0.2369] | EVEN, no significant difference |
| utilisation | 0.0377 | 0.0366 | -2.9% | [-0.0112, +0.0097] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 1.5238 | 0.7805 | -48.8% | [-4.5714, +2.3415] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.7619 | 1.5485 | -58.8% | [-6.7436, +1.6083] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.391 0.42 0.444 0.466 0.485 0.502 0.517 0.53 0.541 0.55 0.557 0.562 0.566 0.571 0.575 0.579 0.583 0.585 0.586
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
| 0 | 6.00 | 6.00 | 616 | 616 | 4.25 | 5.00 | 0.000 | 0.000 | 0.546 | 0.545 |
| 1 | 6.00 | 6.00 | 620 | 615 | 5.00 | 5.75 | 0.000 | 0.000 | 0.622 | 0.541 |
| 2 | 6.00 | 6.00 | 616 | 615 | 6.00 | 6.00 | 0.000 | 0.000 | 0.548 | 0.505 |
| 3 | 6.00 | 6.00 | 623 | 622 | 6.00 | 6.00 | 0.500 | 0.250 | 0.709 | 0.683 |
| 4 | 6.00 | 6.00 | 633 | 634 | 8.50 | 9.00 | 0.000 | 0.000 | 1.02 | 1.01 |
| 5 | 6.00 | 6.00 | 636 | 632 | 9.33 | 10.00 | 0.000 | 0.000 | 1.08 | 0.947 |
| 6 | 6.00 | 6.00 | 638 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 0.949 |
| 7 | 6.00 | 6.00 | 648 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.54 |
| 8 | 6.00 | 6.00 | 647 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.46 |
| 9 | 6.00 | 6.00 | 648 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 1.60 |
| 10 | 6.00 | 6.00 | 647 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.36 |
| 11 | 6.00 | 6.00 | 618 | 618 | 10.00 | 10.00 | 0.000 | 0.000 | 0.622 | 0.598 |
| 12 | 6.00 | 6.00 | 619 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.642 | 0.543 |
| 13 | 6.00 | 6.00 | 627 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.816 | 0.675 |
| 14 | 6.00 | 6.00 | 636 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.04 |
| 15 | 6.00 | 6.00 | 636 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 0.926 |
| 16 | 6.00 | 6.00 | 632 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.987 | 1.05 |
| 17 | 6.00 | 6.00 | 627 | 629 | 10.00 | 10.00 | 0.000 | 0.000 | 0.865 | 0.869 |
| 18 | 6.00 | 6.00 | 620 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.605 | 0.525 |
| 19 | 6.00 | 6.00 | 620 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.632 | 0.549 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
