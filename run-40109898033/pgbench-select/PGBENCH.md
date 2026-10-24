# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,435 tps; base rate 2,465 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `00f7839c8b98`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,231 | 7,226 | -0.1% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,231 | 7,227 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.48 | 1.2 | -19.0% (-107.1 to +69.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.34 | 3.72 | -14.2% (-113.6 to +85.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.367 | 0.364 | -0.8% (-8.0 to +6.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.572 | 0.592 | +3.4% (-27.7 to +34.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 16.1 | -18.2% (-28.5 to -7.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.314 | -1.3% (-12.4 to +9.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 468.2 | 461.0 | -1.5% (-14.0 to +10.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.142 | -1.5% (-13.7 to +10.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.6 | 3.32 | +27.7% (+18.8 to +36.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.2 | -14.1% (-28.9 to +0.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 20, 24, 29; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7233 / 2.1 / 20.0 / 20.0; omni 7221 / 1.2 / 15.5 / 15.8
- rep 2 (omni then native): native 7228 / 1.2 / 19.0 / 20.0; omni 7230 / 1.2 / 15.6 / 18.1
- rep 3 (native then omni): native 7230 / 1.1 / 20.0 / 20.0; omni 7229 / 1.2 / 17.1 / 17.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
