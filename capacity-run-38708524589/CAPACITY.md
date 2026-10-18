# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 5,548 | 5,818 | +4.9% (-35.0% to +44.7%) | **EVEN, no difference beyond the noise** | 8.8 → 8.4 | EVEN, no difference beyond the noise | 1346 → 1463 | 47.0% → 43.4% |
| 1.5 | 5 | 13,500 | 6,350 | 6,181 | -2.7% (-9.7% to +4.4%) | **EVEN, no difference beyond the noise** | 8.8 → 8.0 | EVEN, no difference beyond the noise | 1294 → 1228 | 35.6% → 36.7% |
| 2 | 5 | 13,500 | 10,081 | 9,985 | -1.0% (-2.9% to +1.0%) | **EVEN, no difference beyond the noise** | 12.0 → 12.4 | EVEN, no difference beyond the noise | 826 → 912 | 7.2% → 9.3% |
| 3 | 5 | 13,500 | 12,103 | 12,016 | -0.7% (-2.6% to +1.2%) | **EVEN, no difference beyond the noise** | 14.4 → 13.6 | EVEN, no difference beyond the noise | 599 → 666 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (+4.9%; 95% interval -35.0% to +44.7%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 8.8 → 8.4 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 47.0% → 43.4%.
- At 1.5 cores, the difference in completed work (-2.7%; 95% interval -9.7% to +4.4%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 8.8 → 8.0 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 35.6% → 36.7%.
- At 2 cores, the difference in completed work (-1.0%; 95% interval -2.9% to +1.0%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 12.0 → 12.4 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 7.2% → 9.3%.
- At 3 cores, the difference in completed work (-0.7%; 95% interval -2.6% to +1.2%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 14.4 → 13.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 1,604 → 725 | 0.0 → -0.8 |
| 1.5 → 2 | 7,464 → 7,608 | 6.4 → 8.8 |
| 2 → 3 | 2,021 → 2,031 | 2.4 → 1.2 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity, a GAIN.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is EVEN (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
