# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,301 tps; base rate 495 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,427 | 1,449 | +1.5% (-4.4 to +7.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,451 | 1,451 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.73 | 1.75 | -74.0% (-388.8 to +240.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 105.9 | 5.39 | -94.9% (-467.4 to +277.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.825 | 0.834 | +1.1% (+0.3 to +1.9) | LOSS |
| latency, mean (ms) | 4.31 | 1.16 | -73.1% (-363.7 to +217.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.4 | -7.7% (-11.6 to -3.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.216 | 0.218 | +1.0% (+0.0 to +2.0) | power given |
| host CPU-seconds | 372.7 | 376.1 | +0.9% (+0.0 to +1.8) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.581 | 0.577 | -0.7% (-5.9 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.577 | 1.1 | +90.6% (+81.3 to +99.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -7.2% (-13.0 to -1.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 38, 43; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1445 / 1.9 / 20.0 / 20.0; omni 1449 / 1.7 / 18.8 / 19.1
- rep 2 (omni then native): native 1388 / 16.6 / 19.7 / 20.0; omni 1449 / 1.8 / 18.0 / 18.2
- rep 3 (native then omni): native 1448 / 1.7 / 20.0 / 20.0; omni 1449 / 1.8 / 18.3 / 18.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
