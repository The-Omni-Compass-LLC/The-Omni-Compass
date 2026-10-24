# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,367 tps; base rate 2,455 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,197 | 7,197 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,197 | 7,197 | +0.0% (-0.1 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.52 | 1.34 | -11.7% (-40.2 to +16.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.48 | 3.91 | -12.6% (-55.8 to +30.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.374 | 0.375 | +0.1% (-0.7 to +0.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.592 | 0.564 | -4.8% (-19.7 to +10.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.7 | 18.3 | -7.3% (-7.8 to -6.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.327 | 0.328 | +0.2% (-1.3 to +1.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 483.3 | 484.2 | +0.2% (-1.6 to +1.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.149 | 0.15 | +0.2% (-1.6 to +2.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.64 | 3.41 | +29.0% (+26.9 to +31.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.2% (-5.8 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 11, 22, 20; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7195 / 1.8 / 20.0 / 20.0; omni 7198 / 1.4 / 18.6 / 18.9
- rep 2 (omni then native): native 7196 / 1.5 / 19.2 / 20.0; omni 7197 / 1.3 / 17.7 / 19.0
- rep 3 (native then omni): native 7200 / 1.3 / 20.0 / 20.0; omni 7197 / 1.3 / 18.6 / 19.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,894 tps; base rate 584 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,673 | 1,670 | -0.1% (-1.3 to +1.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,714 | 1,711 | -0.2% (-1.0 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.99 | 7.13 | +2.0% (-5.2 to +9.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 178.4 | 182.1 | +2.1% (-57.0 to +61.2) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.48 | 1.48 | +0.0% (-2.7 to +2.8) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.05 | 6.13 | +1.3% (-56.4 to +59.0) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.6% (-5.1 to +1.9) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.0 | +10.0% (+10.0 to +10.0) | power given |
| host CPU busy (share of the run) | 0.342 | 0.343 | +0.1% (-2.2 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 513.5 | 514.6 | +0.2% (-2.4 to +2.8) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.682 | 0.685 | +0.4% (-1.6 to +2.4) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.03 | 1.78 | +72.7% (+69.9 to +75.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.7% (-4.2 to +2.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 29, 25, 24; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1670 / 7.5 / 20.0 / 20.0; omni 1669 / 7.5 / 19.8 / 20.0
- rep 2 (omni then native): native 1675 / 7.0 / 20.0 / 20.0; omni 1664 / 7.3 / 19.3 / 19.5
- rep 3 (native then omni): native 1674 / 6.5 / 20.0 / 20.0; omni 1679 / 6.5 / 19.9 / 20.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,301 tps; base rate 495 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v17 (digest 7c937d09e4031cc7, 55 files) at `6e4b64630bfc`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,427 | 1,449 | +1.5% (-4.4 to +7.4) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,451 | 1,451 | -0.0% (-0.5 to +0.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.73 | 1.75 | -74.0% (-388.8 to +240.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 105.9 | 5.39 | -94.9% (-467.4 to +277.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.825 | 0.834 | +1.1% (+0.3 to +1.9) | LOSS |
| latency, mean (ms) | 4.31 | 1.16 | -73.1% (-363.7 to +217.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.4 | -7.7% (-11.6 to -3.8) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.216 | 0.218 | +1.0% (+0.0 to +2.0) | power given |
| host CPU-seconds | 372.7 | 376.1 | +0.9% (+0.0 to +1.8) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.581 | 0.577 | -0.7% (-5.9 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.577 | 1.1 | +90.6% (+81.3 to +99.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -7.2% (-13.0 to -1.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 38, 43; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1445 / 1.9 / 20.0 / 20.0; omni 1449 / 1.7 / 18.8 / 19.1
- rep 2 (omni then native): native 1388 / 16.6 / 19.7 / 20.0; omni 1449 / 1.8 / 18.0 / 18.2
- rep 3 (native then omni): native 1448 / 1.7 / 20.0 / 20.0; omni 1449 / 1.8 / 18.3 / 18.4

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
