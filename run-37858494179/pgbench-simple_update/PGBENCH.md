# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

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


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
