# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,876 tps; base rate 281 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `b525b7a07a0c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 825.5 | 824.5 | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 825.5 | 824.5 | -0.1% (-0.6 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.66 | 4.74 | +1.6% (-11.6 to +14.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.59 | 9.81 | +2.3% (-26.6 to +31.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.92 | 1.92 | +0.5% (-1.4 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.4 | 2.42 | +1.0% (-6.7 to +8.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.4 | -6.8% (-10.9 to -2.7) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.233 | 0.235 | +0.8% (-2.1 to +3.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 364.4 | 367.7 | +0.9% (-2.2 to +3.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.981 | 0.991 | +1.0% (-2.3 to +4.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.757 | 1.48 | +94.9% (+88.3 to +101.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.3% (-5.4 to -5.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 24, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 825 / 4.9 / 20.0 / 20.0; omni 826 / 4.7 / 18.4 / 18.9
- rep 2 (omni then native): native 826 / 4.5 / 19.2 / 20.0; omni 825 / 4.7 / 18.2 / 18.9
- rep 3 (native then omni): native 825 / 4.6 / 20.0 / 20.0; omni 823 / 4.8 / 18.5 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
