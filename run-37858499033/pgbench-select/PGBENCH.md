# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,708 tps; base rate 2,356 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,909 | 6,905 | -0.1% (-0.4 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 6,909 | 6,906 | -0.0% (-0.3 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.08 | 1.28 | +17.6% (-2.5 to +37.8) | no difference beyond the noise |
| latency, 99th percentile (ms) | 2.71 | 7.45 | +175.2% (+25.9 to +324.4) | **WORSE** |
| latency, median (ms) | 0.363 | 0.365 | +0.7% (-3.3 to +4.7) | no difference beyond the noise |
| latency, mean (ms) | 0.497 | 0.725 | +46.0% (+24.8 to +67.1) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 18.8 | 11.6 | -38.3% (-60.8 to -15.7) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.302 | 0.309 | +2.4% (-4.9 to +9.7) | no difference beyond the noise |
| host CPU-seconds | 297.0 | 305.4 | +2.8% (-5.4 to +11.0) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.147 | +2.9% (-5.4 to +11.2) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.56 | 2.41 | +54.3% (+45.2 to +63.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 14.0 | -29.9% (-30.2 to -29.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 213, 224, 222; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6911 / 1.4 / 20.0 / 20.0; omni 6909 / 1.5 / 11.8 / 14.0
- rep 2 (omni then native): native 6903 / 0.9 / 16.4 / 20.0; omni 6904 / 1.1 / 11.2 / 14.0
- rep 3 (native then omni): native 6914 / 0.9 / 20.0 / 20.0; omni 6900 / 1.2 / 11.9 / 14.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
