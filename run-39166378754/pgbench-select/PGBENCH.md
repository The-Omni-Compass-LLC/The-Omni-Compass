# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,503 tps; base rate 2,475 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,261 | 7,259 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,261 | 7,259 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.18 | 1.14 | -3.4% (-22.5 to +15.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.51 | 3.14 | -10.7% (-62.6 to +41.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.361 | 0.361 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| latency, mean (ms) | 0.524 | 0.511 | -2.6% (-17.3 to +12.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.1% (-10.3 to -3.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.312 | 0.312 | +0.1% (-0.5 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 458.4 | 458.9 | +0.1% (-0.9 to +1.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.14 | +0.1% (-0.9 to +1.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.27 | +26.7% (+19.5 to +33.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.4% (-6.1 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 11, 20; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7261 / 1.3 / 20.0 / 20.0; omni 7259 / 1.2 / 18.5 / 18.9
- rep 2 (omni then native): native 7261 / 1.2 / 18.4 / 20.0; omni 7261 / 1.1 / 17.3 / 18.9
- rep 3 (native then omni): native 7261 / 1.1 / 20.0 / 20.0; omni 7258 / 1.1 / 18.4 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
