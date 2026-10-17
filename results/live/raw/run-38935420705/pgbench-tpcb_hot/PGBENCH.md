# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,118 tps; base rate 318 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 931.0 | 926.0 | -0.5% (-1.6 to +0.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 931.9 | 930.7 | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.54 | 3.79 | +7.0% (-35.1 to +49.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.39 | 19.5 | +132.7% (-392.4 to +657.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.5 | 1.51 | +0.6% (-5.3 to +6.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.01 | 3.63 | +80.4% (-173.1 to +333.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 17.2 | -11.1% (-20.3 to -2.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.287 | +0.6% (-5.7 to +6.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 492.3 | 495.2 | +0.6% (-5.8 to +6.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.18 | 1.19 | +1.1% (-5.9 to +8.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.817 | 1.61 | +96.6% (+92.8 to +100.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -11.2% (-22.5 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 40, 40, 29; fail-ups per arm: 2, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 931 / 3.6 / 20.0 / 20.0; omni 924 / 3.7 / 17.2 / 17.3
- rep 2 (omni then native): native 932 / 3.7 / 18.2 / 20.0; omni 932 / 3.5 / 16.0 / 17.2
- rep 3 (native then omni): native 930 / 3.3 / 20.0 / 20.0; omni 922 / 4.2 / 18.6 / 18.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
