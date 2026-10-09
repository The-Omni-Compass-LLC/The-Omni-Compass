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


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed in the USA. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
