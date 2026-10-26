# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,085 tps; base rate 2,413 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,073 | 7,080 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,073 | 7,080 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.17 | 1.23 | +5.1% (-9.5 to +19.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.22 | 3.39 | +5.4% (-53.7 to +64.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.366 | 0.369 | +0.8% (-0.4 to +2.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.518 | 0.534 | +3.0% (-10.7 to +16.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.5 | -7.2% (-9.4 to -5.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.312 | 0.316 | +1.3% (-0.8 to +3.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 467.4 | 474.1 | +1.4% (-0.9 to +3.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.149 | +1.3% (-1.2 to +3.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.2 | 9.02 | +10.0% (+6.5 to +13.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.2% (-6.1 to -4.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 16, 20, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7067 / 1.3 / 20.0 / 20.0; omni 7083 / 1.2 / 18.4 / 19.0
- rep 2 (omni then native): native 7073 / 1.1 / 19.7 / 20.0; omni 7080 / 1.2 / 18.4 / 19.1
- rep 3 (native then omni): native 7077 / 1.1 / 20.0 / 20.0; omni 7077 / 1.2 / 18.6 / 18.9

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,911 tps; base rate 587 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,687 | 1,683 | -0.2% (-1.5 to +1.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,720 | 1,721 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.44 | 7.07 | -5.0% (-25.0 to +15.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 141.7 | 159.0 | +12.2% (-91.8 to +116.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.51 | 1.51 | -0.1% (-3.3 to +3.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.35 | 5.55 | +3.7% (-39.3 to +46.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.3% (-4.7 to +2.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.345 | 0.344 | -0.0% (-3.3 to +3.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 519.3 | 518.8 | -0.1% (-3.7 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.684 | 0.685 | +0.1% (-4.3 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.23 | +31.9% (+28.2 to +35.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.8 | -0.8% (-4.4 to +2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 26, 29; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1699 / 7.5 / 20.0 / 20.0; omni 1685 / 6.9 / 19.5 / 19.6
- rep 2 (omni then native): native 1681 / 7.7 / 19.9 / 20.0; omni 1683 / 6.9 / 19.6 / 19.8
- rep 3 (native then omni): native 1680 / 7.2 / 20.0 / 20.0; omni 1681 / 7.5 / 20.0 / 20.2

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,916 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `fa6da97bbaa6`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 842.0 | 843.3 | +0.1% (-0.3 to +0.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 842.1 | 843.3 | +0.1% (-0.3 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.14 | 4.14 | +0.0% (-7.0 to +7.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.96 | 7.96 | -0.0% (-13.9 to +13.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.81 | 1.81 | +0.0% (-1.1 to +1.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.21 | 2.21 | -0.2% (-2.5 to +2.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.3 | -7.5% (-9.7 to -5.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.223 | 0.223 | +0.4% (-2.2 to +3.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 346.9 | 348.3 | +0.4% (-2.4 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.915 | 0.918 | +0.3% (-2.2 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.46 | 2.12 | +45.2% (+44.7 to +45.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.5% (-6.8 to -4.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 16, 16, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 843 / 4.1 / 20.0 / 20.0; omni 845 / 4.2 / 18.3 / 18.8
- rep 2 (omni then native): native 841 / 4.1 / 19.2 / 20.0; omni 843 / 4.2 / 17.9 / 19.0
- rep 3 (native then omni): native 842 / 4.2 / 20.0 / 20.0; omni 842 / 4.0 / 18.5 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
