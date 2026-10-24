# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 16,441 tps; base rate 2,466 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 7,231 | 7,229 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 7,231 | 7,229 | -0.0% (-0.2 to +0.1) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1.37 | 1.23 | -10.0% (-47.7 to +27.8) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 3.99 | 3.43 | -14.1% (-68.8 to +40.7) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.371 | 0.369 | -0.4% (-3.2 to +2.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.564 | 0.533 | -5.5% (-25.3 to +14.3) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.5 | 18.3 | -6.1% (-15.5 to +3.3) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.32 | 0.318 | -0.6% (-4.8 to +3.6) | EVEN, no difference beyond the noise |
| host CPU-seconds | 471.1 | 467.3 | -0.8% (-5.5 to +3.9) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.145 | 0.144 | -0.8% (-5.6 to +4.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.62 | 3.3 | +25.9% (+19.7 to +32.1) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.0 | -5.2% (-5.4 to -5.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 18, 11, 18; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 7232 / 1.5 / 20.0 / 20.0; omni 7230 / 1.2 / 18.4 / 19.0
- rep 2 (omni then native): native 7227 / 1.3 / 18.4 / 20.0; omni 7229 / 1.2 / 18.1 / 18.9
- rep 3 (native then omni): native 7235 / 1.2 / 20.0 / 20.0; omni 7228 / 1.3 / 18.4 / 19.0

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 8,004 tps; base rate 1,201 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v16 (digest 5c5502f12b1c0ce4, 55 files) at `611aad4666db`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 3,313 | 3,337 | +0.7% (-5.7 to +7.2) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 3,518 | 3,514 | -0.1% (-1.1 to +0.9) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 78.6 | 76.4 | -2.8% (-340.1 to +334.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 608.3 | 607.4 | -0.2% (-11.6 to +11.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.643 | 0.639 | -0.7% (-6.3 to +4.9) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 21.3 | 20.1 | -5.4% (-76.3 to +65.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 19.7 | -1.5% (-7.7 to +4.7) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.7 | +8.3% (+1.2 to +15.5) | power given |
| host CPU busy (share of the run) | 0.342 | 0.341 | -0.1% (-2.4 to +2.1) | EVEN, no difference beyond the noise |
| host CPU-seconds | 580.6 | 579.6 | -0.2% (-2.9 to +2.5) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.39 | 0.386 | -0.9% (-10.0 to +8.1) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.864 | 1.35 | +55.9% (+53.5 to +58.2) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 19.8 | -1.1% (-7.4 to +5.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 38, 26, 27; fail-ups per arm: 0, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 3256 / 112.3 / 20.0 / 20.0; omni 3374 / 2.5 / 19.1 / 19.2
- rep 2 (omni then native): native 3367 / 14.2 / 20.0 / 20.0; omni 3318 / 117.9 / 19.9 / 19.9
- rep 3 (native then omni): native 3316 / 109.4 / 20.0 / 20.0; omni 3318 / 108.9 / 20.1 / 20.2

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
