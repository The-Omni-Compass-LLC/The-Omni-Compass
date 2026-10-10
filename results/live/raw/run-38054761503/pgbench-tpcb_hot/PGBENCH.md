# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,130 tps; base rate 470 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,371 | 1,375 | +0.3% (-1.3 to +1.9) | no difference beyond the noise |
| throughput (transactions a second) | 1,376 | 1,377 | +0.1% (-0.1 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.97 | 2.93 | -1.6% (-44.7 to +41.5) | no difference beyond the noise |
| latency, 99th percentile (ms) | 20.7 | 9.85 | -52.4% (-379.5 to +274.7) | no difference beyond the noise |
| latency, median (ms) | 1.18 | 1.18 | -0.3% (-2.1 to +1.5) | no difference beyond the noise |
| latency, mean (ms) | 1.83 | 1.65 | -9.6% (-102.2 to +83.1) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 17.8 | -11.0% (-22.0 to -0.0) | better |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.263 | 0.263 | +0.0% (-2.6 to +2.6) | no difference beyond the noise |
| host CPU-seconds | 456.9 | 457.2 | +0.1% (-2.5 to +2.6) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.74 | 0.739 | -0.2% (-4.3 to +3.9) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.663 | 1.18 | +77.2% (+73.0 to +81.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.5% (-19.7 to +2.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 57, 54, 40; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1362 / 3.4 / 20.0 / 20.0; omni 1376 / 2.8 / 16.9 / 17.3
- rep 2 (omni then native): native 1376 / 2.7 / 20.0 / 20.0; omni 1373 / 3.0 / 17.7 / 18.7
- rep 3 (native then omni): native 1376 / 2.8 / 20.0 / 20.0; omni 1377 / 3.0 / 18.7 / 19.0


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
