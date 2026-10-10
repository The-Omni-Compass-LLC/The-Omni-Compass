# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""The legal notice every generated report carries, at its top and at its end: one wording, written once."""

NOTICE = ("© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial "
          "use, commercialization, monetization, production use, redistribution or hosted service of any part of "
          "Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. All patents, "
          "copyrights and trademarks filed in the USA. Everything in this repository is subject to change at any time; "
          "www.omni-compass.com is the authority of record. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.")
# the founder's wording of 10 October 2026: "all" before patents, copyrights and trademarks; all rights reserved; subject to
# change at any time; the website the authority of record. Every generated report carries it at its top and at its end.
MARK = "© 2026 The Omni-Compass LLC"      # a report carrying this already carries the notice (in this or an earlier wording)


def stamp(lines):
    """A report's lines with the notice under its title and again at its end (a report that already carries it is
    returned unchanged)."""
    lines = list(lines)
    if any(MARK in x for x in lines):
        return lines
    head = 1 if lines and lines[0].startswith("#") else 0
    return lines[:head] + ["", f"> {NOTICE}", ""] + lines[head:] + ["", "---", "", f"*{NOTICE}*"]
