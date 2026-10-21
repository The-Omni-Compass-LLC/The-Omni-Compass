# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## light: 1.0 ms of work a message, 128 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 1943 messages a second; base rate 291.5/s; 3 paired repetitions; engine omni-v13 (digest 0088837333c6f0fc, 47 files) at `3915d40f57d8`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 729 | 725 | -0.5% | -18.8 to 10.9 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 855 | 855 | -0.0% | -0.0152 to 0.00803 | EVEN, no difference beyond the noise |
| end-to-end latency, 95th percentile (ms) | 2,380 | 3,149 | +32.4% | -2,134 to 3,674 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,708 | 4,629 | +24.9% | -2,914 to 4,757 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 7.38 | 7.43 | +0.8% | -0.334 to 0.448 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 318 | 412 | +29.4% | -267 to 454 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 3,325 | 4,017 | +20.8% | -1,873 to 3,257 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 277 | 358 | +29.2% | -227 to 389 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00909 to -0.00273 | GAIN |
| consumers running, most at once | 2 | 2.33 | +16.7% | -1.1 to 1.77 | EVEN, no difference beyond the noise |
| host CPU busy (share of the run) | 0.312 | 0.312 | +0.0% | -0.00704 to 0.00722 | EVEN, no difference beyond the noise |
| host CPU-seconds | 554 | 555 | +0.2% | -11.8 to 14 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 1.69 | 1.7 | +0.7% | 0.00822 to 0.0171 | power given |
| consumer changes written (the knob's moves) | 2 | 4.67 | +133.3% | -0.202 to 5.54 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
