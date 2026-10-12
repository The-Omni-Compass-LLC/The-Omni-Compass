# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The grid's organism runs (tools/run_scale.py, tools/pool_scale.py): a shard cut short hands in every run it finished,
the four stacked joined from the four realms' runs on the same seed equals the four stacked run whole, and a pooled block
short of a run says so."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools import run_scale, pool_scale  # noqa: E402
from tools.run_scale import REALMS, SEED0, joined  # noqa: E402
from realms.harness import STACK  # noqa: E402

KEYS = ("primary", "work", "energy", "viol_pp", "wear", "energy_native_j", "energy_omni_j", "misses_native", "misses_omni",
        "decisions")


class RunScale(unittest.TestCase):
    def test_four_stacked_joined_equals_run_whole(self):
        cat = run_scale.CATALOGS["v5"]
        args = lambda k: (k, 1, SEED0, "v5", cat, "realms", "line")
        _, _, whole = run_scale.job(args(STACK))
        parts = [run_scale.job(args(r))[2] for r in REALMS]
        j = joined(parts)
        for q in KEYS:
            self.assertAlmostEqual(j[q], whole[q], delta=1e-9 * max(1.0, abs(whole[q])), msg=q)
        self.assertEqual(j["restore_ok"], whole["restore_ok"])
        self.assertEqual(j["sums"]["plants"], whole["sums"]["plants"])

    def test_cut_short_hands_in_what_finished(self):
        with tempfile.TemporaryDirectory() as t:
            run_scale.main(["--runs", "3", "--scale", "1", "--organisms", "3", "--out", t, "--workers", "1", "--arm", "v5",
                            "--deadline-min", "0.001"])
            d = json.loads((Path(t) / "SCALE.json").read_text())
            self.assertFalse(d["complete"])
            self.assertEqual(d["runs_done"], 1)                 # the first run always starts; none after the deadline
            self.assertEqual(d["engine"], "omni-v5")
            run = d["per_run"]["energy_facility_industrial"][str(SEED0)]
            self.assertGreater(run["wall_s"], 0.0)
            self.assertIn("sums", run)
            self.assertIn("finished before the deadline", (Path(t) / "SCALE.md").read_text())


def _run(work, viol_omni):
    """A synthetic run record with its plant sums (two plants, native work 1 each)."""
    s = {"w_sum": 2.0 * work, "w_n": 2, "e_omni": 10.0, "e_native": 10.0, "v_omni": viol_omni, "s_omni": 100.0,
         "v_native": 1.0, "s_native": 100.0, "wear_sum": 0.0, "wear_n": 0, "plants": 2}
    c = run_scale.contrast(s, True)
    c["sums"] = s
    return c


class PoolScale(unittest.TestCase):
    def test_joined_stack_and_short_block(self):
        with tempfile.TemporaryDirectory() as t:
            per = {r: {str(SEED0 + i): _run(1.0, 0.5) for i in range(10)} for r in REALMS}
            del per[REALMS[0]][str(SEED0 + 4)]                # a run missing from one realm: that seed cannot be joined
            d = {"runs": 10, "first": 0, "scale": 1, "commit": "0" * 40, "engine": "omni-v5", "arm": "v5", "load": "line",
                 "catalog": "realms/catalog_v5.csv", "stack": "realms", "complete": False, "summary": {}, "per_run": per}
            (Path(t) / "a").mkdir()
            (Path(t) / "a" / "SCALE.json").write_text(json.dumps(d))
            out = Path(t) / "SIX.md"
            pool_scale.main(str(out), str(Path(t) / "*" / "SCALE.json"))
            pooled = json.loads(out.with_suffix(".json").read_text())
            self.assertEqual(pooled["joined_stack_runs"], 9)
            ten = pooled["summary"]["10"]
            self.assertEqual((ten[STACK]["runs"], ten[STACK]["of"], ten[STACK]["joined"]), (9, 10, 9))
            self.assertEqual(ten[REALMS[0]]["runs"], 9)
            self.assertAlmostEqual(ten[STACK]["viol_pp"][0], -0.5)
            self.assertIn("9 of 10", out.read_text())

    def test_engines_never_pooled_across(self):
        with tempfile.TemporaryDirectory() as t:
            for i, eng in enumerate(("omni-v5", "omni-v3")):
                d = {"runs": 1, "scale": 1, "commit": "0" * 40, "engine": eng, "arm": "v5", "load": "line",
                     "catalog": "realms/catalog_v5.csv", "stack": "realms", "summary": {},
                     "per_run": {REALMS[0]: {str(SEED0 + i): _run(1.0, 1.0)}}}
                (Path(t) / str(i)).mkdir()
                (Path(t) / str(i) / "SCALE.json").write_text(json.dumps(d))
            with self.assertRaises(AssertionError):
                pool_scale.main(str(Path(t) / "SIX.md"), str(Path(t) / "*" / "SCALE.json"))


