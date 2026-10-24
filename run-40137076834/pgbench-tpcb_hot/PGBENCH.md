# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,832 tps; base rate 275 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 632.4 | 599.1 | -5.3% (-9.0 to -1.6) | LOSS |
| throughput (transactions a second) | 803.3 | 792.0 | -1.4% (-5.1 to +2.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 780.2 | 2,673 | +242.6% (-293.6 to +778.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3,487 | 3,259 | -6.5% (-66.6 to +53.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.29 | 1.35 | +4.8% (-6.2 to +15.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 174.3 | 309.3 | +77.5% (-75.3 to +230.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.2% (-1.1 to +0.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.198 | 0.196 | -1.1% (-5.3 to +3.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 348.2 | 344.8 | -1.0% (-5.5 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.23 | 1.29 | +4.5% (+1.1 to +8.0) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.593 | 1.15 | +94.2% (+89.9 to +98.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.2% (-0.8 to +0.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 10, 10, 16; fail-ups per arm: 1, 1, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 639 / 391.3 / 20.0 / 20.0; omni 595 / 2675.2 / 20.0 / 20.0
- rep 2 (omni then native): native 569 / 1726.7 / 20.0 / 20.0; omni 538 / 5072.6 / 20.0 / 20.0
- rep 3 (native then omni): native 689 / 222.6 / 20.0 / 20.0; omni 664 / 270.1 / 19.9 / 19.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
