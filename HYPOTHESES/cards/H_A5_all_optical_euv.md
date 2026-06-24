---
id: H_A5
slug: all-optical-euv
title: All-optical EUV chain (HHG → plasma-mirror amplify → metasurface relay) — delete the accelerator entirely; the orthogonal accelerator-free moonshot with a clear go/no-go threshold
domain: light-source
tier: 🜂 ABSTRACT (unverified · falsifiable prediction)
status: abstract-conjecture
unverified: true
since: 2026-06-25
scope: ⚠️ Pure SF moonshot, not a finding — heterogeneous-principle coordinate. No run, no verdict.
---

# H_A5 — all-optical EUV chain

> **🜂 ABSTRACT.** Brainstorm shortlist (`state/flux-wall-brainstorm.md`). The highest-leverage,
> highest-risk heterogeneous bet — unverified conjecture.

## Which wall

Sidesteps the whole accelerator framing: no electron beam → no rep-rate/flux wall *as defined*
(H_008), no beam-quality wall (H_009), minimal footprint (H_010). New walls appear instead
(conversion efficiency, average power of the drive laser).

## Principle

A fully accelerator-free coherent EUV chain: **HHG** (high-harmonic generation) seeds coherent
EUV from an intense IR drive in a gas/solid; a **relativistic plasma-mirror** stage Doppler-upshift-
amplifies it; a near-lossless **EUV metasurface** relays it to the wafer with one element instead
of a multi-mirror column. Tabletop, coherent, minimal bounces — the opposite corner from the
storage ring.

## Falsifiable prediction

End-to-end the chain delivers **≥ 10 W in-band 13.5 nm** — the relevance threshold for HVM
candidacy (still below the 167 W floor, but ~10⁴× over today's HHG records, enough to be a serious
contender). If the conversion-efficiency product (HHG × plasma-mirror × metasurface) cannot exceed
~10⁻⁴ × drive power at plausible drive average power, the moonshot is falsified for HVM.

## How it would be tested

Cascade efficiency budget: HHG conversion × plasma-mirror conversion × metasurface transmission ×
drive average power → in-band W. Each factor has a measured record to anchor against
(reference-match opportunity). Then staged bench demos. Not run here.

## Honest status

Unverified (🜂), most speculative of the five. Today's HHG in-band EUV is ~10⁴× below 10 W; the bet
is that the cascade closes that gap. Each stage is real science in isolation; the *product* at
average power is the wall. Highest payoff (no accelerator) at highest risk.

## Cross-links

- sidesteps: H_004/H_006/H_008/H_009/H_010 (no accelerator). new wall: cascade conversion efficiency.
- source: R6-#1 × R6-#2 × R3-#10 → R7-#10, `state/flux-wall-brainstorm.md`.
