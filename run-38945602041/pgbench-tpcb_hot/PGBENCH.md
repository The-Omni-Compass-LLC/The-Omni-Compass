# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,921 tps; base rate 288 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 558.1 | 645.9 | +15.7% (-15.5 to +46.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 839.4 | 839.9 | +0.1% (-0.4 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 830.0 | 675.8 | -18.6% (-55.3 to +18.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,505 | 1,788 | +18.8% (-73.1 to +110.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 6.74 | 1.3 | -80.7% (-412.5 to +251.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 144.8 | 105.8 | -26.9% (-114.8 to +61.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.9 | -0.5% (-3.0 to +2.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.211 | 0.205 | -2.6% (-6.0 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 369.7 | 359.3 | -2.8% (-6.7 to +1.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.49 | 1.24 | -16.7% (-51.1 to +17.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.601 | 1.16 | +92.3% (+85.1 to +99.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.4% (-2.8 to +2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 12, 16, 4; fail-ups per arm: 3, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 486 / 1145.6 / 20.0 / 20.0; omni 635 / 883.5 / 20.0 / 20.0
- rep 2 (omni then native): native 577 / 636.5 / 20.0 / 20.0; omni 680 / 456.6 / 19.7 / 19.7
- rep 3 (native then omni): native 611 / 708.0 / 20.0 / 20.0; omni 623 / 687.3 / 20.1 / 20.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
