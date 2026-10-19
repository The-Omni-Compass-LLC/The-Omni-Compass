# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,586 tps; base rate 2,488 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,299 | 7,284 | -0.2% (-0.6 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,301 | 7,292 | -0.1% (-0.5 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.51 | 2.63 | +73.3% (-208.6 to +355.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.38 | 11.4 | +79.2% (-217.7 to +376.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.373 | 0.378 | +1.3% (-4.2 to +6.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.662 | 0.857 | +29.6% (-75.9 to +135.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.8 | -5.3% (-7.6 to -2.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.327 | 0.331 | +1.2% (-6.3 to +8.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 482.3 | 489.5 | +1.5% (-6.7 to +9.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.149 | +1.7% (-6.8 to +10.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.42 | +30.8% (+22.1 to +39.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-5.5 to -4.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 24, 37, 37; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7296 / 1.3 / 20.0 / 20.0; omni 7296 / 1.3 / 18.9 / 19.0
- rep 2 (omni then native): native 7291 / 1.9 / 19.7 / 20.0; omni 7270 / 5.0 / 18.8 / 19.0
- rep 3 (native then omni): native 7309 / 1.3 / 20.0 / 20.0; omni 7287 / 1.6 / 18.8 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
