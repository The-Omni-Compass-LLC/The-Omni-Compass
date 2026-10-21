// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
// oc_engine_runs INJECTION.txt RECEIPTS.txt FULL.jsonl : the Python's runs from the jump generator, the mechanism put on in C++
// (the founder's order of 21 October: the Python's runs are the input, the C++ harness puts the mechanism on, the monitor shows
// what comes out). INJECTION.txt is written by tools/engine_runs.py: every draw of every run, the Python's own numbers written
// to round-trip exactly (one decision a line: the senses the brain reads; then the compass law's draws; then the trial's samples).
// Each run goes through the C++ twins of the engine: omnicompass::Governor (sense, assimilate, the brain's RK4) and
// omnicompass::authority (the nervous system's grants to every organ), omnicompass::CompassLaw (cpp/src/compass_law.cpp) and
// omnicompass::Verdict (cpp/src/verdict.cpp), each a line-by-line twin of its Python, sealed (tools/seal.py), so every receipt is
// the Python's to the last bit (tests/test_cpp_engine_runs_parity.py). Out:
// RECEIPTS.txt, one canonical line a run exactly as tools/engine_runs.py canonical() writes it (six decimals), whose SHA-256 is
// the C++ digest; FULL.jsonl, every receipt at full precision for the run-by-run comparison.
#include "omnicompass/compass_law.hpp"
#include "omnicompass/core.hpp"
#include "omnicompass/governor.hpp"
#include "omnicompass/nervous_system.hpp"
#include "omnicompass/verdict.hpp"
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace omnicompass;

namespace {
struct Obs { double q{}, load{}, power{}, thermal{}, network{}, drift{}, stale{}, security{}; bool slo{}; };
struct Run { long k{}; unsigned long long seed{}; std::vector<Obs> obs; double tau{}, r0{}; std::vector<double> inc;
             double cost{}, tol{}, sig{}; std::vector<double> ref, extra; };
struct Receipt { long k{}; unsigned long long seed{}; State x{}; double push{}; long expand{}, contract{}; double calm{}, tau{}, meanF{}, lastF{};
                 int allowed{}; long used{}; };

double num(std::istream& in) { std::string t; if (!(in >> t)) throw std::runtime_error("the injection ended early"); return std::strtod(t.c_str(), nullptr); }
std::string word(std::istream& in) { std::string t; if (!(in >> t)) throw std::runtime_error("the injection ended early"); return t; }

std::vector<Run> read_injection(const std::string& path) {
  std::ifstream in(path); if (!in) throw std::runtime_error("cannot read " + path);
  if (word(in) != "OCRUNS" || num(in) != 1) throw std::runtime_error("not an injection of tools/engine_runs.py (OCRUNS 1)");
  const long n = static_cast<long>(num(in)), decisions = static_cast<long>(num(in)), law_steps = static_cast<long>(num(in));
  std::vector<Run> runs; runs.reserve(n);
  for (long i = 0; i < n; ++i) {
    Run r; if (word(in) != "R") throw std::runtime_error("run line expected"); r.k = static_cast<long>(num(in)); r.seed = std::strtoull(word(in).c_str(), nullptr, 10);
    for (long t = 0; t < decisions; ++t) {
      if (word(in) != "O") throw std::runtime_error("decision line expected");
      Obs o; o.q = num(in); o.load = num(in); o.power = num(in); o.thermal = num(in); o.network = num(in); o.drift = num(in); o.stale = num(in); o.security = num(in); o.slo = num(in) != 0.0;
      r.obs.push_back(o); }
    if (word(in) != "L") throw std::runtime_error("law line expected"); r.tau = num(in); r.r0 = num(in);
    for (long j = 0; j < law_steps; ++j) r.inc.push_back(num(in));
    if (word(in) != "V") throw std::runtime_error("trial line expected"); r.cost = num(in); r.tol = num(in); r.sig = num(in);
    const long nr = static_cast<long>(num(in)); for (long j = 0; j < nr; ++j) r.ref.push_back(num(in));
    const long ne = static_cast<long>(num(in)); for (long j = 0; j < ne; ++j) r.extra.push_back(num(in));
    runs.push_back(std::move(r)); }
  return runs;
}

Receipt run(const Run& r) {                     // tools/engine_runs.py run_draws(), line for line
  Receipt out; out.k = r.k; out.seed = r.seed;
  Governor g;                                   // the adapter's Governor(): the default allocation law, the brain evolving
  const double s_eq = stress_equilibrium(g.params().delta, g.params().alpha_s, g.params().beta_s);
  static const char* ORGANS[] = {"pods", "nodes", "cpufreq", "gpu", "power", "routing"};
  for (const Obs& o : r.obs) {
    const Observation ob{o.q, o.load, o.power, o.thermal, o.network, o.drift, o.stale, o.security, 0};
    const Directive d = g.step(ob, 1.0, 20);   // the Python's governor holds its cap at 1.0 and its 20 machines through these runs
    const State& x = g.state();
    NervousInputs ni;                           // omnicompass/nervous_system.from_governor
    ni.E = x.E; ni.U = x.U; ni.I_U = x.I_U; ni.S = x.S; ni.push = d.push; ni.push_release = g.law().push_release;
    ni.U_gate = g.law().U_gate; ni.s_eq = s_eq; ni.security_block = o.security; ni.slo_clean = o.slo; ni.power_stress = o.power;
    ni.thermal = o.thermal; ni.rollback = d.rollback_authorized; ni.stale = o.stale; ni.autopilot = true; ni.killed = false;
    const Authority a = authority(ni);
    out.push += d.push;                         // push += g.last_push
    for (const char* organ : ORGANS) { const Organ& og = a.organs.at(organ); out.expand += og.expand ? 1 : 0; out.contract += og.contract ? 1 : 0; }
    out.calm = a.scalars.calm; }
  out.x = g.state();
  out.tau = r.tau;
  CompassLaw law(Band{0.2, 1.0}, 1.0, r.tau);
  double rr = r.r0; std::vector<double> fs, absf;
  for (double inc : r.inc) { const double next = rr + inc; rr = 0.0 < next ? next : 0.0; fs.push_back(law.force(rr)); absf.push_back(std::fabs(fs.back())); }
  out.meanF = py_sum(absf) / static_cast<double>(fs.size()); out.lastF = fs.back();
  Verdict v(r.tol, 30, 1, 1800, 60, 1000000, false, "interval");
  v.tick(true); v.observe(r.ref); v.tick(true); v.observe(std::vector<double>(r.extra.begin(), r.extra.begin() + 30));
  long used = 30; std::string verdict;
  while (true) {
    const Tick t = v.tick(true);
    if (t.event && t.event->verdict.rfind("step", 0) == 0) { verdict = t.event->verdict; break; }
    if (used >= static_cast<long>(r.extra.size())) { verdict = "step refused: the trial ran out of samples"; break; }
    v.observe({r.extra[used]}); used += 1; }
  out.allowed = verdict == "step allowed" ? 1 : 0; out.used = used;
  return out;
}

std::string six(double v) { char b[64]; std::snprintf(b, sizeof b, "%.6f", v); std::string s(b); return s == "-0.000000" ? "0.000000" : s; }
std::string full(double v) { char b[64]; std::snprintf(b, sizeof b, "%.17g", v); return b; }
}  // namespace

