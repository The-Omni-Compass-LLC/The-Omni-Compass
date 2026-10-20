# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,606 tps; base rate 541 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,535 | 1,501 | -2.2% (-21.9 to +17.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,587 | 1,568 | -1.2% (-6.3 to +3.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 117.1 | 76.2 | -34.9% (-637.7 to +568.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,334 | 688.7 | -48.4% (-544.6 to +447.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.774 | 0.788 | +1.9% (-3.1 to +6.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 44.1 | 24.3 | -45.0% (-548.1 to +458.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.0 | -4.9% (-6.8 to -3.0) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (-6.0 to +22.7) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.226 | 0.228 | +0.9% (+0.2 to +1.6) | power given |
| host CPU-seconds | 390.2 | 393.5 | +0.9% (+0.4 to +1.3) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.565 | 0.584 | +3.3% (-17.9 to +24.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.6 | 1.11 | +85.1% (+82.5 to +87.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -4.2% (-6.7 to -1.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 51, 45, 34; fail-ups per arm: 3, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1566 / 2.9 / 20.0 / 20.0; omni 1404 / 222.9 / 19.1 / 19.3
- rep 2 (omni then native): native 1475 / 346.1 / 19.9 / 20.0; omni 1555 / 2.7 / 18.7 / 18.9
- rep 3 (native then omni): native 1564 / 2.1 / 20.0 / 20.0; omni 1546 / 3.1 / 19.1 / 19.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
