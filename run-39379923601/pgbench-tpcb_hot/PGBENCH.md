# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,519 tps; base rate 378 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 688.7 | 655.3 | -4.9% (-34.0 to +24.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,061 | 1,058 | -0.3% (-13.0 to +12.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3,366 | 4,090 | +21.5% (-173.5 to +216.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,497 | 5,767 | +28.2% (-134.5 to +191.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 4.36 | 26.6 | +510.3% (-1668.3 to +2688.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 620.1 | 660.7 | +6.5% (-177.3 to +190.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.1 | +0.5% (-1.6 to +2.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.265 | 0.266 | +0.7% (-11.7 to +13.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 461.5 | 464.8 | +0.7% (-11.2 to +12.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.52 | 1.66 | +9.1% (-28.2 to +46.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.645 | 1.22 | +88.9% (+72.4 to +105.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.4% (-1.3 to +2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 4, 10; fail-ups per arm: 12, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 838 / 1548.9 / 20.0 / 20.0; omni 821 / 3552.6 / 20.3 / 20.2
- rep 2 (omni then native): native 588 / 3938.1 / 20.0 / 20.0; omni 466 / 6420.0 / 20.0 / 20.0
- rep 3 (native then omni): native 641 / 4610.7 / 20.0 / 20.0; omni 679 / 2297.0 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
