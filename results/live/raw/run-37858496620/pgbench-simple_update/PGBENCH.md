# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,872 tps; base rate 1,181 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,156 | 3,078 | -2.5% (-6.8 to +1.9) | no difference beyond the noise |
| throughput (transactions a second) | 3,456 | 3,455 | -0.0% (-1.2 to +1.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 223.4 | 345.7 | +54.8% (-74.2 to +183.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 702.2 | 687.7 | -2.1% (-22.0 to +17.9) | no difference beyond the noise |
| latency, median (ms) | 0.779 | 0.787 | +1.0% (-4.1 to +6.2) | no difference beyond the noise |
| latency, mean (ms) | 32.1 | 41.8 | +30.1% (-51.3 to +111.5) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 22.0 | +10.3% (-3.6 to +24.1) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 35.7 | +78.3% (+71.2 to +85.5) | **WORSE** |
| host CPU busy (share of the run) | 0.379 | 0.389 | +2.7% (-0.4 to +5.8) | no difference beyond the noise |
| host CPU-seconds | 430.5 | 442.3 | +2.7% (-0.3 to +5.8) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.455 | 0.48 | +5.3% (+0.2 to +10.5) | **WORSE** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.596 | 1.11 | +86.9% (+73.9 to +99.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.5 | +12.3% (-0.8 to +25.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 182, 202, 171; fail-ups per arm: 2, 2, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3042 / 309.1 / 20.0 / 20.0; omni 2944 / 474.8 / 22.6 / 23.1
- rep 2 (omni then native): native 3230 / 131.7 / 19.9 / 20.0; omni 3109 / 342.0 / 20.6 / 21.2
- rep 3 (native then omni): native 3195 / 229.3 / 20.0 / 20.0; omni 3179 / 220.3 / 22.8 / 23.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
