#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""One-command verification of the Omni-Compass package.

  python verify.py           full verification (about 15-30 minutes, single core)
  python verify.py --full-replay   additionally re-runs all held-out scenarios for every arm and requires the
                                  regenerated RUNS.csv and SUMMARY.json to equal the shipped files
  python verify.py --quick   skips the 20,000-case engine comparison, runs a 1,000,000-decision soak
                             instead of 100,000,000, and replays fewer scenarios
"""
import argparse, csv, hashlib, json, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
ok = True

def check(name, cond, detail=""):
    global ok
    print(("PASS  " if cond else "FAIL  ") + name + (f"  ({detail})" if detail else ""))
    ok = ok and bool(cond)

def all_passed():
    """Every check so far passed: the module-level record, read here so no local name in main() can stand in for it."""
    return globals()["ok"]

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def build_cpp(tmp):
    src = ROOT / "cpp"; b = tmp / "build"
    if shutil.which("cmake"):
        subprocess.run(["cmake", "-S", str(src), "-B", str(b), "-DCMAKE_BUILD_TYPE=Release"], check=True, capture_output=True)
        subprocess.run(["cmake", "--build", str(b), "-j2"], check=True, capture_output=True)
    else:
        b.mkdir(parents=True)
        cxx = shutil.which("g++") or shutil.which("clang++")
        srcs = [str(p) for p in (src / "src").glob("*.cpp")]
        for tool, name in (("run_fixture.cpp", "oc_run_fixture"), ("run_governor.cpp", "oc_governor"), ("soak.cpp", "oc_soak"),
                           ("smoke.cpp", "oc_smoke"), ("run_shield.cpp", "oc_shield"), ("run_hpa.cpp", "oc_hpa"), ("savings.cpp", "oc_savings"),
                           ("run_closure.cpp", "oc_closure"), ("run_conveyance.cpp", "oc_conveyance"), ("run_twins.cpp", "oc_twins"),
                           ("engine_runs.cpp", "oc_engine_runs")):
            subprocess.run([cxx, "-std=c++20", "-O2", "-I", str(src / "include"), *srcs, str(src / "tools" / tool), "-o", str(b / name)], check=True)
    return b

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--quick", action="store_true"); ap.add_argument("--full-replay", action="store_true")
    a = ap.parse_args()
    sys.path.insert(0, str(ROOT / "tools"))
    from code_fingerprint import fingerprint
    prov = json.loads((ROOT / "reference" / "PROVENANCE.json").read_text())
    ref = ROOT / prov["reference_engine"]
    import platform
    pyver = ".".join(platform.python_version_tuple()[:2])
    check("reference engine SHA-256", sha(ref) == prov["reference_engine_sha256"])
    reg = json.loads((ROOT / "results" / "PREREGISTRATION.json").read_text())
    amend = {a["file"]: a for a in json.loads((ROOT / "results" / "LOCK_AMENDMENTS.json").read_text())["amendments"]}

    def locked(f, h):   # unchanged, or changed exactly as a recorded amendment (bug fix) says
        cur = sha(ROOT / f)
        if cur == h:
            return True, ""
        a = amend.get(f)
        same = a is not None and h in a["from_sha256"] and cur == a["to_sha256"]
        return same, (f"amended in {a['commit']}: {a['reason'][:60]}..." if same else "")
    for f, h in reg["sha256"].items():
        same, note = locked(f, h)
        check(f"pre-registered file unchanged or amended on record (SHA-256): {f}", same, note)
    if pyver == reg.get("fingerprint_python", ""):
        check("reference engine program fingerprint", fingerprint(ref) == prov["program_fingerprint"])
        for f, h in reg["code_fingerprint"].items():
            # a file amended on record (its SHA-256 is the amendment's) carries the amended program's fingerprint there
            rec, fp = amend.get(f), fingerprint(ROOT / f)
            amended = rec is not None and sha(ROOT / f) == rec["to_sha256"] and fp == rec.get("to_fingerprint")
            check(f"program fingerprint: {f}", fp == h or amended, f"amended in {rec['commit']}" if amended and fp != h else "")
    else:
        print(f"SKIP  program fingerprints (recorded with Python {reg.get('fingerprint_python')}, running {pyver}; "
              "ast.dump output is interpreter-version dependent; SHA-256 checks above are authoritative)")
    from tests import test_stack_sim_provenance, test_native_equivalence, test_cpp_governor_parity
    test_stack_sim_provenance.main(); check("stack simulator provenance", True)
    if not a.quick:
        from tests import test_core_parity
        test_core_parity.main(); check("core parity vs reference engine and 500 fixtures", True)
    test_native_equivalence.main(20 if a.quick else 60); check("native arm equals reference simulator", True)
    tmp = Path(tempfile.mkdtemp()); b = build_cpp(tmp)
    subprocess.run([str(b / "oc_run_fixture"), str(ROOT / "fixtures" / "current_500_inputs.csv"), str(tmp / "cpp.csv")], check=True)
    r = subprocess.run([sys.executable, str(ROOT / "cpp" / "scripts" / "compare_results.py"), str(ROOT / "fixtures" / "current_500_expected.csv"),
                        str(tmp / "cpp.csv"), str(tmp / "cpp.json")], capture_output=True, text=True)
    rep = json.loads((tmp / "cpp.json").read_text())
    check("C++ core vs 500 fixtures", rep["pass"], f"max abs {rep['max_abs_error']:.2e}")
    test_cpp_governor_parity.main(str(b / "oc_governor"), 20 if a.quick else 60); check("C++ governor vs Python governor (power_protect)", True)
    test_cpp_governor_parity.main(str(b / "oc_governor"), 20 if a.quick else 60, "throughput"); check("C++ governor vs Python governor (throughput)", True)
    for m_ in ("fleet", "fleet_balanced", "fleet_wear"):
        test_cpp_governor_parity.main(str(b / "oc_governor"), 20 if a.quick else 60, m_); check(f"C++ governor vs Python governor ({m_})", True)
    from tools import engine_runs as ER   # the founder's order of 21 October: the Python's runs the input, the C++ harness the mechanism
    check("the Python's runs from the jump generator through the C++ harness (cpp/tools/engine_runs.cpp on the engine's C++ twins): every receipt to 1e-9 and the same digest",
          ER.cpp_check(20 if a.quick else 100, ER.DEFAULT_BASE, b / "oc_engine_runs") == 0)
    from tests import test_cpp_shield_parity
    test_cpp_shield_parity.main(str(b / "oc_shield"), 8 if a.quick else 20); check("C++ shield vs Python shield (enforce and violations)", True)
    from tests import test_cpp_shield_adversarial, test_shield_properties
    test_shield_properties.main(100_000 if a.quick else 1_000_000); check("shield properties: no invariant violated, idempotent, no invented action, minimal intervention (random + adversarial)", True)
    test_cpp_shield_adversarial.main(str(b / "oc_shield"), 50_000 if a.quick else 200_000); check("C++ shield vs Python shield on the adversarial generator", True)
    from tests import test_cpp_closure_parity
    test_cpp_closure_parity.main(str(b / "oc_closure"), 1 if a.quick else 3); check("C++ closure law vs Python closure law, every decision and reserve", True)
    from tests import test_cpp_conveyance_parity
    w = test_cpp_conveyance_parity.main(str(b / "oc_conveyance"), 50 if a.quick else 200)
    check("C++ conveyance law vs Python conveyance law, every allocation (random systems and the CPU+GPU layout)", w < 1e-9)
    from tests import test_cpp_twins_parity
    test_cpp_twins_parity.main(str(b / "oc_twins"), 500 if a.quick else 2000)
    check("C++ nervous system, compass and ledger, GPU rules vs Python, value for value", True)
    from tools import seal
    broken = seal.check()
    check(f"seal: all {len(seal.TWINS)} Python/C++ twins unchanged since proven equal (results/SEAL.json)", not broken, "; ".join(broken))
    from tools import mechanism_identity, tracking_bounds
    bad = mechanism_identity.check()
    check("mechanism identity: F, Theta, C, h, G, M_act, dt, A of both configurations match results/MECHANISM_IDENTITY.json", not bad, "; ".join(bad))
    tb = tracking_bounds.main()     # recomputed; a changed result also shows as a manifest mismatch below
    nt = tb["nearest_target"]
    check("tracking theorem checks (V): drift under F_bar < U_AUTHORITY, discrete ultimate bound inside the basin, no invariance failure",
          nt["drift_within_bound_all"] and nt["F_bar_below_U_AUTHORITY_all"] and nt["ultimate_bound_inside_basin"]
          and nt["invariance_failures"] == 0 and tb["wrong_target"]["invariance_failures"] == 0)
    from tools import release_manifest
    bad = release_manifest.check()
    check("release manifest: engine, C++ seal, GPU protocol, live evidence and license match RELEASE_MANIFEST.json", not bad, "; ".join(bad))
    from tools import legal
    bad = legal.check()
    check("legal notice on every page, header, workflow report and license paper: all rights reserved, all patents, copyrights "
          "and trademarks filed in the USA, www.omni-compass.com and nothing after it, no struck wording anywhere "
          "(tools/legal.py; files locked by a fingerprint keep their header until the next engine version)", not bad, "; ".join(bad[:4]))
    import re as _re
    from tools import omni_version as _ov
    _eng = _ov.version_of(_ov.engine_files())
    _pkg = _re.search(r'^version = "([^"]+)"', (ROOT / "pyproject.toml").read_text(), _re.M)
    check("the package version follows the engine on main (0.N.0 is omni-vN; tools/omni_version.py), so a changed engine "
          "cannot keep an old number", bool(_eng and _pkg and _pkg.group(1) == f"0.{_eng.split('-v')[1]}.0"),
          f"engine {_eng}, package {_pkg.group(1) if _pkg else None}")
    src = (ROOT / "cpp" / "src" / "shield.cpp").read_text()
    mut_src = tmp / "shield_mut.cpp"
    mut_src.write_text(src.replace('return k == "nodes" || k == "terraform_plan" || k == "rollout"; }', 'return k == "nodes" || k == "terraform_plan"; }'))
    others = [str(p) for p in (ROOT / "cpp" / "src").glob("*.cpp") if p.name != "shield.cpp"]
    subprocess.run([shutil.which("g++") or shutil.which("clang++"), "-std=c++20", "-O2", "-I", str(ROOT / "cpp" / "include"), *others, str(mut_src),
                    str(ROOT / "cpp" / "tools" / "run_shield.cpp"), "-o", str(tmp / "oc_shield_mut")], check=True)
    try:
        test_cpp_shield_parity.main(str(tmp / "oc_shield_mut"), 8)
        det3 = False
    except AssertionError:
        det3 = True
    check("negative control: parity test detects a C++ shield that no longer blocks rollouts during a security block", det3)
    from tests import test_cpp_hpa_parity
    test_cpp_hpa_parity.main(str(b / "oc_hpa"), (901,) if a.quick else (901, 902)); check("independent C++ HPA replica law vs fleet harness HPA", True)
    hsrc = (ROOT / "cpp" / "include" / "omnicompass" / "hpa.hpp").read_text()
    hm = tmp / "hmut" / "omnicompass"; hm.mkdir(parents=True)
    for p_ in (ROOT / "cpp" / "include" / "omnicompass").glob("*.hpp"):
        (hm / p_.name).write_text(p_.read_text())
    (hm / "hpa.hpp").write_text(hsrc.replace("tolerance{0.1}", "tolerance{0.05}"))
    subprocess.run([shutil.which("g++") or shutil.which("clang++"), "-std=c++20", "-O2", "-I", str(tmp / "hmut"), str(ROOT / "cpp" / "src" / "hpa.cpp"),
                    str(ROOT / "cpp" / "tools" / "run_hpa.cpp"), "-o", str(tmp / "oc_hpa_mut")], check=True)
    try:
        test_cpp_hpa_parity.main(str(tmp / "oc_hpa_mut"), (901,))
        det4 = False
    except AssertionError:
        det4 = True
    check("negative control: parity test detects a C++ HPA with 5% instead of 10% tolerance", det4)
    r = subprocess.run([str(b / "oc_smoke")], capture_output=True, text=True)
    check("C++ governor contract smoke test (bounds, security, determinism, both modes)", r.returncode == 0 and "SMOKE PASS" in r.stdout)
    n_soak = 1000000 if a.quick else 100000000
    rec_all = json.loads((ROOT / "results" / "SOAK.json").read_text())
    for mode in ("power_protect", "throughput"):
        soak = json.loads(subprocess.run([str(b / "oc_soak"), str(n_soak), mode], capture_output=True, text=True).stdout)
        cps = soak["rss_kb_at_25_50_75_100pct"]
        check(f"soak test ({mode}), {n_soak:,} decisions, no failures, memory flat after warm-up", soak["nonfinite_or_out_of_range"] == 0 and max(cps) == min(cps),
              f"{soak['ns_per_decision']:.0f} ns per decision, RSS checkpoints {cps} kB")
        if not a.quick:
            rec = rec_all[mode]
            same = all(soak[k] == rec[k] for k in ("decisions", "nonfinite_or_out_of_range", "E", "U", "I_U", "S", "B"))
            check(f"soak test ({mode}) reproduces results/SOAK.json (decisions, failures, state ranges)", same)
    hdr = (ROOT / "cpp" / "include" / "omnicompass" / "governor.hpp").read_text()
    mut = tmp / "mut" / "omnicompass"; mut.mkdir(parents=True)
    for src_h in (ROOT / "cpp" / "include" / "omnicompass").glob("*.hpp"):   # every header, so new modules compile too
        (mut / src_h.name).write_text(src_h.read_text())
    (mut / "governor.hpp").write_text(hdr.replace("down_dwell{4}", "down_dwell{3}"))
    cxx = shutil.which("g++") or shutil.which("clang++")
    subprocess.run([cxx, "-std=c++20", "-O2", "-I", str(tmp / "mut"), *[str(p) for p in (ROOT / "cpp" / "src").glob("*.cpp")],
                    str(ROOT / "cpp" / "tools" / "run_governor.cpp"), "-o", str(tmp / "oc_mut")], check=True)
    try:
        test_cpp_governor_parity.main(str(tmp / "oc_mut"), 20)
        detected = False
    except AssertionError:
        detected = True
    check("negative control: parity test detects a mutated C++ governor (dwell 3 instead of 4)", detected)
    (mut / "governor.hpp").write_text(hdr.replace("push_release{0.005}", "push_release{9.0}"))
    subprocess.run([cxx, "-std=c++20", "-O2", "-I", str(tmp / "mut"), *[str(p) for p in (ROOT / "cpp" / "src").glob("*.cpp")],
                    str(ROOT / "cpp" / "tools" / "run_governor.cpp"), "-o", str(tmp / "oc_mut2")], check=True)
    try:
        test_cpp_governor_parity.main(str(tmp / "oc_mut2"), 20)
        detected2 = False
    except AssertionError:
        detected2 = True
    check("negative control: parity test detects a C++ governor without the equation (2) release gate", detected2)
    (mut / "governor.hpp").write_text(hdr.replace("push_add{-9.0}", "push_add{9.0}"))
    subprocess.run([cxx, "-std=c++20", "-O2", "-I", str(tmp / "mut"), *[str(p) for p in (ROOT / "cpp" / "src").glob("*.cpp")],
                    str(ROOT / "cpp" / "tools" / "run_governor.cpp"), "-o", str(tmp / "oc_mut3")], check=True)
    try:
        test_cpp_governor_parity.main(str(tmp / "oc_mut3"), 20)
        detected3 = False
    except AssertionError:
        detected3 = True
    check("negative control: parity test detects a C++ governor with a wrong equation (2) add gate", detected3)
    from benchmarks.stack_benchmark import simulate, ARMS
    from omnicompass import stack_sim as S
    from omnicompass.adapter import AllocationLaw
    n = 5 if a.quick else 20
    for sd in reg["held_out_seeds"]:
        rows = list(csv.DictReader(open(ROOT / "results" / f"heldout_seed_{sd}" / "RUNS.csv")))
        cfg = S.ManagerBenchmarkConfig(profile="full", scenarios=500, steps=72)
        scns = S._mom_generate_scenarios(cfg, sd)[:n]; bad = 0
        for s in scns:
            for arm in ARMS:
                new = simulate(s, arm, cfg, AllocationLaw())
                old = next(r for r in rows if int(r["scenario_id"]) == s.scenario_id and r["arm"] == arm)
                bad += int(new["trace_hash"] != old["trace_hash"] or abs(new["time_healthy"] - float(old["time_healthy"])) > 1e-12)
        check(f"held-out seed {sd}: {n} scenarios x {len(ARMS)} arms replay identically", bad == 0)
        summ = json.loads((ROOT / "results" / f"heldout_seed_{sd}" / "SUMMARY.json").read_text())
        check(f"held-out seed {sd}: observe mode identical to native", summ["observe_mode_identical_to_native"] == summ["scenarios"])
        for arm in ("omni_k8s_protect", "omni_direct", "omni_direct_no_dynamics"):
            check(f"held-out seed {sd}: {arm} invariant violations I1-I5 = 0", summ["means"][arm]["invariant_violations"] == 0.0)
        check(f"held-out seed {sd}: omni_k8s_throughput invariant violations I1-I3, I5 = 0 (I4 not enforced in throughput mode)",
              summ["means"]["omni_k8s_throughput"]["invariant_violations_ex_power"] == 0.0)
        check(f"held-out seed {sd}: layered observe mode identical to Kubernetes alone",
              summ["layered_observe_identical_to_kubernetes"] == summ["scenarios"])
    freg = json.loads((ROOT / "results" / "fleet" / "PREREGISTRATION.json").read_text())
    for f, h in freg["sha256"].items():
        if f != "omnicompass/adapter.py":
            same, note = locked(f, h)
            check(f"fleet pre-registered file unchanged or amended on record (SHA-256): {f}", same, note)
    from fleet.sim import run as frun, arms_for
    from fleet.harness import make_scenario
    frows = list(csv.DictReader(open(ROOT / "results" / "fleet" / "heldout" / "RUNS.csv")))
    fsumm = json.loads((ROOT / "results" / "fleet" / "heldout" / "SUMMARY.json").read_text())
    for v in ("web", "multi", "batch", "gpu", "gpu_always_on"):
        seeds = range(freg["held_out_seed_base"], freg["held_out_seed_base"] + (2 if a.quick else 5))
        bad = 0
        for s_ in seeds:
            scn = make_scenario(v, s_)
            for arm in arms_for(v):
                new = frun(scn, arm)
                old = next(r for r in frows if r["vessel"] == v and int(r["seed"]) == s_ and r["arm"] == arm)
                bad += int(new["trace_hash"] != old["trace_hash"] or abs(float(new["energy_kwh"]) - float(old["energy_kwh"])) > 1e-9)
        check(f"fleet held-out ({v}): {len(seeds)} scenarios x {len(arms_for(v))} arms replay identically", bad == 0)
        check(f"fleet ({v}): observe mode identical to HPA 0.7 + Cluster Autoscaler",
              fsumm["vessels"][v]["observe_identical_to_hpa70_ca"] == fsumm["vessels"][v]["scenarios"])
    from fleet import planetlab as PLm
    pl_rows = list(csv.DictReader(open(ROOT / "results" / "fleet" / "planetlab" / "RUNS.csv")))
    tr = PLm.load_dir(ROOT / "fleet" / "traces" / "planetlab"); badp = 0
    for s_ in range(800000, 800000 + (1 if a.quick else 3)):
        scn = PLm.make_scenario(tr, s_)
        for arm in arms_for("web"):
            new = frun(scn, arm); old = next(r for r in pl_rows if int(r["seed"]) == s_ and r["arm"] == arm)
            badp += int(new["trace_hash"] != old["trace_hash"])
    check("recorded-trace (PlanetLab) runs replay identically", badp == 0)
    tp = json.loads((ROOT / "fleet" / "traces" / "PROVENANCE.json").read_text())
    check("recorded traces match their registered SHA-256", all(hashlib.sha256((ROOT / "fleet" / "traces" / "planetlab" / n).read_bytes()).hexdigest() == v["sha256"] for n, v in tp["files"].items()))
    from tests import test_hpa_three_way
    test_hpa_three_way.main((901,) if a.quick else (901, 902)); check("three-way HPA agreement (harness, C++, external implementation with upstream window)", True)
    import benchmarks.savings as SV
    sv_tmp = tmp / "savings"; sv_tmp.mkdir()
    SV.main(str(b / "oc_savings"), sv_tmp)
    check("C++ savi…4337 tokens truncated…s written reads as that version "
                                    "minus the runner; a changed byte or an extra engine file is no version", True)
    from tests import test_run_pgbench
    test_run_pgbench.main(); check("database runner rule: the direction follows where the time goes, calm gives back one idle server and never one in use, "
                                   "cushion, dwell, cover and fail-up to the pooler's own setting; pgbench's log reads into the gauges; the paired reading by rule", True)
    from tests import test_citylearn_abc
    test_citylearn_abc.main(); check("CityLearn A/B/C rule: a deterministic simulator's runs must reproduce; no battery means nothing to move; "
                                     "a district CityLearn cannot run is listed", True)
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", "tests.test_six_kube"], cwd=ROOT, capture_output=True, text=True)
    check("the organisms with the cluster inside: the same demand in both arms, every simulated knob handed back, an archived "
          "record stored gzipped reads the same", r.returncode == 0, r.stderr[-300:])
    from tests import test_fleet_realdata_paths
    test_fleet_realdata_paths.main(); check("capture replay and PlanetLab vessel on inputs in the real formats", True)
    r = subprocess.run(["bash", "-n", str(ROOT / "fleet" / "capture" / "kube_capture.sh")], capture_output=True)
    check("cluster capture script parses", r.returncode == 0)
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "layout_check.py")], capture_output=True, text=True)
    check("the repository is lined up: the declared root, every link and every named path present (tools/layout_check.py)",
          r.returncode == 0, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "lint_names.py")], capture_output=True, text=True)
    check("every Python file compiles and reads no name that nothing defines (tools/lint_names.py)",
          r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "levels.py"), "--check"], capture_output=True, text=True)
    check("every level on one page: docs/LEVELS.md is rebuilt from the tables it reads (tools/levels.py)",
          r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "power.py"), "--check"], capture_output=True, text=True)
    check("every judged row's minimum detectable effect: docs/POWER.md is rebuilt from the tables it reads (tools/power.py)",
          r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "deviations.py"), "--check"], capture_output=True, text=True)
    check("every change to a preregistration is in the register: docs/DEVIATIONS.md (tools/deviations.py)",
          r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "engine_coverage.py"), "--check"], capture_output=True, text=True)
    check("how much of the engine the tests run: docs/ENGINE_COVERAGE.md is what its record gives (tools/engine_coverage.py)",
          r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "sbom.py"), "--check"], capture_output=True, text=True)
    check("the bill of materials and every dependency's license are what the lock gives (tools/sbom.py; no strong copyleft)",
          r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "reproduce.py"), "--check-recipes"], capture_output=True, text=True)
    check("every table of the engine that stands has the recipe it is rebuilt from (tools/reproduce.py; reproduce.yml rebuilds "
          "them all and compares them byte for byte)", r.returncode == 0, (r.stdout.strip().splitlines() or [r.stderr[-300:]])[-1])
    # GitHub refuses a workflow file that does not parse and never runs it; it records only a failed run named after the file,
    # which no local test saw for ten pushes on 10 October 2026 (an unquoted colon in a step name). Every workflow is parsed here.
    import yaml
    bad_workflows = []
    for wf in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        try:
            doc = yaml.safe_load(wf.read_text(encoding="utf-8"))
            if not isinstance(doc, dict) or "jobs" not in doc or not ({"on", True} & set(doc)):   # YAML 1.1 reads `on` as True
                bad_workflows.append(f"{wf.name}: no on/jobs mapping")
        except Exception as e:  # noqa: BLE001  (any parse error is the finding)
            bad_workflows.append(f"{wf.name}: {str(e).splitlines()[0][:90]}")
    check("every GitHub workflow file parses as YAML with its on and jobs (a file that does not is never run by GitHub)",
          not bad_workflows, "; ".join(bad_workflows)[:300])
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", "tests.test_legal"], cwd=ROOT, capture_output=True, text=True)
    check("the legal tool (tools/legal.py): one notice under every title and at every end, older notices replaced not doubled, "
          "headers rewritten after a shebang, a workflow's own steps kept exactly while each job opens and closes its report "
          "with the notice, locked files untouched, the export bundle complete", r.returncode == 0, r.stderr[-300:])
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", "tests.test_front_page"], cwd=ROOT, capture_output=True, text=True)
    check("the front page keeps itself current (tools/front_page.py): archived runs grouped by what they are, the three newest "
          "complete runs of a kind as A, B and C, a table rebuilt only when its runs changed, the README's latest lines newest first",
          r.returncode == 0, r.stderr[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_index.py")], capture_output=True, text=True)
    check("the Omni index rebuilds from every test's own result file (tools/omni_index.py)", r.returncode == 0, r.stderr[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "wiring_verdicts.py"), "--check"], capture_output=True, text=True)
    check("the wiring verdicts (write, watch, operator's choice per knob) are in line with every table they are read from (tools/wiring_verdicts.py)",
          r.returncode == 0, (r.stdout + r.stderr)[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "benefit_sheet.py"), "--check"], capture_output=True, text=True)
    check("the benefit sheet (one number and one word per benchmark: GAIN, EVEN, LOSS or power given) is in line with every table it is read from (tools/benefit_sheet.py)",
          r.returncode == 0, (r.stdout + r.stderr)[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "readings.py"), "--check"], capture_output=True, text=True)
    check("the key to the words (GAIN, EVEN, LOSS; tools/readings.py) stands word for word at the top of the README, the reading guide "
          "and the manual's front matter", r.returncode == 0, (r.stdout + r.stderr)[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "summary.py"), "--check"], capture_output=True, text=True)
    check("the standing block of the state of play (where things stand: the engine, the muscles, the grid, the index, every benchmark's number) "
          "matches the result files it is read from (tools/summary.py --check; every push realigns)", r.returncode == 0,
          (r.stdout + r.stderr)[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "governors_page.py"), "--check"], capture_output=True, text=True)
    check("the governors and orchestrators the founder named stand on one page, every line read from its own three-run table or "
          "saying where its runs stand (results/live/GOVERNORS.md, tools/governors_page.py --check)", r.returncode == 0,
          (r.stdout + r.stderr)[-300:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "land_engine.py"), "--check"], capture_output=True, text=True)
    check("every place that names the engine that stands names the newest one (tools/land_engine.py --check: the version list, the "
          "conductor's campaign, the grid's manifest and workflows, the package, the front page, CLAUDE.md, the manual, the live "
          "engine's page; the founder's order of 18 October: version after version, nothing left behind)", r.returncode == 0,
          (r.stdout + r.stderr)[-400:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "unicode_math.py"), "--check"], capture_output=True, text=True)
    check("every formula the two manuals print is written in Unicode, never LaTeX markup (the founder's order of 15 October; "
          "tools/unicode_math.py --check)", r.returncode == 0, (r.stdout + r.stderr)[-300:])
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", "tests.test_readings", "tests.test_summary"], cwd=ROOT,
                       capture_output=True, text=True)
    check("the words rule (a reading's word set by the gauge's aim, never its sign; a resource that rose is power given, never a "
          "LOSS; old words read back) and the whole summary straight after a pull (tools/summary.py)", r.returncode == 0, r.stderr[-300:])
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", "tests.test_knob_verdict"], cwd=ROOT, capture_output=True, text=True)
    check("the brain's own verdict on a live knob (tools/knob_verdict.py around the frozen engine's Verdict): every knob starts in watch, a spend that "
          "costs more than it buys is refused, a give-back that costs nothing is allowed one step a trial, a trial holds the knob, native is always free",
          r.returncode == 0, r.stderr[-300:])
    r = subprocess.run([sys.executable, "-m", "unittest", "-q", "tests.test_run_cpu_power"], cwd=ROOT, capture_output=True, text=True)
    check("CPU power harness (tools/run_cpu_power.py) on a modelled machine: the decision rule, the grid of notches, the plug on the kernel's files "
          "(snapshot once, one writer, restore), the meter's wrap-around, the probe, the hand-back from a snapshot file, one paired run with the "
          "brain's verdict allowing notches by trial and the ceiling handed back, the three-run table flagging a modelled machine",
          r.returncode == 0, r.stderr[-300:])
    r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-q", "-s", "tests", "-t", "."], cwd=ROOT,
                       capture_output=True, text=True)
    check("the whole unit-test suite (python -m unittest discover -s tests): every test, so one failing test stops the push "
          "(17 October: tests/test_robust_restart.py had failed for two days and no check ran it)", r.returncode == 0,
          r.stderr[-400:])
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "function_tests.py")], cwd=ROOT, capture_output=True, text=True)
    check("every test file unittest never collects (plain test_* functions or a main(), not called by name above), each in its "
          "own process (tools/function_tests.py; 18 October: 61 such files had never run in this check)", r.returncode == 0,
          (r.stdout + r.stderr)[-800:])
    import benchmarks.multiplicity as MP
    mp_tmp = tmp / "mult.json"; MP.main(mp_tmp)
    check("multiplicity analysis reproduces results/MULTIPLICITY.json",
          json.loads(mp_tmp.read_text()) == json.loads((ROOT / "results" / "MULTIPLICITY.json").read_text()))
    if a.full_replay:
        from benchmarks.stack_benchmark import run as run_bench
        for sd in reg["held_out_seeds"]:
            out = tmp / f"replay_{sd}"
            run_bench(reg["held_out_scenarios_per_seed"], sd, out, AllocationLaw())
            same_runs = (out / "RUNS.csv").read_bytes() == (ROOT / "results" / f"heldout_seed_{sd}" / "RUNS.csv").read_bytes()
            new_s = json.loads((out / "SUMMARY.json").read_text()); old_s = json.loads((ROOT / "results" / f"heldout_seed_{sd}" / "SUMMARY.json").read_text())
            new_law, old_law = new_s.pop("allocation_law"), old_s.pop("allocation_law")
            inert = {"push_add": -9.0}
            law_ok = all(new_law.get(k) == v for k, v in old_law.items()) and all(k in inert and new_law[k] == inert[k] for k in set(new_law) - set(old_law))
            same_summary = new_s == old_s and law_ok
            check(f"full replay, held-out seed {sd}: all scenarios x all arms regenerate RUNS.csv exactly and SUMMARY.json exactly (recorded law may add only inert defaults)", same_runs and same_summary)
    print("\nVERIFICATION:", "PASS" if all_passed() else "FAIL")
    sys.exit(0 if all_passed() else 1)

if __name__ == "__main__":
    main()
