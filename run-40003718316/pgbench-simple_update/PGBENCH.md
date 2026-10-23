# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,860 tps; base rate 579 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,647 | 1,654 | +0.4% (-4.0 to +4.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,696 | 1,699 | +0.1% (-0.6 to +0.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 9.82 | 8.51 | -13.4% (-84.1 to +57.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 210.5 | 189.1 | -10.2% (-126.9 to +106.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.57 | 1.58 | +0.4% (-0.5 to +1.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.49 | 6.84 | -8.7% (-116.5 to +99.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.2% (-9.9 to +3.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.353 | 0.355 | +0.6% (-0.2 to +1.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 531.8 | 534.5 | +0.5% (-0.3 to +1.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.718 | 0.718 | +0.1% (-4.2 to +4.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | +78.4% (+68.9 to +87.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.5% (-8.8 to +3.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 46, 45; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1647 / 12.0 / 20.0 / 20.0; omni 1654 / 8.6 / 20.0 / 20.1
- rep 2 (omni then native): native 1658 / 7.6 / 20.0 / 20.0; omni 1635 / 9.5 / 19.1 / 19.3
- rep 3 (native then omni): native 1635 / 9.9 / 20.0 / 20.0; omni 1672 / 7.5 / 19.0 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
