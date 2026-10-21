# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,805 tps; base rate 2,371 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,950 | 6,949 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 6,950 | 6,949 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.852 | 0.894 | +4.9% (-10.9 to +20.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.63 | 1.92 | +17.9% (-44.7 to +80.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.339 | 0.341 | +0.7% (-1.2 to +2.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.425 | 0.449 | +5.6% (-4.5 to +15.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 16.8 | -15.1% (-29.2 to -1.1) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.378 | 0.379 | +0.4% (-0.8 to +1.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 633.4 | 635.8 | +0.4% (-0.8 to +1.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.203 | 0.203 | +0.4% (-0.5 to +1.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.48 | 3.22 | +29.5% (+26.6 to +32.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.5% (-31.8 to +8.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 35, 12, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6955 / 0.9 / 20.0 / 20.0; omni 6949 / 0.9 / 15.8 / 16.2
- rep 2 (omni then native): native 6945 / 0.8 / 19.3 / 20.0; omni 6940 / 0.9 / 17.4 / 19.4
- rep 3 (native then omni): native 6950 / 0.8 / 20.0 / 20.0; omni 6959 / 0.9 / 17.1 / 17.6

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,704 tps; base rate 556 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,590 | 1,589 | -0.1% (-2.4 to +2.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,631 | 1,629 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.11 | 6.5 | -8.5% (-57.1 to +40.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 180.9 | 181.9 | +0.5% (-54.1 to +55.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.52 | 1.53 | +0.7% (+0.4 to +1.0) | LOSS |
| latency, mean (ms) | 6.22 | 6.18 | -0.6% (-67.0 to +65.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 19.0 | -4.6% (-8.7 to -0.5) | GAIN |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.33 | 0.333 | +0.9% (+0.2 to +1.7) | power given |
| host CPU-seconds | 496.7 | 501.4 | +0.9% (+0.2 to +1.7) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.694 | 0.701 | +1.0% (-0.7 to +2.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.84 | +78.3% (+73.2 to +83.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -3.9% (-6.5 to -1.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 34, 41; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1589 / 8.7 / 20.0 / 20.0; omni 1588 / 6.7 / 19.2 / 19.3
- rep 2 (omni then native): native 1596 / 6.1 / 19.7 / 20.0; omni 1580 / 6.9 / 19.1 / 19.4
- rep 3 (native then omni): native 1587 / 6.5 / 20.0 / 20.0; omni 1600 / 5.9 / 18.7 / 19.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,912 tps; base rate 287 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `e32bbb605501`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 840.8 | 839.7 | -0.1% (-0.7 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 841.6 | 841.1 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.94 | 6.19 | +4.1% (-38.9 to +47.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 23.7 | 24.8 | +4.4% (-47.0 to +55.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.89 | 1.9 | +0.3% (-0.7 to +1.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.85 | 2.96 | +4.0% (-21.6 to +29.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 16.9 | -14.9% (-26.9 to -2.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.233 | 0.235 | +0.7% (-1.8 to +3.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 363.5 | 366.1 | +0.7% (-1.8 to +3.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.961 | 0.969 | +0.8% (-1.8 to +3.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.771 | 1.56 | +102.2% (+96.4 to +108.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.4 | -12.8% (-26.4 to +0.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 61, 46; fail-ups per arm: 1, 0, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 840 / 5.7 / 20.0 / 20.0; omni 839 / 7.1 / 16.0 / 16.3
- rep 2 (omni then native): native 842 / 6.7 / 19.7 / 20.0; omni 843 / 6.0 / 17.5 / 18.5
- rep 3 (native then omni): native 840 / 5.5 / 20.0 / 20.0; omni 837 / 5.5 / 17.3 / 17.6

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
