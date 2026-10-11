# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on one GPU, on top of the card's own firmware: the wires of the card's brain (omni_controller/gpu_brain.py).

The card keeps its own control: NVIDIA's firmware still boosts and still protects the chip. Omni holds two settings the
card already accepts, and nothing else:
  up wire    the clock ceiling: how high boost may climb (NVML locked clocks, or nvidia-smi -lgc FLOOR,MAX; reset with
             -rgc, which hands the clock back to the firmware)
  down wire  the power limit (NVML or nvidia-smi -pl W): the start limit, always, unless a power target is set (brake)

Two paths into the brain:
  signal     the workload (or the proxy in front of it) tells the brain each arrival and each finished request through a
             local datagram socket (--signal PATH; lines "a <id>" and "d <id> <cost_ms>"). An arrival on an idle card is
             answered at once: the ceiling goes back to the top before the next decision, which is what lets the card
             park its clock between bursts without slowing the burst. Without a signal the brain never parks
  decision   every --interval seconds: the card's own readings (power, utilization, clock, temperature, limits, the
             clock-limit reasons), the service's position in its compass from the response times (--latency-file,
             --slo-ms: past the line, or any failed request, is past the wall), the verdict's trials, the guards

Writes go through NVML when the driver library is present (a write takes milliseconds) and through nvidia-smi
otherwise (tens of milliseconds a write). Parking needs the fast path: through nvidia-smi the race comes too late for
the first request after a rest, so the park pedal stays off (--park-slow-path overrides it, for the tests). Every write
is read back; every write and every race and park is in the audit.

Guards: blind (meters unreadable; the response feed silent while work is on the card): fail up. Heat (the card reports a
thermal or hardware slowdown): fail up. One writer: a power limit neither mine nor the start means another writer, so
observe only from then on and exit 5. Restore on exit, kill file, master switch or SIGTERM: clocks reset and the start
limit back, read back.

