# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,457 tps; base rate 2,468 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,242 | 7,242 | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,242 | 7,242 | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.32 | 1.25 | -5.2% (-42.1 to +31.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.93 | 3.66 | -6.9% (-64.8 to +51.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.367 | 0.366 | -0.1% (-1.8 to +1.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.561 | 0.538 | -4.2% (-31.4 to +23.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.4 | -5.6% (-13.6 to +2.4) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.318 | 0.317 | -0.3% (-3.2 to +2.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 467.1 | 465.6 | -0.3% (-3.7 to +3.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.143 | -0.3% (-3.5 to +2.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.33 | +29.1% (+28.3 to +29.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.3% (-5.6 to -5.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 20, 11, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7245 / 1.6 / 20.0 / 20.0; omni 7239 / 1.3 / 18.5 / 19.0
- rep 2 (omni then native): native 7242 / 1.2 / 18.5 / 20.0; omni 7241 / 1.2 / 18.1 / 18.9
- rep 3 (native then omni): native 7238 / 1.2 / 20.0 / 20.0; omni 7244 / 1.3 / 18.6 / 18.9

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 6,966 tps; base rate 1,045 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,875 | 2,880 | +0.2% (-2.9 to +3.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,062 | 3,060 | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 112.6 | 101.5 | -9.9% (-114.5 to +94.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 621.8 | 580.9 | -6.6% (-25.2 to +12.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.712 | 0.733 | +3.0% (-3.9 to +9.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 22.7 | 20.8 | -8.3% (-44.9 to +28.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.8 | -0.9% (-6.8 to +4.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.334 | 0.342 | +2.6% (-1.3 to +6.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 569.2 | 584.1 | +2.6% (-1.6 to +6.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.44 | 0.451 | +2.4% (-5.0 to +9.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.852 | 1.41 | +65.8% (+62.2 to +69.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.7% (-6.1 to +4.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 57, 35, 37; fail-ups per arm: 1, 3, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2847 / 128.4 / 20.0 / 20.0; omni 2887 / 74.3 / 19.3 / 19.4
- rep 2 (omni then native): native 2891 / 92.3 / 20.0 / 20.0; omni 2900 / 73.3 / 19.8 / 19.9
- rep 3 (native then omni): native 2886 / 117.1 / 20.0 / 20.0; omni 2854 / 156.8 / 20.3 / 20.3

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,118 tps; base rate 318 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v7 (digest d6d467b824c585f1, 46 files) at `1ccba53a74fe`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 931.0 | 926.0 | -0.5% (-1.6 to +0.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 931.9 | 930.7 | -0.1% (-0.6 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.54 | 3.79 | +7.0% (-35.1 to +49.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.39 | 19.5 | +132.7% (-392.4 to +657.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.5 | 1.51 | +0.6% (-5.3 to +6.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.01 | 3.63 | +80.4% (-173.1 to +333.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 17.2 | -11.1% (-20.3 to -2.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.285 | 0.287 | +0.6% (-5.7 to +6.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 492.3 | 495.2 | +0.6% (-5.8 to +6.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.18 | 1.19 | +1.1% (-5.9 to +8.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.817 | 1.61 | +96.6% (+92.8 to +100.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.8 | -11.2% (-22.5 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 40, 40, 29; fail-ups per arm: 2, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 931 / 3.6 / 20.0 / 20.0; omni 924 / 3.7 / 17.2 / 17.3
- rep 2 (omni then native): native 932 / 3.7 / 18.2 / 20.0; omni 932 / 3.5 / 16.0 / 17.2
- rep 3 (native then omni): native 930 / 3.3 / 20.0 / 20.0; omni 922 / 4.2 / 18.6 / 18.8

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
