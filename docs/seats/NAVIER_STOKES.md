# Seat sheet: Navier–Stokes existence and smoothness (seat ρ, Rho)

> **Evaluation and simulation use only.** Copyright (c) 2026 The Omni-Compass LLC. Not open source. Any commercial use,
> commercialization, monetization, production use, redistribution or hosted service requires a signed, paid
> Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark applications have been
> filed in the United States by The Omni-Compass LLC. See `LICENSE` and `NOTICE` at the root of this repository.

> `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0`. Copyright (c) 2026 The Omni-Compass LLC.

## In plain words

- **Is the problem solved here? No.** Navier–Stokes is open. Nothing on this page claims otherwise.
- **What this page is:** the exact problem, what Omni-Compass's own mathematics supplies to it, what it does not, and
  every attack tried so far with its result. Every number is recomputed by one program,
  `tools/seats/navier_stokes_check.py` (5 of 5 checks pass).
- **New result on this page:** the attack the team was working on, "the pressure turns the stretching direction away",
  is **false as a general rule**. An explicit, legal flow has the dangerous alignment with that pressure effect exactly
  zero along a whole line and a whole plane (section 7, Attack 10).
- **What Omni supplies:** the energy-loss skeleton (the flow loses energy at least as fast as Omni's equation (1) says).
  That part is real and correct, but it has been known since 1934, and it is mathematically **not enough** on its own
  (section 6).
- **What must be built outside Omni:** control of how fast the stretching can grow, which comes down to one nonlocal
  pressure number on the flow's symmetry sets (section 8). That is the live target.

## 1. The seat

| Item | Value |
|---|---|
| Seat | ρ (Rho), seat 17 of the working 24-seat map (poster label "solid state", role "fluid / Navier–Stokes") |
| Antipode | η (Eta), seat 5: seat + 12 (mod 24) |
| Proof level reached | **Level 1** (target stated). Level 2 and Level 3: not reached (section 6) |

**Source-integrity note.** The monograph's own scientific crosswalk puts fluid mechanics at Ξ and condensed matter at Ρ.
The working map used in the chats puts Navier–Stokes at Ρ. Both are kept, and neither is silently rewritten. The
mathematics below does not depend on which seat carries the label, but the founder should decide which one is official.

## 2. The problem, exactly (Clay Mathematics Institute, official statement by C. Fefferman)

The equations, in three dimensions with viscosity ν > 0, are:

```text
du/dt + (u . grad) u = nu Laplacian(u) - grad p + f        div u = 0        u(x,0) = u0(x)
```

- **Initial data:** u0 is smooth and divergence-free, and on ℝ³ every derivative decays faster than any power:
  |∂^α u0(x)| ≤ C(α,K)(1+|x|)^(−K).
- **Forcing:** where present, f obeys the same kind of decay in x and t.
- **A physically reasonable solution:** u and p smooth on ℝ³ × [0, ∞), with bounded energy, ∫|u(x,t)|² dx < C for all t.

The prize is paid for any one of four statements:

| | Statement |
|---|---|
| (A) | On ℝ³ with f = 0: every such u0 has a smooth, bounded-energy solution for all time. |
| (B) | The same on the periodic box ℝ³/ℤ³. |
| (C) | On ℝ³: some smooth u0 and f admit no such solution (breakdown). |
| (D) | The same breakdown on the periodic box. |

## 3. The standard this sheet is held to

**Proof levels (from the handoff and the monograph):**
- **Level 1:** the seat states the target.
- **Level 2:** Omni's law contains an invariant sector M and a surjective realization map R: M → (Navier–Stokes phase
  space) that preserves its constraints and observables and carries Omni's evolution onto the Navier–Stokes evolution.
- **Level 3:** Omni's law implies the target.

**Status words used below:**
- **Proven:** a published theorem.
- **Shown here:** a proof on this page, with an exact computation in `tools/seats/navier_stokes_check.py`.
- **Open:** no proof known.
- **False:** a counterexample exists.

The repository's evidence classes P, L and S (meter, live, model) are for benchmarks and do not apply. Everything here is
mathematics.

## 4. What is already known (the floor every attempt stands on)

