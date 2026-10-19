# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,503 tps; base rate 2,475 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,261 | 7,259 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,261 | 7,259 | -0.0% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.18 | 1.14 | -3.4% (-22.5 to +15.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.51 | 3.14 | -10.7% (-62.6 to +41.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.361 | 0.361 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| latency, mean (ms) | 0.524 | 0.511 | -2.6% (-17.3 to +12.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.1% (-10.3 to -3.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.312 | 0.312 | +0.1% (-0.5 to +0.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 458.4 | 458.9 | +0.1% (-0.9 to +1.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.14 | 0.14 | +0.1% (-0.9 to +1.2) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.58 | 3.27 | +26.7% (+19.5 to +33.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.4% (-6.1 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 11, 20; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7261 / 1.3 / 20.0 / 20.0; omni 7259 / 1.2 / 18.5 / 18.9
- rep 2 (omni then native): native 7261 / 1.2 / 18.4 / 20.0; omni 7261 / 1.1 / 17.3 / 18.9
- rep 3 (native then omni): native 7261 / 1.1 / 20.0 / 20.0; omni 7258 / 1.1 / 18.4 / 19.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,823 tps; base rate 573 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,641 | 1,647 | +0.4% (-1.6 to +2.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,682 | 1,681 | -0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.66 | 6.29 | -5.6% (-25.3 to +14.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 180.0 | 157.3 | -12.6% (-73.3 to +48.1) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.51 | 1.5 | -0.3% (-1.2 to +0.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.98 | 5.39 | -9.8% (-65.5 to +45.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.5 | -2.4% (-5.9 to +1.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.334 | 0.333 | -0.2% (-0.6 to +0.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 500.7 | 499.3 | -0.3% (-0.6 to +0.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.678 | 0.674 | -0.6% (-2.9 to +1.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.79 | +76.5% (+68.7 to +84.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.7 | -1.7% (-5.4 to +2.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 39, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1645 / 6.8 / 20.0 / 20.0; omni 1649 / 6.2 / 19.8 / 20.0
- rep 2 (omni then native): native 1642 / 6.7 / 20.0 / 20.0; omni 1636 / 6.9 / 19.3 / 19.4
- rep 3 (native then omni): native 1636 / 6.4 / 20.0 / 20.0; omni 1657 / 5.7 / 19.4 / 19.6

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,333 tps; base rate 350 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `8472aaad2bf4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,026 | 1,025 | -0.1% (-1.2 to +1.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,028 | 1,028 | -0.0% (-0.8 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 3.06 | 3.09 | +1.1% (-11.9 to +14.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 7.77 | 7.07 | -9.1% (-98.7 to +80.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.39 | 1.39 | +0.1% (-2.1 to +2.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.83 | 1.97 | +7.4% (-13.6 to +28.5) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 17.5 | -12.2% (-30.5 to +6.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.245 | 0.244 | -0.2% (-2.3 to +2.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 428.6 | 427.9 | -0.2% (-2.2 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.928 | 0.927 | -0.1% (-3.1 to +2.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.645 | 1.2 | +85.2% (+78.4 to +91.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.0 | -10.2% (-30.4 to +10.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 22, 21, 37; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1022 / 3.3 / 20.0 / 20.0; omni 1025 / 3.2 / 18.5 / 18.9
- rep 2 (omni then native): native 1027 / 3.0 / 19.7 / 20.0; omni 1027 / 3.0 / 18.0 / 18.9
- rep 3 (native then omni): native 1030 / 2.9 / 20.0 / 20.0; omni 1024 / 3.1 / 15.9 / 16.1

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
