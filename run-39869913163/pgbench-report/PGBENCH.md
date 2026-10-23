# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,768 tps; base rate 2,515 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,380 | 7,361 | -0.3% (-1.4 to +0.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,380 | 7,380 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.38 | 1.62 | +17.8% (-19.9 to +55.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.21 | 17.5 | +316.7% (-950.0 to +1583.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.368 | 0.371 | +0.8% (-2.9 to +4.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.567 | 0.843 | +48.6% (-124.0 to +221.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.1 | 16.8 | -12.1% (-23.4 to -0.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.323 | 0.326 | +1.0% (-3.8 to +5.8) | EVEN, no difference beyond the noise |
| host CPU-seconds | 474.6 | 480.1 | +1.2% (-4.1 to +6.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.143 | 0.145 | +1.4% (-5.0 to +7.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.61 | 3.4 | +30.4% (+17.8 to +43.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.1 | -14.3% (-44.7 to +16.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 32, 35; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7381 / 1.3 / 20.0 / 20.0; omni 7379 / 1.3 / 18.7 / 19.3
- rep 2 (omni then native): native 7378 / 1.3 / 17.4 / 20.0; omni 7379 / 1.6 / 14.4 / 14.5
- rep 3 (native then omni): native 7380 / 1.6 / 20.0 / 20.0; omni 7324 / 2.0 / 17.4 / 17.6

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,403 tps; base rate 810 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,773 | 1,760 | -0.8% (-38.8 to +37.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,341 | 2,324 | -0.8% (-5.3 to +3.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,604 | 1,724 | +7.5% (-190.7 to +205.6) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,711 | 5,055 | +86.5% (-6.5 to +179.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.19 | 1.15 | -3.3% (-40.0 to +33.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 233.2 | 273.3 | +17.2% (-189.9 to +224.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.2% (-4.2 to +3.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (-2.4 to +22.4) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.376 | 0.373 | -0.8% (-6.0 to +4.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 649.5 | 644.5 | -0.8% (-5.0 to +3.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.825 | 0.821 | -0.5% (-40.0 to +38.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.925 | 1.6 | +72.6% (+61.5 to +83.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.1% (-3.9 to +3.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 45, 53, 67; fail-ups per arm: 2, 3, 7.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1770 / 1373.7 / 20.0 / 20.0; omni 1528 / 2402.2 / 19.9 / 19.9
- rep 2 (omni then native): native 1510 / 3012.1 / 20.0 / 20.0; omni 1796 / 1669.5 / 19.7 / 19.7
- rep 3 (native then omni): native 2040 / 425.1 / 20.0 / 20.0; omni 1955 / 1098.9 / 20.3 / 20.3

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,649 tps; base rate 247 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `464fb9e27535`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 722.2 | 695.6 | -3.7% (-19.0 to +11.6) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 724.2 | 724.9 | +0.1% (-0.1 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.65 | 79.5 | +939.0% (-2928.5 to +4806.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 26.5 | 127.6 | +380.9% (-1117.5 to +1879.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 2.15 | 2.22 | +3.3% (-14.9 to +21.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 3.34 | 10.7 | +220.1% (-669.7 to +1109.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 17.7 | -10.7% (-14.6 to -6.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.231 | 0.241 | +4.4% (-16.5 to +25.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 365.3 | 382.2 | +4.6% (-17.0 to +26.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.12 | 1.23 | +9.1% (-22.1 to +40.3) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.832 | 1.66 | +100.1% (+92.9 to +107.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.1 | -9.7% (-11.9 to -7.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 26, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 719 / 9.7 / 20.0 / 20.0; omni 723 / 7.2 / 17.9 / 18.2
- rep 2 (omni then native): native 724 / 5.5 / 19.4 / 20.0; omni 718 / 14.4 / 17.5 / 18.1
- rep 3 (native then omni): native 724 / 7.7 / 20.0 / 20.0; omni 646 / 216.9 / 17.6 / 17.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
