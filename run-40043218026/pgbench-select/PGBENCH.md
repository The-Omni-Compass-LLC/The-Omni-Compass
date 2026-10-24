# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,287 tps; base rate 2,443 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,161 | 7,166 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,161 | 7,166 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.26 | 1.29 | +2.3% (-2.9 to +7.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.79 | 4.01 | +5.8% (-12.6 to +24.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.368 | 0.368 | +0.0% (-0.7 to +0.7) | EVEN, the same |
| latency, mean (ms) | 0.547 | 0.582 | +6.3% (-4.8 to +17.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.2 | 15.0 | -21.9% (-34.5 to -9.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.317 | +0.2% (-0.5 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 466.0 | 467.1 | +0.2% (-0.8 to +1.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.145 | +0.2% (-1.0 to +1.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.56 | 3.34 | +30.6% (+22.1 to +39.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 15.7 | -21.3% (-28.4 to -14.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 32, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7159 / 1.3 / 20.0 / 20.0; omni 7166 / 1.3 / 15.8 / 16.1
- rep 2 (omni then native): native 7163 / 1.2 / 17.7 / 20.0; omni 7158 / 1.3 / 14.5 / 16.1
- rep 3 (native then omni): native 7162 / 1.3 / 20.0 / 20.0; omni 7173 / 1.3 / 14.8 / 15.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
