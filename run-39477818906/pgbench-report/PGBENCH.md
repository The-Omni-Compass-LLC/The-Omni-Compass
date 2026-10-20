# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 46,624 tps; base rate 6,994 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 19,912 | 19,817 | -0.5% (-4.7 to +3.8) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 20,512 | 20,509 | -0.0% (-0.0 to +0.0) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 17.7 | 33.0 | +86.0% (-260.9 to +433.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 127.2 | 129.3 | +1.6% (-105.2 to +108.4) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.199 | 0.2 | +0.7% (-1.2 to +2.6) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 4.2 | 5.28 | +25.8% (-101.2 to +152.7) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 16.4 | -17.3% (-29.6 to -4.9) | GAIN |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.475 | 0.476 | +0.3% (-0.7 to +1.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 833.2 | 835.9 | +0.3% (-0.7 to +1.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.093 | 0.0938 | +0.9% (-2.9 to +4.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 4.1 | 4.54 | +10.8% (+8.1 to +13.5) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 16.8 | -16.0% (-29.4 to -2.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 22, 23; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 20190 / 2.8 / 20.0 / 20.0; omni 20483 / 2.0 / 15.4 / 15.6
- rep 2 (omni then native): native 19528 / 46.2 / 19.6 / 20.0; omni 19282 / 90.0 / 16.8 / 17.6
- rep 3 (native then omni): native 20018 / 4.2 / 20.0 / 20.0; omni 19685 / 7.0 / 17.0 / 17.2

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,952 tps; base rate 893 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,471 | 2,421 | -2.0% (-14.1 to +10.0) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 2,615 | 2,609 | -0.2% (-0.7 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 69.3 | 184.9 | +166.8% (-822.2 to +1155.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 476.0 | 1,309 | +175.1% (-650.5 to +1000.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.713 | 0.746 | +4.5% (-7.5 to +16.5) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 16.3 | 43.9 | +169.7% (-664.9 to +1004.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.8 | -0.8% (-10.6 to +9.0) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 22.3 | +11.7% (-7.3 to +30.6) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.296 | 0.307 | +3.7% (-3.9 to +11.3) | EVEN, no difference beyond the noise |
| host CPU-seconds | 506.5 | 525.4 | +3.7% (-4.0 to +11.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.455 | 0.483 | +6.0% (-12.8 to +24.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.794 | 1.39 | +75.6% (+69.0 to +82.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.9 | -0.6% (-9.3 to +8.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 47, 41, 52; fail-ups per arm: 1, 2, 2.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2462 / 73.5 / 20.0 / 20.0; omni 2494 / 22.4 / 19.3 / 19.5
- rep 2 (omni then native): native 2497 / 27.8 / 19.9 / 20.0; omni 2309 / 461.9 / 20.7 / 20.7
- rep 3 (native then omni): native 2456 / 106.6 / 20.0 / 20.0; omni 2461 / 70.5 / 19.5 / 19.5

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,206 tps; base rate 331 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `fb90309cad0d`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 960.0 | 946.4 | -1.4% (-5.5 to +2.7) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 970.8 | 970.8 | +0.0% (-0.3 to +0.3) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.75 | 19.1 | +988.5% (-3327.8 to +5304.7) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 70.6 | 788.7 | +1016.4% (-3143.7 to +5176.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.797 | 0.783 | -1.8% (-6.7 to +3.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 2.89 | 20.0 | +592.0% (-1812.4 to +2996.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.9 | 18.2 | -8.7% (-18.5 to +1.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.146 | 0.143 | -2.0% (-10.4 to +6.4) | EVEN, no difference beyond the noise |
| host CPU-seconds | 254.4 | 249.6 | -1.9% (-10.2 to +6.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.589 | 0.586 | -0.4% (-11.6 to +10.8) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.508 | 0.969 | +90.5% (+69.6 to +111.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.6 | -6.8% (-16.0 to +2.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 44, 35, 26; fail-ups per arm: 0, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 961 / 2.1 / 20.0 / 20.0; omni 961 / 1.5 / 17.4 / 17.8
- rep 2 (omni then native): native 954 / 1.7 / 19.7 / 20.0; omni 923 / 54.2 / 18.1 / 18.8
- rep 3 (native then omni): native 965 / 1.4 / 20.0 / 20.0; omni 955 / 1.5 / 19.0 / 19.3

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
