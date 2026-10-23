# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,403 tps; base rate 810 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,773 | 1,760 | -0.8% (-38.8 to +37.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,341 | 2,324 | -0.8% (-5.3 to +3.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,604 | 1,724 | +7.5% (-190.7 to +205.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,711 | 5,055 | +86.5% (-6.5 to +179.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.19 | 1.15 | -3.3% (-40.0 to +33.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 233.2 | 273.3 | +17.2% (-189.9 to +224.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.2% (-4.2 to +3.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.376 | 0.373 | -0.8% (-6.0 to +4.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 649.5 | 644.5 | -0.8% (-5.0 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.825 | 0.821 | -0.5% (-40.0 to +38.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.925 | 1.6 | +72.6% (+61.5 to +83.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-3.9 to +3.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 45, 53, 67; fail-ups per arm: 2, 3, 7.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1770 / 1373.7 / 20.0 / 20.0; omni 1528 / 2402.2 / 19.9 / 19.9
- rep 2 (omni then native): native 1510 / 3012.1 / 20.0 / 20.0; omni 1796 / 1669.5 / 19.7 / 19.7
- rep 3 (native then omni): native 2040 / 425.1 / 20.0 / 20.0; omni 1955 / 1098.9 / 20.3 / 20.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
