# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words every table uses (the founder's orders of 11 and 13 October).

Nobody outside The Omni-Compass LLC has checked or approved these results, so no table says "confirmed": a reading that
holds the same way in runs A, B and C, with every 95% interval clear of zero, says exactly that, "in all three of our
runs". And a reading says only which way the number went against native, **lower** or **higher**, with the gauge named
(13 October: who sets the goalposts differs from one system to the next), and the reader judges it. Every table carries OWN_RUNS. judged() tells a reader of a table (the Omni index, the dossier, the benefit
sheet, the wiring verdicts) whether a row's reading counts, for tables written in these words and for the older tables
in their own words (kept as they were written, the record).
"""

IN_ALL_THREE = "in all three of our runs"
SAME_IN_ALL_THREE = "the same in all three of our runs"
OWN_RUNS = ("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. "
            "Preregistered means the rules were written down in our own repository before the runs; nothing was filed "
            "with any outside body.")


LOWER, HIGHER = "lower", "higher"


def moved(lower: bool) -> str:
    """Which way a number went against native, in the one pair of words every table uses."""
    return LOWER if lower else HIGHER


def in_all_three(lower: bool) -> str:
    """The three-run reading of a number that went the same way in all three runs, every interval clear of zero."""
    return f"**{moved(lower)} {IN_ALL_THREE}**"


NEVER_MORE_UP = f"{HIGHER} in at least one of our runs"          # a count that should never rise (failed, lost, errors) rose
NEVER_MORE_HELD = f"{LOWER} or the same {IN_ALL_THREE}"           # ... and did not rise in any run

STACK_RULE = ("Each run holds three paired repetitions; the paired difference's 95% interval within a run, and the same sign with "
              "every interval clear of zero across the three runs, make a reading **lower** or **higher in all three of our runs** "
              "(which way the number went against native; the reader judges it); a run whose interval includes zero reads **no "
              "difference beyond the noise** (with the count of such runs); clear runs pointing different ways read **the runs "
              "disagree**.")


def never_more_rule(what: str) -> str:
    """The rule sentence for a count that should never rise."""
    return f"{what}: any rise in any run reads **{NEVER_MORE_UP}**."


def stack_reading(rs, direction, same_rel):
    """The three-run reading of one gauge of a stack's A/B/C table (PostgreSQL, Kafka, Redis, MongoDB, MySQL, the machine's
    frequency ceiling), from its three within-run paired results ({"native", "diff", "significant"}). direction is the
    gauge's declared aim, "lower" or "higher", or "never more" (a count that should never rise: any rise in any run is
    marked), or "shown" (shown, never judged). The reading says which way the number went; the reader judges it."""
    if any(r is None for r in rs):
        return "no value"
    if direction == "shown":
        return "shown, not judged"
    if direction == "never more":
        if any(r["diff"] > 0 for r in rs):
            return f"**{NEVER_MORE_UP}**"
        return "same" if all(abs(r["diff"]) <= 1e-12 for r in rs) else f"**{NEVER_MORE_HELD}**"
    if all(abs(r["diff"]) <= same_rel * max(abs(r["native"]), 1e-12) for r in rs):
        return "same"
    clear = [r for r in rs if r["significant"]]
    signs = {(r["diff"] > 0) - (r["diff"] < 0) for r in clear}
    if len(signs) > 1:
        return "**the runs disagree**"
    if len(clear) < len(rs):
        return f"no difference beyond the noise ({len(rs) - len(clear)} of {len(rs)} runs)"
    return in_all_three(rs[0]["diff"] < 0)


def aim_of(direction):
    """A gauge's declared aim from its direction in a stack's gauge list: "lower", "higher", or None (shown only)."""
    return None if direction == "shown" else (HIGHER if direction == "higher" else LOWER)


class Tally:
    """The count under a three-run table: judged rows that moved toward their gauge's declared aim, away from it, and rows
    where the runs disagree."""

    def __init__(self):
        self.toward = self.away = self.disagree = 0

    def add(self, reading, direction):
        if "disagree" in (reading or ""):
            self.disagree += 1
        aim = aim_of(direction)
        if aim is None:
            return
        t = toward_aim(reading, aim == LOWER)
        self.toward += t is True
        self.away += t is False

    def sentence(self, n, what="workloads"):
        return (f"**Across {n} {what}: {self.toward} gauge-rows moved toward the gauge's declared aim, {self.away} away from it, "
                f"{self.disagree} where the runs disagree.**")


DETERMINISTIC_RULE = ("a gauge reads **lower** or **higher in all three of our runs** (which way the number went against native; the "
                      "reader judges it) when all three runs give the same sign")
ACROSS_HEAD = "Lower in all three of our runs | Higher in all three of our runs | Same | The runs differ"
DIFFER = "**the runs differ**"


def aims_lower(direction) -> bool:
    """A gauge's declared aim is lower unless its direction says higher (or never less)."""
    return direction not in ("higher", "never less")


