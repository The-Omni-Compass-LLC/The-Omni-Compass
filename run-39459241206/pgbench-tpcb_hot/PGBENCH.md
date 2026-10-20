# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,635 tps; base rate 245 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 413.7 | 466.0 | +12.6% (-8.5 to +33.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 709.5 | 717.1 | +1.1% (-2.3 to +4.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,999 | 779.4 | -61.0% (-322.0 to +200.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,917 | 1,351 | -53.7% (-270.9 to +163.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 20.3 | 3.16 | -84.5% (-214.2 to +45.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 277.2 | 131.6 | -52.5% (-246.7 to +141.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.162 | 0.16 | -1.3% (-9.0 to +6.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 276.9 | 272.4 | -1.6% (-9.4 to +6.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.49 | 1.3 | -13.0% (-30.6 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.576 | 1.13 | +96.9% (+89.3 to +104.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.1% (-0.1 to +0.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 6, 4, 4; fail-ups per arm: 3, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 445 / 684.0 / 20.0 / 20.0; omni 462 / 846.9 / 20.0 / 20.0
- rep 2 (omni then native): native 375 / 4312.5 / 20.0 / 20.0; omni 463 / 676.9 / 20.0 / 20.0
- rep 3 (native then omni): native 421 / 999.9 / 20.0 / 20.0; omni 473 / 814.4 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
