# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,906 tps; base rate 286 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 839.4 | 838.3 | -0.1% (-0.8 to +0.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 839.8 | 839.0 | -0.1% (-0.5 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.29 | 5.94 | +12.2% (+9.5 to +14.9) | LOSS |
| latency, 99th percentile (ms) | 12.1 | 15.3 | +26.6% (-15.9 to +69.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.89 | 1.91 | +1.0% (-0.1 to +2.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.52 | 2.69 | +6.6% (-4.9 to +18.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.7 | -10.7% (-24.8 to +3.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.232 | 0.236 | +1.5% (+0.3 to +2.6) | power given |
| host CPU-seconds | 362.2 | 367.7 | +1.5% (+0.4 to +2.7) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.959 | 0.975 | +1.7% (+0.9 to +2.4) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.765 | 1.5 | +96.5% (+89.2 to +103.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.6% (-23.7 to +6.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 30, 31, 15; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 839 / 5.2 / 20.0 / 20.0; omni 838 / 5.8 / 17.2 / 17.5
- rep 2 (omni then native): native 838 / 5.1 / 19.5 / 20.0; omni 839 / 5.7 / 16.7 / 17.6
- rep 3 (native then omni): native 841 / 5.5 / 20.0 / 20.0; omni 838 / 6.2 / 19.2 / 19.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
