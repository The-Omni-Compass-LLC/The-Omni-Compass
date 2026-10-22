# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,219 tps; base rate 1,083 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `d27db5f66c71`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,832 | 2,807 | -0.9% (-17.4 to +15.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,166 | 3,163 | -0.1% (-1.4 to +1.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 420.9 | 408.5 | -3.0% (-293.1 to +287.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,467 | 953.8 | -35.0% (-282.0 to +212.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.756 | 0.754 | -0.2% (-20.1 to +19.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 69.7 | 56.8 | -18.5% (-290.8 to +253.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.7% (-5.8 to +2.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.347 | 0.348 | +0.1% (-10.0 to +10.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 590.5 | 591.1 | +0.1% (-10.7 to +10.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.465 | 0.469 | +0.8% (-25.9 to +27.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.862 | 1.4 | +62.1% (+52.5 to +71.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.4% (-5.8 to +2.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 52, 49; fail-ups per arm: 3, 2, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2646 / 806.3 / 20.0 / 20.0; omni 2759 / 326.9 / 20.0 / 20.1
- rep 2 (omni then native): native 2921 / 240.5 / 20.0 / 20.0; omni 2682 / 741.2 / 19.5 / 19.5
- rep 3 (native then omni): native 2928 / 215.9 / 20.0 / 20.0; omni 2980 / 157.5 / 19.5 / 19.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
