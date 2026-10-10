# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,867 tps; base rate 280 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 821.5 | 821.6 | +0.0% (-0.2 to +0.3) | no difference beyond the noise |
| throughput (transactions a second) | 821.6 | 821.8 | +0.0% (-0.3 to +0.4) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.45 | 4.33 | -2.7% (-33.0 to +27.6) | no difference beyond the noise |
| latency, 99th percentile (ms) | 9.12 | 9.31 | +2.1% (-57.7 to +61.8) | no difference beyond the noise |
| latency, median (ms) | 1.86 | 1.83 | -1.4% (-6.7 to +3.8) | no difference beyond the noise |
| latency, mean (ms) | 2.31 | 2.3 | -0.4% (-20.1 to +19.2) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.8 | 18.4 | -7.0% (-12.4 to -1.5) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.23 | 0.225 | -1.9% (-8.1 to +4.4) | no difference beyond the noise |
| host CPU-seconds | 359.3 | 352.4 | -1.9% (-8.3 to +4.5) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.972 | 0.953 | -1.9% (-8.2 to +4.3) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.751 | 1.48 | +96.4% (+89.1 to +103.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.2% (-5.6 to -4.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 25, 27, 17; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 822 / 4.0 / 20.0 / 20.0; omni 822 / 4.6 / 18.5 / 19.0
- rep 2 (omni then native): native 822 / 4.6 / 19.3 / 20.0; omni 822 / 4.3 / 18.4 / 19.0
- rep 3 (native then omni): native 821 / 4.6 / 20.0 / 20.0; omni 820 / 4.2 / 18.3 / 18.9


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
