# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,837 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `36cb1cc37947`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,642 | 1,636 | -0.4% (-4.9 to +4.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,687 | 1,688 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.21 | 19.8 | +140.8% (-493.8 to +775.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 205.8 | 196.1 | -4.7% (-123.9 to +114.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.55 | 1.55 | +0.2% (-3.2 to +3.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.86 | 7.88 | +14.8% (-126.3 to +155.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.4 | -2.8% (-3.7 to -1.9) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.344 | 0.346 | +0.5% (-3.1 to +4.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 519.0 | 522.3 | +0.6% (-3.6 to +4.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.702 | 0.71 | +1.0% (-7.1 to +9.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.82 | +79.7% (+71.1 to +88.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.4% (-3.0 to -1.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 44, 44, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1646 / 8.3 / 20.0 / 20.0; omni 1640 / 9.0 / 19.5 / 19.5
- rep 2 (omni then native): native 1642 / 7.7 / 20.0 / 20.0; omni 1606 / 43.4 / 19.3 / 19.5
- rep 3 (native then omni): native 1638 / 8.6 / 20.0 / 20.0; omni 1663 / 6.9 / 19.5 / 19.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
