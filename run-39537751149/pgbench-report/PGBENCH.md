# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 43,124 tps; base rate 6,469 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 18,976 | 18,974 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 18,976 | 18,974 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.43 | 1.73 | +21.3% (-81.6 to +124.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 8.67 | 10.2 | +17.4% (-248.6 to +283.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.197 | 0.198 | +0.2% (-3.0 to +3.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.514 | 0.575 | +11.8% (-112.4 to +136.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 17.1 | -13.6% (-19.1 to -8.1) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.455 | 0.455 | +0.0% (-1.7 to +1.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 798.8 | 799.5 | +0.1% (-1.9 to +2.0) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0936 | 0.0936 | +0.1% (-1.9 to +2.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.86 | 4.3 | +11.4% (+6.7 to +16.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.4 | -12.8% (-17.4 to -8.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 28, 52, 31; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 18979 / 1.4 / 20.0 / 20.0; omni 18974 / 2.2 / 17.1 / 17.2
- rep 2 (omni then native): native 18986 / 1.4 / 19.2 / 20.0; omni 18974 / 1.9 / 16.2 / 17.3
- rep 3 (native then omni): native 18962 / 1.5 / 20.0 / 20.0; omni 18972 / 1.1 / 17.8 / 17.9

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,848 tps; base rate 577 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,647 | 1,643 | -0.2% (-4.0 to +3.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,695 | 1,694 | -0.1% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.59 | 8.45 | -1.6% (-78.3 to +75.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 192.0 | 207.5 | +8.1% (-83.8 to +100.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.5 | 1.5 | +0.1% (-1.1 to +1.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.85 | 7.4 | +7.9% (-107.8 to +123.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | -2.5% (-4.9 to -0.1) | GAIN |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.338 | 0.339 | +0.2% (-0.5 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds | 507.8 | 508.4 | +0.1% (-0.6 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.685 | 0.688 | +0.3% (-3.2 to +3.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.79 | +77.7% (+72.1 to +83.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.6 | -1.8% (-4.1 to +0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 49, 26, 42; fail-ups per arm: 0, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1644 / 9.8 / 20.0 / 20.0; omni 1652 / 8.0 / 19.7 / 19.8
- rep 2 (omni then native): native 1658 / 6.8 / 20.0 / 20.0; omni 1625 / 9.8 / 19.6 / 19.7
- rep 3 (native then omni): native 1638 / 9.1 / 20.0 / 20.0; omni 1652 / 7.6 / 19.3 / 19.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,643 tps; base rate 246 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `e85212fa7d01`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 404.7 | 453.6 | +12.1% (-5.8 to +30.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 705.9 | 719.6 | +2.0% (-2.4 to +6.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,250 | 1,354 | -39.8% (-237.0 to +157.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,279 | 2,147 | -49.8% (-251.2 to +151.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 21.7 | 7.15 | -67.1% (-201.6 to +67.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 349.2 | 211.1 | -39.5% (-189.7 to +110.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.2% (-0.5 to +0.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.181 | 0.183 | +1.2% (-3.2 to +5.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 318.8 | 321.6 | +0.9% (-3.3 to +5.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.76 | 1.58 | -10.3% (-24.8 to +4.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.564 | 1.11 | +96.3% (+95.0 to +97.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-0.4 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 6, 6, 2; fail-ups per arm: 1, 2, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 406 / 3457.8 / 20.0 / 20.0; omni 474 / 500.8 / 20.0 / 20.0
- rep 2 (omni then native): native 370 / 1944.5 / 20.0 / 20.0; omni 434 / 2153.1 / 19.9 / 20.0
- rep 3 (native then omni): native 438 / 1348.2 / 20.0 / 20.0; omni 453 / 1408.3 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
