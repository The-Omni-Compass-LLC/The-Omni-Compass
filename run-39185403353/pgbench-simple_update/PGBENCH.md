# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,861 tps; base rate 579 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `ce92ff888e73`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,652 | 1,652 | +0.1% (-2.1 to +2.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,699 | 1,697 | -0.1% (-0.4 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.33 | 7.77 | -6.7% (-33.9 to +20.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 211.2 | 189.4 | -10.3% (-72.9 to +52.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.53 | 1.53 | +0.1% (-1.3 to +1.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.2 | 6.79 | -5.8% (-57.6 to +46.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -3.9% (-8.0 to +0.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.344 | 0.344 | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 517.0 | 517.7 | +0.1% (-0.3 to +0.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.696 | 0.696 | +0.1% (-2.5 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.8 | +76.8% (+72.1 to +81.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.5% (-6.2 to +1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 36, 35, 21; fail-ups per arm: 0, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1657 / 7.7 / 20.0 / 20.0; omni 1651 / 8.1 / 19.2 / 19.4
- rep 2 (omni then native): native 1644 / 9.7 / 20.0 / 20.0; omni 1636 / 9.0 / 18.9 / 19.3
- rep 3 (native then omni): native 1653 / 7.6 / 20.0 / 20.0; omni 1670 / 6.2 / 19.6 / 19.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