int main(int argc, char** argv) {
  if (argc != 4) { std::cerr << "usage: oc_engine_runs INJECTION.txt RECEIPTS.txt FULL.jsonl\n"; return 2; }
  try {
    const std::vector<Run> runs = read_injection(argv[1]);
    std::ofstream canon(argv[2]), js(argv[3]);
    bool first = true;
    for (const Run& r : runs) {
      const Receipt c = run(r);
      const double xs[6] = {c.x.E, c.x.U, c.x.I_U, c.x.S, c.x.B, c.x.B_dot};
      if (!first) canon << "\n"; first = false;
      canon << c.k << ":" << c.seed << ":";
      for (int i = 0; i < 6; ++i) canon << (i ? "," : "") << six(xs[i]);
      canon << ":" << six(c.push) << ":" << c.expand << ":" << c.contract << ":" << six(c.calm) << ":" << six(c.tau) << ":" << six(c.meanF)
            << ":" << six(c.lastF) << ":" << c.allowed << ":" << c.used;
      js << "{\"k\":" << c.k << ",\"seed\":" << c.seed << ",\"x\":[";
      for (int i = 0; i < 6; ++i) js << (i ? "," : "") << full(xs[i]);
      js << "],\"push\":" << full(c.push) << ",\"expand\":" << c.expand << ",\"contract\":" << c.contract << ",\"calm\":" << full(c.calm)
         << ",\"tau\":" << full(c.tau) << ",\"meanF\":" << full(c.meanF) << ",\"lastF\":" << full(c.lastF) << ",\"allowed\":" << c.allowed
         << ",\"used\":" << c.used << "}\n"; }
  } catch (const std::exception& e) { std::cerr << "oc_engine_runs: " << e.what() << "\n"; return 1; }
  return 0;
}
