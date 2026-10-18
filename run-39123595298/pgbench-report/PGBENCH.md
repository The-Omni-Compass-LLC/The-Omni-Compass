# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,770 tps; base rate 2,516 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,377 | 7,377 | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,377 | 7,377 | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.55 | 1.39 | -10.5% (-27.6 to +6.5) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4.63 | 4.09 | -11.6% (-33.1 to +9.8) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.372 | 0.37 | -0.6% (-2.7 to +1.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.608 | 0.567 | -6.7% (-19.4 to +6.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.3 | -6.1% (-14.8 to +2.5) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.329 | 0.326 | -0.8% (-3.9 to +2.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 484.0 | 479.5 | -0.9% (-4.6 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.146 | 0.144 | -0.9% (-4.5 to +2.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.66 | 3.35 | +25.7% (+18.4 to +32.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.9 | -5.6% (-6.5 to -4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 11, 11; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7373 / 1.6 / 20.0 / 20.0; omni 7376 / 1.4 / 18.4 / 19.0
- rep 2 (omni then native): native 7377 / 1.5 / 18.5 / 20.0; omni 7371 / 1.3 / 18.1 / 18.8
- rep 3 (native then omni): native 7381 / 1.5 / 20.0 / 20.0; omni 7383 / 1.5 / 18.4 / 18.8

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,812 tps; base rate 572 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,635 | 1,641 | +0.4% (-2.4 to +3.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,677 | 1,678 | +0.0% (-0.4 to +0.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 8.88 | 8.57 | -3.5% (-38.2 to +31.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 173.9 | 170.3 | -2.1% (-76.5 to +72.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.52 | 1.52 | +0.5% (-0.5 to +1.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.28 | 5.89 | -6.2% (-79.7 to +67.2) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.2 | -3.9% (-6.2 to -1.6) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.334 | 0.336 | +0.7% (-0.8 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 502.6 | 506.2 | +0.7% (-0.8 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.683 | 0.685 | +0.3% (-1.1 to +1.7) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.01 | 1.81 | +78.4% (+73.8 to +83.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.3% (-5.1 to -1.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 36, 44; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1640 / 8.6 / 20.0 / 20.0; omni 1639 / 8.5 / 19.4 / 19.5
- rep 2 (omni then native): native 1647 / 7.9 / 20.0 / 20.0; omni 1639 / 8.7 / 19.0 / 19.2
- rep 3 (native then omni): native 1618 / 10.1 / 20.0 / 20.0; omni 1646 / 8.5 / 19.3 / 19.4

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,858 tps; base rate 279 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v10 (digest 4bf39b0d707784de, 47 files) at `faaaff3142e1`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 817.3 | 818.4 | +0.1% (-0.2 to +0.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 817.5 | 818.9 | +0.2% (-0.2 to +0.6) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.84 | 5.29 | +9.4% (-13.1 to +31.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 10.9 | 12.8 | +17.1% (-40.0 to +74.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.88 | 1.88 | +0.5% (-2.0 to +3.0) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.42 | 2.55 | +5.2% (-7.3 to +17.8) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.8 | 18.6 | -5.7% (-7.8 to -3.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.225 | 0.227 | +0.7% (-1.3 to +2.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 351.8 | 354.3 | +0.7% (-1.1 to +2.6) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.957 | 0.962 | +0.6% (-1.4 to +2.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.773 | 1.52 | +96.2% (+83.1 to +109.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.1 | -4.6% (-6.5 to -2.8) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 14, 29, 32; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 817 / 4.8 / 20.0 / 20.0; omni 817 / 5.8 / 19.0 / 19.2
- rep 2 (omni then native): native 819 / 4.7 / 19.3 / 20.0; omni 821 / 5.0 / 18.2 / 19.0
- rep 3 (native then omni): native 816 / 5.0 / 20.0 / 20.0; omni 816 / 5.1 / 18.7 / 19.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
