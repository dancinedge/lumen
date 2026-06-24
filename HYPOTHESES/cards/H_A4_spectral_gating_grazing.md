---
id: H_A4
slug: spectral-gating-grazing
title: Shot-by-shot spectral gating + grazing-incidence column — recover usable in-band flux from an imperfect source AND cut optics loss; the cheapest near-term, non-exotic lever
domain: light-source
tier: 🜂 ABSTRACT (unverified · falsifiable prediction)
status: abstract-conjecture
unverified: true
since: 2026-06-25
scope: ⚠️ Imagination, not a finding — a near-term coordinate for H_008/H_009/H_002. No run, no verdict.
---

# H_A4 — shot-by-shot spectral gating + grazing-incidence column

> **🜂 ABSTRACT.** Brainstorm shortlist (`state/flux-wall-brainstorm.md`). Unverified — but the
> closest to near-term / measurable of the five.

## Which wall

H_009 **in-band fraction** (gating) + H_002 **optics loss** (grazing). A *recovery* lever, not a
new source — it maximizes the usable watts a given source already makes.

## Principle

Measure each pulse's spectrum and **gate** (veto/redirect) out-of-band shots before the wafer, so
only ≤2%-line pulses count toward dose — converts a broad/jittery source (H_009) into an effective
narrow one by selection. Route the surviving photons through a **grazing-incidence** (Wolter-type)
optical column where reflectivity → ~0.9 at shallow angle, instead of near-normal multilayers whose
reflectivity collapses at 6.5 nm (H_002). Demand-side + recovery, both non-exotic.

## Falsifiable prediction

Spectral gating + grazing column delivers **wafer-level in-band watts ≥ 5×** a fixed
normal-incidence, ungated baseline at 6.5 nm. If gating discards so many shots that net delivered
power drops below the ungated case, or grazing optics can't hold litho-grade wavefront/field, the
conjecture is falsified.

## How it would be tested

Multiplies two measurable factors: gating in-band recovery (from the H_009 line model) × grazing
vs normal-incidence column throughput (extends `mirror_chain_throughput` with angle-dependent R).
This one is genuinely runnable next — a candidate to **promote to a verified H_0xx** rather than
stay abstract. Not run here.

## Honest status

Unverified (🜂) but lowest-risk: every piece (spectrometers, grazing optics) exists. Open: gating
duty-cycle cost, and whether grazing optics meet lithographic imaging (NA, field) — grazing is
great for collection, harder for high-NA imaging.

## Cross-links

- recovers against: H_009 (line), H_002 (optics). promote-candidate to verified tier.
- source: R4-#1 × R3-#3 → R7-#4, `state/flux-wall-brainstorm.md`.
