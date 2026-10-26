# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,839 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,658 | 1,657 | -0.0% (-0.8 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,690 | 1,689 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.05 | 5.93 | -2.0% (-11.3 to +7.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 146.0 | 148.4 | +1.6% (-61.6 to +64.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.48 | 1.48 | +0.0% (-0.8 to +0.8) | EVEN, the same |
| latency, mean (ms) | 5.02 | 4.91 | -2.2% (-41.4 to +37.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.2% (-6.4 to +0.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.333 | 0.334 | +0.2% (+0.1 to +0.3) | power given |
| host CPU-seconds | 501.1 | 502.2 | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.672 | 0.673 | +0.2% (-0.7 to +1.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.4 | 3.15 | +30.9% (+24.9 to +36.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | -2.0% (-3.5 to -0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 35, 31; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1666 / 6.2 / 20.0 / 20.0; omni 1660 / 5.9 / 19.6 / 19.7
- rep 2 (omni then native): native 1648 / 6.2 / 19.9 / 20.0; omni 1651 / 6.0 / 19.3 / 19.6
- rep 3 (native then omni): native 1659 / 5.8 / 20.0 / 20.0; omni 1662 / 5.9 / 19.1 / 19.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
