# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb (tpcb (default), scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,626 tps; base rate 844 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine differs from v2: realms/catalog_v1.csv at `ce5eb806f43f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,137 | 2,152 | +0.7% (-18.2 to +19.5) | no difference beyond the noise |
| throughput (transactions a second) | 2,437 | 2,474 | +1.5% (-4.8 to +7.8) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,361 | 432.9 | -68.2% (-363.5 to +227.2) | no difference beyond the noise |
| latency, 99th percentile (ms) | 2,888 | 861.5 | -70.2% (-313.4 to +173.1) | no difference beyond the noise |
| latency, median (ms) | 0.98 | 1.09 | +11.5% (-6.9 to +29.9) | no difference beyond the noise |
| latency, mean (ms) | 171.1 | 56.5 | -67.0% (-330.9 to +197.0) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 9.32 | -53.4% (-56.9 to -49.9) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.379 | 0.42 | +10.8% (+8.6 to +13.0) | **WORSE** |
| host CPU-seconds | 433.0 | 479.5 | +10.7% (+7.7 to +13.7) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.679 | 0.743 | +9.4% (-10.4 to +29.2) | no difference beyond the noise |
| pool size, mean (the knob) | 20.0 | 9.53 | -52.4% (-53.2 to -51.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 161, 175, 163; fail-ups per arm: 9, 9, 9.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2301 / 86.1 / 20.0 / 20.0; omni 2154 / 398.0 / 9.6 / 9.6
- rep 2 (omni then native): native 1946 / 3330.9 / 20.0 / 20.0; omni 2124 / 572.7 / 9.4 / 9.5
- rep 3 (native then omni): native 2165 / 665.6 / 20.0 / 20.0; omni 2177 / 328.1 / 9.0 / 9.5


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
