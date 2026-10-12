# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,572 tps; base rate 2,486 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,283 | 7,285 | +0.0% (-0.2 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 7,283 | 7,285 | +0.0% (-0.2 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.18 | 1.31 | +10.9% (-3.1 to +25.0) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3.1 | 3.95 | +27.3% (+7.4 to +47.2) | **WORSE** |
| latency, median (ms) | 0.365 | 0.367 | +0.4% (-1.1 to +1.8) | no difference beyond the noise |
| latency, mean (ms) | 0.517 | 0.557 | +7.8% (+6.2 to +9.3) | **WORSE** |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.7 | 18.5 | -6.4% (-10.9 to -2.0) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.318 | 0.321 | +1.0% (-1.2 to +3.2) | no difference beyond the noise |
| host CPU-seconds | 310.8 | 314.7 | +1.2% (-1.3 to +3.8) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.142 | 0.144 | +1.2% (-1.2 to +3.6) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.62 | 2.13 | +32.1% (+27.8 to +36.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -4.8% (-5.1 to -4.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 17, 15; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7283 / 1.1 / 20.0 / 20.0; omni 7286 / 1.3 / 18.7 / 19.0
- rep 2 (omni then native): native 7284 / 1.2 / 19.2 / 20.0; omni 7279 / 1.4 / 18.3 / 19.0
- rep 3 (native then omni): native 7283 / 1.2 / 20.0 / 20.0; omni 7291 / 1.2 / 18.4 / 19.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,705 tps; base rate 556 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,603 | 1,600 | -0.2% (-1.6 to +1.2) | no difference beyond the noise |
| throughput (transactions a second) | 1,630 | 1,630 | -0.0% (-0.8 to +0.8) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.85 | 4.7 | -3.2% (-40.7 to +34.4) | no difference beyond the noise |
| latency, 99th percentile (ms) | 113.5 | 144.7 | +27.4% (-150.1 to +205.0) | no difference beyond the noise |
| latency, median (ms) | 1.43 | 1.44 | +0.6% (-0.7 to +1.8) | no difference beyond the noise |
| latency, mean (ms) | 4.4 | 4.81 | +9.2% (-73.5 to +91.9) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.9 | 19.1 | -4.0% (-5.9 to -2.0) | better |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | **WORSE** |
| host CPU busy (share of the run) | 0.311 | 0.312 | +0.3% (-1.3 to +1.9) | no difference beyond the noise |
| host CPU-seconds | 310.3 | 311.5 | +0.4% (-1.3 to +2.1) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.645 | 0.649 | +0.6% (-2.3 to +3.4) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.658 | 1.19 | +80.3% (+73.8 to +86.8) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.3 | -3.4% (-5.8 to -1.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 33, 36, 36; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1613 / 4.2 / 20.0 / 20.0; omni 1601 / 4.7 / 19.3 / 19.5
- rep 2 (omni then native): native 1598 / 5.4 / 19.7 / 20.0; omni 1603 / 4.5 / 19.0 / 19.2
- rep 3 (native then omni): native 1598 / 4.9 / 20.0 / 20.0; omni 1597 / 5.0 / 19.0 / 19.2

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,264 tps; base rate 340 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v5 (digest 1bde1fc6e695d292, 43 files) at `c0bc70570862`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 919.2 | 890.8 | -3.1% (-31.1 to +24.9) | no difference beyond the noise |
| throughput (transactions a second) | 995.3 | 991.0 | -0.4% (-3.2 to +2.4) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 117.1 | 277.6 | +137.1% (-652.0 to +926.2) | no difference beyond the noise |
| latency, 99th percentile (ms) | 468.5 | 1,373 | +193.0% (-964.0 to +1350.1) | no difference beyond the noise |
| latency, median (ms) | 1.21 | 1.21 | -0.4% (-12.0 to +11.1) | no difference beyond the noise |
| latency, mean (ms) | 23.9 | 56.2 | +135.1% (-666.4 to +936.5) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.8 | 18.2 | -8.3% (-38.9 to +22.3) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.7 | +3.3% (-3.8 to +10.5) | no difference beyond the noise |
| host CPU busy (share of the run) | 0.224 | 0.224 | +0.1% (-6.2 to +6.4) | no difference beyond the noise |
| host CPU-seconds | 256.5 | 256.6 | +0.0% (-7.5 to +7.6) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.942 | 0.968 | +2.7% (-32.8 to +38.1) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.432 | 0.836 | +93.5% (+73.9 to +113.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.2 | -9.0% (-36.5 to +18.6) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 14, 37, 45; fail-ups per arm: 1, 2, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 798 / 333.6 / 20.0 / 20.0; omni 832 / 240.6 / 19.8 / 19.9
- rep 2 (omni then native): native 998 / 2.3 / 19.4 / 20.0; omni 850 / 589.7 / 19.1 / 19.1
- rep 3 (native then omni): native 962 / 15.3 / 20.0 / 20.0; omni 991 / 2.4 / 15.5 / 15.7

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
