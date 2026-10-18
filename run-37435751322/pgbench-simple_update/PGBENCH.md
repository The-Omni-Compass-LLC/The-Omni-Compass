# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,711 tps; base rate 557 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,591 | 1,506 | -5.4% (-13.0 to +2.3) | no difference beyond the noise |
| throughput (transactions a second) | 1,631 | 1,633 | +0.1% (-0.9 to +1.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 12.7 | 93.1 | +634.5% (-523.6 to +1792.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 150.7 | 246.3 | +63.4% (-126.0 to +252.9) | no difference beyond the noise |
| latency, median (ms) | 1.55 | 1.88 | +20.7% (+16.8 to +24.6) | **WORSE** |
| latency, mean (ms) | 6.52 | 16.0 | +144.9% (-93.8 to +383.6) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.5 | 12.6 | -35.1% (-55.1 to -15.2) | better |
| server connections alive, most at once | 20.0 | 33.7 | +68.3% (+61.2 to +75.5) | **WORSE** |
| host CPU busy (share of the run) | 0.361 | 0.449 | +24.6% (+22.2 to +27.0) | **WORSE** |
| host CPU-seconds | 366.0 | 468.4 | +28.0% (+24.9 to +31.1) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.767 | 1.04 | +35.4% (+20.4 to +50.4) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 12.6 | -36.8% (-53.3 to -20.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 156, 157, 175; fail-ups per arm: 4, 4, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1611 / 8.3 / 20.0 / 20.0; omni 1536 / 61.0 / 11.4 / 11.4
- rep 2 (omni then native): native 1584 / 15.2 / 18.5 / 20.0; omni 1541 / 55.5 / 12.2 / 12.4
- rep 3 (native then omni): native 1579 / 14.5 / 20.0 / 20.0; omni 1440 / 162.7 / 14.4 / 14.1


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
