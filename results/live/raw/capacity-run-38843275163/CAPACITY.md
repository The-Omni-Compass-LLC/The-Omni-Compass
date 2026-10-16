# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 2,420 | 2,511 | +3.8% (+0.2% to +7.3%) | **GAIN** | 4.8 → 4.8 | EVEN, no difference beyond the noise | 2277 → 2607 | 73.7% → 71.9% |
| 1.5 | 5 | 13,500 | 7,937 | 8,057 | +1.5% (-6.1% to +9.2%) | **EVEN, no difference beyond the noise** | 10.4 → 10.4 | EVEN, no difference beyond the noise | 1069 → 1270 | 30.4% → 29.2% |
| 2 | 5 | 13,500 | 9,608 | 9,545 | -0.7% (-6.9% to +5.5%) | **EVEN, no difference beyond the noise** | 11.6 → 11.6 | EVEN, no difference beyond the noise | 1014 → 1096 | 12.1% → 11.7% |
| 3 | 5 | 13,500 | 12,696 | 12,586 | -0.9% (-2.5% to +0.7%) | **EVEN, no difference beyond the noise** | 16.8 → 16.8 | EVEN, no difference beyond the noise | 406 → 451 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, Omni on top completed 91 more requests within 500 ms than native alone (+3.8%; 95% interval +0.2% to +7.3%, 5 pairs): a GAIN, more work from the same cap. The highest load served within both limits: 4.8 → 4.8 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 73.7% → 71.9%.
- At 1.5 cores, the difference in completed work (+1.5%; 95% interval -6.1% to +9.2%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 10.4 → 10.4 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 30.4% → 29.2%.
- At 2 cores, the difference in completed work (-0.7%; 95% interval -6.9% to +5.5%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 11.6 → 11.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 12.1% → 11.7%.
- At 3 cores, the difference in completed work (-0.9%; 95% interval -2.5% to +0.7%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 16.8 → 16.8 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 11,033 → 11,091 | 11.2 → 11.2 |
| 1.5 → 2 | 3,342 → 2,976 | 2.4 → 2.4 |
| 2 → 3 | 3,088 → 3,042 | 5.2 → 5.2 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity, a GAIN.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is EVEN (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
