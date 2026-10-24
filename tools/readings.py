# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words every table uses: GAIN, EVEN and LOSS (the founder's order of 13 October 2026, night).

Better, same and worse became GAIN, EVEN and LOSS wherever they lived, and where they used to live. A reading is never
decided by the plus or minus sign of its number: it is decided by what the gauge is for, its declared aim. A response time
that fell is a GAIN; work that fell is a LOSS; a bill, an energy draw or a count of machines that fell is a cut, and a cut
is a GAIN; a resource that rose to buy work or speed is power given (the founder's order of 12 October), shown beside what
it bought and never called a loss. KEY says what each word means, letter by letter, and why it was chosen; it stands at
the front of the manual, in the README, in docs/HOW_TO_READ_THE_RESULTS.md and in the summary anyone prints after pulling
the repository (python3 tools/summary.py). This module is the one place the words are written.

Nobody outside The Omni-Compass LLC has checked or approved these results, so no table says "confirmed": a reading that
moved 0.5% or more the same way in runs A, B and C, with every 95% interval clear of zero, says "in all three of our runs";
a change of 0.5% or more that holds its direction but not that strictly still shows its word, with the count of runs clear
of the noise beside it (judge_runs, the founder's order of 24 October 2026); and every table carries OWN_RUNS. classify() reads a reading in any words the repository has used (GAIN/EVEN/LOSS; lower and higher
of 13 October; toward and away; better, worse and "confirmed" of the older tables) so every scorer reads every table alike.

  python3 tools/readings.py --key      the key, as plain text
  python3 tools/readings.py --check    exit 1 if a page that must carry the key does not carry it word for word
  python3 tools/readings.py --fix      write the key into those pages, and "How to read this receipt" into every standing table
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GAIN, EVEN, LOSS = "GAIN", "EVEN", "LOSS"
GIVEN = "power given"                       # a resource spent or held rose: shown beside what it bought, never a LOSS
DISAGREE = "the runs disagree"              # runs clear of the noise point different ways: the test is unstable there
DIFFER = "**the runs differ**"              # a deterministic simulator's runs did not reproduce
SHOWN = "shown, not judged"                 # declared in advance as shown only
IN_ALL_THREE = "in all three of our runs"
SAME_IN_ALL_THREE = "the same in all three of our runs"
OWN_RUNS = ("Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. "
            "Preregistered means the rules were written down in our own repository before the runs; nothing was filed "
            "with any outside body.")

# ------------------------------------------------------------------------------------------------- what a gauge is for
# A gauge's declared aim, as each preregistration writes it:
LOWER = "lower"              # an amount waited, missed or failed (a response time, time over the line): a fall is GAIN, a rise LOSS
HIGHER = "higher"            # work done (work inside the line, throughput, a hit rate): a rise is GAIN, a fall LOSS
SPENT = "spent"              # a resource spent or held (energy, power and its peaks, machines, memory, processor time, a bill, wear): a fall is a
                             # cut, and a cut is GAIN; a rise is power given
NEVER_MORE = "never more"    # a count that must never rise (failed requests, lost messages): any rise in any run is LOSS
NEVER_LESS = "never less"    # a count that must never fall
SHOWN_AIM = "shown"          # shown, never judged
WORK_PER = "work per resource"   # work bought with each unit of a resource (work per energy): a rise is a cut in what each unit
                                 # of work took, a GAIN; a fall is power given (17 October: it falls when more power is given)

# The gauges of a resource spent or held, by the names the tables and the runners give them. A table written before this
# module knew the word "spent" declared them "lower"; aim() reads them as spent wherever they are named.
SPENT_GAUGES = frozenset({
    # Kubernetes (tools/live_reps.py, pilot/bench_report.py)
    "worker nodes in service, mean", "node-hours", "power (W), mean", "power (W), peak", "energy (Wh)",
    "energy, parked workers still on at idle power (Wh)", "energy, the machine's own meter (Wh)", "node-hours per core-hour",
    "HPA replicas, mean", "pods started", "batch: worker machines in service after the queue finished, mean",
    "machines billed, machine-hours", "compute bill at list price ($)",
    # the organisms with the cluster inside (tools/six_kube_report.py)
    "organism energy (J)",
    # the stacks (tools/run_*.py)
    "servers_alive_mean", "servers_alive_max", "consumers_mean", "consumers_max", "maxmemory_mb_mean", "used_mb_mean",
    "cache_mb_mean", "cache_used_mb_mean", "pool_mb_mean", "pool_used_mb_mean", "cpu_busy_share", "cpu_seconds",
    "cpu_s_per_1k_inside", "energy_j", "power_w_mean", "j_per_1k_inside", "wall_j",
    # the independent simulators (pandapower, MuJoCo, the swarms, CityLearn)
    "load_energy_mwh", "losses_mwh", "energy_in_mwh", "tap_operations", "copper_j", "mechanical_j", "standing_j",
    "peak_torque_nm", "mean_abs_torque_nm", "energy_per_mission_j", "fleet_energy_j", "cost_total",
    "electricity_consumption_total", "carbon_emissions_total", "zero_net_energy",
    # CityLearn's peaks, swings and unevenness are the power the district holds from the grid and the wear of moving it, as a
    # Kubernetes cluster's peak power is above (the founder's order of 17 October: one key for every gauge)
    "all_time_peak_average", "daily_peak_average", "ramping_average", "monthly_one_minus_load_factor_average",
    "daily_one_minus_load_factor_average",
    # the Omni index's own measures
    "machines", "energy",
})


def aim(direction, key=None):
    """A gauge's aim from its declared direction: LOWER, HIGHER, SPENT, NEVER_MORE, NEVER_LESS, or None (shown only). A
    gauge declared "lower" whose name is a resource spent or held (SPENT_GAUGES) is SPENT."""
    if direction in (None, SHOWN_AIM, "shown, not judged"):
        return None
    if direction == LOWER and key in SPENT_GAUGES:
        return SPENT
    return direction


aim_of = aim


def word(fell: bool, aim_: str) -> str:
    """The word for a number that went the same way in all three runs (fell, or rose), judged by the gauge's aim, never by
    its sign: GAIN, LOSS, or power given."""
    if aim_ in (HIGHER, NEVER_LESS):
        return LOSS if fell else GAIN
    if aim_ == SPENT:
        return GAIN if fell else GIVEN
    if aim_ == WORK_PER:
        return GIVEN if fell else GAIN
    return GAIN if fell else LOSS                     # lower, never more


SIZE_FLOOR = 0.005           # the founder's floor (20 October 2026; 24 October: a change of 0.5% or more either way is a change and
                             # shows its word): under half of one percent either way, in every run, reads EVEN; from 0.5% up it is a change
EVEN_FLOOR = f"{EVEN}, under the floor"              # every run's change under SIZE_FLOOR
CLEAR_OF_NOISE = "clear of the noise"                # a run whose 95% interval of the paired difference excludes zero
SIGN_OF = {GAIN: "+", LOSS: "−", EVEN: "="}          # the number beside a word carries the word's sign, never the gauge's raw direction (20 October)
_COUNT = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}


