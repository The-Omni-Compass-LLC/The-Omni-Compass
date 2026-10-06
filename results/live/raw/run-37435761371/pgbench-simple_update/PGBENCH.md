# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,787 tps; base rate 568 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,613 | 1,411 | -12.5% (-21.7 to -3.4) | **WORSE** |
| throughput (transactions a second) | 1,666 | 1,658 | -0.5% (-1.4 to +0.5) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 25.6 | 381.6 | +1390.9% (+233.9 to +2547.8) | **WORSE** |
| latency, 99th percentile (ms) | 201.1 | 602.7 | +199.7% (+15.4 to +383.9) | **WORSE** |
| latency, median (ms) | 1.63 | 2.05 | +25.8% (+22.4 to +29.2) | **WORSE** |
| latency, mean (ms) | 9.08 | 48.5 | +434.6% (+18.7 to +850.6) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.5 | 12.8 | -34.1% (-42.3 to -25.8) | better |
| server connections alive, most at once | 20.0 | 35.0 | +75.0% (+62.6 to +87.4) | **WORSE** |
| host CPU busy (share of the run) | 0.38 | 0.47 | +23.6% (+19.1 to +28.1) | **WORSE** |
| host CPU-seconds | 387.2 | 492.3 | +27.1% (+22.1 to +32.2) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.8 | 1.16 | +45.4% (+38.3 to +52.5) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 12.5 | -37.4% (-44.5 to -30.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 167, 144, 180; fail-ups per arm: 3, 3, 4.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1643 / 13.8 / 20.0 / 20.0; omni 1387 / 290.2 / 12.8 / 12.1
- rep 2 (omni then native): native 1608 / 18.8 / 18.4 / 20.0; omni 1397 / 511.8 / 12.4 / 12.3
- rep 3 (native then omni): native 1587 / 44.2 / 20.0 / 20.0; omni 1448 / 342.8 / 13.3 / 13.2


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
