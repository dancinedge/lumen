---
id: H_A3
slug: recirc-cryo-undulator
title: Recirculating micro-storage + cryo many-period undulator — multi-turn radiation (×N) and a long cold undulator (narrow line) break the flux AND beam-quality walls together
domain: light-source
tier: 🜂 ABSTRACT (unverified · falsifiable prediction)
status: abstract-conjecture
unverified: true
since: 2026-06-25
scope: ⚠️ Imagination, not a finding — a coordinate for breaking H_008+H_009. No run, no verdict.
---

# H_A3 — recirculating micro-storage + cryo many-period undulator

> **🜂 ABSTRACT.** Brainstorm shortlist (`state/flux-wall-brainstorm.md`). Unverified conjecture.

## Which wall

Both at once: H_008 **flux** (multi-turn) + H_009 **linewidth** (many-period cold undulator).

## Principle

Inject each LPA bunch into a compact (~m) **micro-storage loop** so it radiates in the undulator
on many turns before its phase space decoheres — turning a single-pass shot into N passes
(average power ×N). Pair it with a **cryogenic in-vacuum undulator** of N≥100 periods: more
periods give a natural line ~1/N, and the cold high-field magnets let the period shrink, so the
radiated line stays inside the 2% in-band budget despite ~1% beam energy spread.

## Falsifiable prediction

≥ 20 useful turns **and** N ≥ 100 undulator periods → average in-band power ×30 over a single-pass
warm undulator, with Δλ/λ ≤ 1%. If decoherence caps useful turns ≪ 20 (emittance/energy-spread
growth per pass), the multiplicative-gain conjecture is falsified.

## How it would be tested

Turn-by-turn emittance/energy-spread growth model (ring optics) → useful-turn count; undulator
linewidth from N + energy spread (extends `undulator_natural_linewidth` / `energy_spread_broadening`).
A future harness run could bound it. Not run here.

## Honest status

Unverified (🜂). Storage of low-energy, high-spread LPA beams is hard (large energy spread →
fast decoherence); the ×30 product is optimistic and turn-count-limited. The ring reintroduces
some footprint (H_010 trade), though far below a full synchrotron.

## Cross-links

- breaks: H_008 + H_009 jointly. trade: partial footprint (H_010).
- builds on: H_004/H_006. source: R2-#5 × R1-#2 → R7-#2, `state/flux-wall-brainstorm.md`.
