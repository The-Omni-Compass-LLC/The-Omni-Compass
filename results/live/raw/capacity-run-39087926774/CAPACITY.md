# The capacity test: native and Omni-Compass on top at the same resource cap

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted). The cap is a quota on the served app's CPU (the same in both arms, enforced by the cluster, not by either controller); the load rises step by step past what the cap can serve, the same requests in both arms. **Completed work**: requests answered within the response-time line over the whole window. **Capacity**: the highest offered rate served while at least 95% of a step's requests are answered within the line and no more than 1% fail or are never sent. Paired within one job (both arms on one runner, order rotated).

| Cap (cores) | Pairs | Offered (requests) | Completed, native | Completed, Omni on top | Difference | Reading | Capacity, native → Omni (req/s) | Capacity reading | p95, native → Omni (ms) | Failed or not sent, native → Omni |
|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | 5 | 13,500 | 4,722 | 4,954 | +4.9% (-23.1% to +33.0%) | **EVEN, no difference beyond the noise** | 7.2 → 7.6 | EVEN, no difference beyond the noise | 1826 → 1226 | 53.3% → 53.4% |
| 1.5 | 5 | 13,500 | 6,193 | 5,855 | -5.5% (-14.5% to +3.6%) | **EVEN, no difference beyond the noise** | 8.0 → 7.6 | EVEN, no difference beyond the noise | 1294 → 1428 | 38.6% → 38.1% |
| 2 | 5 | 13,500 | 10,103 | 9,563 | -5.3% (-12.1% to +1.4%) | **EVEN, no difference beyond the noise** | 12.8 → 13.2 | EVEN, no difference beyond the noise | 881 → 1047 | 10.0% → 13.8% |
| 3 | 5 | 13,500 | 11,149 | 11,045 | -0.9% (-2.8% to +1.0%) | **EVEN, no difference beyond the noise** | 11.6 → 11.6 | EVEN, no difference beyond the noise | 858 → 873 | 0.0% → 0.0% |

**The audit lines** (one per row, in plain words):

- At 1 core, the difference in completed work (+4.9%; 95% interval -23.1% to +33.0%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 7.2 → 7.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 53.3% → 53.4%.
- At 1.5 cores, the difference in completed work (-5.5%; 95% interval -14.5% to +3.6%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 8.0 → 7.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 38.6% → 38.1%.
- At 2 cores, the difference in completed work (-5.3%; 95% interval -12.1% to +1.4%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 12.8 → 13.2 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 10.0% → 13.8%.
- At 3 cores, the difference in completed work (-0.9%; 95% interval -2.8% to +1.0%, 5 pairs) is inside the noise: EVEN, no difference beyond the noise at this cap. The highest load served within both limits: 11.6 → 11.6 requests a second (EVEN, no difference beyond the noise). Failed or never sent: 0.0% → 0.0%.

## Each step up in the cap: what one more core gives each arm

| Cap step (cores) | Completed work per added core, native → Omni | Capacity per added core, native → Omni (req/s) |
|---|---|---|
| 1 → 1.5 | 2,942 → 1,803 | 1.6 → 0.0 |
| 1.5 → 2 | 7,821 → 7,416 | 9.6 → 11.2 |
| 2 → 3 | 1,046 → 1,482 | -1.2 → -1.6 |

Where Omni's figure is the higher, Omni turns each added core into more completed work than native does; where both are the same, the added core is used alike.

## How to read a row

- **Both arms served everything offered** (the cap never reached): the row shows speed, not more work. A run with a fixed offered load, served in full by both arms, can only show faster service for that load (the KEDA add-on run of 12 October: CPU used +32%, 95th-percentile response -55%, the same six workers; faster service for the same work, not yet more completed work).
- **The cap holds native back** (native leaves offered requests unanswered within the line): a higher count for Omni on top at the same cap is more work from the same capacity, a GAIN.
- **Each step up in the cap**: if both arms do more as the cap rises, the step table shows which turns each added core into more completed work.
- Completed work and capacity are work done, so a rise is GAIN and a fall is LOSS; inside the noise is EVEN (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A LOSS is reported as it stands; its cause is looked for in our own wiring, setup and scoring first.

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
