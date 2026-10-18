#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Google key's shape, read before Google's login, so a key cut short when it was copied is named at no cost.

On 18 October the stored GCP_CREDENTIALS ended part of the way through (it had been selected from Cloud Shell's screen),
and every Google set failed at the login with Google's "unexpected end of JSON input". This reads the key from the
environment (GCP_CREDENTIALS, and GCP_PROJECT to compare) and prints only what is wrong with its shape: how many characters
were stored, which fields are missing, where the JSON stops. It never prints a character of the key.
Exit 0: a whole service-account key. Exit 2: what is wrong, and what to store again (docs/GOOGLE_SETUP.md)."""
from __future__ import annotations

import json
import os
import sys

FIELDS = ("type", "project_id", "private_key_id", "private_key", "client_email", "token_uri")
WHOLE = "a whole key is about 2,300 to 2,400 characters, from { to }"


def what_it_holds(raw: str) -> str:
    """What a stored text that is not a key file looks like, read from its shape alone (never a character of it), so the
    person storing it again knows what went wrong: a piece from inside the file, the private key alone, an encoded string,
    an account name, or too little to be any of these."""
    if any(f'"{f}"' in raw for f in FIELDS):
        return "it holds a piece from inside the file (its first line, the {, is missing): the copy started part of the way in"
    if "-----BEGIN PRIVATE KEY-----" in raw or "PRIVATE KEY-----" in raw:
        return "it holds the private key alone, a part of the file; store the whole file"
    if "@" in raw and raw.count(" ") == 0 and n_lines(raw) == 1 and len(raw) < 200:
        return "it looks like an account's address, not the key file"
    if len(raw) >= 200 and all(c.isalnum() or c in "+/=\n\r" for c in raw):
        return "it looks like an encoded string (the middle of the private key, or the file encoded), not the key file"
    if len(raw) >= 100 and all(c.isalnum() or c in "-_.~+/=\n\r" for c in raw):
        return ("it looks like a token or a web-safe encoded string (an access token, for one, which expires within the "
                "hour), not the key file")
    return "it is not the key file"


def n_lines(raw: str) -> int:
    return raw.count("\n") + 1


def problems(raw: str | None, project: str = "") -> list[str]:
    """What is wrong with a stored service-account key, in words that carry none of its characters (empty: whole)."""
    raw = (raw or "").strip()
    if not raw:
        return ["the secret is empty"]
    n = len(raw)
    if not raw.startswith("{"):
        return [f"it does not start with {{ ({n} characters stored; {WHOLE}); {what_it_holds(raw)}"]
    if not raw.endswith("}"):
        return [f"it does not end with }}: it was cut short when it was copied ({n} characters stored; {WHOLE})"]
    try:
        key = json.loads(raw)
    except ValueError as e:
        where = getattr(e, "pos", None)
        return [f"it is not whole JSON (it breaks at character {where} of {n}): it was cut or changed when it was copied"]
    if not isinstance(key, dict):
        return ["it is not a key (not one JSON object)"]
    out = []
    missing = [f for f in FIELDS if not key.get(f)]
    if missing:
        out.append("fields missing: " + ", ".join(missing))
    if key.get("type") and key["type"] != "service_account":
        out.append("it is not a service-account key (its type field reads otherwise)")
    pk = str(key.get("private_key") or "")
    if pk and not ("-----BEGIN PRIVATE KEY-----" in pk and pk.rstrip().endswith("-----END PRIVATE KEY-----")):
        out.append("its private key is not whole")
    if project.strip() and key.get("project_id") and key["project_id"] != project.strip():
        out.append("its project is not the one in GCP_PROJECT (GCP_PROJECT holds the Project ID the key was made in)")
    return out


def main() -> int:
    bad = problems(os.environ.get("GCP_CREDENTIALS"), os.environ.get("GCP_PROJECT", ""))
    if not bad:
        print("GCP_CREDENTIALS: a whole service-account key")
        return 0
    for b in bad:
        print(f"::error::GCP_CREDENTIALS: {b}. Nothing built, nothing billed. Store the key again, whole: "
              "docs/GOOGLE_SETUP.md, section 4 (download the key file and paste all of it).")
    return 2


if __name__ == "__main__":
    sys.exit(main())
