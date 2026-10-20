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
| duration (min) | 20.25 | 20.15 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.5% |
| power (W), mean | 629 | 631 | +0.2% |
| power (W), peak | 652 | 672 | +3.0% |
| energy (Wh) | 212 | 212 | -0.3% |
| energy, parked workers still on at idle power (Wh) | 212 | 212 | -0.3% |
| CPU used (cores), mean | 0.900 | 0.920 | +2.2% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.038 | +2.2% |
| energy per core-hour (Wh) | 700 | 686 | -2.0% |
| node-hours per core-hour | 6.67 | 6.52 | -2.2% |
| pending pods, pod-minutes | 0.267 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.99 | 9.09 | +1.1% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.783 | +0.0% |
| requests timed | 1,035 | 1,145 | +10.6% |
| time over the response line (% of samples) | 1.26 | 0.000 | -100.0% |
| response time (ms), mean | 162 | 49.15 | -69.7% |
| response time (ms), median | 134 | 44.30 | -66.9% |
| response time (ms), 95th percentile | 316 | 72.38 | -77.1% |
| response time (ms), 99th percentile | 517 | 86.05 | -83.4% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2857 | 7.2803 | -0.1% | [-1.9066, +1.8199] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7607 | 0.7607 | -0.0% | [-0.1777, +0.1802] | EVEN, no significant difference |
| utilisation | 0.0370 | 0.0380 | +2.6% | [-0.0090, +0.0118] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.7619 | 0.0000 | -100.0% | [-2.2857, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2442 | 2.3102 | +2.9% | [-3.7142, +3.1444] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.467 0.486 0.502 0.518 0.531 0.542 0.552 0.558 0.563 0.567 0.572 0.576 0.579 0.583 0.584 0.586
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
| 0 | 6.00 | 6.00 | 615 | 617 | 5.00 | 5.00 | 0.000 | 0.000 | 0.524 | 0.547 |
| 1 | 6.00 | 6.00 | 619 | 618 | 5.00 | 5.75 | 0.000 | 0.000 | 0.613 | 0.581 |
| 2 | 6.00 | 6.00 | 619 | 620 | 5.75 | 6.00 | 0.000 | 0.000 | 0.606 | 0.632 |
| 3 | 6.00 | 6.00 | 624 | 626 | 6.00 | 6.00 | 0.250 | 0.000 | 0.742 | 0.789 |
| 4 | 6.00 | 6.00 | 635 | 636 | 9.00 | 9.50 | 0.000 | 0.000 | 1.04 | 1.05 |
| 5 | 6.00 | 6.00 | 636 | 639 | 9.67 | 10.00 | 0.000 | 0.000 | 1.08 | 1.14 |
| 6 | 6.00 | 6.00 | 636 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 0.937 |
| 7 | 6.00 | 6.00 | 647 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 1.43 |
| 8 | 6.00 | 6.00 | 645 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 1.59 |
| 9 | 6.00 | 6.00 | 646 | 657 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 1.63 |
| 10 | 6.00 | 6.00 | 641 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.37 |
| 11 | 6.00 | 6.00 | 619 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.621 | 0.520 |
| 12 | 6.00 | 6.00 | 619 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.599 | 0.541 |
| 13 | 6.00 | 6.00 | 624 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.755 | 0.720 |
| 14 | 6.00 | 6.00 | 637 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 1.09 | 1.07 |
| 15 | 6.00 | 6.00 | 633 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.988 | 0.945 |
| 16 | 6.00 | 6.00 | 636 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.03 |
| 17 | 6.00 | 6.00 | 626 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.801 | 0.740 |
| 18 | 6.00 | 6.00 | 620 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.626 | 0.533 |
| 19 | 6.00 | 6.00 | 619 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.638 | 0.617 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
