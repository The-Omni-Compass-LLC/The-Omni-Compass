# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 35,851 tps; base rate 5,378 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 15,772 | 15,771 | -0.0% (-0.2 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 15,772 | 15,771 | -0.0% (-0.2 to +0.2) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 0.333 | 0.293 | -11.8% (-42.2 to +18.6) | no difference beyond the noise |
| latency, 99th percentile (ms) | 1.14 | 1.87 | +64.5% (-311.0 to +440.0) | no difference beyond the noise |
| latency, median (ms) | 0.158 | 0.152 | -3.8% (-9.5 to +1.9) | no difference beyond the noise |
| latency, mean (ms) | 0.201 | 0.284 | +41.5% (-55.1 to +138.1) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.3 | 11.9 | -38.4% (-51.2 to -25.6) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.352 | 0.34 | -3.3% (-10.7 to +4.1) | no difference beyond the noise |
| host CPU-seconds | 399.3 | 386.4 | -3.2% (-10.3 to +3.8) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.0844 | 0.0817 | -3.2% (-10.3 to +3.9) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 1.77 | 2.2 | +24.4% (+17.1 to +31.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 14.1 | -29.5% (-40.5 to -18.5) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 204, 220, 212; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 15776 / 0.4 / 20.0 / 20.0; omni 15762 / 0.3 / 12.2 / 14.8
- rep 2 (omni then native): native 15766 / 0.3 / 18.0 / 20.0; omni 15769 / 0.3 / 11.7 / 14.3
- rep 3 (native then omni): native 15774 / 0.3 / 20.0 / 20.0; omni 15783 / 0.3 / 11.8 / 13.1

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 7,610 tps; base rate 1,142 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,105 | 3,080 | -0.8% (-5.0 to +3.4) | no difference beyond the noise |
| throughput (transactions a second) | 3,340 | 3,341 | +0.0% (-0.8 to +0.9) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 201.0 | 260.1 | +29.4% (-46.1 to +104.8) | no difference beyond the noise |
| latency, 99th percentile (ms) | 572.9 | 636.2 | +11.0% (-34.4 to +56.5) | no difference beyond the noise |
| latency, median (ms) | 1.03 | 1.04 | +1.1% (+0.6 to +1.6) | **WORSE** |
| latency, mean (ms) | 26.7 | 31.1 | +16.6% (-60.1 to +93.3) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 21.6 | +7.8% (+3.0 to +12.6) | **WORSE** |
| server connections alive, most at once | 20.0 | 36.0 | +80.0% (+55.2 to +104.8) | **WORSE** |
| host CPU busy (share of the run) | 0.414 | 0.421 | +1.7% (+0.5 to +2.9) | **WORSE** |
| host CPU-seconds | 476.3 | 485.1 | +1.8% (+0.6 to +3.1) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 0.512 | 0.525 | +2.6% (-2.5 to +7.7) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.644 | 1.06 | +65.0% (+62.9 to +67.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 22.1 | +10.3% (+7.0 to +13.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 170, 165, 165; fail-ups per arm: 1, 1, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3185 / 37.4 / 20.0 / 20.0; omni 3103 / 162.6 / 21.1 / 21.8
- rep 2 (omni then native): native 3014 / 380.9 / 20.0 / 20.0; omni 3036 / 385.8 / 21.9 / 22.3
- rep 3 (native then omni): native 3115 / 184.7 / 20.0 / 20.0; omni 3100 / 231.9 / 21.6 / 22.1

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,103 tps; base rate 315 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 20 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `310cf31838e7`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 531.6 | 382.2 | -28.1% (-102.5 to +46.3) | no difference beyond the noise |
| throughput (transactions a second) | 878.0 | 885.9 | +0.9% (-7.1 to +8.9) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,402 | 2,522 | +5.0% (-92.6 to +102.5) | no difference beyond the noise |
| latency, 99th percentile (ms) | 3,806 | 3,311 | -13.0% (-111.7 to +85.6) | no difference beyond the noise |
| latency, median (ms) | 28.5 | 135.3 | +375.2% (-563.7 to +1314.2) | no difference beyond the noise |
| latency, mean (ms) | 455.9 | 610.2 | +33.9% (-108.3 to +176.0) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 20.0 | 21.0 | +5.1% (+1.2 to +9.1) | **WORSE** |
| server connections alive, most at once | 20.0 | 30.0 | +50.0% (+28.5 to +71.5) | **WORSE** |
| host CPU busy (share of the run) | 0.224 | 0.237 | +5.8% (-0.1 to +11.8) | no difference beyond the noise |
| host CPU-seconds | 262.6 | 278.6 | +6.1% (+0.2 to +12.0) | **WORSE** |
| host CPU-seconds per 1,000 transactions inside the line | 1.73 | 2.46 | +42.6% (-41.3 to +126.4) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.411 | 0.821 | +100.1% (+95.5 to +104.6) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.1 | +0.7% (-3.4 to +4.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 72, 57, 69; fail-ups per arm: 16, 12, 13.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 705 / 473.6 / 20.0 / 20.0; omni 391 / 1671.8 / 20.7 / 19.8
- rep 2 (omni then native): native 425 / 3568.0 / 20.0 / 20.0; omni 428 / 3016.2 / 21.4 / 20.3
- rep 3 (native then omni): native 465 / 3165.5 / 20.0 / 20.0; omni 328 / 2876.9 / 21.0 / 20.4


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
