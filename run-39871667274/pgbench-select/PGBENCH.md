# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,404 tps; base rate 2,461 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,218 | 7,165 | -0.7% (-3.7 to +2.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,218 | 7,215 | -0.0% (-0.1 to -0.0) | LOSS |
| latency, 95th percentile (ms, lag included) | 1.44 | 1.34 | -7.2% (-54.3 to +39.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.1 | 43.7 | +965.7% (-3170.9 to +5102.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.371 | 0.367 | -1.1% (-8.3 to +6.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.578 | 1.45 | +150.5% (-472.9 to +774.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.3 | 15.5 | -20.0% (-34.4 to -5.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.322 | 0.317 | -1.7% (-12.4 to +8.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 475.3 | 465.8 | -2.0% (-14.0 to +10.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.144 | -1.3% (-12.9 to +10.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.36 | +28.6% (+15.9 to +41.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.5 | -17.7% (-29.7 to -5.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 32, 32, 33; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7217 / 1.7 / 20.0 / 20.0; omni 7064 / 1.6 / 14.9 / 15.4
- rep 2 (omni then native): native 7217 / 1.6 / 18.0 / 20.0; omni 7215 / 1.2 / 14.3 / 16.6
- rep 3 (native then omni): native 7219 / 1.1 / 20.0 / 20.0; omni 7216 / 1.2 / 17.2 / 17.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
