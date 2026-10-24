# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,536 tps; base rate 680 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `e4a97f22dce1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,388 | 1,123 | -19.1% (-92.9 to +54.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,980 | 1,940 | -2.0% (-5.9 to +1.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,057 | 3,623 | +242.6% (-43.4 to +528.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,661 | 5,117 | +208.0% (-89.4 to +505.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.63 | 30.7 | +1776.0% (-2882.0 to +6434.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 179.7 | 524.4 | +191.7% (-119.7 to +503.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.3 | +1.5% (-2.4 to +5.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.317 | 0.307 | -3.1% (-10.2 to +4.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 553.4 | 538.1 | -2.8% (-8.8 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.895 | 1.09 | +22.2% (-63.9 to +108.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.841 | 1.43 | +70.1% (+54.3 to +85.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.3 | +1.3% (-2.3 to +4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 12, 14, 44; fail-ups per arm: 5, 5, 12.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1573 / 487.4 / 20.0 / 20.0; omni 945 / 2143.4 / 20.1 / 20.1
- rep 2 (omni then native): native 1372 / 712.9 / 20.0 / 20.0; omni 1022 / 4661.1 / 20.1 / 20.1
- rep 3 (native then omni): native 1218 / 1972.2 / 20.0 / 20.0; omni 1402 / 4064.3 / 20.7 / 20.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
