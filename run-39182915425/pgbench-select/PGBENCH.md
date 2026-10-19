# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,433 tps; base rate 3,965 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,537 | 11,625 | +0.8% (-2.6 to +4.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,625 | 11,625 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.99 | 2.83 | -29.0% (-258.1 to +200.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 59.8 | 7.7 | -87.1% (-478.8 to +304.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.255 | 0.254 | -0.4% (-3.8 to +3.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.89 | 0.644 | -66.0% (-375.3 to +243.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.3 | 15.8 | -18.3% (-30.4 to -6.1) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.439 | 0.437 | -0.3% (-3.5 to +2.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 753.3 | 751.2 | -0.3% (-4.1 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.144 | -1.0% (-7.9 to +5.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.96 | 3.63 | +22.5% (+11.9 to +33.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.4 | -18.0% (-23.8 to -12.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 38, 28; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11627 / 3.0 / 20.0 / 20.0; omni 11628 / 1.9 / 15.5 / 15.9
- rep 2 (omni then native): native 11358 / 6.9 / 18.0 / 20.0; omni 11625 / 2.1 / 15.4 / 16.6
- rep 3 (native then omni): native 11626 / 2.0 / 20.0 / 20.0; omni 11623 / 4.5 / 16.4 / 16.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
