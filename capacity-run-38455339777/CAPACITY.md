# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 3,532 | 3,364 | -4.7% (-15.6% to +6.1%) | **no difference beyond the noise** | 6.0 → 6.4 | no difference beyond the noise | 1499 → 1890 | 64.5% → 65.8% |
| 1.5 | 5 | 13,500 | 8,165 | 7,886 | -3.4% (-4.6% to -2.3%) | **lower** | 10.4 → 10.4 | no difference beyond the noise | 1072 → 1131 | 25.7% → 25.2% |
| 2 | 5 | 13,500 | 7,956 | 7,754 | -2.5% (-7.5% to +2.4%) | **no difference beyond the noise** | 8.8 → 8.4 | no difference beyond the noise | 1388 → 1567 | 17.1% → 17.7% |
| 3 | 5 | 13,500 | 12,277 | 12,226 | -0.4% (-2.7% to +1.9%) | **no difference beyond the noise** | 14.4 → 15.2 | no difference beyond the noise | 539 → 551 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (-4.7%; 95% interval -15.6% to +6.1%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 6.0 → 6.4 requests a second (no difference beyond the noise). Failed or never sent: 64.5% → 65.8%.
- At 1.5 cores, Omni on top completed 278 fewer requests within 500 ms than native alone (-3.4%; 95% interval -4.6% to -2.3%, 5 pairs), reported as it stands, its cause looked for in our own wiring first. The highest load served within both limits: 10.4 → 10.4 requests a second (no difference beyond the noise). Failed or never sent: 25.7% → 25.2%.
- At 2 cores, the difference in completed work (-2.5%; 95% interval -7.5% to +2.4%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 8.8 → 8.4 requests a second (no difference beyond the noise). Failed or never sent: 17.1% → 17.7%.
- At 3 cores, the difference in completed work (-0.4%; 95% interval -2.7% to +1.9%, 5 pairs) is inside the noise: no difference beyond the noise at this cap. The highest load served within both limits: 14.4 → 15.2 requests a second (no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 9,266 → 9,044 | 8.8 → 8.0 |
| 1.5 → 2 | -417 → -266 | -3.2 → -4.0 |
| 2 → 3 | 4,321 → 4,472 | 5.6 → 6.8 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- A loss is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
