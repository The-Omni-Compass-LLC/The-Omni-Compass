# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top, bowl law |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.75 |
| node-hours | 4.525 | 4.337 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.7 | 515.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.7 | 501.4 |
| response time (ms), mean | 257.4 | 145.8 |
| response time (ms), 95th percentile | 700.5 | 314 |
| response time (ms), 99th percentile | 1733 | 1439 |
| time over the response line (% of samples) | 13.81 | 7.771 |
| failed requests (%) | 4.968 | 4.88 |
| pending pods, pod-minutes | 0.2667 | 0.2667 |
| utilisation (used / allocatable) | 0.09791 | 0.1016 |
| CPU used (cores), mean | 2.35 | 2.338 |
| Omni's own CPU (cores), mean | 0 | 0.0078 |
| CPU used with Omni's own (cores), mean | 2.35 | 2.346 |
| energy per core-hour (Wh, the 25 W standby model) | 291 | 284.4 |
| HPA replicas, mean | 9.559 | 7.979 |
| pods started | 5 | 6 |
| pod start wait, total (s) | 15 | 19 |
| pod start wait, mean (s) | 3 | 3.167 |
| host CPU busy, the real machine under kind (%) | 65.23 | 65.05 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.75 | -4.2% | +nan to +nan | no |
| node-hours | 4.525 | 4.337 | -4.2% | +nan to +nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.7 | 515.6 | -0.0% | +nan to +nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.7 | 501.4 | -2.8% | +nan to +nan | no |
| response time (ms), mean | 257.4 | 145.8 | -43.3% | +nan to +nan | no |
| response time (ms), 95th percentile | 700.5 | 314 | -55.2% | +nan to +nan | no |
| response time (ms), 99th percentile | 1733 | 1439 | -17.0% | +nan to +nan | no |
| time over the response line (% of samples) | 13.81 | 7.771 | -43.7% | +nan to +nan | no |
| failed requests (%) | 4.968 | 4.88 | -1.8% | +nan to +nan | no |
| pending pods, pod-minutes | 0.2667 | 0.2667 | +0.0% | +nan to +nan | no |
| utilisation (used / allocatable) | 0.09791 | 0.1016 | +3.8% | +nan to +nan | no |
| CPU used (cores), mean | 2.35 | 2.338 | -0.5% | +nan to +nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0078 | +0.0078 (native is 0) | +nan to +nan | no |
| CPU used with Omni's own (cores), mean | 2.35 | 2.346 | -0.2% | +nan to +nan | no |
| energy per core-hour (Wh, the 25 W standby model) | 291 | 284.4 | -2.3% | +nan to +nan | no |
| HPA replicas, mean | 9.559 | 7.979 | -16.5% | +nan to +nan | no |
| pods started | 5 | 6 | +20.0% | +nan to +nan | no |
| pod start wait, total (s) | 15 | 19 | +26.7% | +nan to +nan | no |
| pod start wait, mean (s) | 3 | 3.167 | +5.6% | +nan to +nan | no |
| host CPU busy, the real machine under kind (%) | 65.23 | 65.05 | -0.3% | +nan to +nan | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +nan to +nan | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.0 |  |  | 1 |
| bowl | 30.0 | +66.7% | +nan to +nan | 1 |
