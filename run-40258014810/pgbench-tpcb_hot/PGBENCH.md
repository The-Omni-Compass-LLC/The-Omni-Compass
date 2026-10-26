# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,219 tps; base rate 483 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,317 | 1,325 | +0.6% (-22.9 to +24.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,415 | 1,404 | -0.8% (-3.8 to +2.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 242.4 | 86.6 | -64.3% (-455.5 to +327.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,180 | 407.7 | -65.5% (-404.4 to +273.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.847 | 0.845 | -0.2% (-10.8 to +10.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 50.3 | 28.5 | -43.3% (-452.6 to +366.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.6 | -1.7% (-3.9 to +0.6) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.2% (-10.0 to +7.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 373.2 | 368.9 | -1.1% (-10.1 to +7.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.63 | 0.62 | -1.6% (-32.0 to +28.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.18 | 1.63 | +38.1% (+26.1 to +50.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.3% (-2.2 to -0.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 23, 31; fail-ups per arm: 3, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1300 / 525.1 / 20.0 / 20.0; omni 1359 / 8.9 / 19.5 / 19.7
- rep 2 (omni then native): native 1382 / 2.3 / 19.8 / 20.0; omni 1248 / 246.4 / 19.6 / 19.8
- rep 3 (native then omni): native 1269 / 199.7 / 20.0 / 20.0; omni 1368 / 4.4 / 19.7 / 19.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
