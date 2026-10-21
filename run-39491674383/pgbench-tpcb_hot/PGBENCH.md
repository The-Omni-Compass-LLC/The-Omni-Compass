# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 2,291 tps; base rate 344 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `de8da62736d4`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 1,005 | 1,006 | +0.1% (-1.8 to +2.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,009 | 1,008 | -0.1% (-0.9 to +0.7) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2.59 | 2.51 | -3.0% (-22.0 to +16.0) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 19.4 | 4.37 | -77.4% (-422.4 to +267.6) | EVEN, no difference beyond the noise |
| latency, median (ms) | 1.28 | 1.28 | -0.1% (-1.5 to +1.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 1.86 | 1.6 | -13.7% (-113.5 to +86.1) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.4 | 16.4 | -15.8% (-27.9 to -3.6) | GAIN |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.224 | 0.224 | -0.2% (-2.4 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 392.9 | 392.2 | -0.2% (-2.5 to +2.2) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.869 | 0.866 | -0.3% (-4.2 to +3.6) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.625 | 1.14 | +83.3% (+79.7 to +86.9) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.0 | -14.8% (-21.2 to -8.4) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 30, 22, 27; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 998 / 2.8 / 20.0 / 20.0; omni 1008 / 2.5 / 16.3 / 16.6
- rep 2 (omni then native): native 1007 / 2.5 / 18.3 / 20.0; omni 1005 / 2.5 / 16.4 / 17.6
- rep 3 (native then omni): native 1011 / 2.5 / 20.0 / 20.0; omni 1006 / 2.5 / 16.5 / 16.9

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
