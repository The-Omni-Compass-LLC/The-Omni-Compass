# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,284 tps; base rate 493 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,436 | 1,441 | +0.4% (-0.1 to +1.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,444 | 1,445 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.56 | 2.84 | -20.4% (-54.8 to +13.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 34.6 | 14.8 | -57.2% (-141.1 to +26.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.21 | 1.2 | -1.2% (-2.8 to +0.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.33 | 1.79 | -23.3% (-56.6 to +10.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.9 | -5.2% (-11.2 to +0.7) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.264 | 0.26 | -1.5% (-3.7 to +0.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 469.9 | 462.9 | -1.5% (-3.5 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.727 | 0.714 | -1.9% (-3.7 to -0.1) | GAIN |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.559 | 0.994 | +77.8% (+68.6 to +87.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.3% (-9.7 to +1.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 17, 46; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1431 / 4.0 / 20.0 / 20.0; omni 1440 / 2.7 / 18.7 / 18.9
- rep 2 (omni then native): native 1435 / 3.6 / 19.8 / 20.0; omni 1442 / 2.8 / 19.3 / 19.6
- rep 3 (native then omni): native 1441 / 3.2 / 20.0 / 20.0; omni 1443 / 2.9 / 18.7 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
