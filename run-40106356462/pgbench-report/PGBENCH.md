# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 25,264 tps; base rate 3,790 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,094 | 11,090 | -0.0% (-0.4 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,111 | 11,115 | +0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.93 | 2.11 | +9.4% (-91.9 to +110.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 5.76 | 8.22 | +42.6% (-74.2 to +159.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.261 | 0.258 | -1.3% (-4.9 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.842 | 0.792 | -6.0% (-86.1 to +74.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.0 | 16.2 | -15.1% (-20.0 to -10.2) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.435 | 0.431 | -0.9% (-3.4 to +1.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 746.6 | 740.1 | -0.9% (-3.8 to +2.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.15 | 0.148 | -0.8% (-3.5 to +1.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.9 | 3.5 | +20.5% (+18.3 to +22.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.6 | -16.8% (-28.3 to -5.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 26, 20, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11107 / 1.7 / 20.0 / 20.0; omni 11119 / 2.7 / 17.0 / 17.3
- rep 2 (omni then native): native 11080 / 1.6 / 17.1 / 20.0; omni 11058 / 1.4 / 14.7 / 15.6
- rep 3 (native then omni): native 11094 / 2.5 / 20.0 / 20.0; omni 11094 / 2.2 / 16.9 / 17.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,714 tps; base rate 1,157 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,084 | 2,978 | -3.4% (-10.0 to +3.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,391 | 3,389 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 334.0 | 431.1 | +29.1% (-33.5 to +91.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,230 | 1,595 | +29.7% (-169.0 to +228.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.743 | 0.77 | +3.7% (-1.8 to +9.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 50.7 | 71.3 | +40.7% (-98.8 to +180.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.9 | -0.4% (-6.1 to +5.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.362 | 0.367 | +1.4% (-6.2 to +9.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 616.4 | 626.1 | +1.6% (-5.9 to +9.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.444 | 0.468 | +5.3% (-4.9 to +15.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.892 | 1.45 | +63.1% (+48.0 to +78.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.3% (-5.7 to +5.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 44, 39, 63; fail-ups per arm: 2, 4, 6.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3082 / 241.2 / 20.0 / 20.0; omni 3066 / 334.3 / 19.5 / 19.6
- rep 2 (omni then native): native 3130 / 245.1 / 20.0 / 20.0; omni 3000 / 428.3 / 20.4 / 20.4
- rep 3 (native then omni): native 3040 / 515.8 / 20.0 / 20.0; omni 2867 / 530.8 / 19.8 / 19.8

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,366 tps; base rate 505 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v18 (digest 1cb92edb64c4391d, 62 files) at `1aa4ebd3855c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,379 | 1,367 | -0.9% (-22.0 to +20.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,476 | 1,480 | +0.3% (-0.6 to +1.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 193.7 | 213.0 | +10.0% (-509.4 to +529.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 448.8 | 978.7 | +118.1% (-496.9 to +733.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.868 | 0.847 | -2.5% (-10.1 to +5.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 24.4 | 43.4 | +78.0% (-429.6 to +585.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.5 | -2.1% (-15.6 to +11.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.23 | 0.225 | -1.9% (-8.5 to +4.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 395.6 | 388.4 | -1.8% (-8.7 to +5.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.638 | 0.632 | -0.9% (-26.8 to +25.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.59 | 1.09 | +84.4% (+68.6 to +100.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.7% (-15.4 to +12.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 52, 48, 44; fail-ups per arm: 3, 1, 5.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1323 / 451.1 / 20.0 / 20.0; omni 1432 / 3.1 / 18.7 / 18.8
- rep 2 (omni then native): native 1377 / 124.3 / 19.8 / 20.0; omni 1359 / 388.9 / 19.0 / 19.2
- rep 3 (native then omni): native 1437 / 5.6 / 20.0 / 20.0; omni 1311 / 247.1 / 20.8 / 20.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
