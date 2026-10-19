# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,333 tps; base rate 350 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,026 | 1,025 | -0.1% (-1.2 to +1.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,028 | 1,028 | -0.0% (-0.8 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.06 | 3.09 | +1.1% (-11.9 to +14.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.77 | 7.07 | -9.1% (-98.7 to +80.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.39 | 1.39 | +0.1% (-2.1 to +2.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.83 | 1.97 | +7.4% (-13.6 to +28.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 17.5 | -12.2% (-30.5 to +6.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.245 | 0.244 | -0.2% (-2.3 to +2.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 428.6 | 427.9 | -0.2% (-2.2 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.928 | 0.927 | -0.1% (-3.1 to +2.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.645 | 1.2 | +85.2% (+78.4 to +91.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.0 | -10.2% (-30.4 to +10.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 21, 37; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1022 / 3.3 / 20.0 / 20.0; omni 1025 / 3.2 / 18.5 / 18.9
- rep 2 (omni then native): native 1027 / 3.0 / 19.7 / 20.0; omni 1027 / 3.0 / 18.0 / 18.9
- rep 3 (native then omni): native 1030 / 2.9 / 20.0 / 20.0; omni 1024 / 3.1 / 15.9 / 16.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
