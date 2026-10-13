# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 2,440 | 2,331 | -4.4% (-11.0% to +2.1%) | **no difference beyond the noise** | 4.8 → 4.4 | no difference beyond the noise | 1982 → 2175 | 73.8% → 74.8% |
| 1.5 | 5 | 13,500 | 7,472 | 7,303 | -2.3% (-10.2% to +5.7%) | **no difference beyond the noise** | 9.2 → 10.0 | no difference beyond the noise | 1257 → 1125 | 28.0% → 32.2% |
| 2 | 5 | 13,500 | 10,477 | 10,671 | +1.9% (-2.2% to +5.9%) | **no difference beyond the noise** | 13.6 → 14.0 | no difference beyond the noise | 787 → 781 | 8.3% → 7.8% |
| 3 | 5 | 13,500 | 12,299 | 12,102 | -1.6% (-4.3% to +1.1%) | **no difference beyond the noise** | 14.4 → 14.0 | no difference beyond the noise | 591 → 606 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (-4.4%; 95% interval -11.0% to +2.1%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 4.8 → 4.4 requests a second (no difference beyond the noise). Failed or never sent: 73.8% → 74.8%.
- At 1.5 cores, the difference in completed work (-2.3%; 95% interval -10.2% to +5.7%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 9.2 → 10.0 requests a second (no difference beyond the noise). Failed or never sent: 28.0% → 32.2%.
- At 2 cores, the difference in completed work (+1.9%; 95% interval -2.2% to +5.9%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 13.6 → 14.0 requests a second (no difference beyond the noise). Failed or never sent: 8.3% → 7.8%.
- At 3 cores, the difference in completed work (-1.6%; 95% interval -4.3% to +1.1%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 14.4 → 14.0 requests a second (no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 10,065 → 9,944 | 8.8 → 11.2 |
| 1.5 → 2 | 6,009 → 6,734 | 8.8 → 8.0 |
| 2 → 3 | 1,822 → 1,431 | 0.8 → 0.0 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- A loss is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
