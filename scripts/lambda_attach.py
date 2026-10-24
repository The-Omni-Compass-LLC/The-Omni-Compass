#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Run the GPU benchmark on a Lambda machine that is already up, one launched by hand on Lambda's page, instead of renting
another (.github/workflows/lambda-attach.yml; the founder's words of 24 October: a card already billing is the card the run
uses).

  python3 scripts/lambda_attach.py info ID [--ip-out F]              the machine: its state, address, type, hourly price,
                                                                     region, the SSH keys it was launched with, and whether
                                                                     Lambda offers its Jupyter server (no token printed)
  python3 scripts/lambda_attach.py authorize ID --public-file F [--user-out U]
                                                                     the public key F added to the login user's
                                                                     ~/.ssh/authorized_keys through the machine's own Jupyter
                                                                     server, so the workflow can log in by SSH; the user it
                                                                     runs as is written to U; nothing else is touched
  python3 scripts/lambda_attach.py deauthorize ID --public-file F    the same key taken out again

A machine launched by hand holds the SSH key its owner chose, whose private half lives on the owner's own computer; Lambda
gives every machine a Jupyter server with its own token, read here from Lambda's API with the account's key
(LAMBDA_API_KEY, read from the environment as scripts/lambda_gpu.py reads it). The token is never printed. Exit codes: 0 done;
2 the machine is not running, or offers no way in.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lambda_gpu as L  # noqa: E402  (the same API call, its key handling and its redirect rule)


def machine(i: str) -> dict | None:
    d = L.call("GET", f"/instances/{i}", missing_ok=True)
    return None if d is None else (d.get("data") or {})


def info(a) -> int:
    d = machine(a.id)
    if d is None:
        print(f"{a.id}: Lambda knows no such machine (given back, or the id is wrong)")
        return 2
    t = d.get("instance_type") or {}
    print(f"{d.get('id')} | {d.get('name') or '(no name: launched by hand on Lambda)'} | {d.get('status')} | "
          f"{d.get('ip') or '-'} | {t.get('name')} | {t.get('price_cents_per_hour')} cents an hour | "
          f"{(d.get('region') or {}).get('name')}")
    print("launched with SSH keys: " + (", ".join(d.get("ssh_key_names") or []) or "none listed"))
    print("Jupyter server: " + ("offered" if jupyter(d) else "not offered"))
    if a.ip_out and d.get("ip"):
        with open(a.ip_out, "w", encoding="utf-8") as fh:
            fh.write(d["ip"] + "\n")
    return 0 if d.get("status") == "active" and d.get("ip") else 2


def jupyter(d: dict) -> tuple[str, str] | None:
    """The machine's Jupyter server and its token, as Lambda hands them out; https only."""
    url, tok = str(d.get("jupyter_url") or ""), str(d.get("jupyter_token") or "")
    u = urllib.parse.urlsplit(url)
    if not tok or u.scheme != "https" or not u.hostname:
        return None
    return f"https://{u.netloc}", tok


