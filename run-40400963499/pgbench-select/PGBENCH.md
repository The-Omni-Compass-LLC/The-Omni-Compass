# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,753 tps; base rate 2,513 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5e222aa21371`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,371 | 7,368 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,371 | 7,368 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.73 | 1.5 | -13.2% (-72.7 to +46.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.08 | 4.48 | -11.9% (-59.1 to +35.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.371 | 0.371 | +0.1% (-0.3 to +0.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.622 | 0.593 | -4.8% (-21.7 to +12.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.3 | -6.0% (-11.0 to -1.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.325 | 0.326 | +0.4% (-0.7 to +1.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 323.4 | 324.8 | +0.4% (-0.9 to +1.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.147 | +0.5% (-0.7 to +1.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 5.57 | 6.09 | +9.4% (+5.7 to +13.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.7% (-6.0 to -5.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 8, 8, 8; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7374 / 2.2 / 20.0 / 20.0; omni 7367 / 1.5 / 18.6 / 18.9
- rep 2 (omni then native): native 7369 / 1.5 / 18.5 / 20.0; omni 7366 / 1.5 / 17.7 / 18.9
- rep 3 (native then omni): native 7369 / 1.5 / 20.0 / 20.0; omni 7370 / 1.5 / 18.6 / 18.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
