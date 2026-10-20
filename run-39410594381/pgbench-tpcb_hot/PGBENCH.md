# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,771 tps; base rate 416 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,219 | 1,219 | +0.0% (-0.6 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,219 | 1,219 | +0.0% (-0.6 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.49 | 3.42 | -2.0% (-35.1 to +31.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.32 | 7.88 | -15.5% (-126.7 to +95.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.32 | 1.32 | +0.6% (-6.0 to +7.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.71 | -2.5% (-28.2 to +23.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.2% (-15.4 to +0.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.311 | 0.312 | +0.5% (-5.1 to +6.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 546.4 | 548.9 | +0.4% (-5.2 to +6.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.996 | 1 | +0.4% (-4.9 to +5.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.735 | 1.28 | +74.6% (+72.9 to +76.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -7.0% (-8.7 to -5.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 26, 20, 12; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1220 / 3.8 / 20.0 / 20.0; omni 1217 / 3.3 / 18.3 / 18.7
- rep 2 (omni then native): native 1217 / 3.4 / 18.6 / 20.0; omni 1220 / 3.2 / 17.9 / 18.7
- rep 3 (native then omni): native 1220 / 3.3 / 20.0 / 20.0; omni 1221 / 3.7 / 18.1 / 18.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
