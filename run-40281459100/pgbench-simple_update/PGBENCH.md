# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,911 tps; base rate 587 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,687 | 1,683 | -0.2% (-1.5 to +1.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,720 | 1,721 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.44 | 7.07 | -5.0% (-25.0 to +15.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 141.7 | 159.0 | +12.2% (-91.8 to +116.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.51 | 1.51 | -0.1% (-3.3 to +3.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.35 | 5.55 | +3.7% (-39.3 to +46.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.3% (-4.7 to +2.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.345 | 0.344 | -0.0% (-3.3 to +3.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 519.3 | 518.8 | -0.1% (-3.7 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.684 | 0.685 | +0.1% (-4.3 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.23 | +31.9% (+28.2 to +35.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.8 | -0.8% (-4.4 to +2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 26, 29; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1699 / 7.5 / 20.0 / 20.0; omni 1685 / 6.9 / 19.5 / 19.6
- rep 2 (omni then native): native 1681 / 7.7 / 19.9 / 20.0; omni 1683 / 6.9 / 19.6 / 19.8
- rep 3 (native then omni): native 1680 / 7.2 / 20.0 / 20.0; omni 1681 / 7.5 / 20.0 / 20.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
