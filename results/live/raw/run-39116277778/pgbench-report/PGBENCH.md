# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 42,016 tps; base rate 6,302 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 18,430 | 18,463 | +0.2% (-0.6 to +0.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 18,482 | 18,483 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.46 | 4.81 | -25.5% (-145.1 to +94.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 25.4 | 18.6 | -26.7% (-127.0 to +73.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.205 | 0.205 | +0.2% (-4.9 to +5.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.33 | 1.04 | -21.6% (-103.5 to +60.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.7 | -9.9% (-17.3 to -2.6) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.462 | 0.463 | +0.2% (-2.0 to +2.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 800.6 | 802.1 | +0.2% (-2.1 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0965 | 0.0965 | +0.0% (-2.7 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 4.31 | 4.9 | +13.6% (+9.9 to +17.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.2% (-15.9 to -2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 33, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 18326 / 9.8 / 20.0 / 20.0; omni 18423 / 5.2 / 17.4 / 17.5
- rep 2 (omni then native): native 18483 / 4.7 / 19.1 / 20.0; omni 18476 / 6.3 / 17.6 / 18.4
- rep 3 (native then omni): native 18480 / 4.8 / 20.0 / 20.0; omni 18490 / 2.9 / 18.2 / 18.5

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,277 tps; base rate 1,092 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,006 | 3,049 | +1.4% (-6.5 to +9.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,197 | 3,197 | -0.0% (-0.8 to +0.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 120.3 | 46.2 | -61.6% (-401.3 to +278.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 574.4 | 533.0 | -7.2% (-93.3 to +78.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.07 | 1.05 | -1.7% (-7.1 to +3.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 22.2 | 17.6 | -20.5% (-169.5 to +128.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.6 | -1.9% (-6.4 to +2.6) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.408 | 0.406 | -0.5% (-6.5 to +5.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 704.8 | 701.1 | -0.5% (-6.4 to +5.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.521 | 0.511 | -1.9% (-6.6 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.51 | +46.8% (+42.3 to +51.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.5% (-6.2 to +3.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 36, 30, 42; fail-ups per arm: 2, 3, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2966 / 126.2 / 20.0 / 20.0; omni 3046 / 26.1 / 19.7 / 19.8
- rep 2 (omni then native): native 3082 / 5.5 / 20.0 / 20.0; omni 3016 / 107.4 / 19.9 / 20.0
- rep 3 (native then omni): native 2971 / 229.2 / 20.0 / 20.0; omni 3085 / 5.1 / 19.2 / 19.3

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,898 tps; base rate 285 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `f09db2756842`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 833.2 | 831.7 | -0.2% (-1.7 to +1.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 833.7 | 833.6 | -0.0% (-0.7 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.14 | 5.74 | +11.6% (-21.5 to +44.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.3 | 17.7 | +33.6% (-88.3 to +155.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.88 | 1.91 | +1.1% (-1.8 to +4.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.56 | 3.44 | +34.5% (-107.9 to +177.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 17.9 | -10.2% (-13.5 to -6.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.232 | 0.235 | +1.3% (-1.3 to +4.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 361.8 | 366.7 | +1.4% (-1.6 to +4.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.965 | 0.98 | +1.6% (-2.8 to +5.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.763 | 1.5 | +97.0% (+90.2 to +103.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.4 | -8.2% (-16.7 to +0.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 15, 36, 13; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 833 / 5.4 / 20.0 / 20.0; omni 834 / 5.6 / 17.9 / 18.0
- rep 2 (omni then native): native 834 / 5.0 / 19.7 / 20.0; omni 835 / 5.3 / 17.9 / 19.2
- rep 3 (native then omni): native 833 / 5.0 / 20.0 / 20.0; omni 825 / 6.4 / 17.8 / 17.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
