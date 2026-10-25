# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,913 tps; base rate 587 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `96ebf29137fe`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,671 | 1,669 | -0.1% (-3.6 to +3.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,721 | 1,721 | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.92 | 8.96 | +13.0% (-103.3 to +129.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 198.7 | 224.9 | +13.2% (-49.9 to +76.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.52 | 1.52 | +0.2% (-1.0 to +1.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7 | 7.76 | +10.8% (-83.4 to +104.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.8 | -5.8% (-9.5 to -2.0) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.342 | 0.343 | +0.3% (+0.0 to +0.7) | power given |
| host CPU-seconds | 513.3 | 515.0 | +0.3% (-0.1 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.683 | 0.686 | +0.5% (-3.1 to +4.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1 | 1.78 | +77.0% (+73.8 to +80.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.6% (-7.5 to -1.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 46, 30, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1666 / 9.2 / 20.0 / 20.0; omni 1676 / 7.3 / 19.0 / 19.2
- rep 2 (omni then native): native 1679 / 7.3 / 19.9 / 20.0; omni 1650 / 12.5 / 18.4 / 18.8
- rep 3 (native then omni): native 1667 / 7.3 / 20.0 / 20.0; omni 1680 / 7.1 / 19.1 / 19.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
