# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,805 tps; base rate 2,371 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,950 | 6,949 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 6,950 | 6,949 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.852 | 0.894 | +4.9% (-10.9 to +20.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.63 | 1.92 | +17.9% (-44.7 to +80.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.339 | 0.341 | +0.7% (-1.2 to +2.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.425 | 0.449 | +5.6% (-4.5 to +15.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 16.8 | -15.1% (-29.2 to -1.1) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.378 | 0.379 | +0.4% (-0.8 to +1.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 633.4 | 635.8 | +0.4% (-0.8 to +1.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.203 | 0.203 | +0.4% (-0.5 to +1.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.48 | 3.22 | +29.5% (+26.6 to +32.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.5% (-31.8 to +8.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 12, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6955 / 0.9 / 20.0 / 20.0; omni 6949 / 0.9 / 15.8 / 16.2
- rep 2 (omni then native): native 6945 / 0.8 / 19.3 / 20.0; omni 6940 / 0.9 / 17.4 / 19.4
- rep 3 (native then omni): native 6950 / 0.8 / 20.0 / 20.0; omni 6959 / 0.9 / 17.1 / 17.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
