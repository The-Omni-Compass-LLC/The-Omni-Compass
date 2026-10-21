# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 36,403 tps; base rate 5,460 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `3a0af52b3c69`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 16,017 | 16,015 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 16,017 | 16,015 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.309 | 0.329 | +6.4% (-24.0 to +36.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.886 | 1.47 | +65.4% (-113.0 to +243.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.15 | 0.152 | +1.1% (-2.7 to +4.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.198 | 0.223 | +12.1% (-32.9 to +57.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.8 | -10.4% (-23.7 to +2.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.344 | 0.35 | +1.7% (-3.7 to +7.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 584.8 | 595.5 | +1.8% (-3.8 to +7.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0811 | 0.0826 | +1.8% (-3.9 to +7.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.8 | 3.41 | +21.6% (+18.7 to +24.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.0 | -9.8% (-23.0 to +3.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 40, 49, 61; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16017 / 0.3 / 20.0 / 20.0; omni 16014 / 0.3 / 18.7 / 19.0
- rep 2 (omni then native): native 16016 / 0.3 / 19.5 / 20.0; omni 16020 / 0.3 / 17.9 / 18.2
- rep 3 (native then omni): native 16019 / 0.3 / 20.0 / 20.0; omni 16010 / 0.4 / 16.7 / 16.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
