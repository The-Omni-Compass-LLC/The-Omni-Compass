# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The clouds' $0 check (Google Cloud and Amazon, 18 October; Azure, 22 October). A Google key cut short when it was copied,
and an Amazon account on the Free plan, failed every set started there at the login, each using up its A or B; for a while on
21 October the stored Azure key held a text Azure's login refuses, and Azure's own login step quoted its first characters on
the run's page. Now the key's shape is read before Google's and every Azure login (never a character of it printed), each
cloud's pre-flight names every short quota or Amazon's plan in plain words, the check stops before anything is built, and
the conductor starts a cloud's sets only after that cloud's newest check passed."""
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
SECRET = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7" * 30


def key(**over):
    k = {"type": "service_account", "project_id": "omni-compass-123456", "private_key_id": "abc123",
         "private_key": f"-----BEGIN PRIVATE KEY-----\n{SECRET}\n-----END PRIVATE KEY-----\n",
         "client_email": "omni-compass-github@omni-compass-123456.iam.gserviceaccount.com", "client_id": "1",
         "token_uri": "https://oauth2.googleapis.com/token"}
    k.update(over)
    return json.dumps(k, indent=2)


class KeyShape(unittest.TestCase):
    def test_a_whole_key_passes(self):
        self.assertEqual(cloud_key_check.problems(key(), "omni-compass-123456"), [])

    def test_a_key_cut_short_is_named_without_a_character_of_it(self):
        whole = key()
        for cut in (whole[:900], whole[:-3], whole[: len(whole) // 2]):
            bad = cloud_key_check.problems(cut)
            self.assertTrue(bad, cut[-20:])
            self.assertIn("cut", " ".join(bad))
            self.assertFalse(any(SECRET[:12] in b or "omni-compass-123456" in b for b in bad))

    def test_broken_json_missing_fields_and_another_project(self):
        self.assertIn("not whole JSON", cloud_key_check.problems(key().replace('",', '"', 1))[0])
        self.assertIn("private_key", cloud_key_check.problems(key(private_key=""))[0])
        self.assertIn("not whole", cloud_key_check.problems(key(private_key="-----BEGIN PRIVATE KEY-----\nMIIE"))[0])
        self.assertIn("GCP_PROJECT", cloud_key_check.problems(key(), "another-project")[0])
        self.assertEqual(cloud_key_check.problems(""), ["the secret is empty"])

    def test_what_a_stored_text_holds_is_named_from_its_shape(self):
        whole = key()
        cases = {whole[whole.index('"private_key_id"'):]: "piece from inside the file",
                 json.loads(whole)["private_key"]: "private key alone",
                 SECRET[:600]: "encoded string",
                 "ya29." + "a0AfB_xyZ-9q." * 45: "token",
                 "omni-compass-github@omni-compass-123456.iam.gserviceaccount.com": "account's address"}
        for raw, words in cases.items():
            with self.subTest(words=words):
                bad = cloud_key_check.problems(raw)[0]
                self.assertIn(words, bad)
                self.assertNotIn(SECRET[:12], bad)

    def test_the_program_exits_two_and_prints_no_secret(self):
        env = dict(os.environ, GCP_CREDENTIALS=key()[:1200], GCP_PROJECT="omni-compass-123456")
        out = subprocess.run(["python3", str(ROOT / "tools" / "cloud_key_check.py")], env=env, capture_output=True, text=True)
        self.assertEqual(out.returncode, 2)
        self.assertNotIn(SECRET[:12], out.stdout + out.stderr)
        self.assertIn("docs/GOOGLE_SETUP.md", out.stdout)


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
                            self.assertEqual(prev.get("env", {}).get("AZURE_CREDENTIALS"), "${{ secrets.AZURE_CREDENTIALS }}")
                            self.assertEqual(prev.get("if"), s.get("if"))       # skipped exactly when the login is
        self.assertGreaterEqual(seen, 9)      # the nine logins with the key (the inventory signs in without one since 23 October)


def fake_bin(d, name, body):
    p = Path(d) / name
    p.write_text("#!/usr/bin/env bash\n" + body)
    p.chmod(p.stat().st_mode | stat.S_IEXEC)


GCLOUD = r'''
case "$*" in
  *"services list"*) if [ -n "$OFF" ]; then echo compute.googleapis.com; else printf 'compute.googleapis.com\ncontainer.googleapis.com\n'; fi ;;
  *"services enable"*) echo "PERMISSION_DENIED: Permission denied to enable service [container.googleapis.com]" >&2; exit 1 ;;
  *"machine-types describe"*) echo 2 ;;
  *"regions describe"*) echo '{"quotas": [{"metric": "CPUS", "limit": 24, "usage": 0}, {"metric": "SSD_TOTAL_GB", "limit": '"${SSD:-500}"', "usage": 0}, {"metric": "IN_USE_ADDRESSES", "limit": 8, "usage": 0}]}' ;;
  *"project-info describe"*) echo '{"quotas": [{"metric": "CPUS_ALL_REGIONS", "limit": '"${ALL:-32}"', "usage": 0}]}' ;;
  *) echo "unexpected gcloud $*" >&2; exit 9 ;;
esac
'''
AWS = r'''
case "$*" in
  *"sts get-caller-identity"*) echo arn:aws:iam::0:user/x ;;
  *"describe-instance-types"*)
    if [ -n "$DENY" ]; then echo "An error occurred (UnauthorizedOperation) when calling the DescribeInstanceTypes operation: You are not authorized to perform this operation. User: arn:aws:iam::0:user/x is not authorized to perform: ec2:DescribeInstanceTypes with an explicit deny in a service control policy" >&2; exit 254; fi
    echo 2 ;;
  *"get-service-quota"*) echo "${QUOTA:-32}.0" ;;
  *"list-requested-service-quota-change-history-by-quota"*) echo 0 ;;
  *"request-service-quota-increase"*) echo "$*" > "$ASKED"; echo '{}' ;;
  *) echo "unexpected aws $*" >&2; exit 9 ;;
esac
'''


class PreFlight(unittest.TestCase):
    def run_script(self, script, env):
        with tempfile.TemporaryDirectory() as d:
            fake_bin(d, "gcloud", GCLOUD)
            fake_bin(d, "aws", AWS)
            for tool in ("eksctl", "kubectl", "helm"):          # the pre-flight stops before any of them is reached
                fake_bin(d, tool, f'echo "{tool} reached" >&2; exit 9\n')
            e = dict(os.environ, PATH=f"{d}:{os.environ['PATH']}", REP="1", PREFLIGHT_ONLY="1", GCP_PROJECT="p",
                     ASKED=str(Path(d) / "asked"), **env)
            out = subprocess.run(["bash", str(ROOT / "scripts" / script)], env=e, capture_output=True, text=True, cwd=d)
            asked = (Path(d) / "asked").read_text() if (Path(d) / "asked").exists() else ""
            return out.returncode, out.stdout + out.stderr, asked

    def test_google_ready_stops_after_the_preflight(self):
        code, out, _ = self.run_script("gke_paired.sh", {})
        self.assertEqual(code, 0, out)
        self.assertIn("pre-flight only: nothing built, nothing billed", out)
        self.assertNotIn("creating", out)

    def test_google_free_trial_and_short_disk_are_named(self):
        code, out, _ = self.run_script("gke_paired.sh", {"ALL": "8", "SSD": "250"})
        self.assertEqual(code, 2, out)
        self.assertIn("CPUS_ALL_REGIONS needs 10, 8 free", out)
        self.assertIn("SSD_TOTAL_GB needs 500, 250 free", out)
        self.assertIn("activate the full account", out)

    def test_google_services_already_on_are_never_asked_for(self):
        code, out, _ = self.run_script("gcp_services.sh", {})
        self.assertEqual(code, 0, out)
        self.assertIn("services are on", out)
        code, out, _ = self.run_script("gcp_services.sh", {"OFF": "1"})
        self.assertEqual(code, 2, out)
        self.assertIn("container.googleapis.com is off", out)
        self.assertIn("section 4", out)

    def test_amazon_free_plan_is_named(self):
        code, out, _ = self.run_script("eks_paired.sh", {"DENY": "1"})
        self.assertEqual(code, 2, out)
        self.assertIn("Free plan", out)
        self.assertIn("Paid plan", out)

    def test_amazon_short_quota_is_asked_of_amazon(self):
        code, out, asked = self.run_script("eks_paired.sh", {"QUOTA": "5", "QUOTA_REQUEST": "1"})
        self.assertEqual(code, 2, out)
        self.assertIn("an increase to 10 was asked of Amazon", out)
        self.assertIn("--desired-value 10", asked)

    def test_amazon_ready_stops_after_the_preflight(self):
        code, out, asked = self.run_script("eks_paired.sh", {})
        self.assertEqual(code, 0, out)
        self.assertIn("pre-flight only: nothing built, nothing billed", out)
        self.assertNotIn("reached", out)
        self.assertEqual(asked, "")


class ConductorGate(unittest.TestCase):
    NOW = "2026-10-18T20:00:00Z"

    def run_(self, cloud, status, conclusion, created):
        return {"display_title": f"cloud-check {grid.CHECKS[cloud]}", "status": status, "conclusion": conclusion,
                "created_at": created, "id": 1}

    def test_the_states(self):
        g = "Google Cloud"
        cases = [([], "check"),
                 ([self.run_(g, "in_progress", None, "2026-10-18T19:58:00Z")], "wait"),
                 ([self.run_(g, "completed", "success", "2026-10-18T19:00:00Z")], "go"),
                 ([self.run_(g, "completed", "success", "2026-10-17T19:00:00Z")], "check"),
                 ([self.run_(g, "completed", "failure", "2026-10-18T19:30:00Z")], "wait"),
                 ([self.run_(g, "completed", "failure", "2026-10-18T18:30:00Z")], "check"),
                 ([self.run_(g, "completed", "success", "2026-10-18T17:00:00Z"),
                   self.run_(g, "completed", "failure", "2026-10-18T19:30:00Z")], "wait"),     # the newest decides
                 ([self.run_("Amazon", "completed", "success", "2026-10-18T19:00:00Z")], "check")]  # another cloud's
        for runs, want in cases:
            with self.subTest(runs=runs):
                self.assertEqual(grid.check_state(runs, g, self.NOW)[0], want)

    def test_the_workflow_titles_match_the_conductor(self):
        w = yaml.safe_load((ROOT / ".github" / "workflows" / "cloud-check.yml").read_text())
        self.assertEqual(w["run-name"], "cloud-check ${{ github.event.inputs.cloud || 'both' }}")
        self.assertEqual(set(grid.CHECKS.values()), {"google", "amazon", "azure"})
        self.assertEqual(set(w["jobs"]), set(grid.CHECKS.values()))      # one job a cloud, its title the conductor's
        text = (ROOT / ".github" / "workflows" / "cloud-check.yml").read_text()
        self.assertEqual(text.count('PREFLIGHT_ONLY: "1"'), 2)          # it never builds a cluster
        self.assertEqual(text.count("azure_capacity.py preflight"), 1)    # Azure's pre-flight waits for nothing and builds nothing
        self.assertNotIn("az aks create", text)
        self.assertNotIn("az group create", text)
        for cloud, runs in (("google", ("google", "both", "all")), ("amazon", ("amazon", "both", "all")), ("azure", ("azure", "all"))):
            # a push of this file to main runs the two free checks as "both" (23 October); a hand or conductor start names its cloud
            self.assertEqual(w["jobs"][cloud]["if"], "contains(fromJSON('" + json.dumps(list(runs)) + "'), (github.event.inputs.cloud || 'both'))")
        self.assertNotIn("eksctl create", text)
        self.assertNotIn("clusters create", text)

    def test_a_set_waits_for_its_check_and_the_conductor_starts_one(self):
        calls = []

        def api(path, method="GET", data=None, tries=4):
            calls.append((method, path, data))
            if "cloud-check.yml/runs" in path:
                return {"workflow_runs": []}
            if "/runs" in path:
                return {"workflow_runs": []}
            return {}
        with mock.patch.object(grid, "api", side_effect=api), \
             mock.patch.object(grid, "engine", return_value=grid.ENGINE), \
             mock.patch.object(grid, "campaign_open", return_value=True), \
             mock.patch.object(grid, "grid_runs", return_value=[]), \
             mock.patch.object(grid, "next_dispatches", return_value=[]), \
             mock.patch.object(grid, "rerun_queue", return_value=[]), \
             mock.patch.object(grid, "yield_repair_coordinator", return_value=False), \
             mock.patch.object(grid, "jobs_in_flight", return_value=(0, 0, [])), \
             mock.patch.object(grid, "cloud_switch", side_effect=lambda p: "azure" not in str(p)), \
             mock.patch.object(grid.time, "sleep"), \
             mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": os.devnull}):
            self.assertEqual(grid.main(["tick", "--ref", "main"]), 0)
        posts = [(p, d) for m, p, d in calls if m == "POST"]
        self.assertTrue(posts)
        self.assertTrue(all("cloud-check.yml/dispatches" in p for p, _ in posts), posts)   # no set started
        self.assertEqual(sorted(d["inputs"]["cloud"] for _, d in posts), ["amazon", "google"])

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
