# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,882 tps; base rate 432 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,267 | 1,267 | +0.0% (-0.6 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,267 | 1,268 | +0.1% (-0.4 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.31 | 3.52 | +6.1% (-9.9 to +22.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.37 | 9.58 | +30.0% (-53.8 to +113.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.28 | 1.29 | +0.8% (+0.4 to +1.2) | LOSS |
| latency, mean (ms) | 1.65 | 1.79 | +8.5% (-12.0 to +29.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 17.5 | -10.6% (-20.2 to -0.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.307 | 0.31 | +0.8% (+0.4 to +1.2) | power given |
| host CPU-seconds | 535.5 | 539.8 | +0.8% (+0.4 to +1.2) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.939 | 0.946 | +0.8% (-0.1 to +1.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.734 | 1.29 | +75.1% (+70.5 to +79.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.9 | -10.5% (-27.7 to +6.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 25, 26; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1266 / 3.5 / 20.0 / 20.0; omni 1270 / 3.5 / 18.3 / 18.6
- rep 2 (omni then native): native 1267 / 3.3 / 18.6 / 20.0; omni 1265 / 3.5 / 15.7 / 16.3
- rep 3 (native then omni): native 1268 / 3.2 / 20.0 / 20.0; omni 1267 / 3.6 / 18.5 / 18.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
