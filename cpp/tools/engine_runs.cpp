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
// omnicompass::authority (the nervous system's grants to every organ); the compass law and the verdict's interval rule are
// carried here as the live engine page carries them (both proven equal to the Python on these runs by the digest). Out:
// RECEIPTS.txt, one canonical line a run exactly as tools/engine_runs.py canonical() writes it (six decimals), whose SHA-256 is
// the C++ digest; FULL.jsonl, every receipt at full precision for the run-by-run comparison.
#include "omnicompass/core.hpp"
#include "omnicompass/governor.hpp"
#include "omnicompass/nervous_system.hpp"
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

double cl(double v, double lo, double hi) { return v < lo ? lo : (v > hi ? hi : v); }
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

// the compass law (omnicompass/compass_law.py, as the page carries it): a band [0.2, 1.0], center 0.5, cushion 0.05, kp 1, A 1,
// the sensed speed smoothed by 0.5, the damping from tau; the force A·tanh((kp·(p − center) + kd·v)/A), the full force at the cushion
struct Law {
  double lo{0.2}, hi{1.0}, center{0.5}, cushion{0.05}, dt{1.0}, kp{1.0}, A{1.0}, s{0.5}, kd{}, p{}, v{0.0}; bool has{false};
  explicit Law(double tau) : kd(std::max(0.0, 2.0 * std::sqrt(kp * tau / dt) - 1.0) * dt) {}
  double force(double r) {
    const double q = (r - lo) / (hi - lo);
    if (has) v = s * v + (1.0 - s) * (q - p) / dt;
    p = q; has = true;
    if (q >= 1.0 - cushion) return A;
    double f = A * std::tanh((kp * (q - center) + kd * v) / A);
    if (f < 0.0 && v > 0.0 && q > center) f = 0.0;
    return f; }
};

// the verdict's interval rule (omnicompass/verdict.py, judge "interval", as the page carries it): the change in log cost, its 95%
// interval at 1.96 standard errors, a LOSS when the interval sits above zero, measured on while it is wider than the allowance
struct Stats { double m{}, v{}; long n{}; };
Stats log_stats(const std::vector<double>& xs, long n) {
  double s = 0.0; for (long i = 0; i < n; ++i) s += std::log(xs[i]); const double m = s / n;
  double q = 0.0; for (long i = 0; i < n; ++i) { const double d = std::log(xs[i]) - m; q += d * d; }
  return {m, n > 1 ? q / (n - 1) : INFINITY, n}; }
double median(const std::vector<double>& xs, long n) {
  std::vector<double> s(xs.begin(), xs.begin() + n); std::sort(s.begin(), s.end());
  return n % 2 ? s[(n - 1) / 2] : 0.5 * (s[n / 2 - 1] + s[n / 2]); }
struct Judgement { bool loss{}, wide{}, allowed{}; };
Judgement judge(const std::vector<double>& ref, const std::vector<double>& got, long n_got, double tol) {
  const double tau = std::log(1.0 + tol);
  const Stats a = log_stats(ref, static_cast<long>(ref.size())), b = log_stats(got, n_got);
  const double d = b.m - a.m, se = std::sqrt(a.v / a.n + b.v / b.n), lo = d - 1.96 * se, hi = d + 1.96 * se;
  const bool loss = lo > 0.0, wide = (hi - lo) / 2.0 > tau, within = median(got, n_got) <= median(ref, static_cast<long>(ref.size())) * (1.0 + tol);
  return {loss, wide, !loss && within && (lo + hi) / 2.0 <= tau}; }

Receipt run(const Run& r) {
  Receipt out; out.k = r.k; out.seed = r.seed;
  Governor g;                                   // the adapter's Governor(): the default allocation law, the brain evolving
  const AllocationLaw L{};
  // the governor's parameters and clock, kept beside it to read the brain's push as the Python's governor records it
  // (g.last_push = u_push / U_AUTHORITY, u_push = clamp(−dU/dt + KP·(1 − U))), with the betas it sets from each reading
  Parameters p = {4.2, 0.0, 0.0, 1.7, 0.38, 0.705, 1.35, 1.0, -0.40, 1.55, 1.15, 1.0, 2.0, 1.0, 2.5, 0.12, 0.10, 3.782, 3.487, 4.2, 0.719, 0.0};
  double t = 0.0;
  static const char* ORGANS[] = {"pods", "nodes", "cpufreq", "gpu", "power", "routing"};
  for (const Obs& o : r.obs) {
    const Observation ob{o.q, o.load, o.power, o.thermal, o.network, o.drift, o.stale, o.security, 0};
    const Directive d = g.step(ob, 1.0, 20);   // the Python's governor holds its cap at 1.0 and its 20 machines through these runs
    const double q = cl(o.q, 0, 2), load = cl(o.load, 0, 2), pw = cl(o.power, 0, 1.5), th = cl(o.thermal, 0, 1.5), nw = cl(o.network, 0, 1.5),
                 st = cl(o.stale, 0, 1), sec = cl(o.security, 0, 1);
    p.beta_int = cl(0.58 * q + 0.42 * std::max(0.0, load - 0.75), 0, 1);
    p.beta_ext = cl(0.33 * pw + 0.27 * th + 0.20 * nw + 0.12 * st + 0.08 * sec, 0, 1);
    t += MACRO_DT;
    const State& x = g.state();
    const double u_push = std::max(-U_AUTHORITY, std::min(U_AUTHORITY, -derivatives(x, p, t, 0.0).U + KP * (1.0 - x.U)));
    const double push = u_push / U_AUTHORITY;
    out.push += push;
    NervousInputs ni; ni.E = x.E; ni.U = x.U; ni.I_U = x.I_U; ni.S = x.S; ni.push = push; ni.push_release = L.push_release; ni.U_gate = L.U_gate;
    ni.s_eq = stress_equilibrium(p.delta, p.alpha_s, p.beta_s); ni.security_block = o.security; ni.slo_clean = o.slo;
    ni.power_stress = o.power; ni.thermal = o.thermal; ni.rollback = d.rollback_authorized; ni.stale = o.stale; ni.autopilot = true; ni.killed = false;
    const Authority a = authority(ni);
    for (const char* organ : ORGANS) { const Organ& og = a.organs.at(organ); out.expand += og.expand ? 1 : 0; out.contract += og.contract ? 1 : 0; }
    out.calm = a.scalars.calm; }
  out.x = g.state();
  out.tau = r.tau;
  Law law(r.tau); double rr = r.r0, sum = 0.0, last = 0.0;
  for (double inc : r.inc) { rr = std::max(0.0, rr + inc); last = law.force(rr); sum += std::fabs(last); }
  out.meanF = sum / static_cast<double>(r.inc.size()); out.lastF = last;
  long n_got = 30; Judgement J = judge(r.ref, r.extra, n_got, r.tol);
  while (!J.loss && J.wide && n_got < static_cast<long>(r.extra.size())) { ++n_got; J = judge(r.ref, r.extra, n_got, r.tol); }
  out.allowed = J.allowed ? 1 : 0; out.used = n_got;
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
