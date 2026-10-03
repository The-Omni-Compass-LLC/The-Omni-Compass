# Governance

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE` at the root of this repository.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

Omni-Compass is owned, maintained and governed by The Omni-Compass LLC. The company decides the roadmap, accepts or
declines contributions (only under `CLA.md`), cuts releases, and holds every right in the software, its mathematics,
its documentation and its marks.

Engineering rules every change follows:
1. The frozen engine (`omnicompass/core.py`, `omnicompass/adapter.py`) and the reference engine are byte-locked; a
   change is a new version with its own proof.
2. Every Python law with a C++ twin changes in the same commit as its twin, and the seal (`results/SEAL.json`) is
   rewritten only after every parity test passes.
3. Every benchmark is preregistered before it runs; its rule decides its label.
4. `python3 verify.py` must end `VERIFICATION: PASS` on every release.
5. The manual (`docs/OMNI_COMPASS_MANUAL.md`) and the book built from it and the documents (`docs/book/build_book.py`) change in the same commit as the behavior they describe.

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
