# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 26,100 tps; base rate 3,915 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 11,483 | 11,472 | -0.1% (-0.4 to +0.2) | no difference beyond the noise |
| throughput (transactions a second) | 11,483 | 11,478 | -0.0% (-0.2 to +0.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.15 | 2.61 | +21.4% (-7.9 to +50.7) | no difference beyond the noise |
| latency, 99th percentile (ms) | 5.91 | 7.84 | +32.6% (-11.5 to +76.7) | no difference beyond the noise |
| latency, median (ms) | 0.254 | 0.255 | +0.4% (-0.6 to +1.4) | no difference beyond the noise |
| latency, mean (ms) | 0.547 | 0.688 | +25.6% (-33.5 to +84.8) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.3 | 17.2 | -10.7% (-19.3 to -2.1) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.436 | 0.436 | +0.1% (-0.2 to +0.4) | no difference beyond the noise |
| host CPU-seconds | 749.4 | 750.2 | +0.1% (-0.1 to +0.3) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.145 | +0.2% (-0.3 to +0.7) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 3.1 | 3.77 | +21.4% (+19.0 to +23.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.9 | -10.6% (-11.8 to -9.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 31, 41, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 11485 / 2.0 / 20.0 / 20.0; omni 11478 / 2.2 / 17.4 / 17.8
- rep 2 (omni then native): native 11483 / 2.1 / 17.8 / 20.0; omni 11454 / 2.7 / 16.5 / 18.0
- rep 3 (native then omni): native 11480 / 2.4 / 20.0 / 20.0; omni 11482 / 3.0 / 17.7 / 17.9


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