| Result | Who | What it gives |
|---|---|---|
| Global weak solutions with the energy inequality | Leray 1934, Hopf 1951 | Solutions exist forever, but they are not known to be smooth or unique |
| Global regularity in 2D | Ladyzhenskaya and others | The 2D problem is solved: 3D is the hard case |
| Partial regularity | Caffarelli–Kohn–Nirenberg 1982 | Any singular set has one-dimensional parabolic Hausdorff measure zero |
| Blow-up criterion | Beale–Kato–Majda 1984 | Smooth as long as ∫‖ω‖∞ dt stays finite |
| Critical-space criteria | Serrin, Prodi, Ladyzhenskaya; Escauriaza–Seregin–Šverák 2003 (L³) | Smooth while u stays in a scale-invariant space |
| Vorticity-direction criterion | Constantin–Fefferman 1993; Beirão da Veiga–Berselli 2002 | Smooth if the vorticity direction is regular (Lipschitz, later ½-Hölder) where vorticity is large |
| Middle-eigenvalue criteria | Neustupa–Penel; Miller 2020 | Smooth if the positive part of the middle strain eigenvalue λ₂ is controlled |
| Alignment in turbulence | Ashurst–Kerstein–Kerr–Gibson 1987; Nomura–Post 1998 | Vorticity prefers the *middle* strain direction in real turbulence; the local (restricted Euler) dynamics push towards the stretching one, and the nonlocal pressure accounts for the difference |
| **Supercriticality barrier** | **Tao 2016** | An "averaged" Navier–Stokes with the same energy identity and harmonic-analysis bounds blows up. So **no proof can use only energy and those bounds** |
| Non-uniqueness of weak solutions | Buckmaster–Vicol 2019; Albritton–Brué–Colombo 2022 | Weak solutions alone do not settle the problem |
| Blow-up for Euler (no viscosity) | Elgindi 2021 (C^{1,α}); Chen–Hou 2022–23 (smooth data, with a boundary, computer-assisted) | Without viscosity, singularities can form, in symmetric (axisymmetric with swirl) geometry |

## 5. The attachment: what Omni supplies, line by line

The Omni objects are from the frozen engine `omnicompass/core.py` (six-state core) and from the monograph's Piece II/IV
forms as quoted in the handoff.

| Omni object | Navier–Stokes object | Relation | What it gives |
|---|---|---|---|
| Eq (1) dE/dt = −α_E E + drive | Energy ½‖u‖²: dE/dt = −ν‖∇u‖² ≤ −2νE (periodic box 2π, mean zero) | **Identical as an inequality**, with α_E = 2ν (check C5) | Energy decays. Known since Leray. |
| Piece II gradient form dX/dt = −∇Ω | The Stokes part ν∆u is the L² gradient flow of ν/2‖∇u‖² | Analogous for the viscous part only | Nothing for the nonlinearity: the transport term (u·∇)u conserves energy, and nothing in Piece II produces it |
| Eq (7), damped oscillator bath | Fourier modes of the linear Stokes flow (pure decay e^(−ν\|k\|²t), no restoring force) | Weak analogy | Nothing new |
| Eq (2), double well μU(1−U²) | None. Navier–Stokes has no bistability; its local stretching law is a Riccati λ̇ = −λ² + … without saturation | **Contrast** | Shows exactly what NS lacks: Omni's cubic saturates; NS's quadratic does not |
| Shield, clip and "curvature ceiling" | "Stays smooth" | **None.** In Omni the ceiling is imposed by construction; in NS it is the theorem to be proved | Restating the conclusion |
| Ledger / Lyapunov value | Energy (decreasing). Enstrophy ‖ω‖² is not monotone: (1/2)A′ = P − D with the stretching P | Analogous for energy only | The stretching P has no Omni counterpart |
| Eq (3) integrator, spinor drive, eq (8) audit | None | None | — |

## 6. Level 2 and why the Omni share cannot close it alone

**(a) A finite-dimensional Omni sector cannot realize Navier–Stokes (shown here).** The phase space of the Clay problem
(smooth, rapidly decaying, divergence-free fields) is an infinite-dimensional complete metrizable vector space. A finite-
dimensional manifold is σ-compact, and a continuous image of a σ-compact set is σ-compact. An infinite-dimensional
complete metrizable vector space is not σ-compact: its compact subsets have empty interior (Riesz), so by Baire it is
not a countable union of them. So **no continuous surjective realization map R exists** from Omni's state (E, U, I_U, S,
B, B_dot), or from (E, U, S, B), onto the Navier–Stokes phase space. A Level 2 realization needs Omni's role families to
be fields (infinitely many degrees of freedom), as the monograph allows, and then the Navier–Stokes nonlinearity has to
come out of Omni's law.