def even_floor(size: float) -> str:
    """The reading of a gauge whose change was under the floor in every run."""
    return f"{EVEN_FLOOR} (every run under {100 * SIZE_FLOOR:g}%; the largest {100 * size:.2f}%)"


def in_all_three(fell: bool, aim_: str, size: float | None = None) -> str:
    """The three-run reading of a number that went the same way in all three runs, every run at or above the floor and every
    interval clear of zero. size, where the caller has it, is the largest run's relative change: under the founder's floor in every
    run the reading is EVEN, under the floor. judge_runs() is the whole rule; this is its strictest case."""
    if size is not None and size < SIZE_FLOOR:
        return even_floor(size)
    return f"**{word(fell, aim_)} {IN_ALL_THREE}**"


def rel_change(native, diff) -> float:
    """A run's paired change as a share of native, signed (omni − native) / |native|; where native is zero, an arm that moved is
    an unbounded change (±inf) and one that did not is 0.0."""
    if native:
        return diff / abs(native)
    return 0.0 if not diff else math.copysign(math.inf, diff)


def judge_runs(changes, clear, aim_) -> str:
    """The one rule for a gauge read over several runs (the founder's order of 24 October 2026: "Any gauge that gives anything
    over a 0.5 percent change either way is a change ... it has to show its loss or gain"). Every tool that decides a word over
    runs calls it.

    changes: each run's paired change as a share of native, signed (rel_change); the sign is omni against native.
    clear:   each run's 95% interval of the paired difference clear of zero (True or False), or None where the runs carry no
             interval (a deterministic simulator, whose runs reproduce exactly).
    aim_:    what the gauge is for (LOWER, HIGHER, SPENT, WORK_PER, NEVER_MORE, NEVER_LESS), or None for a gauge shown only.

    1. Every run under SIZE_FLOOR (0.5%) either way: EVEN, under the floor. (EVEN, the same is the caller's own measure of no
       change at all, read before this.)
    2. Otherwise only the runs that moved 0.5% or more decide the direction. All the same way: the gauge's word by its aim
       (GAIN, LOSS, or power given for a resource spent that rose; a cut of a resource spent is GAIN), whatever the intervals say.
       All runs moved 0.5% or more the same way with every interval clear of zero: "**GAIN in all three of our runs**", as
       before; else the word stands and its qualifier follows in the same cell, the noise count always shown: "**GAIN** (the same
       way in all three runs; 2 of 3 clear of the noise)", "**LOSS** (2 of 3 runs moved 0.5% or more, the same way, 1 under the
       floor; 1 of 3 clear of the noise)".
    3. The runs that moved 0.5% or more point different ways: the runs disagree.
    A count that must never rise (NEVER_MORE) keeps its strict rule: any rise in any run reads LOSS. The count of runs clear of
    the noise always stands beside a word that is not in all three of our runs."""
    if aim_ is None:
        return SHOWN
    changes = [float(c) for c in changes]
    n = len(changes)
    if aim_ == NEVER_MORE:
        if clear is None and n and all(c > 0 for c in changes):       # a deterministic simulator's runs reproduce: all three rose
            return f"**{LOSS} {IN_ALL_THREE}**"
        if any(c > 0 for c in changes):
            return f"**{NEVER_MORE_UP}**"
        if clear is None and n and all(c < 0 for c in changes):
            return f"**{GAIN} {IN_ALL_THREE}**"
        return EVEN_SAME if all(c == 0 for c in changes) else f"**{NEVER_MORE_HELD}**"
    sizes = [abs(c) for c in changes]
    movers = [i for i, s in enumerate(sizes) if s >= SIZE_FLOOR]
    if not movers:
        return even_floor(max(sizes) if sizes else 0.0)
    ways = {changes[i] > 0 for i in movers}
    if len(ways) > 1:
        return f"**{DISAGREE}**"
    fell = ways == {False}
    w = word(fell, aim_)
    nn = _COUNT.get(n, str(n))
    if len(movers) == n:
        moved = f"the same way in all {nn} runs"
    elif len(movers) == 1:
        moved = f"1 of {n} runs moved {100 * SIZE_FLOOR:g}% or more, {n - 1} under the floor"
    else:
        moved = f"{len(movers)} of {n} runs moved {100 * SIZE_FLOOR:g}% or more, the same way, {n - len(movers)} under the floor"
    if clear is None:                                   # a deterministic simulator: the runs reproduce, no interval to read
        if len(movers) == n:
            return f"**{w} {IN_ALL_THREE}**" if n == 3 else f"**{w} in all {nn} of our runs**"
        return f"**{w}** ({moved}; no interval: the runs reproduce exactly)"
    k = sum(1 for c, ok in zip(changes, clear) if ok and c != 0 and (c < 0) == fell)
    if len(movers) == n and k == n:
        return f"**{w} {IN_ALL_THREE}**" if n == 3 else f"**{w} in all {nn} of our runs**"
    return f"**{w}** ({moved}; {k} of {n} {CLEAR_OF_NOISE})"


