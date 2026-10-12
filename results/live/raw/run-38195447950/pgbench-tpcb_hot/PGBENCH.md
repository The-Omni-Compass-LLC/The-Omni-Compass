# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,264 tps; base rate 340 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 919.2 | 890.8 | -3.1% (-31.1 to +24.9) | no difference beyond the noise |
| throughput (transactions a second) | 995.3 | 991.0 | -0.4% (-3.2 to +2.4) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 117.1 | 277.6 | +137.1% (-652.0 to +926.2) | no difference beyond the noise |
| latency, 99th percentile (ms) | 468.5 | 1,373 | +193.0% (-964.0 to +1350.1) | no difference beyond the noise |
| latency, median (ms) | 1.21 | 1.21 | -0.4% (-12.0 to +11.1) | no difference beyond the noise |
| latency, mean (ms) | 23.9 | 56.2 | +135.1% (-666.4 to +936.5) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.8 | 18.2 | -8.3% (-38.9 to +22.3) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.224 | 0.224 | +0.1% (-6.2 to +6.4) | no difference beyond the noise |
| host CPU-seconds | 256.5 | 256.6 | +0.0% (-7.5 to +7.6) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.942 | 0.968 | +2.7% (-32.8 to +38.1) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.432 | 0.836 | +93.5% (+73.9 to +113.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.0% (-36.5 to +18.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 14, 37, 45; fail-ups per arm: 1, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 798 / 333.6 / 20.0 / 20.0; omni 832 / 240.6 / 19.8 / 19.9
- rep 2 (omni then native): native 998 / 2.3 / 19.4 / 20.0; omni 850 / 589.7 / 19.1 / 19.1
- rep 3 (native then omni): native 962 / 15.3 / 20.0 / 20.0; omni 991 / 2.4 / 15.5 / 15.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