**(b) An unrestricted forcing term makes Level 2 empty.** The Piece IV form contains Q_adapt and Q_ext. If they may be
anything, then every evolution equation can be written in that form, and the realization says nothing. A meaningful
Level 2 has to say what Q is. For Navier–Stokes, that means producing (u·∇)u and the pressure, which is the whole
difficulty.

**(c) The parts Omni does supply are provably insufficient.** Energy decay, the viscous gradient part and a Lyapunov
energy are all properties Tao's averaged equation also has, and that equation blows up. So any proof built only from
the Omni share fails. **The missing piece must use structure specific to Navier–Stokes.**

## 7. The Rho attack ledger (from the handoff, plus this page)

| # | Attack | Result | Status |
|---|---|---|---|
| 0 | Conditional ceiling: A ≥ A* ⟹ P ≤ D | The implication is correct, but A* is the missing theorem | Fails as a proof |
| 1 | Strain-eigenframe split P = ∫λ₃\|ω\|² − Q_align | Exact and useful. Danger when ξ → e₃ | Fails to close |
| 2 | Biot–Savart / Calderón–Zygmund cancellation | Leaves the alignment remainder | Fails to close |
| 3 | Energy + enstrophy + helicity, constant weights | F′ ≤ Cν⁻³A³ + …; cubic not dominated | Fails |
| 4 | Quadratic strain | ‖S‖² = ½‖ω‖²: enstrophy in disguise | Fails |
| 5 | Cubic strain invariant tr(S³) = 3λ₁λ₂λ₃ | No dominating opposite-sign identity found | Fails (as tested; not a general theorem) |
| 6 | Critical nonlocal kernel ‖u‖²_Ḣ^½ | Critical: small data only | Fails for large data |
| 7 | Shannon entropy of normalized enstrophy | Bookkeeping identity; key estimate unproved; not BKM; invented in chat, not from the η seat | Fails |
| 8 | Antipode ρ ↔ η as an estimate | A seating rule, not an operator on velocity fields | Fails |
| 9 | Alignment dynamics D_tξ | At ξ = e₃ the inviscid kick is zero; local dynamics favour alignment | Fails to close |
| **10** | **Transverse pressure Hessian R_perp = (R₁₃² + R₂₃²)^½ needs a lower bound** | **Counterexample: R_perp = 0 exactly in the dangerous regime** | **False (shown here)** |
| **11** | **Diagonal pressure drive on symmetry sets** | Section 8 | **Open: current frontier** |

**Attack 10, shown here.**

*Theorem.* Suppose a smooth Navier–Stokes solution is invariant under a mirror reflection R (u(Rx) = R u(x)), or under
a rotation of order at least 2 about a line. Then at every point of the mirror plane, or of the axis, with unit normal
or axis direction n:
- n is an eigenvector of S;
- ω is parallel to n;
- (I − n⊗n) Hess p · n = 0.

This holds for all time while the solution stays smooth.

*Proof.*
- A = ∇u satisfies A = R A Rᵀ on the fixed set. For a mirror this flips the sign of every entry with exactly one index
  along n, so those entries vanish.
- p(Rx) = p(x) gives Hess p = R (Hess p) Rᵀ, so the same entries of Hess p vanish.
- Vorticity, a pseudovector, keeps only its component along n.
- Smooth solutions are unique, so the symmetry persists in time.
- For a rotation, the transverse block is rotated by an angle in (0, 2π) and must equal itself, so it is zero. ∎

So wherever n carries the largest strain eigenvalue, the flow is in the dangerous regime (ξ = e₃, λ₃ > 0) with R₁₃ =
R₂₃ = 0. **No lower bound on R_perp can follow from incompressibility, Biot–Savart or the Poisson equation.**

*The explicit admissible field* (check C2 in `results/seats/navier_stokes/CHECKS.json`):
- **Construction:** a swirling vortex stretched along its axis on the periodic box, made exactly divergence-free (largest
  \|div u\| = 9×10⁻¹⁶), with the Poisson equation for the pressure met to 4×10⁻¹⁴.
- **Points tested:** 70 points on the axis and the mirror plane are in the dangerous regime. λ₃ reaches 3.0 with
  eigenvalue gap up to 4.5, |ω| reaches 12, and ξ = e₃ to all printed digits.
