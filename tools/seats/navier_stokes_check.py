# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. Evaluation and simulation use only; any other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE.
"""Navier-Stokes seat: every computation the seat sheet (docs/seats/NAVIER_STOKES.md) rests on, rebuilt and asserted.

It builds one admissible velocity field: smooth, periodic on the 2*pi torus, exactly divergence-free (Leray projection in
Fourier space), with swirl and axial stretching, a 4-fold rotation axis (the z-axis) and a mirror plane (z = 0). It then
computes, spectrally, the velocity gradient A, the strain S, the vorticity omega, the pressure from Delta p = -tr(A^2), its
Hessian through the Riesz transforms, and the deviatoric part H_dev, and checks:

  C1  admissible: max |div u| and max |Delta p + tr(A^2)| at rounding level
  C2  on the axis and on the mirror plane, wherever the stretching direction e3 carries the largest strain eigenvalue
      with a clear gap and the vorticity is large: xi = +-e3 and R_perp = |(I - e3 e3) H_dev e3| = 0 to rounding,
      while |H_dev| is of order ten (the pressure-rotation lemma has no lower bound: the RHO pressure branch is false)
  C3  off those sets the same quantity is of order one (the zero is the symmetry, not the field being weak)
  C4  at every aligned point: -e3.(S^2 + W^2 + Hess p).e3 = -lambda3^2 + |S|^2/3 - |omega|^2/6 - e3.H_dev.e3
      (the reduced stretching law of section 6 of the sheet)
  C5  ||grad u||^2 >= ||u||^2 for this mean-zero field on the 2*pi torus (Poincare inequality), so the energy
      E = ||u||^2/2 of the unforced flow obeys dE/dt <= -2 nu E: Omni equation (1) with alpha_E = 2 nu, as an inequality

  python3 tools/seats/navier_stokes_check.py [--n 96] [--out results/seats/navier_stokes/CHECKS.json]
Exit 0 when every check holds."""
from __future__ import annotations

