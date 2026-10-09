# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,835 tps; base rate 275 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 806.1 | 806.6 | +0.1% (-0.0 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 806.2 | 807.0 | +0.1% (-0.0 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.68 | 5.21 | +11.3% (+6.2 to +16.5) | **WORSE** |
| latency, 99th percentile (ms) | 9.23 | 14.8 | +60.4% (+16.7 to +104.0) | **WORSE** |
| latency, median (ms) | 1.88 | 1.9 | +0.7% (-3.1 to +4.4) | no difference beyond the noise |
| latency, mean (ms) | 2.37 | 2.6 | +9.6% (+2.3 to +16.8) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.5 | 10.5 | -46.1% (-58.2 to -34.0) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.223 | 0.228 | +2.4% (-2.6 to +7.4) | no difference beyond the noise |
| host CPU-seconds | 232.7 | 238.6 | +2.5% (-2.7 to +7.7) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.962 | 0.986 | +2.5% (-2.8 to +7.8) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.503 | 1.28 | +154.8% (+145.1 to +164.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 11.9 | -40.6% (-45.8 to -35.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 200, 209, 189; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 805 / 4.5 / 20.0 / 20.0; omni 805 / 5.1 / 10.4 / 11.8
- rep 2 (omni then native): native 806 / 4.8 / 18.4 / 20.0; omni 807 / 5.3 / 10.5 / 12.4
- rep 3 (native then omni): native 807 / 4.7 / 20.0 / 20.0; omni 807 / 5.3 / 10.5 / 11.6


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