def judge_one(change, clear, aim_) -> str:
    """The same rule for one paired comparison (one run, or a model's seeds paired with the engine that stands): under the floor
    EVEN, under the floor; from 0.5% up the gauge's word by its aim, and "(not clear of the noise)" after it where the 95% interval
    includes zero. clear None: no interval (a deterministic comparison)."""
    if aim_ is None:
        return SHOWN
    c = float(change)
    if aim_ == NEVER_MORE:
        return LOSS if c > 0 else EVEN_SAME if c == 0 else GAIN
    if abs(c) < SIZE_FLOOR:
        return f"{EVEN_FLOOR} ({100 * abs(c):.2f}%, under {100 * SIZE_FLOOR:g}%)"
    w = word(c < 0, aim_)
    return w if (clear or clear is None) else f"{w} (not {CLEAR_OF_NOISE})"


def plain(reading) -> str:
    """A reading without its Markdown emphasis, as the tables' JSON twins keep it."""
    return (reading or "").replace("**", "").strip()


def bare_word(reading) -> str:
    """A reading's word alone, its qualifier dropped, for a page that colours a cell by its word: GAIN, LOSS, power given,
    EVEN, under the floor, EVEN, the same, the runs disagree, or the reading as it stands."""
    r = plain(reading)
    for w in (GAIN, LOSS, GIVEN, EVEN_FLOOR, EVEN_SAME, DISAGREE, SHOWN):
        if r.startswith(w):
            return LOSS if r.startswith(NEVER_MORE_UP) else w
    return r


def judge_word(changes, clear, aim_) -> str:
    """judge_runs() reduced to its word (bare_word): the live engine's exporters colour a cell by it."""
    return bare_word(judge_runs(changes, clear, aim_))


# the aims as the live engine's exporters name them
EXPORT_AIMS = {"spent": SPENT, "per": WORK_PER, "up": HIGHER, "down": LOWER, "higher": HIGHER, "lower": LOWER, "shown": None,
               "HIGHER": HIGHER, "LOWER": LOWER, "SPENT": SPENT, "WORK_PER": WORK_PER, "SHOWN": None}


def cut_or_up(fell: bool) -> str:
    """The plain verb for which way a number went, beside its word: cut or up."""
    return "cut" if fell else "up"


EVEN_SAME = f"{EVEN}, the same"                     # under one part in a million of the value (amendment 11), or exactly
# The reading the tables wrote until 24 October 2026 for a run whose interval included zero, whatever the size of the change.
# No tool writes it now (a change of 0.5% or more shows its word: judge_runs); classify() still reads it in older records.
EVEN_NOISE = f"{EVEN}, no difference beyond the noise"


def even_noise(detail: str = "") -> str:
    """The reading of 13 to 24 October 2026 for a run whose interval included zero; kept so the older records read alike.
    Nothing writes it now: judge_runs() is the rule."""
    return f"{EVEN_NOISE} ({detail})" if detail else EVEN_NOISE


NEVER_MORE_UP = f"{LOSS} in at least one of our runs"            # a count that must never rise rose in a run
NEVER_MORE_HELD = f"{GAIN} or {EVEN} {IN_ALL_THREE}"              # ... and rose in none, and fell in at least one

THREE_RUN_RULE = ("A gauge whose change stayed under 0.5% either way in every run reads **EVEN, under the floor**. A change of 0.5% "
                  "or more is a change and never reads EVEN (the founder's order of 24 October 2026): when the runs that moved 0.5% "
                  "or more all move the same way the row reads its word, judged by what the gauge is for and never by its sign (a "
                  "resource spent that rose reads **power given**, never a loss; a cut is GAIN), written **GAIN** or **LOSS in all "
                  "three of our runs** when all three runs moved 0.5% or more the same way with every 95% interval clear of zero, and "
                  "otherwise with its qualifier beside it in the same cell (how many runs moved 0.5% or more, and how many of the three "
                  "were clear of the noise); runs that moved 0.5% or more pointing different ways read **the runs disagree**.")
STACK_RULE = ("Each run holds three paired repetitions; the paired difference's 95% interval within a run says whether that run is "
              "clear of the noise. " + THREE_RUN_RULE)


def never_more_rule(what: str) -> str:
    """The rule sentence for a count that must never rise."""
    return f"{what}: any rise in any run reads **{NEVER_MORE_UP}**."


def stack_reading(rs, direction, same_rel, key=None):
    """The three-run reading of one gauge of a stack's A/B/C table (PostgreSQL, Kafka, Redis, MongoDB, MySQL, the machine's
    frequency ceiling), from its three within-run paired results ({"native", "diff", "significant"}). direction is the
    gauge's declared aim (LOWER, HIGHER, SPENT, NEVER_MORE, or SHOWN_AIM); key is its name, for the resources declared
    "lower" before the word "spent" was written."""
    if any(r is None for r in rs):
        return "no value"
    a = aim(direction, key)
    if a is None:
        return SHOWN
    if a == NEVER_MORE:
        if any(r["diff"] > 0 for r in rs):
            return f"**{NEVER_MORE_UP}**"
        return EVEN_SAME if all(abs(r["diff"]) <= 1e-12 for r in rs) else f"**{NEVER_MORE_HELD}**"
    if all(abs(r["diff"]) <= same_rel * max(abs(r["native"]), 1e-12) for r in rs):
        return EVEN_SAME
    return judge_runs([rel_change(r["native"], r["diff"]) for r in rs], [bool(r["significant"]) for r in rs], a)