class Conductor(unittest.TestCase):
    """scripts/dispatch_grid.py: every square planned once to 1,000 runs, nothing started twice, every shard inside a
    runner's six hours and memory, and the started runs read back from their own names."""

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
        import dispatch_grid
        cls.g = dispatch_grid

    def test_every_square_once_to_1000(self):
        g = self.g
        plan = g.next_dispatches({}, caps={})
        seen = {}
        for d in plan:
            if d["grid"] == "six":
                k, r = ("six", d["size"], d["orgs"][0]), range(d["first"], d["first"] + d["runs"])
                keys = [k]
            else:
                r = range(d["rep_first"], d["rep_first"] + d["reps"])
                keys = [("kube", d["size"], o) for o in d["orgs"]]
            self.assertLessEqual(d["jobs"], g.MAX_JOBS)
            for k in keys:
                s = seen.setdefault(k, set())
                self.assertFalse(s & set(r), f"{k} planned twice")
                s.update(r)
        for size in g.SIZES:
            for o, k in zip(g.ORGS, g.KUBE):
                want = 0 if ("six", size, o) in g.NOT_HERE else 1000
                self.assertEqual(len(seen.get(("six", size, o), ())), want, (size, o))
                want = 0 if ("kube", size, k) in g.NOT_HERE else 1000
                self.assertEqual(len(seen.get(("kube", size, k), ())), want, (size, k))

    def test_shards_fit_a_runner(self):
        g = self.g
        for size in g.SIZES:
            for o in g.ORGS:
                sh = g.shape(size, o)
                if sh is None:
                    self.assertIn(("six", size, o), g.NOT_HERE)
                    continue
                per, w = sh
                self.assertLessEqual(w * g.MEM[size][o], g.RUNNER_GB)
                runs_per_worker = -(-per // w)
                self.assertLess(g.CAL[size][o] + runs_per_worker * g.SEC[size][o], g.DEADLINE_MIN * 60, (size, o))
        for size in g.SIZES:
            for k in g.KUBE:
                if ("kube", size, k) not in g.NOT_HERE:
                    self.assertLess(g.kube_minutes(size, k, size in g.KUBE_SPLIT), 330, (size, k))

    def test_started_runs_read_back_and_not_started_again(self):
        g = self.g
        first = g.next_dispatches({}, caps={})[:12]
        runs = [{"display_title": d["title"], "conclusion": None} for d in first]
        runs.append({"display_title": g.six_title(100, "1", 500, 50), "conclusion": "cancelled"})   # a cancelled run counts for nothing
        cov = g.coverage(runs, {"dispatches": []})
        again = {d["title"] for d in g.next_dispatches(cov, caps={})}
        for d in first:
            self.assertNotIn(d["title"], again)
        self.assertNotIn(500, cov.get(("six", 100, "1"), set()))

    def test_matrix_cuts_the_runs_asked(self):
        g = self.g
        m = g.matrix(100, ["1", "6"], 10, 90)["include"]
        for o in ("1", "6"):
            got = sorted(x for s in m if s["org"] == o for x in range(s["first"], s["first"] + s["n"]))
            self.assertEqual(got, list(range(10, 100)))
        cells = g.kube_matrix([1000], ["compute_ai_cloud"], 1, 2, [7200], True)
        self.assertEqual([(c["rep"], c["arms"]) for c in cells], [(1, "native"), (1, "compass"), (2, "native"), (2, "compass")])
        self.assertEqual(len({f"{c['rep']}{c['tag']}" for c in cells}), 4)        # one artifact name per arm


class RentedMachines(unittest.TestCase):
    """The biggest squares on rented machines: never two machines on one repetition, none past the cap before the first
    times are read back, and the budget counts every machine started."""

    @classmethod
    def setUpClass(cls):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
        import dispatch_grid
        cls.g = dispatch_grid

    def test_batches_do_not_overlap_and_respect_the_cap(self):
        g = self.g
        for cap in (10, 0):
            seen = {}
            for b in g.azure_next({}, cap=cap):
                r = set(range(b["rep_first"], b["rep_first"] + b["reps"]))
                s = seen.setdefault(b["square"], set())
                self.assertFalse(s & r)
                s.update(r)
                self.assertLessEqual(b["reps"], g.AZURE[b["square"]]["per"])
            for sq, s in seen.items():
                self.assertEqual(len(s), cap or 1000, sq)

    def test_started_machines_read_back_and_counted_in_the_budget(self):
        g = self.g
        first = g.azure_next({}, cap=10)[:3]
        runs = [{"display_title": b["title"], "conclusion": "success", "status": "completed", "created_at": "2026-10-12T09:00:00Z"}
                for b in first]
        cov, failing = g.azure_coverage(runs, {"dispatches": []})
        self.assertFalse(failing)
        self.assertAlmostEqual(g.azure_spent(cov), sum(b["usd"] for b in first), delta=0.05)
        again = {b["title"] for b in g.azure_next(cov, cap=10)}
        self.assertFalse(again & {b["title"] for b in first})


if __name__ == "__main__":
    unittest.main()
