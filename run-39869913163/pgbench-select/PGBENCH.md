# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,768 tps; base rate 2,515 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,380 | 7,361 | -0.3% (-1.4 to +0.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,380 | 7,380 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.38 | 1.62 | +17.8% (-19.9 to +55.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.21 | 17.5 | +316.7% (-950.0 to +1583.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.368 | 0.371 | +0.8% (-2.9 to +4.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.567 | 0.843 | +48.6% (-124.0 to +221.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.1 | 16.8 | -12.1% (-23.4 to -0.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.323 | 0.326 | +1.0% (-3.8 to +5.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 474.6 | 480.1 | +1.2% (-4.1 to +6.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.145 | +1.4% (-5.0 to +7.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.4 | +30.4% (+17.8 to +43.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.1 | -14.3% (-44.7 to +16.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 32, 35; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7381 / 1.3 / 20.0 / 20.0; omni 7379 / 1.3 / 18.7 / 19.3
- rep 2 (omni then native): native 7378 / 1.3 / 17.4 / 20.0; omni 7379 / 1.6 / 14.4 / 14.5
- rep 3 (native then omni): native 7380 / 1.6 / 20.0 / 20.0; omni 7324 / 2.0 / 17.4 / 17.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
