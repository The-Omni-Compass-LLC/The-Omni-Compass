# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,888 tps; base rate 283 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `a9694fbc7d2a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 830.4 | 830.8 | +0.0% (-1.1 to +1.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 831.3 | 831.1 | -0.0% (-0.9 to +0.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.4 | 5.5 | +2.0% (-7.7 to +11.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.1 | 13.8 | +5.5% (-54.3 to +65.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.9 | 1.9 | -0.2% (-1.0 to +0.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.62 | 2.59 | -1.0% (-23.3 to +21.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.2 | -12.8% (-16.0 to -9.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.232 | 0.232 | -0.2% (-0.8 to +0.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 362.1 | 361.4 | -0.2% (-0.9 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.969 | 0.967 | -0.2% (-2.0 to +1.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.765 | 1.5 | +96.8% (+95.7 to +97.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.7% (-15.2 to -8.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 26, 30; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 829 / 5.5 / 20.0 / 20.0; omni 833 / 5.4 / 17.2 / 17.5
- rep 2 (omni then native): native 830 / 5.4 / 19.2 / 20.0; omni 831 / 5.5 / 16.9 / 17.5
- rep 3 (native then omni): native 832 / 5.3 / 20.0 / 20.0; omni 828 / 5.6 / 17.5 / 18.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
