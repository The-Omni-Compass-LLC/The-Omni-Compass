# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,879 tps; base rate 2,532 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,422 | 7,355 | -0.9% (-4.7 to +2.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,422 | 7,424 | +0.0% (-0.3 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.85 | 2.45 | +32.1% (-68.1 to +132.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.4 | 52.3 | +868.9% (-2847.1 to +4585.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.378 | 0.376 | -0.4% (-2.7 to +1.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.646 | 1.88 | +190.6% (-610.3 to +991.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.2 | 15.6 | -18.8% (-36.8 to -0.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.339 | 0.337 | -0.5% (-3.9 to +3.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 501.4 | 498.7 | -0.5% (-4.4 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.151 | +0.4% (-2.0 to +2.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.69 | 3.43 | +27.3% (+18.4 to +36.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.2 | -18.8% (-30.8 to -6.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 22, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7422 / 2.2 / 20.0 / 20.0; omni 7224 / 3.7 / 16.4 / 16.6
- rep 2 (omni then native): native 7417 / 1.7 / 17.7 / 20.0; omni 7422 / 2.0 / 15.5 / 16.9
- rep 3 (native then omni): native 7427 / 1.6 / 20.0 / 20.0; omni 7418 / 1.7 / 15.0 / 15.1

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,535 tps; base rate 830 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,376 | 2,367 | -0.4% (-1.8 to +1.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,434 | 2,433 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.19 | 4.16 | -0.8% (-46.5 to +44.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 185.7 | 207.0 | +11.4% (-30.7 to +53.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.06 | 1.04 | -2.2% (-7.6 to +3.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.47 | 6.18 | +12.9% (-41.2 to +67.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.7% (-5.4 to -4.0) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.416 | 0.411 | -1.3% (-4.7 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 721.6 | 712.3 | -1.3% (-4.7 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.675 | 0.669 | -0.9% (-3.5 to +1.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.08 | 1.66 | +54.6% (+50.7 to +58.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -3.8% (-4.1 to -3.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 45, 39, 44; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2376 / 4.5 / 20.0 / 20.0; omni 2376 / 3.7 / 19.0 / 19.2
- rep 2 (omni then native): native 2380 / 4.2 / 20.0 / 20.0; omni 2356 / 4.9 / 19.1 / 19.2
- rep 3 (native then omni): native 2373 / 3.8 / 20.0 / 20.0; omni 2371 / 3.9 / 19.1 / 19.3

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,440 tps; base rate 516 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `19db275eb391`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,505 | 1,507 | +0.2% (-1.7 to +2.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,513 | 1,512 | -0.0% (-0.4 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.43 | 2.14 | -12.0% (-81.2 to +57.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 25.0 | 20.4 | -18.6% (-343.2 to +306.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.862 | 0.847 | -1.8% (-10.2 to +6.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.75 | 1.65 | -5.7% (-147.1 to +135.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.5 | -11.6% (-18.6 to -4.7) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.234 | 0.23 | -1.4% (-9.2 to +6.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 402.3 | 396.8 | -1.4% (-9.1 to +6.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.594 | 0.585 | -1.5% (-10.8 to +7.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.6 | 1.13 | +87.6% (+75.5 to +99.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -11.0% (-18.1 to -3.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 46, 49, 44; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1498 / 3.0 / 20.0 / 20.0; omni 1512 / 1.9 / 18.2 / 18.4
- rep 2 (omni then native): native 1506 / 2.3 / 19.5 / 20.0; omni 1507 / 2.4 / 17.2 / 17.6
- rep 3 (native then omni): native 1509 / 2.0 / 20.0 / 20.0; omni 1501 / 2.1 / 17.1 / 17.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
