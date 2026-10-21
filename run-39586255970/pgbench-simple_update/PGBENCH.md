# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,584 tps; base rate 688 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,971 | 1,974 | +0.1% (-1.1 to +1.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,016 | 2,016 | -0.0% (-0.7 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.65 | 6.2 | -6.8% (-38.1 to +24.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 165.3 | 161.3 | -2.5% (-70.7 to +65.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.26 | 1.27 | +0.3% (-0.5 to +1.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.46 | 5.28 | -3.4% (-67.3 to +60.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.9 | -5.2% (-7.5 to -2.9) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.427 | 0.429 | +0.4% (-0.3 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 730.7 | 733.2 | +0.3% (-0.3 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.824 | 0.826 | +0.2% (-1.7 to +2.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.12 | 1.96 | +75.4% (+70.0 to +80.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -3.9% (-6.7 to -1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 46, 44, 50; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1973 / 7.4 / 20.0 / 20.0; omni 1979 / 6.1 / 19.0 / 19.2
- rep 2 (omni then native): native 1977 / 6.3 / 19.9 / 20.0; omni 1968 / 6.7 / 19.0 / 19.5
- rep 3 (native then omni): native 1964 / 6.3 / 20.0 / 20.0; omni 1974 / 5.8 / 18.8 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
