# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,912 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `0d532c7a2dbd`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 839.7 | 839.9 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 840.5 | 840.2 | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.65 | 5.47 | -3.3% (-19.4 to +12.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 14.1 | 13.5 | -4.3% (-79.8 to +71.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.92 | 1.91 | -0.3% (-0.9 to +0.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.67 | 2.58 | -3.1% (-16.4 to +10.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 16.7 | -15.5% (-18.5 to -12.5) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.237 | 0.237 | -0.1% (-1.5 to +1.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 369.7 | 369.4 | -0.1% (-1.7 to +1.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.978 | 0.977 | -0.1% (-1.8 to +1.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.763 | 1.51 | +97.4% (+90.9 to +104.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.3 | -13.3% (-15.5 to -11.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 41, 28, 23; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 840 / 5.8 / 20.0 / 20.0; omni 841 / 5.2 / 16.8 / 17.2
- rep 2 (omni then native): native 840 / 5.5 / 19.4 / 20.0; omni 840 / 5.6 / 16.2 / 17.4
- rep 3 (native then omni): native 839 / 5.6 / 20.0 / 20.0; omni 840 / 5.6 / 17.2 / 17.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
