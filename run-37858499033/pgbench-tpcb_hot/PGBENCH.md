# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,851 tps; base rate 278 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 814.9 | 813.1 | -0.2% (-0.6 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 815.0 | 813.6 | -0.2% (-0.6 to +0.3) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.25 | 4.48 | +5.4% (-14.3 to +25.1) | no difference beyond the noise |
| latency, 99th percentile (ms) | 8.06 | 12.0 | +49.5% (+13.6 to +85.4) | **WORSE** |
| latency, median (ms) | 1.84 | 1.86 | +1.0% (-0.7 to +2.6) | no difference beyond the noise |
| latency, mean (ms) | 2.25 | 2.43 | +7.9% (+0.6 to +15.1) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.3 | 9.94 | -48.5% (-60.9 to -36.0) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.223 | 0.228 | +2.3% (-0.9 to +5.4) | no difference beyond the noise |
| host CPU-seconds | 232.8 | 238.3 | +2.4% (-0.9 to +5.6) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.952 | 0.977 | +2.6% (-0.4 to +5.6) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.505 | 1.3 | +157.6% (+148.4 to +166.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 11.4 | -42.9% (-48.3 to -37.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 200, 217, 207; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 816 / 4.8 / 20.0 / 20.0; omni 813 / 4.6 / 10.4 / 11.3
- rep 2 (omni then native): native 814 / 4.0 / 17.9 / 20.0; omni 813 / 4.4 / 9.6 / 11.9
- rep 3 (native then omni): native 815 / 4.0 / 20.0 / 20.0; omni 813 / 4.4 / 9.8 / 11.1


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
