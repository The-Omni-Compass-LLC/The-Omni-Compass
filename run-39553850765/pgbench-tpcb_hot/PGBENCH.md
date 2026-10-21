# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,161 tps; base rate 174 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 292.7 | 285.4 | -2.5% (-52.5 to +47.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 508.0 | 504.8 | -0.6% (-5.0 to +3.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,201 | 1,928 | +60.5% (-192.4 to +313.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,767 | 3,147 | +78.1% (-113.3 to +269.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 27.4 | 31.2 | +13.9% (-226.5 to +254.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 218.2 | 325.2 | +49.1% (-123.5 to +221.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.132 | 0.131 | -0.7% (-5.1 to +3.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 233.1 | 231.7 | -0.6% (-5.6 to +4.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.79 | 1.83 | +2.2% (-50.6 to +54.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.52 | 1.05 | +101.0% (+95.6 to +106.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.0% (-0.3 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 4, 0, 6; fail-ups per arm: 1, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 290 / 1130.8 / 20.0 / 20.0; omni 332 / 679.1 / 20.0 / 20.0
- rep 2 (omni then native): native 329 / 708.6 / 20.0 / 20.0; omni 257 / 1349.9 / 20.0 / 20.0
- rep 3 (native then omni): native 258 / 1764.6 / 20.0 / 20.0; omni 268 / 3754.1 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
