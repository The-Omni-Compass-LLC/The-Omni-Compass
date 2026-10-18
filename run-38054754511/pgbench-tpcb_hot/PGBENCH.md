# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,922 tps; base rate 288 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 845.0 | 845.9 | +0.1% (-0.5 to +0.7) | no difference beyond the noise |
| throughput (transactions a second) | 845.0 | 846.0 | +0.1% (-0.4 to +0.7) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.95 | 5.24 | +6.0% (-8.3 to +20.3) | no difference beyond the noise |
| latency, 99th percentile (ms) | 9.71 | 12.4 | +27.6% (-28.4 to +83.5) | no difference beyond the noise |
| latency, median (ms) | 1.87 | 1.87 | -0.1% (-0.7 to +0.6) | no difference beyond the noise |
| latency, mean (ms) | 2.39 | 2.49 | +4.2% (-5.4 to +13.9) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.5 | 16.9 | -13.4% (-26.9 to -0.0) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.231 | 0.231 | +0.2% (-1.0 to +1.3) | no difference beyond the noise |
| host CPU-seconds | 359.4 | 360.1 | +0.2% (-1.0 to +1.4) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.945 | 0.946 | +0.1% (-1.2 to +1.4) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.763 | 1.49 | +95.9% (+90.3 to +101.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.3 | -13.5% (-31.5 to +4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 21, 39, 31; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 844 / 4.9 / 20.0 / 20.0; omni 844 / 5.5 / 18.3 / 19.0
- rep 2 (omni then native): native 845 / 5.0 / 18.5 / 20.0; omni 848 / 5.0 / 16.1 / 16.5
- rep 3 (native then omni): native 846 / 4.9 / 20.0 / 20.0; omni 846 / 5.3 / 16.2 / 16.4


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
