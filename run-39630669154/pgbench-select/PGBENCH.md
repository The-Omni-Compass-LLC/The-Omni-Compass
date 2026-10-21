# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 33,899 tps; base rate 5,085 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `67b7cd6bf1e8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 14,913 | 14,916 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 14,913 | 14,916 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.261 | 0.296 | +13.6% (-7.4 to +34.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.606 | 0.938 | +54.6% (-25.4 to +134.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.146 | 0.149 | +2.1% (-3.1 to +7.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.169 | 0.197 | +17.0% (-5.3 to +39.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 17.5 | -12.1% (-37.6 to +13.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.316 | 0.326 | +3.1% (-3.8 to +10.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 536.4 | 553.9 | +3.2% (-3.6 to +10.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0799 | 0.0825 | +3.2% (-3.5 to +9.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.68 | 3.31 | +23.2% (+14.8 to +31.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -11.2% (-35.4 to +13.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 57, 13, 26; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 14917 / 0.3 / 20.0 / 20.0; omni 14910 / 0.3 / 17.6 / 17.9
- rep 2 (omni then native): native 14918 / 0.2 / 19.7 / 20.0; omni 14926 / 0.3 / 19.4 / 19.6
- rep 3 (native then omni): native 14903 / 0.3 / 20.0 / 20.0; omni 14911 / 0.3 / 15.5 / 15.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
