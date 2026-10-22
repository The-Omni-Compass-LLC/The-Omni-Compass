# The heartbeat sweep: a decision every 5, 10, 15, 20, 30, 60, 75, 90 and 120 seconds

Our own model (evidence class S): what each beat of the governor does against native, in the cloud and on-site, and what it costs the engine; never a benchmark result. The founder's questions of 22 October: does a decision every 10 or 5 seconds do better than 15, is 20 different, what does a faster beat cost, and what a beat slower than 60 seconds does (75, 90 and 120), to show whether, and why, it gains or loses. Run by `tools/heartbeat_sweep.py` (the shipped controller of each checkout on one 5-second plant, eight seeds of a day each, paired by seed; each row named by the engine it ran on: omni-v16, omni-v15). Each reading is the gate's rule (`tools/toy_gate.py`): the mean change over the seeds with its 95% interval, the word by the gauge's aim (`tools/readings.py`). The engine's own cost is a mean a day: its decisions, its processor time, its reads of the cluster and its writes; the fast check's rescues are the pool commands its 5-second check wrote because a pod already waited for a place, apart from the full decision's own, which size the pool ahead of the load (`rescues`). Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

## On-site: native is the pod autoscaler with the cluster autoscaler; with Omni-Compass the governor sizes the pool on top of the pod autoscaler (the max)

### omni-v16 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | up 3.8%, power given | up 2.8%, power given | down 83.5%, GAIN | down 0.3%, GAIN | down 2.1%, GAIN | identical | 17,280 | 51.7 s | 86,412 | 906 | 0.0 |
| 10 s | up 3.4%, power given | up 2.5%, power given | down 83.5%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 8,640 | 36.1 s | 60,540 | 547 | 0.0 |
| 15 s | up 2.9%, power given | up 2.2%, power given | down 83.5%, GAIN | down 0.3%, GAIN | down 2.1%, GAIN | identical | 5,760 | 31.4 s | 51,915 | 420 | 0.0 |
| 20 s | up 2.7%, EVEN | up 2.0%, EVEN | down 79.8%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 4,320 | 28.5 s | 47,616 | 350 | 0.0 |
| 30 s | up 1.6%, EVEN | up 1.3%, EVEN | down 80.7%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 2,880 | 26.2 s | 43,306 | 264 | 0.1 |
| 60 s | up 0.3%, EVEN | up 0.4%, EVEN | down 72.9%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 1,440 | 23.6 s | 39,026 | 190 | 0.4 |
| 75 s | no change, EVEN | up 0.2%, EVEN | down 69.3%, GAIN | down 0.2%, GAIN | down 1.8%, EVEN | identical | 1,152 | 22.7 s | 38,144 | 177 | 0.8 |
| 90 s | down 0.1%, EVEN | up 0.1%, EVEN | down 63.1%, GAIN | down 0.2%, EVEN | down 1.8%, EVEN | identical | 960 | 22.3 s | 37,522 | 130 | 1.4 |
| 120 s | down 0.2%, EVEN | up 0.1%, EVEN | down 57.0%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 720 | 21.7 s | 36,733 | 120 | 3.0 |

#### omni-v16 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | up 0.9%, EVEN | up 0.6%, EVEN | identical | identical | identical | identical |
| 10 s | up 0.5%, EVEN | up 0.3%, EVEN | down 0.2%, EVEN | no change, EVEN | no change, EVEN | identical |
| 20 s | down 0.3%, EVEN | down 0.2%, EVEN | up 22.2%, EVEN | no change, EVEN | no change, EVEN | identical |
| 30 s | down 1.3%, GAIN | down 0.9%, GAIN | up 16.4%, EVEN | no change, EVEN | no change, EVEN | identical |
| 60 s | down 2.6%, GAIN | down 1.7%, GAIN | up 63.7%, EVEN | no change, EVEN | no change, EVEN | identical |
| 75 s | down 2.8%, GAIN | down 1.9%, GAIN | up 85.5%, EVEN | no change, EVEN | up 0.3%, EVEN | identical |
| 90 s | down 2.9%, GAIN | down 2.0%, GAIN | up 122.9%, LOSS | no change, EVEN | up 0.3%, EVEN | identical |
| 120 s | down 3.0%, GAIN | down 2.1%, GAIN | up 160.1%, EVEN | no change, EVEN | no change, EVEN | identical |

