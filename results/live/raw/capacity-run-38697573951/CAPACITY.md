# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 3,745 | 4,064 | +8.5% (-11.2% to +28.3%) | **EVEN, no difference beyond the noise** | 6.4 → 6.4 | EVEN, no difference beyond the noise | 1644 → 1636 | 62.8% → 59.9% |
| 1.5 | 5 | 13,500 | 9,259 | 9,283 | +0.3% (-2.3% to +2.8%) | **EVEN, no difference beyond the noise** | 11.6 → 12.0 | EVEN, no difference beyond the noise | 1020 → 1034 | 18.1% → 18.6% |
| 2 | 5 | 13,500 | 11,244 | 11,316 | +0.6% (-1.3% to +2.6%) | **EVEN, no difference beyond the noise** | 14.4 → 14.0 | EVEN, no difference beyond the noise | 651 → 653 | 5.4% → 4.7% |
| 3 | 5 | 13,500 | 11,475 | 11,339 | -1.2% (-3.4% to +1.1%) | **EVEN, no difference beyond the noise** | 12.4 → 11.6 | EVEN, no difference beyond the noise | 766 → 779 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (+8.5%; 95% interval -11.2% to +28.3%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 6.4 → 6.4 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 62.8% → 59.9%.
- At 1.5 cores, the difference in completed work (+0.3%; 95% interval -2.3% to +2.8%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 11.6 → 12.0 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 18.1% → 18.6%.
- At 2 cores, the difference in completed work (+0.6%; 95% interval -1.3% to +2.6%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 14.4 → 14.0 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 5.4% → 4.7%.
- At 3 cores, the difference in completed work (-1.2%; 95% interval -3.4% to +1.1%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 12.4 → 11.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 11,027 → 10,437 | 10.4 → 11.2 |
| 1.5 → 2 | 3,971 → 4,067 | 5.6 → 4.0 |
| 2 → 3 | 231 → 23 | -2.0 → -2.4 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity, a GAIN.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is EVEN (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
