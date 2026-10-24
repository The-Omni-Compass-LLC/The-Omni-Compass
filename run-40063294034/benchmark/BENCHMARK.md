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
| duration (min) | 20.05 | 20.25 |  |
| worker nodes in service, mean | 6.00 | 5.05 | -15.8% |
| worker nodes in service, min | 6.00 | 5.00 | -16.7% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 1.70 | -15.0% |
| power (W), mean | 624 | 566 | -9.2% |
| power (W), peak | 646 | 620 | -4.2% |
| energy (Wh) | 208 | 191 | -8.3% |
| energy, parked workers still on at idle power (Wh) | 208 | 215 | +3.2% |
| CPU used (cores), mean | 0.751 | 1.10 | +46.5% |
| CPU allocatable (cores), mean | 24.00 | 20.20 | -15.8% |
| utilisation (used / allocatable) | 0.031 | 0.054 | +74.1% |
| energy per core-hour (Wh) | 831 | 515 | -38.0% |
| node-hours per core-hour | 7.99 | 4.59 | -42.5% |
| pending pods, pod-minutes | 0.267 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.83 | 9.28 | +5.1% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.800 | +50.0% |
| requests timed | 1,135 | 1,120 | -1.3% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 57.95 | 75.37 | +30.1% |
| response time (ms), median | 40.80 | 68.00 | +66.7% |
| response time (ms), 95th percentile | 129 | 105 | -19.0% |
| response time (ms), 99th percentile | 207 | 134 | -35.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.9789 | 5.2060 | -42.0% | [-5.8684, -1.6541] | GAIN |
| kwh_per_core_hour | 0.9290 | 0.5780 | -37.8% | [-0.5581, -0.1467] | GAIN |
| utilisation | 0.0310 | 0.0541 | +74.4% | [+0.0100, +0.0372] | GAIN |
| pending_pod_minutes_per_hour | 0.7742 | 0.0000 | -100.0% | [-2.3226, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5610 | 2.3227 | +48.8% | [-3.1345, +3.8774] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.417 0.438 0.457 0.473 0.488 0.5 0.512 0.522 0.531 0.536 0.54 0.544 0.548 0.552 0.555 0.557 0.559 0.56
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
| 0 | 6.00 | 6.00 | 614 | 618 | 5.00 | 5.00 | 0.000 | 0.000 | 0.473 | 0.572 |
| 1 | 6.00 | 5.00 | 612 | 549 | 5.00 | 6.00 | 0.000 | 0.000 | 0.436 | 0.731 |
| 2 | 6.00 | 5.00 | 612 | 551 | 5.00 | 7.50 | 0.000 | 0.000 | 0.476 | 0.786 |
| 3 | 6.00 | 5.00 | 616 | 555 | 5.00 | 8.00 | 0.000 | 0.000 | 0.552 | 0.873 |
| 4 | 6.00 | 5.00 | 630 | 571 | 7.25 | 9.50 | 0.000 | 0.000 | 0.905 | 1.30 |
| 5 | 6.00 | 5.00 | 628 | 572 | 10.00 | 10.00 | 0.000 | 0.000 | 0.845 | 1.36 |
| 6 | 6.00 | 5.00 | 628 | 568 | 10.00 | 10.00 | 0.250 | 0.000 | 0.869 | 1.26 |
| 7 | 6.00 | 5.00 | 644 | 585 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 1.68 |
| 8 | 6.00 | 5.00 | 640 | 588 | 10.00 | 10.00 | 0.000 | 0.000 | 1.16 | 1.80 |
| 9 | 6.00 | 5.00 | 642 | 593 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 1.91 |
| 10 | 6.00 | 5.00 | 636 | 578 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.52 |
| 11 | 6.00 | 5.00 | 612 | 547 | 10.00 | 10.00 | 0.000 | 0.000 | 0.456 | 0.693 |
| 12 | 6.00 | 5.00 | 613 | 546 | 10.00 | 10.00 | 0.000 | 0.000 | 0.466 | 0.643 |
| 13 | 6.00 | 5.00 | 616 | 554 | 10.00 | 10.00 | 0.000 | 0.000 | 0.540 | 0.860 |
| 14 | 6.00 | 5.00 | 632 | 569 | 10.00 | 10.00 | 0.000 | 0.000 | 0.947 | 1.27 |
| 15 | 6.00 | 5.00 | 628 | 564 | 10.00 | 10.00 | 0.000 | 0.000 | 0.841 | 1.16 |
| 16 | 6.00 | 5.00 | 630 | 567 | 10.00 | 10.00 | 0.000 | 0.000 | 0.914 | 1.23 |
| 17 | 6.00 | 5.00 | 617 | 558 | 10.00 | 10.00 | 0.000 | 0.000 | 0.571 | 0.966 |
| 18 | 6.00 | 5.00 | 612 | 547 | 10.00 | 10.00 | 0.000 | 0.000 | 0.448 | 0.686 |
| 19 | 6.00 | 5.00 | 614 | 546 | 10.00 | 10.00 | 0.000 | 0.000 | 0.486 | 0.659 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
