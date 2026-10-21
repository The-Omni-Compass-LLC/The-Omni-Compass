# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,331 tps; base rate 2,300 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,738 | 6,747 | +0.1% (+0.1 to +0.2) | GAIN |
| throughput (transactions a second) | 6,738 | 6,747 | +0.1% (+0.1 to +0.2) | GAIN |
| latency, 95th percentile (ms, lag included) | 0.839 | 0.835 | -0.4% (-7.0 to +6.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.61 | 1.62 | +0.9% (-32.5 to +34.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.342 | 0.342 | -0.1% (-1.6 to +1.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.439 | 0.442 | +0.7% (-7.4 to +8.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 17.7 | -9.7% (-18.5 to -0.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.373 | 0.373 | +0.1% (-1.0 to +1.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 625.4 | 625.6 | +0.0% (-1.0 to +1.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.206 | 0.206 | -0.1% (-1.2 to +1.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.15 | +28.6% (+25.9 to +31.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.7% (-16.4 to -1.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 21, 28; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6740 / 0.8 / 20.0 / 20.0; omni 6748 / 0.8 / 18.3 / 18.6
- rep 2 (omni then native): native 6736 / 0.8 / 18.7 / 20.0; omni 6746 / 0.8 / 17.3 / 18.6
- rep 3 (native then omni): native 6737 / 0.8 / 20.0 / 20.0; omni 6746 / 0.9 / 17.3 / 17.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
