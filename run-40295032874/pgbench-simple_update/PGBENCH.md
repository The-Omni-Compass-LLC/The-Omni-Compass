# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,642 tps; base rate 1,146 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `c8b8e2af081f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,155 | 3,155 | +0.0% (-3.5 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,359 | 3,363 | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 91.1 | 150.0 | +64.8% (-161.0 to +290.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 601.6 | 666.6 | +10.8% (-32.1 to +53.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.7 | 0.69 | -1.4% (-5.2 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 21.4 | 25.1 | +17.2% (-61.1 to +95.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.9 | -0.4% (-3.7 to +2.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 23.0 | +15.0% (+15.0 to +15.0) | power given |
| host CPU busy (share of the run) | 0.355 | 0.35 | -1.2% (-4.7 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 606.2 | 598.6 | -1.3% (-5.0 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.427 | 0.422 | -1.3% (-8.5 to +5.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.31 | 2.8 | +21.2% (+15.1 to +27.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.2% (-2.8 to +2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 40, 44, 41; fail-ups per arm: 1, 3, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3130 / 87.6 / 20.0 / 20.0; omni 3180 / 69.8 / 20.2 / 20.2
- rep 2 (omni then native): native 3170 / 101.3 / 20.0 / 20.0; omni 3131 / 247.9 / 19.6 / 19.8
- rep 3 (native then omni): native 3165 / 84.3 / 20.0 / 20.0; omni 3154 / 132.4 / 19.9 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
