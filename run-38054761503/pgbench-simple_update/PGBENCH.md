# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,385 tps; base rate 1,108 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,980 | 2,965 | -0.5% (-3.3 to +2.3) | no difference beyond the noise |
| throughput (transactions a second) | 3,249 | 3,244 | -0.2% (-0.3 to +0.0) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 287.0 | 349.5 | +21.8% (-24.1 to +67.6) | no difference beyond the noise |
| latency, 99th percentile (ms) | 788.8 | 754.1 | -4.4% (-23.9 to +15.1) | no difference beyond the noise |
| latency, median (ms) | 0.941 | 0.938 | -0.4% (-2.6 to +1.8) | no difference beyond the noise |
| latency, mean (ms) | 35.9 | 38.3 | +6.5% (-25.1 to +38.0) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.5% (-6.5 to -0.6) | better |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (+4.5 to +18.8) | **WORSE** |
| host CPU busy (share of the run) | 0.403 | 0.403 | +0.1% (-2.2 to +2.4) | no difference beyond the noise |
| host CPU-seconds | 695.2 | 696.0 | +0.1% (-2.1 to +2.4) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.518 | 0.522 | +0.6% (-2.1 to +3.3) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.07 | 1.59 | +48.9% (+43.8 to +54.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -2.9% (-6.1 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 75, 66, 62; fail-ups per arm: 5, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2951 / 293.0 / 20.0 / 20.0; omni 2958 / 380.4 / 19.6 / 19.7
- rep 2 (omni then native): native 2993 / 278.8 / 20.0 / 20.0; omni 2995 / 280.4 / 19.1 / 19.2
- rep 3 (native then omni): native 2995 / 289.3 / 20.0 / 20.0; omni 2942 / 387.6 / 19.2 / 19.3


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
