# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,884 tps; base rate 583 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,680 | 1,675 | -0.3% (-1.2 to +0.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,710 | 1,705 | -0.3% (-0.6 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.54 | 6.29 | -3.9% (-29.0 to +21.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 129.2 | 137.1 | +6.1% (-66.0 to +78.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.54 | 1.53 | -0.5% (-2.9 to +1.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.84 | 4.85 | +0.3% (-35.7 to +36.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.1 | -3.9% (-5.7 to -2.0) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.347 | 0.345 | -0.4% (-3.0 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 522.8 | 520.5 | -0.4% (-3.3 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.691 | 0.691 | -0.1% (-3.4 to +3.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.5 | 3.32 | +32.6% (+32.0 to +33.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -3.0% (-5.5 to -0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 33, 34; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1688 / 6.6 / 20.0 / 20.0; omni 1677 / 6.0 / 19.4 / 19.6
- rep 2 (omni then native): native 1676 / 6.7 / 19.7 / 20.0; omni 1676 / 6.0 / 18.9 / 19.2
- rep 3 (native then omni): native 1676 / 6.3 / 20.0 / 20.0; omni 1671 / 6.8 / 19.1 / 19.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
