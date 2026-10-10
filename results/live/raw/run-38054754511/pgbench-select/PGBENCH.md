# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 39,229 tps; base rate 5,884 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `ca745467845c`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 17,233 | 17,193 | -0.2% (-1.5 to +1.0) | no difference beyond the noise |
| throughput (transactions a second) | 17,255 | 17,256 | +0.0% (-0.1 to +0.1) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 7.14 | 8.95 | +25.5% (-255.2 to +306.1) | no difference beyond the noise |
| latency, 99th percentile (ms) | 19.3 | 29.3 | +51.5% (-202.2 to +305.2) | no difference beyond the noise |
| latency, median (ms) | 0.22 | 0.222 | +0.9% (-5.9 to +7.7) | no difference beyond the noise |
| latency, mean (ms) | 1.23 | 1.64 | +32.9% (-174.3 to +240.2) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.6 | 17.7 | -9.6% (-20.3 to +1.1) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | **WORSE** |
| host CPU busy (share of the run) | 0.468 | 0.471 | +0.7% (-2.5 to +3.8) | no difference beyond the noise |
| host CPU-seconds | 807.4 | 814.2 | +0.8% (-2.4 to +4.0) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.104 | 0.105 | +1.1% (-2.4 to +4.5) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 4.44 | 5.08 | +14.4% (+7.8 to +21.0) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.0 | -10.2% (-25.7 to +5.3) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 25, 37, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 17189 / 14.1 / 20.0 / 20.0; omni 17209 / 6.7 / 18.6 / 18.7
- rep 2 (omni then native): native 17261 / 3.4 / 18.7 / 20.0; omni 17256 / 8.5 / 15.9 / 16.5
- rep 3 (native then omni): native 17249 / 3.9 / 20.0 / 20.0; omni 17113 / 11.7 / 18.6 / 18.7


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
