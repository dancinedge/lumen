---
id: H_A2
slug: lpa-micro-sase-fel
title: Compact LPA-driven micro-SASE FEL — exponential photon gain in a short undulator multiplies photons/bunch ~100×, attacking the flux wall at its root while keeping a tabletop footprint
domain: light-source
tier: 🜂 ABSTRACT (unverified · falsifiable prediction)
status: abstract-conjecture
unverified: true
since: 2026-06-25
scope: ⚠️ Imagination, not a finding — a coordinate for breaking H_008. No run, no verdict.
---

# H_A2 — compact LPA-driven micro-SASE FEL

> **🜂 ABSTRACT.** Brainstorm shortlist (`state/flux-wall-brainstorm.md`). Unverified conjecture.

## Which wall

H_008 **flux** — at the root: photons-per-bunch, not just rep-rate.

## Principle

Inject the compact LPA beam (H_004) into a short **free-electron-laser** undulator instead of a
spontaneous one. SASE (self-amplified spontaneous emission) gives **exponential** gain along the
undulator, so photons/bunch grow ~100× over spontaneous undulator radiation (H_006) before
saturation — the same rep-rate now delivers far more in-band power, and the footprint stays
tabletop (no storage ring, unlike H_010).

## Falsifiable prediction

A compact LPA-FEL reaches SASE **saturation in ≤ 5 m** of undulator → photons/bunch ≥ 100×
spontaneous, lifting in-band average power toward the 167 W floor at ≤ 0.3× a storage-ring
footprint. If saturation needs ≫ 5 m (because LPA energy spread, H_009, suppresses gain), the
compact-FEL conjecture is falsified — which ties it to H_A-chirp ideas.

## How it would be tested

FEL gain-length (Pierce parameter) computed from LPA beam current, emittance, and energy spread →
saturation length; then start-to-end FEL simulation. The energy-spread sensitivity is the crux
(H_009). Not run here.

## Honest status

Unverified (🜂). LPA-FEL lasing has early experimental claims but is fragile to beam quality; the
≤5 m / 100× combination at HVM-relevant rep-rate is open. Beam-quality (H_009) is the main threat.

## Cross-links

- breaks: H_008 (flux). threatened by: H_009 (energy spread suppresses SASE gain).
- builds on: H_004 (beam), H_006 (undulator). source: R6-#10 / R7-#1, `state/flux-wall-brainstorm.md`.
