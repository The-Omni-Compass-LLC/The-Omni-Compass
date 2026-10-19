# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,951 tps; base rate 593 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `d44261ca0c5c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,732 | 1,736 | +0.2% (-1.1 to +1.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,739 | 1,740 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.62 | 2.25 | -14.3% (-108.1 to +79.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 24.9 | 19.7 | -20.5% (-247.8 to +206.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.792 | 0.791 | -0.1% (-2.1 to +1.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.61 | 1.45 | -9.6% (-109.1 to +89.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.0 | -4.9% (-5.4 to -4.4) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (-7.4 to +17.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.244 | 0.244 | +0.0% (-2.6 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 419.3 | 419.2 | -0.0% (-2.8 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.538 | 0.537 | -0.2% (-4.3 to +3.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.561 | 0.958 | +70.7% (+58.1 to +83.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.3% (-5.2 to -3.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 59, 46, 17; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1724 / 3.5 / 20.0 / 20.0; omni 1738 / 2.0 / 19.1 / 19.2
- rep 2 (omni then native): native 1734 / 2.6 / 20.0 / 20.0; omni 1733 / 2.8 / 18.9 / 19.1
- rep 3 (native then omni): native 1739 / 1.7 / 20.0 / 20.0; omni 1737 / 2.0 / 19.0 / 19.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
