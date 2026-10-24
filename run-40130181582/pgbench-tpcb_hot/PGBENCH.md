# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,907 tps; base rate 286 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `791ad0fd93b1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 838.0 | 838.6 | +0.1% (-0.5 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 838.0 | 838.6 | +0.1% (-0.5 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.81 | 4.89 | +1.8% (-7.6 to +11.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.33 | 9.92 | +6.3% (-10.4 to +23.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.88 | 1.86 | -1.0% (-5.7 to +3.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.38 | 2.39 | +0.1% (-4.4 to +4.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 18.4 | -6.4% (-12.5 to -0.2) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.228 | 0.226 | -1.0% (-7.7 to +5.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 355.4 | 351.7 | -1.0% (-7.7 to +5.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.942 | 0.932 | -1.1% (-7.2 to +5.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.751 | 1.45 | +92.9% (+88.4 to +97.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.5% (-6.0 to -4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 24, 11, 20; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 839 / 5.0 / 20.0 / 20.0; omni 839 / 5.2 / 18.5 / 18.9
- rep 2 (omni then native): native 836 / 4.7 / 18.8 / 20.0; omni 838 / 4.7 / 18.1 / 18.9
- rep 3 (native then omni): native 840 / 4.8 / 20.0 / 20.0; omni 838 / 4.7 / 18.5 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
