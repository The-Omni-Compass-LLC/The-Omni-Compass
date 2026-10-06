# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.1 | 172.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.1 | 172.9 |
| response time (ms), mean | 538.7 | 514 |
| response time (ms), 95th percentile | 2239 | 2396 |
| response time (ms), 99th percentile | 5848 | 5755 |
| time over the response line (% of samples) | 25.5 | 23.95 |
| failed requests (%) | 4.548 | 3.713 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.248 | 1.69 |
| utilisation (used / allocatable) | 0.09998 | 0.09912 |
| CPU used (cores), mean | 2.399 | 2.379 |
| Omni's own CPU (cores), mean | 0 | 0.01521 |
| CPU used with Omni's own (cores), mean | 2.399 | 2.394 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.7 | 293.1 |
| HPA replicas, mean | 15.22 | 15.33 |
| pods started | 4.5 | 3.6 |
| pod start wait, total (s) | 9.3 | 9.2 |
| pod start wait, mean (s) | 1.806 | 2.236 |
| host CPU busy, the real machine under kind (%) | 70.04 | 69.75 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 286.7 | 277.7 |
| second app: response time (ms), 99th percentile | 1570 | 1155 |
| second app: time over the response line (% of samples) | 15.95 | 15.35 |
| second app: failed requests (%) | 14.12 | 13.96 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.989e-16 to +5.436e-16 | same (under one part in a million) |
| node-hours | 1.515 | 1.515 | +0.0% | -0.008886 to +0.008886 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 173.1 | 172.9 | -0.1% | -1.119 to +0.7879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.1 | 172.9 | -0.1% | -1.119 to +0.7879 | no |
| response time (ms), mean | 538.7 | 514 | -4.6% | -64.59 to +15.25 | no |
| response time (ms), 95th percentile | 2239 | 2396 | +7.0% | -231.2 to +545.8 | no |
| response time (ms), 99th percentile | 5848 | 5755 | -1.6% | -891.5 to +704.3 | no |
| time over the response line (% of samples) | 25.5 | 23.95 | -6.1% | -2.593 to -0.4928 | yes, better |
| failed requests (%) | 4.548 | 3.713 | -18.4% | -1.753 to +0.08376 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.248 | 1.69 | +35.4% | -0.4942 to +1.378 | no |
| utilisation (used / allocatable) | 0.09998 | 0.09912 | -0.9% | -0.001506 to -0.0002079 | yes, less |
| CPU used (cores), mean | 2.399 | 2.379 | -0.9% | -0.03613 to -0.00499 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01521 | +0.0152 (native is 0) | +0.01308 to +0.01734 | yes, more |
| CPU used with Omni's own (cores), mean | 2.399 | 2.394 | -0.2% | -0.02168 to +0.01097 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.7 | 293.1 | +0.8% | +0.4654 to +4.43 | yes, more |
| HPA replicas, mean | 15.22 | 15.33 | +0.7% | -0.2017 to +0.4206 | no |
| pods started | 4.5 | 3.6 | -20.0% | -1.687 to -0.1128 | yes, better |
| pod start wait, total (s) | 9.3 | 9.2 | -1.1% | -2.807 to +2.607 | no |
| pod start wait, mean (s) | 1.806 | 2.236 | +23.8% | -0.06015 to +0.9201 | no |
| host CPU busy, the real machine under kind (%) | 70.04 | 69.75 | -0.4% | -0.7425 to +0.1587 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 286.7 | 277.7 | -3.2% | -30.97 to +12.85 | no |
| second app: response time (ms), 99th percentile | 1570 | 1155 | -26.5% | -1149 to +318.3 | no |
| second app: time over the response line (% of samples) | 15.95 | 15.35 | -3.7% | -1.105 to -0.08596 | yes, better |
| second app: failed requests (%) | 14.12 | 13.96 | -1.2% | -0.6736 to +0.3459 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*