#### omni-v16 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | up 3.5%, power given | up 2.3%, power given | down 38.9%, EVEN | no change, EVEN | no change, EVEN | identical |
| 10 s | up 3.1%, power given | up 2.0%, power given | down 39.1%, EVEN | no change, EVEN | no change, EVEN | identical |
| 15 s | up 2.6%, power given | up 1.7%, power given | down 38.9%, EVEN | no change, EVEN | no change, EVEN | identical |
| 20 s | up 2.4%, power given | up 1.6%, power given | down 25.4%, EVEN | no change, EVEN | no change, EVEN | identical |
| 30 s | up 1.3%, power given | up 0.8%, power given | down 28.9%, EVEN | no change, EVEN | no change, EVEN | identical |
| 75 s | down 0.3%, EVEN | down 0.2%, EVEN | up 13.3%, EVEN | no change, EVEN | up 0.3%, EVEN | identical |
| 90 s | down 0.4%, EVEN | down 0.3%, EVEN | up 36.2%, EVEN | no change, EVEN | up 0.3%, EVEN | identical |
| 120 s | down 0.5%, EVEN | down 0.4%, EVEN | up 58.8%, EVEN | no change, EVEN | identical | identical |

### omni-v15 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | down 1.1%, EVEN | down 0.6%, EVEN | down 87.4%, GAIN | down 0.3%, GAIN | down 2.1%, GAIN | identical | 17,280 | 50.6 s | 86,412 | 1,013 | 0.0 |
| 10 s | down 0.1%, EVEN | up 0.1%, EVEN | down 86.5%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 8,640 | 35.7 s | 60,530 | 598 | 0.0 |
| 15 s | up 0.8%, EVEN | up 0.8%, EVEN | down 87.4%, GAIN | down 0.3%, GAIN | down 2.1%, GAIN | identical | 5,760 | 30.6 s | 51,899 | 459 | 0.0 |
| 20 s | up 1.2%, EVEN | up 1.1%, EVEN | down 83.0%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 4,320 | 28.3 s | 47,601 | 380 | 0.0 |
| 30 s | up 1.4%, EVEN | up 1.2%, EVEN | down 83.7%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 2,880 | 25.7 s | 43,290 | 281 | 0.1 |
| 60 s | up 0.3%, EVEN | up 0.4%, EVEN | down 72.9%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 1,440 | 23.3 s | 39,026 | 190 | 0.4 |
| 75 s | up 0.3%, EVEN | up 0.3%, EVEN | down 69.3%, GAIN | down 0.2%, GAIN | down 1.8%, EVEN | identical | 1,152 | 22.7 s | 38,144 | 177 | 0.8 |
| 90 s | up 0.7%, EVEN | up 0.7%, EVEN | down 63.1%, GAIN | down 0.2%, EVEN | down 1.8%, EVEN | identical | 960 | 22.3 s | 37,522 | 130 | 1.4 |
| 120 s | up 0.8%, EVEN | up 0.7%, EVEN | down 57.0%, GAIN | down 0.2%, GAIN | down 2.1%, GAIN | identical | 720 | 22.0 s | 36,733 | 118 | 3.0 |

#### omni-v15 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | down 1.9%, GAIN | down 1.3%, GAIN | identical | identical | identical | identical |
| 10 s | down 0.9%, GAIN | down 0.6%, GAIN | up 7.1%, EVEN | no change, EVEN | no change, EVEN | identical |
| 20 s | up 0.4%, EVEN | up 0.3%, EVEN | up 34.7%, LOSS | no change, EVEN | no change, EVEN | identical |
| 30 s | up 0.6%, EVEN | up 0.4%, EVEN | up 28.8%, EVEN | no change, EVEN | no change, EVEN | identical |
| 60 s | down 0.5%, EVEN | down 0.4%, EVEN | up 114.5%, LOSS | no change, EVEN | no change, EVEN | identical |
| 75 s | down 0.6%, EVEN | down 0.4%, EVEN | up 143.0%, LOSS | no change, EVEN | up 0.3%, EVEN | identical |
| 90 s | down 0.1%, EVEN | down 0.1%, EVEN | up 192.1%, LOSS | no change, EVEN | up 0.3%, EVEN | identical |
| 120 s | no change, EVEN | no change, EVEN | up 240.8%, LOSS | no change, EVEN | no change, EVEN | identical |

#### omni-v15 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | down 1.4%, EVEN | down 1.0%, EVEN | down 53.4%, GAIN | no change, EVEN | no change, EVEN | identical |
| 10 s | down 0.4%, EVEN | down 0.3%, EVEN | down 50.1%, GAIN | no change, EVEN | identical | identical |
| 15 s | up 0.5%, EVEN | up 0.4%, EVEN | down 53.4%, GAIN | no change, EVEN | no change, EVEN | identical |
| 20 s | up 1.0%, EVEN | up 0.7%, EVEN | down 37.2%, GAIN | no change, EVEN | identical | identical |
| 30 s | up 1.1%, EVEN | up 0.8%, EVEN | down 40.0%, GAIN | no change, EVEN | identical | identical |
| 75 s | no change, EVEN | down 0.1%, EVEN | up 13.3%, EVEN | no change, EVEN | up 0.3%, EVEN | identical |
| 90 s | up 0.4%, EVEN | up 0.3%, EVEN | up 36.2%, EVEN | no change, EVEN | up 0.3%, EVEN | identical |
| 120 s | up 0.5%, EVEN | up 0.3%, EVEN | up 58.8%, EVEN | no change, EVEN | identical | identical |

