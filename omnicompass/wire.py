# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The wire belongs to the brain (Omni v4, docs/OMNI_V4_PLAN.md, section 3).

A muscle is plugged in through one wire: one wire in (the service reading and the lever as it stands), one wire out (one
value for the lever). All the thinking is in the brain; the wire carries the brain's word and nothing else.

  attach    the lever is read once, before any write: the snapshot, the restore point. It never moves after that
  write     one value: clipped to the cover, checked against what the brain last wrote (or the snapshot), sent, and read
            back. Once a wire is plugged into a body, a write is reachable only with the body's key, that is, only from the
            body's own tick: no harness, controller or plant writes around the body
  one       if the lever is found at a value the brain did not write, someone else owns it: the brain stops writing and
  writer    leaves that value alone (restoring over it would fight the new owner)
  restore   the lever back to the snapshot (the hand-back, the kill switch, the end of a run); left alone when someone else
            owns it

Two bands: the cover is the lever's hard range (the device's or the operator's lowest and highest setting), and every write is
clipped to it, so nothing the math does can set the lever outside; the compass is the service reading's own band
(omnicompass/compass_law.py).
"""
from __future__ import annotations

from typing import Optional


def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v


class ForeignWriter(Exception):
    pass


class NotTheBody(PermissionError):
    """A write that did not come from the body's tick."""


class Wire:
    """One wire in, one wire out. Subclasses implement _read_service, _read_lever and _send; everything else is here."""

    def __init__(self, lo: float, hi: float, tolerance: float = 1e-6, name: Optional[str] = None):
        self.lo, self.hi, self.tol = lo, hi, tolerance
        self.name = name
        self.snapshot: Optional[float] = None
        self.last_written: Optional[float] = None
        self.owned = True
        self.writes = 0
        self.clipped = 0
        self._key = None                                   # the body's key, once the wire is plugged into a body

    # the wires ----------------------------------------------------------------------------------------------------
    def _read_service(self) -> float:
        raise NotImplementedError

    def _read_lever(self) -> float:
        raise NotImplementedError

    def _send(self, value: float) -> None:
        raise NotImplementedError

    # the contract -------------------------------------------------------------------------------------------------
    def plug(self, key) -> None:
        """Plugged into a body: from now on only that body's key writes."""
        self._key = key

    def attach(self) -> float:
        """Read the lever once, before any write: the restore point. It never moves after this."""
        if self.snapshot is None:
            self.snapshot = self._read_lever()
        return self.snapshot

    def read(self) -> float:
        return self._read_service()

    def lever(self) -> float:
        return self._read_lever()

    def write(self, value: float, key=None) -> Optional[float]:
        """Clip to the cover, check nobody else moved the lever, send, read back. None: not written (not owned)."""
        if self._key is not None and key is not self._key:
            raise NotTheBody(f"wire {self.name or ''} is the body's: written only from its tick")
        if not self.owned:
            return None
        if self.snapshot is None:
            self.attach()
        now = self._read_lever()
        expected = self.last_written if self.last_written is not None else self.snapshot
        if expected is not None and abs(now - expected) > self.tol:
            self.owned = False                                     # someone else moved it: it is theirs now
            raise ForeignWriter(f"lever at {now}, last written {expected}")
        v = clamp(value, self.lo, self.hi)
        self.clipped += int(v != value)
        if abs(v - now) <= self.tol:
            return now
        self._send(v)
        self.last_written = self._read_lever()
        self.writes += 1
        return self.last_written

    def restore(self) -> bool:
        """The lever back to the snapshot. Left alone when someone else owns it. True: at the snapshot (or not ours)."""
        if not self.owned or self.snapshot is None:
            return True
        if abs(self._read_lever() - self.snapshot) > self.tol:
            self._send(self.snapshot)
        self.last_written = None
        return abs(self._read_lever() - self.snapshot) <= self.tol


Plug = Wire                                                        # the name the v3 harnesses import
