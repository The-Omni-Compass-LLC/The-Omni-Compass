# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The control plane: one process that decides; the hands on the machines and the front do the rest.

The ledger is what is wanted (units per service, the state of every machine, batch tasks done) and what was placed
(every unit: its machine, its port). Every change to it is a line in the journal before it is acted on, so a control
plane that is killed and started again replays the journal and finds the same ledger; the units it finds running on the
machines are taken back as they are, none started again. Every second it:

  1. asks every machine's hand for its status; a machine silent three times running is down, and its units are placed
     again elsewhere; a unit a machine runs that the ledger does not know is stopped;
  2. stops the units retiring once their drain is over (out of the routes first, so no request is lost);
  3. on the brain's beat, decides the units of each service (brain.py: the reflex on work in line, the compass law on the
     95th percentile, the yardstick twin less the depth the verdict has allowed on the service's own response times) and,
     for Omni, the machines (wake before any unit would wait, park one at a time after the load has held low for three
     beats, its units moved first) and each unit's CPU wall (the engine's conveyance: the room its machine can still
     give under 75%, journaled, written to the hand and read back);
  4. places the units the ledger lacks (the scheduler's room rule), retires the extra ones, and lets batch tasks into
     the room the services leave (a task yields its room the moment a service needs it);
  5. writes the routes for the front (only ready units) and one line of the timeline.

The kill switch is a file: while it exists the brain is off and the declared state is held (the declared units, every
machine on, every wall at its request). Every decision is a line in the audit with its reason.
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from omni_orchestrator.brain import OmniBrain, Yardstick, conveyed_limits, machines_needed
from omni_orchestrator.scheduler import BUSY_TOP, place
from omnicompass.verdict import Verdict

ROOT = str(Path(__file__).resolve().parents[1])


def http(method: str, url: str, body: dict | None = None, timeout: float = 5.0):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read() or b"{}")