Native's means over the seeds: machine-hours 133.076; energy per used core-hour 0.036; pods waiting for a place 7.311; 95th percentile response 79.914; 99th percentile response 153.537; minutes over the line 27.000.

## In the cloud: the cloud's own autoscaler makes and deletes machines in every arm; the governor on the machines alone (--give-back-only)

### omni-v16 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | down 1.6%, GAIN | down 0.9%, GAIN | up 15.1%, LOSS | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN | 17,280 | 92.7 s | 86,412 | 5,805 | 0.0 |
| 10 s | down 1.5%, GAIN | down 0.9%, GAIN | up 15.9%, LOSS | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN | 8,640 | 56.4 s | 60,682 | 2,884 | 1.2 |
| 15 s | down 1.8%, GAIN | down 1.0%, GAIN | up 16.8%, LOSS | no change, EVEN | no change, EVEN | identical | 5,760 | 44.4 s | 52,122 | 1,964 | 0.0 |
| 20 s | down 1.0%, EVEN | down 0.5%, EVEN | up 9.2%, EVEN | no change, EVEN | identical | identical | 4,320 | 38.1 s | 47,797 | 1,431 | 3.9 |
| 30 s | down 1.4%, GAIN | down 0.8%, GAIN | up 11.0%, EVEN | no change, EVEN | identical | identical | 2,880 | 32.3 s | 43,515 | 988 | 2.5 |
| 60 s | down 1.0%, EVEN | down 0.5%, EVEN | up 7.5%, EVEN | no change, EVEN | identical | identical | 1,440 | 26.3 s | 39,091 | 538 | 5.5 |
| 75 s | down 1.4%, EVEN | down 0.7%, EVEN | up 9.5%, EVEN | no change, EVEN | identical | identical | 1,152 | 25.3 s | 38,292 | 429 | 6.8 |
| 90 s | down 0.8%, EVEN | down 0.4%, GAIN | up 8.2%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN | 960 | 24.6 s | 37,462 | 360 | 6.0 |
| 120 s | down 0.7%, EVEN | down 0.4%, GAIN | up 4.9%, EVEN | no change, EVEN | identical | identical | 720 | 23.7 s | 36,702 | 285 | 5.4 |

#### omni-v16 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | up 0.2%, EVEN | up 0.1%, EVEN | down 1.5%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.9%, EVEN |
| 10 s | up 0.3%, EVEN | up 0.1%, EVEN | down 0.7%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.9%, EVEN |
| 20 s | up 0.8%, power given | up 0.5%, power given | down 6.5%, EVEN | no change, EVEN | no change, EVEN | identical |
| 30 s | up 0.5%, EVEN | up 0.2%, EVEN | down 5.0%, GAIN | no change, EVEN | no change, EVEN | identical |
| 60 s | up 0.9%, EVEN | up 0.5%, EVEN | down 7.9%, GAIN | no change, EVEN | no change, EVEN | identical |
| 75 s | up 0.5%, EVEN | up 0.3%, EVEN | down 6.3%, EVEN | no change, EVEN | no change, EVEN | identical |
| 90 s | up 1.0%, EVEN | up 0.5%, power given | down 7.3%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN |
| 120 s | up 1.2%, power given | up 0.6%, power given | down 10.2%, EVEN | no change, EVEN | no change, EVEN | identical |

#### omni-v16 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | down 0.6%, EVEN | down 0.4%, EVEN | up 7.0%, EVEN | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN |
| 10 s | down 0.6%, EVEN | down 0.3%, EVEN | up 7.8%, EVEN | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN |
| 15 s | down 0.9%, EVEN | down 0.5%, EVEN | up 8.6%, LOSS | no change, EVEN | no change, EVEN | identical |
| 20 s | down 0.1%, EVEN | no change, EVEN | up 1.6%, EVEN | no change, EVEN | identical | identical |
| 30 s | down 0.4%, EVEN | down 0.3%, EVEN | up 3.2%, EVEN | no change, EVEN | identical | identical |
| 75 s | down 0.4%, EVEN | down 0.2%, EVEN | up 1.8%, EVEN | no change, EVEN | identical | identical |
| 90 s | up 0.2%, EVEN | up 0.1%, EVEN | up 0.7%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN |
| 120 s | up 0.3%, EVEN | up 0.1%, EVEN | down 2.4%, EVEN | no change, EVEN | identical | identical |