- **On the symmetry sets:** R_perp/\|H_dev\| ≤ 1.5×10⁻¹⁵ there, while \|H_dev\| ≥ 9.3. The pressure Hessian is large;
  only its turning part is zero.
- **Off those sets:** R_perp is 2.5 to 8.0 (check C3), so the zero comes from the symmetry, not from a weak field.

**Why this matters.** The flows most often proposed as blow-up candidates are built on exactly these symmetries:
axisymmetric flow with swirl (Hou–Luo; Chen–Hou's Euler blow-up), antiparallel vortex tubes (Kerr), and Kida's
high-symmetry flow. On a symmetry set nothing can turn ξ off e₃: not pressure, not viscosity. So every "break the
alignment" argument fails there, not only the pressure one.

## 8. The frontier, and the "other stuff" to build outside Omni

On a symmetry set the direction is locked, so only the growth of λ₃ is left. For a simple top eigenvalue:
- D_tλ₃ = e₃·(D_tS)·e₃, with D_tS = −(S² + W²) − Hess p + ν∆S;
- at alignment e₃·W²·e₃ = 0;
- Δp = −tr(A²) = −(|S|² − |ω|²/2).

This gives, exactly (check C4: error 2×10⁻¹⁴ at all 70 aligned points):

```text
D_t lambda_3 = - lambda_3^2 + |S|^2/3 - |omega|^2/6  -  e3 . H_dev . e3   + nu e3 . Laplacian(S) . e3
D_t |omega|  =   lambda_3 |omega|                                          + viscous
```

The local terms brake the stretching: the isotropic pressure alone contributes −|ω|²/6, so strong vorticity throttles
its own stretching. Blow-up on a symmetry set therefore needs the single nonlocal scalar **−e₃·H_dev·e₃** to keep
beating that brake.

At the centre of the test field (check C4):

| Term | Value |
|---|---:|
| −λ₃² | −9.0 |
| Isotropic pressure | −19.5 |
| Nonlocal drive −e₃·H_dev·e₃ | +10.9 |
| **Total** | **−17.6** |

Here the nonlocal drive pushes stretching up but loses.

**Attack 11, the precise target (open).** On symmetry sets in the dangerous regime, bound

```text
- e3 . H_dev . e3   <=   theta * ( lambda_3^2 - |S|^2/3 + |omega|^2/6 ) + C,      theta < 1
```

or show it can't be bounded.

This needs an *upper* bound on a nonlocal term, the direction Calderón–Zygmund theory supplies, but only in Lᵖ, not
pointwise, and with a constant of the same size as the brake. So it is a sharp-constant, pointwise question. It is the
"other stuff": it lives in harmonic analysis of the pressure operator, not in Omni's equations. Known axisymmetric work
near the axis (Chen–Strain–Tsai–Yau; Koch–Nadirashvili–Seregin–Šverák) is the nearest literature.

## 9. Proof obligations

| ID | Obligation | Status |
|---|---|---|
| O1 | Energy inequality and global weak solutions | Proven (Leray–Hopf) |
| O2 | Omni eq (1) realizes the energy decay as an inequality, α_E = 2ν | Shown here (C5), a restatement of O1 |
| O3 | Smooth while a critical norm, or ∫‖ω‖∞, stays bounded | Proven (conditional criteria, section 4) |
| O4 | A finite-dimensional Omni sector realizes NS (Level 2) | **False** (section 6a) |
| O5 | Energy-type structure alone suffices | **False** (Tao 2016) |
| O6 | Local dynamics break the dangerous alignment | False (restricted Euler; Attack 9) |
| O7 | Pressure turning has a lower bound in the dangerous regime | **False (shown here, Attack 10)** |
| O8 | Nonlocal diagonal drive bounded by the local brake on symmetry sets | **Open: the frontier (Attack 11)** |
| O9 | Off symmetry sets: alignment broken, or stretching bounded | Open |
| O10 | Clay (A) or (B) | Open |
| O11 | Formal statement of Clay (A) in Lean 4 | Not started |

## 10. Re-running everything

```text
python3 tools/seats/navier_stokes_check.py          # 5 checks, about 4 s, writes results/seats/navier_stokes/CHECKS.json
```

The index of all seats is `docs/seats/README.md`.

---

© 2026 The Omni-Compass LLC. Evaluation and simulation use only; any commercialization or monetization requires a signed,
paid Omni-Compass Enterprise License. Patents, copyrights and trademarks filed in the USA.
