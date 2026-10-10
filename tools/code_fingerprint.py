# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# All patents, copyrights and trademarks filed in the USA. Evaluation and simulation use only; any commercialization,
# monetization or other use requires a signed, paid Omni-Compass Enterprise License. Subject to change at any time;
# www.omni-compass.com is the authority of record. See LICENSE, NOTICE and DISCLOSURES.md.
"""SHA-256 of a Python file's syntax tree with comments and docstrings removed."""
import ast, hashlib, sys


def strip_docstrings(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            b = node.body
            if b and isinstance(b[0], ast.Expr) and isinstance(getattr(b[0], "value", None), ast.Constant) \
                    and isinstance(b[0].value.value, str):
                node.body = b[1:] or [ast.Pass()]
    return tree


def fingerprint(path):
    tree = strip_docstrings(ast.parse(open(path, encoding="utf-8").read()))
    return hashlib.sha256(ast.dump(tree, include_attributes=False).encode()).hexdigest()


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(fingerprint(p), p)
