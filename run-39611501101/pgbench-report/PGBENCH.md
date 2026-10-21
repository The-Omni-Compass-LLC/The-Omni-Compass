# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 25,917 tps; base rate 3,888 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,400 | 11,400 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 11,400 | 11,401 | +0.0% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.02 | 1.12 | +9.9% (-6.5 to +26.3) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2.41 | 3.16 | +31.1% (-47.0 to +109.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.269 | 0.268 | -0.4% (-2.2 to +1.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.402 | 0.483 | +19.9% (-42.1 to +82.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 17.2 | -14.1% (-27.4 to -0.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.449 | 0.447 | -0.5% (-1.9 to +1.0) | EVEN, no difference beyond the noise |
| host CPU-seconds | 780.5 | 776.4 | -0.5% (-2.0 to +0.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.152 | 0.151 | -0.5% (-2.0 to +0.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.58 | 4.21 | +17.6% (+11.8 to +23.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.4 | -12.9% (-29.7 to +3.9) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 46, 33, 47; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11404 / 1.1 / 20.0 / 20.0; omni 11402 / 1.2 / 16.5 / 16.6
- rep 2 (omni then native): native 11404 / 1.0 / 20.0 / 20.0; omni 11398 / 1.1 / 18.4 / 19.0
- rep 3 (native then omni): native 11392 / 0.9 / 20.0 / 20.0; omni 11400 / 1.1 / 16.6 / 16.7

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,812 tps; base rate 572 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,642 | 1,639 | -0.2% (-1.4 to +1.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,677 | 1,675 | -0.1% (-0.8 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.88 | 6.15 | +4.7% (-19.5 to +28.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 160.9 | 168.1 | +4.5% (-46.9 to +55.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.49 | 1.49 | +0.0% (-1.2 to +1.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 5.42 | 5.55 | +2.4% (-40.1 to +45.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.6% (-7.7 to -1.6) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.413 | 0.413 | +0.1% (-0.6 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 705.4 | 705.6 | +0.0% (-0.6 to +0.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.955 | 0.957 | +0.2% (-0.5 to +0.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1 | 1.81 | +80.5% (+77.6 to +83.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.2 | -4.0% (-6.9 to -1.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 44, 44, 39; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1642 / 5.6 / 20.0 / 20.0; omni 1640 / 6.5 / 19.1 / 19.2
- rep 2 (omni then native): native 1646 / 5.9 / 20.0 / 20.0; omni 1635 / 5.9 / 18.8 / 19.0
- rep 3 (native then omni): native 1637 / 6.1 / 20.0 / 20.0; omni 1643 / 6.0 / 19.3 / 19.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,849 tps; base rate 277 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v14 (digest 7afba44615fcff8f, 47 files) at `1c6437bd846a`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 811.5 | 812.3 | +0.1% (-1.4 to +1.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 811.6 | 812.4 | +0.1% (-1.4 to +1.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 5.43 | 5.36 | -1.3% (-20.5 to +18.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 12.2 | 12.2 | -0.1% (-35.1 to +34.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.98 | 1.98 | -0.2% (-2.4 to +2.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.6 | 2.59 | -0.3% (-10.3 to +9.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.4 | -6.6% (-7.9 to -5.3) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.236 | 0.236 | -0.1% (-4.8 to +4.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 369.4 | 369.0 | -0.1% (-5.0 to +4.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.01 | 1.01 | -0.2% (-3.9 to +3.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.774 | 1.51 | +95.2% (+84.2 to +106.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-6.5 to -3.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 30, 12; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 814 / 5.7 / 20.0 / 20.0; omni 809 / 5.3 / 18.6 / 18.9
- rep 2 (omni then native): native 810 / 4.9 / 19.2 / 20.0; omni 815 / 5.3 / 17.9 / 19.0
- rep 3 (native then omni): native 811 / 5.7 / 20.0 / 20.0; omni 813 / 5.5 / 18.8 / 19.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
