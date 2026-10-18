# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,572 tps; base rate 2,486 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,283 | 7,285 | +0.0% (-0.2 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 7,283 | 7,285 | +0.0% (-0.2 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.18 | 1.31 | +10.9% (-3.1 to +25.0) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.1 | 3.95 | +27.3% (+7.4 to +47.2) | **WORSE** |
| latency, median (ms) | 0.365 | 0.367 | +0.4% (-1.1 to +1.8) | no difference beyond the noise |
| latency, mean (ms) | 0.517 | 0.557 | +7.8% (+6.2 to +9.3) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.7 | 18.5 | -6.4% (-10.9 to -2.0) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.318 | 0.321 | +1.0% (-1.2 to +3.2) | no difference beyond the noise |
| host CPU-seconds | 310.8 | 314.7 | +1.2% (-1.3 to +3.8) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.142 | 0.144 | +1.2% (-1.2 to +3.6) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.62 | 2.13 | +32.1% (+27.8 to +36.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-5.1 to -4.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 17, 15; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7283 / 1.1 / 20.0 / 20.0; omni 7286 / 1.3 / 18.7 / 19.0
- rep 2 (omni then native): native 7284 / 1.2 / 19.2 / 20.0; omni 7279 / 1.4 / 18.3 / 19.0
- rep 3 (native then omni): native 7283 / 1.2 / 20.0 / 20.0; omni 7291 / 1.2 / 18.4 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
