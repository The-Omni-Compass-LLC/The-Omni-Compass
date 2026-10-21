// SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
// Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
// Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
// Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
// All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
//
// oc_engine_runs RUNS BASE OUT.csv [START] : the engine's seeded runs of tools/engine_runs.py, run by the C++ engine.
// The same jump generator (seed_k = base + k x 0x9E3779B9 mod 2^32), the same mulberry32 stream and the same draws in the
// same order feed the C++ twins of the engine that stands: the governor's state equations integrated by RK4
// (cpp/src/governor.cpp, 288 decisions), the nervous system's authority per organ (cpp/src/nervous_system.cpp), the
// compass law (cpp/src/compass_law.cpp, 80 steps) and one give-back trial judged by the verdict (cpp/src/verdict.cpp).
// OUT holds one receipt a run at 17 significant digits, then "digest,<SHA-256>" of the receipts written as the Python
// writes them (canonical(): the counts as integers, every other number to six decimals). tests/test_cpp_engine_runs_parity.py
// and tools/engine_runs.py --cpp compare every receipt and the digest with the Python's; the live engine page shows the
// C++'s digest beside the Python's and its own.
#include "omnicompass/compass_law.hpp"
#include "omnicompass/governor.hpp"
#include "omnicompass/nervous_system.hpp"
#include "omnicompass/verdict.hpp"
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <fstream>
#include <string>
#include <vector>
using namespace omnicompass;

