# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,000 tps; base rate 300 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 881.6 | 878.6 | -0.3% (-1.2 to +0.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 882.5 | 880.0 | -0.3% (-1.2 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.06 | 5.29 | +4.6% (+0.6 to +8.6) | LOSS |
| latency, 99th percentile (ms) | 12.0 | 16.8 | +40.7% (+1.9 to +79.4) | LOSS |
| latency, median (ms) | 1.8 | 1.8 | +0.0% (-0.3 to +0.3) | EVEN, the same |
| latency, mean (ms) | 2.54 | 2.63 | +3.4% (-0.4 to +7.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 16.2 | -16.8% (-22.0 to -11.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.313 | 0.313 | +0.1% (-0.9 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 537.7 | 537.9 | +0.0% (-0.8 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.36 | 1.36 | +0.4% (+0.2 to +0.6) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.809 | 1.61 | +98.8% (+96.5 to +101.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.9 | -15.4% (-19.6 to -11.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 45, 33, 33; fail-ups per arm: 1, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 880 / 5.0 / 20.0 / 20.0; omni 878 / 5.3 / 16.3 / 16.5
- rep 2 (omni then native): native 881 / 4.9 / 18.5 / 20.0; omni 880 / 5.1 / 15.6 / 17.2
- rep 3 (native then omni): native 885 / 5.3 / 20.0 / 20.0; omni 878 / 5.4 / 16.8 / 17.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
