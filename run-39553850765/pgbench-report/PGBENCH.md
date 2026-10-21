# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law writing the pool size through PgBouncer's own console inside [2, 90], handed back at the end. The load is pgbench, rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed (`docs/POSTGRES_PREREGISTRATION.md`).

## select (-S, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 15,331 tps; base rate 2,300 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 6,738 | 6,747 | +0.1% (+0.1 to +0.2) | GAIN |
| throughput (transactions a second) | 6,738 | 6,747 | +0.1% (+0.1 to +0.2) | GAIN |
| latency, 95th percentile (ms, lag included) | 0.839 | 0.835 | -0.4% (-7.0 to +6.1) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1.61 | 1.62 | +0.9% (-32.5 to +34.3) | EVEN, no difference beyond the noise |
| latency, median (ms) | 0.342 | 0.342 | -0.1% (-1.6 to +1.4) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 0.439 | 0.442 | +0.7% (-7.4 to +8.9) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 19.6 | 17.7 | -9.7% (-18.5 to -0.9) | GAIN |
| server connections alive, most at once | 20.0 | 20.0 | +0.0% (+0.0 to +0.0) | EVEN, the same |
| host CPU busy (share of the run) | 0.373 | 0.373 | +0.1% (-1.0 to +1.2) | EVEN, no difference beyond the noise |
| host CPU-seconds | 625.4 | 625.6 | +0.0% (-1.0 to +1.1) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 0.206 | 0.206 | -0.1% (-1.2 to +1.0) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 2.45 | 3.15 | +28.6% (+25.9 to +31.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 18.3 | -8.7% (-16.4 to -1.0) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 19, 21, 28; fail-ups per arm: 0, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 6740 / 0.8 / 20.0 / 20.0; omni 6748 / 0.8 / 18.3 / 18.6
- rep 2 (omni then native): native 6736 / 0.8 / 18.7 / 20.0; omni 6746 / 0.8 / 17.3 / 18.6
- rep 3 (native then omni): native 6737 / 0.8 / 20.0 / 20.0; omni 6746 / 0.9 / 17.3 / 17.5

## simple_update (-N, scale 20): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 3,676 tps; base rate 551 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 891.7 | 735.7 | -17.5% (-41.3 to +6.3) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 1,568 | 1,522 | -3.0% (-23.3 to +17.4) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 2,530 | 4,037 | +59.6% (-185.0 to +304.2) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 4,709 | 5,959 | +26.5% (-344.8 to +397.9) | EVEN, no difference beyond the noise |
| latency, median (ms) | 26.9 | 68.9 | +156.4% (-37.3 to +350.1) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 413.3 | 729.1 | +76.4% (-221.8 to +374.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | +0.2% (-0.3 to +0.7) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 21.0 | +5.0% (+5.0 to +5.0) | power given |
| host CPU busy (share of the run) | 0.273 | 0.267 | -2.3% (-24.2 to +19.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 479.8 | 470.3 | -2.0% (-23.7 to +19.7) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.22 | 1.44 | +18.1% (+9.4 to +26.9) | power given |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.818 | 1.44 | +75.9% (+64.5 to +87.3) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | +0.2% (-0.4 to +0.7) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 4, 14, 6; fail-ups per arm: 2, 4, 3.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 772 / 5771.9 / 20.0 / 20.0; omni 714 / 5316.5 / 20.0 / 20.0
- rep 2 (omni then native): native 1064 / 863.1 / 20.0 / 20.0; omni 869 / 1531.6 / 20.1 / 20.1
- rep 3 (native then omni): native 839 / 954.2 / 20.0 / 20.0; omni 624 / 5264.1 / 20.0 / 20.0

## tpcb_hot (tpcb (default), scale 2): line 50 ms, 3 paired repetitions

Native capacity, unlimited: 1,161 tps; base rate 174 tps; steps [1, 2, 3, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 1] × 30 s; 64 clients. Engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change (95% interval) | reading |
|---|---:|---:|---|---|
| work inside the response line (transactions a second answered within the line) | 292.7 | 285.4 | -2.5% (-52.5 to +47.5) | EVEN, no difference beyond the noise |
| throughput (transactions a second) | 508.0 | 504.8 | -0.6% (-5.0 to +3.8) | EVEN, no difference beyond the noise |
| latency, 95th percentile (ms, lag included) | 1,201 | 1,928 | +60.5% (-192.4 to +313.4) | EVEN, no difference beyond the noise |
| latency, 99th percentile (ms) | 1,767 | 3,147 | +78.1% (-113.3 to +269.5) | EVEN, no difference beyond the noise |
| latency, median (ms) | 27.4 | 31.2 | +13.9% (-226.5 to +254.3) | EVEN, no difference beyond the noise |
| latency, mean (ms) | 218.2 | 325.2 | +49.1% (-123.5 to +221.6) | EVEN, no difference beyond the noise |
| failed transactions | 0 | 0 | +0 (+0 to +0) | EVEN, the same |
| server connections alive, mean (the machines) | 20.0 | 20.0 | -0.1% (-0.3 to +0.1) | EVEN, no difference beyond the noise |
| server connections alive, most at once | 20.0 | 20.3 | +1.7% (-5.5 to +8.8) | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.132 | 0.131 | -0.7% (-5.1 to +3.7) | EVEN, no difference beyond the noise |
| host CPU-seconds | 233.1 | 231.7 | -0.6% (-5.6 to +4.4) | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 transactions inside the line | 1.79 | 1.83 | +2.2% (-50.6 to +54.9) | EVEN, no difference beyond the noise |
| the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's) | 0.52 | 1.05 | +101.0% (+95.6 to +106.4) | shown, not judged |
| pool size, mean (the knob) | 20.0 | 20.0 | -0.0% (-0.3 to +0.2) | shown, not judged |

The knob handed back and read back at the end of every omni arm: yes; a foreign writer seen: no; Omni's writes per arm: 4, 0, 6; fail-ups per arm: 1, 0, 0.

Per repetition (inside the line tps / p95 ms / servers alive / pool mean):

- rep 1 (native then omni): native 290 / 1130.8 / 20.0 / 20.0; omni 332 / 679.1 / 20.0 / 20.0
- rep 2 (omni then native): native 329 / 708.6 / 20.0 / 20.0; omni 257 / 1349.9 / 20.0 / 20.0
- rep 3 (native then omni): native 258 / 1764.6 / 20.0 / 20.0; omni 268 / 3754.1 / 20.0 / 20.0

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
