# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine fingerprints (tools/omni_version.py): a checkout reads as exactly one version, or as a version minus the
runners not yet written at that commit, or as no version at all. No result is ever read across versions."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import omni_version as ov  # noqa: E402


class Fingerprints(unittest.TestCase):
    def test_the_checkout_carries_a_declared_version(self):
        files = ov.engine_files()
        self.assertIsNotNone(ov.version_of(files), "the engine in this checkout matches no declared fingerprint")
        self.assertEqual(ov.version_before(files), (None, []))

    def test_every_declared_fingerprint_is_its_own_digest(self):
        for v, path in ov.VERSIONS.items():
            want = json.loads(path.read_text())
            self.assertEqual(want["version"], f"omni-{v}")
            self.assertEqual(ov.digest(want["files"]), want["digest"], v)

    def test_a_commit_before_a_runner_was_written_reads_as_that_version_minus_the_runner(self):
        want = json.loads(ov.VERSIONS["v1"].read_text())["files"]
        files = {n: h for n, h in want.items() if n != "tools/run_pandapower.py"}
        self.assertIsNone(ov.version_of(files))           # not the whole fingerprint
        self.assertEqual(ov.version_before(files), ("omni-v1", ["tools/run_pandapower.py"]))

    def test_one_changed_byte_is_no_version(self):
        want = json.loads(ov.VERSIONS["v1"].read_text())["files"]
        files = dict(want); files["omnicompass/compass_law.py"] = "0" * 64
        self.assertIsNone(ov.version_of(files))
        self.assertEqual(ov.version_before(files), (None, []))
        files.pop("tools/run_pandapower.py")               # a subset with one wrong byte is no version either
        self.assertEqual(ov.version_before(files), (None, []))

    def test_an_extra_engine_file_is_no_version(self):
        want = json.loads(ov.VERSIONS["v3"].read_text())["files"]
        files = dict(want); files["realms/new_rule.py"] = "1" * 64
        self.assertIsNone(ov.version_of(files))
        self.assertEqual(ov.version_before(files), (None, []))


def main():
    r = unittest.TextTestRunner(verbosity=0, stream=open("/dev/null", "w")).run(unittest.defaultTestLoader.loadTestsFromTestCase(Fingerprints))
    assert r.wasSuccessful(), f"{len(r.failures)} failures, {len(r.errors)} errors in tests/test_omni_version.py"
    print("PASS  engine fingerprints: this checkout is one declared version; a commit before a runner was written reads as that version "
          "minus the runner; a changed byte or an extra engine file is no version")


if __name__ == "__main__":
    main()