# --------------------------------------------------------------------------------------------- reading any table's words
_DIRECTION = (("lower or the same in all three of our runs", True), ("lower in all three of our runs", True),
              ("higher in all three of our runs", False), ("higher in at least one of our runs", False),
              ("higher in a repetition", False), ("confirmed lower", True), ("confirmed higher", False))


def classify(reading, aim_=None):
    """A reading in one word for the scorers: "gain", "loss", "given", "noise", "same", "disagree" or "unjudged". Reads every
    table's words: GAIN/EVEN/LOSS and power given; the direction words of 13 October (lower, higher; aim_ turns them into a
    word, and is then required); toward and away from the aim; better, worse and "confirmed" of the older tables. A reading
    that moved away from its aim on a resource spent (aim_ SPENT) is power given."""
    r = (reading or "").strip().strip("*").strip()
    lo = r.lower()
    if not lo or lo.startswith(("shown", "no value", "not taken", "n/a")):
        return "unjudged"
    if lo.startswith(("gain or even", "gain")):
        return "gain"
    if lo.startswith("loss"):
        return "loss"
    if lo.startswith(GIVEN):
        return "given"
    if lo.startswith("even"):
        return "noise" if "noise" in lo else "same"
    if lo.startswith("no difference"):
        return "noise"
    if "disagree" in lo or "runs differ" in lo or "different ways" in lo:
        return "disagree"
    away = ("given" if aim_ in (SPENT, WORK_PER) else "loss")
    for old, cls in (("better", "gain"), ("worse", away), ("toward", "gain"), ("away", away)):   # older tables, kept as written
        if lo.startswith(old) or lo.startswith(f"confirmed {old}") or lo.startswith(f"**{old}"):
            return cls
    for w, fell in _DIRECTION:
        if lo.startswith(w):
            if aim_ is None:
                raise ValueError(f"the reading {reading!r} says a direction; its gauge's aim is needed to give it a word")
            return {GAIN: "gain", LOSS: "loss", GIVEN: "given"}[word(fell, aim_)]
    if lo.startswith("same"):
        return "same"
    # a receipt of its own kind (the robustness test's "the same in all three of our runs" for a hand-back held, "handed back
    # within the allowance ..."): a fact about the governor, not a gauge against native; the caller decides what it is
    raise ValueError(f"unknown reading: {reading!r}")


def landed(table) -> bool:
    """Whether a three-run table carries a result (whole): a gauge row, or a workload beside the tuning one (the table writers
    write a workload only where every run holds it). A table written from runs that failed (its workloads or rows empty: 20
    October, the omni-v12 MongoDB table) has not taken its benchmark's place: the same benchmark's table on an older engine
    stands as that engine's result until the newer engine's three runs land. The one rule every tool that picks a benchmark's
    newest table reads (tools/omni_index.py, tools/benefit_sheet.py, tools/levels.py, tools/power.py, the live engine's
    docs/engine/export_scenarios.py). A Markdown table is read through its JSON twin; one kept only in Markdown, or whose JSON
    is another table's shape (neither rows nor workloads), reads as whole."""
    import json
    p = Path(table)
    if p.suffix == ".md":
        if not p.with_suffix(".json").exists():
            return True
        p = p.with_suffix(".json")
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    if not isinstance(d, dict):
        return False
    if "rows" not in d and "workloads" not in d:
        return True                      # another table's shape (the organisms, a cloud set's repetitions): its own writer decides
    if d.get("rows"):
        return True
    return any(wl != "tuning" for wl in (d.get("workloads") or {}))


def judged(reading: str) -> bool:
    """A reading that holds the same way in all three runs, every interval clear of zero (GAIN, LOSS or power given, or an
    older table's words for the same), or a count that must never rise and rose in a run."""
    r = (reading or "").strip().strip("*").strip()
    lo = r.lower()
    return (lo.startswith("confirmed") or IN_ALL_THREE in r or lo.startswith(NEVER_MORE_UP.lower())
            or lo.startswith("higher in at least one of our runs"))


def toward_aim(reading: str, aim_):
    """For the tools that score the headline: True when a judged reading moved the gauge toward its declared aim (GAIN),
    False when away from it (LOSS or power given), None when it is not judged. aim_ may be True (the aim is lower) or False
    (higher), the way the older scorers named it, or an aim word."""
    if not judged(reading):
        return None
    a = {True: LOWER, False: HIGHER}.get(aim_, aim_) if isinstance(aim_, bool) else aim_
    c = classify(reading, a)
    return True if c == "gain" else False if c in ("loss", "given") else None


def in_gel_words(reading: str, diffs, aim_) -> str:
    """A judged reading in GAIN/EVEN/LOSS, whatever words its table was written in: a direction becomes its word by the
    gauge's aim; an older table's better or worse becomes GAIN, LOSS or power given by the same aim (a judged reading has
    the same sign in every run)."""
    r = (reading or "").strip().strip("*")
    if not judged(r):
        return r
    try:
        c = classify(r, aim_)
    except ValueError:
        signs = {(d > 0) - (d < 0) for d in diffs if d is not None}
        if len(signs) != 1 or aim_ is None:
            return r
        c = {GAIN: "gain", LOSS: "loss", GIVEN: "given"}[word(signs == {-1}, aim_)]
    w = {"gain": GAIN, "loss": LOSS, "given": GIVEN}.get(c)
    if w is None:
        return r
    return NEVER_MORE_UP if r.lower().startswith(("higher in at least one", NEVER_MORE_UP.lower())) else f"{w} {IN_ALL_THREE}"