def across_cells(t, direction) -> str:
    """One gauge's cells under a deterministic simulator's three-run tables ({reading: [cases]}): how many cases read lower
    and how many higher in all three of our runs, the cases named in the column away from the gauge's declared aim, then
    the cases the same and the cases where the runs differ."""
    lo, hi = t.get(in_all_three(True), []), t.get(in_all_three(False), [])
    away = hi if aims_lower(direction) else lo
    cell = lambda xs: f"{len(xs)}" + (f" ({', '.join(xs)})" if xs is away and xs else "")
    return f"{cell(lo)} | {cell(hi)} | {len(t.get('same', []))} | {len(t.get(DIFFER, []))}"


def across_counts(tally, direction_of):
    """(toward, away, differ) over a simulator's tally ({key: {reading: [cases]}}): case-rows that moved toward their gauge's
    declared aim in all three of our runs, away from it, and where the runs differ. direction_of(key) gives the gauge's
    direction."""
    toward = away = differ = 0
    for k, t in tally.items():
        lo, hi = len(t.get(in_all_three(True), [])), len(t.get(in_all_three(False), []))
        low = aims_lower(direction_of(k))
        toward += lo if low else hi
        away += hi if low else lo
        differ += len(t.get(DIFFER, []))
    return toward, away, differ


def in_direction_words(reading: str, diffs) -> str:
    """A judged reading in the direction words, whatever words its table was written in: the older tables' words become
    lower or higher by the sign of the run's own differences (a judged reading has the same sign in every run)."""
    r = (reading or "").strip().strip("*")
    if not judged(r) or r.lower().startswith((LOWER, HIGHER)):
        return r
    signs = {(d > 0) - (d < 0) for d in diffs if d is not None}
    if signs == {-1}:
        return f"{LOWER} {IN_ALL_THREE}"
    if signs == {1}:
        return f"{HIGHER} {IN_ALL_THREE}"
    return r


def row_toward(v) -> bool:
    """Whether a row of an organism report (tools/six_kube_report.py) moved toward its gauge's declared aim: its field
    toward_aim, or, in the receipts written before 13 October, the field they kept for the same thing."""
    return bool(v["toward_aim"] if "toward_aim" in v else v.get("better"))


def toward_aim(reading: str, lower_is_aim: bool):
    """For the tools that score the headline (more work, faster, fewer machines, less energy): True when a judged reading
    moved the gauge toward its declared aim, False when away from it, None when the reading is not judged. Reads the
    direction words, and the older tables' words (kept as they were written)."""
    if not judged(reading):
        return None
    r = (reading or "").strip().strip("*").lower()
    if "better" in r:                       # an older table, kept as written
        return True
    if "worse" in r:
        return False
    if r.startswith(LOWER) or f"confirmed {LOWER}" in r:
        return lower_is_aim
    if r.startswith(HIGHER) or f"confirmed {HIGHER}" in r:
        return not lower_is_aim
    return None


def judged(reading: str) -> bool:
    """A reading that holds the same way in all three runs, every interval clear of zero (lower or higher, the older
    tables' words, or a robustness row held in every repetition of every run), or a count that should never rise and
    rose in a run."""
    r = (reading or "").strip().strip("*").strip()
    return r.startswith("confirmed") or IN_ALL_THREE in r or r.lower().startswith(NEVER_MORE_UP)


def with_own_runs(lines):
    """A table's lines with OWN_RUNS under its title (the legal notice is stamped around them afterwards)."""
    return list(lines[:1]) + ["", OWN_RUNS] + list(lines[1:])
