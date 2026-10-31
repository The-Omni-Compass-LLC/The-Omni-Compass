# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,698 tps; base rate 555 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `f0dbeb8652e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,598 | 1,556 | -2.6% (-6.6 to +1.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,626 | 1,625 | -0.1% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.02 | 319.7 | +7857.7% (-25810.9 to +41526.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 608.9 | 1,437 | +135.9% (-159.3 to +431.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.772 | 0.769 | -0.3% (-6.7 to +6.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 15.6 | 55.2 | +254.9% (-569.7 to +1079.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 22.3 | +11.3% (+1.8 to +20.9) | power given |
| server connections alive, most at once | 20.0 | 34.0 | +70.0% (+32.7 to +107.3) | power given |
| host CPU busy (share of the run) | 0.229 | 0.229 | -0.1% (-6.1 to +6.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 395.1 | 395.2 | +0.0% (-5.9 to +5.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.55 | 0.565 | +2.8% (+0.9 to +4.6) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.29 | 1.74 | +34.6% (+28.8 to +40.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.2 | +10.8% (+0.7 to +20.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 36, 19, 37; fail-ups per arm: 3, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1572 / 8.5 / 20.0 / 20.0; omni 1501 / 952.7 / 22.4 / 22.2
- rep 2 (omni then native): native 1610 / 2.0 / 20.0 / 20.0; omni 1577 / 4.0 / 21.5 / 21.3
- rep 3 (native then omni): native 1614 / 1.6 / 20.0 / 20.0; omni 1591 / 2.2 / 23.0 / 23.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
