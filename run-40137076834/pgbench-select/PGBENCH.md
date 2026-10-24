# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,623 tps; base rate 2,493 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,315 | 7,292 | -0.3% (-0.8 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,315 | 7,310 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.6 | 2.1 | +31.3% (-142.9 to +205.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.88 | 9.79 | +100.7% (-295.6 to +497.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.374 | 0.376 | +0.7% (-2.4 to +3.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.612 | 0.925 | +51.2% (-84.2 to +186.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 16.8 | -13.4% (-28.0 to +1.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.329 | 0.332 | +0.9% (-3.0 to +4.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 486.0 | 491.4 | +1.1% (-3.4 to +5.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.148 | 0.15 | +1.4% (-3.2 to +6.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.42 | +32.2% (+27.6 to +36.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.3 | -13.5% (-22.1 to -4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 41, 29, 54; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7315 / 1.8 / 20.0 / 20.0; omni 7310 / 1.5 / 17.4 / 17.7
- rep 2 (omni then native): native 7310 / 1.6 / 18.4 / 20.0; omni 7277 / 1.7 / 16.9 / 17.7
- rep 3 (native then omni): native 7319 / 1.4 / 20.0 / 20.0; omni 7290 / 3.2 / 16.2 / 16.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
