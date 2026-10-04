# More work, faster, on fewer machines, with less energy: all four in one run

Run: benchmark-reps 37226863122, commit `01d1033` (preregistered in `docs/K8S_BOWL_PREREGISTRATION.md`, "all four in
one run"), ten paired repetitions on real Kubernetes (kind, six workers), native against native with Omni-Compass on top
(bowl law), open-loop load rising one step at a time from 1 to 8 load generators and back down to 1, 180 s a step.
Raw files: `results/live/raw/run-37226863122/`. Recomputed from them with `tools/live_reps.py`. This run's machine floor
was one (the floor of two was adopted after it started).

## In one line

**+29.3% more work (24.6 to 31.8 requests a second inside the line), p95 62.3% lower, 3.6% fewer machines in service,
0.3% less energy, 1.9% less CPU counting Omni-Compass's own: all four better, each proven (95% interval clear of
zero); no measure worse beyond the noise.**

## All columns, mean over repetitions

| Gauge | Native | Omni on top, bowl law |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.784 |
| node-hours | 4.514 | 4.348 |
| energy, parked workers still on at idle power (Wh, declared model) | 511.2 | 509.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.2 | 497.5 |
| response time (ms), mean | 245.2 | 134.6 |
| response time (ms), 95th percentile | 685.8 | 258.3 |
| response time (ms), 99th percentile | 2319 | 1532 |
| time over the response line (% of samples) | 15.32 | 9.061 |
| failed requests (%) | 8.285 | 7.282 |
| pending pods, pod-minutes | 0.4933 | 0.59 |
| utilisation (used / allocatable) | 0.09331 | 0.09383 |
| CPU used (cores), mean | 2.239 | 2.188 |
| Omni's own CPU (cores), mean | 0 | 0.00806 |
| CPU used with Omni's own (cores), mean | 2.239 | 2.196 |
| energy per core-hour (Wh, the 25 W standby model) | 332.2 | 331.5 |
| HPA replicas, mean | 9.39 | 7.833 |
| pods started | 5 | 5.2 |
| pod start wait, total (s) | 15.8 | 17.3 |
| pod start wait, mean (s) | 2.905 | 3.097 |
| host CPU busy, the real machine under kind (%) | 62.96 | 61.76 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.784 | -3.6% | -0.4012 to -0.03098 | yes, better |
| node-hours | 4.514 | 4.348 | -3.7% | -0.3055 to -0.02621 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 511.2 | 509.7 | -0.3% | -3.067 to -0.03068 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 511.2 | 497.5 | -2.7% | -24.11 to -3.364 | yes, better |
| response time (ms), mean | 245.2 | 134.6 | -45.1% | -149.5 to -71.81 | yes, better |
| response time (ms), 95th percentile | 685.8 | 258.3 | -62.3% | -565.1 to -289.8 | yes, better |
| response time (ms), 99th percentile | 2319 | 1532 | -33.9% | -1885 to +310.6 | no |
| time over the response line (% of samples) | 15.32 | 9.061 | -40.9% | -9.035 to -3.492 | yes, better |
| failed requests (%) | 8.285 | 7.282 | -12.1% | -1.671 to -0.3337 | yes, better |
| pending pods, pod-minutes | 0.4933 | 0.59 | +19.6% | -0.2516 to +0.4449 | no |
| utilisation (used / allocatable) | 0.09331 | 0.09383 | +0.6% | -0.001943 to +0.002979 | no |
| CPU used (cores), mean | 2.239 | 2.188 | -2.3% | -0.08277 to -0.0197 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00806 | +0.00806 (native is 0) | +0.006722 to +0.009398 | yes, more |
| CPU used with Omni's own (cores), mean | 2.239 | 2.196 | -1.9% | -0.07505 to -0.0113 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 332.2 | 331.5 | -0.2% | -10.78 to +9.302 | no |
| HPA replicas, mean | 9.39 | 7.833 | -16.6% | -2.657 to -0.4568 | yes, better |
| pods started | 5 | 5.2 | +4.0% | -1.223 to +1.623 | no |
| pod start wait, total (s) | 15.8 | 17.3 | +9.5% | -5.913 to +8.913 | no |
| pod start wait, mean (s) | 2.905 | 3.097 | +6.6% | -0.8169 to +1.2 | no |
| host CPU busy, the real machine under kind (%) | 62.96 | 61.76 | -1.9% | -1.959 to -0.436 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 24.6 |  |  | 10 |
| bowl | 31.8 | +29.3% | +5.4 to +9.0 | 10 |
