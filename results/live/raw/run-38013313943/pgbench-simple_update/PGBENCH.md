# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,549 tps; base rate 1,132 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,124 | 3,133 | +0.3% (-5.3 to +5.9) | no difference beyond the noise |
| throughput (transactions a second) | 3,322 | 3,319 | -0.1% (-0.5 to +0.3) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 90.7 | 111.5 | +22.9% (-253.8 to +299.6) | no difference beyond the noise |
| latency, 99th percentile (ms) | 585.4 | 559.2 | -4.5% (-31.4 to +22.5) | no difference beyond the noise |
| latency, median (ms) | 0.707 | 0.711 | +0.7% (-3.7 to +5.0) | no difference beyond the noise |
| latency, mean (ms) | 21.6 | 20.8 | -3.5% (-87.5 to +80.6) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 18.6 | -6.9% (-11.4 to -2.4) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.353 | 0.356 | +0.7% (-4.1 to +5.6) | no difference beyond the noise |
| host CPU-seconds | 602.1 | 606.2 | +0.7% (-4.1 to +5.4) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.428 | 0.43 | +0.4% (-3.3 to +4.1) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.87 | 1.48 | +69.6% (+61.5 to +77.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | -6.2% (-10.4 to -2.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 92, 105, 70; fail-ups per arm: 2, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3088 / 104.8 / 20.0 / 20.0; omni 3178 / 11.6 / 18.2 / 18.4
- rep 2 (omni then native): native 3151 / 62.6 / 19.9 / 20.0; omni 3119 / 119.1 / 18.6 / 18.8
- rep 3 (native then omni): native 3133 / 104.8 / 20.0 / 20.0; omni 3101 / 203.9 / 18.9 / 19.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
