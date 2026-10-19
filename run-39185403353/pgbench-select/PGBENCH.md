# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 39,585 tps; base rate 5,938 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `ce92ff888e73`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,417 | 17,324 | -0.5% (-1.8 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 17,419 | 17,421 | +0.0% (-0.0 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.316 | 0.333 | +5.5% (-37.6 to +48.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.987 | 19.6 | +1884.6% (-4534.3 to +8303.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.15 | 0.151 | +0.9% (-4.9 to +6.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.218 | 0.774 | +255.7% (-313.9 to +825.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 15.1 | -21.8% (-30.3 to -13.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.358 | 0.361 | +0.9% (-5.6 to +7.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 609.3 | 614.6 | +0.9% (-5.3 to +7.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0777 | 0.0788 | +1.4% (-4.0 to +6.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.92 | 3.48 | +19.1% (+14.5 to +23.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 15.6 | -22.0% (-36.6 to -7.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 43, 37, 45; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17413 / 0.4 / 20.0 / 20.0; omni 17294 / 0.3 / 16.5 / 16.8
- rep 2 (omni then native): native 17420 / 0.3 / 18.1 / 20.0; omni 17423 / 0.3 / 13.5 / 14.4
- rep 3 (native then omni): native 17418 / 0.3 / 20.0 / 20.0; omni 17256 / 0.3 / 15.4 / 15.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
