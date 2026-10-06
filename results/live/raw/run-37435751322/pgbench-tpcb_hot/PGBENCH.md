# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,907 tps; base rate 286 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 833.6 | 805.6 | -3.4% (-6.0 to -0.8) | **WORSE** |
| throughput (transactions a second) | 838.2 | 838.8 | +0.1% (-0.6 to +0.8) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.69 | 41.7 | +442.7% (+134.6 to +750.9) | **WORSE** |
| latency, 99th percentile (ms) | 43.5 | 106.5 | +145.1% (-73.8 to +364.0) | no difference beyond the noise |
| latency, median (ms) | 1.93 | 2.38 | +23.2% (+13.5 to +32.9) | **WORSE** |
| latency, mean (ms) | 3.56 | 8.59 | +141.6% (+41.0 to +242.3) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.2 | 5.46 | -71.5% (-86.3 to -56.8) | better |
| server connections alive, most at once | 20.0 | 23.0 | +15.0% (-17.9 to +47.9) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.263 | 0.327 | +24.2% (+20.6 to +27.9) | **WORSE** |
| host CPU-seconds | 275.8 | 345.1 | +25.1% (+21.5 to +28.7) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 1.1 | 1.43 | +29.5% (+22.3 to +36.7) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 5.53 | -72.4% (-77.2 to -67.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 66, 68, 68; fail-ups per arm: 4, 2, 4.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 828 / 9.8 / 20.0 / 20.0; omni 802 / 43.6 / 6.0 / 6.0
- rep 2 (omni then native): native 837 / 6.8 / 17.5 / 20.0; omni 817 / 31.4 / 5.0 / 5.4
- rep 3 (native then omni): native 835 / 6.5 / 20.0 / 20.0; omni 798 / 50.2 / 5.3 / 5.2


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
