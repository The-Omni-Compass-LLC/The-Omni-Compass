# Kafka: Omni-Compass on top of a consumer group's operator-set size

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Apache Kafka as shipped (one broker, a topic of 8 partitions); native: the consumer group at the operator's count (2); omni: the compass law on the consumer count inside [1, 8], holding the group's own end-to-end latency at 40% of the 500 ms line. The same offered load in both arms. Energy is the host's CPU seconds, the compass's own cost included. Every row is reported, losses included.

## heavy: 5.0 ms of work a message, 1024 B, steps 1 2 3 2 3 4 5 6 5 4 3 2 1 2 1 × 30.0 s

Native capacity 394 messages a second; base rate 59.1/s; 3 paired repetitions; engine omni-v12 (digest d38b58fbe28939b8, 47 files) at `690b955b1c2a`.

| Gauge | native | omni | change | 95% interval of the difference | reading |
|---|---:|---:|---:|---:|---|
| work inside the response line (messages a second handled within the line) | 147 | 147 | -0.1% | -1.07 to 0.666 | EVEN, no difference beyond the noise |
| throughput (messages a second consumed) | 173 | 173 | -0.0% | -0.00183 to -8.62e-05 | LOSS |
| end-to-end latency, 95th percentile (ms) | 2,519 | 2,528 | +0.3% | -233 to 250 | EVEN, no difference beyond the noise |
| end-to-end latency, 99th percentile (ms) | 3,949 | 3,918 | -0.8% | -407 to 346 | EVEN, no difference beyond the noise |
| end-to-end latency, median (ms) | 11.7 | 11.8 | +0.4% | -0.105 to 0.199 | EVEN, no difference beyond the noise |
| end-to-end latency, mean (ms) | 342 | 346 | +1.0% | -26.9 to 33.5 | EVEN, no difference beyond the noise |
| consumer lag, most messages waiting at once | 720 | 732 | +1.7% | -26.7 to 50.7 | EVEN, no difference beyond the noise |
| consumer lag, mean messages waiting | 62.8 | 63.5 | +1.1% | -5.56 to 6.93 | EVEN, no difference beyond the noise |
| messages produced and never consumed | 0 | 0 |  | 0 to 0 | EVEN, the same |
| consumers running, mean (the resources held) | 2 | 1.99 | -0.3% | -0.00665 to -0.00665 | GAIN |
| consumers running, most at once | 2 | 2 | +0.0% | 0 to 0 | EVEN, the same |
| host CPU busy (share of the run) | 0.29 | 0.292 | +0.7% | -0.0095 to 0.0135 | EVEN, no difference beyond the noise |
| host CPU-seconds | 510 | 514 | +0.8% | -15.9 to 23.6 | EVEN, no difference beyond the noise |
| host CPU-seconds per 1,000 messages inside the line | 7.7 | 7.77 | +0.9% | -0.222 to 0.359 | EVEN, no difference beyond the noise |
| consumer changes written (the knob's moves) | 2 | 4 | +100.0% | 2 to 2 | shown, not judged |

Every omni arm handed back to the operator's count: yes; fail-ups: 3.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
