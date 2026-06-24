#!/usr/bin/env python3
"""H_031 — fleet round-2 sharpening: TWO sourced quantitative corrections.
(A) SLICE-SPREAD WALL: the binding FEL constraint for an LPA beam is SLICE energy spread,
    not undulator length. Single-pass active cooling has never been demonstrated; what IS
    demonstrated single-pass (DESY LUX, Nature 2025: 2.13% -> 0.068%) is energy dechirping
    (a longitudinal CORRELATION rotation), which does NOT lower slice spread or 6D brightness.
    A 0.5% slice beam sits ~5x over the Ming-Xie criterion (sigma_d/rho, rho~1e-3) -> the 3D
    gain length diverges and it will NOT lase at 13.5 nm; demonstrated LPA-FEL floor ~24.8-27 nm.
(B) AMORTIZATION BREAK-EVEN: H_021 (FEL source CAPEX < LPP) holds ONLY at fan-out N >= ~2
    and comfortably (~8x) at the design N~10 ($260M/10kW KEK -> ~$26M/scanner), but INVERTS at
    N=1 ($260M > $200M LPP). The cryomodule Wright slope is shallow (~0.95) -> the economics
    come from M9 amortization, not an M7 manufacturing learning curve. TGU is the named (still
    UNVERIFIED) orthogonal escape to the slice-spread wall.

Deterministic, stdlib-only. $0 local.
"""
from __future__ import annotations
import json, os, sys
_HERE=os.path.dirname(os.path.abspath(__file__)); _ROOT=os.path.abspath(os.path.join(_HERE,"..",".."))
sys.path.insert(0, os.path.join(_ROOT,"tool"))
from lumen_optics import Falsifier, evaluate

# (A) slice-spread wall (sourced)
LPA_SLICE_SPREAD = 0.005          # 0.5% best lasing-shot slice spread
FEL_RHO = 0.001                   # Pierce parameter ~1e-3 at 13.5 nm (PRSTAB 14.040702 class)
MINGXIE_RATIO = LPA_SLICE_SPREAD / FEL_RHO   # sigma_d/rho; >~1 kills gain
DECHIRP_REDUCES_SLICE = False     # DESY LUX dechirp is correlation rotation, not slice cooling
LPA_FEL_FLOOR_NM = 24.8           # demonstrated radiation floor at 1 GeV (staged LWFA)
# (B) amortization break-even (sourced)
FEL_SOURCE_CAPEX_M = 260.0        # KEK 10 kW EUV-FEL CAPEX ($M)
LPP_PER_SCANNER_M = 200.0         # ASML EUV >$200M/scanner
DESIGN_FANOUT = 10                # one source -> ~10 scanner ports
CRYOMODULE_WRIGHT = 0.95          # shallow slope (HEP SRF components)

def main()->int:
    break_even_n = FEL_SOURCE_CAPEX_M / LPP_PER_SCANNER_M          # N where per-scanner FEL == LPP
    fel_per_scanner_design = FEL_SOURCE_CAPEX_M / DESIGN_FANOUT     # at N=10
    fel_per_scanner_n1 = FEL_SOURCE_CAPEX_M / 1
    m={"mingxie_ratio":MINGXIE_RATIO,"dechirp_reduces_slice":DECHIRP_REDUCES_SLICE,
       "lpa_fel_floor_nm":LPA_FEL_FLOOR_NM,"break_even_n":break_even_n,
       "fel_per_scanner_design":fel_per_scanner_design,"fel_per_scanner_n1":fel_per_scanner_n1,
       "cryomodule_wright":CRYOMODULE_WRIGHT}
    fs=[
     Falsifier("F-SL-1 DECHIRP-NOT-COOLING", lambda m: m["dechirp_reduces_slice"],
       "demonstrated single-pass dechirp must NOT reduce slice spread (cooling stays undemonstrated)"),
     Falsifier("F-SL-2 SLICE-WALL", lambda m: not (m["mingxie_ratio"]>=2.0),
       "0.5% slice / rho~1e-3 must exceed the Ming-Xie criterion (>=2) -> no 13.5 nm lasing"),
     Falsifier("F-SL-3 LPA-FLOOR", lambda m: not (m["lpa_fel_floor_nm"]>13.5),
       "demonstrated LPA-FEL floor must exceed 13.5 nm (the dial is bounded by slice spread)"),
     Falsifier("F-SL-4 BREAKEVEN-HOLDS", lambda m: not (m["fel_per_scanner_design"]<LPP_PER_SCANNER_M),
       "at the design fan-out the per-scanner FEL CAPEX must beat LPP (H_021 holds amortized)"),
     Falsifier("F-SL-5 BREAKEVEN-INVERTS", lambda m: not (m["fel_per_scanner_n1"]>LPP_PER_SCANNER_M),
       "at N=1 the FEL CAPEX must EXCEED LPP (H_021 inverts unamortized -> M9 is load-bearing)"),
     Falsifier("F-SL-6 WRIGHT-SHALLOW", lambda m: not (m["cryomodule_wright"]>=0.90),
       "cryomodule Wright slope must be shallow (>=0.90) -> economics from M9 amortization not M7 learning"),
    ]
    led=evaluate(m,fs); v="SUPPORTED" if led["all_pass"] else "FALSIFIED"; led["verdict"]=v
    print("H_031 slice-spread wall + amortization break-even (fleet r2)")
    print(f"  (A) Ming-Xie ratio sigma_d/rho = {MINGXIE_RATIO:.1f} (>=2 -> no 13.5nm lasing); dechirp reduces slice? {DECHIRP_REDUCES_SLICE}")
    print(f"      demonstrated LPA-FEL floor {LPA_FEL_FLOOR_NM} nm > 13.5 nm; TGU = named UNVERIFIED escape")
    print(f"  (B) break-even N* = {break_even_n:.1f}; per-scanner FEL ${fel_per_scanner_design:.0f}M @N=10 (<${LPP_PER_SCANNER_M:.0f}M LPP) but ${fel_per_scanner_n1:.0f}M @N=1 (>LPP)")
    print(f"      cryomodule Wright {CRYOMODULE_WRIGHT} (shallow) -> M9 amortization is the lever, not M7 learning")
    for r in led["falsifiers"]: print(f"  {r['name']:<26} {r['status']}")
    print(f"VERDICT: {v}  ({led['n_pass']}/{led['n_total']} falsifiers PASS)")
    json.dump(led, open(os.path.join(_HERE,"result.json"),"w"), indent=2); return 0
if __name__=="__main__": raise SystemExit(main())