class Control:
    def __init__(self, spec: dict, state_dir: str, brain: str, beat: float, kill_file: str | None = None,
                 room_rule: str = "requests"):
        self.spec, self.brain_kind, self.beat, self.room_rule = spec, brain, beat, room_rule
        self.dir = Path(state_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.journal_path, self.audit_path = self.dir / "journal.jsonl", self.dir / "audit.jsonl"
        self.timeline_path = self.dir / "timeline.jsonl"
        self.routes_path = Path(spec["routes"])
        self.kill_file = Path(kill_file) if kill_file else self.dir / "KILL"
        self.floor, self.boot_s, self.drain_s = spec.get("floor_machines", 2), spec.get("boot_s", 10), spec.get("drain_s", 2)
        self.step_units, self.hold = spec.get("step_units", 2), spec.get("park_hold_beats", 3)
        self.how = "pack" if brain in ("omni", "omni_native") else "spread"
        now = time.time()
        self.machines = {m["name"]: {"name": m["name"], "url": m["url"], "cpu_m": m["cpu_m"], "state": "awake",
                                     "miss": 0, "until": 0.0, "since": now} for m in spec["machines"]}
        self.services = {s["name"]: s for s in spec["services"]}
        self.desired = {n: s["replicas"] for n, s in self.services.items()}
        self.jobs = {j["name"]: j for j in spec.get("jobs", [])}
        self.done: dict[str, set] = {n: set() for n in self.jobs}
        self.units: dict[str, dict] = {}
        self.seq, self.port = 0, spec.get("port_base", 9100)
        self.replayed = self.replay()
        self.brains = {n: OmniBrain(s["line_ms"], beat, s["min"], s["max"], spec.get("max_step", 3), self.hold)
                       for n, s in self.services.items()}
        self.yard = {n: Yardstick(s["min"], s["max"]) for n, s in self.services.items()}
        # the verdict (omnicompass/verdict.py), one a service: a unit fewer than the twin is tried on the service's own
        # response times, stepwise, within the 2% allowance; a trial every 2 beats at the earliest, a refused step tried
        # again after 24 beats, a phase given up after 12 beats
        self.verdicts = {n: Verdict(tolerance=0.02, min_samples=30, probe_every=2, recheck=24, max_steps=s["max"],
                                    max_trial=12, incremental=True) for n, s in self.services.items()} if brain == "omni" else {}
        self.front_seq = 0                                # the front's answers already handed to the verdict
        self.last_n: dict[str, int] = {}                  # the units standing at the last beat, and the step the phase
        self.phase_floor: dict[str, int] = {}             # asked for then: the trial counts only work served at its step
        self.phase_anchor: dict[str, int] = {}            # the twin as each phase found it: its steps are counted from there
        self.phase_rate: dict[str, float] = {}            # the arrivals (last 5 s) as each phase found them: its traffic
        # a trial the traffic abandoned cost a unit below the twin and measured nothing; the next waits 6 beats, doubled at
        # each abandonment in a row, up to the verdict's recheck (24 beats), and a trial judged to its end clears the hold
        self.abandoned: dict[str, int] = {}
        self.trial_hold: dict[str, int] = {}
        self.busy_raw: dict[str, float | None] = {}
        self.cpu_prev: dict[str, tuple[float, float]] = {}
        self.next_beat, self.next_yard = now + beat, now + 15.0
        self.short: dict[str, int] = {}
        self.stopping: set[str] = set()
        self.park_calm, self.killed, self.stop = 0, False, False
        self.pool = ThreadPoolExecutor(12)
        self.routes_last = None

    # ---- the ledger and its journal --------------------------------------------------------------------------------
    def apply(self, ev: dict) -> None:
        k = ev["ev"]
        if k == "desired":
            self.desired[ev["service"]] = ev["n"]
        elif k == "unit":
            u = dict(ev["u"])
            u.setdefault("ready", False)
            self.units[u["id"]] = u
            self.seq = max(self.seq, u["seq"] + 1)
            self.port = max(self.port, u["port"] + 1)
        elif k == "retire":
            if ev["id"] in self.units:
                self.units[ev["id"]].update(state="retiring", retire_at=ev["at"])
        elif k == "gone":
            self.units.pop(ev["id"], None)
        elif k == "machine":
            m = self.machines.get(ev["name"])
            if m is not None:
                m.update(state=ev["state"], until=ev.get("until", 0.0), since=ev.get("t", time.time()))
        elif k == "task_done":
            self.done.setdefault(ev["job"], set()).add(ev["index"])
        elif k == "limit":
            if ev["id"] in self.units:
                self.units[ev["id"]]["conveyed_m"] = ev["limit_m"]

    def record(self, ev: dict) -> None:
        ev = {"t": time.time(), **ev}
        with open(self.journal_path, "a") as f:
            f.write(json.dumps(ev) + "\n")
            f.flush()
            os.fsync(f.fileno())
        self.apply(ev)

    def replay(self) -> int:
        if not self.journal_path.exists():
            return 0
        n = 0
        for line in self.journal_path.read_text().splitlines():
            try:
                self.apply(json.loads(line))
                n += 1
            except (ValueError, KeyError):
                continue
        return n

    def audit(self, kind: str, **kw) -> None:
        with open(self.audit_path, "a") as f:
            f.write(json.dumps({"t": time.time(), "kind": kind, **kw}) + "\n")

    # ---- the machines' hands ---------------------------------------------------------------------------------------
    def poll(self) -> dict[str, dict | None]:
        def get(m):
            try:
                return http("GET", m["url"] + "/status", timeout=1.0)
            except Exception:
                return None
        futs = {n: self.pool.submit(get, m) for n, m in self.machines.items()}
        return {n: f.result() for n, f in futs.items()}

    def _delete(self, url: str, uid: str) -> None:
        try:
            http("DELETE", f"{url}/units/{uid}", timeout=10.0)
        except Exception:
            pass
        self.stopping.discard(uid)

    def stop_unit(self, m: dict, uid: str) -> None:
        if uid not in self.stopping:
            self.stopping.add(uid)
            self.pool.submit(self._delete, m["url"], uid)

    def sync(self, status: dict, now: float) -> None:
        for name, m in self.machines.items():
            st = status.get(name)
            if st is None:
                m["miss"] += 1
                if m["miss"] >= 3 and m["state"] != "down":
                    lost = [u for u in self.units.values() if u["machine"] == name]
                    self.record({"ev": "machine", "name": name, "state": "down"})
                    for u in lost:
                        self.record({"ev": "gone", "id": u["id"]})
                    self.audit("machine down", machine=name, why="no answer three times running",
                               units_lost=[u["id"] for u in lost])
                continue
            m["miss"] = 0
            prev = m.get("_cpu")                         # the machine's measured busy share, millicores, smoothed over its polls
            m["_cpu"] = (st.get("time", now), st.get("cpu_s", 0.0))
            if prev and m["_cpu"][0] > prev[0]:
                rate = max(0.0, (m["_cpu"][1] - prev[1]) / (m["_cpu"][0] - prev[0]) * 1000.0)
                m["busy_m"] = rate if m.get("busy_m") is None else 0.5 * m["busy_m"] + 0.5 * rate
            if m["state"] == "down":
                self.record({"ev": "machine", "name": name, "state": "awake"})
                self.audit("machine back", machine=name, why="its hand answers again; it joins empty")
            seen = set()
            for r in st["units"]:
                uid = r["id"]
                seen.add(uid)
                u = self.units.get(uid)
                if u is None or u["machine"] != name:
                    if uid not in self.stopping:
                        self.audit("stray unit stopped", machine=name, unit=uid, why="not in the ledger")
                    self.stop_unit(m, uid)
                    continue
                u.update(ready=bool(r["ready"]), agent_state=r["state"], restarts=r["restarts"], cpu_s=r["cpu_s"],
                         limit_m=r.get("limit_m"), ever_ready=u.get("ever_ready", False) or bool(r["ready"]))
                if u.get("kind") == "service" and not u["ever_ready"] and r["restarts"] >= 2 and u["state"] != "retiring":
                    # a unit that cannot come up where it stands (its port taken, its machine lying) is placed again
                    # elsewhere with a new port, instead of being started on the same spot forever
                    self.audit("unit replaced", unit=uid, machine=name, why=f"{r['restarts']} starts and never ready")
                    self.record({"ev": "gone", "id": uid})
                    self.stop_unit(m, uid)
                    continue
                if u.get("kind") == "task" and r["state"] in ("succeeded", "failed") and u["state"] != "retiring":
                    if r["state"] == "succeeded":
                        self.record({"ev": "task_done", "job": u["job"], "index": u["index"]})
                    else:
                        self.audit("task failed", unit=uid, why="three tries; it goes back in the queue")
                    self.record({"ev": "gone", "id": uid})
                    self.stop_unit(m, uid)
            for u in [u for u in self.units.values() if u["machine"] == name and u["id"] not in seen]:
                if u["state"] != "retiring" and now - u["born"] > 5.0:
                    self.record({"ev": "gone", "id": u["id"]})
                    self.audit("unit lost", unit=u["id"], machine=name, why="its machine no longer runs it")

    def retire(self, u: dict, why: str, drain: float | None = None) -> None:
        self.record({"ev": "retire", "id": u["id"], "at": time.time() + (self.drain_s if drain is None else drain)})
        self.audit("unit retiring", unit=u["id"], machine=u["machine"], why=why)

    def retire_due(self, now: float) -> None:
        for u in [u for u in self.units.values() if u["state"] == "retiring" and now >= u["retire_at"]]:
            self.stop_unit(self.machines[u["machine"]], u["id"])
            self.record({"ev": "gone", "id": u["id"]})

    # ---- placing -------------------------------------------------------------------------------------------------
    def _start(self, u: dict, spec: dict) -> None:
        self.record({"ev": "unit", "u": u})
        url = self.machines[u["machine"]]["url"]

        def go():
            try:
                http("POST", url + "/units", spec)
            except Exception:
                pass                                     # not started: the next checks find it missing and place it again
        self.pool.submit(go)

    def place_service(self, name: str, svc: dict) -> bool:
        m = place(svc["req_m"], name, self.machines, list(self.units.values()), self.how, self.room_rule)
        if m is None:
            victim = next((u for u in self.units.values() if u.get("kind") == "task" and u["state"] != "retiring"
                           and self.machines[u["machine"]]["state"] == "awake"), None)
            if victim is not None:
                self.retire(victim, f"a batch task yields its room to {name}", drain=0.0)
            return False
        uid, port = f"{name}-{self.seq}", self.port
        u = {"id": uid, "seq": self.seq, "kind": "service", "service": name, "machine": m, "port": port,
             "req_m": svc["req_m"], "state": "placed", "born": time.time()}
        spec = {"id": uid, "kind": "service", "port": port, "limit_m": svc["limit_m"], "mem_mb": svc.get("mem_mb", 256),
                "health": svc.get("health", "/health"), "cwd": ROOT,
                "cmd": [sys.executable, "-m", "omni_orchestrator.workload", "serve", "--port", str(port), "--k",
                        str(svc["k"]), "--unit", uid]}
        self._start(u, spec)
        self.audit("unit placed", unit=uid, machine=m, service=name)
        return True

    def place_task(self, jname: str, j: dict, index: int) -> bool:
        m = place(j["req_m"], f"job:{jname}", self.machines, list(self.units.values()), "pack", self.room_rule)
        if m is None:
            return False
        uid = f"{jname}-{index}-{self.seq}"
        u = {"id": uid, "seq": self.seq, "kind": "task", "job": jname, "index": index, "machine": m, "port": 0,
             "req_m": j["req_m"], "state": "placed", "born": time.time()}
        spec = {"id": uid, "kind": "task", "limit_m": j["limit_m"], "mem_mb": j.get("mem_mb", 256), "cwd": ROOT,
                "cmd": [sys.executable, "-m", "omni_orchestrator.workload", "task", "--job", jname, "--index",
                        str(index), "--k", str(j["k"]), "--out", j["out"]]}
        self._start(u, spec)
        self.audit("task placed", unit=uid, machine=m, job=jname, index=index)
        return True

    def count_on(self, machine: str, service: str | None = None) -> int:
        return sum(1 for u in self.units.values() if u["machine"] == machine and u["state"] != "retiring"
                   and (service is None or u.get("service") == service))

    def reconcile(self) -> None:
        self.short = {}
        for name, svc in self.services.items():
            mine = [u for u in self.units.values() if u.get("service") == name and u["state"] != "retiring"]
            movers = [u for u in mine if self.machines[u["machine"]]["state"] == "draining"]
            staying = [u for u in mine if u not in movers]
            want = self.desired[name]
            for k in range(want - len(staying)):
                if not self.place_service(name, svc):
                    self.short[name] = want - len(staying) - k
                    break
            staying = [u for u in self.units.values() if u.get("service") == name and u["state"] != "retiring"
                       and self.machines[u["machine"]]["state"] != "draining"]
            if movers and len(staying) >= want and sum(1 for u in staying if u["ready"]) >= want:
                for u in movers:
                    self.retire(u, "its machine is being parked; a replacement elsewhere is ready")
            extra = len(staying) - want
            if extra > 0:
                if self.how == "pack":
                    key = lambda u: (u["ready"], self.count_on(u["machine"]), -u["born"])
                else:
                    key = lambda u: (u["ready"], -self.count_on(u["machine"], name), -u["born"])
                for u in sorted(staying, key=key)[:extra]:
                    self.retire(u, f"{want} units wanted")

    def batch(self) -> None:
        if any(self.short.values()):
            return                                       # the services come first
        for jname, j in self.jobs.items():
            running = [u for u in self.units.values() if u.get("job") == jname and u["state"] != "retiring"]
            busy = {u["index"] for u in running}
            pending = [i for i in range(j["tasks"]) if i not in self.done[jname] and i not in busy]
            for i in pending[:max(0, j["parallel"] - len(running))]:
                if not self.place_task(jname, j, i):
                    break

    # ---- the brain -----------------------------------------------------------------------------------------------
    def front_stats(self) -> dict | None:
        try:
            return http("GET", self.spec["front_stats"], timeout=1.0)
        except Exception:
            return None

    def busy(self, name: str, now: float) -> float | None:
        """The service's busy share as the yardstick reads it: the processor its units used over their requests, each
        unit's use capped at its request (a Kubernetes pod never uses more than its limit, here its request; a unit
        Omni has conveyed more to would otherwise read as more pods than Kubernetes would hold). The uncapped share is
        kept in busy_raw for the audit."""
        used = raw = req = 0.0
        for u in self.units.values():
            if u.get("service") != name or u["state"] == "retiring" or "cpu_s" not in u:
                continue
            prev = self.cpu_prev.get(u["id"])
            self.cpu_prev[u["id"]] = (now, u["cpu_s"])
            if prev is None or now - prev[0] <= 0:
                continue
            dt = now - prev[0]
            d = max(0.0, u["cpu_s"] - prev[1])
            raw += d
            used += min(d, u["req_m"] / 1000.0 * dt)
            req += u["req_m"] / 1000.0 * dt
        self.busy_raw[name] = raw / req if req > 0 else None
        return used / req if req > 0 else None

    def front_recent(self) -> dict | None:
        """The front's reading with every answer's response time since the last beat (for the verdict)."""
        try:
            out = http("GET", f"{self.spec['front_stats']}?since={self.front_seq}", timeout=1.0)
            self.front_seq = int(out.get("seq", self.front_seq))
            return out
        except Exception:
            return None

    def think(self, now: float) -> None:
        stats = self.front_recent() if self.brain_kind in ("omni", "omni_native") else None
        for name, svc in self.services.items():
            n = len([u for u in self.units.values() if u.get("service") == name and u["state"] != "retiring"
                     and self.machines[u["machine"]]["state"] != "draining"])
            if self.brain_kind == "off":
                want, why = svc["replicas"], {"rule": "the declared units, no brain"}
            elif self.brain_kind == "yardstick":
                if now < self.next_yard:
                    continue
                self.next_yard = now + 15.0
                busy = self.busy(name, now)
                want = self.yard[name].recommend(now, n, busy)
                why = {"rule": "the yardstick: Kubernetes' published autoscaling rule", "busy": busy}
            elif self.brain_kind == "omni_native":
                # Omni on top of the native rule (the engine's strict form, as on the kind rigs): the units are the
                # yardstick's, Kubernetes' rule on the same readings, never fewer; Omni's reflex and fail-up add above it;
                # no fold below the twin and no verdict; Omni's conveyance, room rule, packing and machines on top
                busy = self.busy(name, now)
                p95 = (stats or {}).get("p95_5s", 0.0)
                waiting = int((stats or {}).get("line", 0))
                reading = svc["line_ms"] if stats and waiting > 2 * max(1, int(stats.get("hands", 1))) else p95
                brain = self.brains[name]
                twin = brain.twin.recommend(now, n, busy)
                want, why = brain.decide(now, n, busy, reading, waiting, 0, False, twin=twin)
                why["rule"] = "Omni on native: the yardstick's units at least; Omni's reflex, conveyance and machines on top"
                why["busy_raw"] = None if self.busy_raw.get(name) is None else round(self.busy_raw[name], 3)
            else:
                busy = self.busy(name, now)
                p95 = (stats or {}).get("p95_5s", 0.0)
                waiting = int((stats or {}).get("line", 0))
                reading = p95
                if stats and waiting > 2 * max(1, int(stats.get("hands", 1))):
                    reading = svc["line_ms"]             # work waiting in line past twice the hands: at the wall
                brain, v = self.brains[name], self.verdicts.get(name)
                twin = brain.twin.recommend(now, n, busy)
                depth, trial, anchor = 0, False, None
                if v is not None:
                    calm = waiting == 0 and brain.law.band.position(reading) < brain.law.band.wall_high
                    rate = float((stats or {}).get("n_5s", 0.0))      # the arrivals of the last 5 s
                    r0 = self.phase_rate.get(name)
                    if v.phase is not None and r0 is not None and abs(rate - r0) > 0.15 * max(r0, 5.0):
                        # a trial is paired under the same traffic (omnicompass/verdict.py): the arrivals moved by more
                        # than 15% since the phase began, so what it measured is the traffic, not the step; abandoned
                        k = self.abandoned.get(name, 0) + 1
                        wait = min(v.recheck, 6 * 2 ** (k - 1))
                        self.abandoned[name], self.trial_hold[name] = k, v.t + 1 + wait
                        self.audit("verdict", service=name, verdict="trial abandoned (the traffic changed)", step=v.trial,
                                   arrivals_5s_was=r0, arrivals_5s_now=rate, next_trial_after_beats=wait)
                        calm = False
                    elif v.phase is None and v.t + 1 < self.trial_hold.get(name, 0):
                        calm = False                     # the traffic has been moving faster than a trial: none starts yet
                    # the work served over the last beat counts for the trial only if the units stood at its step the
                    # whole beat (the knob at the step the verdict asked for, and unchanged since)
                    if stats and stats.get("recent") and n == self.last_n.get(name) == self.phase_floor.get(name):
                        v.observe(stats["recent"])
                    if waiting > 0 and v.allowed > 0:
                        # the immune reaction: work waited under an allowed depth, so one step goes back to the twin and
                        # is not tried again until the recheck has passed
                        v.allowed -= 1
                        v.refused_until[v.allowed + 1] = v.t + v.recheck
                        self.audit("verdict", service=name, verdict="depth handed back: work waited in line",
                                   step=v.allowed + 1, waiting=waiting)
                    depth, trial, ev = v.tick(calm)
                    if ev:
                        self.audit("verdict", service=name, **ev)
                        if ev.get("verdict") == "trial":
                            self.phase_anchor[name] = twin   # the step is counted from the twin as the phase found it
                            self.phase_rate[name] = rate     # and judged only under the traffic the phase found
                        elif str(ev.get("verdict", "")).startswith("step "):
                            self.abandoned[name] = 0         # a trial judged to its end: the traffic held still for one
                    anchor = self.phase_anchor.get(name, twin) if trial else None
                want, why = brain.decide(now, n, busy, reading, waiting, depth, trial, twin=twin, anchor=anchor)
                why["busy_raw"] = None if self.busy_raw.get(name) is None else round(self.busy_raw[name], 3)
                self.last_n[name], self.phase_floor[name] = n, why["floor"]
            if want != self.desired[name]:
                self.audit("units", service=name, was=self.desired[name], now=want, why=why)
                self.record({"ev": "desired", "service": name, "n": want})
        if self.brain_kind in ("omni", "omni_native"):
            self.machine_brain(now)
            self.convey(now)

    def _set_limit(self, url: str, uid: str, limit_m: float) -> None:
        try:
            http("POST", f"{url}/units/{uid}/limit", {"limit_m": limit_m}, timeout=5.0)
        except Exception:
            pass                                         # not taken: the read-back differs and the next beat writes again

    def convey(self, now: float) -> None:
        """The engine's conveyance (omni-v7, omni-v13) on Omni's own machines: each service unit's CPU wall set to the
        room its machine can still give under 75%, shared among the service's units there, never under the request;
        batch tasks on the machine are the other workload, counted by their limits. Written to the hand, journaled,
        read back; audited when the intention changes."""
        for m in self.machines.values():
            if m["state"] != "awake":
                continue
            on = [u for u in self.units.values() if u["machine"] == m["name"] and u["state"] != "retiring"]
            ours = [u for u in on if u.get("kind") == "service"]
            others_m = sum(float(u.get("conveyed_m") or u["req_m"]) for u in on if u.get("kind") != "service")
            want = conveyed_limits(m["cpu_m"], m.get("busy_m"), ours, others_m)
            if want is None:
                continue
            for u in ours:
                w = want[u["id"]]
                meant = float(u.get("conveyed_m") or u["req_m"])
                if abs(w - meant) >= 10.0:
                    self.record({"ev": "limit", "id": u["id"], "limit_m": w})
                    self.audit("limit conveyed" if w > meant else "limit handed back", unit=u["id"], machine=m["name"],
                               was=meant, now=w, why=f"the machine {m['busy_m']:.0f} m busy of {m['cpu_m']} m; "
                               f"{len(ours)} unit(s) share the room under 75%, other workloads {others_m:.0f} m")
                held = u.get("limit_m")
                if abs(w - meant) >= 10.0 or (held is not None and abs(held - w) >= 10.0):
                    self.pool.submit(self._set_limit, m["url"], u["id"], w)

    def hand_back_limits(self) -> None:
        """Every conveyed wall back to the request (the declared state), as the kill switch asks."""
        for u in self.units.values():
            if u.get("kind") == "service" and u.get("conveyed_m") and u["conveyed_m"] != u["req_m"]:
                self.record({"ev": "limit", "id": u["id"], "limit_m": float(u["req_m"])})
                self.pool.submit(self._set_limit, self.machines[u["machine"]]["url"], u["id"], float(u["req_m"]))

    def machine_brain(self, now: float) -> None:
        room = max(m["cpu_m"] for m in self.machines.values()) * (BUSY_TOP if self.room_rule == "busy" else 1.0)
        req = max(s["req_m"] for s in self.services.values())
        tasks_m = sum(u["req_m"] for u in self.units.values() if u.get("kind") == "task" and u["state"] != "retiring")
        units = sum(self.desired.values())
        need = machines_needed(units, req, room, self.step_units, self.floor, tasks_m)
        live = [m for m in self.machines.values() if m["state"] in ("awake", "booting")]
        awake = [m for m in self.machines.values() if m["state"] == "awake"]
        booting = [m for m in self.machines.values() if m["state"] == "booting"]
        draining = [m for m in self.machines.values() if m["state"] == "draining"]
        short = any(self.short.values())
        if need > len(live) or (short and not booting):
            # a unit with no room waits only for a machine already on its way: one is woken, not one a beat
            self.park_calm = 0
            k = max(1, need - len(live))
            for m in draining[:k]:
                self.record({"ev": "machine", "name": m["name"], "state": "awake"})
                self.audit("machine kept", machine=m["name"], why=f"the units wanted need {need} machines; its drain is undone")
                k -= 1
            for m in [m for m in self.machines.values() if m["state"] == "parked"][:max(0, k)]:
                self.record({"ev": "machine", "name": m["name"], "state": "booting", "until": now + self.boot_s})
                self.audit("machine woken", machine=m["name"],
                           why=f"{units} units wanted need {need} machines with room for {self.step_units} more"
                           if need > len(live) else "a unit found no room")
        elif short:
            self.park_calm = 0                           # a machine is booting for the unit that waits
        elif need < len(awake) and not draining and not booting:
            self.park_calm += 1
            if self.park_calm >= self.hold:
                m = min(awake, key=lambda m: (self.count_on(m["name"]), m["name"]))
                self.record({"ev": "machine", "name": m["name"], "state": "draining"})
                self.audit("machine draining", machine=m["name"],
                           why=f"{units} units wanted need {need} machines; {len(awake)} awake")
                self.park_calm = 0
        else:
            self.park_calm = 0

    def machines_step(self, now: float) -> None:
        for m in self.machines.values():
            if m["state"] == "booting" and now >= m["until"]:
                self.record({"ev": "machine", "name": m["name"], "state": "awake"})
                self.audit("machine awake", machine=m["name"], why="booted")
            elif m["state"] == "draining":
                if not any(u["machine"] == m["name"] for u in self.units.values()):
                    self.record({"ev": "machine", "name": m["name"], "state": "parked"})
                    self.audit("machine parked", machine=m["name"], why="empty")
                elif now - m["since"] > 60:
                    self.record({"ev": "machine", "name": m["name"], "state": "awake"})
                    self.audit("machine kept", machine=m["name"], why="its units found no room elsewhere in 60 s")

    def kill_switch(self, now: float) -> None:
        on = self.kill_file.exists()
        if on and not self.killed:
            self.killed = True
            for name, svc in self.services.items():
                if self.desired[name] != svc["replicas"]:
                    self.record({"ev": "desired", "service": name, "n": svc["replicas"]})
            for m in self.machines.values():
                if m["state"] == "draining":
                    self.record({"ev": "machine", "name": m["name"], "state": "awake"})
                elif m["state"] == "parked":
                    self.record({"ev": "machine", "name": m["name"], "state": "booting", "until": now + self.boot_s})
            self.hand_back_limits()
            self.audit("kill switch on", why="the brain is off; the declared state is held: the declared units, every "
                       "machine on, every wall at its request")
        elif not on and self.killed:
            self.killed = False
            self.audit("kill switch off", why="the brain resumes")

    # ---- the front and the record ----------------------------------------------------------------------------------
    def write_routes(self) -> None:
        routes = {name: sorted(({"id": u["id"], "host": "127.0.0.1", "port": u["port"], "ready": True}
                                for u in self.units.values() if u.get("service") == name and u["ready"]
                                and u["state"] != "retiring" and self.machines[u["machine"]]["state"] != "down"),
                               key=lambda r: r["id"]) for name in self.services}
        if routes == self.routes_last:
            return
        tmp = self.routes_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(routes))
        os.replace(tmp, self.routes_path)
        self.routes_last = routes

    def timeline(self, now: float) -> None:
        states = {}
        for m in self.machines.values():
            states[m["state"]] = states.get(m["state"], 0) + 1
        row = {"t": now, "brain": self.brain_kind, "killed": self.killed, "desired": dict(self.desired),
               "units": {n: sum(1 for u in self.units.values() if u.get("service") == n and u["state"] != "retiring")
                         for n in self.services},
               "ready": {n: sum(1 for u in self.units.values() if u.get("service") == n and u["ready"]
                                and u["state"] != "retiring") for n in self.services},
               "machines": states, "short": dict(self.short),
               "tasks_running": sum(1 for u in self.units.values() if u.get("kind") == "task" and u["state"] != "retiring"),
               "tasks_done": {j: len(d) for j, d in self.done.items()},
               # the processor conveyed above the requests (millicores, every service unit standing) and the verdict's state
               "conveyed_m": sum(max(0.0, float(u.get("conveyed_m") or u["req_m"]) - u["req_m"]) for u in self.units.values()
                                 if u.get("kind") == "service" and u["state"] != "retiring"),
               "depth": {n: v.allowed for n, v in self.verdicts.items()},
               "trial": {n: v.phase for n, v in self.verdicts.items() if v.phase}}
        with open(self.timeline_path, "a") as f:
            f.write(json.dumps(row) + "\n")

    def step(self, now: float) -> None:
        self.sync(self.poll(), now)
        self.retire_due(now)
        self.kill_switch(now)
        if not self.killed and now >= self.next_beat:
            self.next_beat = now + self.beat
            self.think(now)
        self.machines_step(now)
        self.reconcile()
        self.batch()
        self.write_routes()
        self.timeline(now)

    def run(self) -> None:
        self.audit("control plane started", brain=self.brain_kind, beat=self.beat, journal_lines_replayed=self.replayed,
                   units_in_ledger=len(self.units))
        while not self.stop:
            t = time.time()
            try:
                self.step(t)
            except Exception as e:                       # a failed check is recorded and the next comes on time
                self.audit("error", error=repr(e)[:300])
            time.sleep(max(0.05, 1.0 - (time.time() - t)))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--spec", required=True)
    ap.add_argument("--state-dir", required=True)
    ap.add_argument("--brain", choices=("omni", "omni_native", "yardstick", "off"), default="omni",
                    help="omni: Omni direct, Omni alone on the machines; omni_native: Omni on top of the native rule "
                         "(Kubernetes' autoscaling rule holds the units, Omni conveys, places, parks and adds above it); "
                         "yardstick: the native rule alone; off: the declared units, no brain")
    ap.add_argument("--beat", type=float, default=60.0, help="the brain's beat in seconds (the dial: 5 to 120 s)")
    ap.add_argument("--kill-file", default=None)
    ap.add_argument("--room-rule", choices=("requests", "busy"), default="requests",
                    help="room by requests alone (Kubernetes' way), or also under 75%% of the machine's measured busy share")
    a = ap.parse_args(argv)
    c = Control(json.loads(Path(a.spec).read_text()), a.state_dir, a.brain, a.beat, a.kill_file, a.room_rule)
    signal.signal(signal.SIGTERM, lambda *_: setattr(c, "stop", True))
    c.run()


if __name__ == "__main__":
    main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
