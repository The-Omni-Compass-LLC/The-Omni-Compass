# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 3,222 | 3,270 | +1.5% (-14.3% to +17.3%) | **EVEN, no difference beyond the noise** | 5.6 → 5.2 | EVEN, no difference beyond the noise | 2006 → 1880 | 66.6% → 67.5% |
| 1.5 | 5 | 13,500 | 5,044 | 4,957 | -1.7% (-9.1% to +5.7%) | **EVEN, no difference beyond the noise** | 7.2 → 6.8 | EVEN, no difference beyond the noise | 1734 → 1503 | 44.7% → 46.5% |
| 2 | 5 | 13,500 | 9,635 | 9,457 | -1.9% (-8.8% to +5.1%) | **EVEN, no difference beyond the noise** | 12.0 → 12.0 | EVEN, no difference beyond the noise | 1031 → 1096 | 12.4% → 12.6% |
| 3 | 5 | 13,500 | 11,742 | 11,702 | -0.3% (-1.2% to +0.6%) | **EVEN, no difference beyond the noise** | 13.2 → 13.2 | EVEN, no difference beyond the noise | 660 → 653 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (+1.5%; 95% interval -14.3% to +17.3%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 5.6 → 5.2 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 66.6% → 67.5%.
- At 1.5 cores, the difference in completed work (-1.7%; 95% interval -9.1% to +5.7%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 7.2 → 6.8 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 44.7% → 46.5%.
- At 2 cores, the difference in completed work (-1.9%; 95% interval -8.8% to +5.1%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 12.0 → 12.0 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 12.4% → 12.6%.
- At 3 cores, the difference in completed work (-0.3%; 95% interval -1.2% to +0.6%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 13.2 → 13.2 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 3,644 → 3,374 | 3.2 → 3.2 |
| 1.5 → 2 | 9,183 → 8,999 | 9.6 → 10.4 |
| 2 → 3 | 2,106 → 2,245 | 1.2 → 1.2 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity, a GAIN.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is EVEN (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