def row_gain(v) -> bool:
    """Whether a row of an organism report (tools/six_kube_report.py) is a GAIN: its field gain, or, in the receipts written
    before, the fields they kept for the same thing (toward_aim since 13 October, better before)."""
    for k in ("gain", "toward_aim", "better"):
        if k in v:
            return bool(v[k])
    return False


row_toward = row_gain


# ---------------------------------------------------------------------------------------- labels written by a rule
GAIN_AND_LOSS = f"{GAIN} AND {LOSS}"        # a muscle with one aim toward and one away: both stand in the table
GAIN_GIVEN = f"{GAIN}, {GIVEN}"             # service toward its aim, bought with a resource spent
# The words for the labels the rules write (the realms of v5, tools/run_realms_v5.py; the engine harness's and the card
# bench's preregistered labels, realms/harness.py and tools/gpu_reps.py, which keep their recorded wording until the
# engine's next version), and for the names the older results used.
LABEL_WORDS = {
    "TOWARD ITS AIMS": GAIN, "BOTH WAYS": GAIN_AND_LOSS, "MIXED": GAIN_AND_LOSS, "AWAY FROM ITS AIMS": LOSS, "WORSE": LOSS,
    "SAME AS NATIVE": EVEN, "AT ITS LIMIT ON NATIVE": EVEN,
    "SUPERIOR WITHIN GUARDRAILS": GAIN, "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF": GAIN_AND_LOSS,
    "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF": GAIN_GIVEN, "NONINFERIOR / INCONCLUSIVE": EVEN, "NOT ESTABLISHED": EVEN,
    "AWAY FROM ITS AIM": LOSS, "INVALID": "INVALID",
}
GAIN_PARTS = ("MORE WORK", "FASTER", "FEWER MISSES", "LESS ENERGY")


def gel_of_label(label):
    """GAIN, EVEN, LOSS, GAIN AND LOSS, "GAIN, power given" or INVALID for a label a rule wrote; None if it is no label."""
    lab = (label or "").replace("**", "").strip()
    if lab in LABEL_WORDS:
        return LABEL_WORDS[lab]
    if lab in (GAIN, EVEN, LOSS, GAIN_AND_LOSS, GAIN_GIVEN):
        return lab
    parts = [x.strip() for x in lab.split("+")]
    if lab and all(x in GAIN_PARTS for x in parts):        # the gains a muscle showed, joined: MORE WORK + FASTER ...
        return GAIN
    return None


LABEL_SHOWN = {
    "TOWARD ITS AIMS": GAIN, "BOTH WAYS": GAIN_AND_LOSS, "MIXED": GAIN_AND_LOSS, "AWAY FROM ITS AIMS": LOSS, "WORSE": LOSS,
    "SAME AS NATIVE": f"{EVEN} (the same as native)", "AT ITS LIMIT ON NATIVE": f"{EVEN} (at its limit on native)",
    "SUPERIOR WITHIN GUARDRAILS": f"{GAIN} (within the guardrails)",
    "ENERGY IMPROVEMENT WITH SERVICE TRADEOFF": f"{GAIN_AND_LOSS} (energy cut, service traded for it)",
    "SERVICE IMPROVEMENT WITH ENERGY TRADEOFF": f"{GAIN_GIVEN} (service GAIN, energy given for it)",
    "NONINFERIOR / INCONCLUSIVE": f"{EVEN} (inside the noise, within the guardrails)",
    "NOT ESTABLISHED": f"{EVEN} (not established: inside the noise, a guardrail crossed on the mean)",
    "AWAY FROM ITS AIM": LOSS, "INVALID": "INVALID",
}


def labelled(label) -> str:
    """A label as a table shows it, its word first: "GAIN (fewer misses)", "EVEN (at its limit on native)", "LOSS"."""
    lab = (label or "").replace("**", "").strip()
    if lab in LABEL_SHOWN:
        return LABEL_SHOWN[lab]
    w = gel_of_label(lab)
    if w is None or w == lab:
        return lab
    return f"{w} ({lab.lower()})"


# ------------------------------------------------------------------------------------- the count under a three-run table
class Tally:
    """The count under a three-run table: gauge-rows that read GAIN, LOSS and power given (and how many of each in all three of
    our runs, every interval clear of zero), rows that read EVEN, and rows where the runs disagree."""

    def __init__(self):
        self.gain = self.loss = self.given = self.even = self.disagree = 0
        self.gain3 = self.loss3 = self.given3 = 0

    def add(self, reading, direction, key=None):
        c = classify(reading, aim(direction, key))
        strict = IN_ALL_THREE in (reading or "") and not (reading or "").lstrip("*").lower().startswith("gain or even")
        self.gain += c == "gain"
        self.loss += c == "loss"
        self.given += c == "given"
        self.gain3 += c == "gain" and strict
        self.loss3 += c == "loss" and strict
        self.given3 += c == "given" and strict
        self.even += c in ("noise", "same")
        self.disagree += c == "disagree"

    def sentence(self, n, what="workloads"):
        return (f"**Across {n} {what}: {self.gain} gauge-rows GAIN ({self.gain3} in all three of our runs), {self.loss} LOSS "
                f"({self.loss3} in all three of our runs), {self.given} power given ({self.given3} in all three of our runs), "
                f"{self.even} EVEN, {self.disagree} where the runs disagree.**")

    def counts(self):
        return f"{self.gain} GAIN, {self.loss} LOSS, {self.given} power given, {self.even} EVEN, {self.disagree} disagree"


