# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,649 tps; base rate 247 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 722.2 | 695.6 | -3.7% (-19.0 to +11.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 724.2 | 724.9 | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.65 | 79.5 | +939.0% (-2928.5 to +4806.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 26.5 | 127.6 | +380.9% (-1117.5 to +1879.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 2.15 | 2.22 | +3.3% (-14.9 to +21.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.34 | 10.7 | +220.1% (-669.7 to +1109.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.7 | -10.7% (-14.6 to -6.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.231 | 0.241 | +4.4% (-16.5 to +25.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 365.3 | 382.2 | +4.6% (-17.0 to +26.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.12 | 1.23 | +9.1% (-22.1 to +40.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.832 | 1.66 | +100.1% (+92.9 to +107.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.1 | -9.7% (-11.9 to -7.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 26, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 719 / 9.7 / 20.0 / 20.0; omni 723 / 7.2 / 17.9 / 18.2
- rep 2 (omni then native): native 724 / 5.5 / 19.4 / 20.0; omni 718 / 14.4 / 17.5 / 18.1
- rep 3 (native then omni): native 724 / 7.7 / 20.0 / 20.0; omni 646 / 216.9 / 17.6 / 17.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