namespace {
constexpr int DECISIONS = 288, LAW_STEPS = 80;
const char* ORGANS[] = {"pods", "nodes", "cpufreq", "gpu", "power", "routing"};

struct Mulberry32 {                                  // the page's generator (function mulberry32), bit for bit
  uint32_t a;
  double operator()() {
    a += 0x6D2B79F5u;
    uint32_t t = (a ^ (a >> 15)) * (1u | a);
    t = (t + ((t ^ (t >> 7)) * (61u | t))) ^ t;
    return static_cast<double>(t ^ (t >> 14)) / 4294967296.0;
  }
};

uint32_t jump(uint32_t base, uint32_t k) { return base + k * 0x9E3779B9u; }

struct Draw {                                        // tools/engine_runs.py Draw: the draws in one order, from one stream
  Mulberry32 r;
  double uniform(double a, double b) { return a + (b - a) * r(); }
  template <size_t N> double choice(const std::array<double, N>& xs) { return xs[static_cast<size_t>(r() * N)]; }
  double gauss(double mu, double sigma) {
    const double u1 = r(), u2 = r();
    return mu + sigma * std::sqrt(-2.0 * std::log(1.0 - u1)) * std::cos(2.0 * M_PI * u2);
  }
};

struct Receipt {
  long k; uint32_t seed; State x; double push; long expand, contract; double calm, tau, meanF, lastF; long allowed, used;
};

Receipt one_run(long k, uint32_t base) {
  const uint32_t seed = jump(base, static_cast<uint32_t>(k));
  Draw d{Mulberry32{seed}};
  Governor g{};
  double push = 0.0, calm = 0.0; long expand = 0, contract = 0;
  const Parameters& p = g.params();
  const double s_eq = stress_equilibrium(p.delta, p.alpha_s, p.beta_s);
  for (int i = 0; i < DECISIONS; ++i) {
    double q = d.choice(std::array<double, 3>{0.0, 0.0, -1.0});    // -1 stands for the Python's None
    if (q == -1.0) q = d.uniform(0, 0.6);
    const double load = d.uniform(0.2, 1.4), power = d.uniform(0, 1.1), thermal = d.uniform(0, 1.1);
    const double network = d.uniform(0, 0.4), drift = d.uniform(0, 0.5);
    const double stale = d.choice(std::array<double, 4>{0, 0, 0, 1}), security = d.choice(std::array<double, 4>{0, 0, 0, 1});
    const bool slo_clean = d.r() < 0.8;
    const Directive dv = g.step(Observation{q, load, power, thermal, network, drift, stale, security, 0}, 1.0, 20);
    const State& x = g.state();
    NervousInputs ni;                                // omnicompass/nervous_system.from_governor
    ni.E = x.E; ni.U = x.U; ni.I_U = x.I_U; ni.S = x.S; ni.push = dv.push; ni.push_release = g.law().push_release;
    ni.U_gate = g.law().U_gate; ni.s_eq = s_eq; ni.security_block = security; ni.slo_clean = slo_clean;
    ni.power_stress = power; ni.thermal = thermal; ni.rollback = dv.rollback_authorized; ni.stale = stale;
    ni.autopilot = true; ni.killed = false;
    const Authority a = authority(ni);
    push += dv.push;
    for (const char* o : ORGANS) {
      expand += a.organs.at(o).expand ? 1 : 0;
      contract += a.organs.at(o).contract ? 1 : 0;
    }
    calm = a.scalars.calm;
  }
  const double tau = d.uniform(1, 8);
  CompassLaw law(Band{0.2, 1.0}, 1.0, tau);
  double r = d.uniform(0.2, 1.1);
  std::vector<double> fs, absf;
  for (int i = 0; i < LAW_STEPS; ++i) {
    const double next = r + d.gauss(0, 0.06);
    r = 0.0 < next ? next : 0.0;                     // max(0.0, r + gauss)
    fs.push_back(law.force(r));
    absf.push_back(std::fabs(fs.back()));
  }
  const double cost = d.choice(std::array<double, 7>{-0.04, 0, 0.01, 0.02, 0.03, 0.05, 0.08});
  const double tol = d.choice(std::array<double, 4>{0.005, 0.01, 0.02, 0.03}), sig = d.choice(std::array<double, 3>{0.1, 0.25, 0.4});
  std::vector<double> ref, extra;
  for (int i = 0; i < 30; ++i) ref.push_back(std::exp(d.gauss(0, sig)));
  for (int i = 0; i < 90; ++i) extra.push_back(std::exp(d.gauss(0, sig)) * (1 + cost));
  Verdict v(tol, 30, 1, 1800, 60, 1000000, false, "interval");
  v.tick(true); v.observe(ref); v.tick(true); v.observe(std::vector<double>(extra.begin(), extra.begin() + 30));
  long used = 30;
  std::string verdict;
  while (true) {
    const Tick t = v.tick(true);
    if (t.event && t.event->verdict.rfind("step", 0) == 0) { verdict = t.event->verdict; break; }
    if (used >= static_cast<long>(extra.size())) { verdict = "step refused: the trial ran out of samples"; break; }
    v.observe({extra[used]}); used += 1;
  }
  return Receipt{k, seed, g.state(), push, expand, contract, calm, tau, py_sum(absf) / fs.size(), fs.back(),
                 verdict == "step allowed" ? 1 : 0, used};
}

std::string six(double v) {                          // f"{v:.6f}", a negative zero written as zero
  char b[64]; std::snprintf(b, sizeof b, "%.6f", v);
  const std::string s = b;
  return s == "-0.000000" ? "0.000000" : s;
}

std::string canonical_line(const Receipt& r) {       // tools/engine_runs.py canonical(), one run
  std::string s = std::to_string(r.k) + ":" + std::to_string(r.seed) + ":";
  const double xs[] = {r.x.E, r.x.U, r.x.I_U, r.x.S, r.x.B, r.x.B_dot};
  for (int i = 0; i < 6; ++i) s += (i ? "," : "") + six(xs[i]);
  s += ":" + six(r.push) + ":" + std::to_string(r.expand) + ":" + std::to_string(r.contract) + ":" + six(r.calm) + ":" +
       six(r.tau) + ":" + six(r.meanF) + ":" + six(r.lastF) + ":" + std::to_string(r.allowed) + ":" + std::to_string(r.used);
  return s;
}

// SHA-256 (FIPS 180-4), for the digest of the receipts
struct Sha256 {
  uint32_t h[8] = {0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19};
  static uint32_t rotr(uint32_t x, int n) { return (x >> n) | (x << (32 - n)); }
  void block(const unsigned char* p) {
    static const uint32_t K[64] = {
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5, 0xd807aa98, 0x12835b01,
        0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174, 0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da, 0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147,
        0x06ca6351, 0x14292967, 0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070, 0x19a4c116, 0x1e376c08,
        0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3, 0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2};
    uint32_t w[64];
    for (int i = 0; i < 16; ++i) w[i] = uint32_t(p[4 * i]) << 24 | uint32_t(p[4 * i + 1]) << 16 | uint32_t(p[4 * i + 2]) << 8 | p[4 * i + 3];
    for (int i = 16; i < 64; ++i) {
      const uint32_t s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^ (w[i - 15] >> 3);
      const uint32_t s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^ (w[i - 2] >> 10);
      w[i] = w[i - 16] + s0 + w[i - 7] + s1;
    }
    uint32_t a = h[0], b = h[1], c = h[2], d = h[3], e = h[4], f = h[5], g = h[6], hh = h[7];
    for (int i = 0; i < 64; ++i) {
      const uint32_t t1 = hh + (rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)) + ((e & f) ^ (~e & g)) + K[i] + w[i];
      const uint32_t t2 = (rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)) + ((a & b) ^ (a & c) ^ (b & c));
      hh = g; g = f; f = e; e = d + t1; d = c; c = b; b = a; a = t1 + t2;
    }
    h[0] += a; h[1] += b; h[2] += c; h[3] += d; h[4] += e; h[5] += f; h[6] += g; h[7] += hh;
  }
  std::string hex(const std::string& msg) {
    std::string m = msg;
    const uint64_t bits = uint64_t(msg.size()) * 8;
    m += char(0x80);
    while (m.size() % 64 != 56) m += char(0);
    for (int i = 7; i >= 0; --i) m += char((bits >> (8 * i)) & 0xff);
    for (size_t i = 0; i < m.size(); i += 64) block(reinterpret_cast<const unsigned char*>(m.data() + i));
    char out[65];
    for (int i = 0; i < 8; ++i) std::snprintf(out + 8 * i, 9, "%08x", h[i]);
    return std::string(out, 64);
  }
};

