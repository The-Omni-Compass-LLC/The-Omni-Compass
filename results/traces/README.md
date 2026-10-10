# Public demand traces, turned into load schedules

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Any commercial use requires a signed,
> paid Omni-Compass Enterprise License. See [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE).

The six Kubernetes tests drive the real cluster with load schedules of our own. The schedules here are derived from
demand traces somebody else published, by a rule written before the runs (`docs/TRACES_PREREGISTRATION.md`), with
`tools/trace_schedule.py`. Each folder holds the receipt (`schedule.json`: the source, every part read with its SHA-256,
the counts, the raw levels, the stepped schedule, the rule) and the one line the workflow takes (`LOAD_STEPS.txt`).
Anyone can re-derive a folder with the tool; the parts are public and the rule is deterministic.

| Folder | Source | What is counted | Schedule |
|---|---|---|---|
| `google2011/` | Google cluster-usage traces 2011 (`clusterdata-2011-2`, `job_events`), the trace's first day | jobs submitted an hour, 24 hours | 24 steps of 108 s, load generators 1 to 8 by min and max, one step a bin |

The parts themselves (about 0.8 MB each) are not kept here; the tool downloads them into a cache and records their
SHA-256 in the receipt.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass
Enterprise License. All patents, copyrights and trademarks filed in the USA. All rights reserved. Subject to change at any time.
