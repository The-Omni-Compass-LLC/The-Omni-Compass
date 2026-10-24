#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Azure's key, its shape read before Azure's login, so a key cut short or stored in the wrong form is named at no cost.

  python3 tools/cloud_key_check.py azure     AZURE_CREDENTIALS whole, or the four boxes (AZURE_CLIENT_ID, AZURE_TENANT_ID,
                                             AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_SECRET)

For a while on the night of 21 October AZURE_CREDENTIALS held a text that is not the JSON block Azure's login takes (a
collect failed at 23:37 UTC; the block was whole again by 00:00), and Azure's own login step quoted its first characters on
the run's page while refusing it. This reads the key from the environment and prints only what is wrong with its shape: how
many characters were stored, which fields or boxes are missing, where the JSON stops, what the stored text looks like. It
never prints a character of the key, and it runs before Azure's own login step, so a key in the wrong form never reaches a
step that would quote it. Exit 0: a whole key, handed to the login masked. Exit 2: what is wrong, and what to store again
(docs/AZURE_SETUP.md, section 7)."""
from __future__ import annotations

import json
import os
import sys

def n_lines(raw: str) -> int:
    return raw.count("\n") + 1


def before_brace(raw: str) -> str:
    """Words for a text that holds a { but not at its start: something was pasted in front of the key (a name, a quote, a
    word), counted, never shown. Empty when there is no { or it stands first."""
    i = raw.find("{")
    if i <= 0:
        return ""
    return (f"{i} character{'s stand' if i != 1 else ' stands'} before its first {{ (a name, a quotation mark or a word "
            "pasted with it): store only from { to }")


def shape_words(raw: str) -> str:
    """The stored text's outline, so the person can tell which text it was: its lines, and whether it holds spaces, a web
    address or quotation marks. Never a character of it."""
    n = n_lines(raw)
    bits = [f"{n} line{'s' if n != 1 else ''}"]
    marks = [w for w, hit in (("spaces", " " in raw), ("a web address", "://" in raw), ("quotation marks", '"' in raw))
             if hit]
    bits.append(("with " + ", ".join(marks) + " in it") if marks else "no spaces")
    return "; it is " + ", ".join(bits)


# Azure: the block `az ad sp create-for-rbac ... --sdk-auth` prints (docs/AZURE_SETUP.md, section 3), the form azure/login's
# creds input takes; its four fields that login reads
AZURE_FIELDS = ("clientId", "clientSecret", "subscriptionId", "tenantId")
AZURE_WHOLE = "the whole block is about 400 to 700 characters on about ten lines, from { to }"


def _guid(s: str) -> bool:
    parts = s.split("-")
    return [len(x) for x in parts] == [8, 4, 4, 4, 12] and all(all(c in "0123456789abcdefABCDEF" for c in x) for x in parts)


def azure_what_it_holds(raw: str) -> str:
    """What a stored text that is not the JSON block looks like, from its shape alone (never a character of it)."""
    if before_brace(raw):
        return before_brace(raw)
    if any(f'"{f}"' in raw for f in AZURE_FIELDS):
        return "it holds a piece from inside the block (its first line, the {, is missing): the copy started part of the way in"
    one = raw.strip()
    if len(one) == 88 and one.endswith("==") and all(c.isalnum() or c in "+/=" for c in one):
        return ("it looks like a storage account's access key (88 characters, encoded: the size Azure gives every storage "
                "and database account key, from a storage account's Access keys page), not the block: such a key opens one "
                "storage account, never the subscription")
    if _guid(one):
        return ("it holds one identifier alone (an application, tenant or subscription ID, a 36-character GUID), not the "
                "whole block")
    if "\n" not in one and " " not in one and 30 <= len(one) <= 48:
        return ("it looks like a client secret's value alone (one line, no { or }): Azure's login needs the whole block that "
                "the line in section 3 prints, the secret one of its fields")
    if "=" in one and ";" in one:
        return "it looks like a connection string, not the block"
    return "it is not the block" + shape_words(one)


def azure_problems(raw: str | None) -> list[str]:
    """What is wrong with a stored AZURE_CREDENTIALS, in words that carry none of its characters (empty: whole)."""
    raw = (raw or "").strip()
    if not raw:
        return ["the secret is empty"]
    n = len(raw)
    if not raw.startswith("{"):
        return [f"it does not start with {{ ({n} characters stored; {AZURE_WHOLE}); {azure_what_it_holds(raw)}"]
    if not raw.endswith("}"):
        return [f"it does not end with }}: it was cut short when it was copied ({n} characters stored; {AZURE_WHOLE})"]
    try:
        block = json.loads(raw)
    except ValueError as e:
        where = getattr(e, "pos", None)
        return [f"it is not whole JSON (it breaks at character {where} of {n}): it was cut or changed when it was copied"]
    if not isinstance(block, dict):
        return ["it is not the block (not one JSON object)"]
    out = []
    missing = [f for f in AZURE_FIELDS if not str(block.get(f) or "").strip()]
    if missing:
        out.append("fields missing: " + ", ".join(missing))
    bad_ids = [f for f in ("clientId", "subscriptionId", "tenantId") if f not in missing and not _guid(str(block[f]).strip())]
    if bad_ids:
        out.append("not a 36-character GUID: " + ", ".join(bad_ids))
    return out


# Azure's four boxes (24 October): the same login typed one value to a box, as the portal shows each value on its own, so no
# block is assembled by hand. The three IDs are the boxes the sign-in without a password already reads (docs/AZURE_SETUP.md,
# section 8); the password is AZURE_CLIENT_SECRET, or AZURE_CREDENTIALS when that box holds a password's value alone.
AZURE_BOXES = (("AZURE_CLIENT_ID", "clientId", "the Application (client) ID"),
               ("AZURE_TENANT_ID", "tenantId", "the Directory (tenant) ID"),
               ("AZURE_SUBSCRIPTION_ID", "subscriptionId", "the Subscription ID"))


def _secret_value(s: str) -> bool:
    """A client secret's value as the portal's Value column gives it: one line of 30 to 48 characters, no spaces, no { },
    and not an ID (the Secret ID column beside it is a 36-character GUID, never the password; a storage account's key is
    88 characters)."""
    return bool(s) and not _guid(s) and not s.startswith("{") and " " not in s and "\n" not in s and 30 <= len(s) <= 48


def azure_login(env) -> tuple[str | None, str, list[str]]:
    """The block azure/login's creds takes, from AZURE_CREDENTIALS whole or from the four boxes: (block, where it came from,
    problems). Every problem names a box and what is wrong with its shape, never a character of it."""
    raw = (env.get("AZURE_CREDENTIALS") or "").strip()
    one = azure_problems(raw)
    if not one:
        return json.dumps(json.loads(raw), separators=(",", ":")), "AZURE_CREDENTIALS, the whole block", []
    secret = (env.get("AZURE_CLIENT_SECRET") or "").strip()
    secret_box = "AZURE_CLIENT_SECRET"
    if not secret and _secret_value(raw):
        secret, secret_box = raw, "AZURE_CREDENTIALS"
    four, block = [], {}
    for box, field, what in AZURE_BOXES:
        v = (env.get(box) or "").strip()
        if not v:
            four.append(f"{box} is empty (it takes {what}, a 36-character ID)")
        elif not _guid(v):
            four.append(f"{box} is not a 36-character ID ({len(v)} characters stored; it takes {what})")
        else:
            block[field] = v
    if not secret:
        four.append("AZURE_CLIENT_SECRET is empty (it takes the password's Value from Certificates & secrets, about 40 "
                    "characters)")
    elif _guid(secret):
        four.append(f"{secret_box} holds a 36-character ID, not a password: on Certificates & secrets copy the Value column, "
                    "never the Secret ID beside it")
    elif not _secret_value(secret):
        four.append(f"{secret_box} is not a password's value ({len(secret)} characters stored, {n_lines(secret)} line(s))")
    else:
        block["clientSecret"] = secret
    if not four:
        block = {f: block[f] for f in AZURE_FIELDS}
        return json.dumps(block, separators=(",", ":")), f"the four boxes (the password from {secret_box})", []
    return None, "", ["AZURE_CREDENTIALS: " + "; ".join(one), "the four boxes: " + "; ".join(four)]


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if args[:1] == ["azure"]:
        block, where, bad = azure_login(os.environ)
        if block:
            print(f"Azure's login: whole, from {where}")
            out = os.environ.get("GITHUB_ENV")
            if out:
                # the next step's azure/login reads it as env.AZ_CREDS; masked first, so no log line can carry it
                print(f"::add-mask::{block}")
                with open(out, "a", encoding="utf-8") as fh:
                    fh.write(f"AZ_CREDS={block}\n")
            return 0
        for b in bad:
            print(f"::error::{b}.")
        print("::error::Nothing built, nothing billed. Fill either way (docs/AZURE_SETUP.md, section 7): the four boxes, one "
              "value each, from the app's Overview page, its Certificates & secrets and the subscription; or "
              "AZURE_CREDENTIALS with the whole block from { to }.")
        return 2
    print("usage: python3 tools/cloud_key_check.py azure")
    return 2

if __name__ == "__main__":
    sys.exit(main())
