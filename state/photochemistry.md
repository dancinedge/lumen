# Photochemistry (광화학) — the recording layer

Pillar 2 of the lumen research hub. The photoresist that converts the projected
light pattern into a developable chemical pattern. This is where the optics
trade-off (high NA → shallow depth-of-focus) turns into a process-control problem.
Items marked `?` need verification before use.

## Why it gets harder with the next generation

- **Shallow depth-of-focus forces ultra-thin resist.** Higher NA shrinks DoF, so the
  resist film must be extremely thin and uniform — thickness/uniformity control
  becomes the dominant difficulty and a leading error source (per the source note,
  `euv-source-problem.md`, 15:52–16:40).
- **Fewer photons per feature.** EUV photons are energetic (~92 eV at 13.5 nm) so a
  given dose delivers fewer photons → **shot noise / stochastic defects** (missing or
  bridged features) become a hard limiter at small pitch.
- **Shorter wavelength changes the chemistry.** At ~6.5 nm photon energy rises
  further, shifting absorption and secondary-electron behavior `?`.

## Resist families (to expand)

- **CAR** (Chemically Amplified Resist) — incumbent; amplification helps dose but
  worsens stochastic blur at the smallest nodes.
- **MOR / metal-oxide resists** (e.g. Sn-oxo clusters) — higher EUV absorption,
  better resolution/stochastics; adoption growing for High-NA `?`.
- **Dry / vapor-deposited resist** — emerging alternative for thin-film uniformity `?`.

## Open questions

- Stochastic-defect floor vs dose vs resolution — the three-way trade ("RLS" tradeoff:
  Resolution / Line-edge-roughness / Sensitivity).
- Which resist chemistry tolerates the ultra-thin regime that High-NA / shorter-λ demands?
