# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 46,379 tps; base rate 6,957 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 20,082 | 20,341 | +1.3% (-4.7 to +7.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 20,408 | 20,406 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 10.6 | 2.62 | -75.2% (-409.3 to +258.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 90.8 | 22.5 | -75.2% (-413.4 to +262.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.199 | 0.197 | -0.7% (-4.5 to +3.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.08 | 0.983 | -68.1% (-376.9 to +240.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 16.1 | -18.0% (-32.4 to -3.7) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (-7.4 to +17.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.461 | 0.461 | +0.2% (-2.1 to +2.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 796.6 | 799.0 | +0.3% (-2.1 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0882 | 0.0873 | -1.0% (-6.2 to +4.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.74 | 4.15 | +11.0% (+5.9 to +16.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.5 | -17.6% (-32.2 to -3.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 23, 20, 25; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 19577 / 26.9 / 20.0 / 20.0; omni 20386 / 2.5 / 17.7 / 17.8
- rep 2 (omni then native): native 20328 / 2.5 / 18.8 / 20.0; omni 20383 / 2.1 / 14.4 / 15.6
- rep 3 (native then omni): native 20341 / 2.4 / 20.0 / 20.0; omni 20254 / 3.2 / 16.1 / 16.1

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,615 tps; base rate 1,142 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,149 | 3,150 | +0.0% (-4.2 to +4.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,350 | 3,350 | -0.0% (-0.4 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 92.9 | 114.3 | +23.0% (-138.4 to +184.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 596.7 | 577.1 | -3.3% (-13.9 to +7.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.692 | 0.701 | +1.3% (-7.0 to +9.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 21.8 | 21.8 | -0.1% (-45.5 to +45.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-6.5 to +6.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.35 | 0.355 | +1.3% (-5.3 to +8.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 596.4 | 604.7 | +1.4% (-4.9 to +7.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.421 | 0.427 | +1.3% (-6.8 to +9.5) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.873 | 1.41 | +62.0% (+51.6 to +72.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.2% (-6.0 to +6.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 39, 39, 24; fail-ups per arm: 1, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3110 / 114.7 / 20.0 / 20.0; omni 3172 / 68.2 / 20.2 / 20.2
- rep 2 (omni then native): native 3175 / 60.6 / 20.0 / 20.0; omni 3150 / 129.5 / 19.4 / 19.5
- rep 3 (native then omni): native 3162 / 103.4 / 20.0 / 20.0; omni 3127 / 145.1 / 20.4 / 20.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,912 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `6d871e2baad1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 826.6 | 835.0 | +1.0% (-5.2 to +7.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 839.6 | 839.0 | -0.1% (-0.7 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.84 | 5.42 | -20.8% (-106.6 to +64.9) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 125.1 | 45.9 | -63.3% (-467.1 to +340.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.89 | 1.87 | -1.0% (-1.5 to -0.4) | GAIN |
| latency, mean (ms) | 5.99 | 3.23 | -46.0% (-277.5 to +185.4) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.2 | -6.7% (-10.2 to -3.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.232 | 0.23 | -1.1% (-2.1 to -0.1) | GAIN |
| host CPU-seconds | 362.7 | 358.5 | -1.2% (-2.4 to +0.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.975 | 0.954 | -2.2% (-9.7 to +5.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.759 | 1.48 | +94.6% (+88.9 to +100.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.6% (-6.5 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 22, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 810 / 9.2 / 20.0 / 20.0; omni 841 / 5.2 / 18.4 / 18.8
- rep 2 (omni then native): native 837 / 5.3 / 18.5 / 20.0; omni 827 / 5.9 / 17.5 / 18.8
- rep 3 (native then omni): native 832 / 6.0 / 20.0 / 20.0; omni 838 / 5.1 / 18.7 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
