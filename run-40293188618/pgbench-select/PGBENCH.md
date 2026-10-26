# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 36,773 tps; base rate 5,516 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `2d426169d766`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 15,854 | 16,172 | +2.0% (-6.8 to +10.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 16,176 | 16,172 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 43.0 | 0.341 | -99.2% (-520.9 to +322.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 182.4 | 1.21 | -99.3% (-516.9 to +318.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.159 | 0.156 | -1.9% (-12.1 to +8.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.69 | 0.215 | -96.8% (-505.0 to +311.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.1 | -8.9% (-11.3 to -6.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.362 | 0.355 | -1.9% (-12.7 to +8.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 626.4 | 613.5 | -2.1% (-13.3 to +9.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0878 | 0.0843 | -4.0% (-17.7 to +9.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 10.1 | 10.6 | +4.6% (-3.6 to +12.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.5 | -7.5% (-10.5 to -4.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 26, 22; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 16182 / 1.4 / 20.0 / 20.0; omni 16172 / 0.4 / 18.4 / 18.8
- rep 2 (omni then native): native 15207 / 127.3 / 19.7 / 20.0; omni 16172 / 0.3 / 17.7 / 18.3
- rep 3 (native then omni): native 16173 / 0.3 / 20.0 / 20.0; omni 16173 / 0.3 / 18.2 / 18.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