### omni-v15 against native

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line | Decisions a day | Governor CPU a day | Cluster reads a day | Writes a day | The fast check's rescues a day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 s | down 2.2%, GAIN | down 1.2%, GAIN | up 20.5%, LOSS | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN | 17,280 | 91.6 s | 86,412 | 6,516 | 0.0 |
| 10 s | down 1.7%, GAIN | down 0.9%, GAIN | up 15.9%, LOSS | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN | 8,640 | 56.6 s | 60,682 | 3,151 | 1.2 |
| 15 s | down 1.9%, GAIN | down 1.0%, GAIN | up 22.2%, LOSS | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN | 5,760 | 44.4 s | 52,124 | 2,093 | 0.0 |
| 20 s | down 1.1%, EVEN | down 0.5%, EVEN | up 13.2%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN | 4,320 | 39.0 s | 47,792 | 1,572 | 3.8 |
| 30 s | down 1.4%, GAIN | down 0.8%, GAIN | up 11.0%, EVEN | no change, EVEN | identical | identical | 2,880 | 33.2 s | 43,515 | 1,045 | 2.5 |
| 60 s | down 1.0%, EVEN | down 0.5%, EVEN | up 7.5%, EVEN | no change, EVEN | identical | identical | 1,440 | 26.7 s | 39,091 | 538 | 5.5 |
| 75 s | down 1.4%, EVEN | down 0.7%, EVEN | up 9.5%, EVEN | no change, EVEN | identical | identical | 1,152 | 25.7 s | 38,292 | 429 | 6.8 |
| 90 s | down 0.8%, EVEN | down 0.4%, GAIN | up 8.2%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN | 960 | 24.8 s | 37,462 | 360 | 6.0 |
| 120 s | down 0.7%, EVEN | down 0.4%, GAIN | up 4.9%, EVEN | no change, EVEN | identical | identical | 720 | 23.9 s | 36,702 | 285 | 5.4 |

#### omni-v15 at each beat against itself at 15 s (the factory's beat)

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | down 0.3%, EVEN | down 0.2%, EVEN | down 1.3%, EVEN | no change, EVEN | up 0.1%, EVEN | up 0.5%, EVEN |
| 10 s | up 0.3%, EVEN | up 0.1%, EVEN | down 5.1%, EVEN | no change, EVEN | up 0.1%, EVEN | up 0.5%, EVEN |
| 20 s | up 0.9%, power given | up 0.5%, power given | down 7.3%, EVEN | no change, EVEN | no change, EVEN | identical |
| 30 s | up 0.6%, EVEN | up 0.2%, EVEN | down 9.2%, EVEN | no change, EVEN | down 0.6%, EVEN | down 0.5%, EVEN |
| 60 s | up 1.0%, EVEN | up 0.5%, EVEN | down 12.0%, EVEN | no change, EVEN | down 0.6%, EVEN | down 0.5%, EVEN |
| 75 s | up 0.5%, EVEN | up 0.3%, EVEN | down 10.4%, GAIN | no change, EVEN | down 0.6%, EVEN | down 0.5%, EVEN |
| 90 s | up 1.1%, EVEN | up 0.6%, power given | down 11.4%, EVEN | no change, EVEN | no change, EVEN | identical |
| 120 s | up 1.3%, EVEN | up 0.6%, power given | down 14.1%, EVEN | no change, EVEN | down 0.6%, EVEN | down 0.5%, EVEN |

#### omni-v15 at each beat against itself at 60 s

| Beat | Machine-hours | Energy per used core-hour | Pods waiting for a place | 95th percentile response | 99th percentile response | Minutes over the line |
|---|---|---|---|---|---|---|
| 5 s | down 1.2%, EVEN | down 0.7%, EVEN | up 12.1%, EVEN | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN |
| 10 s | down 0.7%, EVEN | down 0.4%, EVEN | up 7.8%, EVEN | no change, EVEN | up 0.7%, EVEN | up 0.9%, EVEN |
| 15 s | down 0.9%, EVEN | down 0.5%, EVEN | up 13.6%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN |
| 20 s | down 0.1%, EVEN | no change, EVEN | up 5.3%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN |
| 30 s | down 0.4%, EVEN | down 0.3%, EVEN | up 3.2%, EVEN | no change, EVEN | identical | identical |
| 75 s | down 0.4%, EVEN | down 0.2%, EVEN | up 1.8%, EVEN | no change, EVEN | identical | identical |
| 90 s | up 0.2%, EVEN | up 0.1%, EVEN | up 0.7%, EVEN | no change, EVEN | up 0.6%, EVEN | up 0.5%, EVEN |
| 120 s | up 0.3%, EVEN | up 0.1%, EVEN | down 2.4%, EVEN | no change, EVEN | identical | identical |

Native's means over the seeds: machine-hours 133.076; energy per used core-hour 0.036; pods waiting for a place 7.311; 95th percentile response 79.914; 99th percentile response 153.537; minutes over the line 27.000.

