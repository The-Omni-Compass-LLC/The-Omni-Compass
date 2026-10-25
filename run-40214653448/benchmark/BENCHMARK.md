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
| duration (min) | 20.10 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 5.05 | -15.8% |
| worker nodes in service, min | 6.00 | 5.00 | -16.7% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 1.69 | -15.8% |
| power (W), mean | 626 | 559 | -10.8% |
| power (W), peak | 652 | 621 | -4.8% |
| energy (Wh) | 210 | 187 | -10.8% |
| energy, parked workers still on at idle power (Wh) | 210 | 211 | +0.5% |
| CPU used (cores), mean | 0.816 | 0.888 | +8.8% |
| CPU allocatable (cores), mean | 24.00 | 20.20 | -15.8% |
| utilisation (used / allocatable) | 0.034 | 0.044 | +29.3% |
| energy per core-hour (Wh) | 768 | 629 | -18.1% |
| node-hours per core-hour | 7.36 | 5.69 | -22.6% |
| pending pods, pod-minutes | 0.250 | 0.267 | +6.7% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.00 | 8.86 | -1.5% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.767 | 0.517 | -32.6% |
| requests timed | 1,125 | 1,145 | +1.8% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 67.38 | 48.88 | -27.5% |
| response time (ms), median | 46.90 | 43.60 | -7.0% |
| response time (ms), 95th percentile | 153 | 72.18 | -52.8% |
| response time (ms), 99th percentile | 248 | 87.90 | -64.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.0339 | 6.5315 | -18.7% | [-3.4909, +0.4728] | EVEN, no significant difference |
| kwh_per_core_hour | 0.8352 | 0.7158 | -14.3% | [-0.3080, +0.0736] | EVEN, no significant difference |
| utilisation | 0.0337 | 0.0437 | +29.7% | [-0.0015, +0.0226] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.7258 | 0.7805 | +7.5% | [-2.1774, +2.3415] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2197 | 1.5000 | -32.4% | [-5.1711, +3.0366] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.391 0.416 0.436 0.455 0.472 0.485 0.499 0.51 0.52 0.528 0.533 0.537 0.541 0.545 0.549 0.552 0.554 0.556 0.557
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
| 0 | 6.00 | 6.00 | 616 | 617 | 5.00 | 5.00 | 0.000 | 0.000 | 0.551 | 0.561 |
| 1 | 6.00 | 5.00 | 616 | 541 | 6.00 | 5.00 | 0.000 | 0.000 | 0.527 | 0.506 |
| 2 | 6.00 | 5.00 | 615 | 541 | 6.00 | 5.00 | 0.000 | 0.000 | 0.519 | 0.528 |
| 3 | 6.00 | 5.00 | 620 | 545 | 6.00 | 5.00 | 0.250 | 0.250 | 0.643 | 0.633 |
| 4 | 6.00 | 5.00 | 632 | 559 | 7.50 | 8.00 | 0.000 | 0.000 | 0.959 | 1.02 |
| 5 | 6.00 | 5.00 | 629 | 561 | 10.00 | 9.75 | 0.000 | 0.000 | 0.918 | 1.05 |
| 6 | 6.00 | 5.00 | 630 | 564 | 10.00 | 10.00 | 0.000 | 0.000 | 0.941 | 1.08 |
| 7 | 6.00 | 5.00 | 644 | 578 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 1.52 |
| 8 | 6.00 | 5.00 | 642 | 584 | 10.00 | 10.00 | 0.000 | 0.000 | 1.23 | 1.66 |
| 9 | 6.00 | 5.00 | 646 | 578 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.51 |
| 10 | 6.00 | 5.00 | 639 | 574 | 10.00 | 10.00 | 0.000 | 0.000 | 1.16 | 1.40 |
| 11 | 6.00 | 5.00 | 615 | 540 | 10.00 | 10.00 | 0.000 | 0.000 | 0.501 | 0.503 |
| 12 | 6.00 | 5.00 | 617 | 543 | 10.00 | 10.00 | 0.000 | 0.000 | 0.588 | 0.578 |
| 13 | 6.00 | 5.00 | 622 | 546 | 10.00 | 10.00 | 0.000 | 0.000 | 0.718 | 0.647 |
| 14 | 6.00 | 5.00 | 629 | 560 | 10.00 | 10.00 | 0.000 | 0.000 | 0.894 | 0.933 |
| 15 | 6.00 | 5.00 | 632 | 558 | 10.00 | 10.00 | 0.000 | 0.000 | 0.983 | 0.974 |
| 16 | 6.00 | 5.00 | 629 | 560 | 10.00 | 10.00 | 0.000 | 0.000 | 0.842 | 1.02 |
| 17 | 6.00 | 5.00 | 624 | 549 | 10.00 | 10.00 | 0.000 | 0.000 | 0.761 | 0.749 |
| 18 | 6.00 | 5.00 | 616 | 542 | 10.00 | 10.00 | 0.000 | 0.000 | 0.515 | 0.563 |
| 19 | 6.00 | 5.00 | 618 | 541 | 10.00 | 10.00 | 0.000 | 0.000 | 0.592 | 0.540 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
