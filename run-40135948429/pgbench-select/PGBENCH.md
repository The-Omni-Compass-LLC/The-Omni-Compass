# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,879 tps; base rate 2,532 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,422 | 7,355 | -0.9% (-4.7 to +2.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,422 | 7,424 | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.85 | 2.45 | +32.1% (-68.1 to +132.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.4 | 52.3 | +868.9% (-2847.1 to +4585.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.378 | 0.376 | -0.4% (-2.7 to +1.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.646 | 1.88 | +190.6% (-610.3 to +991.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.2 | 15.6 | -18.8% (-36.8 to -0.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.339 | 0.337 | -0.5% (-3.9 to +3.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 501.4 | 498.7 | -0.5% (-4.4 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.151 | +0.4% (-2.0 to +2.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.69 | 3.43 | +27.3% (+18.4 to +36.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.2 | -18.8% (-30.8 to -6.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 22, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7422 / 2.2 / 20.0 / 20.0; omni 7224 / 3.7 / 16.4 / 16.6
- rep 2 (omni then native): native 7417 / 1.7 / 17.7 / 20.0; omni 7422 / 2.0 / 15.5 / 16.9
- rep 3 (native then omni): native 7427 / 1.6 / 20.0 / 20.0; omni 7418 / 1.7 / 15.0 / 15.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
