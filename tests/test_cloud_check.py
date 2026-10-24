# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Azure's $0 check (22 October). For a while on 21 October the stored Azure key held a text Azure's login refuses, and
Azure's own login step quoted its first characters on the run's page. Now the key's shape is read before every Azure login
(never a character of it printed), from the one box or the four (24 October), the check stops before anything is built,
and the conductor starts Azure's sets only after its newest check passed. Azure is the one cloud the benchmarks rent."""
import json
import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

from scripts import dispatch_grid as grid
from tools import cloud_key_check

ROOT = Path(__file__).resolve().parents[1]
AZ_SECRET = "Xq8Q~kLm.0aB1cD2eF3gH4iJ5kL6mN7oP8qR9sT0"


def az_block(**over):
    b = {"clientId": "0b1c2d3e-1111-2222-3333-444455556666", "clientSecret": AZ_SECRET,
         "subscriptionId": "11111111-2222-3333-4444-555555555555", "tenantId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
         "activeDirectoryEndpointUrl": "https://login.microsoftonline.com", "resourceManagerEndpointUrl": "https://management.azure.com/"}
    b.update(over)
    return json.dumps(b, indent=2)


class AzureKeyShape(unittest.TestCase):
    def test_the_whole_block_passes(self):
        self.assertEqual(cloud_key_check.azure_problems(az_block()), [])

    def test_every_wrong_form_is_named_without_a_character_of_it(self):
        whole = az_block()
        cases = {AZ_SECRET: "client secret's value alone",
                 "0b1c2d3e-1111-2222-3333-444455556666": "one identifier alone",
                 whole[whole.index('"clientSecret"'):]: "piece from inside the block",
                 whole[:150]: "cut short",
                 "'" + whole + "'": "1 character stands before its first {",
                 "Ab9+" * 21 + "Xy==": "storage account's access key",
                 "see https://portal.azure.com for the key " + AZ_SECRET: "1 line, with spaces, a web address in it",
                 whole.replace('",', '"', 1): "not whole JSON",
                 json.dumps({"appId": "0b1c2d3e-1111-2222-3333-444455556666", "password": AZ_SECRET,
                             "tenant": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"}): "fields missing: clientId, clientSecret, subscriptionId, tenantId",
                 az_block(tenantId="contoso"): "not a 36-character GUID: tenantId",
                 "": "the secret is empty"}
        for raw, words in cases.items():
            with self.subTest(words=words):
                bad = " ".join(cloud_key_check.azure_problems(raw))
                self.assertIn(words, bad)
                for piece in (AZ_SECRET[:10], AZ_SECRET[-10:], "0b1c2d3e", "aaaaaaaa", "11111111"):
                    self.assertNotIn(piece, bad)

    def test_the_program_exits_two_and_prints_no_secret(self):
        for raw in (AZ_SECRET, az_block()[:300]):
            env = dict(os.environ, AZURE_CREDENTIALS=raw)
            out = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"], env=env, capture_output=True, text=True)
            self.assertEqual(out.returncode, 2)
            self.assertNotIn(AZ_SECRET[:10], out.stdout + out.stderr)
            self.assertIn("docs/AZURE_SETUP.md", out.stdout)
        env = dict(os.environ, AZURE_CREDENTIALS=az_block())
        out = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"], env=env, capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stdout)
        self.assertNotIn(AZ_SECRET[:10], out.stdout + out.stderr)

    def test_every_azure_login_reads_the_key_shape_first(self):
        """A key in another form never reaches azure/login, whose refusal quotes the stored text's first characters."""
        seen = 0
        for f in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            w = yaml.safe_load(f.read_text())
            for name, job in (w.get("jobs") or {}).items():
                steps = job.get("steps") or []
                for k, s in enumerate(steps):
                    if str(s.get("uses", "")).startswith("azure/login@"):
                        given = s.get("with") or {}
                        if "creds" not in given:
                            # the sign-in without a password (OIDC, the inventory since 23 October): no stored key text
                            # reaches azure/login, only the three IDs, and the job asks GitHub for its token
                            with self.subTest(workflow=f.name, job=name, login="oidc"):
                                self.assertTrue({"client-id", "tenant-id", "subscription-id"} <= set(given))
                                self.assertEqual((w.get("permissions") or job.get("permissions") or {}).get("id-token"), "write")
                            continue
                        seen += 1
                        prev = steps[k - 1]
                        with self.subTest(workflow=f.name, job=name):
                            self.assertIn("cloud_key_check.py azure", str(prev.get("run", "")))
                            for box in ("AZURE_CREDENTIALS", "AZURE_CLIENT_ID", "AZURE_TENANT_ID", "AZURE_SUBSCRIPTION_ID",
                                        "AZURE_CLIENT_SECRET"):
                                self.assertEqual(prev.get("env", {}).get(box), "${{ secrets.%s }}" % box)
                            # the login reads the block the check wrote, from the one box or the four
                            self.assertEqual(given.get("creds"), "${{ env.AZ_CREDS }}")
                            self.assertEqual(prev.get("if"), s.get("if"))       # skipped exactly when the login is
        self.assertGreaterEqual(seen, 9)      # the nine logins with the key (the inventory signs in without one since 23 October)


AZ_IDS = {"AZURE_CLIENT_ID": "0b1c2d3e-1111-2222-3333-444455556666", "AZURE_TENANT_ID": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
          "AZURE_SUBSCRIPTION_ID": "11111111-2222-3333-4444-555555555555"}


class AzureFourBoxes(unittest.TestCase):
    """24 October: the login typed one value to a box, as the portal shows each value, so no block is assembled by hand."""

    def test_the_whole_block_still_wins(self):
        block, where, bad = cloud_key_check.azure_login({"AZURE_CREDENTIALS": az_block()})
        self.assertEqual(bad, [])
        self.assertEqual(json.loads(block)["clientSecret"], AZ_SECRET)
        self.assertIn("whole block", where)

    def test_four_boxes_make_the_block(self):
        block, where, bad = cloud_key_check.azure_login(dict(AZ_IDS, AZURE_CLIENT_SECRET=AZ_SECRET))
        self.assertEqual(bad, [])
        self.assertEqual(json.loads(block), {"clientId": AZ_IDS["AZURE_CLIENT_ID"], "clientSecret": AZ_SECRET,
                                             "subscriptionId": AZ_IDS["AZURE_SUBSCRIPTION_ID"],
                                             "tenantId": AZ_IDS["AZURE_TENANT_ID"]})
        self.assertIn("four boxes", where)

    def test_the_password_alone_in_the_one_box_with_the_three_ids(self):
        block, where, bad = cloud_key_check.azure_login(dict(AZ_IDS, AZURE_CREDENTIALS=AZ_SECRET))
        self.assertEqual(bad, [])
        self.assertIn("AZURE_CREDENTIALS", where)

    def test_each_wrong_box_is_named_without_a_character_of_it(self):
        cases = [(dict(AZ_IDS, AZURE_CREDENTIALS=AZ_IDS["AZURE_CLIENT_ID"]), "AZURE_CLIENT_SECRET is empty"),
                 (dict(AZ_IDS, AZURE_CLIENT_SECRET="99999999-8888-7777-6666-555555555555"), "never the Secret ID"),
                 ({"AZURE_CLIENT_SECRET": AZ_SECRET}, "AZURE_CLIENT_ID is empty"),
                 (dict(AZ_IDS, AZURE_TENANT_ID="contoso", AZURE_CLIENT_SECRET=AZ_SECRET), "AZURE_TENANT_ID is not a 36-character ID"),
                 (dict(AZ_IDS, AZURE_CREDENTIALS="Ab9+" * 21 + "Xy=="), "storage account's access key")]
        for env, words in cases:
            with self.subTest(words=words):
                block, _, bad = cloud_key_check.azure_login(env)
                self.assertIsNone(block)
                said = " ".join(bad)
                self.assertIn(words, said)
                for piece in (AZ_SECRET[:10], "0b1c2d3e", "aaaaaaaa", "11111111", "99999999"):
                    self.assertNotIn(piece, said)

    def test_the_program_writes_the_masked_block_for_the_login(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "env"
            env = dict(os.environ, GITHUB_ENV=str(out), AZURE_CREDENTIALS="", AZURE_CLIENT_SECRET=AZ_SECRET, **AZ_IDS)
            run = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"], env=env,
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stdout)
            written = out.read_text()
            self.assertTrue(written.startswith("AZ_CREDS={"))
            self.assertEqual(json.loads(written.split("=", 1)[1])["clientSecret"], AZ_SECRET)
            # the only line that carries it is the mask command, which the runner swallows
            shown = [ln for ln in run.stdout.splitlines() if AZ_SECRET in ln]
            self.assertTrue(shown and all(ln.startswith("::add-mask::") for ln in shown))
            bad = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py"), "azure"],
                                 env=dict(os.environ, AZURE_CREDENTIALS="0b1c2d3e-1111-2222-3333-444455556666"),
                                 capture_output=True, text=True)
            self.assertEqual(bad.returncode, 2)
            self.assertIn("AZURE_CLIENT_SECRET", bad.stdout)
            self.assertIn("docs/AZURE_SETUP.md", bad.stdout)


class ConductorGate(unittest.TestCase):
    NOW = "2026-10-18T20:00:00Z"

    def run_(self, cloud, status, conclusion, created):
        return {"display_title": f"cloud-check {grid.CHECKS[cloud]}", "status": status, "conclusion": conclusion,
                "created_at": created, "id": 1}

    def test_the_states(self):
        g = "Azure"
        cases = [([], "check"),
                 ([self.run_(g, "in_progress", None, "2026-10-18T19:58:00Z")], "wait"),
                 ([self.run_(g, "completed", "success", "2026-10-18T19:00:00Z")], "go"),
                 ([self.run_(g, "completed", "success", "2026-10-17T19:00:00Z")], "check"),
                 ([self.run_(g, "completed", "failure", "2026-10-18T19:30:00Z")], "wait"),
                 ([self.run_(g, "completed", "failure", "2026-10-18T18:30:00Z")], "check"),
                 ([self.run_(g, "completed", "success", "2026-10-18T17:00:00Z"),
                   self.run_(g, "completed", "failure", "2026-10-18T19:30:00Z")], "wait"),     # the newest decides
                 ([{"display_title": "cloud-check all", "status": "completed", "conclusion": "success",
                    "created_at": "2026-10-18T19:00:00Z", "id": 2}], "check")]                 # another title is not read
        for runs, want in cases:
            with self.subTest(runs=runs):
                self.assertEqual(grid.check_state(runs, g, self.NOW)[0], want)

    def test_the_workflow_titles_match_the_conductor(self):
        w = yaml.safe_load((ROOT / ".github" / "workflows" / "cloud-check.yml").read_text())
        self.assertEqual(w["run-name"], "cloud-check ${{ github.event.inputs.cloud || 'azure' }}")
        self.assertEqual(set(grid.CHECKS.values()), {"azure"})
        self.assertEqual(set(w["jobs"]), set(grid.CHECKS.values()))      # one job, its title the conductor's
        self.assertEqual([c for c, _, _ in grid.CLOUDS], ["Azure"])        # Azure is the one cloud (24 October)
        text = (ROOT / ".github" / "workflows" / "cloud-check.yml").read_text()
        self.assertEqual(text.count("azure_capacity.py preflight"), 1)    # Azure's pre-flight waits for nothing and builds nothing
        self.assertNotIn("az aks create", text)
        self.assertNotIn("az group create", text)
        self.assertEqual(w["jobs"]["azure"]["if"], "contains(fromJSON('[\"azure\", \"all\"]'), (github.event.inputs.cloud || 'azure'))")

    def test_an_azure_set_waits_for_azures_check(self):
        """22 October: an Azure set that failed at the login counted as started; Azure's sets now wait for its own check."""
        calls = []

        def api(path, method="GET", data=None, tries=4):
            calls.append((method, path, data))
            return {"workflow_runs": []} if "/runs" in path else {}
        with mock.patch.object(grid, "api", side_effect=api), \
             mock.patch.object(grid, "engine", return_value=grid.ENGINE), \
             mock.patch.object(grid, "campaign_open", return_value=True), \
             mock.patch.object(grid, "grid_runs", return_value=[]), \
             mock.patch.object(grid, "next_dispatches", return_value=[]), \
             mock.patch.object(grid, "rerun_queue", return_value=[]), \
             mock.patch.object(grid, "yield_repair_coordinator", return_value=False), \
             mock.patch.object(grid, "jobs_in_flight", return_value=(0, 0, [])), \
             mock.patch.object(grid, "cloud_switch", side_effect=lambda p: "azure" in str(p)), \
             mock.patch.object(grid.time, "sleep"), \
             mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": os.devnull}):
            self.assertEqual(grid.main(["tick", "--ref", "main"]), 0)
        posts = [(p, d) for m, p, d in calls if m == "POST"]
        self.assertEqual([(p.split("/")[-2], d["inputs"]) for p, d in posts], [("cloud-check.yml", {"cloud": "azure"})])
        self.assertEqual(grid.check_state([], "Azure")[0], "check")


if __name__ == "__main__":
    unittest.main()
