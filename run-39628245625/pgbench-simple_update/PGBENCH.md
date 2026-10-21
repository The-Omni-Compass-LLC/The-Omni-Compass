# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,590 tps; base rate 688 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `990711a99dc4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,972 | 1,980 | +0.4% (-1.8 to +2.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,019 | 2,020 | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.67 | 6.14 | -7.8% (-34.5 to +18.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 164.4 | 152.0 | -7.6% (-71.6 to +56.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.27 | 1.27 | -0.2% (-2.9 to +2.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.57 | 4.97 | -10.8% (-73.1 to +51.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -3.7% (-7.4 to +0.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.429 | 0.429 | -0.0% (-2.1 to +2.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 734.9 | 734.8 | -0.0% (-2.1 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.828 | 0.825 | -0.4% (-1.5 to +0.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.17 | 1.98 | +69.4% (+68.6 to +70.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.5 | -2.7% (-6.5 to +1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 32, 23; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1980 / 6.8 / 20.0 / 20.0; omni 1984 / 5.9 / 18.9 / 19.1
- rep 2 (omni then native): native 1977 / 6.6 / 19.9 / 20.0; omni 1971 / 6.9 / 19.2 / 19.5
- rep 3 (native then omni): native 1959 / 6.6 / 20.0 / 20.0; omni 1986 / 5.7 / 19.5 / 19.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
