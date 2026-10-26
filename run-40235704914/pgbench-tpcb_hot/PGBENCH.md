# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,422 tps; base rate 513 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `5ce458c7e7d2`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,405 | 1,387 | -1.3% (-12.4 to +9.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,495 | 1,486 | -0.6% (-6.8 to +5.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 103.3 | 219.1 | +112.0% (-330.3 to +554.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,394 | 3,195 | +33.5% (-605.7 to +672.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.878 | 0.88 | +0.2% (-4.4 to +4.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 68.6 | 100.4 | +46.3% (-582.5 to +675.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.6 | -1.6% (-2.6 to -0.6) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.235 | 0.234 | -0.5% (-1.3 to +0.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 405.5 | 403.5 | -0.5% (-0.9 to -0.1) | GAIN |
| host CPU-seconds per 1,000 transactions inside the line | 0.641 | 0.648 | +1.0% (-9.9 to +11.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.27 | 1.78 | +39.7% (+29.6 to +49.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.4% (-2.3 to -0.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 32, 26, 27; fail-ups per arm: 2, 4, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1407 / 97.9 / 20.0 / 20.0; omni 1383 / 166.0 / 19.6 / 19.7
- rep 2 (omni then native): native 1397 / 166.0 / 19.9 / 20.0; omni 1319 / 484.8 / 19.6 / 19.7
- rep 3 (native then omni): native 1410 / 46.1 / 20.0 / 20.0; omni 1458 / 6.4 / 19.7 / 19.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
