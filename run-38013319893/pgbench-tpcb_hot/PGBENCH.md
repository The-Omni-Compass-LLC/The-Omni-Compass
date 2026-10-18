# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,705 tps; base rate 406 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,179 | 1,187 | +0.7% (-2.7 to +4.1) | no difference beyond the noise |
| throughput (transactions a second) | 1,189 | 1,190 | +0.2% (-0.2 to +0.5) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.28 | 3.66 | -14.6% (-86.7 to +57.5) | no difference beyond the noise |
| latency, 99th percentile (ms) | 45.2 | 13.4 | -70.4% (-406.0 to +265.1) | no difference beyond the noise |
| latency, median (ms) | 1.36 | 1.35 | -0.6% (-2.2 to +0.9) | no difference beyond the noise |
| latency, mean (ms) | 2.72 | 2.11 | -22.4% (-158.6 to +113.7) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.5 | 18.1 | -7.3% (-11.9 to -2.6) | better |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.271 | 0.27 | -0.4% (-1.9 to +1.0) | no difference beyond the noise |
| host CPU-seconds | 472.7 | 470.6 | -0.4% (-1.9 to +1.0) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.891 | 0.881 | -1.1% (-5.3 to +3.0) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.664 | 1.21 | +82.6% (+80.8 to +84.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.5 | -7.4% (-12.5 to -2.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 37, 36, 38; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 1166 / 5.7 / 20.0 / 20.0; omni 1192 / 3.6 / 18.6 / 18.9
- rep 2 (omni then native): native 1188 / 3.8 / 18.6 / 20.0; omni 1182 / 3.8 / 17.5 / 18.1
- rep 3 (native then omni): native 1183 / 3.4 / 20.0 / 20.0; omni 1188 / 3.6 / 18.2 / 18.5


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