The audit (--audit) carries the records the bench reads (snapshot, decision with telemetry and decided_by, write and
actuator for each power-limit write, clock_write for each clock write, restored) plus race, park and cruise records with
their timestamps and the verdict's events. Exit: 0 clean, 3 restore failed, 4 a write refused, 5 another writer.
"""
from __future__ import annotations

import argparse
import json
import os
import shlex
import signal
import socket
import subprocess
import sys
import threading
import time

from omnicompass import master
from omni_controller.gpu_brain import CardBrain
from omni_controller.gpu_governor import query, snapshot, throttle, slowed, WriteFailed, SNAPSHOT
from omni_controller.muscles import latency_sense, latency_window


def smi_run(smi, args):
    try:
        p = subprocess.run(shlex.split(smi) + args, capture_output=True, text=True, timeout=20)
        return p.returncode, p.stderr.strip()[:300]
    except (subprocess.SubprocessError, OSError) as e:
        return -1, f"{type(e).__name__}: {e}"[:300]


def query_top_clock(smi, g):
    try:
        out = subprocess.run(shlex.split(smi) + ["-i", str(g), "--query-gpu=clocks.max.sm", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=10, check=True).stdout
        return float(out.strip().splitlines()[0])
    except (subprocess.SubprocessError, OSError, ValueError, IndexError):
        return None


def query_default_limit(smi, g):
    """The card's factory power limit (watts), or None if the driver will not say."""
    try:
        out = subprocess.run(shlex.split(smi) + ["-i", str(g), "--query-gpu=power.default_limit", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=10, check=True).stdout
        return float(out.strip().splitlines()[0])
    except (subprocess.SubprocessError, OSError, ValueError, IndexError):
        return None


def query_min_clock(smi, g):
    """The lowest graphics clock the card supports (the floor of a -lgc range); 300 MHz if the driver will not list them."""
    try:
        out = subprocess.run(shlex.split(smi) + ["-i", str(g), "--query-supported-clocks=graphics", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=10, check=True).stdout
        return int(min(float(x) for x in out.split() if x.strip()))
    except (subprocess.SubprocessError, OSError, ValueError):
        return 300


class Nvml:
    """The fast path: the driver's own library (nvidia-ml-py). Writes take milliseconds instead of a process start."""
    def __init__(self, g):
        import pynvml as n                                    # noqa: N813  (the library's own name)
        n.nvmlInit()
        self.n, self.h = n, n.nvmlDeviceGetHandleByIndex(int(g))

    def set_clock(self, floor, mhz):
        self.n.nvmlDeviceSetGpuLockedClocks(self.h, int(floor), int(mhz))

    def reset_clock(self):
        self.n.nvmlDeviceResetGpuLockedClocks(self.h)

    def set_limit(self, w):
        self.n.nvmlDeviceSetPowerManagementLimit(self.h, int(round(w * 1000)))

    def read(self):
        n, h = self.n, self.h
        r = {"draw": n.nvmlDeviceGetPowerUsage(h) / 1000.0, "temp": float(n.nvmlDeviceGetTemperature(h, n.NVML_TEMPERATURE_GPU)),
             "util": n.nvmlDeviceGetUtilizationRates(h).gpu / 100.0, "limit": n.nvmlDeviceGetPowerManagementLimit(h) / 1000.0,
             "clock_mhz": float(n.nvmlDeviceGetClockInfo(h, n.NVML_CLOCK_SM))}
        try:
            r["enforced"] = n.nvmlDeviceGetEnforcedPowerLimit(h) / 1000.0
        except Exception:  # noqa: BLE001  older drivers
            r["enforced"] = r["limit"]
        for f in ("nvmlDeviceGetCurrentClocksEventReasons", "nvmlDeviceGetCurrentClocksThrottleReasons"):
            if hasattr(n, f):
                try:
                    r["reasons"] = f"0x{getattr(n, f)(h):016x}"
                    break
                except Exception:  # noqa: BLE001
                    continue
        return r


class GpuCompass:
    def __init__(self, a):
        self.a = a
        self.g = int(str(a.gpus).split(",")[0])
        self.log = open(a.audit, "a")
        self.lock = threading.RLock()
        self.writes = 0
        self.foreign = False
        self.clock_set = False
        self.enforced_ok = query(a.smi, [self.g], enforced=True) is not None
        s = query(a.smi, [self.g], self.enforced_ok)
        if s is None:
            raise SystemExit("nvidia-smi unreadable at start: no snapshot, so I take no authority")
        snap = snapshot(a.smi, [self.g])
        self.start = s[self.g]["limit"]
        dflt = query_default_limit(a.smi, self.g)
        self.capped = dflt is not None and self.start < dflt - 1.0
        self.expect = self.start
        self.top = query_top_clock(a.smi, self.g) or s[self.g]["clock_mhz"]
        self.c_floor = query_min_clock(a.smi, self.g)
        self.nvml = None
        if a.nvml != "off":
            try:
                self.nvml = Nvml(self.g)
            except Exception as e:  # noqa: BLE001  no library, no driver binding: the slow path
                if a.nvml == "on":
                    raise SystemExit(f"NVML requested but unavailable: {e}")
        self.signal_on = bool(a.signal)
        # parking needs a race in time: through nvidia-smi a write takes tens of milliseconds, which the modelled card
        # showed costs the first request after a rest about 1% (amendment 13). So the park pedal needs the fast path
        slow_path = self.nvml is None and not a.park_slow_path
        self.brain = CardBrain(self.top, self.c_floor, self.start, allow=a.allow, samples=a.verdict_samples,
                               decision_s=a.interval, hold_ms=a.hold_ms, rest_ms=a.rest_ms, busy_step_mhz=a.busy_step_mhz,
                               busy_gain=a.busy_gain, probe_every_s=a.probe_every_s, recheck_s=a.recheck_s,
                               trial_s=a.trial_s, learn_samples=a.learn_samples, signal=self.signal_on,
                               park=not (a.no_park or slow_path), cruise=not a.no_cruise, power_target_w=a.power_target_w)
        self.written_ceiling = self.top
        self.last_arrival = {}                     # request id -> arrival time (the signal's view of work in flight)
        self.audit({"snapshot": {str(self.g): {"limit_w": self.start, "min_limit_w": s[self.g]["min"],
                                               "enforced_w": s[self.g]["enforced"] if self.enforced_ok else None,
                                               "clock_top_mhz": self.top, "clock_floor_mhz": self.c_floor,
                                               **{f: snap[f][str(self.g)] for f in SNAPSHOT}}},
                    "engine": "card brain, two wires (v4)", "mode": a.mode, "path": "nvml" if self.nvml else "nvidia-smi",
                    "signal": a.signal or None, "park_levels_mhz": self.brain.levels, "operator_cap": self.capped,
                    "verdict": {"allow": a.allow, "samples": a.verdict_samples, "probe_every_s": a.probe_every_s,
                                "recheck_s": a.recheck_s, "trial_s": a.trial_s, "busy_gain": a.busy_gain},
                    "covers": {"clock_mhz": [self.c_floor, round(self.top)], "power_w": [s[self.g]["min"], self.start]}})
        if a.mode == "cap" and snap["power.management"][str(self.g)].lower() != "enabled":
            self.audit({"refused": "power management not Enabled: a written limit would not bind"})
            raise SystemExit("power management not Enabled: cap mode refused, no authority taken")

    def audit(self, rec):
        with self.lock:
            self.log.write(json.dumps({"time": time.time(), **rec}) + "\n"); self.log.flush()

    # ---- the wires ------------------------------------------------------------------------------------------------
    def write_ceiling(self, mhz, why):
        """The up wire: at the top the clock goes back to the firmware (reset); under it, a locked range floor..mhz."""
        mhz = float(mhz)
        with self.lock:
            if abs(mhz - self.written_ceiling) < 0.5 and not (mhz >= self.top and self.clock_set):
                return
            if self.a.mode != "cap" or self.foreign:
                self.audit({"would_clock_write": round(mhz), "why": why}); self.written_ceiling = mhz; return
            t0 = time.time()
            if mhz >= self.top:
                cmd = ["-i", str(self.g), "-rgc"]
                rc, err = self._reset()
            else:
                cmd = ["-i", str(self.g), "-lgc", f"{self.c_floor},{int(round(mhz))}"]
                rc, err = self._lock(int(round(mhz)))
            self.audit({"clock_write": cmd, "why": why, "rc": rc, "stderr": err, "t_requested": t0,
                        "write_s": round(time.time() - t0, 5), "path": "nvml" if self.nvml else "nvidia-smi"})
            if rc != 0:
                raise WriteFailed(f"clock write {cmd} returned {rc}: {err}")
            self.clock_set = mhz < self.top
            self.written_ceiling = mhz
            self.writes += 1

    def _lock(self, mhz):
        if self.nvml:
            try:
                self.nvml.set_clock(self.c_floor, mhz); return 0, ""
            except Exception as e:  # noqa: BLE001
                return 1, f"NVML: {e}"[:300]
        return smi_run(self.a.smi, ["-i", str(self.g), "-lgc", f"{self.c_floor},{mhz}"])

    def _reset(self):
        if self.nvml:
            try:
                self.nvml.reset_clock(); return 0, ""
            except Exception as e:  # noqa: BLE001
                return 1, f"NVML: {e}"[:300]
        return smi_run(self.a.smi, ["-i", str(self.g), "-rgc"])

    def write_limit(self, w, why):
        w = int(w)
        cmd = ["nvidia-smi", "-i", str(self.g), "-pl", str(w)]
        with self.lock:
            if self.a.mode != "cap" or self.foreign:
                self.audit({"would_write": cmd, "why": why}); return
            self.audit({"write": cmd, "why": why})
            t0 = time.time()
            if self.nvml:
                try:
                    self.nvml.set_limit(w); rc, err = 0, ""
                except Exception as e:  # noqa: BLE001
                    rc, err = 1, f"NVML: {e}"[:300]
            else:
                rc, err = smi_run(self.a.smi, ["-i", str(self.g), "-pl", str(w)])
            act = {"gpu": self.g, "requested_w": w, "t_requested": t0, "rc": rc, "stderr": err}
            if rc != 0:
                self.audit({"actuator": act, "write_failed": cmd})
                raise WriteFailed(f"power limit {w} W returned {rc}: {err}")
            self.writes += 1
            s = query(self.a.smi, [self.g], self.enforced_ok)
            if s is not None:
                back = s[self.g]
                act.update({"readback_w": back["limit"], "enforced_w": back["enforced"], "t_readback": time.time(),
                            "realized": abs(back["limit"] - w) < 1.0, "override": back["enforced"] < back["limit"] - 1.0})
                if act["realized"]:
                    act["delay_s"] = round(act["t_readback"] - t0, 3)
                    self.expect = w
            self.audit({"actuator": act})

    # ---- the signal: arrivals and finished requests, answered at once -------------------------------------------------
    def on_arrival(self, rid):
        with self.lock:
            now = time.time()
            self.last_arrival[rid] = now
            w = self.brain.arrival(now, rid)
            if w:
                self.write_ceiling(w[0], w[1])
                self.audit({"race": {"id": rid, "to_mhz": round(w[0])}})

    def on_done(self, rid, cost):
        with self.lock:
            now = time.time()
            self.last_arrival.pop(rid, None)
            w = self.brain.done(now, rid, cost)
            if w:
                self.write_ceiling(w[0], w[1])
                self.audit({w[1]: {"id": rid, "to_mhz": round(w[0])}})

    def on_idle(self):
        with self.lock:
            w = self.brain.idle_due(time.time())
            if w:
                self.write_ceiling(w[0], w[1])
                self.audit({"park": {"to_mhz": round(w[0]), "step": self.brain.park_step}})

    def listen(self, stop):
        """The signal thread: a datagram socket the workload writes to; idle checks between messages."""
        path = self.a.signal
        try:
            os.unlink(path)
        except OSError:
            pass
        sk = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        sk.bind(path)
        try:
            os.chmod(path, 0o666)                    # the workload may run as another user than the governor
        except OSError:
            pass
        while not stop["now"]:
            nxt = self.brain.next_idle_check()
            timeout = 0.2 if nxt is None else min(0.2, max(0.0005, nxt - time.time()))
            sk.settimeout(timeout)
            try:
                msg = sk.recv(256).decode(errors="replace").split()
            except socket.timeout:
                msg = None
            except OSError:
                break
            try:
                if msg and msg[0] == "a" and len(msg) >= 2:
                    self.on_arrival(msg[1])
                elif msg and msg[0] == "d" and len(msg) >= 2:
                    self.on_done(msg[1], float(msg[2]) if len(msg) > 2 and msg[2] not in ("", "nan") else None)
                nxt = self.brain.next_idle_check()
                if nxt is not None and time.time() >= nxt:
                    self.on_idle()
            except WriteFailed as e:
                self.audit({"fatal": f"write failed: {e}"}); stop["failed"] = True; stop["now"] = True
            except Exception as e:  # noqa: BLE001  a bad message is logged, never fatal
                self.audit({"error": f"signal: {type(e).__name__}: {e}"})
        sk.close()

    # ---- the decision ---------------------------------------------------------------------------------------------
    def position(self):
        a = self.a
        if not (a.latency_file and a.slo_ms):
            return 0.0, None
        ls = latency_sense(a.latency_file, a.latency_window_s)
        if self.signal_on:
            # with the signal the brain knows when nothing is on the card: a silent feed then is an idle card, not a
            # blind one. Blind only if a request has been on the card longer than two windows without finishing
            stuck = any(time.time() - t > 2.0 * a.latency_window_s for t in self.last_arrival.values())
            if stuck:
                return None, ls
            if ls["blind"]:
                return 0.0, ls
        elif ls["blind"]:
            return None, ls
        bare = a.slo_ms / 10.0
        w = latency_window(a.latency_file, a.latency_window_s)["ms"]
        mean = sum(w) / len(w) if w else ls["p95"]
        resp = (mean - bare) / (a.slo_ms - bare)
        if ls["fail"] or ls["p95"] >= a.slo_ms:
            resp = max(resp, 1.0)
        return resp, ls

    def read(self):
        if self.nvml:
            try:
                r = self.nvml.read()
                return r, r.get("reasons")
            except Exception:  # noqa: BLE001  fall through to nvidia-smi
                pass
        s = query(self.a.smi, [self.g], self.enforced_ok)
        if s is None:
            return None, None
        thr = throttle(self.a.smi, [self.g])
        return s[self.g], (thr or {}).get(self.g)

    def step(self):
        a, g = self.a, self.g
        r, reasons = self.read()
        with self.lock:
            if r is not None and abs(r["limit"] - self.expect) >= 1.0 and not self.foreign:
                self.foreign = True
                self.audit({"foreign_writer": {"gpu": g, "reads_w": r["limit"], "expected_w": self.expect},
                            "action": "observe only from now on; both wires left to the other writer"})
            p, ls = self.position() if r is not None else (None, None)
            heat = slowed(reasons)
            tele = None if r is None else {"util": r["util"], "draw_w": r["draw"], "clock_mhz": r["clock_mhz"], "limit_w": r["limit"]}
            ceiling, lid, why = self.brain.decide(time.time(), tele, p, heat)
            n_clk, n_draw = self.brain.native()
            for ev in self.brain.take_events():
                self.audit(ev)
            self.audit({"decision": {str(g): {"telemetry": None if r is None else {
                            "util": r["util"], "draw_w": r["draw"], "temp_c": r["temp"], "limit_w": r["limit"],
                            "enforced_w": r.get("enforced"), "clock_mhz": r["clock_mhz"], "throttle": reasons},
                        "position": None if p is None else round(p, 4),
                        "latency_p95_ms": None if not ls else ls.get("p95"),
                        "ceiling_mhz": round(ceiling), "want_w": int(lid), "decided_by": why,
                        "native_busy_clock_mhz": n_clk, "native_busy_draw_w": n_draw, **self.brain.state()}}})
            self.write_ceiling(ceiling, why)
            cur = r["limit"] if r is not None else self.expect
            if abs(lid - cur) >= a.min_change_w or (abs(lid - self.start) < 0.5 and abs(cur - lid) >= 1.0):
                self.write_limit(lid, why)

    def restore(self):
        failed = []
        if self.a.mode == "cap" and not self.foreign:
            rc, err = self._reset()
            self.audit({"clock_write": ["-i", str(self.g), "-rgc"], "why": "restore", "rc": rc, "stderr": err})
            if rc != 0:
                failed.append(f"-rgc returned {rc}: {err}")
            s = query(self.a.smi, [self.g], self.enforced_ok)
            if s is None or abs(s[self.g]["limit"] - self.start) >= 1.0:
                try:
                    self.write_limit(self.start, "reset: the limit read at start")
                except WriteFailed as e:
                    failed.append(str(e))
        s = query(self.a.smi, [self.g], self.enforced_ok) or {}
        back = s[self.g]["limit"] if self.g in s else None
        ok = self.foreign or (not failed and back is not None and abs(back - self.start) < 1.0)
        self.audit({"restored": {str(self.g): back}, "start": {str(self.g): self.start}, "ok": ok,
                    "writes": self.writes, "foreign_writer": self.foreign, "restore_write_failed": failed,
                    "brain": self.brain.state()})
        return ok


def parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["watch", "cap"], default="watch")
    ap.add_argument("--gpus", default="0")
    ap.add_argument("--smi", default=os.environ.get("NVIDIA_SMI", "nvidia-smi"))
    ap.add_argument("--nvml", choices=["auto", "on", "off"], default="auto", help="the fast write path (driver library)")
    ap.add_argument("--signal", default="", help="datagram socket the workload reports arrivals and finished requests to")
    ap.add_argument("--interval", type=float, default=0.25, help="seconds between decisions")
    ap.add_argument("--duration", type=float, default=0.0)
    ap.add_argument("--audit", default="gpu_compass_audit.jsonl")
    ap.add_argument("--kill-file", default="/tmp/omni-gpu-kill")
    ap.add_argument("--latency-file", default="")
    ap.add_argument("--slo-ms", type=float, default=0.0)
    ap.add_argument("--latency-window-s", type=float, default=5.0, help="seconds of response times the position reads")
    ap.add_argument("--learn-samples", type=int, default=15, help="busy readings before the card's own level is reported")
    ap.add_argument("--floor-w", type=float, default=0.0, help="the declared envelope's lowest watts (a power target never goes under it)")
    ap.add_argument("--allow", type=float, default=0.005, help="the most a step may add to the card's own time on a request (0.5%%: inside the measurement; the engine's outer bound is 2%%)")
    ap.add_argument("--verdict-samples", type=int, default=30, help="requests measured at the reference and at the trial step")
    ap.add_argument("--probe-every-s", type=float, default=8.0, help="seconds between trials")
    ap.add_argument("--recheck-s", type=float, default=900.0, help="seconds before a refused step is tried again")
    ap.add_argument("--trial-s", type=float, default=120.0, help="the most a trial phase may take before it is abandoned")
    ap.add_argument("--hold-ms", type=float, default=20.0, help="idle milliseconds before the clock parks")
    ap.add_argument("--rest-ms", type=float, default=80.0, help="idle milliseconds after which a request counts as from rest")
    ap.add_argument("--busy-step-mhz", type=float, default=60.0, help="one cruise step under the top clock")
    ap.add_argument("--busy-gain", type=float, default=0.02, help="the least share of busy watts a cruise step must save")
    ap.add_argument("--no-park", action="store_true", help="never park (the park pedal off)")
    ap.add_argument("--park-slow-path", action="store_true", help="park even when writes go through nvidia-smi (tests only)")
    ap.add_argument("--no-cruise", action="store_true", help="never lower the ceiling under queued work")
    ap.add_argument("--power-target-w", type=float, default=None, help="brake: the lid at this target (never under --floor-w)")
    ap.add_argument("--min-change-w", type=float, default=3.0)
    # kept so older callers keep working; the brain has no use for them (anything that does not work is removed)
    ap.add_argument("--race-util", type=float, default=0.95, help=argparse.SUPPRESS)
    ap.add_argument("--down-gain", type=float, default=None, help=argparse.SUPPRESS)
    ap.add_argument("--min-change-mhz", type=float, default=15.0, help=argparse.SUPPRESS)
    return ap


def main(argv=None):
    a = parser().parse_args(argv)
    if a.power_target_w is not None and a.floor_w:
        a.power_target_w = max(a.power_target_w, a.floor_w)
    master.refuse_if_off("GPU governor (two wires)")
    gov = GpuCompass(a)
    back = ([[a.smi, "-i", str(gov.g), "-rgc"], [a.smi, "-i", str(gov.g), "-pl", str(int(round(gov.start)))]]
            if a.mode == "cap" else [])
    master.register("GPU governor (two wires)", restore=back, stale_s=max(60.0, 5 * a.interval))
    stop = {"now": False, "failed": False}
    signal.signal(signal.SIGTERM, lambda *_: stop.__setitem__("now", True))
    lt = None
    if a.signal:
        lt = threading.Thread(target=gov.listen, args=(stop,), daemon=True); lt.start()
    t0 = time.time()
    failed = False
    try:
        while not stop["now"] and not os.path.exists(a.kill_file) and not master.is_off() and (a.duration <= 0 or time.time() - t0 < a.duration):
            try:
                master.heartbeat(); gov.step()
            except WriteFailed as e:
                gov.audit({"fatal": f"write failed: {e}"}); failed = True
                break
            except Exception as e:  # noqa: BLE001  a failed decision is logged; the kill path still runs
                gov.audit({"error": f"{type(e).__name__}: {e}"})
            end = time.time() + a.interval
            while time.time() < end and not stop["now"] and not os.path.exists(a.kill_file) and not master.is_off():
                time.sleep(min(0.05, max(0.001, end - time.time())))
    finally:
        stop["now"] = True
        if lt is not None:
            lt.join(timeout=2.0)
        ok = gov.restore()
    failed = failed or stop.get("failed", False)
    return 5 if gov.foreign else 3 if not ok else 4 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
