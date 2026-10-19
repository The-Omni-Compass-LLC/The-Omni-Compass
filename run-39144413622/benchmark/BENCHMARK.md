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
| duration (min) | 20.05 | 20.23 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.02 | +0.9% |
| power (W), mean | 625 | 643 | +2.8% |
| power (W), peak | 646 | 681 | +5.3% |
| energy (Wh) | 209 | 217 | +3.8% |
| energy, parked workers still on at idle power (Wh) | 209 | 217 | +3.8% |
| CPU used (cores), mean | 0.784 | 1.24 | +58.5% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.033 | 0.052 | +58.5% |
| energy per core-hour (Wh) | 797 | 517 | -35.1% |
| node-hours per core-hour | 7.65 | 4.83 | -36.9% |
| pending pods, pod-minutes | 0.533 | 0.533 | +0.0% |
| pending pods, peak | 2.00 | 2.00 | +0.0% |
| HPA replicas, mean | 8.59 | 9.43 | +9.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.517 | -34.0% |
| requests timed | 1,130 | 1,100 | -2.7% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 62.05 | 95.27 | +53.5% |
| response time (ms), median | 42.90 | 81.95 | +91.0% |
| response time (ms), 95th percentile | 135 | 152 | +12.8% |
| response time (ms), 99th percentile | 206 | 174 | -15.5% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.4804 | 5.4570 | -35.7% | [-4.8710, -1.1385] | GAIN |
| kwh_per_core_hour | 0.8795 | 0.5797 | -34.1% | [-0.4860, -0.1200] | GAIN |
| utilisation | 0.0324 | 0.0509 | +56.9% | [+0.0066, +0.0314] | GAIN |
| pending_pod_minutes_per_hour | 1.4634 | 1.5238 | +4.1% | [-4.3902, +4.5714] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2322 | 1.5238 | -31.7% | [-3.6722, +2.2857] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.468 0.487 0.504 0.52 0.534 0.546 0.556 0.562 0.566 0.571 0.576 0.581 0.585 0.589 0.59 0.591
- nodes decided per minute: 6 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 613 | 633 | 4.00 | 5.00 | 0.000 | 0.500 | 0.435 | 0.999 |
| 1 | 6.00 | 6.00 | 618 | 625 | 4.50 | 8.00 | 0.000 | 0.000 | 0.581 | 0.779 |
| 2 | 6.00 | 6.00 | 612 | 623 | 5.00 | 8.00 | 0.000 | 0.000 | 0.430 | 0.729 |
| 3 | 6.00 | 6.00 | 616 | 631 | 5.00 | 8.00 | 0.500 | 0.000 | 0.543 | 0.927 |
| 4 | 6.00 | 6.00 | 630 | 648 | 8.00 | 10.00 | 0.000 | 0.000 | 0.936 | 1.40 |
| 5 | 6.00 | 6.00 | 628 | 649 | 8.00 | 10.00 | 0.000 | 0.000 | 0.853 | 1.41 |
| 6 | 6.00 | 6.00 | 629 | 647 | 8.00 | 10.00 | 0.000 | 0.000 | 0.894 | 1.37 |
| 7 | 6.00 | 6.00 | 644 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.02 |
| 8 | 6.00 | 6.00 | 642 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.09 |
| 9 | 6.00 | 6.00 | 641 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.23 | 2.12 |
| 10 | 6.00 | 6.00 | 637 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.09 | 1.96 |
| 11 | 6.00 | 6.00 | 615 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.514 | 0.809 |
| 12 | 6.00 | 6.00 | 615 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.516 | 0.651 |
| 13 | 6.00 | 6.00 | 619 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.626 | 0.910 |
| 14 | 6.00 | 6.00 | 632 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 0.945 | 1.49 |
| 15 | 6.00 | 6.00 | 631 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.968 | 1.36 |
| 16 | 6.00 | 6.00 | 629 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.888 | 1.42 |
| 17 | 6.00 | 6.00 | 621 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.685 | 1.18 |
| 18 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.542 | 0.738 |
| 19 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.512 | 0.723 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