DETERMINISTIC_RULE = ("a gauge reads **GAIN** or **LOSS in all three of our runs** when all three runs moved 0.5% or more with the same "
                      "sign, judged by what the gauge is for and never by its sign (a resource spent that rose reads **power given**); a "
                      "change under 0.5% in every run reads **EVEN, under the floor** (the founder's floor of 20 October 2026, a change "
                      "of 0.5% or more always a change: 24 October)")
ACROSS_HEAD = "GAIN in all three of our runs | LOSS in all three of our runs | Power given in all three of our runs | EVEN | The runs differ"
ACROSS_RULE = "|---|---:|---:|---:|---:|---:|"


def across_cells(t, direction=None, key=None) -> str:
    """One gauge's cells under a deterministic simulator's three-run tables ({reading: [cases]}): how many cases read GAIN,
    LOSS and power given in all three of our runs (the cases named where they read LOSS or power given), then the cases
    EVEN and the cases where the runs differ."""
    a = aim(direction, key)
    by = {"gain": [], "loss": [], "given": [], "even": [], "disagree": []}
    for reading, cases in t.items():
        c = classify(reading, a)
        by["even" if c in ("noise", "same") else c if c in by else "even"].extend(cases)
    cell = lambda xs, named: f"{len(xs)}" + (f" ({', '.join(xs)})" if named and xs else "")
    return (f"{cell(by['gain'], False)} | {cell(by['loss'], True)} | {cell(by['given'], True)} | {len(by['even'])} | "
            f"{len(by['disagree'])}")


def across_counts(tally, direction_of):
    """(gain, loss, given, differ) over a simulator's tally ({gauge: {reading: [cases]}}): case-rows that read GAIN, LOSS
    and power given in all three of our runs, and where the runs differ. direction_of(gauge) gives the gauge's direction."""
    g = l_ = gv = d = 0
    for k, t in tally.items():
        a = aim(direction_of(k), k)
        for reading, cases in t.items():
            c = classify(reading, a)
            g += len(cases) * (c == "gain"); l_ += len(cases) * (c == "loss"); gv += len(cases) * (c == "given")
            d += len(cases) * (c == "disagree")
    return g, l_, gv, d


def with_own_runs(lines):
    """A table's lines with OWN_RUNS under its title (the legal notice is stamped around them afterwards)."""
    return list(lines[:1]) + ["", OWN_RUNS] + list(lines[1:])


# ------------------------------------------------------------------------------------------------------------- the key
def word_sign(word):
    """The sign a number carries beside its word (the founder's order of 20 October, said again on 22 October: the word GAIN can
    never have a minus beside it): GAIN '+', LOSS '−', EVEN '=', power given '+' (what Omni put in); a reading with no word of
    its own (shown, tuning, the runs disagree) keeps the number's own direction."""
    w = str(word or "")
    if w.startswith("GAIN") or w.startswith("power given"):
        return "+"
    if w.startswith("LOSS"):
        return "−"
    if w.startswith("EVEN"):
        return "="
    return None


def by_word(x, word, unit="%", digits=1):
    """A change beside its word, carrying the word's sign: 'GAIN +73.0%' is printed as '+73.0% GAIN' by the caller; here the
    number alone: '+73.0%', '−16.8%', '=0.9%'; with no word of its own, the number's own sign."""
    if x is None or x != x:
        return "—"
    sg = word_sign(word)
    size = f"{abs(x):.{digits}f}{unit}"
    return f"{sg}{size}" if sg else f"{'+' if x > 0 else '−' if x < 0 else '±'}{size}"


def interval_by_word(lo, hi, word, unit="%", digits=1):
    """A 95% interval beside its word: with GAIN or LOSS the two sizes from the smaller to the larger, each with the word's
    sign ('+47.3% to +127.5%'); with EVEN, or with no word of its own, the interval as it lies, crossing zero ('−1.9% to
    +3.7%')."""
    sg = word_sign(word)
    f = lambda v: f"{abs(v):.{digits}f}{unit}"
    if sg in ("+", "−") and not (lo < 0 < hi):      # an interval that crosses zero lies as measured, whatever the word
        a, b = sorted((abs(lo), abs(hi)))
        return f"{sg}{f(a)} to {sg}{f(b)}"
    raw = lambda v: f"{'+' if v > 0 else '−' if v < 0 else '±'}{f(v)}"
    return f"{raw(lo)} to {raw(hi)}"


KEY_TITLE = "The key: GAIN, EVEN and LOSS"
KEY_BEGIN = "<!-- the key: GAIN, EVEN and LOSS (tools/readings.py) -->"
KEY_END = "<!-- end of the key -->"
LETTERS = (
    (GAIN, "surplus and positive variance", (("G", "Growth", "asset appreciation"), ("A", "Advantage", "risk reduction"),
                                             ("I", "Improvement", "margin expansion"), ("N", "Net-positive", "profitable outcome")),
     "the gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a "
     "resource cut"),
    (EVEN, "the break-even baseline: equilibrium", (("E", "Equalized", "zero variance"), ("V", "Verified baseline", "expected norm"),
                                                    ("E", "Equilibrium", "balanced risk"), ("N", "Neutral", "no net change")),
     "no change of 0.5% or more either way in any run (under the floor), or the same; a change of 0.5% or more is never EVEN; "
     "a knob native already runs at the top of its range is EVEN, at its limit on native"),
    (LOSS, "actuarial deficit and exposure", (("L", "Leakage", "capital drain"), ("O", "Off-track", "adverse selection"),
                                              ("S", "Setback", "claim liability"), ("S", "Subpar", "negative variance")),
     "the gauge moved away from its declared aim: less work done, a longer wait, more misses or failures"),
)


