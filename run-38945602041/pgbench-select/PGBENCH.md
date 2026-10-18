# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,228 tps; base rate 2,434 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `cf8dccec0604`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,139 | 7,140 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,139 | 7,140 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.21 | 1.33 | +10.2% (-7.6 to +28.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.21 | 3.91 | +21.6% (-14.2 to +57.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.371 | 0.373 | +0.5% (-1.2 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.526 | 0.558 | +6.2% (-5.2 to +17.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.4 | -6.0% (-13.6 to +1.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.32 | 0.323 | +1.0% (-1.6 to +3.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 472.8 | 478.2 | +1.1% (-1.9 to +4.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.149 | +1.1% (-1.9 to +4.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.37 | +30.5% (+27.2 to +33.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.2% (-5.6 to -4.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 20, 11, 26; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7137 / 1.2 / 20.0 / 20.0; omni 7144 / 1.3 / 18.4 / 19.0
- rep 2 (omni then native): native 7140 / 1.2 / 18.6 / 20.0; omni 7142 / 1.4 / 18.1 / 18.9
- rep 3 (native then omni): native 7139 / 1.3 / 20.0 / 20.0; omni 7135 / 1.3 / 18.5 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
