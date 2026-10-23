# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,911 tps; base rate 2,537 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6fcdf41aad34`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,442 | 7,443 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,442 | 7,443 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.58 | 1.48 | -6.3% (-45.0 to +32.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.97 | 4.84 | -2.5% (-34.8 to +29.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.367 | 0.369 | +0.5% (-1.2 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.609 | 0.604 | -0.8% (-14.4 to +12.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.2 | -6.6% (-11.3 to -1.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.324 | 0.327 | +0.9% (-1.5 to +3.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 475.7 | 480.9 | +1.1% (-1.6 to +3.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.142 | 0.144 | +1.1% (-1.8 to +4.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.66 | 3.36 | +26.6% (+25.5 to +27.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.5% (-6.2 to -4.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 11, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7440 / 1.9 / 20.0 / 20.0; omni 7436 / 1.5 / 18.6 / 18.9
- rep 2 (omni then native): native 7444 / 1.5 / 18.4 / 20.0; omni 7448 / 1.5 / 17.5 / 18.9
- rep 3 (native then omni): native 7442 / 1.4 / 20.0 / 20.0; omni 7444 / 1.4 / 18.4 / 18.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
