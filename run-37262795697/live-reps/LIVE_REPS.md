# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.645 |
| node-hours | 2.516 | 2.364 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 263.9 |
| response time (ms), mean | 535.8 | 519.9 |
| response time (ms), 95th percentile | 3171 | 3544 |
| response time (ms), 99th percentile | 4953 | 5347 |
| time over the response line (% of samples) | 15.66 | 15.99 |
| failed requests (%) | 0.2377 | 0.3097 |
| pending pods, pod-minutes | 191.5 | 213.8 |
| utilisation (used / allocatable) | 0.0639 | 0.07089 |
| CPU used (cores), mean | 1.534 | 1.601 |
| Omni's own CPU (cores), mean | 0 | 0.0212 |
| CPU used with Omni's own (cores), mean | 1.534 | 1.623 |
| energy per core-hour (Wh, the 25 W standby model) | 434.8 | 395.3 |
| HPA replicas, mean | 2.481 | 3.08 |
| pods started | 0 | 0.1429 |
| pod start wait, total (s) | 0 | 0.1429 |
| pod start wait, mean (s) | 0 | 0.1429 |
| host CPU busy, the real machine under kind (%) | 43.77 | 47.22 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 595.1 | 641.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.379 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (bowl law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 7 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.645 | -5.9% | -0.4102 to -0.3005 | yes, better |
| node-hours | 2.517 | 2.364 | -6.1% | -0.1683 to -0.1394 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275 | -0.2% | -2.05 to +0.6937 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 263.9 | -4.3% | -12.71 to -10.98 | yes, better |
| response time (ms), mean | 601.9 | 519.9 | -13.6% | -103.1 to -61.01 | yes, better |
| response time (ms), 95th percentile | 3531 | 3544 | +0.4% | -262.1 to +289.7 | no |
| response time (ms), 99th percentile | 5376 | 5347 | -0.5% | -201.8 to +144.9 | no |
| time over the response line (% of samples) | 16.75 | 15.99 | -4.5% | -1.202 to -0.3108 | yes, better |
| failed requests (%) | 0.2319 | 0.3097 | +33.5% | -0.009219 to +0.1648 | no |
| pending pods, pod-minutes | 203.9 | 213.8 | +4.9% | +1.866 to +17.95 | yes, worse |
| utilisation (used / allocatable) | 0.06758 | 0.07089 | +4.9% | +0.001375 to +0.005245 | yes, more |
| CPU used (cores), mean | 1.622 | 1.601 | -1.3% | -0.06518 to +0.02435 | no |
| Omni's own CPU (cores), mean | 0 | 0.0212 | +0.0212 (native is 0) | +0.01886 to +0.02354 | yes, more |
| CPU used with Omni's own (cores), mean | 1.622 | 1.623 | +0.0% | -0.04364 to +0.0452 | no |
| energy per core-hour (Wh, the 25 W standby model) | 407.3 | 395.3 | -3.0% | -23.3 to -0.7462 | yes, better |
| HPA replicas, mean | 2.716 | 3.08 | +13.4% | -0.7673 to +1.496 | no |
| pods started | 0 | 0.1429 | +0.143 (native is 0) | -0.2067 to +0.4924 | no |
| pod start wait, total (s) | 0 | 0.1429 | +0.143 (native is 0) | -0.2067 to +0.4924 | no |
| pod start wait, mean (s) | 0 | 0.1429 | +0.143 (native is 0) | -0.2067 to +0.4924 | no |
| host CPU busy, the real machine under kind (%) | 46.3 | 47.22 | +2.0% | +0.5453 to +1.309 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 634.4 | 641.9 | +1.2% | -1.146 to +16 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.379 | -10.3% | -0.6774 to -0.5644 | yes, better |
