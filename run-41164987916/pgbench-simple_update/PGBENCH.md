# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,010 tps; base rate 602 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,724 | 1,732 | +0.5% (-2.0 to +2.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,763 | 1,765 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.71 | 6.9 | +2.8% (-49.9 to +55.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 173.0 | 127.0 | -26.6% (-145.1 to +91.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.45 | 1.46 | +0.2% (-1.4 to +1.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.75 | 4.91 | -14.6% (-89.6 to +60.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 23.9 | +19.4% (+9.1 to +29.8) | power given |
| server connections alive, most at once | 20.0 | 35.3 | +76.7% (+40.8 to +112.5) | power given |
| host CPU busy (share of the run) | 0.421 | 0.422 | +0.3% (-0.3 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 720.6 | 722.8 | +0.3% (-0.2 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.929 | 0.927 | -0.1% (-2.2 to +1.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.52 | 3.3 | +31.4% (+27.6 to +35.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 24.0 | +20.2% (+11.1 to +29.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 38, 46; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1725 / 6.1 / 20.0 / 20.0; omni 1749 / 6.1 / 22.9 / 23.2
- rep 2 (omni then native): native 1722 / 7.8 / 20.0 / 20.0; omni 1732 / 6.7 / 24.4 / 24.4
- rep 3 (native then omni): native 1726 / 6.2 / 20.0 / 20.0; omni 1716 / 7.9 / 24.3 / 24.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
