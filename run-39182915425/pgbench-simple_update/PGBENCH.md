# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,847 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,641 | 1,637 | -0.2% (-6.1 to +5.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,692 | 1,691 | -0.1% (-0.7 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 13.9 | 18.5 | +33.0% (-427.7 to +493.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 197.9 | 216.3 | +9.3% (-109.8 to +128.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.58 | 1.58 | +0.4% (-4.0 to +4.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 7.46 | 8.12 | +8.8% (-169.0 to +186.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.5% (-6.7 to -0.2) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.349 | 0.351 | +0.4% (-3.9 to +4.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 526.7 | 529.3 | +0.5% (-4.4 to +5.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.713 | 0.719 | +0.7% (-8.6 to +10.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.82 | +77.3% (+76.5 to +78.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.4 | -2.8% (-6.6 to +0.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 33, 39, 35; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1653 / 8.0 / 20.0 / 20.0; omni 1650 / 8.0 / 19.5 / 19.7
- rep 2 (omni then native): native 1652 / 7.7 / 20.0 / 20.0; omni 1610 / 40.1 / 19.4 / 19.5
- rep 3 (native then omni): native 1617 / 25.9 / 20.0 / 20.0; omni 1652 / 7.4 / 19.0 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
