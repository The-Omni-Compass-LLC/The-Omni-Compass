# Nervous system

> **PROPRIETARY - EVALUATION AND SIMULATION USE ONLY.** Copyright (c) 2026 The Omni-Compass LLC. This is not open-source software (`SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`). Any commercial use, commercialization, monetization, production use, redistribution, hosted service or incorporation into a product requires a signed, paid **Omni-Compass Enterprise License** from The Omni-Compass LLC. Protected by copyright, patents and trademarks: All patent applications, copyright registrations and trademark applications covering the Omni-Compass engine, its mathematics and its software have been filed in the United States by The Omni-Compass LLC. See [`LICENSE`](../LICENSE).

Omni-Compass is one field. Muscles are nerves.

```
telemetry  ->  afferent (per muscle)
           ->  one six-state engine
           ->  reflex (shield)
           ->  efferent (only WIRED + authority + not killed)
           ->  native controller on kill
```

`omnicompass/nervous.py` is the register. It does not invent GPU or chiller physics.

| Status | Meaning |
|---|---|
| wired | this tree can sense and push |
| sensed | this tree can sense; it does not push |
| open | named, no plant, no push |

Wired today: `nodes`, `hpa`, `power_cap`.  
Sensed: `heat`, `network`, `security`.  
Open: GPU, cooling, grid, queues, agents, …  
Never a muscle: value alignment.

```bash
python k8s_controlplane/test_nervous.py
```

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
All patent applications, copyright registrations and trademark applications filed in the United States. All rights reserved. Everything in this repository is subject to change at any time; www.omni-compass.com is the authority of record. See `LICENSE` and
`NOTICE` at the root of this repository.*
