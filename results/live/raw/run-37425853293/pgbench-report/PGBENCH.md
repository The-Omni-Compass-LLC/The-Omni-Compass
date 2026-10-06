# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 25,978 tps; base rate 3,897 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine differs from v2: realms/catalog_v1.csv at `a5d13663ef4a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,423 | 5,995 | -47.5% (-56.0 to -39.0) | **WORSE** |
| throughput (transactions a second) | 11,428 | 10,373 | -9.2% (-9.6 to -8.8) | **WORSE** |
| latency, 95th percentile (ms, lag included) | 4.06 | 3,886 | +95700.0% (+93469.8 to +97930.1) | **WORSE** |
| latency, 99th percentile (ms) | 15.9 | 5,996 | +37692.6% (+36645.9 to +38739.4) | **WORSE** |
| latency, median (ms) | 0.259 | 4.12 | +1491.0% (+1348.4 to +1633.6) | **WORSE** |
| latency, mean (ms) | 0.963 | 759.8 | +78834.2% (+76703.4 to +80964.9) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.2 | 2.48 | -87.1% (-103.9 to -70.3) | better |
| server connections alive, most at once | 20.0 | 16.3 | -18.3% (-97.2 to +60.6) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.449 | 0.447 | -0.4% (-0.6 to -0.2) | better |
| host CPU-seconds | 515.2 | 510.3 | -1.0% (-1.2 to -0.7) | better |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.285 | +89.3% (+57.4 to +121.1) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 2.54 | -87.3% (-87.3 to -87.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 18, 18; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11424 / 3.4 / 20.0 / 20.0; omni 5573 / 3889.9 / 2.6 / 2.5
- rep 2 (omni then native): native 11431 / 4.5 / 17.5 / 20.0; omni 6351 / 3920.3 / 2.3 / 2.5
- rep 3 (native then omni): native 11414 / 4.2 / 20.0 / 20.0; omni 6061 / 3847.7 / 2.5 / 2.5

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,929 tps; base rate 889 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine differs from v2: realms/catalog_v1.csv at `a5d13663ef4a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,478 | 2,123 | -14.3% (-35.9 to +7.3) | no difference beyond the noise |
| throughput (transactions a second) | 2,608 | 2,598 | -0.4% (-1.8 to +1.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 64.9 | 553.7 | +753.4% (-104.8 to +1611.6) | no difference beyond the noise |
| latency, 99th percentile (ms) | 568.5 | 879.0 | +54.6% (-76.9 to +186.2) | no difference beyond the noise |
| latency, median (ms) | 1.15 | 1.43 | +23.8% (+17.7 to +30.0) | **WORSE** |
| latency, mean (ms) | 19.9 | 79.9 | +301.7% (-307.0 to +910.4) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 8.11 | -59.5% (-62.2 to -56.7) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.411 | 0.452 | +9.9% (+8.1 to +11.7) | **WORSE** |
| host CPU-seconds | 474.5 | 522.4 | +10.1% (+8.2 to +12.0) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.638 | 0.825 | +29.3% (-2.1 to +60.6) | no difference beyond the noise |
| pool size, mean (the knob) | 20.0 | 7.99 | -60.1% (-61.5 to -58.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 155, 145, 125; fail-ups per arm: 8, 7, 7.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2492 / 27.8 / 20.0 / 20.0; omni 1895 / 766.7 / 8.4 / 7.9
- rep 2 (omni then native): native 2452 / 144.9 / 20.0 / 20.0; omni 2267 / 451.1 / 8.0 / 8.1
- rep 3 (native then omni): native 2489 / 21.9 / 20.0 / 20.0; omni 2207 / 443.2 / 8.0 / 7.9

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,936 tps; base rate 290 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine differs from v2: realms/catalog_v1.csv at `a5d13663ef4a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 850.0 | 806.9 | -5.1% (-10.5 to +0.4) | no difference beyond the noise |
| throughput (transactions a second) | 850.6 | 851.3 | +0.1% (-0.0 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.37 | 53.7 | +541.9% (-92.5 to +1176.2) | no difference beyond the noise |
| latency, 99th percentile (ms) | 24.4 | 195.9 | +701.8% (-269.1 to +1672.8) | no difference beyond the noise |
| latency, median (ms) | 1.96 | 2.38 | +21.7% (+16.4 to +27.0) | **WORSE** |
| latency, mean (ms) | 3.12 | 12.1 | +288.6% (+21.2 to +556.0) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.0 | 5.28 | -72.3% (-87.7 to -56.8) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.267 | 0.314 | +17.5% (+11.8 to +23.1) | **WORSE** |
| host CPU-seconds | 279.3 | 329.4 | +17.9% (+11.7 to +24.2) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 1.1 | 1.36 | +24.3% (+12.0 to +36.6) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 5.37 | -73.1% (-77.5 to -68.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 78, 75, 60; fail-ups per arm: 5, 3, 4.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 850 / 8.9 / 20.0 / 20.0; omni 786 / 78.6 / 5.7 / 5.7
- rep 2 (omni then native): native 848 / 6.9 / 17.1 / 20.0; omni 810 / 43.3 / 4.7 / 5.0
- rep 3 (native then omni): native 852 / 9.3 / 20.0 / 20.0; omni 824 / 39.3 / 5.4 / 5.4


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
