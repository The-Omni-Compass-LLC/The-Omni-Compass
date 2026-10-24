# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,293 tps; base rate 344 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `f22776e60a87`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,007 | 1,007 | -0.0% (-1.8 to +1.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,010 | 1,008 | -0.2% (-0.5 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.96 | 2.84 | -4.1% (-27.8 to +19.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.7 | 5.52 | -70.5% (-394.9 to +253.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.35 | 1.34 | -1.0% (-4.7 to +2.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.99 | 1.74 | -12.6% (-103.9 to +78.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.4 | -12.0% (-25.1 to +1.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.239 | 0.237 | -0.9% (-5.2 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 419.2 | 415.4 | -0.9% (-5.0 to +3.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.925 | 0.917 | -0.9% (-3.3 to +1.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.629 | 1.17 | +85.8% (+83.2 to +88.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -10.9% (-26.3 to +4.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 21, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1000 / 3.2 / 20.0 / 20.0; omni 1007 / 2.8 / 18.8 / 19.3
- rep 2 (omni then native): native 1010 / 2.9 / 19.2 / 20.0; omni 1004 / 2.9 / 16.4 / 17.0
- rep 3 (native then omni): native 1011 / 2.8 / 20.0 / 20.0; omni 1008 / 2.9 / 16.9 / 17.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
