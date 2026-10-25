# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,353 tps; base rate 2,453 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,190 | 7,176 | -0.2% (-1.0 to +0.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,190 | 7,197 | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.01 | 1.37 | -31.9% (-127.8 to +63.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.28 | 11.7 | +121.6% (-418.0 to +661.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.381 | 0.373 | -2.0% (-8.0 to +4.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.651 | 0.843 | +29.4% (-69.0 to +127.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 14.7 | -24.9% (-35.0 to -14.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.336 | 0.326 | -2.8% (-11.2 to +5.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 498.9 | 482.8 | -3.2% (-12.8 to +6.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.154 | 0.15 | -3.0% (-12.5 to +6.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.71 | 3.52 | +29.9% (+26.9 to +32.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 15.6 | -22.1% (-37.9 to -6.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 34, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7193 / 1.2 / 20.0 / 20.0; omni 7183 / 1.3 / 14.7 / 14.9
- rep 2 (omni then native): native 7192 / 1.9 / 18.6 / 20.0; omni 7199 / 1.3 / 14.6 / 17.0
- rep 3 (native then omni): native 7186 / 3.0 / 20.0 / 20.0; omni 7147 / 1.5 / 14.7 / 14.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
