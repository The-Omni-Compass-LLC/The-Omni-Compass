# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,448 tps; base rate 667 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,128 | 1,410 | +24.9% (-47.5 to +97.4) | no difference beyond the noise |
| throughput (transactions a second) | 1,914 | 1,947 | +1.7% (-7.7 to +11.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,060 | 804.6 | -60.9% (-300.3 to +178.4) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3,953 | 1,520 | -61.6% (-301.5 to +178.4) | no difference beyond the noise |
| latency, median (ms) | 15.3 | 2.82 | -81.5% (-263.9 to +100.9) | no difference beyond the noise |
| latency, mean (ms) | 382.4 | 137.0 | -64.2% (-296.7 to +168.3) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 20.4 | +2.2% (+0.8 to +3.6) | **WORSE** |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (+4.5 to +18.8) | **WORSE** |
| host CPU busy (share of the run) | 0.302 | 0.309 | +2.1% (-8.6 to +12.8) | no difference beyond the noise |
| host CPU-seconds | 530.2 | 538.0 | +1.5% (-7.5 to +10.4) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.05 | 0.863 | -17.8% (-63.1 to +27.5) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.82 | 1.44 | +76.0% (+70.8 to +81.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.4 | +1.9% (+1.0 to +2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 31, 37; fail-ups per arm: 5, 10, 13.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1004 / 3671.7 / 20.0 / 20.0; omni 1663 / 195.2 / 20.3 / 20.3
- rep 2 (omni then native): native 1152 / 1032.4 / 20.0 / 20.0; omni 1210 / 1374.8 / 20.5 / 20.4
- rep 3 (native then omni): native 1229 / 1475.4 / 20.0 / 20.0; omni 1356 / 843.7 / 20.5 / 20.4


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
