# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,729 tps; base rate 2,509 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,357 | 7,350 | -0.1% (-0.4 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 7,357 | 7,352 | -0.1% (-0.2 to +0.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.33 | 1.92 | -17.9% (-60.1 to +24.3) | no difference beyond the noise |
| latency, 99th percentile (ms) | 6.06 | 5.89 | -2.8% (-45.8 to +40.1) | no difference beyond the noise |
| latency, median (ms) | 0.388 | 0.385 | -0.9% (-4.6 to +2.9) | no difference beyond the noise |
| latency, mean (ms) | 0.706 | 0.71 | +0.5% (-38.8 to +39.8) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.9 | 18.6 | -6.7% (-11.4 to -1.9) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.348 | 0.346 | -0.7% (-3.1 to +1.7) | no difference beyond the noise |
| host CPU-seconds | 520.6 | 516.3 | -0.8% (-3.8 to +2.1) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.157 | 0.156 | -0.7% (-3.9 to +2.4) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.67 | 3.52 | +31.7% (+25.3 to +38.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | -6.0% (-10.7 to -1.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 50, 72, 44; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7358 / 1.9 / 20.0 / 20.0; omni 7353 / 1.8 / 19.0 / 19.1
- rep 2 (omni then native): native 7357 / 2.3 / 19.7 / 20.0; omni 7340 / 2.0 / 18.0 / 18.4
- rep 3 (native then omni): native 7357 / 2.8 / 20.0 / 20.0; omni 7357 / 1.9 / 18.8 / 18.9


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
