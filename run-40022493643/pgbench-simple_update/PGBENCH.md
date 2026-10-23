# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,802 tps; base rate 570 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,626 | 1,632 | +0.4% (-2.8 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,674 | 1,672 | -0.1% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.08 | 8.32 | +2.9% (-58.5 to +64.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 206.5 | 183.4 | -11.2% (-84.1 to +61.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.53 | 1.57 | +2.4% (+0.5 to +4.3) | LOSS |
| latency, mean (ms) | 7.16 | 6.47 | -9.5% (-94.6 to +75.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -3.8% (-9.4 to +1.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.342 | 0.353 | +3.0% (+0.9 to +5.1) | power given |
| host CPU-seconds | 516.1 | 533.2 | +3.3% (+0.8 to +5.8) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.705 | 0.726 | +2.9% (+0.1 to +5.7) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.84 | +81.1% (+74.6 to +87.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.7% (-7.5 to +2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 30, 36, 41; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1629 / 9.0 / 20.0 / 20.0; omni 1633 / 8.4 / 19.7 / 19.9
- rep 2 (omni then native): native 1631 / 7.1 / 20.0 / 20.0; omni 1618 / 9.6 / 19.1 / 19.3
- rep 3 (native then omni): native 1618 / 8.1 / 20.0 / 20.0; omni 1646 / 6.9 / 18.9 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