def run_code(base: str, tok: str, code: str) -> tuple[str, str]:
    """One piece of Python run in a kernel of the machine's Jupyter server; the kernel is shut down after. Returns the
    reply's status and everything the code printed."""
    import websocket  # websocket-client (pip install websocket-client), on the workflow's runner only

    def req(method: str, path: str, body: dict | None = None) -> dict:
        r = urllib.request.Request(base + path, method=method, data=None if body is None else json.dumps(body).encode(),
                                   headers={"Authorization": f"token {tok}", "Content-Type": "application/json"})
        with urllib.request.urlopen(r, timeout=60) as f:
            text = f.read().decode()
        return json.loads(text) if text else {}

    kid = req("POST", "/api/kernels", {"name": "python3"})["id"]
    try:
        ws = websocket.create_connection(base.replace("https://", "wss://", 1) + f"/api/kernels/{kid}/channels",
                                         header=[f"Authorization: token {tok}"], timeout=120, suppress_origin=True)
        mid = uuid.uuid4().hex
        ws.send(json.dumps({"header": {"msg_id": mid, "username": "omni-compass", "session": uuid.uuid4().hex,
                                       "msg_type": "execute_request", "version": "5.3", "date": ""},
                            "parent_header": {}, "metadata": {}, "channel": "shell",
                            "content": {"code": code, "silent": False, "store_history": False, "user_expressions": {},
                                        "allow_stdin": False, "stop_on_error": True}}))
        out, status = [], None
        while status is None:
            m = json.loads(ws.recv())
            if (m.get("parent_header") or {}).get("msg_id") != mid:
                continue
            kind = m.get("msg_type") or (m.get("header") or {}).get("msg_type")
            c = m.get("content") or {}
            if kind == "stream":
                out.append(c.get("text", ""))
            elif kind == "error":
                out.append(f"{c.get('ename', '')}: {c.get('evalue', '')}\n")
            elif kind == "execute_reply":
                status = c.get("status", "unknown")
        ws.close()
        return status, "".join(out)
    finally:
        try:
            req("DELETE", f"/api/kernels/{kid}")
        except Exception:  # noqa: BLE001  (a kernel left over is the machine's own; it dies with the machine)
            pass


ADD = """import getpass, os
k = {key!r}
d = os.path.expanduser("~/.ssh"); os.makedirs(d, mode=0o700, exist_ok=True)
p = os.path.join(d, "authorized_keys")
have = open(p).read() if os.path.exists(p) else ""
if k not in have.splitlines():
    with open(p, "a") as f:
        f.write(("\\n" if have and not have.endswith("\\n") else "") + k + "\\n")
os.chmod(p, 0o600)
print("LOGIN=" + getpass.getuser())
"""

REMOVE = """import os
k = {key!r}
p = os.path.expanduser("~/.ssh/authorized_keys")
if os.path.exists(p):
    keep = [l for l in open(p).read().splitlines() if l.strip() != k]
    open(p, "w").write("\\n".join(keep) + ("\\n" if keep else ""))
print("removed")
"""


def _key(path: str) -> str:
    key = open(path, encoding="utf-8").read().strip()
    if not key.startswith(("ssh-ed25519 ", "ssh-rsa ", "ecdsa-sha2-")) or "\n" in key:
        sys.exit(f"{path}: not one public key line")
    return key


def authorize(a) -> int:
    d = machine(a.id)
    j = jupyter(d or {})
    if not d or d.get("status") != "active" or not j:
        print(f"{a.id}: not running, or Lambda offers no Jupyter server on it: no way in without its owner's own key")
        return 2
    status, out = run_code(*j, ADD.format(key=_key(a.public_file)))
    login = next((l.split("=", 1)[1].strip() for l in out.splitlines() if l.startswith("LOGIN=")), "")
    if status != "ok" or not login:
        print(f"the key was not added ({status}): {out.strip()[-300:]}")
        return 2
    if a.user_out:
        with open(a.user_out, "w", encoding="utf-8") as fh:
            fh.write(login + "\n")
    print(f"this run's public key is in {login}'s authorized_keys on {a.id}")
    return 0


def deauthorize(a) -> int:
    d = machine(a.id)
    j = jupyter(d or {})
    if not d or d.get("status") != "active" or not j:
        print(f"{a.id}: not running: nothing to take out")
        return 0
    status, out = run_code(*j, REMOVE.format(key=_key(a.public_file)))
    print(f"this run's public key taken out of {a.id}: {status}")
    return 0 if status == "ok" else 2


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("info"); p.add_argument("id"); p.add_argument("--ip-out", default=""); p.set_defaults(fn=info)
    p = sub.add_parser("authorize"); p.add_argument("id"); p.add_argument("--public-file", required=True)
    p.add_argument("--user-out", default=""); p.set_defaults(fn=authorize)
    p = sub.add_parser("deauthorize"); p.add_argument("id"); p.add_argument("--public-file", required=True)
    p.set_defaults(fn=deauthorize)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