def key_lines():
    """The key as Markdown lines (the manual's front matter, the README, the reading guide and the summary carry it)."""
    L = [f"## {KEY_TITLE}", "",
         "Every judged reading in Omni-Compass is one of three words: **GAIN**, **EVEN** or **LOSS**. Better, same and worse "
         "are not used anywhere. The word is decided by what the gauge is for, never by the plus or minus sign of its number: "
         "who sets the aim differs from one system to the next, and each gauge's aim is written in its preregistration before "
         "the runs.", "",
         "| Word | What each letter stands for | Its sense in underwriting | What it means in a table |", "|---|---|---|---|"]
    for w, sense, letters, meaning in LETTERS:
        L.append(f"| **{w}** | " + "; ".join(f"**{a}** {b} ({c})" for a, b, c in letters) + f" | {sense} | {meaning} |")
    L += ["", "How the sign of a number becomes a word:", "",
          "- **Time waited, missed or failed** (a response time, time over the line, failed requests): a fall is GAIN, a rise is LOSS.",
          "- **Work done** (work inside the line, throughput, a hit rate): a rise is GAIN, a fall is LOSS.",
          "- **A resource spent or held** (energy, the power drawn and its peaks and swings, machines, memory, processor time, a "
          "bill, wear on a part): a fall is a **cut**, and a cut is GAIN. A rise is **power given**: what Omni put in to buy the work "
          "and the speed shown beside it. Power given is always shown and never hidden, and it is never called a loss (the "
          "founder's order of 12 October 2026: the max rides every muscle's edge; it never shaves). A peak is power held, so a peak "
          "that rose is power given, in a data centre and in a building alike (17 October).",
          "- **Work bought with each unit of a resource** (work per energy): a rise is a cut in what each unit of work took, a GAIN; "
          "a fall is power given, because it falls when more power is given for the same work.",
          "- So a minus can read GAIN (a response time cut 65%, a bill cut 30%) and a plus can read LOSS (failed requests up).",
          "- **The floor** (the founder's orders of 20 and 24 October 2026): a change under half of one percent (0.5%) either way, in "
          "every run, reads **EVEN, under the floor**; the row keeps its measured size. A change of 0.5% or more either way is a "
          "change and never reads EVEN: \"Any gauge that gives anything over a 0.5 percent change either way is a change ... it has "
          "to show its loss or gain\" (24 October). It reads GAIN, LOSS or power given by the gauge's aim, with the count of runs "
          "clear of the noise beside the word.",
          "- **The sign beside a word** (the same order): the number next to a word carries the word's sign, never the gauge's raw "
          "direction, so that no one mistakes which way a number went: GAIN **+**, LOSS **−**, EVEN **=**. A bill cut 3% reads "
          "GAIN +3%, failed requests up 2% read LOSS −2%, and a change under the floor reads EVEN =0.3%.", "",
          "Some preregistrations name their outcome with a label written before the runs (for example SUPERIOR WITHIN "
          "GUARDRAILS in the card protocol). The label stays as it was frozen, and every table shows it with its word first: "
          + "; ".join(f"{k} reads {v}" for k, v in LABEL_SHOWN.items() if k not in ("WORSE", "MIXED", "AWAY FROM ITS AIM", "INVALID"))
          + ". A run that breaks its own validity checks reads INVALID and carries no word.", "",
          "A reading is decided over our three runs, A, B and C. Only the runs that moved 0.5% or more decide its direction; when "
          "they all move the same way the gauge reads its word. \"GAIN in all three of our runs\" means all three runs moved 0.5% "
          "or more the same way with every 95% interval clear of zero. Where a run's interval includes zero, or a run stayed under "
          "the floor, the word stands and its qualifier follows in the same cell, the count of runs clear of the noise always shown: "
          "\"GAIN (the same way in all three runs; 2 of 3 clear of the noise)\", \"LOSS (2 of 3 runs moved 0.5% or more, the same "
          "way, 1 under the floor; 1 of 3 clear of the noise)\". The other readings are **EVEN, under the floor** (every run under "
          "0.5%), **EVEN, the same** (no change at all), **the runs disagree** (runs that moved 0.5% or more pointing different ways: "
          "the test is unstable there and is looked into) and **shown, not judged** (a gauge declared in advance as shown only, such "
          "as the knob's own setting). A count that must never rise (failed requests, lost messages) reads LOSS on any rise in any "
          "run. Tables written before 24 October 2026 read a run whose interval included zero as \"EVEN, no difference beyond the "
          "noise\" whatever its size; every published table has been read again by this rule (`tools/reread_key.py`).", "",
          "Why these three words: they are the words of underwriting and actuarial work, where every outcome is graded as "
          "surplus, break-even or deficit, and each letter spells out the same rule. Omni-Compass is there to add (GAIN), never "
          "to take (LOSS), and to hand a muscle back to its own native setting where it cannot add (EVEN). Its first rule is do no "
          "harm, in the founder's meaning of 19 October 2026: the organism Omni-Compass governs is never left turning out less "
          "than its native controllers make it turn out, nor less healthy, and every muscle works only as far as its own limit "
          "(`DISCLOSURES.md`, section 3). So **LOSS should never appear**: where it does, the row stays in the table, its cause "
          "is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again.", "",
          "Disclosure and disclaimer: GAIN, EVEN and LOSS, and the letters behind them, are The Omni-Compass LLC's own convention "
          "for reading its own results. The underwriting senses explain the words; they are not an actuarial, financial or "
          "insurance opinion, and no outside body defined, reviewed or approved them. A reading states what our own runs "
          "measured against native under the declared aims, not a promise about any other system; every number stands beside "
          "its word, so a reader can judge it by any other convention. " + OWN_RUNS]
    return L


