# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 37,847 tps; base rate 5,677 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,652 | 16,571 | -0.5% (-1.4 to +0.4) | no difference beyond the noise |
| throughput (transactions a second) | 16,652 | 16,648 | -0.0% (-0.2 to +0.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.424 | 6.25 | +1374.5% (-341.7 to +3090.8) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.99 | 33.6 | +741.9% (-272.4 to +1756.3) | no difference beyond the noise |
| latency, median (ms) | 0.155 | 0.167 | +8.0% (+1.5 to +14.4) | **WORSE** |
| latency, mean (ms) | 0.29 | 1.41 | +384.2% (-100.7 to +869.1) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.6 | 7.27 | -63.0% (-66.5 to -59.4) | better |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-22.5 to +29.2) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.371 | 0.421 | +13.4% (+8.8 to +18.1) | **WORSE** |
| host CPU-seconds | 422.4 | 480.4 | +13.7% (+8.7 to +18.7) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.0846 | 0.0966 | +14.3% (+8.5 to +20.1) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 7.31 | -63.5% (-71.8 to -55.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 114, 97, 117; fail-ups per arm: 1, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16661 / 0.4 / 20.0 / 20.0; omni 16536 / 8.9 / 7.4 / 7.4
- rep 2 (omni then native): native 16644 / 0.4 / 18.9 / 20.0; omni 16633 / 3.1 / 6.4 / 6.6
- rep 3 (native then omni): native 16651 / 0.4 / 20.0 / 20.0; omni 16543 / 6.8 / 8.0 / 7.9


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
