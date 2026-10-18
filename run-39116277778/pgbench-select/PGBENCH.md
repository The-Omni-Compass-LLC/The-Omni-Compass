# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 42,016 tps; base rate 6,302 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 18,430 | 18,463 | +0.2% (-0.6 to +0.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 18,482 | 18,483 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.46 | 4.81 | -25.5% (-145.1 to +94.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 25.4 | 18.6 | -26.7% (-127.0 to +73.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.205 | 0.205 | +0.2% (-4.9 to +5.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.04 | -21.6% (-103.5 to +60.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.7 | -9.9% (-17.3 to -2.6) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.462 | 0.463 | +0.2% (-2.0 to +2.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 800.6 | 802.1 | +0.2% (-2.1 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0965 | 0.0965 | +0.0% (-2.7 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 4.31 | 4.9 | +13.6% (+9.9 to +17.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.2% (-15.9 to -2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 33, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 18326 / 9.8 / 20.0 / 20.0; omni 18423 / 5.2 / 17.4 / 17.5
- rep 2 (omni then native): native 18483 / 4.7 / 19.1 / 20.0; omni 18476 / 6.3 / 17.6 / 18.4
- rep 3 (native then omni): native 18480 / 4.8 / 20.0 / 20.0; omni 18490 / 2.9 / 18.2 / 18.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
