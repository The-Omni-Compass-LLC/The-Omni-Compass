# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,340 tps; base rate 2,451 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,190 | 7,193 | +0.0% (-0.2 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 7,190 | 7,193 | +0.0% (-0.2 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.17 | 1.25 | +6.6% (-15.1 to +28.3) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.21 | 3.69 | +14.7% (-29.2 to +58.5) | no difference beyond the noise |
| latency, median (ms) | 0.365 | 0.366 | +0.5% (-2.1 to +3.0) | no difference beyond the noise |
| latency, mean (ms) | 0.534 | 0.542 | +1.5% (-18.6 to +21.6) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.7 | 18.5 | -6.3% (-12.3 to -0.3) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.313 | 0.316 | +0.8% (-3.0 to +4.6) | no difference beyond the noise |
| host CPU-seconds | 461.1 | 465.3 | +0.9% (-3.7 to +5.5) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.144 | +0.9% (-3.9 to +5.6) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.6 | 3.38 | +30.1% (+27.1 to +33.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.0% (-5.0 to -4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 23, 25, 23; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7189 / 1.2 / 20.0 / 20.0; omni 7193 / 1.2 / 18.5 / 19.0
- rep 2 (omni then native): native 7188 / 1.2 / 19.2 / 20.0; omni 7196 / 1.2 / 18.5 / 19.0
- rep 3 (native then omni): native 7192 / 1.1 / 20.0 / 20.0; omni 7189 / 1.3 / 18.5 / 19.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
