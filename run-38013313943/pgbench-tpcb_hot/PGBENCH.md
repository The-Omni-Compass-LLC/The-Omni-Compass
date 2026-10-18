# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,530 tps; base rate 380 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,107 | 1,112 | +0.4% (-2.1 to +2.9) | no difference beyond the noise |
| throughput (transactions a second) | 1,114 | 1,115 | +0.1% (-0.5 to +0.7) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.93 | 3.82 | -2.8% (-52.7 to +47.0) | no difference beyond the noise |
| latency, 99th percentile (ms) | 38.9 | 15.9 | -59.1% (-427.4 to +309.3) | no difference beyond the noise |
| latency, median (ms) | 1.39 | 1.41 | +1.2% (+0.1 to +2.4) | **WORSE** |
| latency, mean (ms) | 2.48 | 2.17 | -12.4% (-151.2 to +126.4) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.2 | 17.2 | -10.7% (-22.9 to +1.5) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.263 | 0.267 | +1.4% (-0.0 to +2.8) | no difference beyond the noise |
| host CPU-seconds | 459.9 | 466.2 | +1.4% (-0.0 to +2.7) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.923 | 0.932 | +1.0% (-2.7 to +4.6) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.691 | 1.31 | +89.1% (+85.7 to +92.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.6% (-14.3 to -8.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 41, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1097 / 4.7 / 20.0 / 20.0; omni 1114 / 3.7 / 17.3 / 17.4
- rep 2 (omni then native): native 1111 / 3.6 / 17.7 / 20.0; omni 1108 / 4.1 / 16.8 / 17.8
- rep 3 (native then omni): native 1114 / 3.5 / 20.0 / 20.0; omni 1114 / 3.7 / 17.5 / 17.8


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
