#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Rent one Lambda Cloud GPU machine for one Omni-Compass GPU run, and always give it back
(.github/workflows/lambda-gpu.yml; docs/omni_v5/BENCHMARKS_V5.md, "The 8-GPU benchmark, one button").

  python3 scripts/lambda_gpu.py plan --type gpu_8x_a100_80gb_sxm4 --hours 11.5   the price, the regions with a machine
                                                                                free, the estimate; rents nothing
  python3 scripts/lambda_gpu.py launch --type T --name N --ssh-key-name K [--region R]   rents one; prints its id
  python3 scripts/lambda_gpu.py wait ID [--timeout 1800]    until it is running; prints its address
  python3 scripts/lambda_gpu.py status ID                   its state and address
  python3 scripts/lambda_gpu.py list [--prefix omni-]       our machines, with how long each has been up
  python3 scripts/lambda_gpu.py terminate ID [ID ...]       gives them back; the bill stops

The key is read from the environment (LAMBDA_API_KEY), never from the command line, and is never printed. LAMBDA_API sets
the address of the API (default https://cloud.lambdalabs.com/api/v1). A machine is named omni-<test>-<epoch>-<hours>, so
anyone listing the account can see when it was rented and the hour budget it was rented for.
Exit codes: 0 done; 2 usage or a refused request; 3 no machine of that type free anywhere; 4 unknown type; 5 not
running in time; 6 over the cost ceiling.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = os.environ.get("LAMBDA_API", "https://cloud.lambdalabs.com/api/v1").rstrip("/")


def call(method: str, path: str, body: dict | None = None) -> dict:
    key = os.environ.get("LAMBDA_API_KEY", "")
    if not key:
        sys.exit("LAMBDA_API_KEY is not set (it lives only in the repository's secrets)")
    req = urllib.request.Request(API + path, method=method,
                                 data=None if body is None else json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                          "Accept": "application/json", "User-Agent": "omni-compass-lambda-gpu"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode()).get("error", {})
            msg = f"{err.get('code', '')} {err.get('message', '')} {err.get('suggestion', '')}".strip()
        except Exception:                                        # noqa: BLE001  (the body may not be JSON)
            msg = ""
        print(f"Lambda refused {method} {path}: HTTP {e.code} {msg}", file=sys.stderr)
        sys.exit(2)
    except urllib.error.URLError as e:
        print(f"Lambda unreachable for {method} {path}: {e.reason}", file=sys.stderr)
        sys.exit(2)


def instance_types() -> dict:
    return call("GET", "/instance-types").get("data", {})


def plan(a) -> int:
    types = instance_types()
    if a.type not in types:
        print(f"unknown instance type {a.type}; offered: {', '.join(sorted(types))}")
        return 4
    t = types[a.type]
    cents = t.get("instance_type", {}).get("price_cents_per_hour", 0)
    regions = [r["name"] for r in t.get("regions_with_capacity_available", [])]
    est = cents / 100.0 * a.hours
    print(f"type {a.type}: ${cents / 100.0:.2f} an hour; free now in: {', '.join(regions) or 'nowhere'}")
    print(f"estimate for {a.hours:g} hours: ${est:.2f} (the bill stops when the machine is given back)")
    if a.max_cost and est > a.max_cost:
        print(f"over the ceiling of ${a.max_cost:.2f}: nothing rented")
        return 6
    if not regions:
        print("no machine of this type is free in any region now: nothing rented")
        return 3
    return 0


def launch(a) -> int:
    region = a.region
    if not region:
        types = instance_types()
        if a.type not in types:
            print(f"unknown instance type {a.type}")
            return 4
        free = [r["name"] for r in types[a.type].get("regions_with_capacity_available", [])]
        if not free:
            print("no machine of this type is free in any region now: nothing rented")
            return 3
        region = free[0]
    body = {"region_name": region, "instance_type_name": a.type, "ssh_key_names": [a.ssh_key_name], "quantity": 1,
            "name": a.name}
    ids = call("POST", "/instance-operations/launch", body).get("data", {}).get("instance_ids", [])
    if not ids:
        print("Lambda accepted the request but returned no machine")
        return 2
    print(ids[0])
    return 0


def status(a) -> int:
    d = call("GET", f"/instances/{a.id}").get("data", {})
    print(f"{d.get('id', a.id)} {d.get('name', '')} {d.get('status', 'unknown')} {d.get('ip') or '-'}")
    return 0


def wait(a) -> int:
    t_end = time.time() + a.timeout
    while time.time() < t_end:
        d = call("GET", f"/instances/{a.id}").get("data", {})
        st, ip = d.get("status"), d.get("ip")
        if st == "active" and ip:
            print(ip)
            return 0
        if st in ("terminated", "unhealthy"):
            print(f"machine {a.id} is {st}", file=sys.stderr)
            return 5
        time.sleep(a.every)
    print(f"machine {a.id} not running after {a.timeout} s", file=sys.stderr)
    return 5


def age_hours(name: str, now: float) -> float | None:
    parts = name.split("-")
    try:
        return (now - int(parts[2])) / 3600.0
    except (IndexError, ValueError):
        return None


def list_(a) -> int:
    now = time.time()
    for d in call("GET", "/instances").get("data", []):
        name = d.get("name") or ""
        if not name.startswith(a.prefix):
            continue
        age = age_hours(name, now)
        print(f"{d.get('id')} {name} {d.get('status')} {d.get('ip') or '-'} "
              f"{'%.2f' % age if age is not None else '?'}h")
    return 0


def terminate(a) -> int:
    done = call("POST", "/instance-operations/terminate", {"instance_ids": a.ids}).get("data", {})
    gone = [d.get("id") for d in done.get("terminated_instances", [])]
    print("given back: " + (", ".join(gone) or "none listed"))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("--type", required=True); p.add_argument("--hours", type=float, required=True)
    p.add_argument("--max-cost", type=float, default=0.0); p.set_defaults(fn=plan)
    p = sub.add_parser("launch"); p.add_argument("--type", required=True); p.add_argument("--name", required=True)
    p.add_argument("--ssh-key-name", required=True); p.add_argument("--region", default=""); p.set_defaults(fn=launch)
    p = sub.add_parser("status"); p.add_argument("id"); p.set_defaults(fn=status)
    p = sub.add_parser("wait"); p.add_argument("id"); p.add_argument("--timeout", type=float, default=1800.0)
    p.add_argument("--every", type=float, default=15.0); p.set_defaults(fn=wait)
    p = sub.add_parser("list"); p.add_argument("--prefix", default="omni-"); p.set_defaults(fn=list_)
    p = sub.add_parser("terminate"); p.add_argument("ids", nargs="+"); p.set_defaults(fn=terminate)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
