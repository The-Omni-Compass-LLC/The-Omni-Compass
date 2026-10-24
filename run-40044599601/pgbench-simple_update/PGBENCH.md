# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,315 tps; base rate 797 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,571 | 1,635 | +4.1% (-21.7 to +29.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,282 | 2,326 | +1.9% (-6.0 to +9.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,848 | 966.9 | -47.7% (-122.7 to +27.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,834 | 2,625 | -45.7% (-232.9 to +141.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.4 | 1.92 | +37.2% (-177.8 to +252.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 318.0 | 184.2 | -42.1% (-118.6 to +34.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.9 | +4.5% (-4.5 to +13.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.7 | +13.3% (-12.5 to +39.2) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.363 | 0.371 | +2.2% (-4.0 to +8.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 630.2 | 644.5 | +2.3% (-4.9 to +9.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.893 | 0.881 | -1.4% (-33.8 to +31.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.896 | 1.56 | +73.6% (+66.4 to +80.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.8 | +4.1% (-4.3 to +12.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 62, 35, 16; fail-ups per arm: 9, 9, 5.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1493 / 1835.8 / 20.0 / 20.0; omni 1637 / 917.8 / 20.7 / 20.6
- rep 2 (omni then native): native 1608 / 1135.5 / 20.0 / 20.0; omni 1780 / 829.6 / 21.7 / 21.6
- rep 3 (native then omni): native 1610 / 2574.1 / 20.0 / 20.0; omni 1487 / 1153.3 / 20.3 / 20.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
