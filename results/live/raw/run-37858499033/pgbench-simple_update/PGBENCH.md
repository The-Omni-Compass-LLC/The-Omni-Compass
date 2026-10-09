# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,570 tps; base rate 386 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,036 | 1,051 | +1.4% (-15.4 to +18.3) | no difference beyond the noise |
| throughput (transactions a second) | 1,130 | 1,132 | +0.2% (+0.1 to +0.3) | better |
| latency, 95th percentile (ms, lag included) | 86.3 | 77.7 | -10.0% (-207.9 to +187.9) | no difference beyond the noise |
| latency, 99th percentile (ms) | 300.3 | 216.4 | -27.9% (-123.3 to +67.4) | no difference beyond the noise |
| latency, median (ms) | 0.843 | 0.84 | -0.3% (-5.8 to +5.2) | no difference beyond the noise |
| latency, mean (ms) | 15.3 | 12.5 | -18.4% (-164.1 to +127.2) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 21.9 | +9.3% (-3.4 to +22.1) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 34.3 | +71.7% (+52.7 to +90.6) | **WORSE** |
| host CPU busy (share of the run) | 0.179 | 0.182 | +1.7% (+1.5 to +1.9) | **WORSE** |
| host CPU-seconds | 209.2 | 212.6 | +1.6% (+1.1 to +2.2) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.674 | 0.675 | +0.2% (-17.0 to +17.4) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.439 | 0.949 | +116.3% (+108.5 to +124.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.2 | +11.1% (-1.9 to +24.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 134, 139, 129; fail-ups per arm: 2, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1049 / 73.1 / 20.0 / 20.0; omni 1034 / 100.9 / 22.6 / 23.0
- rep 2 (omni then native): native 1062 / 64.2 / 20.0 / 20.0; omni 1026 / 98.5 / 22.3 / 22.6
- rep 3 (native then omni): native 997 / 121.5 / 20.0 / 20.0; omni 1092 / 33.6 / 20.7 / 21.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
