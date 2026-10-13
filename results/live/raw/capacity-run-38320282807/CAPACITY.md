# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 3,729 | 3,828 | +2.6% (-10.5% to +15.8%) | **no difference beyond the noise** | 6.4 → 6.4 | no difference beyond the noise | 1918 → 2116 | 61.6% → 60.7% |
| 1.5 | 5 | 13,500 | 6,363 | 5,954 | -6.4% (-13.5% to +0.6%) | **no difference beyond the noise** | 8.0 → 7.6 | no difference beyond the noise | 1445 → 1250 | 33.1% → 36.8% |
| 2 | 5 | 13,500 | 10,861 | 11,271 | +3.8% (-8.8% to +16.3%) | **no difference beyond the noise** | 12.4 → 12.8 | no difference beyond the noise | 780 → 726 | 5.5% → 3.8% |
| 3 | 5 | 13,500 | 11,911 | 11,837 | -0.6% (-2.2% to +1.0%) | **no difference beyond the noise** | 14.4 → 14.0 | no difference beyond the noise | 651 → 651 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (+2.6%; 95% interval -10.5% to +15.8%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 6.4 → 6.4 requests a second (no difference beyond the noise). Failed or never sent: 61.6% → 60.7%.
- At 1.5 cores, the difference in completed work (-6.4%; 95% interval -13.5% to +0.6%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 8.0 → 7.6 requests a second (no difference beyond the noise). Failed or never sent: 33.1% → 36.8%.
- At 2 cores, the difference in completed work (+3.8%; 95% interval -8.8% to +16.3%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 12.4 → 12.8 requests a second (no difference beyond the noise). Failed or never sent: 5.5% → 3.8%.
- At 3 cores, the difference in completed work (-0.6%; 95% interval -2.2% to +1.0%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 14.4 → 14.0 requests a second (no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 5,267 → 4,253 | 3.2 → 2.4 |
| 1.5 → 2 | 8,996 → 10,634 | 8.8 → 10.4 |
| 2 → 3 | 1,050 → 566 | 2.0 → 1.2 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- A loss is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
