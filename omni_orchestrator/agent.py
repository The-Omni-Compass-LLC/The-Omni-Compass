# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A machine's hand: one process per machine, the only thing that starts or stops a unit on it.

It holds the machine's walls (omni/<machine>: its CPU quota and memory), starts each unit in walls of its own under them
and on the machine's cores, and watches every unit twice a second: a service is probed on its health path (ready at its
first answer; killed and started again after three missed answers, or when it never answers in its first 30 s); a unit
whose process ends is started again after a wait that doubles from 1 s to 30 s; a batch task that ends with 0 is done,
and one that fails three times is failed. The units keep running whatever happens to the control plane: the hand needs
no one to keep them alive.

HTTP on 127.0.0.1:<port>:
  GET  /status          the machine, its walls, the processor it used, and every unit with its state
  POST /units           start a unit: {"id", "kind": "service"|"task", "cmd": [...], "port", "limit_m", "mem_mb",
                        "health", "env"}
  POST /units/<id>/limit  move the unit's CPU wall: {"limit_m"}; answers with the wall as the kernel now holds it
                        (the control plane's conveyance: a unit given the processor its machine can spare, or handed back)
  DELETE /units/<id>    stop a unit: SIGTERM to its process group, SIGKILL after 3 s, its walls removed
  POST /stop_all        stop every unit
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from omni_orchestrator.cgroup import Walls


def probe(port: int, path: str, timeout: float = 1.0) -> bool:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


class Unit:
    def __init__(self, spec: dict):
        self.spec = spec
        self.id = spec["id"]
        self.kind = spec.get("kind", "service")
        self.proc: subprocess.Popen | None = None
        self.state = "starting"
        self.ready = False
        self.restarts = 0
        self.fails = 0
        self.exit_code = None
        self.started = 0.0
        self.not_before = 0.0
        self.backoff = 1.0
        self.want = True


class Agent:
    def __init__(self, name: str, cores: set[int], cpu_m: float, mem_mb: float, state_dir: str):
        self.name, self.cores, self.cpu_m, self.mem_mb = name, cores, cpu_m, mem_mb
        self.dir = Path(state_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.walls = Walls(name)
        for p in self.walls.pids():                      # a restarted hand finds its machine empty: what a lost hand
            try:                                         # left behind is gone with it
                os.kill(p, signal.SIGKILL)
            except OSError:
                pass
        self.walls.remove()
        self.walled = self.walls.make(cpu_m, mem_mb)
        self.units: dict[str, Unit] = {}
        self.lock = threading.Lock()
        self.pool = ThreadPoolExecutor(8)

    # ---- the units -----------------------------------------------------------------------------------------------
    def start_unit(self, spec: dict) -> None:
        with self.lock:
            if spec["id"] in self.units:
                return
            u = Unit(spec)
            self.units[u.id] = u
        Walls(self.name, u.id).make(spec.get("limit_m"), spec.get("mem_mb"))
        self._spawn(u)

    def _spawn(self, u: Unit) -> None:
        env = {**os.environ, "OMNI_UNIT": u.id, "OMNI_MACHINE": self.name,
               **{k: str(v) for k, v in (u.spec.get("env") or {}).items()}}
        with open(self.dir / f"{u.id}.log", "ab") as log:
            u.proc = subprocess.Popen(u.spec["cmd"], stdout=log, stderr=subprocess.STDOUT, env=env,
                                      cwd=u.spec.get("cwd"), start_new_session=True)
        Walls(self.name, u.id).join(u.proc.pid)          # inside its walls before it has done any work
        if self.cores:
            try:
                os.sched_setaffinity(u.proc.pid, self.cores)
            except OSError:
                pass
        u.started, u.state, u.ready, u.fails = time.time(), "starting", False, 0

    def _kill(self, u: Unit, grace: float) -> None:
        p = u.proc
        if p is None:
            return
        try:
            os.killpg(p.pid, signal.SIGTERM)
        except OSError:
            pass
        try:
            p.wait(grace)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(p.pid, signal.SIGKILL)
            except OSError:
                pass
            p.wait(5)

    def stop_unit(self, uid: str) -> bool:
        with self.lock:
            u = self.units.pop(uid, None)
        if u is None:
            return False
        u.want = False
        self._kill(u, 3.0)
        Walls(self.name, uid).remove()
        return True

    def stop_all(self) -> int:
        with self.lock:
            ids = list(self.units)
        for uid in ids:
            self.stop_unit(uid)
        return len(ids)

    def set_limit(self, uid: str, limit_m: float) -> float | None:
        """Move a unit's CPU wall and read back what the kernel holds; None when the unit is not here."""
        with self.lock:
            u = self.units.get(uid)
            if u is None:
                return None
            u.spec["limit_m"] = limit_m                  # a unit started again keeps the wall it was given
        w = Walls(self.name, uid)
        w.set_cpu(limit_m)
        return w.cpu_limit_m()

    # ---- the watch -----------------------------------------------------------------------------------------------
    def supervise(self) -> None:
        while True:
            now = time.time()
            with self.lock:
                units = [u for u in self.units.values() if u.want]
            probes = {}
            for u in units:
                if u.proc is None:
                    if now >= u.not_before:
                        self._spawn(u)
                    continue
                code = u.proc.poll()
                if code is not None:
                    u.exit_code, u.ready, u.proc = code, False, None
                    if u.kind == "task" and code == 0:
                        u.state, u.want = "succeeded", False
                    elif u.kind == "task" and u.restarts >= 2:
                        u.state, u.want = "failed", False
                    else:
                        u.restarts += 1
                        u.state = "crashed"
                        u.not_before = now + u.backoff
                        u.backoff = min(30.0, u.backoff * 2)
                    continue
                if u.kind == "task":
                    u.state = "running"
                elif u.spec.get("health"):
                    probes[u.id] = self.pool.submit(probe, u.spec["port"], u.spec["health"])
            for u in units:
                f = probes.get(u.id)
                if f is None:
                    continue
                if f.result():
                    u.ready, u.fails, u.state = True, 0, "running"
                    if now - u.started > 60:
                        u.backoff = 1.0                  # a unit that has held for a minute starts its waits afresh
                else:
                    u.fails += 1
                    if (u.ready and u.fails >= 3) or (not u.ready and now - u.started > 30):
                        u.ready, u.state = False, "unhealthy"
                        self._kill(u, 0.5)               # the next watch sees it end and starts it again
            time.sleep(0.5)

    def status(self) -> dict:
        with self.lock:
            units = list(self.units.values())
        return {"machine": self.name, "cpu_m": self.cpu_m, "mem_mb": self.mem_mb, "walled": self.walled,
                "cores": sorted(self.cores), "cpu_s": self.walls.cpu_s(), "time": time.time(),
                "units": [{"id": u.id, "kind": u.kind, "state": u.state, "ready": u.ready, "restarts": u.restarts,
                           "pid": u.proc.pid if u.proc else None, "port": u.spec.get("port"),
                           "exit_code": u.exit_code, "cpu_s": Walls(self.name, u.id).cpu_s(),
                           "limit_m": Walls(self.name, u.id).cpu_limit_m()} for u in units]}


def serve(agent: Agent, port: int) -> None:
    class Handler(BaseHTTPRequestHandler):
        def _send(self, code: int, obj) -> None:
            body = json.dumps(obj).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _body(self) -> dict:
            n = int(self.headers.get("Content-Length") or 0)
            return json.loads(self.rfile.read(n) or b"{}")

        def do_GET(self):
            if self.path == "/status":
                self._send(200, agent.status())
            else:
                self._send(404, {"error": "no such path"})

        def do_POST(self):
            if self.path == "/units":
                agent.start_unit(self._body())
                self._send(200, {"ok": True})
            elif self.path.startswith("/units/") and self.path.endswith("/limit"):
                got = agent.set_limit(self.path.split("/")[2], float(self._body()["limit_m"]))
                self._send(200 if got is not None else 404, {"limit_m": got})
            elif self.path == "/stop_all":
                self._send(200, {"stopped": agent.stop_all()})
            else:
                self._send(404, {"error": "no such path"})

        def do_DELETE(self):
            if self.path.startswith("/units/"):
                self._send(200, {"stopped": agent.stop_unit(self.path.split("/", 2)[2])})
            else:
                self._send(404, {"error": "no such path"})

        def log_message(self, *a):
            pass

    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    srv.daemon_threads = True
    srv.serve_forever(poll_interval=0.2)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--name", required=True)
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--cores", default="", help="the machine's cores, e.g. 0 or 0,1 (empty: any)")
    ap.add_argument("--cpu-m", type=float, required=True, help="the machine's processor, millicores")
    ap.add_argument("--mem-mb", type=float, default=2048)
    ap.add_argument("--state-dir", required=True)
    a = ap.parse_args(argv)
    cores = {int(c) for c in a.cores.split(",") if c.strip()}
    agent = Agent(a.name, cores, a.cpu_m, a.mem_mb, a.state_dir)
    threading.Thread(target=agent.supervise, daemon=True).start()
    signal.signal(signal.SIGTERM, lambda *_: (agent.stop_all(), agent.walls.remove(), os._exit(0)))
    serve(agent, a.port)


if __name__ == "__main__":
    main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
