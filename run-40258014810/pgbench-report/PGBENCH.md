# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,493 tps; base rate 2,474 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,256 | 7,259 | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,256 | 7,259 | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.41 | 1.44 | +2.1% (-23.5 to +27.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.05 | 3.94 | -2.8% (-49.4 to +43.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.371 | 0.372 | +0.3% (-1.5 to +2.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.565 | 0.57 | +0.8% (-14.9 to +16.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 18.4 | -7.2% (-12.5 to -2.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.325 | 0.326 | +0.5% (-2.3 to +3.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 486.9 | 489.6 | +0.6% (-2.7 to +3.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.15 | +0.5% (-3.1 to +4.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.37 | 9.13 | +9.2% (+1.1 to +17.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.7% (-9.9 to -1.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 20, 12; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7265 / 1.7 / 20.0 / 20.0; omni 7257 / 1.6 / 18.6 / 19.1
- rep 2 (omni then native): native 7254 / 1.3 / 19.5 / 20.0; omni 7257 / 1.5 / 18.4 / 19.1
- rep 3 (native then omni): native 7249 / 1.3 / 20.0 / 20.0; omni 7263 / 1.3 / 18.2 / 18.5

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,839 tps; base rate 576 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,658 | 1,657 | -0.0% (-0.8 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,690 | 1,689 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.05 | 5.93 | -2.0% (-11.3 to +7.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 146.0 | 148.4 | +1.6% (-61.6 to +64.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.48 | 1.48 | +0.0% (-0.8 to +0.8) | EVEN, the same |
| latency, mean (ms) | 5.02 | 4.91 | -2.2% (-41.4 to +37.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.3 | -3.2% (-6.4 to +0.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.333 | 0.334 | +0.2% (+0.1 to +0.3) | power given |
| host CPU-seconds | 501.1 | 502.2 | +0.2% (-0.1 to +0.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.672 | 0.673 | +0.2% (-0.7 to +1.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.4 | 3.15 | +30.9% (+24.9 to +36.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | -2.0% (-3.5 to -0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 35, 31; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1666 / 6.2 / 20.0 / 20.0; omni 1660 / 5.9 / 19.6 / 19.7
- rep 2 (omni then native): native 1648 / 6.2 / 19.9 / 20.0; omni 1651 / 6.0 / 19.3 / 19.6
- rep 3 (native then omni): native 1659 / 5.8 / 20.0 / 20.0; omni 1662 / 5.9 / 19.1 / 19.5

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,219 tps; base rate 483 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `b659f0eebc58`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,317 | 1,325 | +0.6% (-22.9 to +24.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,415 | 1,404 | -0.8% (-3.8 to +2.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 242.4 | 86.6 | -64.3% (-455.5 to +327.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,180 | 407.7 | -65.5% (-404.4 to +273.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.847 | 0.845 | -0.2% (-10.8 to +10.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 50.3 | 28.5 | -43.3% (-452.6 to +366.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.6 | -1.7% (-3.9 to +0.6) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.216 | 0.213 | -1.2% (-10.0 to +7.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 373.2 | 368.9 | -1.1% (-10.1 to +7.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.63 | 0.62 | -1.6% (-32.0 to +28.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.18 | 1.63 | +38.1% (+26.1 to +50.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.3% (-2.2 to -0.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 23, 31; fail-ups per arm: 3, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1300 / 525.1 / 20.0 / 20.0; omni 1359 / 8.9 / 19.5 / 19.7
- rep 2 (omni then native): native 1382 / 2.3 / 19.8 / 20.0; omni 1248 / 246.4 / 19.6 / 19.8
- rep 3 (native then omni): native 1269 / 199.7 / 20.0 / 20.0; omni 1368 / 4.4 / 19.7 / 19.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
