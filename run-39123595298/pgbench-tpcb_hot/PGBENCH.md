# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,858 tps; base rate 279 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 817.3 | 818.4 | +0.1% (-0.2 to +0.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 817.5 | 818.9 | +0.2% (-0.2 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.84 | 5.29 | +9.4% (-13.1 to +31.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.9 | 12.8 | +17.1% (-40.0 to +74.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.88 | 1.88 | +0.5% (-2.0 to +3.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.42 | 2.55 | +5.2% (-7.3 to +17.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 18.6 | -5.7% (-7.8 to -3.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.225 | 0.227 | +0.7% (-1.3 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 351.8 | 354.3 | +0.7% (-1.1 to +2.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.957 | 0.962 | +0.6% (-1.4 to +2.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.773 | 1.52 | +96.2% (+83.1 to +109.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.6% (-6.5 to -2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 14, 29, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 817 / 4.8 / 20.0 / 20.0; omni 817 / 5.8 / 19.0 / 19.2
- rep 2 (omni then native): native 819 / 4.7 / 19.3 / 20.0; omni 821 / 5.0 / 18.2 / 19.0
- rep 3 (native then omni): native 816 / 5.0 / 20.0 / 20.0; omni 816 / 5.1 / 18.7 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
