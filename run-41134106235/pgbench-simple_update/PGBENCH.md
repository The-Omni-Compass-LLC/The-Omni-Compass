# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,857 tps; base rate 729 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f8335c835a67`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,104 | 2,081 | -1.1% (-2.8 to +0.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,136 | 2,138 | +0.1% (-0.3 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6 | 13.4 | +123.9% (-108.3 to +356.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 99.4 | 165.9 | +67.0% (-18.8 to +152.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.27 | 1.3 | +2.3% (-2.7 to +7.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4 | 6.25 | +56.5% (-16.3 to +129.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 24.7 | +23.4% (+16.5 to +30.4) | power given |
| server connections alive, most at once | 20.0 | 35.3 | +76.7% (+50.8 to +102.5) | power given |
| host CPU busy (share of the run) | 0.449 | 0.455 | +1.3% (-1.3 to +3.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 776.9 | 787.9 | +1.4% (-1.3 to +4.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.82 | 0.841 | +2.6% (-1.0 to +6.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.9 | 3.75 | +29.5% (+24.7 to +34.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 24.8 | +23.8% (+15.9 to +31.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 32, 37, 39; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2115 / 6.4 / 20.0 / 20.0; omni 2081 / 11.5 / 24.0 / 24.0
- rep 2 (omni then native): native 2091 / 5.9 / 20.0 / 20.0; omni 2063 / 19.7 / 25.0 / 25.2
- rep 3 (native then omni): native 2107 / 5.8 / 20.0 / 20.0; omni 2100 / 9.1 / 25.0 / 25.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
