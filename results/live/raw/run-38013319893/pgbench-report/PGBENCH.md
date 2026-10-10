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

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 5,431 tps; base rate 815 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v3 (digest b53d05449ee04c4b, 40 files) at `3aac0ab7d384`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 2,318 | 2,319 | +0.0% (-2.6 to +2.7) | no difference beyond the noise |
| throughput (transactions a second) | 2,392 | 2,390 | -0.1% (-0.2 to +0.0) | no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 4.11 | 2.02 | -50.8% (-310.7 to +209.0) | no difference beyond the noise |
| latency, 99th percentile (ms) | 377.3 | 365.4 | -3.2% (-66.9 to +60.6) | no difference beyond the noise |
| latency, median (ms) | 0.669 | 0.674 | +0.7% (-3.2 to +4.6) | no difference beyond the noise |
| latency, mean (ms) | 9.94 | 9.91 | -0.3% (-94.5 to +93.8) | no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | same |
| server connections alive, mean (the machines) | 19.8 | 17.4 | -12.2% (-32.9 to +8.5) | no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | same |
| host CPU busy (share of the run) | 0.262 | 0.264 | +0.7% (-5.0 to +6.5) | no difference beyond the noise |
| host CPU-seconds | 448.7 | 451.7 | +0.7% (-5.2 to +6.5) | no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.43 | 0.433 | +0.7% (-7.9 to +9.2) | no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.756 | 1.36 | +79.7% (+61.6 to +97.7) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 17.7 | -11.4% (-29.9 to +7.1) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 52, 90, 98; fail-ups per arm: 1, 1, 1.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 2306 / 8.7 / 20.0 / 20.0; omni 2322 / 1.7 / 19.1 / 19.2
- rep 2 (omni then native): native 2331 / 1.7 / 19.5 / 20.0; omni 2303 / 2.8 / 17.2 / 17.6
- rep 3 (native then omni): native 2318 / 2.0 / 20.0 / 20.0; omni 2331 / 1.5 / 15.9 / 16.3

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
