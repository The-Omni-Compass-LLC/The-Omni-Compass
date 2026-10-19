# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,586 tps; base rate 2,488 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,299 | 7,284 | -0.2% (-0.6 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,301 | 7,292 | -0.1% (-0.5 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.51 | 2.63 | +73.3% (-208.6 to +355.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 6.38 | 11.4 | +79.2% (-217.7 to +376.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.373 | 0.378 | +1.3% (-4.2 to +6.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.662 | 0.857 | +29.6% (-75.9 to +135.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.8 | -5.3% (-7.6 to -2.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.327 | 0.331 | +1.2% (-6.3 to +8.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 482.3 | 489.5 | +1.5% (-6.7 to +9.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.149 | +1.7% (-6.8 to +10.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.42 | +30.8% (+22.1 to +39.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-5.5 to -4.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 24, 37, 37; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7296 / 1.3 / 20.0 / 20.0; omni 7296 / 1.3 / 18.9 / 19.0
- rep 2 (omni then native): native 7291 / 1.9 / 19.7 / 20.0; omni 7270 / 5.0 / 18.8 / 19.0
- rep 3 (native then omni): native 7309 / 1.3 / 20.0 / 20.0; omni 7287 / 1.6 / 18.8 / 19.1

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,729 tps; base rate 559 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,599 | 1,607 | +0.5% (-2.4 to +3.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,641 | 1,641 | +0.0% (-0.2 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.43 | 5.99 | -6.9% (-61.6 to +47.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 179.7 | 147.4 | -18.0% (-112.9 to +76.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.5 | 1.5 | +0.0% (-0.8 to +0.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.27 | 5.2 | -17.0% (-113.3 to +79.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.6 | -2.0% (-4.5 to +0.6) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.327 | 0.327 | +0.2% (-0.3 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 490.8 | 491.6 | +0.2% (-0.4 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.682 | 0.68 | -0.3% (-3.6 to +2.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.77 | +75.1% (+71.6 to +78.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.8 | -1.0% (-3.4 to +1.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 23, 24, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1609 / 6.0 / 20.0 / 20.0; omni 1612 / 6.1 / 19.7 / 19.9
- rep 2 (omni then native): native 1605 / 6.0 / 20.0 / 20.0; omni 1597 / 6.6 / 19.7 / 20.0
- rep 3 (native then omni): native 1584 / 7.4 / 20.0 / 20.0; omni 1612 / 5.3 / 19.4 / 19.6

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,910 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `5031411ae285`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 840.9 | 839.2 | -0.2% (-0.3 to -0.1) | LOSS |
| throughput (transactions a second) | 840.9 | 839.3 | -0.2% (-0.3 to -0.1) | LOSS |
| latency, 95th percentile (ms, lag included) | 4.58 | 4.61 | +0.7% (-15.6 to +16.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 9.32 | 9.76 | +4.8% (-45.6 to +55.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.86 | 1.86 | -0.1% (-1.6 to +1.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.34 | 2.35 | +0.6% (-9.0 to +10.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.1 | -7.7% (-9.1 to -6.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.233 | 0.232 | -0.5% (-3.3 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 363.8 | 361.8 | -0.5% (-3.6 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.961 | 0.958 | -0.4% (-3.5 to +2.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.762 | 1.48 | +94.4% (+89.8 to +99.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.7% (-7.2 to -4.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 21, 22; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 839 / 4.7 / 20.0 / 20.0; omni 838 / 4.4 / 18.5 / 18.9
- rep 2 (omni then native): native 842 / 4.5 / 19.0 / 20.0; omni 840 / 4.8 / 17.5 / 18.7
- rep 3 (native then omni): native 842 / 4.6 / 20.0 / 20.0; omni 840 / 4.6 / 18.4 / 18.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
