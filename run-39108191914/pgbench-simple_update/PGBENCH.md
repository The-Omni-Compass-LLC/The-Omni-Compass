# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,615 tps; base rate 1,142 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,149 | 3,150 | +0.0% (-4.2 to +4.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,350 | 3,350 | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 92.9 | 114.3 | +23.0% (-138.4 to +184.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 596.7 | 577.1 | -3.3% (-13.9 to +7.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.692 | 0.701 | +1.3% (-7.0 to +9.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 21.8 | 21.8 | -0.1% (-45.5 to +45.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-6.5 to +6.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.35 | 0.355 | +1.3% (-5.3 to +8.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 596.4 | 604.7 | +1.4% (-4.9 to +7.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.421 | 0.427 | +1.3% (-6.8 to +9.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.873 | 1.41 | +62.0% (+51.6 to +72.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.2% (-6.0 to +6.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 39, 24; fail-ups per arm: 1, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3110 / 114.7 / 20.0 / 20.0; omni 3172 / 68.2 / 20.2 / 20.2
- rep 2 (omni then native): native 3175 / 60.6 / 20.0 / 20.0; omni 3150 / 129.5 / 19.4 / 19.5
- rep 3 (native then omni): native 3162 / 103.4 / 20.0 / 20.0; omni 3127 / 145.1 / 20.4 / 20.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
