# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 38,530 tps; base rate 5,780 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `a9694fbc7d2a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,948 | 16,947 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 16,949 | 16,953 | +0.0% (-0.0 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.415 | 0.338 | -18.6% (-48.9 to +11.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.88 | 2.13 | -56.3% (-223.4 to +110.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.158 | 0.154 | -2.7% (-4.6 to -0.9) | GAIN |
| latency, mean (ms) | 0.32 | 0.273 | -14.8% (-24.8 to -4.8) | GAIN |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.2 | -13.0% (-29.2 to +3.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.372 | 0.362 | -2.6% (-4.7 to -0.5) | GAIN |
| host CPU-seconds | 631.3 | 615.3 | -2.5% (-4.8 to -0.2) | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.0828 | 0.0807 | -2.5% (-4.7 to -0.3) | GAIN |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.07 | 3.47 | +13.3% (+9.6 to +16.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.5% (-27.6 to +4.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 37, 35; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16945 / 0.4 / 20.0 / 20.0; omni 16946 / 0.3 / 18.0 / 18.3
- rep 2 (omni then native): native 16948 / 0.5 / 19.4 / 20.0; omni 16935 / 0.4 / 17.7 / 18.6
- rep 3 (native then omni): native 16952 / 0.3 / 20.0 / 20.0; omni 16959 / 0.3 / 15.9 / 16.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
