# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 25,657 tps; base rate 3,849 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,290 | 11,288 | -0.0% (-0.2 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 11,290 | 11,288 | -0.0% (-0.2 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.39 | 1.71 | +22.6% (-13.1 to +58.2) | no difference beyond the noise |
| latency, 99th percentile (ms) | 4.1 | 5.31 | +29.5% (+16.4 to +42.6) | **WORSE** |
| latency, median (ms) | 0.251 | 0.253 | +0.9% (+0.4 to +1.5) | **WORSE** |
| latency, mean (ms) | 0.455 | 0.526 | +15.5% (+1.5 to +29.5) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.0 | 12.2 | -35.7% (-54.9 to -16.6) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.426 | 0.43 | +0.9% (+0.4 to +1.4) | **WORSE** |
| host CPU-seconds | 487.7 | 492.3 | +0.9% (+0.1 to +1.8) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.144 | 0.145 | +1.0% (+0.3 to +1.7) | **WORSE** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.82 | 2.5 | +37.6% (+35.3 to +39.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 13.8 | -30.9% (-33.4 to -28.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 208, 203, 215; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11298 / 1.6 / 20.0 / 20.0; omni 11287 / 1.7 / 12.4 / 13.9
- rep 2 (omni then native): native 11285 / 1.4 / 17.0 / 20.0; omni 11285 / 1.7 / 11.9 / 14.0
- rep 3 (native then omni): native 11287 / 1.2 / 20.0 / 20.0; omni 11291 / 1.8 / 12.3 / 13.6

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,872 tps; base rate 1,181 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,156 | 3,078 | -2.5% (-6.8 to +1.9) | no difference beyond the noise |
| throughput (transactions a second) | 3,456 | 3,455 | -0.0% (-1.2 to +1.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 223.4 | 345.7 | +54.8% (-74.2 to +183.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 702.2 | 687.7 | -2.1% (-22.0 to +17.9) | no difference beyond the noise |
| latency, median (ms) | 0.779 | 0.787 | +1.0% (-4.1 to +6.2) | no difference beyond the noise |
| latency, mean (ms) | 32.1 | 41.8 | +30.1% (-51.3 to +111.5) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 22.0 | +10.3% (-3.6 to +24.1) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 35.7 | +78.3% (+71.2 to +85.5) | **WORSE** |
| host CPU busy (share of the run) | 0.379 | 0.389 | +2.7% (-0.4 to +5.8) | no difference beyond the noise |
| host CPU-seconds | 430.5 | 442.3 | +2.7% (-0.3 to +5.8) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.455 | 0.48 | +5.3% (+0.2 to +10.5) | **WORSE** |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.596 | 1.11 | +86.9% (+73.9 to +99.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.5 | +12.3% (-0.8 to +25.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 182, 202, 171; fail-ups per arm: 2, 2, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3042 / 309.1 / 20.0 / 20.0; omni 2944 / 474.8 / 22.6 / 23.1
- rep 2 (omni then native): native 3230 / 131.7 / 19.9 / 20.0; omni 3109 / 342.0 / 20.6 / 21.2
- rep 3 (native then omni): native 3195 / 229.3 / 20.0 / 20.0; omni 3179 / 220.3 / 22.8 / 23.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,835 tps; base rate 275 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 806.1 | 806.6 | +0.1% (-0.0 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 806.2 | 807.0 | +0.1% (-0.0 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.68 | 5.21 | +11.3% (+6.2 to +16.5) | **WORSE** |
| latency, 99th percentile (ms) | 9.23 | 14.8 | +60.4% (+16.7 to +104.0) | **WORSE** |
| latency, median (ms) | 1.88 | 1.9 | +0.7% (-3.1 to +4.4) | no difference beyond the noise |
| latency, mean (ms) | 2.37 | 2.6 | +9.6% (+2.3 to +16.8) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.5 | 10.5 | -46.1% (-58.2 to -34.0) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.223 | 0.228 | +2.4% (-2.6 to +7.4) | no difference beyond the noise |
| host CPU-seconds | 232.7 | 238.6 | +2.5% (-2.7 to +7.7) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.962 | 0.986 | +2.5% (-2.8 to +7.8) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.503 | 1.28 | +154.8% (+145.1 to +164.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 11.9 | -40.6% (-45.8 to -35.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 200, 209, 189; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 805 / 4.5 / 20.0 / 20.0; omni 805 / 5.1 / 10.4 / 11.8
- rep 2 (omni then native): native 806 / 4.8 / 18.4 / 20.0; omni 807 / 5.3 / 10.5 / 12.4
- rep 3 (native then omni): native 807 / 4.7 / 20.0 / 20.0; omni 807 / 5.3 / 10.5 / 11.6


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
