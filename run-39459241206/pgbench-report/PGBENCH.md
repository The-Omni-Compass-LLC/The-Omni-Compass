# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 39,368 tps; base rate 5,905 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,319 | 17,284 | -0.2% (-1.1 to +0.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 17,319 | 17,315 | -0.0% (-0.2 to +0.2) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.251 | 0.265 | +5.6% (-4.9 to +16.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 0.487 | 1.34 | +175.8% (-341.1 to +692.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.139 | 0.14 | +0.7% (-1.1 to +2.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.166 | 0.404 | +143.2% (-359.8 to +646.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.0 | -9.2% (-21.3 to +2.8) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.337 | 0.338 | +0.6% (-3.4 to +4.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 569.7 | 573.2 | +0.6% (-3.3 to +4.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0731 | 0.0737 | +0.8% (-2.2 to +3.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.96 | 3.44 | +16.0% (+11.0 to +21.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.7% (-19.9 to +2.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 26, 47; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17331 / 0.3 / 20.0 / 20.0; omni 17226 / 0.3 / 18.6 / 18.8
- rep 2 (omni then native): native 17318 / 0.2 / 19.7 / 20.0; omni 17309 / 0.3 / 18.5 / 18.8
- rep 3 (native then omni): native 17308 / 0.2 / 20.0 / 20.0; omni 17319 / 0.3 / 17.1 / 17.2

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 4,024 tps; base rate 604 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,723 | 1,712 | -0.6% (-5.0 to +3.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,772 | 1,771 | -0.1% (-0.4 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 6.87 | 23.9 | +248.7% (-834.8 to +1332.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 195.6 | 224.8 | +14.9% (-65.6 to +95.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.46 | 1.47 | +0.9% (-1.4 to +3.2) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 6.62 | 8.06 | +21.9% (-106.8 to +150.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.1 | -4.5% (-8.3 to -0.7) | GAIN |
| server connections alive, most at once | 20.0 | 21.3 | +6.7% (-0.5 to +13.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.425 | 0.429 | +0.8% (+0.0 to +1.6) | power given |
| host CPU-seconds | 725.4 | 731.4 | +0.8% (+0.0 to +1.7) | power given |
| host CPU-seconds per 1,000 transactions inside the line | 0.935 | 0.95 | +1.5% (-3.6 to +6.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.04 | 1.83 | +76.0% (+73.6 to +78.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.3% (-7.2 to +0.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 48, 39, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1724 / 7.0 / 20.0 / 20.0; omni 1731 / 6.8 / 19.4 / 19.6
- rep 2 (omni then native): native 1724 / 6.5 / 20.0 / 20.0; omni 1678 / 58.1 / 19.1 / 19.4
- rep 3 (native then omni): native 1721 / 7.1 / 20.0 / 20.0; omni 1727 / 6.9 / 18.8 / 19.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,635 tps; base rate 245 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `6f4be24ffb43`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 413.7 | 466.0 | +12.6% (-8.5 to +33.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 709.5 | 717.1 | +1.1% (-2.3 to +4.5) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,999 | 779.4 | -61.0% (-322.0 to +200.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 2,917 | 1,351 | -53.7% (-270.9 to +163.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 20.3 | 3.16 | -84.5% (-214.2 to +45.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 277.2 | 131.6 | -52.5% (-246.7 to +141.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.1% (-0.1 to +0.2) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.162 | 0.16 | -1.3% (-9.0 to +6.5) | EVEN, no difference beyond the noise |
| host CPU-seconds | 276.9 | 272.4 | -1.6% (-9.4 to +6.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.49 | 1.3 | -13.0% (-30.6 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.576 | 1.13 | +96.9% (+89.3 to +104.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.1% (-0.1 to +0.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 6, 4, 4; fail-ups per arm: 3, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 445 / 684.0 / 20.0 / 20.0; omni 462 / 846.9 / 20.0 / 20.0
- rep 2 (omni then native): native 375 / 4312.5 / 20.0 / 20.0; omni 463 / 676.9 / 20.0 / 20.0
- rep 3 (native then omni): native 421 / 999.9 / 20.0 / 20.0; omni 473 / 814.4 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
