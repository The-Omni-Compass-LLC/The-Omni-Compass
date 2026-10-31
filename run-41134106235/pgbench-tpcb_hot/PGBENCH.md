# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,860 tps; base rate 279 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 817.3 | 817.2 | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 817.4 | 818.2 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.9 | 5.05 | +3.0% (-15.7 to +21.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.1 | 11.5 | +13.2% (-29.2 to +55.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.81 | 1.8 | -0.5% (-3.4 to +2.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.35 | 2.58 | +9.7% (-25.3 to +44.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-33.0 to +53.0) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.294 | 0.293 | -0.4% (-2.6 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 507.3 | 505.7 | -0.3% (-2.5 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.38 | 1.38 | -0.3% (-2.6 to +2.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.46 | 2.14 | +46.4% (+45.1 to +47.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (-0.1 to +0.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 2, 0; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 818 / 5.1 / 20.0 / 20.0; omni 818 / 5.6 / 20.0 / 20.0
- rep 2 (omni then native): native 815 / 4.7 / 20.0 / 20.0; omni 815 / 4.9 / 20.0 / 20.0
- rep 3 (native then omni): native 819 / 4.9 / 20.0 / 20.0; omni 819 / 4.6 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
