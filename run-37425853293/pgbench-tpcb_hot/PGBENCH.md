# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

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
