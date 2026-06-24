# Changelog

All notable changes to lumen are recorded here (append-only).

## Unreleased

- Define direction: lumen targets the next-generation semiconductor-lithography
  light-source problem (EUV 13.5 nm first; the sub-13.5 nm / 6.5 nm stable-source gap
  is the central target). Filled ARCHITECTURE.json overview (scope + core dilemma:
  roadmap gap, NA-vs-DoF, shorter-wavelength source) and components (three reference
  fields: light-source, photochemistry, optics). Added first state artifact
  `state/euv-source-problem.md` (sourced reference note).


- Scaffold the `lumen` project: standard `src/` + `state/` layout, with the architecture SSOT as
  `ARCHITECTURE.json` (JSON `children` tree) + `architecture.html` viewer + `serve.py`, plus
  CHANGELOG/CLAUDE docs. Scope framed as the general "engineer a light source nature does not
  stably provide" problem, with EUV (13.5 nm) as the first instance.