std::string g17(double x) { char b[40]; std::snprintf(b, sizeof b, "%.17g", x); return b; }
}  // namespace

int main(int argc, char** argv) {
  if (argc < 4) { std::fprintf(stderr, "usage: oc_engine_runs RUNS BASE OUT.csv [START]\n"); return 2; }
  const long n = std::stol(argv[1]), start = argc > 4 ? std::stol(argv[4]) : 0;
  const uint32_t base = static_cast<uint32_t>(std::stoul(argv[2]));
  std::ofstream out(argv[3]);
  out << "k,seed,E,U,I_U,S,B,B_dot,push,expand,contract,calm,tau,meanF,lastF,allowed,used\n";
  std::string canon;
  for (long k = start; k < start + n; ++k) {
    const Receipt r = one_run(k, base);
    out << r.k << "," << r.seed << "," << g17(r.x.E) << "," << g17(r.x.U) << "," << g17(r.x.I_U) << "," << g17(r.x.S) << ","
        << g17(r.x.B) << "," << g17(r.x.B_dot) << "," << g17(r.push) << "," << r.expand << "," << r.contract << "," << g17(r.calm)
        << "," << g17(r.tau) << "," << g17(r.meanF) << "," << g17(r.lastF) << "," << r.allowed << "," << r.used << "\n";
    canon += (k > start ? "\n" : "") + canonical_line(r);
  }
  const std::string dg = Sha256{}.hex(canon);
  out << "digest," << dg << "\n";
  std::printf("%ld runs from base %u through the C++ engine: digest %s\n", n, base, dg.c_str());
  return 0;
}
