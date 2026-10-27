# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,754 tps; base rate 563 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,611 | 1,608 | -0.2% (-0.9 to +0.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,651 | 1,650 | -0.1% (-0.5 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.01 | 7.28 | +3.9% (-5.5 to +13.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 182.9 | 180.2 | -1.5% (-18.7 to +15.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.58 | 1.58 | +0.1% (-2.1 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.23 | 6.21 | -0.2% (-23.4 to +23.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.2% (-2.0 to -0.4) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.344 | 0.343 | -0.2% (-0.6 to +0.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 347.2 | 346.4 | -0.2% (-0.7 to +0.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.718 | 0.718 | -0.0% (-1.2 to +1.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.56 | 2.1 | +34.3% (+32.9 to +35.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.3% (-0.6 to +0.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 17, 12; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1613 / 7.1 / 20.0 / 20.0; omni 1614 / 7.4 / 19.8 / 20.0
- rep 2 (omni then native): native 1608 / 6.9 / 19.9 / 20.0; omni 1606 / 6.9 / 19.6 / 20.0
- rep 3 (native then omni): native 1613 / 7.0 / 20.0 / 20.0; omni 1605 / 7.5 / 19.8 / 19.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
