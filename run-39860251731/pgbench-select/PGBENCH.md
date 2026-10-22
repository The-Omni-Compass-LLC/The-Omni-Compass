# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 25,605 tps; base rate 3,841 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `15915c961cd2`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,269 | 11,263 | -0.1% (-0.1 to -0.0) | LOSS |
| throughput (transactions a second) | 11,269 | 11,263 | -0.1% (-0.1 to -0.0) | LOSS |
| latency, 95th percentile (ms, lag included) | 1.06 | 1.11 | +4.5% (-16.9 to +25.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.65 | 2.8 | +5.9% (-32.4 to +44.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.276 | 0.276 | +0.0% (-5.6 to +5.6) | EVEN, the same |
| latency, mean (ms) | 0.417 | 0.441 | +5.7% (-13.3 to +24.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.3 | -12.2% (-24.3 to -0.1) | GAIN |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.451 | 0.451 | -0.1% (-3.8 to +3.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 784.6 | 783.3 | -0.2% (-3.7 to +3.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.155 | 0.155 | -0.1% (-3.6 to +3.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.55 | 4.2 | +18.2% (+14.1 to +22.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.4 | -13.1% (-26.3 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 40, 55; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11269 / 1.1 / 20.0 / 20.0; omni 11262 / 1.1 / 18.5 / 18.6
- rep 2 (omni then native): native 11268 / 1.0 / 19.0 / 20.0; omni 11262 / 1.0 / 16.7 / 16.8
- rep 3 (native then omni): native 11270 / 1.0 / 20.0 / 20.0; omni 11265 / 1.2 / 16.6 / 16.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
