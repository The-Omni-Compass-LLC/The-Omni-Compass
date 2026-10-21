# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,704 tps; base rate 556 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,590 | 1,589 | -0.1% (-2.4 to +2.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,631 | 1,629 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.11 | 6.5 | -8.5% (-57.1 to +40.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 180.9 | 181.9 | +0.5% (-54.1 to +55.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.52 | 1.53 | +0.7% (+0.4 to +1.0) | LOSS |
| latency, mean (ms) | 6.22 | 6.18 | -0.6% (-67.0 to +65.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.0 | -4.6% (-8.7 to -0.5) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.33 | 0.333 | +0.9% (+0.2 to +1.7) | power given |
| host CPU-seconds | 496.7 | 501.4 | +0.9% (+0.2 to +1.7) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.701 | +1.0% (-0.7 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | +78.3% (+73.2 to +83.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -3.9% (-6.5 to -1.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 34, 41; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1589 / 8.7 / 20.0 / 20.0; omni 1588 / 6.7 / 19.2 / 19.3
- rep 2 (omni then native): native 1596 / 6.1 / 19.7 / 20.0; omni 1580 / 6.9 / 19.1 / 19.4
- rep 3 (native then omni): native 1587 / 6.5 / 20.0 / 20.0; omni 1600 / 5.9 / 18.7 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