import argparse, json, sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def build(n: int, width: float = 0.45, swirl: float = 6.0, stretch: float = 1.5):
    x = -np.pi + 2 * np.pi * np.arange(n) / n
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    k1 = np.fft.fftfreq(n, 1.0 / n)
    K = np.meshgrid(k1, k1, k1, indexing="ij")
    K2 = K[0] ** 2 + K[1] ** 2 + K[2] ** 2
    K2[0, 0, 0] = 1.0
    F, Fi = np.fft.fftn, (lambda a: np.real(np.fft.ifftn(a)))
    d = lambda f, i: Fi(1j * K[i] * F(f))
    G = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / width ** 2)
    u_swirl = [swirl * G * (-Y), swirl * G * X, 0 * G]                 # azimuthal, divergence-free, axisymmetric
    psi = stretch * Z * G                                             # poloidal part: curl(psi * (-y, x, 0))
    Ap = [psi * (-Y), psi * X, 0 * G]
    u_pol = [d(Ap[2], 1) - d(Ap[1], 2), d(Ap[0], 2) - d(Ap[2], 0), d(Ap[1], 0) - d(Ap[0], 1)]
    uh = [F(u_swirl[i] + u_pol[i]) for i in range(3)]
    kdu = sum(K[i] * uh[i] for i in range(3)) / K2
    uh = [uh[i] - K[i] * kdu for i in range(3)]                       # Leray projection: exactly divergence-free
    nyq = (np.abs(K[0]) == n // 2) | (np.abs(K[1]) == n // 2) | (np.abs(K[2]) == n // 2)
    uh = [np.where(nyq, 0, h) for h in uh]                            # no unpaired Nyquist modes (keeps the symmetry exact)
    for h in uh:
        h[0, 0, 0] = 0                                                # mean zero
    u = [Fi(h) for h in uh]
    A = [[Fi(1j * K[j] * uh[i]) for j in range(3)] for i in range(3)]  # A_ij = du_i/dx_j
    trA2 = sum(A[i][j] * A[j][i] for i in range(3) for j in range(3))
    ph = F(trA2) / K2
    ph[0, 0, 0] = 0                                                   # Delta p = -tr(A^2)
    H = [[Fi(-K[i] * K[j] * ph) for j in range(3)] for i in range(3)]
    return dict(x=x, u=u, A=A, H=H, trA2=trA2, K=K, uh=uh, n=n)


def point(f, idx):
    a = np.array([[f["A"][i][j][idx] for j in range(3)] for i in range(3)])
    h = np.array([[f["H"][i][j][idx] for j in range(3)] for i in range(3)])
    S, W = 0.5 * (a + a.T), 0.5 * (a - a.T)
    w = np.array([a[2, 1] - a[1, 2], a[0, 2] - a[2, 0], a[1, 0] - a[0, 1]])
    lam, V = np.linalg.eigh(S)
    e3 = V[:, 2]
    Hd = h - np.trace(h) / 3 * np.eye(3)
    v = Hd @ e3
    wn = np.linalg.norm(w)
    lhs = -e3 @ (S @ S + W @ W + h) @ e3
    rhs = -lam[2] ** 2 + np.sum(S * S) / 3 - wn ** 2 / 6 - e3 @ Hd @ e3
    return dict(lam3=float(lam[2]), gap=float(lam[2] - lam[1]), omega=float(wn),
                align=float(abs(w @ e3) / wn) if wn > 0 else 0.0,
                r_perp=float(np.linalg.norm(v - (e3 @ v) * e3)), h_dev=float(np.linalg.norm(Hd)),
                drive=float(-(e3 @ Hd @ e3)), budget_lhs=float(lhs), budget_rhs=float(rhs))


def dangerous(p):
    return p["omega"] > 1.0 and p["gap"] > 0.2 and p["align"] > 0.999 and p["lam3"] > 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=96)
    ap.add_argument("--out", default=str(ROOT / "results" / "seats" / "navier_stokes" / "CHECKS.json"))
    a = ap.parse_args(argv)
    f = build(a.n)
    n, c0, x = f["n"], f["n"] // 2, f["x"]
    div = sum(f["A"][i][i] for i in range(3))
    lap = sum(f["H"][i][i] for i in range(3))
    out, fails = {"grid": n, "checks": {}}, []

    def check(name, ok, **data):
        out["checks"][name] = {"pass": bool(ok), **data}
        print(("PASS  " if ok else "FAIL  ") + name)
        if not ok:
            fails.append(name)

    check("C1 admissible field", np.abs(div).max() < 1e-12 and np.abs(lap + f["trA2"]).max() < 1e-10,
          max_div=float(np.abs(div).max()), max_poisson_residual=float(np.abs(lap + f["trA2"]).max()))
    axis = [dict(z=float(x[k]), **point(f, (c0, c0, k))) for k in range(c0 - 6, c0 + 7)]
    plane = [dict(x=float(x[i]), y=float(x[j]), **point(f, (i, j, c0)))
             for i in range(c0 - 8, c0 + 9) for j in range(c0 - 8, c0 + 9)]
    sym = [p for p in axis + plane if dangerous(p)]
    worst = max(p["r_perp"] / p["h_dev"] for p in sym)
    check("C2 symmetry sets: dangerous alignment with R_perp = 0", len(sym) >= 50 and worst < 1e-12
          and min(p["h_dev"] for p in sym) > 5,
          dangerous_points=len(sym), max_r_perp_over_h_dev=worst, min_h_dev=min(p["h_dev"] for p in sym),
          max_lambda3=max(p["lam3"] for p in sym), max_omega=max(p["omega"] for p in sym),
          axis=[p for p in axis if dangerous(p)])
    off = [point(f, (c0 + s, c0 + 1, c0 + 1)) for s in (2, 4, 6)]
    check("C3 off the symmetry sets R_perp is of order one", min(p["r_perp"] for p in off) > 0.1,
          r_perp=[p["r_perp"] for p in off], align=[p["align"] for p in off])
    err = max(abs(p["budget_lhs"] - p["budget_rhs"]) for p in sym)
    centre = point(f, (c0, c0, c0))
    check("C4 reduced stretching law at every aligned point", err < 1e-9, max_abs_error=err,
          centre={k: centre[k] for k in ("lam3", "omega", "drive", "budget_lhs")})
    g2 = sum(np.sum(np.abs(f["K"][j] * f["uh"][i]) ** 2) for i in range(3) for j in range(3))
    u2 = sum(np.sum(np.abs(f["uh"][i]) ** 2) for i in range(3))
    check("C5 Poincare: ||grad u||^2 >= ||u||^2 (dE/dt <= -2 nu E)", g2 >= u2, ratio=float(g2 / u2))
    out["verdict"] = "PASS" if not fails else "FAIL: " + ", ".join(fails)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print(out["verdict"])
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
