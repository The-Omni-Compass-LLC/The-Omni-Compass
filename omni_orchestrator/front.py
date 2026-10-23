# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One address for a service: its own process, so the service answers while the control plane is down.

Every request joins one line; each ready unit has one hand (a thread with one kept-open connection) that takes the next
request from the line, hands it to its unit and waits for the answer, so a unit works on one request at a time and the
waiting happens here, where it is measured. The units are read from the routes file the control plane writes (only
ready units are in it). A unit that fails to answer sends the request back to the head of the line for another unit
(three tries in all) and rests half a second before taking work again; a unit that leaves the routes finishes the
request in hand and takes no more.

HTTP on 127.0.0.1:<port>: any GET is the service's (GET /work?n=...); GET /_stats is this front's own reading: the
answers of the last 5 and 10 s (count, failures, the 50th, 95th and 99th percentiles of the response time), the line's
length and the hands working; GET /_stats?since=<seq> adds every answer's response time after that sequence number
(the pieces of work the control plane's verdict measures a trial on). Every second the same reading is appended to the
stats file.
"""
from __future__ import annotations

import argparse
import collections
import http.client
import json
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def pct(xs: list[float], q: float) -> float:
    if not xs:
        return 0.0
    s = sorted(xs)
    return s[min(len(s) - 1, int(q * len(s)))]


class Job:
    __slots__ = ("path", "done", "status", "body", "tries", "t0")

    def __init__(self, path: str):
        self.path, self.done, self.status, self.body, self.tries, self.t0 = path, threading.Event(), 0, b"", 0, time.time()


class Hand(threading.Thread):
    def __init__(self, front: "Front", uid: str, host: str, port: int):
        super().__init__(daemon=True)
        self.front, self.uid, self.host, self.port, self.alive = front, uid, host, port, True

    def run(self):
        conn = None
        misses = 0
        while self.alive:
            j = self.front.take(self)
            if j is None:
                break
            try:
                if conn is None:
                    conn = http.client.HTTPConnection(self.host, self.port, timeout=15)
                conn.request("GET", j.path)
                r = conn.getresponse()
                j.body, j.status = r.read(), r.status
                j.done.set()
                misses = 0
            except Exception:
                if conn is not None:
                    conn.close()
                    conn = None
                j.tries += 1
                if j.tries < 3:
                    self.front.requeue(j)
                else:
                    j.status, j.body = 502, b"no unit answered"
                    j.done.set()
                misses += 1
                time.sleep(0.5 if misses < 3 else 2.0)
        if conn is not None:
            conn.close()


class Front:
    def __init__(self, routes: str, service: str, stats_path: str):
        self.routes, self.service, self.stats_path = Path(routes), service, Path(stats_path)
        self.line: collections.deque[Job] = collections.deque()
        self.cv = threading.Condition()
        self.hands: dict[str, Hand] = {}
        self.done: collections.deque = collections.deque(maxlen=200_000)   # (time, ms, ok)
        self.recent: collections.deque = collections.deque(maxlen=20_000)  # (seq, ms) of the answers, for the verdict
        self.seq = 0
        self.mtime = 0.0
        self.busy = 0

    def submit(self, path: str) -> Job:
        j = Job(path)
        with self.cv:
            self.line.append(j)
            self.cv.notify()
        if not j.done.wait(30):
            j.status, j.body = 504, b"no answer in 30 s"
        ms = 1000.0 * (time.time() - j.t0)
        self.done.append((time.time(), ms, j.status == 200))
        if j.status == 200:
            with self.cv:
                self.seq += 1
                self.recent.append((self.seq, ms))
        return j

    def since(self, seq: int) -> dict:
        """The response times of every answer after sequence number seq (the last 5,000 at most), and the newest seq."""
        with self.cv:
            xs = [ms for s, ms in self.recent if s > seq]
            return {"seq": self.seq, "recent": [round(x, 2) for x in xs[-5000:]]}

    def take(self, hand: Hand) -> Job | None:
        with self.cv:
            while hand.alive and not self.line:
                self.cv.wait(0.5)
            if not hand.alive:
                return None
            return self.line.popleft()

    def requeue(self, j: Job) -> None:
        with self.cv:
            self.line.appendleft(j)
            self.cv.notify()

    def read_routes(self) -> None:
        try:
            m = self.routes.stat().st_mtime
        except OSError:
            return
        if m == self.mtime:
            return
        self.mtime = m
        try:
            units = {u["id"]: u for u in json.loads(self.routes.read_text()).get(self.service, []) if u.get("ready")}
        except (OSError, ValueError):
            return
        for uid, u in units.items():
            if uid not in self.hands:
                h = Hand(self, uid, u.get("host", "127.0.0.1"), int(u["port"]))
                self.hands[uid] = h
                h.start()
        for uid in [x for x in self.hands if x not in units]:
            self.hands.pop(uid).alive = False
        with self.cv:
            self.cv.notify_all()

    def reading(self) -> dict:
        now = time.time()
        out = {"t": now, "line": len(self.line), "hands": len(self.hands)}
        for w in (1, 5, 10):
            xs = [(ms, ok) for t, ms, ok in list(self.done) if t >= now - w]
            ok_ms = [ms for ms, ok in xs if ok]
            out[f"n_{w}s"] = len(xs)
            out[f"fail_{w}s"] = sum(1 for _, ok in xs if not ok)
            out[f"p50_{w}s"] = round(pct(ok_ms, 0.50), 1)
            out[f"p95_{w}s"] = round(pct(ok_ms, 0.95), 1)
            out[f"p99_{w}s"] = round(pct(ok_ms, 0.99), 1)
        return out

    def loop(self) -> None:
        nxt = time.time()
        while True:
            self.read_routes()
            if time.time() >= nxt:
                with open(self.stats_path, "a") as f:
                    f.write(json.dumps(self.reading()) + "\n")
                nxt += 1.0
            time.sleep(0.2)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--service", required=True)
    ap.add_argument("--routes", required=True)
    ap.add_argument("--stats", required=True)
    a = ap.parse_args(argv)
    front = Front(a.routes, a.service, a.stats)

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def do_GET(self):
            if self.path == "/_stats" or self.path.startswith("/_stats?"):
                q = urllib.parse.parse_qs(urllib.parse.urlsplit(self.path).query)
                out = front.reading()
                if "since" in q:
                    out.update(front.since(int(q["since"][0])))
                body, code = json.dumps(out).encode(), 200
            else:
                j = front.submit(self.path)
                body, code = j.body, j.status
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    threading.Thread(target=front.loop, daemon=True).start()
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    srv.daemon_threads = True
    srv.request_queue_size = 256
    srv.serve_forever(poll_interval=0.2)


if __name__ == "__main__":
    main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
