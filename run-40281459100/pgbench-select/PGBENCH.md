# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,085 tps; base rate 2,413 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,073 | 7,080 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,073 | 7,080 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.17 | 1.23 | +5.1% (-9.5 to +19.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.22 | 3.39 | +5.4% (-53.7 to +64.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.366 | 0.369 | +0.8% (-0.4 to +2.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.518 | 0.534 | +3.0% (-10.7 to +16.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.5 | -7.2% (-9.4 to -5.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.312 | 0.316 | +1.3% (-0.8 to +3.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 467.4 | 474.1 | +1.4% (-0.9 to +3.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.149 | +1.3% (-1.2 to +3.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.2 | 9.02 | +10.0% (+6.5 to +13.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.2% (-6.1 to -4.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 16, 20, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7067 / 1.3 / 20.0 / 20.0; omni 7083 / 1.2 / 18.4 / 19.0
- rep 2 (omni then native): native 7073 / 1.1 / 19.7 / 20.0; omni 7080 / 1.2 / 18.4 / 19.1
- rep 3 (native then omni): native 7077 / 1.1 / 20.0 / 20.0; omni 7077 / 1.2 / 18.6 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
