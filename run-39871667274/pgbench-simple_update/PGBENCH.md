# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,838 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,643 | 1,644 | +0.0% (-4.7 to +4.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,688 | 1,688 | +0.0% (-0.5 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.64 | 7.95 | +4.0% (-88.3 to +96.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 202.3 | 208.7 | +3.2% (-123.2 to +129.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.51 | 1.52 | +0.5% (-1.6 to +2.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.85 | 7.18 | +4.7% (-137.7 to +147.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.4% (-9.8 to +1.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.343 | 0.344 | +0.5% (-1.6 to +2.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 515.1 | 518.3 | +0.6% (-2.0 to +3.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.697 | 0.701 | +0.6% (-6.5 to +7.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.81 | +77.7% (+72.6 to +82.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.6% (-9.3 to +2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 26, 33, 35; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1649 / 7.1 / 20.0 / 20.0; omni 1645 / 8.0 / 19.6 / 19.8
- rep 2 (omni then native): native 1652 / 6.7 / 20.0 / 20.0; omni 1624 / 9.6 / 18.8 / 19.0
- rep 3 (native then omni): native 1629 / 9.1 / 20.0 / 20.0; omni 1663 / 6.3 / 18.9 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
