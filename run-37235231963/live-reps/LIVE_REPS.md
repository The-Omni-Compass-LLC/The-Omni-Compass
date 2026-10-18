# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top, bowl law |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.799 |
| node-hours | 4.516 | 4.362 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.5 | 515.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.5 | 504.4 |
| response time (ms), mean | 276.8 | 157.4 |
| response time (ms), 95th percentile | 708.5 | 323.9 |
| response time (ms), 99th percentile | 2460 | 1797 |
| time over the response line (% of samples) | 18.57 | 11.57 |
| failed requests (%) | 10.48 | 8.988 |
| pending pods, pod-minutes | 0.59 | 0.635 |
| utilisation (used / allocatable) | 0.1022 | 0.1021 |
| CPU used (cores), mean | 2.454 | 2.396 |
| Omni's own CPU (cores), mean | 0 | 0.00913 |
| CPU used with Omni's own (cores), mean | 2.454 | 2.405 |
| energy per core-hour (Wh, the 25 W standby model) | 303.5 | 300.6 |
| HPA replicas, mean | 9.643 | 8.989 |
| pods started | 4.2 | 5.7 |
| pod start wait, total (s) | 13.9 | 17.9 |
| pod start wait, mean (s) | 2.75 | 2.532 |
| host CPU busy, the real machine under kind (%) | 68.76 | 67.65 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.799 | -3.3% | -0.472 to +0.07017 | no |
| node-hours | 4.516 | 4.362 | -3.4% | -0.3579 to +0.04983 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.5 | 515.8 | -0.3% | -2.154 to -1.306 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.5 | 504.4 | -2.5% | -28.24 to +2.104 | no |
| response time (ms), mean | 276.8 | 157.4 | -43.1% | -150.5 to -88.25 | yes, better |
| response time (ms), 95th percentile | 708.5 | 323.9 | -54.3% | -496 to -273.3 | yes, better |
| response time (ms), 99th percentile | 2460 | 1797 | -27.0% | -1243 to -82.8 | yes, better |
| time over the response line (% of samples) | 18.57 | 11.57 | -37.7% | -9.103 to -4.89 | yes, better |
| failed requests (%) | 10.48 | 8.988 | -14.2% | -2.317 to -0.662 | yes, better |
| pending pods, pod-minutes | 0.59 | 0.635 | +7.6% | -0.3471 to +0.4371 | no |
| utilisation (used / allocatable) | 0.1022 | 0.1021 | -0.1% | -0.003007 to +0.002707 | no |
| CPU used (cores), mean | 2.454 | 2.396 | -2.3% | -0.06601 to -0.0489 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00913 | +0.00913 (native is 0) | +0.00795 to +0.01031 | yes, more |
| CPU used with Omni's own (cores), mean | 2.454 | 2.405 | -2.0% | -0.05721 to -0.03944 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 303.5 | 300.6 | -1.0% | -14.31 to +8.365 | no |
| HPA replicas, mean | 9.643 | 8.989 | -6.8% | -1.472 to +0.1631 | no |
| pods started | 4.2 | 5.7 | +35.7% | +0.02055 to +2.979 | yes, worse |
| pod start wait, total (s) | 13.9 | 17.9 | +28.8% | -3.025 to +11.02 | no |
| pod start wait, mean (s) | 2.75 | 2.532 | -7.9% | -0.9293 to +0.4928 | no |
| host CPU busy, the real machine under kind (%) | 68.76 | 67.65 | -1.6% | -1.39 to -0.8171 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
