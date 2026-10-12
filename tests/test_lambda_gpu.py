# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Lambda launcher (scripts/lambda_gpu.py) against a stand-in for Lambda's API on this machine: it prices before it
rents, refuses over the cost ceiling or with no machine free, rents in a region with a machine free, waits until the
machine runs, lists our machines with their age, gives them back, and never prints the key. Nothing leaves this machine.
"""
import contextlib
import io
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

KEY = "secret-key-never-printed-123"
STATE = {"instances": {}, "polls": 0, "capacity": True, "auth_ok": True}


class FakeLambda(BaseHTTPRequestHandler):
    def log_message(self, *a):                       # quiet
        pass

    def reply(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def authed(self):
        if self.headers.get("Authorization") != f"Bearer {KEY}":
            self.reply(401, {"error": {"code": "global/invalid-api-key", "message": "bad key"}})
            return False
        return True

    def do_GET(self):
        if not self.authed():
            return
        if self.path == "/api/v1/instance-types":
            regions = [{"name": "us-east-1", "description": "Virginia"}] if STATE["capacity"] else []
            self.reply(200, {"data": {
                "gpu_8x_a100_80gb_sxm4": {"instance_type": {"name": "gpu_8x_a100_80gb_sxm4", "price_cents_per_hour": 1432},
                                          "regions_with_capacity_available": regions},
                "gpu_1x_a10": {"instance_type": {"name": "gpu_1x_a10", "price_cents_per_hour": 75},
                               "regions_with_capacity_available": regions}}})
        elif self.path == "/api/v1/instances":
            self.reply(200, {"data": list(STATE["instances"].values())})
        elif self.path.startswith("/api/v1/instances/"):
            i = self.path.rsplit("/", 1)[1]
            d = STATE["instances"].get(i)
            if d is None:
                self.reply(404, {"error": {"code": "global/object-does-not-exist", "message": "no such instance"}})
                return
            STATE["polls"] += 1
            if STATE["polls"] >= 2 and d["status"] == "booting":
                d.update(status="active", ip="203.0.113.7")
            self.reply(200, {"data": d})
        else:
            self.reply(404, {"error": {"code": "not-found", "message": self.path}})

    def do_POST(self):
        if not self.authed():
            return
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if self.path == "/api/v1/instance-operations/launch":
            assert body["ssh_key_names"] == ["omni-key"] and body["quantity"] == 1
            i = f"inst{len(STATE['instances']) + 1}"
            STATE["instances"][i] = {"id": i, "name": body["name"], "status": "booting", "ip": None,
                                     "region": {"name": body["region_name"]}}
            self.reply(200, {"data": {"instance_ids": [i]}})
        elif self.path == "/api/v1/instance-operations/terminate":
            gone = []
            for i in body["instance_ids"]:
                if i in STATE["instances"]:
                    STATE["instances"][i]["status"] = "terminated"
                    gone.append({"id": i})
            self.reply(200, {"data": {"terminated_instances": gone}})
        else:
            self.reply(404, {"error": {"code": "not-found", "message": self.path}})


def run(argv):
    import lambda_gpu
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        try:
            rc = lambda_gpu.main(argv)
        except SystemExit as e:
            rc = e.code
    return rc, out.getvalue()


def test_lambda_launcher_end_to_end():
    srv = HTTPServer(("127.0.0.1", 0), FakeLambda)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    os.environ["LAMBDA_API"] = f"http://127.0.0.1:{srv.server_address[1]}/api/v1"
    for v in ("NO_PROXY", "no_proxy"):                # the stand-in is on this machine: never through a proxy
        os.environ[v] = ",".join(x for x in (os.environ.get(v, ""), "127.0.0.1", "localhost") if x)
    os.environ["LAMBDA_API_KEY"] = KEY
    import importlib
    import lambda_gpu
    importlib.reload(lambda_gpu)                     # pick up LAMBDA_API
    try:
        printed = ""
        rc, o = run(["plan", "--type", "gpu_8x_a100_80gb_sxm4", "--hours", "11.5", "--max-cost", "400"]); printed += o
        assert rc == 0 and "$14.32 an hour" in o and "us-east-1" in o and "$164.68" in o, o
        rc, o = run(["plan", "--type", "gpu_8x_a100_80gb_sxm4", "--hours", "27", "--max-cost", "300"]); printed += o
        assert rc == 6 and "nothing rented" in o, o                                   # over the ceiling
        rc, o = run(["plan", "--type", "gpu_9x_imaginary", "--hours", "1"]); printed += o
        assert rc == 4, o                                                             # unknown type
        STATE["capacity"] = False
        rc, o = run(["plan", "--type", "gpu_1x_a10", "--hours", "9"]); printed += o
        assert rc == 3 and "nowhere" in o, o                                          # no machine free
        rc, o = run(["launch", "--type", "gpu_1x_a10", "--name", "omni-1card-1-8", "--ssh-key-name", "omni-key"])
        printed += o
        assert rc == 3 and not STATE["instances"], o                                  # never rents blind
        STATE["capacity"] = True
        name = f"omni-8card-{int(time.time()) - 7200}-10"
        rc, o = run(["launch", "--type", "gpu_8x_a100_80gb_sxm4", "--name", name, "--ssh-key-name", "omni-key"])
        printed += o
        assert rc == 0 and o.strip() == "inst1" and STATE["instances"]["inst1"]["region"]["name"] == "us-east-1", o
        rc, o = run(["wait", "inst1", "--timeout", "10", "--every", "0.01"]); printed += o
        assert rc == 0 and o.strip() == "203.0.113.7", o                              # booting, then running
        rc, o = run(["list"]); printed += o
        assert rc == 0 and "inst1" in o and " 2.00h" in o, o                          # its age, from its name
        rc, o = run(["terminate", "inst1"]); printed += o
        assert rc == 0 and "inst1" in o and STATE["instances"]["inst1"]["status"] == "terminated", o
        rc, o = run(["wait", "inst1", "--timeout", "1", "--every", "0.01"]); printed += o
        assert rc == 5, o                                                             # a given-back machine never runs
        os.environ["LAMBDA_API_KEY"] = "wrong"
        rc, o = run(["list"]); printed += o
        assert rc == 2 and "HTTP 401" in o, o                                         # a refused key is reported
        assert KEY not in printed and "wrong" not in printed, "the key must never be printed"
    finally:
        os.environ["LAMBDA_API_KEY"] = KEY
        srv.shutdown()


if __name__ == "__main__":
    test_lambda_launcher_end_to_end()
    print("test_lambda_gpu: OK")
