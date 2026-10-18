# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,293 tps; base rate 2,444 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,164 | 6,711 | -6.3% (-22.5 to +9.8) | no difference beyond the noise |
| throughput (transactions a second) | 7,165 | 7,161 | -0.1% (-0.3 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.5 | 123.6 | +3429.2% (-7499.6 to +14357.9) | no difference beyond the noise |
| latency, 99th percentile (ms) | 16.6 | 195.2 | +1077.8% (-1464.1 to +3619.7) | no difference beyond the noise |
| latency, median (ms) | 0.383 | 0.457 | +19.1% (+17.0 to +21.2) | **WORSE** |
| latency, mean (ms) | 1.04 | 16.4 | +1479.5% (-2981.3 to +5940.4) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.1 | 7.18 | -62.3% (-78.3 to -46.3) | better |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-22.0 to +35.4) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.358 | 0.44 | +22.9% (+19.1 to +26.6) | **WORSE** |
| host CPU-seconds | 356.9 | 450.7 | +26.3% (+21.6 to +30.9) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.166 | 0.225 | +35.3% (+11.3 to +59.2) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 7.24 | -63.8% (-69.7 to -58.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 113, 79, 91; fail-ups per arm: 1, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7167 / 4.0 / 20.0 / 20.0; omni 6814 / 48.7 / 7.8 / 7.8
- rep 2 (omni then native): native 7164 / 3.3 / 17.2 / 20.0; omni 7118 / 21.5 / 6.6 / 7.0
- rep 3 (native then omni): native 7162 / 3.2 / 20.0 / 20.0; omni 6202 / 300.5 / 7.1 / 7.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
