# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,849 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,645 | 1,639 | -0.4% (-4.1 to +3.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,695 | 1,690 | -0.3% (-0.8 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.68 | 9.43 | +22.8% (-101.6 to +147.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 206.8 | 202.8 | -1.9% (-75.3 to +71.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.52 | 1.52 | +0.3% (-0.7 to +1.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.16 | 7.3 | +1.9% (-87.8 to +91.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.6 | -6.9% (-9.5 to -4.4) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.342 | 0.342 | +0.1% (-1.7 to +2.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 513.7 | 514.3 | +0.1% (-1.7 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.697 | +0.5% (-1.5 to +2.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.81 | +78.3% (+75.1 to +81.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.5% (-9.1 to -1.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 32, 34, 39; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1649 / 6.9 / 20.0 / 20.0; omni 1650 / 7.5 / 18.4 / 18.6
- rep 2 (omni then native): native 1650 / 8.2 / 20.0 / 20.0; omni 1617 / 14.3 / 18.5 / 19.1
- rep 3 (native then omni): native 1636 / 7.9 / 20.0 / 20.0; omni 1651 / 6.5 / 18.8 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
