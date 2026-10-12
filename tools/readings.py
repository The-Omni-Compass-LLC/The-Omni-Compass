# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words every three-run table uses (the founder's order of 11 October).

Nobody outside The Omni-Compass LLC has checked or approved these results, so no table says "confirmed": a reading that
holds the same way in runs A, B and C, with every 95% interval clear of zero, says exactly that, "in all three of our
runs". Every table carries OWN_RUNS. judged() tells a reader of a table (the Omni index, the dossier, the benefit sheet,
the wiring verdicts) whether a row's reading counts, for tables written in these words and for the older tables that
still say "confirmed".
"""

IN_ALL_THREE = "in all three of our runs"
SAME_IN_ALL_THREE = "the same in all three of our runs"
OWN_RUNS = ("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. "
            "Preregistered means the rules were written down in our own repository before the runs; nothing was filed "
            "with any outside body.")


def judged(reading: str) -> bool:
    """A reading that holds the same way in all three runs, every interval clear of zero (better, worse, lower,
    higher, or a robustness row held in every repetition of every run)."""
    r = (reading or "").strip().strip("*").strip()
    return r.startswith("confirmed") or IN_ALL_THREE in r


def with_own_runs(lines):
    """A table's lines with OWN_RUNS under its title (the legal notice is stamped around them afterwards)."""
    return list(lines[:1]) + ["", OWN_RUNS] + list(lines[1:])
