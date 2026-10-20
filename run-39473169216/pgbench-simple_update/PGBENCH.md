# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,069 tps; base rate 610 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `ac0eeaef8ecc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,742 | 1,749 | +0.4% (-2.2 to +3.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,789 | 1,790 | +0.1% (-0.4 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.53 | 8.35 | -2.1% (-45.0 to +40.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 172.5 | 173.3 | +0.5% (-96.7 to +97.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.48 | 1.49 | +0.4% (-1.8 to +2.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.27 | 6.13 | -2.2% (-94.7 to +90.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.8 | -5.8% (-8.3 to -3.4) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.43 | 0.432 | +0.4% (-0.9 to +1.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 734.6 | 738.1 | +0.5% (-0.9 to +1.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.937 | 0.938 | +0.1% (-3.8 to +4.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.05 | 1.86 | +76.9% (+74.7 to +79.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-7.8 to -1.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 31, 40; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1738 / 9.5 / 20.0 / 20.0; omni 1748 / 7.9 / 18.8 / 18.9
- rep 2 (omni then native): native 1748 / 8.0 / 20.0 / 20.0; omni 1735 / 9.4 / 19.0 / 19.3
- rep 3 (native then omni): native 1740 / 8.1 / 20.0 / 20.0; omni 1763 / 7.7 / 18.6 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
