# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,848 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,647 | 1,643 | -0.2% (-4.0 to +3.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,695 | 1,694 | -0.1% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.59 | 8.45 | -1.6% (-78.3 to +75.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 192.0 | 207.5 | +8.1% (-83.8 to +100.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.5 | 1.5 | +0.1% (-1.1 to +1.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.85 | 7.4 | +7.9% (-107.8 to +123.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | -2.5% (-4.9 to -0.1) | GAIN |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.338 | 0.339 | +0.2% (-0.5 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 507.8 | 508.4 | +0.1% (-0.6 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.685 | 0.688 | +0.3% (-3.2 to +3.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.79 | +77.7% (+72.1 to +83.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | -1.8% (-4.1 to +0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 49, 26, 42; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1644 / 9.8 / 20.0 / 20.0; omni 1652 / 8.0 / 19.7 / 19.8
- rep 2 (omni then native): native 1658 / 6.8 / 20.0 / 20.0; omni 1625 / 9.8 / 19.6 / 19.7
- rep 3 (native then omni): native 1638 / 9.1 / 20.0 / 20.0; omni 1652 / 7.6 / 19.3 / 19.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
