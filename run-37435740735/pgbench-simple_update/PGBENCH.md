# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,446 tps; base rate 667 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 997.4 | 1,252 | +25.6% (-78.9 to +130.0) | no difference beyond the noise |
| throughput (transactions a second) | 1,858 | 1,907 | +2.6% (-5.2 to +10.4) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3,122 | 1,249 | -60.0% (-139.7 to +19.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 5,405 | 2,292 | -57.6% (-154.3 to +39.1) | no difference beyond the noise |
| latency, median (ms) | 36.4 | 18.4 | -49.4% (-439.6 to +340.9) | no difference beyond the noise |
| latency, mean (ms) | 564.7 | 246.2 | -56.4% (-189.0 to +76.2) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 22.4 | +12.2% (+9.0 to +15.4) | **WORSE** |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+67.6 to +92.4) | **WORSE** |
| host CPU busy (share of the run) | 0.307 | 0.365 | +18.7% (+10.9 to +26.5) | **WORSE** |
| host CPU-seconds | 360.6 | 425.7 | +18.0% (+11.6 to +24.5) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 1.22 | 1.18 | -3.3% (-92.2 to +85.6) | no difference beyond the noise |
| pool size, mean (the knob) | 20.0 | 21.4 | +7.1% (+1.0 to +13.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 189, 183, 207; fail-ups per arm: 26, 20, 18.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1132 / 3123.9 / 20.0 / 20.0; omni 910 / 2305.3 / 22.6 / 20.9
- rep 2 (omni then native): native 977 / 2815.5 / 20.0 / 20.0; omni 1395 / 826.4 / 22.5 / 21.7
- rep 3 (native then omni): native 883 / 3427.6 / 20.0 / 20.0; omni 1452 / 614.9 / 22.1 / 21.7


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
