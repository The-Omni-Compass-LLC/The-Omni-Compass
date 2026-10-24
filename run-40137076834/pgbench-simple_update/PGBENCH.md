# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,705 tps; base rate 1,006 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,813 | 2,830 | +0.6% (-1.4 to +2.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,954 | 2,950 | -0.1% (-0.7 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 34.5 | 9.5 | -72.4% (-277.8 to +133.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 525.9 | 477.9 | -9.1% (-13.1 to -5.1) | GAIN |
| latency, median (ms) | 0.722 | 0.706 | -2.2% (-14.2 to +9.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 16.7 | 14.4 | -13.3% (-37.3 to +10.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.6 | -2.0% (-6.8 to +2.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.331 | 0.325 | -2.0% (-12.3 to +8.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 564.8 | 553.3 | -2.0% (-12.2 to +8.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.446 | 0.435 | -2.6% (-13.9 to +8.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.853 | 1.37 | +60.1% (+58.9 to +61.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.6% (-6.7 to +3.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 34, 38, 41; fail-ups per arm: 2, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2800 / 58.1 / 20.0 / 20.0; omni 2836 / 7.9 / 20.0 / 20.1
- rep 2 (omni then native): native 2809 / 38.8 / 20.0 / 20.0; omni 2834 / 8.1 / 19.3 / 19.3
- rep 3 (native then omni): native 2829 / 6.5 / 20.0 / 20.0; omni 2820 / 12.5 / 19.5 / 19.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
