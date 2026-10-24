# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,894 tps; base rate 584 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,673 | 1,670 | -0.1% (-1.3 to +1.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,714 | 1,711 | -0.2% (-1.0 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.99 | 7.13 | +2.0% (-5.2 to +9.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 178.4 | 182.1 | +2.1% (-57.0 to +61.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.48 | 1.48 | +0.0% (-2.7 to +2.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.05 | 6.13 | +1.3% (-56.4 to +59.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.6% (-5.1 to +1.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.342 | 0.343 | +0.1% (-2.2 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 513.5 | 514.6 | +0.2% (-2.4 to +2.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.682 | 0.685 | +0.4% (-1.6 to +2.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.78 | +72.7% (+69.9 to +75.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.7% (-4.2 to +2.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 25, 24; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1670 / 7.5 / 20.0 / 20.0; omni 1669 / 7.5 / 19.8 / 20.0
- rep 2 (omni then native): native 1675 / 7.0 / 20.0 / 20.0; omni 1664 / 7.3 / 19.3 / 19.5
- rep 3 (native then omni): native 1674 / 6.5 / 20.0 / 20.0; omni 1679 / 6.5 / 19.9 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
