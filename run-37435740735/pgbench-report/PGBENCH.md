# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,366 tps; base rate 2,455 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,199 | 6,795 | -5.6% (-20.2 to +9.0) | no difference beyond the noise |
| throughput (transactions a second) | 7,199 | 7,181 | -0.2% (-1.2 to +0.7) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.66 | 142.9 | +5266.7% (-12868.4 to +23401.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 13.0 | 300.3 | +2206.5% (-4663.9 to +9076.9) | no difference beyond the noise |
| latency, median (ms) | 0.38 | 0.445 | +17.3% (+13.1 to +21.5) | **WORSE** |
| latency, mean (ms) | 0.878 | 17.1 | +1850.0% (-3999.5 to +7699.5) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.3 | 7.51 | -61.1% (-71.2 to -51.1) | better |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (-22.9 to +39.6) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.352 | 0.435 | +23.5% (+22.6 to +24.5) | **WORSE** |
| host CPU-seconds | 350.7 | 445.8 | +27.1% (+26.0 to +28.3) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.162 | 0.219 | +35.0% (+13.5 to +56.6) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 7.58 | -62.1% (-65.1 to -59.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 117, 102, 100; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7201 / 2.6 / 20.0 / 20.0; omni 6341 / 366.8 / 7.9 / 7.8
- rep 2 (omni then native): native 7198 / 2.7 / 18.0 / 20.0; omni 6872 / 44.8 / 7.0 / 7.3
- rep 3 (native then omni): native 7196 / 2.7 / 20.0 / 20.0; omni 7173 / 17.2 / 7.6 / 7.6

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,446 tps; base rate 667 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 997.4 | 1,252 | +25.6% (-78.9 to +130.0) | no difference beyond the noise |
| throughput (transactions a second) | 1,858 | 1,907 | +2.6% (-5.2 to +10.4) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3,122 | 1,249 | -60.0% (-139.7 to +19.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 5,405 | 2,292 | -57.6% (-154.3 to +39.1) | no difference beyond the noise |
| latency, median (ms) | 36.4 | 18.4 | -49.4% (-439.6 to +340.9) | no difference beyond the noise |
| latency, mean (ms) | 564.7 | 246.2 | -56.4% (-189.0 to +76.2) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 22.4 | +12.2% (+9.0 to +15.4) | **WORSE** |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+67.6 to +92.4) | **WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.365 | +18.7% (+10.9 to +26.5) | **WORSE** |
| host CPU-seconds | 360.6 | 425.7 | +18.0% (+11.6 to +24.5) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 1.22 | 1.18 | -3.3% (-92.2 to +85.6) | no difference beyond the noise |
| pool size, mean (the knob) | 20.0 | 21.4 | +7.1% (+1.0 to +13.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 189, 183, 207; fail-ups per arm: 26, 20, 18.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1132 / 3123.9 / 20.0 / 20.0; omni 910 / 2305.3 / 22.6 / 20.9
- rep 2 (omni then native): native 977 / 2815.5 / 20.0 / 20.0; omni 1395 / 826.4 / 22.5 / 21.7
- rep 3 (native then omni): native 883 / 3427.6 / 20.0 / 20.0; omni 1452 / 614.9 / 22.1 / 21.7

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,769 tps; base rate 415 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,217 | 1,182 | -2.9% (-8.2 to +2.5) | no difference beyond the noise |
| throughput (transactions a second) | 1,217 | 1,219 | +0.1% (-0.3 to +0.6) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.6 | 29.4 | +715.2% (-364.8 to +1795.3) | no difference beyond the noise |
| latency, 99th percentile (ms) | 10.8 | 107.6 | +898.7% (-445.0 to +2242.4) | no difference beyond the noise |
| latency, median (ms) | 1.3 | 1.49 | +15.2% (+7.8 to +22.5) | **WORSE** |
| latency, mean (ms) | 1.78 | 6.29 | +253.6% (-101.0 to +608.1) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.4 | 5.97 | -69.2% (-92.2 to -46.3) | better |
| server connections alive, most at once | 20.0 | 29.0 | +45.0% (-52.0 to +142.0) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.313 | 0.359 | +14.7% (+12.8 to +16.6) | **WORSE** |
| host CPU-seconds | 364.3 | 418.0 | +14.8% (+12.7 to +16.8) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.998 | 1.18 | +18.2% (+10.5 to +25.9) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 6.07 | -69.6% (-83.2 to -56.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 74, 73, 62; fail-ups per arm: 0, 2, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1217 / 3.6 / 20.0 / 20.0; omni 1169 / 35.6 / 6.2 / 6.1
- rep 2 (omni then native): native 1219 / 3.8 / 18.3 / 20.0; omni 1167 / 41.2 / 6.8 / 7.1
- rep 3 (native then omni): native 1215 / 3.4 / 20.0 / 20.0; omni 1210 / 11.3 / 5.0 / 5.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
