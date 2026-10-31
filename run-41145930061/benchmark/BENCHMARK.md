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
| duration (min) | 20.23 | 20.08 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.7% |
| power (W), mean | 630 | 638 | +1.4% |
| power (W), peak | 652 | 676 | +3.7% |
| energy (Wh) | 212 | 214 | +0.6% |
| energy, parked workers still on at idle power (Wh) | 212 | 214 | +0.6% |
| CPU used (cores), mean | 0.910 | 1.15 | +26.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.038 | 0.048 | +26.1% |
| energy per core-hour (Wh) | 692 | 556 | -19.6% |
| node-hours per core-hour | 6.59 | 5.23 | -20.7% |
| pending pods, pod-minutes | 0.000 | 0.533 | new |
| pending pods, peak | 0.000 | 2.00 | new |
| HPA replicas, mean | 9.20 | 9.39 | +2.1% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.533 | -31.9% |
| requests timed | 1,025 | 1,120 | +9.3% |
| time over the response line (% of samples) | 1.17 | 0.000 | -100.0% |
| response time (ms), mean | 175 | 75.79 | -56.7% |
| response time (ms), median | 141 | 68.55 | -51.5% |
| response time (ms), 95th percentile | 374 | 105 | -71.9% |
| response time (ms), 99th percentile | 522 | 123 | -76.4% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.1993 | 6.0026 | -16.6% | [-2.9501, +0.5611] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7520 | 0.6329 | -15.8% | [-0.2821, +0.0572] | EVEN, no significant difference |
| utilisation | 0.0374 | 0.0469 | +25.3% | [-0.0023, +0.0221] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.0000 | 1.5360 | n/a | [+0.0000, +4.6080] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2797 | 1.5360 | -32.6% | [-3.8035, +3.0902] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.445 0.468 0.487 0.503 0.518 0.531 0.543 0.553 0.559 0.564 0.569 0.574 0.579 0.582 0.586 0.588 0.589
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
| 0 | 6.00 | 6.00 | 618 | 618 | 5.00 | 7.00 | 0.000 | 0.000 | 0.587 | 0.582 |
| 1 | 6.00 | 6.00 | 618 | 621 | 7.00 | 7.00 | 0.000 | 0.000 | 0.638 | 0.689 |
| 2 | 6.00 | 6.00 | 618 | 622 | 7.00 | 7.00 | 0.000 | 0.000 | 0.601 | 0.730 |
| 3 | 6.00 | 6.00 | 624 | 631 | 7.00 | 7.25 | 0.000 | 0.500 | 0.752 | 0.935 |
| 4 | 6.00 | 6.00 | 634 | 644 | 9.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.30 |
| 5 | 6.00 | 6.00 | 634 | 644 | 9.33 | 10.00 | 0.000 | 0.000 | 1.04 | 1.27 |
| 6 | 6.00 | 6.00 | 635 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.28 |
| 7 | 6.00 | 6.00 | 645 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 1.66 |
| 8 | 6.00 | 6.00 | 648 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 1.99 |
| 9 | 6.00 | 6.00 | 646 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 1.97 |
| 10 | 6.00 | 6.00 | 640 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 1.53 |
| 11 | 6.00 | 6.00 | 620 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.650 | 0.727 |
| 12 | 6.00 | 6.00 | 620 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.662 | 0.649 |
| 13 | 6.00 | 6.00 | 624 | 629 | 10.00 | 10.00 | 0.000 | 0.000 | 0.762 | 0.946 |
| 14 | 6.00 | 6.00 | 638 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.13 | 1.30 |
| 15 | 6.00 | 6.00 | 634 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.30 |
| 16 | 6.00 | 6.00 | 634 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.39 |
| 17 | 6.00 | 6.00 | 627 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.826 | 1.17 |
| 18 | 6.00 | 6.00 | 619 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.638 | 0.742 |
| 19 | 6.00 | 6.00 | 618 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.597 | 0.655 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
