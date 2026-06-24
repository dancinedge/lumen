---
id: H_031
slug: slice-spread-and-breakeven
title: Fleet-r2 sharpening — the binding FEL constraint is SLICE energy spread (not undulator length); single-pass cooling is undemonstrated and dechirping (DESY LUX 2.13%→0.068%) is correlation rotation that does NOT lower slice spread, so a 0.5% LPA slice sits ~5× over the Ming-Xie criterion and will not lase at 13.5 nm (demonstrated floor ~24.8 nm); and H_021's FEL-CAPEX-<-LPP holds only at fan-out N≥~2 (~8× at N=10) but inverts at N=1, the cryomodule Wright slope being shallow (~0.95) so the economics are M9-amortization not M7-learning
domain: light-source
status: supported
exploration_method: fleet round-2 (accel + econ lanes, published data)
verification_method: deterministic harness + 6 pre-registered falsifiers
pre_register_frozen: true
frozen_at: 2026-06-25
deterministic: true
llm: none
sharpens: H_007/H_011 (wavelength dial), H_028 (cooling lens), H_021/H_030 (CAPEX/amortization)
---
# H_031 — slice-spread wall + amortization break-even (fleet r2)
## (A) The wavelength dial is bounded by SLICE spread, not undulator length
- Single-pass active cooling of a GeV bunch slice has **never been demonstrated** (optical-stochastic cooling is multi-turn / storage-ring only).
- What IS demonstrated single-pass — DESY LUX (Nature 2025): 2.13%→0.068% — is **energy dechirping**, a longitudinal *correlation* rotation. It does NOT lower the slice spread or the 6D brightness.
- A 0.5% slice beam is **~5× over the Ming-Xie criterion** (σ_δ/ρ, ρ~1e-3 at 13.5 nm) → the 3D gain length diverges → it will not lase at 13.5 nm. Demonstrated LPA-FEL radiation floor is **~24.8–27 nm**.
- **Named orthogonal escape (UNVERIFIED):** a transverse-gradient undulator (TGU) tolerates percent-level spread — the one route that could let a 0.5% beam lase at 13.5 nm without cooling. Not yet quantified → break-walls keeps the wall non-terminal pending the TGU check.
## (B) H_021 holds only amortized — break-even fan-out
- KEK 10 kW EUV-FEL ~$260 M → ~$26 M/scanner at the design fan-out N~10 (**~8× cheaper** than >$200 M/scanner LPP); break-even N* ≈ 1.3, so it **holds at N≥2 but inverts at N=1** ($260 M > $200 M).
- The cryomodule Wright slope is **shallow (~0.95**, ~15% over a fleet) → the economics come from **M9 amortization across scanners, not an M7 manufacturing learning curve**. Confirms the H_030 funded-form correction with a number.
## Falsifiers
F-SL-1 dechirp doesn't reduce slice (cooling undemonstrated) · F-SL-2 σ_δ/ρ≥2 (no 13.5 nm lasing) · F-SL-3 LPA floor >13.5 nm · F-SL-4 FEL<LPP at design N · F-SL-5 FEL>LPP at N=1 · F-SL-6 Wright≥0.90 shallow.
## Honest Limits
L1 ρ~1e-3 is a representative class value, not a GENESIS run for the literal spec (the TGU escape, named here, is the proper next probe); L2 break-even uses public-press CAPEX ($260 M, >$200 M) — order-level; L3 "M9 not M7" is about the *dominant* lever, both contribute.
## Verdict
```
verdict_class: SUPPORTED  (6/6)
Ming-Xie σ_δ/ρ=5.0 (no 13.5nm) · LPA floor 24.8nm · break-even N*=1.3 ($26M@N=10, $260M@N=1) · Wright 0.95
key_finding: the wavelength "dial" is bounded by SLICE spread (dechirping is not cooling; 0.5% slice
             won't lase at 13.5 nm — only a TGU, unverified, could), and the CAPEX win is real ONLY
             amortized across a fan-out (M9), since the manufacturing learning curve (M7) is shallow.
honest_note: ρ representative not GENESIS (L1); press-order CAPEX (L2); M9-dominant not M7-absent (L3).
```
**State output**: `state/h031_slice_spread_and_breakeven_2026_06_25/result.json`
