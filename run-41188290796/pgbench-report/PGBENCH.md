# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 35,918 tps; base rate 5,388 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 15,795 | 15,801 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 15,797 | 15,801 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.295 | 0.304 | +3.1% (-32.4 to +38.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.05 | 0.843 | -19.8% (-219.1 to +179.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.148 | 0.15 | +1.1% (-3.1 to +5.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.239 | 0.197 | -17.6% (-88.7 to +53.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.336 | 0.339 | +0.7% (-5.7 to +7.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 580.4 | 584.2 | +0.7% (-6.0 to +7.3) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0817 | 0.0822 | +0.6% (-5.9 to +7.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 9.67 | 10.3 | +6.1% (-2.8 to +14.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 15794 / 0.3 / 20.0 / 20.0; omni 15795 / 0.3 / 20.0 / 20.0
- rep 2 (omni then native): native 15794 / 0.3 / 20.0 / 20.0; omni 15798 / 0.3 / 20.0 / 20.0
- rep 3 (native then omni): native 15798 / 0.3 / 20.0 / 20.0; omni 15811 / 0.3 / 20.0 / 20.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,883 tps; base rate 732 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,715 | 1,894 | +10.4% (-30.8 to +51.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,139 | 2,146 | +0.3% (-1.5 to +2.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,985 | 196.0 | -90.1% (-475.8 to +295.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,690 | 491.5 | -81.7% (-428.8 to +265.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.04 | 0.985 | -5.4% (-32.2 to +21.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 247.1 | 29.8 | -87.9% (-460.2 to +284.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 29.1 | +45.4% (+36.4 to +54.3) | power given |
| server connections alive, most at once | 20.0 | 37.3 | +86.7% (+58.0 to +115.4) | power given |
| host CPU busy (share of the run) | 0.332 | 0.338 | +1.9% (-1.9 to +5.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 577.2 | 586.0 | +1.5% (-0.9 to +3.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.756 | 0.688 | -8.9% (-46.5 to +28.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.2 | 2.89 | +31.1% (+30.1 to +32.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 28.9 | +44.3% (+33.7 to +55.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 67, 59, 68; fail-ups per arm: 7, 11, 9.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1497 / 5438.6 / 20.0 / 20.0; omni 1977 / 94.2 / 29.9 / 29.8
- rep 2 (omni then native): native 1935 / 148.8 / 20.0 / 20.0; omni 1850 / 264.2 / 28.5 / 28.1
- rep 3 (native then omni): native 1714 / 367.9 / 20.0 / 20.0; omni 1855 / 229.6 / 28.9 / 28.7

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,995 tps; base rate 299 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v22 (digest 0e23a0bc561b900a, 65 files) at `4b9d088e03cf`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 877.0 | 875.1 | -0.2% (-1.4 to +0.9) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 877.1 | 878.0 | +0.1% (-0.2 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.87 | 5.12 | +5.1% (-22.4 to +32.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.4 | 23.2 | +123.0% (-449.1 to +695.0) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.76 | 1.76 | +0.0% (-2.2 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.31 | 3.49 | +51.0% (-177.3 to +279.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.303 | 0.303 | +0.1% (-1.9 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 521.1 | 521.6 | +0.1% (-2.0 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.32 | 1.32 | +0.3% (-2.6 to +3.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.49 | 2.15 | +44.1% (+43.0 to +45.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 0, 0, 0; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 876 / 4.8 / 20.0 / 20.0; omni 877 / 4.9 / 20.0 / 20.0
- rep 2 (omni then native): native 877 / 5.0 / 20.0 / 20.0; omni 877 / 4.8 / 20.0 / 20.0
- rep 3 (native then omni): native 878 / 4.8 / 20.0 / 20.0; omni 871 / 5.6 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
