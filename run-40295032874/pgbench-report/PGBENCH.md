# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,496 tps; base rate 2,474 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `c8b8e2af081f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,255 | 7,253 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,255 | 7,253 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.43 | 1.27 | -11.2% (-46.3 to +23.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.47 | 3.63 | -18.7% (-62.5 to +25.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.368 | 0.369 | +0.1% (-0.7 to +0.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.585 | 0.554 | -5.3% (-21.1 to +10.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.0 | 15.0 | -21.0% (-37.5 to -4.5) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.321 | 0.321 | +0.1% (-1.7 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 479.8 | 480.4 | +0.1% (-2.0 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.147 | 0.147 | +0.1% (-2.0 to +2.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 8.53 | 9.35 | +9.6% (+2.2 to +17.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 15.9 | -20.5% (-40.3 to -0.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 21, 21, 15; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7260 / 1.7 / 20.0 / 20.0; omni 7259 / 1.3 / 14.8 / 15.0
- rep 2 (omni then native): native 7252 / 1.3 / 17.1 / 20.0; omni 7254 / 1.3 / 13.0 / 14.9
- rep 3 (native then omni): native 7253 / 1.3 / 20.0 / 20.0; omni 7248 / 1.2 / 17.3 / 17.8

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,642 tps; base rate 1,146 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `c8b8e2af081f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,155 | 3,155 | +0.0% (-3.5 to +3.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,359 | 3,363 | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 91.1 | 150.0 | +64.8% (-161.0 to +290.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 601.6 | 666.6 | +10.8% (-32.1 to +53.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.7 | 0.69 | -1.4% (-5.2 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 21.4 | 25.1 | +17.2% (-61.1 to +95.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.9 | -0.4% (-3.7 to +2.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 23.0 | +15.0% (+15.0 to +15.0) | power given |
| host CPU busy (share of the run) | 0.355 | 0.35 | -1.2% (-4.7 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 606.2 | 598.6 | -1.3% (-5.0 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.427 | 0.422 | -1.3% (-8.5 to +5.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.31 | 2.8 | +21.2% (+15.1 to +27.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.2% (-2.8 to +2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 40, 44, 41; fail-ups per arm: 1, 3, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3130 / 87.6 / 20.0 / 20.0; omni 3180 / 69.8 / 20.2 / 20.2
- rep 2 (omni then native): native 3170 / 101.3 / 20.0 / 20.0; omni 3131 / 247.9 / 19.6 / 19.8
- rep 3 (native then omni): native 3165 / 84.3 / 20.0 / 20.0; omni 3154 / 132.4 / 19.9 / 20.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,509 tps; base rate 376 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v21 (digest b658f05d43c1e602, 63 files) at `c8b8e2af081f`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,097 | 1,104 | +0.6% (-1.2 to +2.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,103 | 1,104 | +0.2% (-0.4 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.43 | 3 | -12.7% (-73.7 to +48.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 29.4 | 6.23 | -78.9% (-417.6 to +259.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.31 | 1.32 | +0.3% (-2.0 to +2.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.22 | 1.7 | -23.2% (-118.7 to +72.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 16.7 | -15.3% (-18.9 to -11.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.246 | 0.247 | +0.6% (-2.2 to +3.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 430.9 | 433.3 | +0.5% (-2.3 to +3.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.873 | 0.872 | -0.1% (-4.6 to +4.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.36 | 1.91 | +40.4% (+37.2 to +43.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.5 | -12.5% (-15.2 to -9.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 27, 24, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1088 / 4.5 / 20.0 / 20.0; omni 1104 / 3.1 / 17.1 / 17.4
- rep 2 (omni then native): native 1099 / 2.9 / 19.3 / 20.0; omni 1104 / 2.9 / 15.9 / 17.3
- rep 3 (native then omni): native 1104 / 2.9 / 20.0 / 20.0; omni 1104 / 3.0 / 17.2 / 17.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
