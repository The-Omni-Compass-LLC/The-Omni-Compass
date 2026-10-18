# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,926 tps; base rate 439 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `bf26c1cebd84`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,271 | 1,251 | -1.6% (-5.4 to +2.2) | no difference beyond the noise |
| throughput (transactions a second) | 1,285 | 1,283 | -0.1% (-1.6 to +1.3) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.07 | 10.5 | +409.2% (-659.7 to +1478.1) | no difference beyond the noise |
| latency, 99th percentile (ms) | 60.7 | 203.9 | +235.9% (-209.3 to +681.0) | no difference beyond the noise |
| latency, median (ms) | 0.816 | 0.847 | +3.8% (+0.1 to +7.5) | **WORSE** |
| latency, mean (ms) | 2.87 | 9.71 | +238.4% (-346.4 to +823.1) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.9 | 6.12 | -69.3% (-98.4 to -40.2) | better |
| server connections alive, most at once | 20.0 | 23.7 | +18.3% (+11.2 to +25.5) | **WORSE** |
| host CPU busy (share of the run) | 0.204 | 0.234 | +14.6% (+8.3 to +20.9) | **WORSE** |
| host CPU-seconds | 235.6 | 270.0 | +14.6% (+8.0 to +21.2) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.618 | 0.72 | +16.5% (+5.2 to +27.9) | **WORSE** |
| pool size, mean (the knob) | 20.0 | 6.24 | -68.8% (-96.6 to -41.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 113, 151, 48; fail-ups per arm: 6, 7, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1275 / 2.0 / 20.0 / 20.0; omni 1257 / 6.2 / 5.5 / 5.8
- rep 2 (omni then native): native 1267 / 2.1 / 19.8 / 20.0; omni 1226 / 20.8 / 8.6 / 8.7
- rep 3 (native then omni): native 1272 / 2.1 / 20.0 / 20.0; omni 1270 / 4.6 / 4.3 / 4.3


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. Nothing here is set in stone. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
