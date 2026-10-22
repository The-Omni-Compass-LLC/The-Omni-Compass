# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,139 tps; base rate 321 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `36cb1cc37947`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 747.3 | 737.7 | -1.3% (-27.8 to +25.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 938.9 | 933.1 | -0.6% (-3.0 to +1.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 622.3 | 1,091 | +75.3% (-349.2 to +499.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,306 | 1,722 | +31.8% (-175.7 to +239.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.32 | 1.3 | -1.9% (-26.0 to +22.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 86.2 | 120.4 | +39.7% (-197.2 to +276.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.4% (-7.9 to +5.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.229 | 0.228 | -0.6% (-7.2 to +6.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 400.7 | 397.7 | -0.7% (-7.7 to +6.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.19 | 1.2 | +0.7% (-32.0 to +33.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.626 | 1.21 | +93.9% (+83.8 to +103.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.4% (-7.6 to +4.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 16, 16, 38; fail-ups per arm: 5, 3, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 720 / 547.0 / 20.0 / 20.0; omni 737 / 2174.4 / 20.1 / 20.0
- rep 2 (omni then native): native 732 / 865.8 / 20.0 / 20.0; omni 786 / 403.4 / 20.0 / 20.0
- rep 3 (native then omni): native 789 / 454.2 / 20.0 / 20.0; omni 690 / 694.5 / 19.1 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
