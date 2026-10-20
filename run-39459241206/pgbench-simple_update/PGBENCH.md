# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,024 tps; base rate 604 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,723 | 1,712 | -0.6% (-5.0 to +3.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,772 | 1,771 | -0.1% (-0.4 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.87 | 23.9 | +248.7% (-834.8 to +1332.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 195.6 | 224.8 | +14.9% (-65.6 to +95.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.46 | 1.47 | +0.9% (-1.4 to +3.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.62 | 8.06 | +21.9% (-106.8 to +150.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.5% (-8.3 to -0.7) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.425 | 0.429 | +0.8% (+0.0 to +1.6) | power given |
| host CPU-seconds | 725.4 | 731.4 | +0.8% (+0.0 to +1.7) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.935 | 0.95 | +1.5% (-3.6 to +6.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.04 | 1.83 | +76.0% (+73.6 to +78.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.3% (-7.2 to +0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 39, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1724 / 7.0 / 20.0 / 20.0; omni 1731 / 6.8 / 19.4 / 19.6
- rep 2 (omni then native): native 1724 / 6.5 / 20.0 / 20.0; omni 1678 / 58.1 / 19.1 / 19.4
- rep 3 (native then omni): native 1721 / 7.1 / 20.0 / 20.0; omni 1727 / 6.9 / 18.8 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
