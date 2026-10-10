# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,754 tps; base rate 563 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,611 | 1,613 | +0.1% (-1.1 to +1.3) | no difference beyond the noise |
| throughput (transactions a second) | 1,653 | 1,652 | -0.1% (-0.2 to +0.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.46 | 6.18 | -4.3% (-28.3 to +19.8) | no difference beyond the noise |
| latency, 99th percentile (ms) | 198.8 | 182.9 | -8.0% (-37.9 to +21.8) | no difference beyond the noise |
| latency, median (ms) | 1.53 | 1.53 | -0.1% (-0.9 to +0.8) | no difference beyond the noise |
| latency, mean (ms) | 6.5 | 6.1 | -6.1% (-39.2 to +27.0) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -4.0% (-5.1 to -2.8) | better |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | **WORSE** |
| host CPU busy (share of the run) | 0.336 | 0.336 | +0.0% (-1.0 to +1.0) | no difference beyond the noise |
| host CPU-seconds | 506.2 | 506.2 | +0.0% (-1.2 to +1.2) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.698 | 0.698 | -0.1% (-2.2 to +2.0) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1 | 1.81 | +80.9% (+77.8 to +84.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -2.9% (-4.7 to -1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 53, 48, 49; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1616 / 6.2 / 20.0 / 20.0; omni 1615 / 6.2 / 19.3 / 19.5
- rep 2 (omni then native): native 1611 / 6.3 / 19.9 / 20.0; omni 1607 / 6.5 / 19.2 / 19.5
- rep 3 (native then omni): native 1605 / 6.9 / 20.0 / 20.0; omni 1616 / 5.9 / 19.1 / 19.3


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
