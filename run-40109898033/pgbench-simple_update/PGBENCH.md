# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,789 tps; base rate 568 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,627 | 1,634 | +0.5% (-1.1 to +2.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,668 | 1,667 | -0.1% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.94 | 6.49 | -6.4% (-45.8 to +33.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 176.4 | 157.1 | -10.9% (-83.1 to +61.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.51 | 1.5 | -0.6% (-1.6 to +0.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.09 | 5.42 | -11.0% (-65.9 to +43.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.9 | -5.3% (-17.6 to +7.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (-6.0 to +22.7) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.342 | 0.34 | -0.6% (-0.8 to -0.4) | GAIN |
| host CPU-seconds | 514.2 | 510.6 | -0.7% (-1.1 to -0.3) | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.702 | 0.694 | -1.2% (-3.1 to +0.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.8 | +77.9% (+74.6 to +81.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -4.1% (-16.9 to +8.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 36, 32, 28; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1627 / 7.0 / 20.0 / 20.0; omni 1631 / 6.7 / 18.0 / 18.2
- rep 2 (omni then native): native 1629 / 6.5 / 20.0 / 20.0; omni 1628 / 7.1 / 18.8 / 19.2
- rep 3 (native then omni): native 1624 / 7.3 / 20.0 / 20.0; omni 1644 / 5.7 / 20.0 / 20.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
