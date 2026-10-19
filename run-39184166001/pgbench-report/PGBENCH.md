# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,132 tps; base rate 3,920 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,495 | 11,494 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,495 | 11,494 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.26 | 1.25 | -1.2% (-34.8 to +32.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.1 | 3.36 | +8.4% (-63.0 to +79.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.27 | 0.27 | +0.1% (-0.4 to +0.7) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.453 | 0.523 | +15.2% (-37.3 to +67.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 15.7 | -19.8% (-26.8 to -12.9) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.451 | 0.451 | -0.0% (-0.3 to +0.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 784.8 | 784.8 | -0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.152 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.59 | 4.22 | +17.6% (+15.0 to +20.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.2 | -19.1% (-25.2 to -13.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 28, 36; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11494 / 1.4 / 20.0 / 20.0; omni 11495 / 1.2 / 15.5 / 15.6
- rep 2 (omni then native): native 11500 / 1.2 / 18.6 / 20.0; omni 11495 / 1.3 / 15.2 / 16.3
- rep 3 (native then omni): native 11491 / 1.2 / 20.0 / 20.0; omni 11492 / 1.3 / 16.3 / 16.6

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,938 tps; base rate 591 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,689 | 1,688 | -0.1% (-4.2 to +4.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,733 | 1,732 | -0.1% (-0.1 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.83 | 9.09 | +16.0% (-128.1 to +160.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 177.8 | 170.9 | -3.9% (-112.3 to +104.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.55 | 1.54 | -0.5% (-2.7 to +1.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.26 | 6.59 | +5.2% (-120.6 to +131.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 18.6 | -7.2% (-10.6 to -3.8) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.348 | 0.347 | -0.3% (-1.3 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 521.9 | 520.3 | -0.3% (-1.3 to +0.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.687 | 0.685 | -0.2% (-3.8 to +3.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.81 | +75.7% (+72.8 to +78.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.8 | -5.8% (-10.4 to -1.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 49, 34, 36; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1685 / 8.2 / 20.0 / 20.0; omni 1693 / 7.1 / 18.2 / 18.4
- rep 2 (omni then native): native 1696 / 6.9 / 20.0 / 20.0; omni 1663 / 13.4 / 18.7 / 19.1
- rep 3 (native then omni): native 1686 / 8.3 / 20.0 / 20.0; omni 1707 / 6.8 / 18.7 / 19.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,923 tps; base rate 289 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v11 (digest 745aa53ec8eeb67b, 47 files) at `75478eb28444`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 844.6 | 845.9 | +0.2% (-0.1 to +0.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 844.7 | 846.3 | +0.2% (+0.0 to +0.4) | GAIN |
| latency, 95th percentile (ms, lag included) | 5.48 | 5.55 | +1.2% (-4.0 to +6.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 13.2 | 13.8 | +4.2% (-8.0 to +16.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.91 | 1.92 | +0.8% (-1.3 to +2.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.57 | 2.63 | +2.4% (+0.4 to +4.5) | LOSS |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.3 | 17.0 | -11.9% (-19.9 to -4.0) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.238 | 0.24 | +0.8% (-1.1 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 371.6 | 374.5 | +0.8% (-1.2 to +2.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.978 | 0.984 | +0.6% (-1.6 to +2.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.761 | 1.5 | +97.0% (+96.5 to +97.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.7% (-17.2 to -6.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 25, 24, 24; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 845 / 5.5 / 20.0 / 20.0; omni 846 / 5.4 / 17.7 / 18.2
- rep 2 (omni then native): native 845 / 5.4 / 18.0 / 20.0; omni 846 / 5.6 / 16.3 / 17.3
- rep 3 (native then omni): native 844 / 5.6 / 20.0 / 20.0; omni 846 / 5.6 / 17.1 / 17.5

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
