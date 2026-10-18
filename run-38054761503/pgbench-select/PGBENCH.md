# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,435 tps; base rate 3,965 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,629 | 11,625 | -0.0% (-0.1 to +0.0) | no difference beyond the noise |
| throughput (transactions a second) | 11,629 | 11,625 | -0.0% (-0.1 to +0.0) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.3 | 1.3 | -0.5% (-35.0 to +33.9) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.05 | 3.18 | +4.3% (-39.6 to +48.3) | no difference beyond the noise |
| latency, median (ms) | 0.274 | 0.275 | +0.1% (-2.6 to +2.9) | no difference beyond the noise |
| latency, mean (ms) | 0.454 | 0.464 | +2.3% (-25.6 to +30.1) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.7 | 18.2 | -7.2% (-8.1 to -6.4) | better |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.457 | 0.457 | -0.1% (-1.7 to +1.6) | no difference beyond the noise |
| host CPU-seconds | 794.6 | 793.9 | -0.1% (-1.8 to +1.7) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.152 | -0.0% (-1.8 to +1.7) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.63 | 4.23 | +16.4% (+15.3 to +17.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.7 | -6.4% (-12.1 to -0.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 27, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11634 / 1.2 / 20.0 / 20.0; omni 11627 / 1.3 / 18.7 / 19.0
- rep 2 (omni then native): native 11625 / 1.5 / 19.0 / 20.0; omni 11623 / 1.3 / 17.5 / 18.2
- rep 3 (native then omni): native 11628 / 1.3 / 20.0 / 20.0; omni 11624 / 1.4 / 18.5 / 19.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