def key_block():
    """The key between its two markers, as a page carries it."""
    return [KEY_BEGIN] + key_lines() + [KEY_END]


def key_text() -> str:
    """The key as plain text, for a terminal."""
    out = []
    for ln in key_lines():
        if ln.startswith("|---"):
            continue
        if ln.startswith("| **"):
            cells = [c.strip() for c in ln.strip("|").split("|")]
            out += [f"{cells[0]}: {cells[1]}", f"    underwriting: {cells[2]}", f"    in a table: {cells[3]}"]
            continue
        if ln.startswith("| Word"):
            continue
        out.append(ln)
    return re.sub(r"\*\*|`", "", "\n".join(out)).replace("## ", "")


# ---------------------------------------------------------------------------------- how to read this receipt
RECEIPT_BEGIN = "<!-- how to read this receipt (tools/readings.py) -->"
RECEIPT_END = "<!-- end: how to read this receipt -->"


def receipt_key_lines():
    """The short reading instruction every receipt and table carries under its title (the founder's order of 16 October,
    night: whoever reads a report must know, before the first number, how a plus, a minus or a zero becomes a word)."""
    return [
        "**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by "
        "the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, "
        "a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: no change of 0.5% or more either way in any run "
        "(under the floor), the same, or the knob at its limit on native; a change of 0.5% or more is never EVEN. **LOSS**: the "
        "gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, "
        "the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one "
        "that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and "
        "never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus "
        "can read GAIN (a "
        "response time cut) and a plus can read LOSS (failed requests up). A reading holds **in all three of our runs** when runs A, "
        "B and C all moved 0.5% or more the same way with every interval clear of zero; otherwise its word carries beside it how "
        "many runs moved 0.5% or more and how many were clear of the noise; **the runs disagree** names runs that moved 0.5% or "
        "more in different ways, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring "
        "and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, "
        "section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. " + OWN_RUNS,
    ]


def receipt_key():
    """The block between its markers, as every table writer emits it under the title."""
    return [RECEIPT_BEGIN, *receipt_key_lines(), RECEIPT_END]


# The standing tables that must carry the block: every page a reader is sent to for a result on the engine that stands.
RECEIPT_PAGES = ("results/live/V7_*.md", "results/realms_v5/REALMS_V5.md", "results/grid_v5/GRID.md", "docs/BENEFIT_SHEET.md",
                 "docs/WIRING_VERDICTS.md", "docs/STATE_OF_PLAY.md")


def receipt_pages(root: Path = ROOT):
    out = []
    for pat in RECEIPT_PAGES:
        out += sorted(str(p.relative_to(root)) for p in root.glob(pat))
    return out


def _with_receipt_key(text: str) -> str:
    """The text with the block in place: replaced where its markers stand, else inserted after the notice under the title."""
    block = "\n".join(receipt_key())
    if RECEIPT_BEGIN in text and RECEIPT_END in text:
        a = text.index(RECEIPT_BEGIN)
        b = text.index(RECEIPT_END) + len(RECEIPT_END)
        return text[:a] + block + text[b:]
    lines = text.split("\n")
    at = None
    for i, ln in enumerate(lines[:12]):
        if ln.startswith("> ©"):                       # the legal notice under the title: the block goes right after it
            at = i + 1
            break
    if at is None:
        for i, ln in enumerate(lines[:4]):
            if ln.startswith("# "):
                at = i + 1
                break
    if at is None:
        return text
    while at < len(lines) and lines[at].strip() == "":
        at += 1
    return "\n".join(lines[:at] + [block, ""] + lines[at:])


def check_receipts(root: Path = ROOT):
    """The standing tables that do not carry the reading block word for word."""
    bad = []
    for p in receipt_pages(root):
        t = (root / p).read_text()
        if RECEIPT_BEGIN not in t or RECEIPT_END not in t or _with_receipt_key(t) != t:
            bad.append(p)
    return bad


KEY_PAGES = ("README.md", "docs/HOW_TO_READ_THE_RESULTS.md", "docs/OMNI_COMPASS_MANUAL.md",
             "docs/OMNI_COMPASS_OWNERS_MANUAL.md", "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md")


def _with_key(text: str) -> str:
    block = "\n".join(key_block())
    if KEY_BEGIN in text and KEY_END in text:
        a = text.index(KEY_BEGIN)
        b = text.index(KEY_END) + len(KEY_END)
        return text[:a] + block + text[b:]
    return text


def check_pages(root: Path = ROOT):
    """The pages that must carry the key and do not carry it word for word."""
    bad = []
    for p in KEY_PAGES:
        f = root / p
        if not f.exists():
            continue
        t = f.read_text()
        if KEY_BEGIN not in t or KEY_END not in t or _with_key(t) != t:
            bad.append(p)
    return bad


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--key", action="store_true"); g.add_argument("--check", action="store_true"); g.add_argument("--fix", action="store_true")
    a = ap.parse_args(argv)
    if a.key:
        print(key_text())
        return 0
    if a.fix:
        for p in KEY_PAGES:
            f = ROOT / p
            if f.exists():
                t = f.read_text(); n = _with_key(t)
                if n != t:
                    f.write_text(n); print(f"the key rewritten in {p}")
        for p in receipt_pages():
            f = ROOT / p
            t = f.read_text(); n = _with_receipt_key(t)
            if n != t:
                f.write_text(n); print(f"how to read this receipt written in {p}")
        return 0
    bad = check_pages()
    for p in bad:
        print(f"{p}: the key (between {KEY_BEGIN} and {KEY_END}) is missing or not word for word")
    for p in check_receipts():
        bad.append(p)
        print(f"{p}: the block 'How to read this receipt' (between {RECEIPT_BEGIN} and {RECEIPT_END}) is missing or not word for word")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
