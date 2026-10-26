# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 37,388 tps; base rate 5,608 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b11b4d3825b1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,450 | 16,452 | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 16,450 | 16,452 | +0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.791 | 0.505 | -36.2% (-232.2 to +159.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.2 | 3.77 | -27.5% (-224.2 to +169.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.163 | 0.162 | -0.6% (-3.7 to +2.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.363 | 0.321 | -11.7% (-116.2 to +92.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.3% (-15.4 to +6.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.374 | 0.373 | -0.5% (-3.9 to +3.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 648.5 | 645.6 | -0.5% (-4.2 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0876 | 0.0872 | -0.5% (-4.3 to +3.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 10.3 | 10.9 | +5.7% (+3.2 to +8.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.5% (-13.4 to +6.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 11, 10; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16455 / 1.5 / 20.0 / 20.0; omni 16458 / 0.5 / 18.1 / 18.4
- rep 2 (omni then native): native 16451 / 0.4 / 19.9 / 20.0; omni 16452 / 0.4 / 19.6 / 19.8
- rep 3 (native then omni): native 16445 / 0.5 / 20.0 / 20.0; omni 16445 / 0.6 / 19.7 / 19.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
