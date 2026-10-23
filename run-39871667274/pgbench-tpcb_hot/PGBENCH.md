# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,900 tps; base rate 285 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 835.7 | 835.5 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 835.9 | 836.2 | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.85 | 4.95 | +2.1% (-11.8 to +16.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.99 | 12.2 | +21.9% (-4.4 to +48.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.88 | 1.88 | -0.1% (-2.8 to +2.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.41 | 2.52 | +4.6% (-2.1 to +11.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.1 | -13.0% (-16.7 to -9.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.23 | 0.231 | +0.3% (-4.1 to +4.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 358.6 | 359.4 | +0.2% (-4.4 to +4.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.953 | 0.956 | +0.3% (-3.9 to +4.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.768 | 1.5 | +95.2% (+88.3 to +102.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.7% (-17.6 to -5.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 19, 35; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 837 / 5.1 / 20.0 / 20.0; omni 835 / 4.9 / 17.3 / 17.7
- rep 2 (omni then native): native 836 / 4.9 / 19.1 / 20.0; omni 837 / 5.0 / 16.4 / 17.2
- rep 3 (native then omni): native 834 / 4.6 / 20.0 / 20.0; omni 835 / 4.9 / 17.8 / 18.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
