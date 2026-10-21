# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,643 tps; base rate 246 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 404.7 | 453.6 | +12.1% (-5.8 to +30.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 705.9 | 719.6 | +2.0% (-2.4 to +6.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,250 | 1,354 | -39.8% (-237.0 to +157.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,279 | 2,147 | -49.8% (-251.2 to +151.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 21.7 | 7.15 | -67.1% (-201.6 to +67.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 349.2 | 211.1 | -39.5% (-189.7 to +110.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.2% (-0.5 to +0.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.181 | 0.183 | +1.2% (-3.2 to +5.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 318.8 | 321.6 | +0.9% (-3.3 to +5.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.76 | 1.58 | -10.3% (-24.8 to +4.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.564 | 1.11 | +96.3% (+95.0 to +97.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-0.4 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 6, 6, 2; fail-ups per arm: 1, 2, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 406 / 3457.8 / 20.0 / 20.0; omni 474 / 500.8 / 20.0 / 20.0
- rep 2 (omni then native): native 370 / 1944.5 / 20.0 / 20.0; omni 434 / 2153.1 / 19.9 / 20.0
- rep 3 (native then omni): native 438 / 1348.2 / 20.0 / 20.0; omni 453 / 1408.3 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
