# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,361 tps; base rate 3,954 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,600 | 11,594 | -0.1% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,600 | 11,595 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.36 | 2.13 | -9.6% (-20.2 to +1.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.29 | 6.12 | -16.1% (-19.4 to -12.8) | GAIN |
| latency, median (ms) | 0.254 | 0.252 | -0.5% (-2.0 to +1.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.593 | 0.554 | -6.5% (-14.4 to +1.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.4 | -6.9% (-8.4 to -5.4) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.436 | 0.434 | -0.3% (-1.5 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 747.8 | 745.2 | -0.4% (-1.5 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | -0.3% (-1.3 to +0.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.93 | 3.6 | +23.1% (+17.3 to +28.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.6% (-7.5 to -3.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 30, 30; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11604 / 2.5 / 20.0 / 20.0; omni 11593 / 2.4 / 18.6 / 18.7
- rep 2 (omni then native): native 11608 / 2.6 / 19.2 / 20.0; omni 11596 / 2.3 / 17.7 / 18.9
- rep 3 (native then omni): native 11588 / 2.0 / 20.0 / 20.0; omni 11592 / 1.7 / 18.8 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
