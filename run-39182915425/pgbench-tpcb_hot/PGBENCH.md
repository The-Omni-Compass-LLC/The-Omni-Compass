# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,914 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `bc2eb38f4ca8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 840.5 | 840.3 | -0.0% (-1.0 to +0.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 841.9 | 841.0 | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.02 | 5.63 | -6.5% (-94.9 to +82.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 18.4 | 15.3 | -16.8% (-219.5 to +185.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.93 | 1.94 | +0.8% (-6.0 to +7.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.78 | 2.72 | -2.3% (-50.1 to +45.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 17.5 | -9.9% (-14.4 to -5.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.239 | 0.241 | +0.9% (-7.2 to +9.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 372.8 | 376.5 | +1.0% (-7.6 to +9.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.986 | 0.996 | +1.0% (-8.5 to +10.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.772 | 1.51 | +96.1% (+85.6 to +106.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.1% (-19.3 to +1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 32, 26, 12; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 836 / 8.1 / 20.0 / 20.0; omni 840 / 5.3 / 17.7 / 18.2
- rep 2 (omni then native): native 843 / 4.9 / 18.3 / 20.0; omni 840 / 6.3 / 16.3 / 17.4
- rep 3 (native then omni): native 842 / 5.0 / 20.0 / 20.0; omni 841 / 5.2 / 18.5 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
