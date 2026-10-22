# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,179 tps; base rate 477 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,324 | 1,237 | -6.5% (-23.4 to +10.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,394 | 1,393 | -0.1% (-0.1 to -0.0) | LOSS |
| latency, 95th percentile (ms, lag included) | 56.5 | 299.9 | +430.3% (-716.0 to +1576.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,750 | 922.2 | -66.5% (-215.4 to +82.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.844 | 0.854 | +1.2% (-7.1 to +9.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 71.4 | 51.0 | -28.6% (-234.4 to +177.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.4 | -2.9% (-7.1 to +1.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.212 | 0.215 | +1.2% (-5.1 to +7.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 366.3 | 371.0 | +1.3% (-5.2 to +7.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.615 | 0.67 | +8.9% (-16.6 to +34.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.572 | 1.05 | +83.2% (+71.5 to +95.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.3% (-5.7 to +1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 39, 21; fail-ups per arm: 2, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1327 / 50.7 / 20.0 / 20.0; omni 1343 / 8.4 / 19.5 / 19.5
- rep 2 (omni then native): native 1328 / 45.0 / 20.0 / 20.0; omni 1194 / 514.2 / 19.0 / 19.3
- rep 3 (native then omni): native 1317 / 74.0 / 20.0 / 20.0; omni 1174 / 377.0 / 19.7 / 19.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
