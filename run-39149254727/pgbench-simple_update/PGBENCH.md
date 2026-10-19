# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,791 tps; base rate 569 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,625 | 1,624 | -0.1% (-3.6 to +3.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,667 | 1,668 | +0.0% (-0.6 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.29 | 10.5 | +43.8% (-185.5 to +273.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 180.6 | 173.4 | -4.0% (-112.8 to +104.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.53 | 1.53 | +0.0% (-1.7 to +1.7) | EVEN, the same |
| latency, mean (ms) | 6.36 | 6.63 | +4.2% (-102.5 to +110.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.7% (-6.2 to -1.1) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.341 | 0.342 | +0.1% (-2.0 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 513.6 | 514.2 | +0.1% (-2.3 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.702 | 0.704 | +0.2% (-5.0 to +5.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.02 | 1.81 | +77.4% (+75.3 to +79.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.5% (-6.1 to +1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 42, 23, 34; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1634 / 7.5 / 20.0 / 20.0; omni 1625 / 6.8 / 19.1 / 19.3
- rep 2 (omni then native): native 1621 / 7.0 / 20.0 / 20.0; omni 1601 / 17.9 / 19.5 / 19.8
- rep 3 (native then omni): native 1620 / 7.4 / 20.0 / 20.0; omni 1644 / 6.7 / 19.2 / 19.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
