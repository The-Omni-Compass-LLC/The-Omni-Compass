# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.887 |
| node-hours | 1.518 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 157 |
| response time (ms), mean | 143.8 | 76.55 |
| response time (ms), 95th percentile | 326.3 | 116.9 |
| response time (ms), 99th percentile | 516.7 | 168.5 |
| time over the response line (% of samples) | 1.915 | 0.01212 |
| failed requests (%) | 0 | 0 |
| pending pods, pod-minutes | 0.2617 | 0.48 |
| utilisation (used / allocatable) | 0.03756 | 0.03649 |
| CPU used (cores), mean | 0.9015 | 0.8596 |
| Omni's own CPU (cores), mean | 0 | 0.00974 |
| CPU used with Omni's own (cores), mean | 0.9015 | 0.8693 |
| energy per core-hour (Wh, the 25 W standby model) | 751.2 | 756 |
| HPA replicas, mean | 8.538 | 8.107 |
| pods started | 4.5 | 3.9 |
| pod start wait, total (s) | 14 | 17.4 |
| pod start wait, mean (s) | 2.76 | 3.634 |
| host CPU busy, the real machine under kind (%) | 27.11 | 26.6 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (bowl law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.887 | -1.9% | -0.164 to -0.06174 | yes, better |
| node-hours | 1.518 | 1.491 | -1.8% | -0.0396 to -0.0144 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.1 | -0.1% | -0.6873 to +0.2697 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 157 | -1.5% | -3.394 to -1.323 | yes, better |
| response time (ms), mean | 143.8 | 76.55 | -46.8% | -92.07 to -42.51 | yes, better |
| response time (ms), 95th percentile | 326.3 | 116.9 | -64.2% | -281.8 to -137 | yes, better |
| response time (ms), 99th percentile | 516.7 | 168.5 | -67.4% | -464.4 to -232.1 | yes, better |
| time over the response line (% of samples) | 1.915 | 0.01212 | -99.4% | -3.046 to -0.7601 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2617 | 0.48 | +83.4% | +0.06686 to +0.3698 | yes, worse |
| utilisation (used / allocatable) | 0.03756 | 0.03649 | -2.9% | -0.002601 to +0.0004555 | no |
| CPU used (cores), mean | 0.9015 | 0.8596 | -4.6% | -0.08053 to -0.003236 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00974 | +0.00974 (native is 0) | +0.008207 to +0.01127 | yes, more |
| CPU used with Omni's own (cores), mean | 0.9015 | 0.8693 | -3.6% | -0.06947 to +0.005187 | no |
| energy per core-hour (Wh, the 25 W standby model) | 751.2 | 756 | +0.6% | -29.28 to +38.84 | no |
| HPA replicas, mean | 8.538 | 8.107 | -5.1% | -0.9537 to +0.09078 | no |
| pods started | 4.5 | 3.9 | -13.3% | -2.039 to +0.8385 | no |
| pod start wait, total (s) | 14 | 17.4 | +24.3% | -3.755 to +10.55 | no |
| pod start wait, mean (s) | 2.76 | 3.634 | +31.7% | -0.827 to +2.575 | no |
| host CPU busy, the real machine under kind (%) | 27.11 | 26.6 | -1.9% | -1.379 to +0.3596 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
