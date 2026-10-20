# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The control panel (tools/omni_control.py): every button behind a token and a role, every press logged, every change
made through the governor's own hand-back, the kill switch for every governor, the two-person arm."""
import json, os, sys, tempfile, textwrap, threading, time, unittest, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.omni_control as C

FAKE = textwrap.dedent(f"""
    import json, os, sys, time
    sys.path.insert(0, {str(ROOT)!r})
    from omnicompass import master
    args = sys.argv[1:]
    kill = args[args.index("--kill-file") + 1]
    out = os.environ["FAKE_OUT"]
    with open(out, "a") as f:
        f.write(json.dumps({{"start": args}}) + "\\n")
    while True:
        if os.path.exists(kill) or master.is_off():
            with open(out, "a") as f:
                f.write(json.dumps({{"handed_back": True}}) + "\\n")
            sys.exit(0)
        time.sleep(0.02)
""")


class Panel(unittest.TestCase):
    def setUp(self):
        self.d = Path(tempfile.mkdtemp())
        self.env = {k: os.environ.get(k) for k in ("OMNI_MASTER_OFF", "OMNI_REGISTRY", "FAKE_OUT")}
        os.environ["OMNI_MASTER_OFF"] = str(self.d / "switch" / "OFF")
        os.environ["OMNI_REGISTRY"] = str(self.d / "switch" / "running")
        os.environ["FAKE_OUT"] = str(self.d / "fake.jsonl")
        (self.d / "fake.py").write_text(FAKE)
        self.tokens = self.d / "tokens.json"
        self.tok = {n: C.make_token(self.tokens, n, r) for n, r in
                    (("vera", ["viewer"]), ("otto", ["operator"]), ("sam", ["security"]), ("sue", ["security"]))}
        self.panel = C.Panel([sys.executable, str(self.d / "fake.py")], self.d / "panel.kill", self.d / "state.json",
                             self.d / "control.jsonl", handback_s=10)
        self.srv = C.server(self.panel, self.tokens, "127.0.0.1", 0)
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self.srv.server_address[1]}"

    def tearDown(self):
        with self.panel.lock:
            self.panel._hand_back()
        self.srv.shutdown(); self.srv.server_close()
        for k, v in self.env.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def call(self, path, who=None, body=None):
        req = urllib.request.Request(self.url + path, data=None if body is None else json.dumps(body).encode(),
                                     method="GET" if body is None else "POST")
        if who:
            req.add_header("Authorization", "Bearer " + self.tok[who])
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read().decode()
                return r.status, (json.loads(raw) if r.headers.get_content_type() == "application/json" else raw)
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read().decode())

    def starts(self):
        p = Path(os.environ["FAKE_OUT"])
        return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []

    def test_reads_need_a_token_and_the_console_and_document_do_not(self):
        self.assertEqual(self.call("/v1/status")[0], 401)
        code, page = self.call("/")
        self.assertEqual(code, 200); self.assertIn("Kill switch", page); self.assertIn("www.omni-compass.com", page)
        code, doc = self.call("/v1/openapi.json")
        self.assertEqual(code, 200)
        self.assertTrue({f"/v1/{b}" for b in C.BUTTONS} <= set(doc["paths"]))
        code, st = self.call("/v1/status", "vera")
        self.assertEqual((code, st["master_switch"], st["desired"]["mode"]), (200, "ON", "off"))

    def test_a_viewer_cannot_press_and_the_refusal_is_logged(self):
        code, out = self.call("/v1/mode", "vera", {"mode": "autopilot"})
        self.assertEqual(code, 403)
        last = self.panel.presses()[-1]
        self.assertEqual((last["who"], last["button"], last["outcome"]), ("vera", "mode", "refused"))
        self.assertEqual(self.starts(), [])

    def test_every_change_goes_through_the_governors_own_hand_back(self):
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 200)
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "watch"})[0], 200)
        self.assertEqual(self.call("/v1/dial", "otto", {"dial": "save"})[0], 200)
        t0 = time.time()
        while len(self.starts()) < 5 and time.time() - t0 < 10:      # the last start is written once the child is up
            time.sleep(0.05)
        ev = self.starts()
        self.assertEqual([("start" if "start" in e else "back") for e in ev], ["start", "back", "start", "back", "start"])
        first, watch, save = ev[0]["start"], ev[2]["start"], ev[4]["start"]
        self.assertNotIn("--dry-run", first); self.assertEqual(first[first.index("--dial") + 1], "max")
        self.assertIn("--dry-run", watch)
        self.assertEqual(save[save.index("--dial") + 1], "save"); self.assertIn("--dry-run", save)
        self.assertEqual(json.loads((self.d / "state.json").read_text())["dial"], "save")

    def test_reset_needs_a_reason_then_hands_back_and_stops(self):
        self.call("/v1/mode", "otto", {"mode": "autopilot"})
        self.assertEqual(self.call("/v1/reset", "otto", {})[0], 400)
        code, out = self.call("/v1/reset", "otto", {"reason": "maintenance window"})
        self.assertEqual((code, out["mode"], out["reset"]["handed_back"]), (200, "off", True))
        self.assertFalse(self.panel.running())

    def test_the_kill_switch_is_security_only_and_holds_until_two_arm_it(self):
        self.call("/v1/mode", "otto", {"mode": "autopilot"})
        self.assertEqual(self.call("/v1/kill", "otto", {"reason": "x"})[0], 403)
        code, out = self.call("/v1/kill", "sam", {"reason": "drill"})
        self.assertEqual((code, out["master_switch"]), (200, "OFF"))
        time.sleep(0.3)
        self.assertFalse(self.panel.running())
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 409)       # nothing starts while OFF
        self.assertEqual(self.call("/v1/arm", "sam", {"reason": "drill over"})[0], 202)
        self.assertEqual(self.call("/v1/arm", "sam", {"reason": "again"})[0], 202)            # the same holder twice is one
        code, out = self.call("/v1/arm", "sue", {"reason": "drill over"})
        self.assertEqual((code, out["master_switch"], out["armed_by"]), (200, "ON", ["sam", "sue"]))
        self.assertEqual(self.call("/v1/mode", "otto", {"mode": "autopilot"})[0], 200)

    def test_every_press_is_logged_with_its_holder(self):
        self.call("/v1/mode", "otto", {"mode": "watch", "reason": "trial"})
        self.call("/v1/mode", "otto", {"mode": "bogus"})
        log = self.panel.presses()
        self.assertEqual([(x["who"], x["button"], x["outcome"]) for x in log],
                         [("otto", "mode", "done"), ("otto", "mode", "refused")])
        self.assertEqual(log[0]["reason"], "trial")
        code, page = self.call("/metrics", "vera")
        self.assertIn('omni_control_presses_total{button="mode",outcome="done"} 1', page)
        self.assertIn('omni_control_mode{mode="watch"} 1', page)

    def test_tokens_are_kept_as_digests_only(self):
        stored = self.tokens.read_text()
        for t in self.tok.values():
            self.assertNotIn(t, stored)
        self.assertEqual(oct(self.tokens.stat().st_mode & 0o777), "0o600")

    def test_a_bind_beyond_the_loopback_needs_https(self):
        with self.assertRaises(SystemExit):
            C.server(self.panel, self.tokens, "0.0.0.0", 0)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
