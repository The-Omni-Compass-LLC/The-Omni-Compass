# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 4,821 | 4,635 | -3.9% (-10.1% to +2.4%) | **EVEN, no difference beyond the noise** | 8.0 → 7.2 | EVEN, no difference beyond the noise | 1812 → 1804 | 55.2% → 54.8% |
| 1.5 | 4 | 13,500 | 6,796 | 6,896 | +1.5% (-4.7% to +7.6%) | **EVEN, no difference beyond the noise** | 9.5 → 9.0 | EVEN, no difference beyond the noise | 1138 → 1251 | 37.0% → 34.7% |
| 2 | 5 | 13,500 | 11,007 | 11,010 | +0.0% (-1.9% to +1.9%) | **EVEN, no difference beyond the noise** | 15.2 → 15.6 | EVEN, no difference beyond the noise | 706 → 649 | 7.8% → 8.1% |
| 3 | 5 | 13,500 | 11,266 | 11,309 | +0.4% (-3.3% to +4.0%) | **EVEN, no difference beyond the noise** | 12.8 → 12.8 | EVEN, no difference beyond the noise | 773 → 780 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (-3.9%; 95% interval -10.1% to +2.4%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 8.0 → 7.2 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 55.2% → 54.8%.
- At 1.5 cores, the difference in completed work (+1.5%; 95% interval -4.7% to +7.6%, 4 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 9.5 → 9.0 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 37.0% → 34.7%.
- At 2 cores, the difference in completed work (+0.0%; 95% interval -1.9% to +1.9%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 15.2 → 15.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 7.8% → 8.1%.
- At 3 cores, the difference in completed work (+0.4%; 95% interval -3.3% to +4.0%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 12.8 → 12.8 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 3,950 → 4,522 | 3.0 → 3.6 |
| 1.5 → 2 | 8,423 → 8,228 | 11.4 → 13.2 |
| 2 → 3 | 259 → 299 | -2.4 → -2.8 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity, a GAIN.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is EVEN (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
